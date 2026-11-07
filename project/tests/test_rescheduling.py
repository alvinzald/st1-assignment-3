from datetime import datetime, timezone
from typing import cast

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import (
    Appointment,
    AppointmentStatus,
)
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def make_services():
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    service = AppointmentService(store)

    patients.register_patient('P1', 'Alex')
    patients.register_patient('P2', 'Blair')
    practitioners.register_practitioner('D1', 'Taylor', 'General')
    practitioners.register_practitioner('D2', 'Jordan', 'Dental')

    return store, service


def appointment_snapshot(store):
    return [
        (
            appointment,
            appointment.appointment_id,
            appointment.patient,
            appointment.practitioner,
            appointment.date_time,
            appointment.status,
        )
        for appointment in store.list_appointments()
    ]


def test_reschedule_preserves_identity_and_updates_session_views():
    store, service = make_services()
    earlier = service.book_appointment(
        'A1', 'P1', 'D1', datetime(2026, 10, 1, 9, 0)
    )
    target = service.book_appointment(
        'A2', 'P2', 'D1', datetime(2026, 10, 1, 10, 0)
    )
    later = service.book_appointment(
        'A3', 'P1', 'D1', datetime(2026, 10, 1, 11, 0)
    )
    new_time = datetime(2026, 10, 1, 12, 0)

    result = service.reschedule_appointment('A2', new_time)

    assert result is target
    assert target.appointment_id == 'A2'
    assert target.patient is store.find_patient('P2')
    assert target.practitioner is store.find_practitioner('D1')
    assert target.date_time == new_time
    assert target.status is AppointmentStatus.SCHEDULED
    assert service.find_appointment('A2') is target
    assert service.list_practitioner_appointments('D1') == [
        earlier,
        later,
        target,
    ]

    reused_slot = service.book_appointment(
        'A4', 'P1', 'D1', datetime(2026, 10, 1, 10, 0)
    )
    assert reused_slot.status is AppointmentStatus.SCHEDULED
    assert service.find_appointment('A2') is target
    assert len(store.list_appointments()) == 4


def test_reschedule_allows_same_time_no_op():
    _, service = make_services()
    original_time = datetime(2026, 10, 1, 9, 0)
    target = service.book_appointment('A1', 'P1', 'D1', original_time)

    result = service.reschedule_appointment('A1', original_time)

    assert result is target
    assert target.date_time == original_time
    assert target.status is AppointmentStatus.SCHEDULED


def test_reschedule_methods_accept_new_date_time_keyword():
    store, service = make_services()
    initial_time = datetime(2026, 10, 1, 9, 0)
    target = service.book_appointment('A1', 'P1', 'D1', initial_time)
    service_time = datetime(2026, 10, 1, 10, 0)
    domain_time = datetime(2026, 10, 1, 11, 0)

    assert service.reschedule_appointment(
        'A1', new_date_time=service_time
    ) is target
    assert target.date_time == service_time

    target.reschedule(new_date_time=domain_time)
    assert target.date_time == domain_time
    assert service.find_appointment('A1') is target
    assert store.list_appointments() == [target]


def test_reschedule_rejects_unknown_and_invalid_ids_without_mutation():
    store, service = make_services()
    target = service.book_appointment(
        'A1', 'P1', 'D1', datetime(2026, 10, 1, 9, 0)
    )
    before = appointment_snapshot(store)

    with pytest.raises(LookupError):
        service.reschedule_appointment(
            'A9', datetime(2026, 10, 1, 10, 0)
        )

    for invalid_id in ('', '   ', 123):
        with pytest.raises(ValueError):
            service.reschedule_appointment(
                cast(str, invalid_id), datetime(2026, 10, 1, 10, 0)
            )

    assert appointment_snapshot(store) == before
    assert service.find_appointment('A1') is target


