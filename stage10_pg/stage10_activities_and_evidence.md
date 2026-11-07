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

Every changed file inspected, including new/untracked files: [PR#13](https://github.com/alvinzald/st1-assignment-3/pull/13)
  - [domain.py](../project/smartcare/domain.py)
  - [services.py](../project/smartcare/services.py)
  - [test_rescheduling.py](../project/tests/test_rescheduling.py)
  - [copilot_plan_prompt.md](evidence/copilot_plan_prompt.md)
  - [stage10_activities_and_evidence.md](stage10_activities_and_evidence.md)

Unexpected changes, scope creep, secrets/dependencies/configuration, unrelated cleanup: [No unrelated functionality, new dependencies, configuration changes or secrets identified. The changes remain within the approved Stage 10 implementation and evidence scope.]

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
| RES-01 / AC-RES-01 successful move | [`test_reschedule_preserves_identity_and_updates_session_views`] | [A scheduled appointment moves to an available time.] | [Passed] | [[PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13)] |
| RES-02 same object and participant identities | [`test_reschedule_preserves_identity_and_updates_session_views`] | [Original appointment object, ID, patient and practitioner are preserved.] | [Passed] | [[PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13)] |
| RES-03 / AC-RES-02 unknown and invalid IDs | [`test_reschedule_rejects_unknown_and_invalid_ids_without_mutation`] | [Unknown IDs raise `LookupError`; invalid IDs raise `ValueError` without mutation.] | [Passed] | [[PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13)] |
| RES-04 / AC-RES-03 conflicting practitioner | [`test_reschedule_rejects_scheduled_practitioner_conflict_without_mutation`] | [Conflicting scheduled appointments are rejected without changing existing records.] | [Passed] | [[PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13)] |
| AC-RES-04 different practitioner allowed | [`test_reschedule_allows_other_practitioner_and_inactive_slot_occupants`] | [Different practitioners may have appointments at the same time.] | [Passed] | [[PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13)] |
| RES-06 / AC-RES-05 cancelled and completed | [`test_non_scheduled_appointment_cannot_be_rescheduled`] | [`CANCELLED` and `COMPLETED` appointments reject rescheduling, including same-time requests.] | [Passed] | [[PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13)] |
| RES-05-R2 / AC-RES-06-R2 lookup and listing order | [`test_reschedule_preserves_identity_and_updates_session_views`] | [Lookup returns the updated appointment and listing reflects the correct chronological order.] | [Passed] | [[PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13)] |
| Self-exclusion and same-time no-op | [`test_reschedule_allows_same_time_no_op`] | [An appointment does not conflict with itself, and its current time remains valid.] | [Passed] | [[PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13)] |
| Invalid datetime and failed-state snapshots | [`test_invalid_reschedule_time_does_not_mutate_state`] | [Invalid datetimes raise `ValueError` and leave stored records unchanged.] | [Passed] | [[PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13)] |
| Successful old-slot reuse | [`test_reschedule_preserves_identity_and_updates_session_views`] | [Another appointment can be booked into the original slot after rescheduling.] | [Passed] | [[PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13)] |

| Suite | Command / working directory | Code SHA | Actual count and result | Evidence |
|---|---|---|---|---|
| Focused PG | [`python -m pytest -q tests/test_rescheduling.py` / `project/`] | [`83fa1e2`] | [13 passed] | [[Comment 6705299493](https://github.com/alvinzald/st1-assignment-3/pull/13#issuecomment-6705299493)] |
| Common independently | [`python -m pytest -q --ignore=tests/test_rescheduling.py` / `project/`] | [`83fa1e2`] | [13 passed] | [[Comment 6705299493](https://github.com/alvinzald/st1-assignment-3/pull/13#issuecomment-6705299493)] |
| Full cumulative | [`python -m pytest -q` / `project/`] | [`83fa1e2`] | [13 passed] | [[Comment 6705299493](https://github.com/alvinzald/st1-assignment-3/pull/13#issuecomment-6705299493)] |
| Integrated retest | [`python -m pytest -q` / `project/`] | [`8785aa5`] | [50 passed] | [Merged PR#13](https://github.com/alvinzald/st1-assignment-3/pull/13) |

Failures / diagnosis / corrections and reruns / unresolved concerns:
- [No test failures were observed.]
- [Human review identified incorrect parameter names (`date_time` instead of `new_date_time`) and missing same-time rejection tests for inactive appointments.]
- [Copilot corrected both issues]
- [Human verification confirmed 13 focused, 37 existing and 50 cumulative tests passing.]

## H Decisions corrections and independent review

| Significant agent action | Human review and evidence | Accept / Modify / Reject and reason | Manual correction or recovery | Recheck evidence |
|---|---|---|---|---|
| [Added rescheduling methods in domain.py and services.py.] | [[PR#13](https://github.com/alvinzald/st1-assignment-3/pull/13)] | [Modify: Parameter names did not match the requirements.] | [Asked Copilot to rename `date_time` to `new_date_time` in both methods.] | [[Comment 6705299493](https://github.com/alvinzald/st1-assignment-3/pull/13#issuecomment-6705299493)] |
| [Generated rescheduling tests in test_rescheduling.py.] | [[PR#13](https://github.com/alvinzald/st1-assignment-3/pull/13)] | [Modify: Same-time rejection checks for inactive appointments were missing.] | [Asked Copilot to add boundary checks for `CANCELLED` and `COMPLETED` appointments.] | [[Comment 6705299493](https://github.com/alvinzald/st1-assignment-3/pull/13#issuecomment-6705299493)] |

Final proposal decision: [Accepted after modification]

Evidence supporting decision: [[PR#13](https://github.com/alvinzald/st1-assignment-3/pull/13)]

If rejected, how the required feature was subsequently completed and verified: [Not applicable. The proposal was modified and accepted rather than rejected.]

Saved proposal and targeted recovery details if needed: [[Saved proposal](evidence/copilot_plan_prompt.md). Recovery SHA is `299607323d5258b6c5a1c1af86cd94726abe7e16`]

Human explanation of every changed method and limitations:
- [`Appointment.reschedule()` validates the appointment status and new datetime before updating its time.]
- [`AppointmentService.reschedule_appointment()` handles lookup, conflict checking and delegates the update to the domain method.]
- [Rescheduling is only available for `SCHEDULED` appointments and uses the existing in-memory data store.]
- [Changes remain visible only during the current session.]

Another PG / willing UG / tutor reviewer, actual PR/diff review and feedback: [pending]

Corrections, recheck and actual approval before integration: [links]

Integrated PG SHA / common protected SHA: [Protected Stage 9 SHA: `299607323d5258b6c5a1c1af86cd94726abe7e16`]

Each assessed PG member's implementation, supervision and test contribution:
- [Alvin Zaldivar - [defined requirements](https://github.com/alvinzald/st1-assignment-3/issues/12#issue-6257067352), [approved copilot plan](https://github.com/alvinzald/st1-assignment-3/issues/12#issuecomment-6704696945), supervised implementation, [reviewed code and tests](https://github.com/alvinzald/st1-assignment-3/pull/13#issue-6257535831), [verified results](https://github.com/alvinzald/st1-assignment-3/pull/13#issuecomment-6705299493)]

Optional UG help, acknowledged separately: [response or none]

## I Four reflections

1. Which agent change had the greatest blast radius? [I think the service-level rescheduling method carried the most risk. A mistake in the conflict-checking logic could allow overlapping appointments, affecting the reliability of the existing booking system.]
2. Did the plan predict it? [Yes. Copilot's plan already considered scheduling conflicts and proposed reusing the existing conflict-checking method rather than introducing new logic.]
3. What did you reject or manually correct? [I noticed that Copilot used the wrong parameter names in both rescheduling methods, so I requested corrections. I also asked it to include missing test cases for rescheduling inactive appointments to their existing time.]
4. What evidence justified final approval? [After reviewing the corrections, I independently ran the tests and confirmed that all 50 passed, including the 13 new rescheduling cases. This supported my decision to accept the implementation after modification, although independent reviewer approval is still pending.]

## J Ten formative questions

1. What is the difference between an AI assistant and an engineering agent? [An AI assistant mainly helps by answering questions or suggesting solutions. An engineering agent goes further by carrying out development tasks, such as modifying files and running tests.]
2. What is the simplified agent loop used in Stage 10? [The agent examines the task, prepares a plan, waits for approval, makes the approved changes and checks the results. The developer then reviews the work and decides whether to accept it.]
3. Why should an agent plan be reviewed before repository edits begin? [Reviewing the plan first gives the developer a chance to catch unnecessary or risky changes before they affect the project.]
4. What is meant by the blast radius of a software change? [It refers to how much of the system could be affected by a change, including parts that were not directly modified.]
5. Why is diff review essential for agentic changes? [An agent's summary might not tell the whole story. Reviewing the diff lets us see exactly what changed and whether anything was modified without a good reason.]
6. What is a human approval gate? [It is a point in the workflow where the agent must get permission from a developer before continuing with certain actions.]
7. What is test accommodation and why is it dangerous? [This happens when tests are adjusted to agree with faulty code instead of correcting the code itself. The tests might pass, but the underlying problem would still exist.]
8. What is rollback in the context of agentic software engineering? [Rollback means undoing changes made by the agent when they cause problems or fall outside the agreed scope, allowing the project to return to a known working state.]
9. Who remains accountable for accepted agentic changes? [The developer and the team are still responsible for the submitted work. Using an agent does not transfer responsibility for mistakes to the AI.]
10. What is the Stage 10 engineering rule? [The agent can help with the development work, but the developer must decide what it is allowed to do, check what it actually did and approve the outcome based on evidence.]

## K Completion and Stage 11 handover

- [x] Common Stage 9 checkpoint protected; UG pathway unaffected.
- [x] RES-01–06 and RES-05-R2 implemented in the same project.
- [x] Domain/service boundaries, current exceptions and coding standard preserved.
- [x] Positive/negative/boundary cases and failed-state checks verified.
- [x] Common tests remain valid and independently passing; full suite passes.
- [x] Plan reviewed before bounded actions; every file and test diff inspected.
- [x] Actual agent route, decisions, corrections and rechecks recorded honestly.
- [x] No unrelated features, persistence, dependencies or staff solutions introduced.
- [ ] Another-member or tutor review and integrated retest complete.
- [x] Tutorial, four reflections, ten formative responses and PG contributions complete.
- [x] Each PG member can explain their code and supervision.
- [X] README PG note, actual integrated SHA and limitations recorded.

Unresolved issues / owner / action: [response]

Stage 11 handover references to extension, tests, dependencies and actual AI/review evidence:
- [Introduced rescheduling methods in `domain.py` and `services.py`]
- [Added 13 new tests in test_rescheduling.py.]
- [No new dependencies were introduced.]
- [Implementation, Copilot decisions and verification evidence are available in PR #13 and the Stage 10 evidence record.]

Submitted SHA / explanation if later than tested code: [`8785aa5ca9195677d47ec87461e1d5dec8279c8b`]

Stage 11 materials are supplied from the beginning. Begin Stage 11 only after Stage 10 has been integrated, verified and recorded. UG follows the protected common code from Stage 9 to Stage 12.
