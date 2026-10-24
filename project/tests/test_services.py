
from datetime import datetime
import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.services import PatientService, PractitionerService

from smartcare.domain import Appointment, AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)

def test_patient_lookup():
    store = SmartCareDataStore()
    service = PatientService(store)
    patient = service.register_patient("P001", "Alice")

    assert service.find_patient("P001") is patient
    assert service.find_patient(" P001 ") is patient

    with pytest.raises(LookupError):
        service.find_patient("P999")

    with pytest.raises(LookupError):
        service.find_patient("p001")

    for invalid_id in ["", "   ", 123]:
        with pytest.raises(ValueError):
            service.find_patient(invalid_id)


def test_practitioner_lookup():
    store = SmartCareDataStore()
    service = PractitionerService(store)
    practitioner = service.register_practitioner(
        "D001", "Dr Smith", "Cardiology"
    )

    assert service.find_practitioner("D001") is practitioner
    assert service.find_practitioner(" D001 ") is practitioner

    with pytest.raises(LookupError):
        service.find_practitioner("D999")

    with pytest.raises(LookupError):
        service.find_practitioner("d001")

    for invalid_id in ["", "   ", 123]:
        with pytest.raises(ValueError):
            service.find_practitioner(invalid_id)

def make_booked_appointment():
    store = SmartCareDataStore()
    PatientService(store).register_patient('P1', 'Test Patient')
    PractitionerService(store).register_practitioner(
        'DR1', 'Dr Test', 'General'
    )
    service = AppointmentService(store)
    appointment = service.book_appointment(
        'A1', 'P1', 'DR1', datetime(2026, 10, 1, 9, 0)
    )
    return store, service, appointment


def test_cancel_success_and_history():
    store, service, appointment = make_booked_appointment()

    result = service.cancel_appointment('A1')

    assert result is appointment
    assert result.status is AppointmentStatus.CANCELLED
    assert service.find_appointment('A1') is appointment
    assert appointment in store.list_appointments()


def test_cancel_invalid_status():
    store, service, appointment = make_booked_appointment()

    service.cancel_appointment('A1')

    with pytest.raises(ValueError):
        service.cancel_appointment('A1')
    assert appointment.status is AppointmentStatus.CANCELLED

    completed = Appointment(
        'A2', appointment.patient, appointment.practitioner,
        datetime(2026, 10, 2, 9, 0),
        status=AppointmentStatus.COMPLETED
    )
    store.add_appointment(completed)

    with pytest.raises(ValueError):
        service.cancel_appointment('A2')
    assert completed.status is AppointmentStatus.COMPLETED


def test_cancel_invalid_id():
    store, service, appointment = make_booked_appointment()

    with pytest.raises(LookupError):
        service.cancel_appointment('A9')

    for invalid_id in ['', '   ']:
        with pytest.raises(ValueError):
            service.cancel_appointment(invalid_id)

    assert appointment.status is AppointmentStatus.SCHEDULED