@pytest.mark.parametrize(
    'invalid_time',
    [
        None,
        '2026-10-01 10:00',
        datetime(2026, 10, 1, 10, 0, tzinfo=timezone.utc),
        datetime(2026, 10, 1, 10, 0, 1),
        datetime(2026, 10, 1, 10, 0, 0, 1),
    ],
)
def test_invalid_reschedule_time_does_not_mutate_state(invalid_time):
    store, service = make_services()
    target = service.book_appointment(
        'A1', 'P1', 'D1', datetime(2026, 10, 1, 9, 0)
    )
    before = appointment_snapshot(store)

    with pytest.raises(ValueError):
        service.reschedule_appointment('A1', cast(datetime, invalid_time))

    assert appointment_snapshot(store) == before
    assert service.find_appointment('A1') is target

    with pytest.raises(ValueError):
        target.reschedule(cast(datetime, invalid_time))
    assert appointment_snapshot(store) == before


def test_reschedule_rejects_scheduled_practitioner_conflict_without_mutation():
    store, service = make_services()
    target = service.book_appointment(
        'A1', 'P1', 'D1', datetime(2026, 10, 1, 9, 0)
    )
    blocker = service.book_appointment(
        'A2', 'P2', 'D1', datetime(2026, 10, 1, 10, 0)
    )
    before = appointment_snapshot(store)

    with pytest.raises(ValueError, match='SCHEDULED appointment'):
        service.reschedule_appointment(
            'A1', datetime(2026, 10, 1, 10, 0)
        )

    assert appointment_snapshot(store) == before
    assert service.find_appointment('A1') is target
    assert service.find_appointment('A2') is blocker


def test_reschedule_allows_other_practitioner_and_inactive_slot_occupants():
    store, service = make_services()
    target = service.book_appointment(
        'A1', 'P1', 'D1', datetime(2026, 10, 1, 9, 0)
    )
    new_time = datetime(2026, 10, 1, 10, 0)
    other_practitioner = service.book_appointment(
        'A2', 'P2', 'D2', new_time
    )
    patient_service = PatientService(store)
    practitioner_service = PractitionerService(store)
    cancelled = Appointment(
        'A3',
        patient_service.find_patient('P2'),
        practitioner_service.find_practitioner('D1'),
        new_time,
        AppointmentStatus.CANCELLED,
    )
    completed = Appointment(
        'A4',
        patient_service.find_patient('P1'),
        practitioner_service.find_practitioner('D1'),
        new_time,
        AppointmentStatus.COMPLETED,
    )
    store.add_appointment(cancelled)
    store.add_appointment(completed)

    result = service.reschedule_appointment('A1', new_time)

    assert result is target
    assert target.date_time == new_time
    assert other_practitioner.date_time == new_time
    assert target.status is AppointmentStatus.SCHEDULED
    assert service.find_appointment('A3') is cancelled
    assert service.find_appointment('A4') is completed


@pytest.mark.parametrize(
    'status',
    [AppointmentStatus.CANCELLED, AppointmentStatus.COMPLETED],
)
def test_non_scheduled_appointment_cannot_be_rescheduled(status):
    store, service = make_services()
    patient_service = PatientService(store)
    practitioner_service = PractitionerService(store)
    original_time = datetime(2026, 10, 1, 9, 0)
    target = Appointment(
        'A1',
        patient_service.find_patient('P1'),
        practitioner_service.find_practitioner('D1'),
        original_time,
        status,
    )
    store.add_appointment(target)
    before = appointment_snapshot(store)

    with pytest.raises(ValueError, match='Only SCHEDULED'):
        service.reschedule_appointment(
            'A1', datetime(2026, 10, 1, 10, 0)
        )

    assert appointment_snapshot(store) == before
    with pytest.raises(ValueError, match='Only SCHEDULED'):
        target.reschedule(datetime(2026, 10, 1, 10, 0))
    assert appointment_snapshot(store) == before

    with pytest.raises(ValueError, match='Only SCHEDULED'):
        service.reschedule_appointment('A1', original_time)
    assert appointment_snapshot(store) == before
    with pytest.raises(ValueError, match='Only SCHEDULED'):
        target.reschedule(original_time)
    assert appointment_snapshot(store) == before
