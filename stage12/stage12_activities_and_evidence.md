# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: [Group 6, Wed 4:30-6:30]
Members and UG/PG applicability: [Noor Anwari, Kaneez Fizza, Alvin]


## A Release scope and starting SHA

Release label/version and requirements baseline: [ SmartCare Stage 12 Final Release, Overview/revision 2 requirements.]
Common starting SHA / branch / applicable members: [(8c5c69866fb74155027829c8fa85822ca14c2b04), main, All members]
PG starting SHA / branch / applicable members or not applicable: [(8a8bc8f80a699cae201b4ed4a799e7a351199faf), main, Alvin]
Working-state review and approved integration: [Previous stages were reviewed and merged into main. Git status and changes checked before Stage 12.]
Protected common candidate and PG differences: [Stage 9 common SHA preserved. PG work adds rescheduling and additional assurance tests.]
Feature freeze / owner / verifier: [No new optional features, Owner: [Noor Anwari], Verifier: [Alvin]]


## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify: [All tests pass, but the README, dependency review and missing limitation must be completed before final sign-off.]

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope | Evidence | Location/link and SHA | Reviewer | Sufficient? | Gap/action |
|---|---|---|---|---|---|
| Cancellation history works | [Automated tests confirm cancelled appointments remain in history and can be retrieved.] | [Workflow tests](project/tests/test_workflows.py) -(8a8bc8f80a699cae201b4ed4a799e7a351199faf) |[Noor Anwari]  | [Yes, subject to final release verification] | [Confirm tests pass on the final release candidate] |
| Architecture responsibilities are appropriate | [Domain, services, data store, queries and console have separate responsibilities.] | [Stage 9 evidence](../stage09/stage09_activities_and_evidence.md) — 8a8bc8f80a699cae201b4ed4a799e7a351199faf] | [Noor Anwari] | [Yes] | [None] |
| Rescheduling is safe — PG only | [response] | [response] | [response] | [response] | [response] |
| AI use is responsible — common recheck / PG assurance | [response] | [response] | [response] | [response] | [response] |
| System is maintainable | [Code has separate responsibilities, automated tests and README documentation.] | [README](../project/README.md) — 8a8bc8f80a699cae201b4ed4a799e7a351199faf | [Alvin] | [Yes] | [Confirm maintainability in final review.] |
| FR-01–03 register/find and validation | [Automated tests for patient and practitioner registration, lookup and validation.] | [[Service tests](../project/tests/test_services.py) — 8a8bc8f80a699cae201b4ed4a799e7a351199faf] | [noor] | [yes] | [none] |
| FR-04–05 booking/conflict rules | [Automated tests check valid bookings and prevent conflicting appointments.] | [[Workflow tests](../project/tests/test_workflows.py) — 8a8bc8f80a699cae201b4ed4a799e7a351199faf] | [Noor] | [Yes] | [none] |
| FR-06–08 cancellation/history/find | [Automated tests confirm cancellation keeps appointment history and appointments remain retrievable.] |[Workflow tests](../project/tests/test_workflows.py) — 8a8bc8f80a699cae201b4ed4a799e7a351199faf | [Noor] | [yes] | [None] |
| FR-09 and QRY/FP listing/filter/order/purity | [Automated tests verify filtering, sorting, purity and practitioner appointment listing.] | [Query tests](../project/tests/test_queries.py) — 8a8bc8f80a699cae201b4ed4a799e7a351199faf | [Noor] | [Yes] | [None] |
| UI full console sequence and error recovery | [Manual UI-01 and UI-02 tests confirm menu operations and invalid-input recovery.] | [[Console test evidence](../stage09/console_test_evidence.txt) — 8a8bc8f80a699cae201b4ed4a799e7a351199faf] | [Alvin] | [Yes] | [None] |
| Session-only scope / FR-10 retired | [Data is stored only during the session. FR-10 is no longer required.] | [[README](../project/README.md) — 8a8bc8f80a699cae201b4ed4a799e7a351199faf] | [Alvin] | [Yes] | [None] |
| PG RES and assurance integration | [Stage 10 rescheduling tests and Stage 11 assurance tests.] | [Stage 10](../stage10_pg/stage10_activities_and_evidence.md), [Stage 11](../stage11_pg/stage11_activities_and_evidence.md), [rescheduling tests](../project/tests/test_rescheduling.py) — recorded PG SHA 8a8bc8f80a699cae201b4ed4a799e7a351199faf | [alvin] | [Earlier 52-test suite is reported as passing; this supports the PG checkpoint, not a separate final assurance sign-off.] | [Check Stage 11 risk decisions, requirement-specific assertions and the exact release candidate before accepting the PG extension.] |


