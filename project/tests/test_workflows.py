
from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def make_services():
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    patients.register_patient('P1', 'Alex')
    practitioners.register_practitioner('D1', 'Taylor', 'General')
    practitioners.register_practitioner('D2', 'Jordan', 'Dental')

    return store, appointments


def test_booking_with_different_practitioners():
    store, service = make_services()
    time = datetime(2026, 10, 1, 9, 0)

    a1 = service.book_appointment('A1', 'P1', 'D1', time)
    a2 = service.book_appointment('A2', 'P1', 'D2', time)

    assert a1.status is AppointmentStatus.SCHEDULED
    assert a2.status is AppointmentStatus.SCHEDULED
    assert len(store.list_appointments()) == 2


def test_duplicate_unknown_and_conflict():
    store, service = make_services()
    time = datetime(2026, 10, 1, 9, 0)
    service.book_appointment('A1', 'P1', 'D1', time)

    with pytest.raises(ValueError):
        service.book_appointment('A1', 'P1', 'D1', time)

    with pytest.raises(LookupError):
        service.book_appointment('A2', 'P99', 'D1', time)

    with pytest.raises(ValueError):
        service.book_appointment('A3', 'P1', 'D1', time)

    assert len(store.list_appointments()) == 1
    assert store.find_appointment('A2') is None
    assert store.find_appointment('A3') is None


def test_cancel_history_and_freed_slot():
    store, service = make_services()
    time = datetime(2026, 10, 1, 9, 0)

    a1 = service.book_appointment('A1', 'P1', 'D1', time)
    service.cancel_appointment('A1')

    assert a1.status is AppointmentStatus.CANCELLED
    assert service.find_appointment('A1') is a1

    a2 = service.book_appointment('A2', 'P1', 'D1', time)

    assert a2.status is AppointmentStatus.SCHEDULED
    assert len(store.list_appointments()) == 2


def test_practitioner_history_and_filter():
    store, service = make_services()
    time = datetime(2026, 10, 1, 9, 0)

    service.book_appointment('A1', 'P1', 'D1', time)
    service.cancel_appointment('A1')
    service.book_appointment('A2', 'P1', 'D1', time)
    service.book_appointment('A3', 'P1', 'D2', time)

    all_results = service.list_practitioner_appointments('D1')
    scheduled = service.list_practitioner_appointments(
        'D1', AppointmentStatus.SCHEDULED
    )

    assert [a.appointment_id for a in all_results] == ['A1', 'A2']
    assert [a.appointment_id for a in scheduled] == ['A2']
    assert len(store.list_appointments()) == 3
