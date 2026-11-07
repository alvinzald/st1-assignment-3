# Stage 10 PG agentic rescheduling activities and evidence

PG-only stage. Undergraduate students are not required to complete this record. UG-only groups retain this supplied template unchanged as intentionally not applicable; do not fabricate N/A responses. Optional UG help is voluntary and unassessed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage10_pg/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Protect the common Stage 9 SHA and UG Stage 12 pathway.

This is a blank student record. Use actual accessible links and concise evidence; do not invent an agent session, test result or approval. Retain this record's headings when linking equivalent issue/PR evidence.

Group/tutorial: [Wed 4:30-6:30]
Assessed PG members and roles: [Alvin Zaldivar]
Optional UG contributors: [none]

## A Access baseline and recovery

- Confirmed GitHub Copilot feature/mode, version/environment and teaching-team approval reference: [GitHub Copilot coding assistant/Auto mode (model selected dynamically), version 1.0.103/Windows, [Approval Reference at 35:00](https://uclearn.canberra.edu.au/courses/20399/external_tools/197)]
- Actual account access and tool permissions check: [response]
- Live route or convenor-confirmed equivalent staged interaction: [response]
- Access limitation and tutor resolution if applicable: [response]
- Protected Stage 9 common SHA / recoverable reference: [299607323d5258b6c5a1c1af86cd94726abe7e16]
- Common baseline command / project working directory / actual result: [python -m pytest / st1-assignment-3/project / All 37 tests passed with no failures]
- Clean branch and preparer / recovery baseline: [Alvin Zaldivar]
- Evidence-only later SHA if different / explanation: [response]

## B Tutorial activities

### B1 Rewrite the vague task

“Improve SmartCare appointment scheduling.” Write your bounded goal, requirements, exclusions, constraints, acceptance criteria and Definition of Done:
- [Add appointment rescheduling feature which which will let an existing `SCHEDULED` appointment to move to another valid date and time]
- [The feature must preserve the original appointment object, ID, patient and practitioner. It must reject invalid IDs, invalid dates and times, conflicting practitioner schedules and attempts to reschedule `CANCELLED` or `COMPLETED` appointments. Failed attempts must leave existing records unchanged.]
- [The implementation should follow the current domain and service structure, reuse the existing conflict-checking logic and datetime validation, and keep the changes limited to rescheduling. Database redesign, notifications, external libraries, unrelated features and changes to cancellation behaviour are excluded.]
- [The feature is complete when successful and rejected rescheduling scenarios behave as required, lookup and listing reflect the updated time, and all new and existing tests pass. The changes must also pass human code review before integration.]
Predicted changed files and human test intentions:
- [[domain.py](../project/smartcare/domain.py) — Add the rescheduling method and its validation.]
- [[services.py](..project/smartcare/services.py) — Handle appointment lookup, conflict checks and rescheduling.]
- [[test_rescheduling.py](..project/tests/test_rescheduling.py) — Add positive, negative and boundary tests.]
- [[README.md](../README.md) — Document the PG rescheduling feature.]

### B2 Judge every proposed plan step

| Proposed step | Accept / Modify / Reject | Requirement evidence and reason |
|---|---|---|
| Redesign database schema | [Reject] | [RES-05-R2 / SmartCare uses an in-memory data store, a database redesign is unnecessary and outside the scope of Stage 10.] |
| Add notifications | [Reject] | [RES-01~06 / Notifications are not included in requirements, adding them would introduce unrelated functionality and increase the scope of the implementation.] |
| Introduce calendar library | [Reject] | [An external calendar library is unnecessary and explicitly excluded under Section 3's out-of-scope requirements.] |
| Modify Patient | [Reject] | [RES-02/ Existing patient and practitioner identities to remain unchanged. Rescheduling should not require modifications to the Patient class.] |
| Add rescheduling | [Accept] | [RES-01 / Requires rescheduling.] |
| Rewrite all tests | [Reject] | [RES-01~06 / Meaningful tests are required to verify rescheduling behaviour, but don't require rewriting existing tests. Previous tests to be preserved so regressions can still be detected. New tests should be added in [test_rescheduling.py](..project/tests/test_rescheduling.py) instead.] |

### B3 Six proposed changes

| File or action | Expected? | Review concern and evidence needed |
|---|---|---|
| Appointment in project/smartcare/domain.py | [Yes] | [RES-01 / Check that rescheduling validates the appointment state and new datetime.] |
| project/smartcare/services.py | [Yes] | [RES-04 / Verify if conflicts are checked before changing the appointment time.] |
| Proposed sqlite_repository.py / schema change | [No] | [RES-05-R2 / Only current-session visibility is required. Check that no unnecessary persistence is introduced.] |
| Patient fields in project/smartcare/domain.py | [No] | [RES-02 / Patient identity must remain unchanged. Check that no unrelated fields are modified.] |
| requirements-dev.txt adds calendar package | [No] | [RES-01 / Existing datetime handling should be sufficient. Check that no unnecessary dependency is added.] |
| Existing appointment assertions weakened | [No] | [RES-01–06 / Check that tests still verify the required behaviour rather than simply passing.] |

### B4 Approval gate

Agent says “All tests pass.” Give at least SIX distinct checks before approval.
1. [Verify that scheduled appointments can be moved to a valid, available time (RES-01).]
2. [Confirm that the original appointment object, ID and participants remain unchanged (RES-02).]
3. [Check that invalid and unknown appointment IDs are rejected with the correct errors (RES-03).]
4. [Verify that scheduling conflicts are rejected while allowing different practitioners at the same time (RES-04).]
5. [Confirm that lookup and listing reflect the updated appointment time (RES-05-R2).]
6. [Verify that CANCELLED and COMPLETED appointments cannot be rescheduled (RES-06).]

Additional checks if useful: 
- [Review the code and check code diff for unexpected changes.]
- [Run the focused and existing test suites.]
- [Confirm that failed operations leave records unchanged.]

### B5 Exit question

Why does increasing AI autonomy increase rather than decrease the importance of software engineering discipline? [It can make more changes with less human oversight which increases the risk of errors. Software engineering practices help ensure changes meet requirements, properly reviewed, and tested before approval.]

## C Human task specification before AI

- Goal: [Implement appointment rescheduling so that an existing scheduled appointment can be moved to another valid, available time.]
- Requirements RES-01–06 with RES-05-R2:
  - [RES-01: Reschedule a known `SCHEDULED` appointment to a valid free time]
  - [RES-02: Keep the existing appointment object, ID, patient and practitioner identities; only time changes. The service returns that same object.]
  - [RES-03: A valid unknown appointment ID raises `LookupError`. Invalid/blank IDs raise ValueError under the existing ID contract.]
  - [RES-04: Reject another SCHEDULED appointment for the same practitioner at the exact new datetime with ValueError. Exclude the target appointment itself; another practitioner is allowed.]
  - [RES-05-R2: Updated time is visible through subsequent lookup and listing in this session, with current sorting. This replaces the original persistence requirement.]
  - [RES-06: CANCELLED and COMPLETED targets raise ValueError without mutation, even for a same-time request.]
- Out of scope:
  - [Database redesign]
  - [Notifications]
  - [External calendar libraries]
  - [Authentication changes]
  - [Recurring appointments]
  - [Unrelated features]
- Architecture constraints:
  - [Follow the existing domain and service structure]
  - [Reuse datetime validation and the `has_practitioner_conflict` helper]
  - [Keep the in-memory data store and existing behaviour unchanged]
- Acceptance criteria:
  - [x] [RES-01–06 with RES-05-R2 must be satisfied]
  - [x] [Successful rescheduling]
  - [x] [Identity preservation]
  - [x] [Correct error handling]
  - [x] [Conflict rejection]
  - [x] [Current-session visibility]
  - [x] [Unchanged state after failed operations]
- Definition of Done:
  - [x] [Rescheduling works as required]
  - [x] [New and existing tests pass]
  - [x] [All changes remain within scopes]
  - [x] [The implementation has been reviewed and approveds]
- Issue / PG owner: [Implement Guarded Appointment Rescheduling / Alvin Zaldivar]
- Human expected positive, negative and boundary tests:
  - [Valid rescheduling: Confirm that a `SCHEDULED` appointment can move to an available date and time]
  - [Preserved identities: Verify that the appointment object, ID, patient and practitioner remain unchanged]
  - [Invalid or unknown IDs: Check that blank or invalid IDs raise `ValueError` and unknown valid IDs raise `LookupError`]
  - [Scheduling conflicts: Verify that another SCHEDULED appointment for the same practitioner and time is rejected]
  - [Different practitioners: Confirm that appointments for different practitioners can share the same time]
  - [Invalid appointment states: Check that `CANCELLED` and `COMPLETED` appointments cannot be rescheduled]
  - [Invalid dates and times: Verify that incorrect types, timezone-aware dates and times and nonzero seconds or microseconds are rejected]
  - [Same-time requests: Confirm that rescheduling a `SCHEDULED` appointment to its existing time is allowed without changes]
  - [Old-slot reuse: Verify that another appointment can use the original time after a successful move]
  - [State preservation: Confirm that rejected rescheduling attempts leave appointment details and stored records unchanged]
  - [Lookup and listing: Verify that the new appointment time appears in subsequent lookup and correctly sorted listing results]
- Allowed files:
  - [[domain.py](../project/smartcare/domain.py)]
  - [[services.py](..project/smartcare/services.py)]
  - [[test_rescheduling.py](..project/tests/test_rescheduling.py) ]
  - [[README.md](../README.md)]
  - [[stage10_activities_and_evidence.md](stage10_activities_and_evidence.md)]
- Forbidden/unnecessary files and changes:
  - [Database and schema changes]
  - [New external dependencies]
  - [Unrelated participant modifications]
  - [Weakened existing tests]
  - [Changes to cancellation/history behaviour]
- Baseline/recovery link: [299607323d5258b6c5a1c1af86cd94726abe7e16]
- Evidence that human analysis preceded agent use: [9152380aca380a64a66431c00fb532694c856bda]

## D Agent plan and approval

Actual plan-only prompt/context and response or confirmed equivalent artefacts: [[prompt](evidence/copilot_plan_prompt.md)] [[response](https://github.com/alvinzald/st1-assignment-3/issues/12#issuecomment-6704660853)]

| Plan step / action | Requirement link | Reason | Expected files | Accept / Modify / Reject | Conditions / evidence |
|---|---|---|---|---|---|
| [Add a guarded domain reschedule operation] | [RES-01, RES-02, RES-06] | [Reuse datetime validation; only scheduled appointments can move, and failed attempts must preserve state and identities.] | [project\smartcare\domain.py] | [Accept] | [Only the appointment time should change and rejected operations must not mutate state.] |
| [Add service-level rescheduling] | [RES-01, RES-03, RES-04, RES-06] | [Handle lookup and conflict checking before updating the appointment.] | [services.py] | [Accept] | [Reuse the existing conflict helper and exclude the target appointment.] |
| [Add focused rescheduling tests] | [RES-01–06, RES-05-R2] | [Verify the requirements without weakening existing tests.] | [test_rescheduling.py] | [Accept] | [Cover positive, negative and boundary cases, then run focused and full test suites.] |

Approved bounded scope / forbidden changes / verification plan:
  - [Proposed scope is limited to rescheduling methods and focused tests.]
  - [No database changes, external dependencies, unrelated features or modifications to existing tests.]
  - [Verification will include focused rescheduling tests, existing regression tests and the full suite.]
Human plan approver and approval before edits: [[Approval](https://github.com/alvinzald/st1-assignment-3/issues/12#issuecomment-6704696945)]
Tool permissions and any expanded-scope requests / decision: [Plan mode was used with "Allow All" disabled. Copilot reported no file edits or command execution during planning. No expanded-scope requests were reported.]

## E Production diff review

Actual proposal / branch diff / version reviewed: [links]

| File | Change purpose and reason | Requirement / test link | Expected? | Architecture OK? | Decision | Notes / correction |
|---|---|---|---|---|---|---|
| [domain.py] | [Added guarded rescheduling with datetime and status validation.] | [RES-01, RES-02, RES-06] | [Yes] | [Yes] | [Modify] | [Corrected the parameter name from date_time to new_date_time to match the required interface.] |
| [services.py] | [Added appointment lookup, conflict checking and rescheduling coordination.] | [RES-01, RES-03, RES-04, RES-06] | [Yes] | [Yes] | [Modify] | [Corrected the parameter name to new_date_time. Existing conflict helper is reused.] |

Every changed file inspected, including new/untracked files: [evidence]
Unexpected changes, scope creep, secrets/dependencies/configuration, unrelated cleanup: [No unexpected changes or unrelated functionality identified in the reviewed code. No new dependencies or configuration changes observed.]

## F Separate test review

| Test | Criterion | Actual assertion | Assertion meaningful / adequate? | Agent changed expected behaviour? | Human or agent authorship | Decision and reason |
|---|---|---|---|---|---|---|
| [test_reschedule_preserves_identity_and_updates_session_views] | [RES-01, RES-02, RES-05-R2] | [Checks object identity, updated time, listing order and old-slot reuse.] | [Yes] | [No] | [Copilot] | [Accept: because it covers successful rescheduling and related requirements.] |
| [test_reschedule_allows_same_time_no_op] | [RES-01, RES-04] | [Checks that the same appointment and time are retained.] | [Yes] | [No] | [Copilot] | [Accept: because it verifies the permitted no-op behaviour.] |
| [test_reschedule_methods_accept_new_date_time_keyword] | [RES-01, RES-02] | [Checks that both methods accept new_date_time and update the same object.] | [Yes] | [No] | [Copilot, revised with human feedback] | [Accept: after it uses the required method signatures.] |
| [test_reschedule_rejects_unknown_and_invalid_ids_without_mutation] | [RES-03] | [Checks the correct exceptions and unchanged stored records.] | [Yes] | [No] | [Copilot] | [Accept: since it covers invalid and unknown IDs.] |
| [test_invalid_reschedule_time_does_not_mutate_state] | [RES-01, RES-06 datetime contract] | [Checks invalid datetime rejection and unchanged records at both domain and service levels.] | [Yes] | [No] | [Copilot] | [Accept: since it covers datetime validation at both levels.] |
| [test_reschedule_rejects_scheduled_practitioner_conflict_without_mutation] | [RES-04] | [Checks conflict rejection and unchanged appointments.] | [Yes] | [No] | [Copilot] | [Accept: since it confirms conflicting appointments are rejected.] |
| [test_reschedule_allows_other_practitioner_and_inactive_slot_occupants] | [RES-04] | [Checks that different practitioners and inactive appointments do not prevent rescheduling.] | [Yes] | [No] | [Copilot] | [Accept: because it confirms correct conflict handling.] |
| [test_non_scheduled_appointment_cannot_be_rescheduled] | [RES-06] | [Checks rejection of `CANCELLED` and `COMPLETED` appointments without mutation.] | [Yes] | [No] | [Copilot, revised with human feedback] | [Modify: added missing boundary checks for RES-06 and verified all 50 tests pass.] |

Comparison with original common tests / any proposed weakening: [The original 37 tests still pass, and Copilot added 13 rescheduling test cases without replacing existing tests. No weakened assertions identified during the test review.]

Independent human checks and corrections:
- [Reviewed Copilot's tests and requested two improvements:]
  - [Verifying the `new_date_time` keyword argument]
  - [Checking same-time rejection for `CANCELLED` and `COMPLETED` appointments]
- [Copilot implemented both changes.]
- [Ran the focused, existing and full test suites, obtaining 13, 37 and 50 passing tests respectively.]

## G Actual verification

| Requirement / acceptance scenario | Test or demonstration | Meaningful expected result | Actual result | Evidence / version |
|---|---|---|---|---|
| RES-01 / AC-RES-01 successful move | [response] | [response] | [response] | [response] |
| RES-02 same object and participant identities | [response] | [response] | [response] | [response] |
| RES-03 / AC-RES-02 unknown and invalid IDs | [response] | [response] | [response] | [response] |
| RES-04 / AC-RES-03 conflicting practitioner | [response] | [response] | [response] | [response] |
| AC-RES-04 different practitioner allowed | [response] | [response] | [response] | [response] |
| RES-06 / AC-RES-05 cancelled and completed | [response] | [response] | [response] | [response] |
| RES-05-R2 / AC-RES-06-R2 lookup and listing order | [response] | [response] | [response] | [response] |
| Self-exclusion and same-time no-op | [response] | [response] | [response] | [response] |
| Invalid datetime and failed-state snapshots | [response] | [response] | [response] | [response] |
| Successful old-slot reuse | [response] | [response] | [response] | [response] |

| Suite | Command / working directory | Code SHA | Actual count and result | Evidence |
|---|---|---|---|---|
| Focused PG | [response] | [response] | [response] | [response] |
| Common independently | [response] | [response] | [response] | [response] |
| Full cumulative | [response] | [response] | [response] | [response] |
| Integrated retest | [response] | [response] | [response] | [response] |

Failures / diagnosis / corrections and reruns / unresolved concerns: [response]

## H Decisions corrections and independent review

| Significant agent action | Human review and evidence | Accept / Modify / Reject and reason | Manual correction or recovery | Recheck evidence |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |

Final proposal decision: [Accepted / Accepted after modification / Rejected]
Evidence supporting decision: [response]
If rejected, how the required feature was subsequently completed and verified: [response or not applicable]
Saved proposal and targeted recovery details if needed: [response or not applicable]
Human explanation of every changed method and limitations: [response]
Another PG / willing UG / tutor reviewer, actual PR/diff review and feedback: [links]
Corrections, recheck and actual approval before integration: [links]
Integrated PG SHA / common protected SHA: [response]
Each assessed PG member's implementation, supervision and test contribution: [response and links]
Optional UG help, acknowledged separately: [response or none]

## I Four reflections

1. Which agent change had the greatest blast radius? [response]
2. Did the plan predict it? [response]
3. What did you reject or manually correct? [response; report honestly if none]
4. What evidence justified final approval? [response]

## J Ten formative questions

1. What is the difference between an AI assistant and an engineering agent? [response]
2. What is the simplified agent loop used in Stage 10? [response]
3. Why should an agent plan be reviewed before repository edits begin? [response]
4. What is meant by the blast radius of a software change? [response]
5. Why is diff review essential for agentic changes? [response]
6. What is a human approval gate? [response]
7. What is test accommodation and why is it dangerous? [response]
8. What is rollback in the context of agentic software engineering? [response]
9. Who remains accountable for accepted agentic changes? [response]
10. What is the Stage 10 engineering rule? [response]

## K Completion and Stage 11 handover

- [ ] Common Stage 9 checkpoint protected; UG pathway unaffected.
- [ ] RES-01–06 and RES-05-R2 implemented in the same project.
- [ ] Domain/service boundaries, current exceptions and coding standard preserved.
- [ ] Positive/negative/boundary cases and failed-state checks verified.
- [ ] Common tests remain valid and independently passing; full suite passes.
- [ ] Plan reviewed before bounded actions; every file and test diff inspected.
- [ ] Actual agent route, decisions, corrections and rechecks recorded honestly.
- [ ] No unrelated features, persistence, dependencies or staff solutions introduced.
- [ ] Another-member or tutor review and integrated retest complete.
- [ ] Tutorial, four reflections, ten formative responses and PG contributions complete.
- [ ] Each PG member can explain their code and supervision.
- [ ] README PG note, actual integrated SHA and limitations recorded.

Unresolved issues / owner / action: [response]
Stage 11 handover references to extension, tests, dependencies and actual AI/review evidence: [response]
Submitted SHA / explanation if later than tested code: [response]
Stage 11 materials are supplied from the beginning. Begin Stage 11 only after Stage 10 has been integrated, verified and recorded. UG follows the protected common code from Stage 9 to Stage 12.
