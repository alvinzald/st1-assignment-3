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
| PG RES and assurance integration | [Stage 10 rescheduling tests and Stage 11 assurance tests.] | [response] | [alvin] | [response] | [response] |


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
| Purpose and included common/PG scope | [project/README.md] | [Noor] | [response] |
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

Delivered features: [response]
Important fixes: [response]
Architecture/quality improvements: [response]
Known limitations: [response]
AI-assisted development note: [response]

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Session-only synthetic data and minute-precision local time: [response]
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: [response]
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: [response]
Difference between accepted scope limit and unresolved required behaviour: [response]
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
Candidate recovery plan / known-good SHA: [response]
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

Strongest evidence SmartCare is ready: [response]
Weakest area: [response]
How AI use changed from Stage 1 to Stage 12: [response]
Start doing — engineering and AI use: [response]
Stop doing — engineering and AI use: [response]
Continue doing — engineering and AI use: [response]
What worked / caused rework / future delivery improvement: [response]
One paragraph — If AI can write code why do we still need software engineers: [response]

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | [response] |
| Two requirements and acceptance criteria | [response] |
| Domain model and architecture | [response] |
| Design trade-off | [response] |
| Meaningful test and its limits / 100 percent coverage | [response] |
| Diagnosed defect and verification | [response] |
| Shared store and session-state/query responsibilities | [response] |
| What would break if session-state lookup/query responsibilities changed? | [response] |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | [response] |
| FR-07 retained history test | [response] |
| Actual AI change rejected/modified or honestly accepted with verification | [response] |
| Unresolved limitation / future production work | [response] |
| Personal implementation contribution | [response] |
| Personal test/review/design/integration contribution | [response] |
| PG agentic change and rescheduling verification | [response] |
| PG responsible-AI risk/remediation or supported no finding | [response] |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: [response or not undertaken]
Separate reflection / peer / common team viva evidence links and routing: [response]
No further coding stage. Later corrections use the published assessment process.
