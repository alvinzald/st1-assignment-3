# SmartCare 

Requirements baseline: SmartCare A3 2026 revision 2. Python 3.13 and pytest 8.3.5 verified. Runtime uses only the standard library.

From this directory, using a Python environment with the development dependency installed:

```sh
python main.py
python main.py --interactive
python -m pytest 
```

If needed in your approved environment: `python -m pip install -r requirements-dev.txt`.

The demo registers synthetic records and books/finds an appointment. All supplied tests pass. Data exists only in this session and is lost on exit; FR-10 restart persistence is retired. Use synthetic information only.

`domain.py` contains the entities, status and guarded cancellation. `data_store.py` holds three dictionaries through add/find/list methods. The three services share that object. Supplied registration, booking, appointment lookup and conflict checking work. IDs are trimmed, non-blank and case-sensitive. Properties provide read-only identity/appointment state; changes go through domain methods. No special architecture terminology is required.

## Stage 9 - Interactive Menu
Stage 6 and Stage 9 tasks are completed. The interactive menu allows user to register and find patients and practitioners, book and cancel appointments, find appointment history, and list appointments by practitioner and status.
Queries filter and sort appointments without changing the original list. Cancelled appointments remain in history, and their time slots can be booked again.

## Stages 10–11 – PG Features

The PG extension adds appointment rescheduling and additional tests. Rescheduling allows an existing appointment to be moved to another available time while keeping its identity and participants. The tests check valid rescheduling, conflicts, invalid changes and appointment history.

Service booking accepts IDs and a `datetime` (local, minute precision). Console parser accepts exactly `YYYY-MM-DD HH:MM`. Store lookups return None when absent; service lookups raise LookupError. Invalid values, duplicates, conflicts and illegal transitions raise ValueError. Lists are new containers holding the stored objects. No age, duration, patient-conflict or past-date rules apply.
