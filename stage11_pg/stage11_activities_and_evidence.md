# Stage 11 PG assurance activities and evidence

PG-only stage. Undergraduate students are not required to complete this record. UG-only groups retain this supplied template unchanged as intentionally not applicable; do not fabricate N/A responses. Optional UG participation is unassessed.

Working draft. Bracketed answers are based on available Stage 10 evidence and the Stage 11 handout. Proposed tutorial responses should be checked and adjusted by the student; no Stage 11 inspection, Copilot audit, new test or independent approval is claimed. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied file in stage11_pg/ in your EXISTING repository. Preserve project/, earlier records/tests and the protected common Stage 9 SHA. Do not copy staff references or fabricate AI evidence.

Group/tutorial: [Wed 4:30-6:30, Group 6]
Assessed PG members and contributions: [Alvin Zaldivar — PG owner; Stage 11 assurance work, verification and sign-off pending]
Optional UG contributors: [None confirmed at this stage]

## A Handover and human-first scope

Integrated Stage 10 code SHA / protected Stage 9 common SHA: [`8785aa5ca9195677d47ec87461e1d5dec8279c8b` / `299607323d5258b6c5a1c1af86cd94726abe7e16`]
Recoverable branch / baseline / actual commands, working directory and results: [Integrated Stage 10 baseline on `main`: `git status --short` showed a clean working tree and `python -m pytest -q` from `project/` returned 50 passed. Stage 11 assurance branch and new baseline checks: pending.]
Domain, store, services, queries, console, entry point, tests and rescheduling inspected: [PENDING — inspect the actual Stage 11 baseline files before recording findings.]
Selected PG feature and common workflow / requirements / code locations: [PG: appointment rescheduling (RES-01–06, including RES-05-R2) in `project/smartcare/domain.py`, `services.py` and `tests/test_rescheduling.py`. Common workflow: patient lookup (FR-02) through `PatientService` and `SmartCareDataStore`; inspect actual code/tests before finalising risk claims.]
Actual available earlier AI, issue, PR and dependency evidence: [Stage 10 [issue #12](https://github.com/alvinzald/st1-assignment-3/issues/12), [Copilot proposal](https://github.com/alvinzald/st1-assignment-3/issues/12#issuecomment-6704660853), [human approval](https://github.com/alvinzald/st1-assignment-3/issues/12#issuecomment-6704696945), [PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13) and [independent test comment](https://github.com/alvinzald/st1-assignment-3/pull/13#issuecomment-6705299493). Dependency inspection for Stage 11 pending.]
Missing evidence / honest limitation: [Stage 10 was merged without the required independent teammate/tutor review; this remains an unresolved limitation. Stage 11 code inspection, Copilot audit, assurance tests and reviewer evidence have not yet been completed.]
Assets and trust boundaries: [Assets to assess: synthetic patient/practitioner records, appointment identity/status/time, cancellation history, assertions, requirements and Git history. Boundaries to inspect: console input to services, services to domain/store, query inputs/outputs, repository content to Copilot, external dependency sources and Copilot edits to reviewed code. Actual risks and controls pending inspection.]
Scope, assumptions, exclusions and initial observations made BEFORE Copilot: [PENDING HUMAN-FIRST ACTIVITY — personally inspect the actual source and record initial observations in Section C before asking Copilot for Stage 11 findings. Working scope: session-only SmartCare; no SQL, restart persistence, clinical deployment or new scheduling features.]
Confirmed Copilot mode / student entitlement / permissions / approval reference: [Earlier Stage 10: GitHub Copilot in PyCharm on Windows, Plan and Agent modes available, with "Allow All" disabled during planning. Teaching approval reference: [UC Learn, around 35:00](https://uclearn.canberra.edu.au/courses/20399/external_tools/197). Reconfirm Stage 11 permissions/version before use.]
Plan-only to human approval to bounded editing check / approved equivalent route: [Stage 10 used a plan-first workflow with [recorded human approval](https://github.com/alvinzald/st1-assignment-3/issues/12#issuecomment-6704696945). Stage 11 review-only permissions and any later edit approval: pending.]
Overview/revision 2 availability / source: [SmartCare A3 Requirements Baseline 2026, Revision 2, supplied with the assignment materials; Stage 10 requirement mappings also appear in [Stage 10 evidence](../stage10_pg/stage10_activities_and_evidence.md).]
Assigned PG owner / independent reviewer: [Alvin Zaldivar / independent teammate or tutor reviewer pending]

## B Original tutorial activities


### B1 Risk classification

| Scenario | Risk | Why | Control |
|---|---|---|---|
| AI explains a public Python error | [Low] | [Uses public information for learning; little risk if no private code or data is shared.] | [Check the explanation against Python documentation and try the fix myself.] |
| Student pastes an API key into AI | [High] | [The credential could be exposed outside the project.] | [Do not paste keys; remove any exposed key and rotate it if one was shared.] |
| Agent proposes unknown package | [Medium–High] | [The package may be unnecessary, untrusted or incompatible with the project.] | [Do not install it until its purpose, source, licence and approval are checked.] |
| AI-generated code logs patient names | [High] | [Unnecessary logs could expose patient information.] | [Remove or minimise sensitive logging and test what is actually written to output.] |
| Agent modifies deployment configuration | [High] | [A configuration change may affect security or runtime behaviour outside the approved feature.] | [Require permission first, inspect the diff and keep a rollback option.] |

### B2 Green Amber Red
Choose GREEN / AMBER / RED and justify each.

| Use | Classification | Reason and policy/control |
|---|---|---|
| Ask AI to explain pytest fixture | [GREEN] | [Learning assistance with low impact; I still need to understand the explanation.] |
| Generate 100 lines of assessed domain code | [AMBER, only if permitted] | [A significant code contribution that needs disclosure, human review and independent tests. Not acceptable if the assessment prohibits generated code.] |
| Paste real patient record for debugging | [RED] | [Discloses private data unnecessarily. Use synthetic records instead.] |
| Use AI to draft test ideas then verify | [AMBER] | [Useful assistance, but I need to select meaningful assertions and verify the cases myself.] |
| Agent autonomously deletes repository files | [RED] | [Unapproved destructive changes could remove work or evidence. Require explicit scope approval and recovery controls.] |

### B3 VERIFY patient search
Record one concrete question/evidence item for each letter against the current PatientService/shared-store contract.

| VERIFY element | Question or evidence |
|---|---|
| Validate | [Does a known patient ID return the registered `Patient`, while an unknown valid ID raises `LookupError` and invalid IDs raise `ValueError`?] |
| Examine | [Check `PatientService.find_patient()` and `SmartCareDataStore.find_patient()` to confirm that the service raises the error while the store returns `None` for a missing record.] |
| Run meaningful tests | [Use a registered patient and fresh store; assert object identity for a known ID, `LookupError` for an unknown ID and `ValueError` for blank/invalid IDs.] |
| Inspect risks | [Check that the lookup cannot fabricate a patient, return unrelated records or expose unnecessary personal details.] |
| Fit architecture/policy | [Confirm that the service handles lookup errors and the store only manages its records, without adding unrelated logging or dependencies.] |
| You remain responsible | [I must review the actual method and tests before accepting any AI suggestion about patient search.] |

### B4 TRUST decision
The feature passes tests but adds an unreviewed package and logs full patient records. Should it be accepted?

| TRUST element | Reason/evidence/action |
|---|---|
| Trace | [Check why the package was introduced, its source and the associated requirement or approval. No clear justification is provided.] |
| Review | [Do not approve it based on a passing test count; another person needs to inspect the dependency and logging changes.] |
| Understand | [Find out what the package does and why full patient records are being logged.] |
| Secure | [Unnecessary patient logging creates a privacy risk, and the new package has not been checked.] |
| Test | [Review output/logging behaviour and rerun meaningful tests after removing or correcting the risky changes.] |

Decision and reason: [Reject in its current form. Passing tests do not justify an unreviewed dependency or unnecessary patient-data logging. Correct these issues, review the diff and retest before approval.]
Exit: Why is a technically correct AI-generated feature still potentially unacceptable? [It may work as expected but still expose data, introduce unapproved dependencies or create risks that the tests were not designed to detect.]

### B5 Sanitised critique only
Identify the hard-coded demo-key placeholder, unnecessary requests import, patient-ID/name logging, fabricated lookup and missing test/provenance evidence. Do not copy or run the old audit target.

| Concern | Observed example evidence | Severity | Correction and recheck |
|---|---|---|---|
| Hard-coded demo-key placeholder | [The teaching snippet assigns an `API_KEY` literal in source code; it is described as a demo placeholder, not evidence of a leaked real key.] | [Medium] | [Remove embedded key patterns, use configuration if a secret is genuinely needed, and scan the diff for credentials.] |
| Unnecessary `requests` import | [The example imports `requests` even though patient lookup should use the existing in-memory store.] | [Medium] | [Remove the unnecessary import/dependency and verify the code still runs without it.] |
| Patient ID/name logging | [The example logs a patient's identifier and name.] | [High] | [Remove unnecessary logging or minimise its content; check captured output using synthetic data.] |
| Fabricated patient lookup | [The example builds a new dictionary from supplied values instead of looking up a stored patient; empty IDs return `None`.] | [High] | [Use the actual store/service contract; test registered identity and required `LookupError`/`ValueError` cases.] |
| Missing test/provenance evidence | [No meaningful test assertions or origin/review evidence are supplied for the example.] | [Medium] | [Request traceable source evidence and tests of known, unknown and invalid IDs; verify results independently.] |

## C Actual risk register

| Risk | Artefact | Likelihood | Impact | Control | Status |
|---|---|---|---|---|---|
| [Rescheduling and cancellation may cause inconsistent appointment history or listing results.] | [`domain.py`, `services.py`, `data_store.py`] | [Uncertain. Existing rescheduling tests pass, but combined workflow coverage needs checking.] | [Medium] | [Test rescheduling followed by cancellation, then check lookup and listing results.] | [Pending verification] |
| [Queries may accidentally modify stored appointment collections.] | [`queries.py`, `data_store.py`] | [Unknown until inspected.] | [Medium] | [Check whether queries return separate list containers without modifying the original collection.] | [Pending verification] |
| [Console errors or diagnostic output may reveal unnecessary patient information.] | [`console.py`, `main.py`] | [Unknown. No information exposure has been confirmed.] | [High] | [Inspect error handling and displayed information to check whether unnecessary details are exposed.] | [Pending verification] |

## D Actual findings tests and corrective actions

For each of at least TWO new/materially strengthened tests, explain the earlier coverage gap and the incorrect behaviour its assertions detect:
- [Added test for rescheduling followed by cancellation. Previous tests covered these operations separately, but not their combined behaviour. The new test checks that the appointment remains accessible, retains its updated time and `CANCELLED` status, and frees its slot for another booking.]
- [Added test for patient lookup across separate data stores. This checks that records from one SmartCare session are not accidentally accessible through another store, even when the same patient ID is used.]

| Claim / risk / requirement | Location / version | Independent check / test | Observed result / finding or no finding | Action / owner | Recheck / limitation |
|---|---|---|---|---|---|
| [Rescheduling followed by cancellation may affect appointment history.] | [`domain.py`, `services.py`, `test_assurance.py`] | [`test_reschedule_then_cancel_preserves_history`] | [Passed. The cancelled appointment remained accessible with its updated time, and the slot could be reused. No defect identified.] | [Alvin Zaldivar / Added a combined workflow test. No production change needed.] | [Passed. Only current-session behaviour was tested.] |
| [Patient records may not be properly isolated between data stores.] | [`data_store.py`, `services.py`, `test_assurance.py`] | [`test_patient_lookup_isolated_between_sessions`] | [Passed. The second store could not retrieve records from the first. No defect identified.] | [Alvin Zaldivar / Added a session-isolation test. No production change needed.] | [Passed. Does not establish authentication or access control.] |
| [Console output may expose unnecessary patient information.] | [`console.py`, `main.py`] | [Copilot read-only inspection; further human inspection pending.] | [Conditional privacy risk. No confirmed vulnerability.] | [Alvin Zaldivar / Review displayed information against the teaching application's requirements.] | [Pending manual inspection.] |

| Assurance test | Earlier gap | Input/setup | Meaningful assertion | Incorrect result detected | Evidence/result |
|---|---|---|---|---|---|
| [Reschedule then cancel] | [No combined rescheduling and cancellation test.] | [Book an appointment, move it to another time, cancel it and attempt a new booking in the released slot.] | [Original appointment remains accessible with its new time and CANCELLED status. The released slot can be reused.] | [Lost appointment history, incorrect status or an incorrectly occupied slot.] | [2-test focused suite passed.] |
| [Patient lookup session isolation] | [Existing patient lookup tests did not establish isolation between separate data stores.] | [Create two stores, register a patient in the first and attempt lookup from the second. Then register the same ID separately.] | [The second store cannot access the first store's patient, and the two records remain independent.] | [Patient records leaking between separate stores or incorrectly shared objects.] | [2-test focused suite passed.] |
| Additional if useful | [Not required.] | [Not required.] | [Not required.] | [Not required.] | [Not required.] |

| Suite | Command / project working directory | Tested code SHA | Actual result | Evidence |
|---|---|---|---|---|
| Assurance focused | [`python -m pytest -q tests/test_assurance.py` / `project/`] | [Stage 10 base `8785aa5` + local Stage 11 changes] | [2 passed] | [Local terminal output; repository evidence link pending.] |
| Previous PG independently | [`python -m pytest -q --ignore=tests/test_assurance.py` / `project/`] | [Stage 10 base `8785aa5` + local Stage 11 changes] | [50 passed] | [Local terminal output; repository evidence link pending.] |
| Common independently | [`python -m pytest -q --ignore=tests/test_assurance.py --ignore=tests/test_rescheduling.py` / `project/`] | [Stage 10 base `8785aa5` + local Stage 11 changes] | [37 passed] | [Local terminal output; repository evidence link pending.] |
| Full PG cumulative | [`python -m pytest -q` / `project/`] | [Stage 10 base `8785aa5` + local Stage 11 changes] | [52 passed] | [Local terminal output; repository evidence link pending.] |
| Integrated retest | [`python -m pytest -q` / `project/`] | [`15b4833`] | [52 passed in 0.08s] | [[Merged PR #14](https://github.com/alvinzald/st1-assignment-3/pull/14)] |

Confirmed defect / minimal correction / before-after evidence, or justified no-change decision: [No production defect was identified by the two new assurance tests. Both passed, so no production code changes were necessary. The new tests provide additional coverage for combined appointment operations and session isolation.]

Preserved earlier assertions / inspected test diff: [The 50 existing tests remain unchanged and all pass. Two new assurance tests were added in `test_assurance.py`. Final diff inspection is pending.]

Unresolved failures, action and owner: [No failing tests. Remaining work includes manual privacy inspection, final evidence review and independent approval.]

## E VERIFY assessment

| VERIFY element | Evidence | Finding/action |
|---|---|---|
| Validate against requirements | [Reviewed RES-01–06, RES-05-R2 and the existing appointment history and patient lookup contracts. The new tests cover rescheduling followed by cancellation and patient lookup across separate data stores.] | [Both new tests passed. The tested behaviour matches the expected contracts.] |
| Examine implementation | [Reviewed the query and data store methods, which create separate list containers without changing the original collection. Also checked the console and service responsibilities.] | [No query mutation defect identified. The existing architecture remains unchanged.] |
| Run meaningful tests | [Ran the assurance, previous PG, common and full test suites from `project/`. Results were 2, 50, 37 and 52 passed respectively.] | [All tests passed. The new tests cover scenarios that were not previously tested together.] |
| Inspect risks and assumptions | [Checked appointment history, data isolation, query mutation and console output. Patient information is displayed for requested lookup and appointment operations.] | [No confirmed production defect.] |
| Fit architecture and policy | [The implementation follows the existing domain, service, data store, query and console structure. Production imports use the Python standard library, while pytest is used for testing.] | [No unnecessary dependency or architecture change identified. The review is limited to the teaching application's requirements and confirmed Copilot permissions.] |
| You remain responsible | [Alvin Zaldivar selected the initial risks, approved Copilot's read-only review and independently ran the tests.] | [I remain responsible for reviewing the findings, accepting changes and documenting unresolved limitations.] |

## F TRUST assessment

| TRUST element | Evidence | Status/action |
|---|---|---|
| Trace | [Stage 10 rescheduling requirements, Copilot contributions and corrections are documented in [Issue #12](https://github.com/alvinzald/st1-assignment-3/issues/12) and [PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13). Stage 11 audit findings are recorded in Section G.] | [Available changes and AI contributions can be traced. Missing independent Stage 10 approval remains documented.] |
| Review | [Reviewed Copilot's findings and classified them as evidence gaps, conditional risks or testing gaps. Proposed assurance tests were also checked against the expected behaviour.] | [My review is recorded, but an independent reviewer has not yet approved Stage 11.] |
| Understand | [Rescheduling test checks appointment identity, cancellation history and slot reuse. Patient isolation test checks that separate data stores do not share patient records.] | [Both tests passed. I can explain what they verify and why the additional coverage is useful.] |
| Secure | [Reviewed console output, error handling, dependencies and the application structure. No hard-coded credentials, unnecessary diagnostic logging or new runtime packages were identified in the inspected files. Patient information is displayed as part of requested operations.] | [No confirmed security defect. Access to shared terminal output remains a conditional privacy risk. This review does not establish production-level security or clinical suitability.] |
| Test | [The two new assurance tests passed. The previous 50 tests and the common suite of 37 tests also passed. The updated full suite now has 52 passing tests.] | [Current working-tree verification passed. Pending final integrated test.] |

## G GitHub Copilot audit

Sanitised material / actual prompt, context, version and response links:Sanitised material / actual prompt, context, version and response links:
- **Actual Prompt:** [[Prompt](evidence/copilot_audit_prompt.md)]
- **Context:** [One in-memory SmartCareDataStore; domain, services, pure queries and console; Stage 10 rescheduling; actual tests. No SQL, restart persistence or external calendar API is required.]
- **Version:** [version 1.0.103/Windows]
- **Response Links:** [[Response](evidence/copilot_audit_prompt.md)]

Evidence that human scope and initial observations preceded Copilot: [I identified three possible risks in Section C before running the Copilot audit: inconsistent appointment history after rescheduling and cancellation, queries modifying stored records, and unnecessary patient information being displayed. Copilot was then given these observations as part of its review scope.]

Actual supported route or approved equivalent / access limitations: [Used GitHub Copilot Chat in PyCharm with a read-only inspection scope (plan). Copilot requested permission before accessing the repository files and GitHub evidence, which I approved. No file changes, package installations or test commands were performed during the audit.]

Significant earlier AI contributions reviewed / available evidence / missing provenance: [Stage 10 rescheduling was implemented with Copilot assistance. Human review identified incorrect parameter names and missing boundary tests, which were corrected before integration. The implementation and available evidence are recorded in [Issue #12](https://github.com/alvinzald/st1-assignment-3/issues/12) and [PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13). Copilot's Stage 11 audit also identified that the GitHub records do not show independent approval before the Stage 10 merge. This remains an evidence limitation.]

| AI claim | Affected requirement/code/evidence | Observed vs speculative / human verification | Severity / Accept Modify Reject / reason | Outcome / correction or no change | Recheck / limit |
|---|---|---|---|---|---|
| [Independent review evidence is missing from the Stage 10 PR.] | [[PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13)] | [Copilot reported no recorded GitHub reviews or checks. Stage 10 was merged without independent reviewer approval, although the integrated tests passed.] | [Medium / Accept: The missing approval is a genuine evidence gap, not a confirmed code defect.] | [No code change required. Record the missing review honestly.] | [Independent review remains incomplete. The integrated Stage 10 suite passed 50 tests.] |
| [Console output may expose unnecessary patient information.] | [`console.py`, `main.py` / Privacy and data minimisation] | [Copilot identified patient names, IDs and appointment details in console output. This may be expected for the local teaching application. Whether the output is unnecessarily exposed still needs checking.] | [Low / Modify: Treat as a conditional privacy risk rather than a confirmed vulnerability.] | [No production change proposed. Review whether the displayed information is necessary for the current requirements.] | [Pending manual inspection. No authentication or clinical deployment requirements should be assumed.] |
| [There is no combined test for rescheduling followed by cancellation.] | [`domain.py`, `services.py`, `test_rescheduling.py` / RES-05-R2 and appointment history] | [Copilot found separate coverage for rescheduling and cancellation but no combined sequence. No incorrect behaviour was identified in the inspected code.] | [Low / Accept: This is a reasonable testing gap worth addressing.] | [Add an assurance test for rescheduling followed by cancellation, checking appointment identity, retained history, status and slot reuse.] | [Pending test implementation and execution.] |

No false/rejected suggestion, if applicable: [No clearly false finding was identified in Copilot's audit. Its query-mutation inspection found that the code uses separate list containers, so it did not confirm my initial concern. The remaining findings were either evidence gaps or conditional risks, rather than confirmed production defects. Further human verification is still required.]

## H Dependency provenance and privacy review

| Dependency/artefact | Source | Purpose | Licence/provenance | Verified? | Decision | Evidence link |
|---|---|---|---|---|---|---|
| [Python standard library] | [Official Python documentation] | [Provides the application's runtime functionality, including datetime handling and input processing.] | [Python Software Foundation licence and incorporated software notices.] | [Yes, for the reviewed source imports. Installed environment not separately audited.] | [Keep. No additional runtime library needed.] | [Python licence](https://docs.python.org/3.13/license.html) |
| [`pytest==8.3.5`] | [`requirements-dev.txt` / PyPI] | [Runs automated tests during development.] | [MIT licence.] | [Declared version and test execution checked. Package installation source not independently verified.] | [Keep. Required for testing, not application runtime.] | [pytest 8.3.5](https://pypi.org/project/pytest/8.3.5/) |
| [Stage 10 Copilot-assisted rescheduling] | [GitHub Copilot / Issue #12 and PR #13] | [Added appointment rescheduling and its tests.] | [AI contributions and human corrections documented. Independent Stage 10 approval was not obtained.] | [Partially. Implementation and tests verified, with an outstanding review limitation.] | [Retain the implementation and disclose the missing approval.] | [Issue #12](https://github.com/alvinzald/st1-assignment-3/issues/12), [PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13) |

Actual runtime imports / test-tool dependencies / versions checked: [The application uses Python standard-library modules and its own SmartCare modules. Verified Python 3.14.7 and pytest 8.3.5 in the active virtual environment. `requirements-dev.txt` declares `pytest==8.3.5`. No additional third-party runtime dependency was identified in the reviewed code. Installed package sources were not independently verified.]

Secret/data/output/input/permission/minimisation checks and evidence: [Reviewed the console output and input handling. Patient IDs, names and appointment details are displayed during requested operations, which is expected for this teaching application. No hard-coded credentials or unnecessary diagnostic logging were identified in the inspected files. Shared terminal access remains a possible privacy risk. Copilot's Stage 11 audit was approved for read-only inspection.]

Requirements/model/code/tests/Stage 10 provenance links:
- [Stage 10 requirements and implementation: [Issue #12](https://github.com/alvinzald/st1-assignment-3/issues/12)]
- [Code changes and review evidence: [PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13)]
- [Stage 11 assurance tests: `project/tests/test_assurance.py` — 2 passed locally.]
- [Stage 11 Copilot prompt and response: links recorded in Section G.]

Bias/hidden assumptions / name formats / unnecessary fields / accessibility / scheduling policy: [The application uses simplified patient and practitioner records for teaching purposes. Assumptions about names, required fields, accessibility and appointment availability may not suit a real clinical system. These were considered as limitations rather than reasons to introduce new requirements.]

Policy questions or unresolved provenance / responsible contact: [No additional package or licensing issue was identified from the reviewed changes. The installed dependency environment has not been fully audited, and Stage 10 was merged without independent approval. Any unresolved assessment or licensing questions should be referred to the unit teaching team.]

## I Independent review and final audit statement

Human reviewer / PR or diff link / feedback: [Alvin Zaldivar. Reviewed the Stage 11 assurance changes and accepted the implementation based on the code inspection and 52 passing tests. [Review comment](https://github.com/alvinzald/st1-assignment-3/pull/14#issuecomment-6707719669).]

Corrections and recheck / approval before integration: [No production corrections were necessary. Two assurance tests were added and all 52 tests passed.]

Overall decision: [Not yet acceptable for final sign-off. The current technical results support the implementation within the teaching application's scope, but independent review and integration verification are still outstanding.]

Unresolved risks: [The console displays patient information during requested operations, which could present a privacy risk if terminal output is shared. Stage 10 also lacks independent reviewer approval. No confirmed production vulnerability was identified.]

Evidence supporting decision:
- [Stage 10 implementation and changes: [PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13)]
- [Stage 11 Copilot audit: Evidence recorded in Section G.]
- [Two new assurance tests passed.]
- [Previous 50 tests and 37 common tests passed independently.]
- [Full cumulative suite passed all 52 tests.]
- [Dependency and privacy review recorded in Section H.]

Remediation owner / action / status: [Alvin Zaldivar — Obtain independent review, address any feedback and verify the integrated Stage 11 code. No production correction is currently required.]

Residual limitations and conditions of acceptance: [SmartCare is a session-only teaching application using synthetic data. The review does not establish clinical suitability, full security compliance or protection against shared terminal access. Final acceptance requires independent review and integrated verification.]

Accountable reviewer and PG member sign-off:  [Alvin Zaldivar — responsible for the assurance review, test verification and final technical decisions. Self-review completed; independent reviewer sign-off not obtained.]

Integrated PG SHA / protected common SHA: 
- Integrated PG SHA: [`15b4833659840e7ce8f81fb461b0eefdcd98a4ab`]
- Protected common SHA: [`299607323d5258b6c5a1c1af86cd94726abe7e16`]

## J Reflections

1. Which risk would have been easy to miss if you only checked whether tests passed? [The privacy concerns surrounding console output would have been easy to overlook. The application can pass all its functional tests while still displaying information that might be exposed if someone else has access to the terminal.]

2. Which AI audit finding was false or overstated? If none, state honestly and explain verification. [No clearly false findings were identified. Copilot raised concerns about console access but correctly treated them as conditional risks rather than confirmed vulnerabilities. It also found no evidence of query mutation, which was consistent with the implementation and existing tests.]

3. What evidence supports your final trust decision? [I reviewed Copilot's findings, inspected the relevant code and added two assurance tests. All 52 tests passed, including the existing 37 common tests. No production defects were confirmed, although independent approval and integrated verification are still pending.]

## K Ten formative questions


1. What does least privilege mean? [Giving a user or tool only the access needed for its assigned task, rather than unrestricted permissions.]
2. What is provenance in AI-assisted software engineering? [Knowing where code or suggestions came from, who approved them and what evidence supports their use.]
3. What is data minimisation? [Only collecting, sharing or keeping information that is necessary for the task.]
4. What is dependency hallucination? [When AI suggests a package, library or version that does not exist or is not actually needed.]
5. What is software supply-chain risk? [The possibility that third-party packages, tools or their sources introduce security, licensing or reliability problems.]
6. What does the VERIFY framework ask students to do? [Check AI-assisted work against requirements, examine the code, run meaningful tests, inspect risks, confirm it fits the architecture and take responsibility for the result.]
7. What does the TRUST framework ask students to do? [Trace where changes came from, review them, understand how they work, check security and test them before deciding whether they are acceptable.]
8. What does an AMBER AI-use classification mean in this course? [AI made a meaningful contribution, so the use needs to be allowed by course policy, documented and independently checked.]
9. Who remains responsible for professionally accepted AI-assisted software? [The developer and team who accept and submit it, not the AI tool.]
10. What is the Stage 11 engineering rule? [Do not trust AI-assisted code or audit claims just because they sound convincing or pass tests. Check the evidence and make the final decision yourself.]

## L Completion and Stage 12 handover

- [x] Actual SmartCare scope and human-first observations recorded.
- [x] All tutorial activities and every VERIFY/TRUST element addressed.
- [x] At least two meaningful assurance tests with added-value explanations.
- [x] Real findings/no-findings and corrective actions or no-change evidence recorded.
- [x] Earlier assertions preserved; common and PG suites independently checked.
- [x] Copilot claims reviewed and actual decisions recorded honestly.
- [x] Dependency/provenance/privacy review and residual limits documented.
- [ ] Independent human review, integration and retest recorded.
- [x] All three reflections and ten formative questions answered.
- [x] Accountable PG contribution/sign-off and protected UG pathway retained.

Unresolved issues / owner / handover action:
- [Alvin Zaldivar completed the self-review and integrated Stage 11 through PR #14. Independent review by another person was not obtained.]
- [No production defect confirmed. The integrated application passed all 52 tests.]
- [The remaining privacy and assurance limitations are documented in Sections H and I.]

Tested code SHA / command / working directory / observed result: [Integrated SHA: `15b4833659840e7ce8f81fb461b0eefdcd98a4ab`. Command: `python -m pytest -q` from `project/`. Result: 52 passed in 0.08s.]

Final submitted SHA / later evidence-only change explanation: [Tested integrated code SHA: `15b4833659840e7ce8f81fb461b0eefdcd98a4ab`. Final documentation-only commit SHA pending.]
Tested code SHA / command / working directory / observed result:
- [Tested working tree: Stage 10 baseline `8785aa5ca9195677d47ec87461e1d5dec8279c8b` with local Stage 11 assurance changes.]
- [`python -m pytest -q tests/test_assurance.py` — 2 passed.]
- [`python -m pytest -q --ignore=tests/test_assurance.py` — 50 passed.]
- [`python -m pytest -q --ignore=tests/test_assurance.py --ignore=tests/test_rescheduling.py` — 37 passed.]
- [`python -m pytest -q` — 52 passed.]
- [Working directory: `project/`.]
- [Stage 11 PR commit: `834cb01`. Final verification of the committed and integrated code is pending.]

Final submitted SHA / later evidence-only change explanation:
- [Pending integration. Current Stage 11 PR commit: `834cb01`. Final integrated SHA and any later documentation-only changes will be recorded separately.]

Stage 12 handover links to same project/tests/assurance conclusion and limitations:
- [SmartCare application: [project/](../project/)]
- [Stage 10 rescheduling: [PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13)]
- [Stage 11 assurance tests: [test_assurance.py](../project/tests/test_assurance.py)]
- [Stage 11 implementation and documentation: [PR #14](https://github.com/alvinzald/st1-assignment-3/pull/14)]
- [Two assurance tests were added, covering rescheduling followed by cancellation and patient lookup isolation between data stores.]
- [All 52 tests passed locally, including 37 common tests. No production correction was necessary.]
- [No new runtime dependencies were introduced. Independent review remains incomplete, and the assurance conclusion is limited to the session-only teaching application.]
- [Protected Stage 9 common SHA: `299607323d5258b6c5a1c1af86cd94726abe7e16`.]

Begin Stage 12 after the previous applicable stage is integrated, verified and recorded. Its handout and blank record are already supplied.
