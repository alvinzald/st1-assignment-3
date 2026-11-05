# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage09/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Use the Stage 9 handout and Overview/revision 2 baseline. Keep responses concise and link accessible artefacts; do not paste entire logs or private peer ratings.

Group: <Wed 4:30-6:30>
Members and responsibilities: 
Noor Anwari (UG): [Stage 9 Implementation and testing]
Stage 8 integrated SHA: [1ababa89870941dfbee51f16b418e476ea8010bb] 
command: [python -m pytest]
working directory: [project/]
and actual result:[20 passed in 0.07s]

## A. Tutorial activities

### A1 Session state classification

| Information | Required session/domain or transient state? | Requirement or reason |
|---|---|---|
| Patient identity |session/domain state |Needed to register and find patients |
| Appointment history |Session/domain state |FR-07 requires cancelled appointments to remain accessible.|
| Temporary menu choice |Transient state |Only needed to decide which menu action to permit. |
| Practitioner specialty |Session/domain state |Part of the practitioner's registered information. |
| Debug print output |Transient state |Only used to investigate problems, not part of stored records. |
| Appointment status |Session/domain state |Needed to identify whether an appointment is scheduled, cancelled or completed |

What is intentionally lost on exit? 
[All registered patients, practitioners and appointments are lost when the program exits because the data is only stored in memory.]

### A2 Interface and domain data plan

Plan before AI. This replaces schema/key design; no database tables are required.

| Function or component | Explicit inputs and types | Outputs | Responsibility and validation | Domain source / existing constraint |
|---|---|---|---|---|
| appointment_sort_key |appointment: Appointment |tuple[datetime, str] |Provides a key for sorting without changing the appointment |Uses date_time and appointment_id |
| select_appointments |appointments list, practioner ID, optional status|list[Appointment] |Filters and sorts appointments without changing the original list |Uses existing practitioner ID, appointment status and sorting fields |
| Service listing |Practitioner ID, optional status |List of appointment objects |Validates the practitioner and uses the query function to return appointment |Uses registered practitioners and appointments from the datastore |
| Console |User input (str) and service objects |Displays messages; run_menu returns None |Shows menu, reads input, calls services and handles invalid entries |Uses existing services and appointment formatting fucntions |

Relate patient ID/name, practitioner ID/name/specialty, and appointment ID/actual participants/date_time/status to the existing contracts: [Patient stores the ID and name, while practitioner stores the ID, name and speciality. Appointment stores its ID, registered Patient and Practitioner objects, data_time and status. The domain classes and services handle validation, while the datastore keeps the records. Cancelled appointments remain available for history]

### A3 Responsibility violations

| Conceptual case | Violation | Correct boundary and reason |
|---|---|---|
| Appointment.cancel reads input |Domain class handles user input |The console should read input. Appointment should only handle cancellation rules and status. |
| Service prints/reads the menu |Service handles user interaction. |The console should display the menu and read choices. Services should handle business operations. |
| Query sorts its source in place |Changes the original list, so it is not pure. |Use sorted() to return a new list without changing the original |
| Store prints Appointment saved |Datastore handles output messages. |The datastore should return the appointment. The console should display the message. |

### A4 Sorting comparison

For `appointments.sort(key=appointment_sort_key)` and `result = sorted(appointments, key=appointment_sort_key)`, predict source order, return value and result identity. Give a meaningful mutation check: [appointments.sort() changes the original list and returns None. The result is the same list, not a new one. sorted(appointments) keeps the original list unchanged and returns a new sorted list.
To check mutation, we can copy the original list before sorting and compare it afterwards using assert appointments == original. We should also check that the returned list is a different object using assert result is not appointments.]

Score-example prediction and explanation of passing the named key: [For [('Bea', 8), ('Ali', 8), ('Chen', 5)], the sorted result is [('Chen', 5), ('Ali', 8), ('Bea', 8)].
The scores are sorted from lowest to highest. When scores are equal, names are sorted alphabetically. We use key=score_key without brackets because we are passing the function itself to sorted(). Writing score_key() would call the function immediately instead.]

### A5 Exit question

Explain cancellation versus deletion, and checks for same-session lookup, all-status listing and SCHEDULED-only exclusion:
 [Cancellation changes the appointment status to CANCELLED instead of deleting it, so the appointment history is kept. We can check this by finding the cancelled appointment using its ID in the same session. An all-status listing should include the cancelled appointment, while a SCHEDULED-only listing should exclude it because it is no longer scheduled.]

## B. Human design and contracts

Complete before GitHub Copilot. Record any interface/integrity decision and its reasoning: [We will use the existing domain classes and datastore without adding new fields. The query functions will filter appointments by practitioner ID and optional status, then sort by date/time and appointment ID without changing the original list. The service will validate the practitioner and status, while the console will handle user input and display results. Cancelled appointments will remain availbale for history.]

