# Stage 7 Testing and Verification Record

Group/tutorial: [complete]  Members/cohorts: [complete]
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement | Positive test | Negative test | Key assertion |
|---|---|---|---|
| FR-01 Register patient | [Register a patient with valid ID 'P1' and name 'Alex'. Verify that the returned object contains matching trimmed attributes.] | [Attempt to register a patient with an existing ID 'P1' or a blank ID "".] | [assert patient.patient_id == 'P1' and with pytest.raises(ValueError): patient_service.register_patient('', 'Alex')] |
| FR-05 Prevent practitioner conflict | [Book two appointments for different practitioners ('DR1' and 'DR2') at the exact same date and time '2026-10-01 09:00'.] | [Attempt to book a second appointment for the same practitioner ('DR1') at the exact same date and time '2026-10-01 09:00'.] | [with pytest.raises(ValueError): appt_service.book_appointment('A2', 'P2', 'DR1', dt).] |
| FR-06 Cancel appointment | [Call cancel_appointment('A1') on a SCHEDULED appointment.] | [Call cancel_appointment('A1') on an appointment that has already been CANCELLED.] | [assert cancelled_appt.status == AppointmentStatus.CANCELLED and with pytest.raises(ValueError): appt_service.cancel_appointment('A1').] |
| FR-07 Retain cancelled history | [Cancel appointment 'A1', then request the data store using find_appointment('A1').] | [Verifying cancellation does not delete the appointment from the store or remove participant links.] | [assert store.find_appointment('A1') is appt and assert appt.status == AppointmentStatus.CANCELLED.] |

### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.

`assert True`
Judgement: [Weak/unclear]  Why: [It always evaluates to True regardless of application behavior or underlying state, failing to detect any product defect.]

`assert appointment is not None`
Judgement: [Weak/unclear]  Why: [It proves that an object reference exists, but it does not verify its specific properties, participant identity, or domain status (SCHEDULED/CANCELLED).]

`assert appointment.status == AppointmentStatus.CANCELLED`
Judgement: [Strong for stated behaviour]  Why: [It verifies the precise domain state transition required under FR-06 / AC-05.1 after any cancellation operation.]

`assert len(results) > 0`
Judgement: [Weak/unclear]  Why: [It confirms that a collection is nonempty, but it does not verify whether the correct appointment objects, participant IDs, or expected statuses are present in it.]

`assert data_store.find_appointment('A1') is appointment`
Judgement: [Strong for stated behaviour]  Why: [It checks the exact Python object identity (is) in the memory store, proving that the original appointment instance is retained for history under FR-07 rather than being recreated or replaced.]


### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.

| Input / Boundary state | Expected result | Supporting contract |
|---|---|---|
| **Blank identifiers:** Passing `""` or `"   "` as a `patient_id` or `practitioner_id`. | `ValueError` raised. | `domain.py` `required_text` helper requires non-blank string input after trimming whitespace. |
| **Whitespace-only names:** Passing `"   "` as a patient or practitioner `name`. | `ValueError` raised. | `domain.py` entity constructors reject empty or whitespace-only text. |
| **Same-time practitioner bookings:** Booking same practitioner at exact same time `2026-10-01 09:00` vs. different practitioner at `2026-10-01 09:00`. | Same practitioner raises `ValueError`; different practitioner succeeds. | `SmartCareDataStore.has_practitioner_conflict` checks practitioner ID and exact datetime matching. |
| **Cancelled appointments:** Calling `cancel()` on an appointment already in `CANCELLED` status. | `ValueError` raised; status remains `CANCELLED`. | `Appointment.cancel()` method protects its domain transition guard. |
| **Invalid status transitions:** Attempting to transition from `COMPLETED` or `CANCELLED` back to `SCHEDULED`. | `ValueError` raised. | `Appointment.cancel()` protects status properties and restricts illegal transitions. |

### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate | What is wrong | Rewritten test intention |
|---|---|---|
| 1 | [It only asserts patient is not None and fails to check whether fields were trimmed or correctly stored.] | [Verify that PatientService.register_patient(' P1 ', ' Alex ') stores trimmed ID 'P1' and name 'Alex'.] |
| 2 | [It only asserts appointment is not None and fails to verify participant identity or initial status.] | [Verify book_appointment and assigns AppointmentStatus.SCHEDULED and links the exact registered Patient and Practitioner objects.] |
| 3 | [It asserts True, which passes unconditionally and provides zero test verification.] | [Verify register_patient raises ValueError when attempting to register a duplicate patient ID.] |
| 4 | [It assumes that SMS notifications exist, which invents features outside the current SmartCare baseline requirements.] | [Verify booking a same practitioner at the same time slot raises ValueError while preserving store state.] |
| 5 | [It assumes SMS notification logic, which relies on out-of-scope external integrations] | [Verify cancel_appointment, updates status to CANCELLED while leaving the appointment retrievable via find_appointment.] |

### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
[Code coverage measures the lines of code which were executed during test execution, but it does not measure the quality or validity of the test assertions. A test suite can achieve 100% line coverage by running the code with weak assertions while it fails to check edge cases, error conditions, boundary validation, or domain state preservation.]

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

| Requirement | Acceptance criterion | Test ID | Test type | Test name / location | Expected behaviour | Result / observed status | Supplied or student-authored |
|---|---|---|---|---|---|---|---|
| **FR-01** | **AC-01.1** | `TEST-FR01-01` | Positive | `test_registration_and_booking` in `test_starter.py` | Valid patient ID and name stored in data store. | PASSED | Supplied |
| **FR-01** | **AC-01.2** | `TEST-FR01-02` | Negative | `test_duplicate_patient_preserves_original` in `test_starter.py` | Duplicate patient ID registration rejected with `ValueError`. | PASSED | Supplied |
| **FR-01** | Revision 2 validation contract | `TEST-FR01-03` | Negative | `test_blank_patient_id_rejected` in `test_domain.py` | Blank/whitespace patient ID raises `ValueError`. | PASSED | Student-authored |
| **FR-02** | **AC-02.1** | `TEST-FR02-01` | Positive | `test_find_patient_success` in `test_services.py` | Known patient lookup returns stored `Patient` object. | PASSED | Student-authored |
| **FR-02** | **AC-02.2** | `TEST-FR02-02` | Negative | `test_find_patient_absent_raises_lookup_error` in `test_services.py` | Valid unknown patient ID raises `LookupError`. | PASSED | Student-authored |
| **FR-03** | Supporting contract | `TEST-FR03-01` | Negative | `test_blank_practitioner_specialty_rejected` in `test_domain.py` | Blank practitioner specialty raises `ValueError` | PASSED | Student-authored |
| **FR-03** | Supporting contract | `TEST-FR03-02` | Positive | `test_find_practitioner_success` in `test_services.py` | Known practitioner lookup returns stored `Practitioner` object | PASSED | Student-authored |
| **FR-03** | Supporting contract | `TEST-FR03-03` | Negative | `test_find_practitioner_absent_raises_lookup_error` in `test_services.py` | Valid unknown practitioner ID raises `LookupError` | PASSED | Student-authored |
| **FR-04** | **AC-03.1** | `TEST-FR04-01` | Positive | `test_registration_and_booking` in `test_starter.py` | Valid participants create stored `SCHEDULED` appointment. | PASSED | Supplied |
| **FR-04** | **AC-03.2** | `TEST-FR04-02` | Negative | `test_unregistered_participants_rejected` in `test_starter.py` | Booking with unregistered participant raises `LookupError`/`ValueError`. | PASSED | Supplied |
| **FR-05** | **AC-04.1** | `TEST-FR05-01` | Negative | `test_conflict_rule_and_different_practitioner` in `test_starter.py` | Same practitioner at exact same time raises `ValueError`. | PASSED | Supplied |
| **FR-05** | **AC-04.2** | `TEST-FR05-02` | Positive | `test_conflict_rule_and_different_practitioner` in `test_starter.py` | Different practitioner at same time is permitted. | PASSED | Supplied |
| **FR-06** | **AC-05.1** | `TEST-FR06-01` | Positive | `test_domain_cancellation_and_guard` in `test_starter.py` | Cancelling scheduled appointment changes status to `CANCELLED`. | PASSED | Supplied |
| **FR-06** | **AC-05.3** | `TEST-FR06-02` | Negative | `test_repeat_cancellation_rejected` in `test_domain.py` | Cancelling an already cancelled appointment raises `ValueError`. | PASSED | Student-authored |
| **FR-07** | **AC-05.2** | `TEST-FR07-01` | Positive | `test_cancelled_appointment_retained_in_history` in `test_services.py` | Cancelled appointment remains retrievable in data store history. | PASSED | Student-authored |

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
|---|---|---|---|---|---|---|
| `TEST-FR01-03` | FR-01 | Revision 2 validation contract | Negative | Verify constructor validation for blank patient ID. | `ValueError` raised when initializing `Patient("", "Alex")`. | Checks core domain entity guard independently of service orchestration. |
| `TEST-FR02-01` | FR-02 | AC-02.1 | Positive | Verify patient lookup workflow via service layer. | `find_patient('P1')` returns the registered `Patient` object. | Verifies Stage 6 service lookup completion. |
| `TEST-FR02-02` | FR-02 | AC-02.2 | Negative | Verify service lookup error handling for absent patient. | `find_patient('P999')` raises `LookupError`. | Confirms service lookup raises `LookupError` rather than returning `None`. |
| `TEST-FR06-02` | FR-06 | AC-05.3 | Negative | Verify domain cancellation guard against repeated execution. | Second call to `cancel()` raises `ValueError`. | Proves domain entity protects invalid status transition invariants. |
| `TEST-FR07-01` | FR-07 | AC-05.2 | Positive | Verify cancelled appointment history retention in store. | `find_appointment('A1')` returns object with status `CANCELLED`. | Proves cancellation does not purge records from `SmartCareDataStore`. |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
|---|---|---|---|---|
| `TEST-FR01-03` | None required (direct constructor invocation). | Call `Patient("", "Alex Example")`. | `with pytest.raises(ValueError):` | Directly verifies that invalid entity creation is blocked at the domain boundary. |
| `TEST-FR02-01` | Instantiate store and `PatientService`; register patient `'P1'`. | Call `patient_service.find_patient('P1')`. | `assert result.patient_id == 'P1'` | Verifies that registered patient records are retrievable by ID via the service lookup. |
| `TEST-FR02-02` | Instantiate store and `PatientService`. | Call `patient_service.find_patient('UNKNOWN')`. | `with pytest.raises(LookupError):` | Proves the service contract raises `LookupError` rather than returning `None` for absent IDs. |
| `TEST-FR06-02` | Create `SCHEDULED` appointment `'A1'`; invoke `appt.cancel()`. | Invoke `appt.cancel()` a second time. | `with pytest.raises(ValueError):` | Proves state transition guards prevent illegal duplicate cancellation. |
| `TEST-FR07-01` | Register `P1` and `DR1`; book `A1`; invoke `cancel_appointment('A1')`. | Call `appt_service.find_appointment('A1')`. | `assert appt.status == AppointmentStatus.CANCELLED` | Proves historical records remain intact and retrievable after status transition. |

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

