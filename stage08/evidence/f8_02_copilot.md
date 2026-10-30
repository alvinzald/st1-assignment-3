# F8-02 GitHub Copilot Debugging Review

**Member:** Alvin Zaldivar
**Date:** 30 October 2026

## Actual Prompt

Observed behaviour: [Cancelled appointments become inaccessible through lookup. System raises `LookupError: Appointment not found`]

Expected behaviour and requirement: [`find_appointment()` should return the appointment even if it has been cancelled, based on FR-07, FR-08 and AC-05.2]

Steps to reproduce:
  - [Register patient `Alex` (P1)]
  - [Register practitioner `Chris` (D1), specialty `GP`]
  - [Book appointment `A1` for `Alex` with `Chris` at `2026-10-01 09:00`]
  - [Cancel appointment `A1`]
  - [Find appointment `A1`]
  
Failing Test:
    - Test path: [`project/tests/test_services.py:74`]
    - Test name: [`test_cancel_success_and_history`]
    - Expected Result: [Cancelled appointment can still be looked up.]
    - Actual Result: [`LookupError: Appointment not found`]

My hypothesis:
My earlier suspicion was that cancellation deleted the appointment, but the regression test contradicted this. The find_appointment() method incorrectly excludes appointments with CANCELLED status, causing it to return None even though the appointment remains stored.

Relevant code:
data_store.py, services.py

Task:
Rank the three most likely causes. For each, identify the evidence I should inspect to distinguish it from the other possible causes.
Do not rewrite the entire application.
Do not invent requirements.
Treat all suggested explanations as hypotheses.

## Copilot Response

| Rank | Hypothesis | Evidence to inspect to distinguish it |
|---|---|---|
| 1 | **`find_appointment()` filters out cancelled records.** | In `project/smartcare/data_store.py:92–96`, inspect the ID match and status condition. It returns a matching appointment only when `appointment.status.value != "cancelled"`. After cancellation, compare `store.list_appointments()` with `store.find_appointment('A1')`; the regression test reports the appointment remains listed while lookup returns `None`, which fits this cause. |
| 2 | **The lookup uses an unexpected appointment ID.** | Trace the ID from `AppointmentService.find_appointment()` at `project/smartcare/services.py:125–134` into the data store. Compare the argument, after trimming, with the stored appointment’s ID. A mismatch would explain a `None` result even without a status filter. |
| 3 | **Cancellation or the service/store setup leaves lookup searching the wrong state.** | Check whether `cancel_appointment()` at `services.py:136–148` retains and updates the same appointment object, and whether cancellation and lookup use the same `SmartCareDataStore`. The regression test’s retained-list assertion weighs against deletion, but checking object identity and store identity distinguishes this from the lookup filter. |

The filter is the strongest hypothesis given the inspected code and regression-test observation; the other causes remain possibilities to rule out with the checks above.