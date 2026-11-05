from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)
from smartcare.queries import (
    appointment_sort_key,
    select_appointments,
)
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)

def make_appointments():
    patient = Patient('P1', 'Alex')
    dr1 = Practitioner('DR1', 'Taylor', 'General')
    dr2 = Practitioner('DR2', 'Jordan', 'Dental')

    time1 = datetime(2026, 10, 1, 9, 0)
    time2 = datetime(2026, 10, 1, 10, 0)

    a3 = Appointment('A3', patient, dr1, time2)
    a2 = Appointment('A2', patient, dr2, time1)
    a1 = Appointment(
        'A1', patient, dr1, time1, AppointmentStatus.CANCELLED
    )
    a4 = Appointment(
        'A4', patient, dr1, time1, AppointmentStatus.COMPLETED
    )

    return [a3, a2, a4, a1]


def test_qry_01_selects_only_requested_practitioner():
    appointments = make_appointments()

    result = select_appointments(appointments, 'DR1')

    assert [a.appointment_id for a in result] == ['A1', 'A4', 'A3']
    assert all(a.practitioner.practitioner_id == 'DR1' for a in result)


def test_qry_02_filters_by_status():
    appointments = make_appointments()

    all_statuses = select_appointments(appointments, 'DR1')
    scheduled = select_appointments(
        appointments, 'DR1', AppointmentStatus.SCHEDULED
    )
    cancelled = select_appointments(
        appointments, 'DR1', AppointmentStatus.CANCELLED
    )
    completed = select_appointments(
        appointments, 'DR1', AppointmentStatus.COMPLETED
    )

    assert len(all_statuses) == 3
    assert [a.appointment_id for a in scheduled] == ['A3']
    assert [a.appointment_id for a in cancelled] == ['A1']
    assert [a.appointment_id for a in completed] == ['A4']


def test_qry_03_sorts_by_datetime_then_id():
    appointments = make_appointments()
    original = list(appointments)

    result = select_appointments(appointments, 'DR1')

    assert [a.appointment_id for a in result] == ['A1', 'A4', 'A3']
    assert appointments == original


def test_fp_03_named_sorting_key():
    appointments = make_appointments()
    appointment = appointments[0]

    assert appointment_sort_key(appointment) == (
        appointment.date_time,
        appointment.appointment_id,
    )

def test_qry_04_known_practitioner_no_appointments():
    store = SmartCareDataStore()
    PractitionerService(store).register_practitioner(
        'DR1', 'Taylor', 'General'
    )
    service = AppointmentService(store)

    result = service.list_practitioner_appointments('DR1')

    assert result == []
    assert result is not store.list_appointments()


def test_qry_04_unknown_practitioner():
    store = SmartCareDataStore()
    service = AppointmentService(store)

    with pytest.raises(LookupError):
        service.list_practitioner_appointments('DR99')


def test_qry_04_invalid_practitioner_id():
    store = SmartCareDataStore()
    service = AppointmentService(store)

    with pytest.raises(ValueError):
        service.list_practitioner_appointments('')


def test_qry_04_invalid_status():
    store = SmartCareDataStore()
    PractitionerService(store).register_practitioner(
        'DR1', 'Taylor', 'General'
    )
    service = AppointmentService(store)

    with pytest.raises(ValueError):
        service.list_practitioner_appointments('DR1', 'scheduled')

def test_qry_02_none_and_no_match():
    appointments = make_appointments()

    assert select_appointments(appointments, 'DR1', None) == \
        select_appointments(appointments, 'DR1')

    result = select_appointments(
        appointments, 'DR2', AppointmentStatus.CANCELLED
    )
    assert result == []
    assert result is not appointments

def test_fp_01_repeatability():
    appointments = make_appointments()
    before = [
        (a, a.appointment_id, a.date_time, a.status)
        for a in appointments
    ]

    first = select_appointments(appointments, 'DR1')
    second = select_appointments(appointments, 'DR1')

    assert first == second
    assert first is not second
    assert [
        (a, a.appointment_id, a.date_time, a.status)
        for a in appointments
    ] == before

def test_fp_02_new_lists():
    appointments = make_appointments()

    for source in [
        [],
        sorted(appointments, key=appointment_sort_key),
        appointments,
    ]:
        before = list(source)
        result = select_appointments(source, 'DR1')

        assert result is not source
        assert source == before
        assert all(any(a is b for b in source) for a in result)

def test_fp_03_key_is_used(monkeypatch):
    import smartcare.queries as queries

    calls = []
    original_key = queries.appointment_sort_key

    def tracking_key(appointment):
        calls.append(appointment)
        return original_key(appointment)

    monkeypatch.setattr(queries, 'appointment_sort_key', tracking_key)

    result = queries.select_appointments(make_appointments(), 'DR1')

    assert len(calls) == 3
    assert [a.appointment_id for a in result] == ['A1', 'A4', 'A3']

def test_cancelled_history_and_rejected_request():
    store = SmartCareDataStore()
    PatientService(store).register_patient('P1', 'Alex')
    PractitionerService(store).register_practitioner(
        'DR1', 'Taylor', 'General'
    )
    service = AppointmentService(store)

    booked = service.book_appointment(
        'A1', 'P1', 'DR1', datetime(2026, 10, 1, 9, 0)
    )
    service.cancel_appointment('A1')

    assert service.find_appointment('A1') is booked
    assert service.list_practitioner_appointments('DR1') == [booked]
    assert service.list_practitioner_appointments(
        'DR1', AppointmentStatus.SCHEDULED
    ) == []

    with pytest.raises(ValueError):
        service.list_practitioner_appointments('DR1', 'scheduled')

    assert store.list_appointments() == [booked]
    assert booked.status is AppointmentStatus.CANCELLED