| Requirement | Input / session data | Operation and responsible component | Expected result or error | Test / evidence |
|---|---|---|---|---|
|QRY-01 |Appointments, practitioner ID |select_appontments() in queries.py |Only appointments for the requested practitioner |Test with two practitioners |
|QRY-02 |Appointments, AppointmentStatus or None |select_appontments() |None returns all statuses; explicit status returns matching appointments |Test each status and no matches |
|QRY-03 |Appointment date/time & ID |appointment_sort_key() & select_appointments() |Sorted by date/time, then appointment ID |Test equal times and unchanged source |
|FP-01 |Same appointments & filters |Pure query functions |Repeated calls return the same results without side effects |Repeat query and compare results |
|FP-02 |Empty, sorted & unsorted lists |select_appointments() |Returns a new list without changing the source |Check list identity and original order |
|FP-03 |appointment object |appointment_sort_key() |Returns (date_time,appointment_id) |Test the key directly and its use in sorting |
|Practitioner listing |Practitioner ID & optional status |AppointmentService.list.practioner_appointments()|Ordered list; unknown practitioner raises LookupError; invalid status raises ValueError |Service tests |
|Interactive menu |User input and shared services | run_menu() in console.py |Register, find,book,cancel, and list; repeat until exit |Workflow tests and manual testing |

Cover QRY-01–04, FP-01–03, UI-01–02 and relevant FR-01–09. Explain empty versus unknown versus invalid, enum conversion, actual object identity, error handling and unchanged state on rejection: 
[QRY-01–04 will test filtering, sorting and validation. FP-01–03 will check purity, new lists and the sorting key. UI-01–02 and FR-01–09 will cover registration, lookup, booking, cancellation, history, listing and error handling.
No matches return an empty list, unknown IDs raise LookupError, and invalid inputs raise ValueError. The console converts status input to an enum. Appointments use the actual registered objects, and rejected operations must not change existing data.]

## C. Implementation and query verification

| Requirement / test ID | Code location | Case and meaningful assertion | Actual result | Evidence link |
|---|---|---|---|---|
|QRY-01 |queries.py, test_queries.py |Checks that only appointments for the requested practitioner are returned. |Passed |(project/tests/test_queries.py) |
|QRY-02 |queries.py, test_queries.py |Checks status filtering, all statuses and no matching appointments.|Passed |(project/tests/test_queries.py)|
|QRY-03 |queries.py, test_queries.py |Checks sorting by date/time and appointment ID without changing the original list.|Passed |(project/tests/test_queries.py)|
|QRY-04 |queries.py, test_queries.py |Checks empty results, unknown practitioners and invalid inputs.|Passed |(project/tests/test_queries.py) |
|FP-01 |queries.py, test_queries.py |Checks that repeated queries give the same result without changing the original data.|Passed |(project/tests/test_queries.py) |
|FP-02 |queries.py, test_queries.py |Checks that a new list is returned for empty, sorted and unsorted inputs. |Passed |(project/tests/test_queries.py) |
|FP-03 |queries.py, test_queries.py |Checks that the named sorting key is used.|Passed |(project/tests/test_queries.py) |
|History|services.py, test_queries.py |Checks that cancelled appointments remain in the history.|Passed |(project/tests/test_queries.py) |
Include practitioner isolation, every enum status/default all, equal-time ID tie-break, named-key reuse, repeated calls, empty/already-sorted fresh lists, unchanged source order/fields, known-empty/unknown/invalid service cases and retained history.

Purity explanation from code inspection, including absence of hidden state and I/O: 
[The select_appointments() function only uses the inputs provided to it. It filters appointments by practitioner ID and status, then sorts them using appointment_sort_key(). It uses sorted() to return a new list without changing the original list. The function does not access the data store, use global variables, print anything or ask for user input.]

What the tests do and do not establish: 
[The tests check that appointments are filtered and sorted correctly, a new list is returned, and the original data is not changed. They also check invalid inputs, empty results and cancelled appointment history. However, passing these tests does not mean the whole system is working correctly. The tests only cover the cases we tested. The console menu and complete user workflow still need to be tested.]

## D. Integrated console and workflow evidence

| Scenario / acceptance ID | Reproducible inputs / artefact | Expected result | Observed result and state check | Evidence link |
|---|---|---|---|---|
| UI-01 full menu workflow |Run python main.py --interactive. Register and find patient and practitioners, book appointments, cancel, retrieve, list and filter appointments, then exit. |The menu should complete all operations, reject booking conflicts, keep cancelled history and allow a new booking in a freed slot. |Registration, lookup, booking, cancellation, retrieval and filtering worked. Cancelled appointments remained in history, and a new booking in the freed slot succeeded. |[console testing evidence](stage09/console_test_evidence.txt)|
| UI-02 invalid-input recovery |Enter invalid IDs, duplicate IDs, invalid date, repeated cancellation and menu choice 99. |nvalid inputs should show an error without crashing or changing existing records. The menu should continue working. |Tested invalid dates, duplicate IDs, repeated cancellation and unknown menu choice. Errors were displayed and the menu continued. An invalid booking ID was not saved |[console testing evidence](stage09/console_test_evidence.txt)|
| Automated service workflow |tests/test_workflows.py and python -m pytest -q |Verify booking, conflict rejection, cancellation history, freed slots and practitioner filtering. |All 37 tests passed. Rejected bookings did not add records, cancelled appointments remained available, and filtering returned the correct appointments. |[workflow tests](project/tests/test_workflows.py) |

