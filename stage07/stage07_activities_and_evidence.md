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
| **Blank identifiers:** Passing `""` or `"   "` as a `patient_id` or `practitioner_id`[cite: 28]. | `ValueError` raised[cite: 28]. | `domain.py` `required_text` helper requires non-blank string input after trimming whitespace[cite: 28]. |
| **Whitespace-only names:** Passing `"   "` as a patient or practitioner `name`[cite: 28]. | `ValueError` raised[cite: 28]. | `domain.py` entity constructors reject empty or whitespace-only text[cite: 28]. |
| **Same-time practitioner bookings:** Booking same practitioner at exact same time `2026-10-01 09:00` vs. different practitioner at `2026-10-01 09:00`[cite: 30, 34]. | Same practitioner raises `ValueError`; different practitioner succeeds[cite: 30, 34]. | `SmartCareDataStore.has_practitioner_conflict` checks practitioner ID and exact datetime matching[cite: 30]. |
| **Cancelled appointments:** Calling `cancel()` on an appointment already in `CANCELLED` status[cite: 28, 34]. | `ValueError` raised; status remains `CANCELLED`[cite: 28, 34]. | `Appointment.cancel()` method protects its domain transition guard[cite: 28]. |
| **Invalid status transitions:** Attempting to transition from `COMPLETED` or `CANCELLED` back to `SCHEDULED`[cite: 28]. | `ValueError` raised[cite: 28]. | `Appointment.cancel()` protects status properties and restricts illegal transitions[cite: 28]. |

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
| **FR-01** | **AC-01.1** | `TEST-FR01-01` | Positive | `test_registration_and_booking` in `test_starter.py` | Valid patient ID and name stored in data store[cite: 28, 30, 42]. | PASSED | Supplied[cite: 34] |
| **FR-01** | **AC-01.2** | `TEST-FR01-02` | Negative | `test_duplicate_patient_preserves_original` in `test_starter.py` | Duplicate patient ID registration rejected with `ValueError`[cite: 30, 34]. | PASSED | Supplied[cite: 34] |
| **FR-01** | Revision 2 validation contract | `TEST-FR01-03` | Negative | `test_blank_patient_id_rejected` in `test_domain.py` | Blank/whitespace patient ID raises `ValueError`[cite: 28, 34, 42]. | PASSED | Student-authored[cite: 42] |
| **FR-02** | **AC-02.1** | `TEST-FR02-01` | Positive | `test_find_patient_success` in `test_services.py` | Known patient lookup returns stored `Patient` object[cite: 30, 31, 42]. | PASSED | Student-authored[cite: 42] |
| **FR-02** | **AC-02.2** | `TEST-FR02-02` | Negative | `test_find_patient_absent_raises_lookup_error` in `test_services.py` | Valid unknown patient ID raises `LookupError`[cite: 31, 42]. | PASSED | Student-authored[cite: 42] |
| **FR-04** | **AC-03.1** | `TEST-FR04-01` | Positive | `test_registration_and_booking` in `test_starter.py` | Valid participants create stored `SCHEDULED` appointment[cite: 28, 30, 34]. | PASSED | Supplied[cite: 34] |
| **FR-04** | **AC-03.2** | `TEST-FR04-02` | Negative | `test_unregistered_participants_rejected` in `test_starter.py` | Booking with unregistered participant raises `LookupError`/`ValueError`[cite: 31, 34]. | PASSED | Supplied[cite: 34] |
| **FR-05** | **AC-04.1** | `TEST-FR05-01` | Negative | `test_conflict_rule_and_different_practitioner` in `test_starter.py` | Same practitioner at exact same time raises `ValueError`[cite: 30, 34]. | PASSED | Supplied[cite: 34] |
| **FR-05** | **AC-04.2** | `TEST-FR05-02` | Positive | `test_conflict_rule_and_different_practitioner` in `test_starter.py` | Different practitioner at same time is permitted[cite: 30, 34]. | PASSED | Supplied[cite: 34] |
| **FR-06** | **AC-05.1** | `TEST-FR06-01` | Positive | `test_domain_cancellation_and_guard` in `test_starter.py` | Cancelling scheduled appointment changes status to `CANCELLED`[cite: 28, 34]. | PASSED | Supplied[cite: 34] |
| **FR-06** | **AC-05.3** | `TEST-FR06-02` | Negative | `test_repeat_cancellation_rejected` in `test_domain.py` | Cancelling an already cancelled appointment raises `ValueError`[cite: 28, 42]. | PASSED | Student-authored[cite: 42] |
| **FR-07** | **AC-05.2** | `TEST-FR07-01` | Positive | `test_cancelled_appointment_retained_in_history` in `test_services.py` | Cancelled appointment remains retrievable in data store history[cite: 28, 30, 42]. | PASSED | Student-authored[cite: 42] |

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
|---|---|---|---|---|---|---|
| `TEST-FR01-03` | FR-01 | Revision 2 validation contract | Negative | Verify constructor validation for blank patient ID[cite: 28, 42]. | `ValueError` raised when initializing `Patient("", "Alex")`[cite: 28, 34]. | Checks core domain entity guard independently of service orchestration[cite: 28, 42]. |
| `TEST-FR02-01` | FR-02 | AC-02.1 | Positive | Verify patient lookup workflow via service layer[cite: 31, 42]. | `find_patient('P1')` returns the registered `Patient` object[cite: 31]. | Verifies Stage 6 service lookup completion[cite: 31, 42]. |
| `TEST-FR02-02` | FR-02 | AC-02.2 | Negative | Verify service lookup error handling for absent patient[cite: 31, 42]. | `find_patient('P999')` raises `LookupError`[cite: 31]. | Confirms service lookup raises `LookupError` rather than returning `None`[cite: 31]. |
| `TEST-FR06-02` | FR-06 | AC-05.3 | Negative | Verify domain cancellation guard against repeated execution[cite: 28, 42]. | Second call to `cancel()` raises `ValueError`[cite: 28]. | Proves domain entity protects invalid status transition invariants[cite: 28, 42]. |
| `TEST-FR07-01` | FR-07 | AC-05.2 | Positive | Verify cancelled appointment history retention in store[cite: 28, 30, 42]. | `find_appointment('A1')` returns object with status `CANCELLED`[cite: 28, 30]. | Proves cancellation does not purge records from `SmartCareDataStore`[cite: 28, 30, 42]. |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
|---|---|---|---|---|
| `TEST-FR01-03` | None required (direct constructor invocation)[cite: 42]. | Call `Patient("", "Alex Example")`[cite: 28, 34]. | `with pytest.raises(ValueError):`[cite: 34, 42] | Directly verifies that invalid entity creation is blocked at the domain boundary[cite: 28, 42]. |
| `TEST-FR02-01` | Instantiate store and `PatientService`; register patient `'P1'`[cite: 30, 31, 42]. | Call `patient_service.find_patient('P1')`[cite: 31]. | `assert result.patient_id == 'P1'`[cite: 28, 42] | Verifies that registered patient records are retrievable by ID via the service lookup[cite: 31, 42]. |
| `TEST-FR02-02` | Instantiate store and `PatientService`[cite: 30, 31, 42]. | Call `patient_service.find_patient('UNKNOWN')`[cite: 31]. | `with pytest.raises(LookupError):`[cite: 31, 42] | Proves the service contract raises `LookupError` rather than returning `None` for absent IDs[cite: 31, 42]. |
| `TEST-FR06-02` | Create `SCHEDULED` appointment `'A1'`; invoke `appt.cancel()`[cite: 28, 42]. | Invoke `appt.cancel()` a second time[cite: 28, 42]. | `with pytest.raises(ValueError):`[cite: 28, 42] | Proves state transition guards prevent illegal duplicate cancellation[cite: 28, 42]. |
| `TEST-FR07-01` | Register `P1` and `DR1`; book `A1`; invoke `cancel_appointment('A1')`[cite: 28, 30, 42]. | Call `appt_service.find_appointment('A1')`[cite: 30, 31]. | `assert appt.status == AppointmentStatus.CANCELLED`[cite: 28, 42] | Proves historical records remain intact and retrievable after status transition[cite: 28, 30, 42]. |

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