## C Full regression results

| Suite/scope | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|---|---|---|---|---|---|
| Complete common | [Python 3.14.2] | [project/ — python -m pytest -q] | [8a8bc8f80a699cae201b4ed4a799e7a351199faf] | [52 Test passed in 0.05s] | [52 passed in 0.05s] |
| Complete PG if applicable | [Python 3.14.2] | [project/ — python -m pytest -q] | [8a8bc8f80a699cae201b4ed4a799e7a351199faf] | [all tests passed] | [52 Test passed in 0.05s] |
| Affected focused checks after correction | [N/A] | [N/A] | [N/A] | [N/A] | [N/A] |
| Complete PG if applicable | [Python 3.14.2] | [project/ — python -m pytest -q] | [8a8bc8f80a699cae201b4ed4a799e7a351199faf] | [all tests passed] | [52 Test passed in 0.05s] |
| Full integrated recheck | [Python 3.14.2] | [project/ — python -m pytest -q] | [] | [all tests passed] | [52 passed in 0.05s] |
Prior assertions preserved / reviewed test diff: [All previous tests were kept. No existing test assertions were changed during Stage 12.]
Remaining failure / limitation: [NONE]


## D Console and end to end demonstration

| Demo step | Synthetic setup/input | Expected requirement | Observed result | Evidence/link |
|---|---|---|---|---|
| Problem and stakeholders | [SmartCare appointment management system] | [Help clinics manage patients, practitioners and appointments.] | [SmartCare supports registration, booking, cancellation and appointment lookup.] | [[README](../project/README.md)] |
| Register and find Patient and two Practitioners | [Register P1, DR1, DR2; find each; search P99] | [FR-01–03 registration, lookup and validation] | [Patient and practitioners registered and found successfully. Unknown lookup handled without crashing.] | [stage12/console_demo_evidence.txt] |
| Valid booking | [Book A1 for P1 with DR1 at 2026-12-01 09:00] | [FR-04: Valid appointment booking] | [Appointment A1 booked successfully] | [stage12/console_demo_evidence.txt] |
| Same practitioner exact-time conflict rejected | [Book A2 with DR1 at the same time as A1] | [FR-05: Reject conflicting bookings] | [Booking rejected; A2 not created] | [stage12/console_demo_evidence.txt] |
| Different practitioner same time allowed | [Book A3 with DR2 at the same time as A1] | [FR-05: Different practitioner at the same time allowed] | [A3 booked successfully (after confirmation)] | [stage12/console_demo_evidence.txt] |
| Cancel SCHEDULED and retain/find CANCELLED object | [Cancel A1, then find A1] | [FR-06–08: Cancellation retains appointment history] | [A1 remains retrievable with CANCELLED status] | [stage12/console_demo_evidence.txt] |
| Invalid/repeated cancellation rejected | [Cancel A1 again, then try cancelling A99] | [FR-06–08: Reject invalid/repeated cancellation] | [Both rejected without changing appointment history] | [stage12/console_demo_evidence.txt] |
| Default all-status listing | [List DR1 appointments with blank status filter] | [FR-09: Default listing includes all statuses] | [A1 listed with CANCELLED status] | [stage12/console_demo_evidence.txt] |
| Explicit filtering / empty vs unknown / deterministic order | [Filter DR1 and DR2 by status; search DR99] | [R-09, QRY-01–04: Filtering, empty results, unknown practitioner and sortin] | [check evidence file] | [stage12/console_demo_evidence.txt] |
| Invalid date/status/menu/lookup recovery and continued operation | [Invalid date, status, menu choice and unknown patient; then find A3] | [UI error recovery and continued operation] | [Errors handled; A3 still retrievable] | [stage09/console_test_evidence.txt] |
| Session-only limitation and normal exit | [Enter 0 to exit] | [Session-only data and normal exit] | [Menu exited normally; data is not saved permanently] | [stage12/console_demo_evidence.txt] |
| One meaningful requirement-linked pytest test explained | [Test that cancelled appointments remain retrievable] | [R-06–08: Cancellation must retain appointment history] | [Full test suite passed: 52 tests in 0.05s] | [Workflow tests](../project/tests/test_workflows.py) |
| Architecture and one actual AI decision / known limitation | [response] | [response] | [response] | [response] |
| PG reschedule identity/participants/time and no-op | [response] | [response] | [response] | [response] |
| PG conflict/invalid status/failure non-mutation | [response] | [response] | [response] | [response] |
| PG old slot / current lookup/list ordering / assurance risks | [response] | [response] | [response] | [response] |
Stable demo owner / fresh process / command: [response]
PG demonstrations through service/tests or not applicable: [response]


