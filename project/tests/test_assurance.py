
from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def test_reschedule_then_cancel_preserves_history():
    store = SmartCareDataStore()
    PatientService(store).register_patient("P1", "Alex")
    PractitionerService(store).register_practitioner(
        "D1", "Taylor", "General"
    )
    service = AppointmentService(store)

    original_time = datetime(2026, 10, 1, 9, 0)
    new_time = datetime(2026, 10, 1, 10, 0)

    appointment = service.book_appointment(
        "A1", "P1", "D1", original_time
    )

    assert service.reschedule_appointment("A1", new_time) is appointment
    assert service.cancel_appointment("A1") is appointment

    assert service.find_appointment("A1") is appointment
    assert appointment.date_time == new_time
    assert appointment.status is AppointmentStatus.CANCELLED

    cancelled = service.list_practitioner_appointments(
        "D1", AppointmentStatus.CANCELLED
    )
    assert cancelled == [appointment]

    replacement = service.book_appointment(
        "A2", "P1", "D1", new_time
    )
    assert replacement.status is AppointmentStatus.SCHEDULED
    assert len(store.list_appointments()) == 2


def test_patient_lookup_isolated_between_sessions():
    first_store = SmartCareDataStore()
    second_store = SmartCareDataStore()

    first_service = PatientService(first_store)
    second_service = PatientService(second_store)

    first_patient = first_service.register_patient("P1", "Alex")

    assert first_service.find_patient("P1") is first_patient

    with pytest.raises(LookupError):
        second_service.find_patient("P1")

    assert second_store.find_patient("P1") is None
    assert second_store.list_patients() == []

    second_patient = second_service.register_patient("P1", "Ben")

    assert second_service.find_patient("P1") is second_patient
    assert first_service.find_patient("P1") is first_patient
    assert second_patient is not first_patient
