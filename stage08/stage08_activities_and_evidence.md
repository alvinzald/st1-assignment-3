# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

- Group/tutorial: [Wed 4:30-6:30, Group 6]
- Members and UG/PG cohorts:
  - [Member 1: Noor Anwari, [nooranwari](https://github.com/nooranwari), UG]
  - [Member 2: Alvin Zaldivar, [alvinzald](https://github.com/alvinzald), PG]
  - [Member 3: Kaneez Fiza, [u3327559](https://github.com/u3327559), UG]
- Record owner / contribution links for each member: [Alvin Zaldivar]

Use concise results and accessible artefact links rather than copying entire logs. Keep human-first entries before consulting GitHub Copilot. Link shared evidence once; do not repeat it across sections. No entries below are specimen answers or claimed results.

## A. Tutorial activities

### A.1 Classify all five statements
For each, choose symptom, evidence or hypothesis/opinion, and explain your reason. These are discussion statements, not confirmed diagnoses.

| Statement                                                         | Classification     | Reason |
| ----------------------------------------------------------------- | ------------------ | --- |
| Appointment disappears after cancellation.                        | [Symptom]            | [Describes the observable problem but not what is causing it.] |
| The data-store removal path is probably being called.             | [Hypothesis/Opinion] | [Possible explanation that still needs to be investigated.] |
| The failing test shows store.find_appointment('A1') returns None. | [Evidence]           | [Specific result from a failing test.] |
| The service layer is badly designed.                              | [Hypothesis/Opinion] | [Subjective judgement without concrete evidence.] |
| Traceback points to smartcare/services.py line 42 in the example. | [Evidence]           | [Identifies a specific line that could indicate where the problem occurred, but not the root cause.] |

The example line number is illustrative; inspect the actual line in your run. The removal hypothesis must be tested against the current project, which has no public delete operation.

Response and reason: [filled as table above]

### A.2 Build a debugging record
Choose the cancelled-history scenario or a same-practitioner/time booking. Before changing code, record expected behaviour, observed behaviour, minimal reproduction, a hypothesis and evidence to inspect. Use a requirement to justify the expectation. Keep the initial hypothesis even if later evidence disproves it.

Response and reason: 
- Expected behaviour: [The system should find the cancelled appointment and retain its history, as required by FR-07 and FR-08.]
- Observed behaviour: [The system does not find the cancelled appointment, raises `LookupError: Appointment not found`.]
- Minimal reproduction: [Book appointment A -> Cancel appointment A -> Find appointment A]
- Hypothesis: [Cancelling appointment deletes it.]
- Evidence to inspect: [List all stored appointments after cancellation and compare with lookup result.]

### A.3 Test defect or product defect
A test expects cancelled appointments to be deleted, but FR-07 says history must be retained. What should be changed? Explain why. Also decide whether a test expecting different practitioners at the same time to conflict reflects AC-04.2. Do not assume every failing test is correct.

Response and reason:
- Cancelled appointments: [The test should be changed because its expectation contradicts FR-07, which requires cancelled appointment history to be retained. Tests should reflect functional requirements.]
- Appointment vs practitioner conflicts: [Test is incorrect because AC-04.2 explicitly allows different practitioners to have appointments at the same time. The test should be changed to permit this behaviour.]

### A.4 Refactoring smell hunt
Consider a hypothetical 70-line AppointmentService method containing duplicate status strings, direct collection manipulation, printing, validation and four nested conditionals. Identify the smells and propose small refactorings that preserve required behaviour. The direct collection work replaces the old storage-specific scenario; use the existing SmartCareDataStore boundary. Do not implement an extra architecture.
Classify these proposed changes as refactoring, repair or feature: rename appt to appointment; extract a repeated conflict helper; add rescheduling; restore retained cancellation lookup; replace a magic status string with the existing enum. Explain the behaviour that must remain unchanged.

Response and reason:

| Characteristic | Smell | Proposed refactoring | Reason | 
| -------------- | ----- | -------------------- | ------ |
| 70-line method | [Long method] | [Extract smaller methods for distinct responsibilities.] | [Improve readability and make the code easier to maintain.] |
| Duplicate status strings | [Duplication / magic strings] | [Replace hardcoded strings with existing `AppointmentStatus` enum.] | [Reduce duplication and avoid inconsistent status values.] |
| Direct collection manipulation | [Misplaced responsibility] | [Use existing methods from `data_store`] | [Collection management should be handled by the data store, not the service.] |
| Printing and validation | [Mixed responsibilities] | [Move printing to the UI layer and keep domain validation in the domain class.] | [Separate business logic while keeping validation with appropriate responsibility.] |
| Four nested conditionals | [Deep nesting] | [Use guard clauses or extract smaller methods] | [Reduce complexity and makes the logic easier to follow.] |

| Proposed change | Classification | Reason |
| --------------- | -------------- | ------ |
| Rename appt to appointment | [Refactoring] | [Improve readability without changing behaviour.] |
| Extract repeated conflict logic into a helper | [Refactoring] | [Reduce duplication while preserving existing booking rules.] |
| Add appointment booking feature | [Feature] | [Introduce functionality that does not currently exist.] |
| Restore cancelled appointment lookup | [Repair] | [Correct a behaviour that does not meet the requirement to retain appointment history (FR-07).] |
| Replace a magic status string with the existing enum | [Refactoring] | [Improve consistency and maintainability without changing behaviour.] |

### A.5 Traceback and hypothesis ranking
Using one actual failure, identify its exception/assertion, expected and observed values, test line, application call path and supporting requirement. List three plausible causes and rank them by fit with the available evidence. For each cause, name a check that could distinguish it from the others. Explain why a traceback alone does not establish the cause.

Response and reason:

Traceback
- Failing test: [`test_cancel_success_and_history`]
- Exception: [`LookupError: Appointment not found`]
- Expected behaviour: [`find_appointment('A1')` returns the same cancelled appointment object.]
- Observed behaviour: [The lookup raises a `LookupError` instead of returning the appointment.]
- Test location: [`tests\tests_services.py`, `line 74`]
- Application call path: [`Test` -> `AppointmentService.find_appointment()` -> `SmartCareDataStore.find_appointment()` -> `LookupError` at `services.py:133`]
- Supporting requirements:
  - [FR-07 (retain cancellation history)]
  - [FR-08 (appointment lookup)]

Hypothesis ranking

| Rank | Hypothesis | Reason | Check to distinguish | 
| -- | -- | -- | -- |
| [1] | [Lookup filters out cancelled appointments.] | [The `find_appointment()` code contains a condition that excludes cancelled appointments: `if (appointment.appointment_id == appointment_id.strip() and appointment.status.value != "cancelled")`] | [Compare results from `list_appointments()` with `find_appointment('A1')` after cancellation.] |
| [2] | [Cancellation deletes the appointment.] | [Appointment becomes inaccessible after cancellation.] | [List stored appointments after cancellation to see whether the cancelled appointment still exists.] |
| [3] | [Service uses a different data-store instance.] | [The appointment might exist in a different data-store. Least likely because the failing test uses the same service instance to cancel and retrieve the appointment.] | [Check whether the service and booking operation reference the same store instance.] |

[The traceback alone is insufficient because the traceback shows where the exception was raised, but not necessarily where the bug originated. For example, the exception could have been raised in search, but the root cause may be because what we're searching for was not stored in the right place.]

### A.6 Exit question
Why is changing code immediately after seeing a failure often a poor debugging strategy?

Response and reason: 
[Changing code based on our first instinct might lead us to modify something that isn't actually broken, potentially introducing more bugs. We should investigate the failure and identify its root cause before attempting a fix.]

- [x] Classification responses (1–5, each with reason): [[Section A.1](#a1-classify-all-five-statements)]
- [x] Tutorial debugging record — expected; observed; reproduction; hypothesis; evidence to inspect: [[Section A.2](#a2-build-a-debugging-record)]
- [x] Traceback — exception/assertion; expected/observed values; test line; call path; requirement; ranked causes and discriminating checks: [[Section A.5](#a5-traceback-and-hypothesis-ranking)]

## B. Stage 7 baseline and safe preparation

- Stage 7 code SHA and requirement baseline: 
  - Stage 7 code SHA: [`edd11e9fa09edfb7e9b61b13029ac5b11c50f3b3`]
  - Requirement baseline: [SmartCare Revision 2 requirements]
    - [Practitioner booking conflicts: FR-05, AC-04.1, AC-04.2]
    - [Cancellation, retained appointment history and lookup: FR-06, FR-07, FR-08]
- Baseline test command / working directory / observed result / evidence: 
  - Test command: [`python -m pytest`]
  - Working directory: [`project/`]
  - Observed result: [18 passed, 0 failed]
  - Evidence: [[Stage 8 preparation evidence](evidence/preparation_terminal.jpeg)]
- Clean preparation SHA if a record-only commit followed Stage 7: [`8ac8b4d281e44d592bc2346170d65a16f9626e30`]
- Branch and preparer / how teammates obtained this branch: 
  - Branch: [`debug/stage08`]
  - Preparer: [[Alvin Zaldivar](https://github.com/alvinzald)]
  - Branching issue: [After the utility was applied, a teammate accessed debug/stage08 but still obtained 18 passing tests instead of the expected failures.]
  - Resolution: [Following the tutor's recommendation, the prepared faulty state (`81f59f6`) was merged into main through PR #8 (merge SHA `5869830`). The teammate was then able to reproduce the failing tests.]
  - Current branch: [A new debug/stage08 branch was created from the updated main for the Stage 8 repairs, without reapplying the utility.]
  - Synchronisation: [Teammates obtained the faulty state through the updated main branch after the merge.]
- Downloaded tool version, source SHA256 and --check outcome: 
  - Tool version: [1.1]
  - Source SHA256: [Unavailable. The utility was removed after preparation, and its source hash was not recorded.]
  - `-- check` outcome: [`preflight PASS`]
- --apply and --verify output summaries / artefact references: 
  - `--apply` outcome: [`PASS`: The utility successfully introduced F8-01 (practitioner conflict) and F8-02 (retained-history lookup).]
  - `--verify` outcome: [`VERIFIED`: Exactly two expected diagnostic failures were detected, with both approved symptom signatures present.]
- Bounded diff inspected and recovery location (not committed):
  - Bounded diff: [Commit `81f59f6` modified only `project/smartcare/data_store.py` (11 insertions, 18 deletions), affecting `find_appointment()` and `has_practitioner_conflict()`.]
  - Recovery location: [`project/.stage8_faults/` (local preparation backup, excluded from submission).]
- Prepared faulty-state commit SHA: [`81f59f65a9100f068afe7892d9f60ea92cd81a8b`]
- Preparation or recovery issues and resolution, if any:
  - Issue: [After the preparation utility was successfully applied, a teammate accessed the debug/stage08 branch but still obtained 18 passing tests instead of the expected failures. The exact cause of the branch synchronisation issue was not established.]
  - Resolution: [Following the tutor's recommendation, the prepared faulty state was merged into main through PR #8 (`5869830`). The teammate was then able to reproduce the failures. A new `debug/stage08` branch was subsequently created from main to continue] debugging and repairs.
- Initial prepared full-suite command / result / key failures:
  - Test command: [`py -m pytest -q`]
  - Working directory: [`project/ `]
  - Tested SHA: [`5869830` (prepared faulty state integrated into main).]
  - Result: [15 passed, 3 failed (18 tests total).]
  - Key failures:
    - [F8-01: `test_conflict_rule_and_different_practitioner`: A conflicting booking was accepted instead of raising ValueError.]
    - [F8-02: `test_cancel_success_and_history`: Looking up a cancelled appointment raised LookupError.]
    - [F8-02: `test_cancel_invalid_status`: Repeated cancellation raised LookupError instead of ValueError. ]
  - Evidence: [[Initial Stage 8 pytest results](evidence/initial_tests.txt)]

## C. F8-01 diagnosis and repair

- Symptom / observed behaviour: [The system accepted a double booking for the same practitioner at the exact same date and time instead of rejecting it.]
- Expected behaviour and requirement: [The system should reject the new booking, based on FR-05 and AC-04.1]
- Minimal synthetic reproduction steps:
  - [Register patient `Alex` (P1)]
  - [Register patient `Ben` (P2)]
  - [Register practitioner `Chris` (D1), specialty `GP`]
  - [Book appointment `A1` for `Alex` with `Chris` at `2026-10-01 09:00`]
  - [Book appointment `A2` for `Ben` with `Chris` at `2026-10-01 09:00`]
- Meaningful failing test path/name and exact relevant failure: 
  - Existing test:
    - Test path: [`project/tests/test_starter.py:127`]
    - Test name: [`test_conflict_rule_and_different_practitioner`]
    - Expected result: [`ValueError` raised for conflicting booking]
    - Actual result: [Failed: DID NOT RAISE `ValueError`]
  - Stage 8 Regression test:
    - Test path: [`project/tests/test_regressions.py:34`]
    - Test name: [`test_f8_01_rejects_double_booking_without_mutation`]
    - Expected result: [`ValueError` raised for conflicting booking, with existing stored appointments unchanged.]
    - Actual result: [Failed: DID NOT RAISE `ValueError`]
    - Evidence: [F8-01 failing regression test](evidence/f8_01_booking_conflict_before_repair.txt)
- Human hypothesis and intended checks: [Section E: F8-01 Human Entry](#f8-01-human-entry)
- Supported root cause and inspected code/runtime evidence: [`has_practitioner_conflict()` uses `!=` instead of `==` when checking practitioner IDs. This made it not detect bookings from the same practitioner at the same time as a conflict. Code inspection and failing regression test confirms the issue.]
- Smallest justified fix / diff / why other behaviour is preserved: [Changed `!=` to `==` in the practitioner ID comparison. This operator change corrects the conflict detection without modifying the booking process or other methods. The existing test also confirmed that different practitioners can still be booked at the same time.]
- Focused verification result: [[F8-01 after repair](evidence/f8_01_booking_conflict_after_repair.txt)]
  - [x] [`test_conflict_rule_and_different_practitioner` passed after repair.]
  - [x] [`test_f8_01_rejects_double_booking_without_mutation` passed after repair.]
- Repair SHA: [`82552e5d45155e9367c51dff90ece2fdec23618a`]

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: [Cancelled appointments become inaccessible through lookup. System raises `LookupError: Appointment not found`]
- Expected behaviour and requirement: [`find_appointment()` should return the appointment even if it has been cancelled, based on FR-07, FR-08 and AC-05.2]
- Minimal synthetic reproduction steps:
  - [Register patient `Alex` (P1)]
  - [Register practitioner `Chris` (D1), specialty `GP`]
  - [Book appointment `A1` for `Alex` with `Chris` at `2026-10-01 09:00`]
  - [Cancel appointment `A1`]
  - [Find appointment `A1`]
- Meaningful failing test path/name and exact relevant failure:
  - Existing test 1:
    - Test path: [`project/tests/test_services.py:74`]
    - Test name: [`test_cancel_success_and_history`]
    - Expected Result: [Cancelled appointment can still be looked up.]
    - Actual Result: [`LookupError: Appointment not found`]
  - Existing test 2:
    - Test path: [`project/tests/test_services.py:84`]
    - Test name: [`test_cancel_invalid_status`]
    - Expected Result: [Cancelling an appointment whose `AppointmentStatus` is not `SCHEDULED` should raise a `ValueError`.]
    - Actual Result: [`LookupError: Appointment not found`]
  - Stage 8 Regression test:
    - Test path: [`project/tests/test_regressions.py:72`]
    - Test name: [`test_f8_02_cancelled_appointment_remains_accessible`]
    - Expected result: [`find_appointment('A1')` returns the original cancelled appointment.]
    - Actual result: [`AssertionError: assert None is <smartcare.domain.Appointment object at 0x000001C731A7B4D0>.`]
    - Supporting observation: [The appointment remains in `list_appointments()` with `cancelled` status, but lookup returns `None`.]
    - Evidence: [F8-02 failing regression test](evidence/f8_02_cancelled_lookup_before_repair.txt)
- Human hypothesis and intended checks: [Section E: F8-02 Human Entry](#f8-02-human-entry)
- Supported root cause and inspected code/runtime evidence: [In `data_store.py`: `find_appointment()` filtered out appointments with cancelled status. The regression test showed that the cancelled appointment appears in `list_appointments()`, but `find_appointment('A1')` returned `None`. This confirms that the issue was caused by the lookup filter rather than deletion.]
- Smallest justified fix / diff / why other behaviour is preserved: [In find_appointment(): Removed the `appointment.status.value != "cancelled"` condition. This allows cancelled appointments to not be rejected while preserving the existing ID matching logic. All three focused tests passed after the change.]
- Focused verification result: [[F8-02 after repair](evidence/f8_02_cancelled_lookup_after_repair.txt)]
  - [x] [`test_cancel_success_and_history` passed after repair.]
  - [x] [`test_cancel_invalid_status` passed after repair.]
  - [x] [`test_f8_02_cancelled_appointment_remains_accessible` passed after repair.]
- Repair SHA: [`5af4c990f1a5aa2ee896c424975bb5dc855cd2e7`]

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

### F8-01 human entry
- Likely cause and why plausible: [The `has_practitioner_conflict()` method uses `!=` instead of `==` when comparing practitioner IDs. This could be the cause because it's supposed to check for sameness in conflicts.]
- Evidence intended to inspect: [Attempt to book appointment for a different practitioner at the same time.]
- Competing explanation: [The service might be passing incorrect parameters to `has_practitioner_conflict()`.]
- Discriminating check: [Inspect the arguments passed from `AppointmentService.book_appointment()` and compare them with the values received by `SmartCareDataStore.has_practitioner_conflict()`.]
- Member and saved sequence/time or commit showing this preceded consultation: [Alvin Zaldivar at 30 Oct 2026 18:35]

### F8-02 human entry
- Likely cause and why plausible: [The `find_appointment()` method excludes appointments with `cancelled` status, causing it to return `None` even though the appointment remains stored. The code explicitly checks `appointment.status.value != "cancelled"`, which prevents cancelled appointments from being returned.]
- Evidence intended to inspect: [Compare the results from `list_appointments()` and `find_appointment('A1')` after cancellation to check if the appointment is still stored but excluded from lookup. Inspect `find_appointment()` to identify what might cause this.]
- Competing explanation: [The appointment lookup might be passing an incorrect ID to compare.]
- Discriminating check: [Compare the stored appointment ID against the lookup arg to determine whether the IDs match.]
- Member and saved sequence/time or commit showing this preceded consultation: [Alvin Zaldivar at 30 Oct 2026 19:40]

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review
Actual prompt / output reference and member: [[F8-01 Copilot Prompt](evidence/f8_01_booking_conflict_copilot.md), Alvin Zaldivar]
1. Suggestion: The practitioner comparison is inverted in `has_practitioner_conflict()`.
   - Evidence to check: Check `project/smartcare/data_store.py:108–114`: the condition uses `appointment.practitioner.practitioner_id != practitioner_id`. For the reproduced D1/D1 booking, that condition is false, so the conflict is missed. This best fits the symptom, but remains a hypothesis until the executed code path is confirmed.
   - Observed evidence: [The code uses `!=`, and our regression test failed because the second booking did not raise `ValueError`.]
   - Assessment: [Correct]
   - Decision: [Accept]
   - Reason: [The code and failing regression test support this diagnosis.]
2. Suggestion: `book_appointment()` passes the wrong values or does not reach the conflict check.
   - Evidence to check: Trace the call at `project/smartcare/services.py:115–122`; confirm it invokes the store method with the new practitioner’s ID and the requested time. The source currently shows those values being passed, which makes this less likely; a runtime spy or breakpoint could confirm the values actually received.
   - Observed evidence: [The service passes `practitioner.practitioner_id` and `date_time` correctly.]
   - Assessment: [Wrong]
   - Decision: [Reject]
   - Reason: [Second booking completes without raising an exception, indicating that the conflict check was reached but did not detect the conflict.]
3. Suggestion: The stored appointment does not qualify as a conflict candidate—for example, it is missing, has a different time/practitioner, or is not scheduled.
   - Evidence to check: After booking A1, inspect `list_appointments()` and compare its practitioner ID, date_time, and status with the second booking’s inputs. Also confirm both operations use the same store. The predicate checks these fields at `data_store.py:109–112`; mismatches could prevent a conflict independently of the ID comparison.
   - Observed evidence: [The test successfully creates A1 with practitioner D1 at the specified datetime. Code inspection shows that newly booked appointments are stored with SCHEDULED status.]
   - Assessment: [Wrong]
   - Decision: [Reject]
   - Reason: [The test setup and booking code indicate that `A1` should qualify as a conflict.]

Final human conclusion and comparison with initial hypothesis: [The #1 suggestion from copilot supports the hypothesis. Copilot did not change my original conclusion, and the alternative explanations were less consistent with the available evidence.]

### F8-02 Copilot review
Actual prompt / output reference and member: [[F8-02 Copilot Prompt](evidence/f8_02_booking_conflict_copilot.md), Alvin Zaldivar]
1. Suggestion: find_appointment() filters out cancelled records.
   - Evidence to check: In `project/smartcare/data_store.py:92–96`, inspect the ID match and status condition. It returns a matching appointment only when `appointment.status.value != "cancelled"`. After cancellation, compare `store.list_appointments()` with `store.find_appointment('A1')`; the regression test reports the appointment remains listed while lookup returns None, which fits this cause.
   - Observed evidence: [The appointment remains stored with `CANCELLED` status, but `find_appointment('A1')` returns None. The code explicitly excludes cancelled appointments.]
   - Assessment: [Correct]
   - Decision: [Accept]
   - Reason: [The code inspection and failing regression test support the diagnosis]
2. Suggestion: The lookup uses an unexpected appointment ID.
   - Evidence to check: 
   - Observed evidence: [Trace the ID from `AppointmentService.find_appointment()` at `project/smartcare/services.py:125–134` into the data store. Compare the argument, after trimming, with the stored appointment’s ID. A mismatch would explain a `None` result even without a status filter.]
   - Assessment: [Wrong]
   - Decision: [Reject]
   - Reason: [The IDs match in our reproduction, so an ID mismatch does not explain the failure.]
3. Suggestion: Cancellation or the service/store setup leaves lookup searching the wrong state.
   - Evidence to check: Check whether `cancel_appointment()` at `services.py:136–148` retains and updates the same appointment object, and whether cancellation and lookup use the same `SmartCareDataStore`. The regression test’s retained-list assertion weighs against deletion, but checking object identity and store identity distinguishes this from the lookup filter.
   - Observed evidence: [The regression test confirms  that the appointment remains in `list_appointments()`. The services are initialised using the same `SmartCareDataStore` instance.]
   - Assessment: [Wrong]
   - Decision: [Reject]
   - Reason: [The appointment remains stored, and the services share the same data store.]

Final human conclusion and comparison with initial hypothesis: [My initial hypothesis was that cancellation deleted the appointment from storage. After inspecting the code and running the regression test, I revised my hypothesis to the lookup method incorrectly filtering out cancelled appointments. Copilot's top-ranked diagnosis supported this revised hypothesis, while the other suggestions were less consistent with the evidence.]

## G. Failing to passing regression evidence

| Checkpoint | Code SHA or precise diff | Command and working directory | Actual result and artefact reference |
|---|---|---|---|
| F8-01 before repair | [`edd11e9fa09edfb7e9b61b13029ac5b11c50f3b3`] | [`python -m pytest tests/test_regressions.py::test_f8_01_rejects_double_booking_without_mutation -v` in `project/`] | [[F8-01 Before Repair](evidence/f8_01_booking_conflict_before_repair.txt)] |
| F8-01 after repair | [`82552e5d45155e9367c51dff90ece2fdec23618a`] | [`python -m pytest tests/test_regressions.py::test_f8_01_rejects_double_booking_without_mutation tests/test_starter.py::test_conflict_rule_and_different_practitioner -v` in `project/`] | [[F8-01 After Repair](evidence/f8_01_booking_conflict_after_repair.txt)] |
| F8-02 before repair | [`edd11e9fa09edfb7e9b61b13029ac5b11c50f3b3`] | [`python -m pytest tests/test_regressions.py::test_f8_02_cancelled_appointment_remains_accessible -v` in `project/`] | [[F8-02 Before Repair](evidence/f8_02_cancelled_lookup_before_repair.txt)] |
| F8-02 after repair | [`5af4c990f1a5aa2ee896c424975bb5dc855cd2e7`] | [`python -m pytest tests/test_regressions.py::test_f8_02_cancelled_appointment_remains_accessible tests/test_services.py::test_cancel_success_and_history tests/test_services.py::test_cancel_invalid_status -v` in `project/`] | [[F8-02 After Repair](evidence/f8_02_cancelled_lookup_after_repair.txt)] |
| Full suite after both repairs, before refactor | [`5af4c990f1a5aa2ee896c424975bb5dc855cd2e7`] | [`python -m pytest tests -v in project/`] | [[Full Suite After Repairs](evidence/full_suite_after_repairs.txt)] |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour:
 - [F8-01 verifies that conflicting bookings raise `ValueError` without changing existing records, while allowing different practitioners to share a timeslot.]
 - [F8-02 verifies that cancelled appointments remain stored and retrievable, and that repeated cancellation raises `ValueError` without changing their status.]

Unrelated failures investigated / resolution: [Not applicable: All three initial failures were related to F8-01 or F8-02. After both repairs, all 20 tests passed with no remaining failures.]

## H. Refactoring decision and before/after verification

- Smell: [Inefficient dictionary lookup in `find_appointment()`]
- Exact Location: [`project/smartcare/data_store.py:92`]
- Small proposed structural change / why justified: [Replace the loop in `find_appointment()` with a direct dictionary lookup using `.get()`. This simplifies the code, improves lookup efficiency, and makes it consistent with the other data-store lookup methods without changing its expected behaviour.]
- External behaviour to preserve / relevant tests: [The method must still raise `ValueError` for invalid IDs, return `None` for missing appointments, and return the same appointment object regardless of status. The F8-02 regression test and existing service tests protect these behaviours, while the full 20-test suite checks for unintended changes.]
- Before result: see G, full passing suite.
- Actual change / diff: [Replaced the loop in `find_appointment()` with `self._appointments.get(appointment_id.strip())` and added a docstring for consistency. ]
- Separate refactor SHA: [`afe473afa7fc9ab0486777db97daf7c4749ab585`]
- Focused after-refactor command and directory: [`python -m pytest tests/test_regressions.py::test_f8_02_cancelled_appointment_remains_accessible tests/test_services.py::test_cancel_success_and_history tests/test_services.py::test_cancel_invalid_status -v` in `project/`]
  - Results: 3 passed
  - Evidence: [[Appointment Lookup - Focused](evidence/appointment_lookup_refactor_focused.txt)]
- Full after-refactor commands and directory: [`python -m pytest tests -v` in `project/`]
  - Results: 20 passed
  - Evidence: [[Appointment Lookup - Full Suite](evidence/appointment_lookup_refactor_full_suite.txt)]
- Result: [Accepted]
  - Reason: [Replacing the unnecessary loop with a direct dictionary lookup improved readability and efficiency.]
  - Behaviour-preservation conclusion: [The focused tests and full suite passed after refactoring (20/20).]

## I. Git, human review and integration

- Issues for both defects / refactor scope and owners: 
  - F8-01: [The system accepted a double booking for the same practitioner at the exact same date and time instead of rejecting it.]
  - F8-02: [Cancelled appointments become inaccessible through lookup.]
  - Refactor: [Simplified `find_appointment()` in `project/smartcare/data_store.py` by replacing unnecessary iteration with a direct dictionary lookup using `.get()` and adding a docstring. No intended changes to external behaviour.]
  - Owner: [Alvin Zaldivar]
- Branch / prepared, repair and refactor checkpoints: 
  - Branch: [`debug/stage08`]
  - Checkpoint B: [`edd11e9fa09edfb7e9b61b13029ac5b11c50f3b3`]
  - Checkpoint C: [`82552e5d45155e9367c51dff90ece2fdec23618a`]
  - Checkpoint D: [`5af4c990f1a5aa2ee896c424975bb5dc855cd2e7`]
  - Checkpoint H: [`afe473afa7fc9ab0486777db97daf7c4749ab585`]
- PR link: [[Pull Request #9](https://github.com/alvinzald/st1-assignment-3/pull/9)]
- Another member's reviewer identity: [Kaneez Fiza]
- Key human feedback, difference from Copilot findings and response/outcome: [pending review]
- Actual review approval / merge evidence: [pending review]
- Integrated code SHA and team pull/retest command / working directory / result: [pending review]
- Evidence-only later SHA / explanation if different: [pending integration]
- Each member's substantive contribution and artefact: 
  - Alvin Zaldivar: [Investigated and repaired F8-01 and F8-02, developed regression tests, evaluated Copilot diagnoses, performed the behaviour-preserving refactoring, and documented the Stage 8 evidence. Artefacts: `data_store.py`, `test_regressions.py`, `stage08_activities_and_evidence.md`, and supporting evidence files.]
  - Kaneez Fiza: [Reviewer]
  - Noor Anwari: [Integrator]

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence? [None stood out as convincing but unsupported. I  already inspected the code and run regression tests before consulting Copilot, so I had strong evidence for my hypotheses. Its alternative suggestions, such as an incorrect appointment ID in F8-02, were possible explanations but did not fit the evidence I already gathered.]
2. What evidence changed your group's view? [I initially suspected that cancelled appointments were being deleted. However, the regression test showed that the appointment remained in `list_appointments()` but could not be retrieved through `find_appointment()`. This led us to investigate the lookup condition instead.]
3. How did regression tests protect the refactoring? [The regression tests helped confirm that changing `find_appointment()` to use a direct dictionary lookup did not reintroduce either defect. The full suite passed all 20 tests before and after refactoring, confirming the tested behaviour was preserved.]

## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

Response: [Reproduce the issue, check the expected behaviour, and investigate what might be causing it.]

2. Where should expected behaviour come from during debugging?

Response: [System requirements, acceptance criteria, and existing contracts, not personal assumptions.]

3. What is a debugging hypothesis?

Response: [A possible explanation for a problem that can be checked through testing or code inspection.]

4. What is a regression test and why is it retained?

Response: [A regression test checks that a previously fixed issue does not return after making changes. Keeping these tests helps catch problems introduced by future updates.]

5. What is meant by root cause?

Response: [The underlying issue that caused the failure, rather than just the error or symptom we observed.]

6. What is refactoring?

Response: [Improving how the code is written or organised without changing what the program actually does.]

7. What is a swallowed exception?

Response: [An exception that gets caught but is ignored or not properly handled, which can make problems harder to identify.]

8. What is a code smell?

Response: [Something in the code that suggests it could be improved, such as unnecessary repetition or overly complicated logic. It doesn't necessarily mean the code is broken.]

9. How should GitHub Copilot-generated debugging diagnoses be treated?

Response: [Treated as possible explanations, not confirmed answers. They still need to be checked against the code, requirements, and test results.]

10. What is the Stage 8 engineering rule?

Response: [Diagnose the problem before fixing it. Changes should be based on evidence, kept as small as possible, and tested to make sure existing behaviour is preserved.]

## L. Completion and handover

- [x] Existing project, earlier tests and stage records preserved.
- [x] Passing Stage 7 SHA and safe preparation details recorded.
- [x] Both defects reproduced with meaningful failing tests.
- [x] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [x] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [x] One genuine refactor verified under passing before/after tests.
- [ ] Human PR review, feedback resolution and integrated retest recorded.
- [x] Tutorial, three reflections and ten formative responses complete.
- [x] Local recovery metadata excluded from submitted source.
- [ ] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: see I.
Submitted SHA and evidence-only difference if any: [pending]
Unresolved issues or incomplete checks / owner / next action: [pending]
Handover note: [Both Stage 8 defects have been repaired, regression tests added, and appointment lookup refactored. The code and supporting evidence are included in the PR. Once reviewed, merged, and verified on main, the project will be ready for Stage 9.]