## E Final code quality and AI review

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | [[Stage 9 evidence](../stage09/stage09_activities_and_evidence.md) and project/smartcare/queries.py] | [No issues identified in the Stage 9 review. Responsibilities are separated.] | [No change required] |
| PascalCase and snake_case naming | [project/smartcare/domain.py, services.py, queries.py] | [Classes use PascalCase and functions use snake_case.] | [No change needed based on the reviewed code.] |
| Useful type hints and meaningful docstrings | [project/smartcare/queries.py, services.py] | [Type hints are used.] | [No changes made.] |
| Four-space indentation and imports/layout | [project/smartcare/] | [No formatting issues ] | [No changes made.] |
| Focused methods / duplication / dead or commented code | [project/smartcare/] | [None] | [no changes] |
| Globals / leakage / unnecessary inheritance or frameworks | [project/smartcare/] | [No issues] | [No changes] |
| No SQLite/persistence/repository ABCs/speculative features | [] | [response] | [response] |
| Synthetic data / secrets / dependencies / provenance | [response] | [response] | [response] |
| Significant common Copilot contributions and human verification | [response] | [response] | [response] |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST | [response] | [response] | [response] |

| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Access route or approved equivalent / limitations: [response]
Available AI evidence and missing evidence honestly disclosed: [response]


## F README and reproducibility check

| README item | Location | Verifier | Result/gap |
|---|---|---|---|
| Purpose and included common/PG scope | [project/README.md] | [Noor] | [Project documentation describes patient/practitioner registration, booking, cancellation, queries and console use; PG rescheduling is a separate extension for Alvin.] |
| Out-of-scope capabilities and known limitations | [project/README.md] | [Noor] | [Session-only storage and retired FR-10 are documented. Other limitations are also explained. No gap identified.] |
| Confirmed teaching Python version and dependency installation | [project/README.md] | [Noor] | [README specifies Python 3.13 and pytest 8.3.5. Dependencies installed successfully. Local tests passed using Python 3.14.2.] |
| Working directory / demo / interactive / test commands | [project/README.md] | [Noor] | [EADME includes all required commands. Demo and tests ran successfully. No gap identified.] |
| Repository structure and architecture responsibilities | [project/README.md] | [Noor] | [README explains the domain, data store and services. Query responsibilities are also explained. Console responsibilities could be clearer.] |
| Responsible AI summary / synthetic-data rule | [response] | [response] | [response] |
| Release label/version and SHA links | [response] | [response] | [response] |
Root README index and project/README verified: [response]
Fresh clone or extracted ZIP / candidate identity: [response]
Verifier and clean environment / actual version: [response]
Setup/run/test commands and observed results: [response]
Missing local file or setup gap / remedy and recheck: [response]


