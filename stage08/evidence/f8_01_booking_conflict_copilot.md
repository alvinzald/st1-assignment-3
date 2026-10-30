# F8-01 GitHub Copilot Debugging Review

**Member:** Alvin Zaldivar
**Date:** 30 October 2026

## Actual Prompt

Act as a software debugging assistant for our SmartCare Python application.

Observed behaviour: The system accepted a double booking for the same practitioner at the exact same date and time instead of rejecting it.

Expected behaviour: The system should reject the new booking

Steps to reproduce:
- [Register patient `Alex` (P1)]
- [Register patient `Ben` (P2)]
- [Register practitioner `Chris` (D1), specialty `GP`]
- [Book appointment `A1` for `Alex` with `Chris` at `2026-10-01 09:00`]
- [Book appointment `A2` for `Ben` with `Chris` at `2026-10-01 09:00`]


Failing test:
- Test path: [`project/tests/test_starter.py:127`]
- Test name: [`test_conflict_rule_and_different_practitioner`]
- Expected result: [`ValueError` raised for conflicting booking]
- Actual result: [Failed: DID NOT RAISE `ValueError`]

My hypothesis:
The `has_practitioner_conflict()` method uses `!=` instead of `==` when comparing practitioner IDs. This could be the cause because it's supposed to check for sameness in conflicts.`

Relevant code:
services.py,  data_store.py

Task:
Rank the three most likely causes. For each, identify the evidence I should inspect to distinguish it from the other possible causes.
Do not rewrite the entire application.
Do not invent requirements.
Treat all suggested explanations as hypotheses.

## Copilot Response

| Rank | Hypothesis | Evidence to inspect to distinguish it |
|---|---|---|
| 1 | **The practitioner comparison is inverted** in `has_practitioner_conflict()`. | Check `project/smartcare/data_store.py:108–114`: the condition uses `appointment.practitioner.practitioner_id != practitioner_id`. For the reproduced D1/D1 booking, that condition is false, so the conflict is missed. This best fits the symptom, but remains a hypothesis until the executed code path is confirmed. |
| 2 | **`book_appointment()` passes the wrong values or does not reach the conflict check.** | Trace the call at `project/smartcare/services.py:115–122`; confirm it invokes the store method with the new practitioner’s ID and the requested time. The source currently shows those values being passed, which makes this less likely; a runtime spy or breakpoint could confirm the values actually received. |
| 3 | **The stored appointment does not qualify as a conflict candidate**—for example, it is missing, has a different time/practitioner, or is not scheduled. | After booking A1, inspect `list_appointments()` and compare its practitioner ID, `date_time`, and status with the second booking’s inputs. Also confirm both operations use the same store. The predicate checks these fields at `data_store.py:109–112`; mismatches could prevent a conflict independently of the ID comparison. |

The different-practitioner case is a useful discriminator: the test also expects a same-time D2 booking to succeed (`test_starter.py:129–134`), so any fix or diagnosis should account for both outcomes.