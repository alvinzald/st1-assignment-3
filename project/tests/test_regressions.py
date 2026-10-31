
from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def test_f8_01_rejects_double_booking_without_mutation():
    # Arrange: Register patients and practitioner
    store = SmartCareDataStore()
    patient_service = PatientService(store)
    practitioner_service = PractitionerService(store)
    appointment_service = AppointmentService(store)

    patient_service.register_patient('P1', 'Alex')
    patient_service.register_patient('P2', 'Ben')
    practitioner_service.register_practitioner('D1', 'Chris', 'General')

    when = datetime(2026, 10, 1, 9, 0)

    # Act: Book the first appointment
    original = appointment_service.book_appointment(
        'A1', 'P1', 'D1', when
    )

    # Assert: Reject a conflicting booking
    with pytest.raises(ValueError):
        appointment_service.book_appointment(
            'A2', 'P2', 'D1', when
        )

    # Assert: Rejection must not change stored appointments
    assert store.find_appointment('A1') is original
    assert original.status is AppointmentStatus.SCHEDULED
    assert all(
        appointment.appointment_id != 'A2'
        for appointment in store.list_appointments()
    )


def test_f8_02_cancelled_appointment_remains_accessible():
    # Arrange: Register patient and practitioner
    store = SmartCareDataStore()
    patient_service = PatientService(store)
    practitioner_service = PractitionerService(store)
    appointment_service = AppointmentService(store)

    patient_service.register_patient('P1', 'Alex')
    practitioner_service.register_practitioner('D1', 'Chris', 'General')

    when = datetime(2026, 10, 1, 9, 0)

    # Act: Book and cancel an appointment
    original = appointment_service.book_appointment(
        'A1', 'P1', 'D1', when
    )
    cancelled = appointment_service.cancel_appointment('A1')

    # Assert: Cancellation changes status but retains history
    assert cancelled is original
    assert original.status is AppointmentStatus.CANCELLED
    assert original in store.list_appointments()

    # Assert: Cancelled appointment remains accessible
    assert store.find_appointment('A1') is original
    assert appointment_service.find_appointment('A1') is original

    # Assert: Repeated cancellation is rejected without mutation
    with pytest.raises(ValueError):
        appointment_service.cancel_appointment('A1')

    assert original.status is AppointmentStatus.CANCELLED
    assert len(store.list_appointments()) == 1