## G Known limitations debt and release notes

Delivered features: [Common: patient and practitioner registration/lookup, appointment booking with conflict checks, cancellation with retained history, appointment lookup, practitioner listing/filtering/sorting and an interactive console. PG only: appointment rescheduling and assurance checks.]
Important fixes: [Earlier Stage 8 work corrected same-practitioner booking conflicts and retained-history lookup after cancellation. Stage 10 PG review also addressed rescheduling method signatures and added boundary tests. No separate Stage 12 code fix is established by the attached evidence.]
Architecture/quality improvements: [SmartCare separates domain entities and state rules, the shared in-memory data store, coordinating services, pure appointment-query helpers and console interaction. Regression, query and rescheduling tests were added across the stages.]
Known limitations: [Records exist only for the current process and appointment times are naive local values with minute precision. The course application has no real-patient deployment safeguards, authentication/roles, database persistence, patient portal, notifications, billing, clinical decision support, production concurrency guarantees or operational monitoring.]
AI-assisted development note: [GitHub Copilot was used to support parts of implementation and review, with human responsibility for accepting changes and checking them against tests and requirements. PG Stage 11 covers responsible-AI assurance. Passing tests alone does not certify privacy, security or AI provenance.]

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| In-memory, session-only storage | Records disappear when SmartCare exits. | Accepted course scope; high priority for a real deployment | Add durable storage only under a revised requirement, with migration and persistence tests. | [Accepted for course release because FR-10 is retired; clearly document the restriction.] |
| No production access control | Real patient data would lack appropriate user authentication and permissions. | Critical before real use | Design and test authentication, authorisation and privacy safeguards. | [Excluded from the course release; it must not be described as clinically deployable.] |
| Naive local minute-precision time | Time zone and daylight-saving rules are not defined for multi-region scheduling. | Future product work | Establish a timezone and scheduling policy with boundary tests. | [Accepted course limitation if disclosed.] |
| Concurrency, monitoring and accessibility not evaluated for production | Multi-user operations, fault detection and inclusive usability are unproven. | Future product work | Add concurrency/load tests, monitoring and accessibility/user evaluation. | [Accepted as out of scope for the teaching prototype, not production readiness.] |
Session-only synthetic data and minute-precision local time: [Only synthetic records may be used; they remain in memory for the current process and are lost on exit. Appointment times are naive local date/time values at minute precision.]
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: [These capabilities are excluded from the current teaching requirements. The application is not suitable for handling real clinical data or providing clinical advice.]
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: [Enterprise concurrency, multi-timezone scheduling, production operations and accessibility/usability evaluation have not been established by the unit tests or the console log.]
Difference between accepted scope limit and unresolved required behaviour: [A stated exclusion such as retired FR-10 persistence is an accepted scope limit. Failure to reject a practitioner conflict under FR-05 or retain a cancelled appointment under FR-07 would be an unmet requirement and would need correction, not a limitation label.]
PG assurance residual risks / owner / status or not applicable: [response]


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] | [response] | [response] |
Justified no-change conclusion if no defect found: [response]
Release blockers still open / status: [response]


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: [None]
Independent reviewer / feedback / response: [None]
Integration commit / full recheck: [response]
Tracked and untracked file inspection / cleanliness: [None]
Secrets/staff material/caches/tool-metadata exclusion check: [None]
Candidate recovery plan / known-good SHA: [Keep the common SHA 8c5c69866fb74155027829c8fa85822ca14c2b04 and PG SHA 8a8bc8f80a699cae201b4ed4a799e7a351199faf recorded in section A. Recover from these immutable commits using a separate branch or a reviewed revert/correction commit rather than deleting Git history.]
Named substantive contributions: [response]


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: [response]
Approver / date / rationale and evidence: [response]
What risks remain / conditions / owners: [response]
Can the team explain the system: [response]
Can a change be recovered: [response]
Common decision / PG decision where different: [response]


