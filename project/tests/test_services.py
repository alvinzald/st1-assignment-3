
import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.services import PatientService, PractitionerService


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