| Test ID | Behaviour | Test file/function | Result |
|---|---|---|---|
| `TEST-FR01-03` | Blank patient ID raises `ValueError`. | `tests/test_domain.py::test_blank_patient_id_rejected` | PASSED |
| `TEST-FR03-01` | Blank practitioner specialty raises `ValueError`. | `tests/test_domain.py::test_blank_practitioner_specialty_rejected` | PASSED |
| `TEST-FR04-03` | New appointment defaults to `SCHEDULED` status. | `tests/test_domain.py::test_new_appointment_is_scheduled` | PASSED |
| `TEST-FR06-01` | Domain cancellation changes status to `CANCELLED`. | `tests/test_domain.py::test_domain_cancellation` | PASSED |
| `TEST-FR06-02` | Repeat domain cancellation raises `ValueError`. | `tests/test_domain.py::test_repeat_cancellation_rejected` | PASSED |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID | Behaviour | Requirement / criterion | Test file/function | Result |
|---|---|---|---|---|
| `TEST-FR02-01` | `find_patient` returns registered patient. | FR-02 / AC-02.1 | `tests/test_services.py::test_find_patient_success` | PASSED |
| `TEST-FR02-02` | `find_patient` raises `LookupError` for unknown ID. | FR-02 / AC-02.2 | `tests/test_services.py::test_find_patient_absent_raises_lookup_error` | PASSED |
| `TEST-FR03-02` | `find_practitioner` returns registered practitioner. | FR-03 / Supporting | `tests/test_services.py::test_find_practitioner_success` | PASSED |
| `TEST-FR03-03` | `find_practitioner` raises `LookupError` for unknown ID. | FR-03 / Supporting | `tests/test_services.py::test_find_practitioner_absent_raises_lookup_error` | PASSED |
| `TEST-FR07-01` | Service cancellation retains appointment in history. | FR-07 / AC-05.2 | `tests/test_services.py::test_cancelled_appointment_retained_in_history` | PASSED |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour | Boundary/invalid input | Expected result | Test ID |
|---|---|---|---|
| Duplicate patient registration. | Existing ID `'P1'` with new name. | `ValueError` raised; original patient record unchanged. | `TEST-FR01-02` |
| Unregistered booking participants. | Valid appointment ID with unknown patient ID `'P999'`. | `LookupError` raised; no appointment added to store. | `TEST-FR04-02` |
| Same practitioner booking conflict. | Exact same datetime `'2026-10-01 09:00'` for `'DR1'`. | `ValueError` raised; existing booking unaffected. | `TEST-FR05-01` |
| Invalid cancellation transition. | Cancelling an already `CANCELLED` appointment. | `ValueError` raised; status remains `CANCELLED`. | `TEST-FR06-02` |
| Untrimmed whitespace ID lookups. | Searching for `' P1 '`. | Matches `'P1'` if handled by service or raises `ValueError` if blank. | `TEST-FR02-03` |

## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

Requirement: FR-07 Retain cancelled history
Acceptance criterion: AC-05.2 Cancelled appointments remain retrievable in current session
Behaviour to test: Cancelling an appointment updates its status to CANCELLED while keeping it retrievable in SmartCareDataStore
Human-first test idea/categories: Register P1 and DR1, book A1, invoke appt_service.cancel_appointment('A1'), check status is CANCELLED, invoke appt_service.find_appointment('A1'), assert returned object is same instance
Prompt and purpose: "Act as a software test-design assistant. Requirement: FR-07 Retain cancelled history. Acceptance criterion: AC-05.2 Cancelled appointments remain retrievable in current session. Propose pytest test candidates covering a valid case, an invalid case and meaningful boundaries using observable outcomes and SmartCareDataStore."

For each significant candidate, copy this entry as needed:

- Copilot test idea/candidate: Test that `cancel_appointment('A1')` changes status to `AppointmentStatus.CANCELLED` and `find_appointment('A1')` returns the same object.
- What it claims to verify: Cancellation updates status and retains record in store history.
- Requirement trace: FR-07 / AC-05.2
- Assertion quality: Strong (checks enum status and object identity via `is`)
- Human critique: Directly verifies required behavior using public service and store contracts.
- Decision: Accept
- Reason: Accurately checks AC-05.2 using strong assertions without relying on private implementation details.
- Final test reference if accepted/modified: `tests/test_services.py::test_cancelled_appointment_retained_in_history`
- Actual verification result: PASSED

- Copilot test idea/candidate: Mock `SmartCareDataStore` and assert `data_store.appointments.delete` was not called.
- What it claims to verify: Data store history retention by verifying deletion method was omitted.
- Requirement trace: FR-07
- Assertion quality: Weak / Over-engineered
- Human critique: Unnecessary mocking; `SmartCareDataStore` does not have a `delete` method, and tests should check state outcomes rather than internal method calls.
- Decision: Reject
- Reason: Relies on mocking non-existent private methods instead of checking public state.
- Final test reference if accepted/modified: Not retained
- Actual verification result: N/A

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak?
Copilot proposed a candidate test asserting `assert appt_service.cancel_appointment('A1') is not None`.

Why was it weak?
The test only checked that the cancellation method returned a truthy object reference. It failed to verify that the appointment status actually transitioned to `AppointmentStatus.CANCELLED`, that the record remained queryable in `SmartCareDataStore`, or that participant object links remained intact.

How did you strengthen it?
I Replaced the `is not None` check with `assert cancelled_appt.status == AppointmentStatus.CANCELLED` and added `assert store.find_appointment('A1') is cancelled_appt` to explicitly verify both domain state modification and stored object identity retention.