## K Final tested release SHA

Exact common tested SHA: [response]
Exact PG tested SHA or not applicable: [response]
Final submitted SHA / repository URL: [response]
Evidence-only later commit and difference explanation: [response]
Executable changes after testing and re-verification: [response]
Source ZIP name / SHA correspondence / extracted comparison: [response]


## L Submission package verification

- [ ] Feature freeze and scoped requirements traced.
- [ ] Applicable full regressions, integrated demo and invalid paths verified.
- [ ] Architecture/code quality and final AI/dependency checks complete.
- [ ] Root README and project/README reproduced by another verifier.
- [ ] Release notes, technical debt and limitations visible.
- [ ] Independent human review, integration and release decision recorded.
- [ ] Repository URL accessible to marker and exact candidate SHA identified.
- [ ] One source ZIP from submitted commit with root README.md and .gitignore.
- [ ] project/ source and all accumulated applicable tests included.
- [ ] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [ ] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [ ] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [ ] Mixed-group common protection and candidate upload routing checked.
- [ ] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: [response]
Deadline/timezone: [response]
Repository access arrangement: [response]
Mixed-candidate upload arrangement: [response]
Oral/video recording/accessibility arrangements: [response]
Remaining administration or release dependency: [response]


## M Formative questions

1. What is a release candidate? [A version of software that is ready for final testing before release]

2. What is feature freeze and why is it used? [Feature freeze means stopping new features so the team can focus on fixing problems, testing and preparing the release.]

3. What is regression testing in a release context? [Regression testing checks that existing features still work after changes are made.]

4. What is a known limitation? [A known limitation is something the software cannot do or does not support. For example, SmartCare does not save data after the application closes.]

5. What is technical debt? [Technical debt is work that may need to be fixed or improved later because of earlier design or coding decisions.]

6. What are release notes? [Release notes explain what is included in the release, what has changed and any known limitations.]

7. What is software maintenance? [Software maintenance means fixing bugs, improving software and keeping it working after release.]

8. What is the purpose of the individual demonstration/viva? [To check that each student understands the project, their contributions, the code, testing and design decisions.]

9. What should the final responsible-AI check establish before release? [It should confirm that AI-generated suggestions were reviewed, tested and verified by humans, and that no private data or unverified claims are included.]

10. What is the main course conclusion about AI and the role of the software engineer? [AI can help developers write and review code, but software engineers are still responsible for understanding requirements, making decisions, testing and ensuring software quality.]


## N Reflection viva and handover