| Test ID | Behaviour | Test file/function | Result |
|---|---|---|---|
| `TEST-FR01-03` | Blank patient ID raises `ValueError`[cite: 28, 34]. | `tests/test_domain.py::test_blank_patient_id_rejected`[cite: 34, 42] | PASSED[cite: 42] |
| `TEST-FR03-01` | Blank practitioner specialty raises `ValueError`[cite: 28, 34]. | `tests/test_domain.py::test_blank_practitioner_specialty_rejected`[cite: 34, 42] | PASSED[cite: 42] |
| `TEST-FR04-03` | New appointment defaults to `SCHEDULED` status[cite: 28, 34]. | `tests/test_domain.py::test_new_appointment_is_scheduled`[cite: 34, 42] | PASSED[cite: 42] |
| `TEST-FR06-01` | Domain cancellation changes status to `CANCELLED`[cite: 28, 34]. | `tests/test_domain.py::test_domain_cancellation`[cite: 34, 42] | PASSED[cite: 42] |
| `TEST-FR06-02` | Repeat domain cancellation raises `ValueError`[cite: 28, 42]. | `tests/test_domain.py::test_repeat_cancellation_rejected`[cite: 42] | PASSED[cite: 42] |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID | Behaviour | Requirement / criterion | Test file/function | Result |
|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour | Boundary/invalid input | Expected result | Test ID |
|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] |

## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

Requirement: [complete]
Acceptance criterion: [quote]
Behaviour to test: [complete]
Human-first test idea/categories: [complete]
Prompt and purpose: [complete or link]

For each significant candidate, copy this entry as needed:
- Copilot test idea/candidate: [complete]
- What it claims to verify: [complete]
- Requirement trace: [complete]
- Assertion quality: [complete]
- Human critique: [complete]
- Decision: [Accept / Modify / Reject]
- Reason: [complete]
- Final test reference if accepted/modified: [link or not retained]
- Actual verification result: [complete; do not claim an unrun test passed]

Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak? [response]
Why was it weak? [response]
How did you strengthen it? [response]
Accepted / modified / rejected test decisions and evidence: [link actual decisions in H]

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command | Working directory | Code SHA | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
|---|---|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

Individual test runs and changed-order independence evidence: [commands, results, links]
Optional tutor-led demonstration notes: [optional; leave blank if not used]
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: [concise links where applicable]

## K What the Suite Still Does Not Prove

What does your test suite still not prove? [response]
Coverage if used: [result or not used]
Which uncovered areas matter, and why does coverage percentage alone not establish correctness? [response]
Optional fixtures/parametrisation used and why, if any: [response or not used]

## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task | Branch | PR | Reviewer | Key feedback | Outcome |
|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member | Actual contribution | Evidence link |
|---|---|---|
| [complete] | [complete] | [complete] |

## N Formative Questions

1. What question does verification answer?
[response]

2. What question does validation answer?
[response]

3. What is a unit test?
[response]

4. What is a pytest fixture?
[response]

5. What is parametrisation in pytest?
[response]

6. What is regression testing?
[response]

7. What does code coverage tell us, and what does it not prove?
[response]

8. What makes an assertion weak?
[response]

9. What is the appropriate role of GitHub Copilot as a test assistant?
[response]

10. What is the Stage 7 engineering rule?
[response]

## O Stage Completion

Tested Stage 7 main SHA: [complete]
Full-suite result: [complete]
Unresolved defects and effect on baseline: [complete or none]
Clean working tree and integration evidence: [complete]
Stage 8 handover status: [complete; no Stage 8 work assigned]
All tutorial/formative responses and traceability/Copilot decisions complete: [confirm]
