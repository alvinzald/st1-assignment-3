"""Stage 9 contracts for pure collection processing."""


from datetime import datetime

from smartcare.domain import Appointment, AppointmentStatus


def appointment_sort_key(appointment: Appointment) -> tuple[datetime, str]:
    """Return the date/time and appointment ID ordering key without side
    effects.
    """
    return appointment.date_time, appointment.appointment_id    ##('Stage 9: named sorting key')


def select_appointments(
    appointments: list[Appointment],
    practitioner_id: str,
    status: AppointmentStatus | None = None,
) -> list[Appointment]:
    """Select and sort appointments without changing the original list."""
    selected = []

    for appointment in appointments:
        if appointment.practitioner.practitioner_id == practitioner_id:
            if status is None or appointment.status == status:
                selected.append(appointment)

    return sorted(selected, key=appointment_sort_key)  ##('Stage 9: pure query')