Strongest evidence SmartCare is ready: [The group recorded 52 passing tests at its PG checkpoint, and the Stage 12 console evidence shows registration, lookup, booking, conflict rejection, cancellation/history and normal exit working with synthetic inputs. This is useful evidence for the course release, but does not replace independent release checks.]
Weakest area: [The supplied materials do not yet demonstrate a fresh-clone/ZIP reproduction or independent final release approval. Some demo scenarios, including malformed date/status/menu recovery and deterministic sorting ties, are not shown in the attached Stage 12 console transcript.]
How AI use changed from Stage 1 to Stage 12: [response]
Start doing — engineering and AI use: [response]
Stop doing — engineering and AI use: [response]
Continue doing — engineering and AI use: [response]
What worked / caused rework / future delivery improvement: [response]
One paragraph — If AI can write code why do we still need software engineers: [AI can help produce code and suggest tests, but it cannot take responsibility for whether the result matches the requirements. Software engineers still need to decide what the system should do, check design choices, test real behaviour and identify the risks that automated tests might miss. In SmartCare, we had to check rules such as conflicting bookings and keeping cancelled appointments in history. Human review, teamwork and release decisions are still important, even when AI helps with implementation.]

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | [SmartCare helps clinic reception staff manage patient and practitioner records and appointments within one application session. Patients and practitioners are stakeholders; clinic staff are the console users. See [README](../project/README.md) and the Stage 12 console log.] |
| Two requirements and acceptance criteria | [FR-05: a second SCHEDULED appointment for the same practitioner and exact time must be rejected without storing it, while another practitioner is allowed. FR-07: after cancelling A1, finding A1 must still return that same appointment with CANCELLED status. See [workflow tests](../project/tests/test_workflows.py) and [Stage 12 console evidence](console_demo_evidence.txt).] |
| Domain model and architecture | [`Patient`, `Practitioner`, `Appointment` and `AppointmentStatus` express entity data and rules. `SmartCareDataStore` holds session objects; services coordinate operations; pure functions in `queries.py` filter/sort; the console handles user input. See `project/smartcare/`.] |
| Design trade-off | [One shared in-memory store keeps the course app small and lets services and queries see the same objects. The trade-off is that records disappear on exit; persistent storage is intentionally outside the revised requirements.] |
| Meaningful test and its limits / 100 percent coverage | [The same-practitioner conflict regression checks a booking rule that previously failed; a test passing does not prove other date, state or console paths are safe. Even 100% line coverage would not prove correct assertions or real-world readiness. See `project/tests/test_regressions.py`.] |
| Diagnosed defect and verification | [In Stage 8, the practitioner conflict check used the wrong practitioner comparison and allowed conflicting bookings; cancelled appointments also failed the retained-history lookup. Focused regression tests exposed these faults, and later common regression runs passed. See [Stage 8 evidence](../stage08/stage08_activities_and_evidence.md).] |
| Shared store and session-state/query responsibilities | [All services use the same `SmartCareDataStore` for current-session records. Lookup returns the stored appointment, while `appointment_sort_key` and `select_appointments` are pure query helpers that select and order explicitly provided appointments without changing them.] |
| What would break if session-state lookup/query responsibilities changed? | [Services might disagree about whether an appointment exists, cancellation history could disappear from lookup, and listings could become out of sync or mutate stored records. FR-07, FR-09 and query purity/order tests would need rechecking.] |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | [An `Appointment` can validate its own status transition to CANCELLED. It cannot know other appointments in the clinic, so `AppointmentService` checks practitioner/time clashes through the shared store before booking or rescheduling.] |
| FR-07 retained history test | [Cancel A1, then look up A1 by the same ID: it must still exist with CANCELLED status. The attached console log shows this, and `test_f8_02_cancelled_appointment_remains_accessible` in `project/tests/test_regressions.py` was written for the earlier defect.] |
| Actual AI change rejected/modified or honestly accepted with verification | [response] |
| Unresolved limitation / future production work | [Current-session data only, naive minute-precision times and no production access control. Real deployment would require secure storage, roles/privacy protections, timezone policy, concurrency and operational validation.] |
| Personal implementation contribution | [response] |
| Personal test/review/design/integration contribution | [response] |
| PG agentic change and rescheduling verification | [Alvin's PG Stage 10 added `Appointment.reschedule()` and `AppointmentService.reschedule_appointment()`. Earlier evidence records 13 rescheduling tests for identity preservation, conflict handling, no-op and other boundary cases; see [Stage 10 PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13) and [tests](../project/tests/test_rescheduling.py).] |
| PG responsible-AI risk/remediation or supported no finding | [response] |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: [response or not undertaken]
Separate reflection / peer / common team viva evidence links and routing: [response]
No further coding stage. Later corrections use the published assessment process.