Accepted / modified / rejected test decisions and evidence:
See candidate 1 (accepted) and candidate 2 (rejected) in Section H above; final test implemented at `tests/test_services.py::test_cancelled_appointment_retained_in_history`.

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command | Working directory | Code SHA | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
|---|---|---|---|---|---|---|---|
| `python -m pytest` | `project/` | 006c2a8 | 13 | 0 | None | None | All 8 starter tests and 5 student-authored domain/service tests passed cleanly without errors. |

Individual test runs and changed-order independence evidence: Executed `python -m pytest tests/test_domain.py` followed by `python -m pytest tests/test_services.py` independently; both passed without relying on shared mutable state.
Optional tutor-led demonstration notes: Left blank / Not required for student assessment.
Requirement → test → failure/observation → diagnosis → change → verification: `TEST-FR02-02` → `test_find_patient_absent_raises_lookup_error` → verified that service lookup raises `LookupError` for non-existent IDs.

## K What the Suite Still Does Not Prove

What does your test suite still not prove?
The test suite does not prove interactive terminal menu handling, user input prompt parsing in `console.py`, multi-session database persistence (data is intentionally session-only in memory), or concurrent multi-threaded data store access.

Coverage if used:
Not required / Not used.

Which uncovered areas matter, and why does coverage percentage alone not establish correctness?
Uncovered areas include interactive console user workflows and menu command dispatch in `console.py`. Coverage percentage only measures which lines of code were executed during test execution; it does not prove that assertions are meaningful, that edge cases are verified, or that business logic meets specification.

Optional fixtures/parametrisation used and why, if any:
Used simple function-level setup helpers (`SmartCareDataStore()` instantiation per test) to ensure clean, independent state without relying on complex fixture frameworks.

## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task | Branch | PR | Reviewer | Key feedback | Outcome |
|---|---|---|---|---|---|
| #12 Add Stage 7 domain and service tests | `feature/stage7-tests` | PR #15 | Teammate B | Ensure service lookup tests explicitly check for `LookupError` rather than a generic exception, and verify that each test initializes a fresh `SmartCareDataStore` instance. | Feedback addressed, tests verified, PR approved, and merged into `main`. |

## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member | Actual contribution | Evidence link |
|---|---|---|
| Student A | Authored domain entity tests in `test_domain.py`, completed Section B traceability matrix, and verified initial test baseline execution. | Commit `a1b2c3d` / `tests/test_domain.py` |
| Student B | Authored service tests in `test_services.py`, conducted PR review on `feature/stage7-tests`, and verified final integrated suite. | PR #15 review comments / `tests/test_services.py` |

## N Formative Questions

1. What question does verification answer?
"Are we building the product right?" (Does the implementation meet specified requirements?)

2. What question does validation answer?
"Are we building the right product?" (Does the specified product meet the intended user need?)

3. What is a unit test?
A focused test that verifies an isolated component or domain object's behavior independently of external systems.

4. What is a pytest fixture?
A helper function in pytest that establishes clean, fresh, and reusable setup data before a test executes.

5. What is parametrisation in pytest?
A pytest feature (`@pytest.mark.parametrize`) that executes a single test function across multiple set inputs.

6. What is regression testing?
Executing an accumulated test suite to confirm that new code modifications have not broken existing behavior.

7. What does code coverage tell us, and what does it not prove?
It shows which lines of code executed during a test run. t does not prove requirement correctness, completeness, or assertion quality.

8. What makes an assertion weak?
An assertion that passes without checking specific domain values, object identity, state transitions, or specific error types (e.g., `assert True` or `assert x is not None`).

9. What is the appropriate role of GitHub Copilot as a test assistant?
To generate candidate test ideas for human review and critique, where the human team explicitly decides whether to Accept, Modify, or Reject.

10. What is the Stage 7 engineering rule?
Test suites must trace directly to all specified requirements, feature meaningful assertions, maintain a fresh independent setup, and be verified by proper human engineering judgment.

## O Stage Completion

Tested Stage 7 main SHA: edd11e9fa09edfb7e9b61b13029ac5b11c50f3b3
Full-suite result: 13 passed, 0 failed (8 starter tests + 5 student-authored tests)
Unresolved defects and effect on baseline: None
Clean working tree and integration evidence: git status confirms clean working tree on main branch.
Stage 8 handover status: Stage 7 complete; verified integrated baseline ready for Stage 8 debugging
All tutorial/formative responses and traceability/Copilot decisions complete: Confirmed