Include registration/find, booking, conflict rejection, different-practitioner booking, cancellation, retrieval, listing/filtering, freed slot and exit; duplicate/unknown/blank IDs, malformed/impossible date, invalid status, unknown choice and repeated cancellation. Identify before/after state and subsequent successful action.

## E. GitHub Copilot review and human decisions

Human design completed before AI: <Section A (A1–A5) of this evidence file.>
Actual prompt/context supplied: <GitHub Copilot reviewed Stage 9 queries, services,
console and tests using the required review prompt>
Actual response: [GitHub Copilot review](stage09/copilot_review.txt)

| AI finding | Code/test evidence | Severity | Accept/Modify/Reject and reason | Change or no change | Actual verification |
|---|---|---|---|---|---|
|No automated console tests |console.py,test_workflows.py,console_test_evidence.txt |Important |Modify - Manual console testing is allowed by the assignment. However, the evidence should also include an impossible date |No new automated test required. Check and complete manual evidence if needed |UI-01 and UI-02 were manually tested, including malformed and impossible dates. The console displayed errors and continued running. All 37 automated tests passed. |
|Query does not validate status directly |queries.py, services.py, test_queries.py |Optional |Reject - The service already validates the status before calling the query. |No change |Invalid status is rejected by the service and tested. |
|Returned objects can be modified |data_store.py, domain.py |Optional |Reject - The requirements do not ask for immutable objects |No change |Existing tests passed. No domain changes were needed. |

Responsibility check: explain how domain invariants, shared-store collections, service coordination, pure queries and console effects remain separate: 
[The responsibilities are separated in SmartCare. The domain classes manage rules such as preventing repeated cancellation. The data store keeps patients, practitioners and appointments in shared collections. The services handle operations such as booking, cancellation and validation. The query functions filter and sort appointments without changing the original data. The console handles user input, displays results and shows error messages. This keeps each part focused on its own responsibility.]

## F. Required reflections

1. Which integration concern was architectural rather than a filtering/sorting detail? <!-- response -->
2. Which Copilot suggestion did you reject as over-engineering, and why? <!-- response -->
3. How did you prove cancelled appointments remain retrievable and listable in the same session? <!-- response -->

## G. Ten formative answers

1. What makes select_appointments pure, and what side effect breaks purity? <!-- response -->
2. Which explicit inputs are needed, and why avoid a global store? <!-- response -->
3. How can a new list reuse Appointment objects safely? <!-- response -->
4. Why use a named key, and what breaks equal-time ties? <!-- response -->
5. How do default and explicit status filters differ? <!-- response -->
6. How do empty, unknown practitioner and invalid filter cases differ? <!-- response -->
7. Which console errors recover, and how is unchanged state checked? <!-- response -->
8. What is data integrity for registered participants, conflicts and history? <!-- response -->
9. What is Copilot's review role, and who verifies findings? <!-- response -->
10. How do pure functions and OOP responsibilities work together? <!-- response -->

## H. Review, completion and common handover

Issues and bounded branches: <!-- links -->
PR/diff and another-member human reviewer: <!-- actual links/name -->
Review responses and Copilot comparison: <!-- links -->
Integrated common Stage 9 SHA: <!-- complete -->
Full regression command, working directory, actual count/result and evidence: <!-- complete -->
README run instructions and scope/limitations: <!-- link -->
Unresolved issues and support/action: <!-- complete -->
UG common candidate / PG future branch plan: <!-- complete -->

- [ ] Query contracts, purity, new lists and named-key ordering verified.
- [ ] Service empty/unknown/invalid cases and cancellation history verified.
- [ ] Every console command and invalid-input recovery demonstrated.
- [ ] Query and workflow tests plus all previous tests pass; actual evidence linked.
- [ ] Human design, Copilot critique, review and integration recorded honestly.
- [ ] Reflections and ten formative responses completed.
- [ ] README updated; earlier code/tests/records preserved.
- [ ] Common SHA protected for UG Stage 12; PG Stage 10/11 work deferred until approved.

No persistence, rescheduling or assurance implementation is part of Stage 9. UG: 6→7→8→9→12. PG: 6→7→8→9→10→11→12. Mixed groups keep one repository and protect the common candidate.
