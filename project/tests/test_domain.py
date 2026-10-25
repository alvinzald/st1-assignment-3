import sys
from pathlib import Path

# Add the 'smartcare' package folder to sys.path
SMARTCARE_DIR = Path(__file__).resolve().parent.parent / "smartcare"
PROJECT_DIR = Path(__file__).resolve().parent.parent

for path in (SMARTCARE_DIR, PROJECT_DIR):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import pytest
from datetime import datetime

try:
    from domain import Patient, Practitioner, Appointment, AppointmentStatus
except ModuleNotFoundError:
    from smartcare.domain import Patient, Practitioner, Appointment, AppointmentStatus

def test_blank_patient_id_rejected():
    """TEST-FR01-03: Verify constructor validation for blank or whitespace patient ID."""
    with pytest.raises(ValueError):
        Patient("", "Alex Example")
    with pytest.raises(ValueError):
        Patient("   ", "Alex Example")


def test_blank_practitioner_specialty_rejected():
    """TEST-FR03-01: Verify constructor validation for blank or whitespace practitioner specialty."""
    with pytest.raises(ValueError):
        Practitioner("DR1", "Dr. Smith", "")
    with pytest.raises(ValueError):
        Practitioner("DR1", "Dr. Smith", "   ")


def test_new_appointment_is_scheduled():
    """TEST-FR04-03: Verify newly constructed appointment defaults to SCHEDULED status."""
    patient = Patient("P1", "Alex Example")
    practitioner = Practitioner("DR1", "Dr. Smith", "Cardiology")
    appt = Appointment("A1", patient, practitioner, datetime(2026, 10, 1, 9, 0))
    assert appt.status == AppointmentStatus.SCHEDULED


def test_domain_cancellation():
    """TEST-FR06-01: Verify domain cancellation updates appointment status to CANCELLED."""
    patient = Patient("P1", "Alex Example")
    practitioner = Practitioner("DR1", "Dr. Smith", "Cardiology")
    appt = Appointment("A1", patient, practitioner, datetime(2026, 10, 1, 9, 0))
    appt.cancel()
    assert appt.status == AppointmentStatus.CANCELLED


def test_repeat_cancellation_rejected():
    """TEST-FR06-02: Verify domain cancellation guard prevents repeated execution."""
    patient = Patient("P1", "Alex Example")
    practitioner = Practitioner("DR1", "Dr. Smith", "Cardiology")
    appt = Appointment("A1", patient, practitioner, datetime(2026, 10, 1, 9, 0))
    appt.cancel()
    with pytest.raises(ValueError):
        appt.cancel()