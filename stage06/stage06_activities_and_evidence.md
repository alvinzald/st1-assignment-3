# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: Wed 4:30-6:30, Group 6
- Members, GitHub usernames and cohorts: 
  - Member 1: Noor Anwari, [nooranwari](https://github.com/nooranwari), UG 
  - Member 2: Alvin Zaldivar, [alvinzald](https://github.com/alvinzald), PG 
  - Member 3: Kaneez Fiza, [u3327559](https://github.com/u3327559), UG
- Repository URL: [https://github.com/alvinzald/st1-assignment-3](https://github.com/alvinzald/st1-assignment-3)
- Starting SHA: 9e5cc239878432cdfe6badecce52c9285ec61f79

## A Requirement to issue activities

### FR-02 Patient Search

- Title: Find a patient or practitioner by ID
- Context: 
  - Right now `PatientService.find_patient` is not written. 
  - It only raises `NotImplementedError`, so staff cannot get a registered patient by their ID.
  - The data store returns None for an unknown ID, but the service should raise `LookupError`.
  - `PractitionerService.find_practitioner` is also not written and follows the same pattern, so it is covered here as a supporting operation.
- Requirement: FR-02 (AC-02.1, AC-02.2), FR-03 is practitioner registration.
- Acceptance criteria:
  - [x] If the patient is registered, looking up their ID returns that same stored patient.
  - [x] A valid ID that is not registered raises `LookupError`.
  - [x] A blank, or non-text ID raises `ValueError`.
  - [x] `PractitionerService.find_practitioner` follows the same three rules for practitioners.
- Scope: 
  - Included: 
    - `PatientService.find_patient`, `PractitionerService.find_practitioner` and their tests in `tests/test_services.py`.
  - Not included: 
    - searching by name, login or password rules, changes to `data_store.py` or `domain.py` and `cancel_appointment`.
- Definition of Done: 
  - [x] Code is merged into main using a Pull Request.
  - [x] There is a test for every acceptance criterion and they all pass.
  - [x] The starter tests still pass.
  - [x] A teammate has reviewed the code and all feedback is fixed.
  - [x] Evidence is written in the Stage 6 file.
- Owner: [Noor Anwari](https://github.com/nooranwari)
- Actual issue link: [https://github.com/alvinzald/st1-assignment-3/issues/1#issue-5908488276](https://github.com/alvinzald/st1-assignment-3/issues/1#issue-5908488276)

### FR-06 Appointment Cancellation with FR-07 retained history

- Title: FR-06/FR-07 Appointment Cancellation: cancel and keep history
- Context:
  - Right now `AppointmentService.cancel_appointment` is not written.
  - The rule is already in `Appointment.cancel()` in `domain.py`.
  - The service should find the appointment and use that method, not repeat the rule.
- Requirement: FR-06 and FR-07
- Acceptance criteria:
  - [x] Cancelling a `SCHEDULED` appointment sets its status to `CANCELLED` and returns the same appointment object.
  - [x] The cancelled appointment can still be found by its ID with status `CANCELLED` (history is kept).
  - [x] Cancelling a `CANCELLED` or `COMPLETED` appointment raises `ValueError` and leaves its status unchanged.
  - [x] An unknown appointment ID raises `LookupError`.
  - [x] A blank or invalid ID raises `ValueError`.
- Scope:
  - Included:
    - AppointmentService.cancel_appointment and its tests in tests/test_services.py.
  - Not included:
    - deleting appointments, setting the status directly in the service, a cancel option in the menu, rescheduling, and changes to booking or conflict checking.
- Definition of Done:
  - [x] Code is merged into main using a Pull Request.
  - [x] There is a test for every acceptance criterion and they all pass.
  - [x] Booking and conflict tests still pass.
  - [x] A teammate has reviewed the code and all feedback is fixed.
  - [x] Evidence is written in the Stage 6 file.
- Owner: [Noor Anwari](https://github.com/nooranwari)
- Actual issue link: [https://github.com/alvinzald/st1-assignment-3/issues/2#issue-5908596769]([https://github.com/alvinzald/st1-assignment-3/issues/2#issue-5908596769])

## B Commit quality

| Original example | Strong or Weak | Reason |
|---|---|---|
| changes | Weak | it does not explain or describe what was changed |
| final version | Weak | [does not describe] |
| Add patient search by ID | Strong  | Clearly describes the feature added |
| fix stuff | Weak | does not explain what was fixed |
| Prevent cancellation of completed appointments | Strong | Clearly explains the behaviour being changed |

## C Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns:
  - A cancellation PR should only change cancellation.
  - The renamed patient fields, restructured code and new dependency are unrelated, so the PR is bigger and harder to review.
- Responsibility and architecture concerns:
  - Patient owns its fields, and cancellation belongs to `Appointment.cancel()` and the service.
  - Renaming patient fields could break other code that uses them. A new dependency changes what the whole project needs to run.
- Testing and review concerns:
  - Patient owns its fields, and cancellation belongs to `Appointment.cancel()` and the service.
  - Renaming patient fields could break other code that uses them. A new dependency changes what the whole project needs to run.
- Changes to remove or separate, with reasons:
  - Remove the unrelated patient field changes, code restructuring and new dependency. If needed, these should be handled in separate issues and PRs.

## D Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: Copilot has not explained which requirements were checked, which tests passed, or whether the code handles errors correctly.
- Follow-up review question 1: Does patient lookup return the original stored patient object?
- Follow-up review question 2: Does practitioner lookup return the original stored practitioner object?
- Follow-up review question 3: Does cancellation raise an error when the appointment does not exist?
- Follow-up review question 4: Does cancellation prevent completed appointments from being cancelled?
- Follow-up review question 5: Does cancellation keep the appointment in the data store for history?
- Additional questions if useful: NA

## E Team workflow agreement

| Practice | Team agreement |
|---|---|
| Branch naming | Each team member will create a feature branches when necessary. When creating branch, use a clear name such as feature/patient_lookups or feature/find_lookups (it is just an example) |
| Commit message convention | Use short, clear commit messages describing the changes, such as add patient or fix cancellation tests. |
| PR size | Keep pull requests small and focused on one task or feature to make reviewing easier. |
| Another-member review requirement | At least one other team member must review the changes and provide feedback before merging. |
| Merge rule | Merge into the main branch only after tests pass and another team member has reviewed and approved the pull request. |
| Significant Copilot disclosure rule | Any significant use of GitHub Copilot must be recorded in the relevant stage activity/evidence file, including what was suggested, what was accepted or changed, and how it was checked. |

## F Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link | Requirement | Owner | Acceptance criteria or precise link | Status |
|---|---|---|---|---|
| [#1](https://github.com/alvinzald/st1-assignment-3/issues/1#issue-5908488276) | [FR-02/FR-03] | Noor Anwari | Users can search for patients and practitioners using the supported search details. The system returns matching records and handles cases where no match is found. | Open |
| [#2](https://github.com/alvinzald/st1-assignment-3/issues/2#issue-5908596769) | [FR-06/FR-07] | Noor Anwari | Users can cancel an existing appointment. The system updates its status to cancelled and retains the appointment record for history. | Open |

## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

- PR link and title: [Implement patient and practitioner lookup with tests](https://github.com/alvinzald/st1-assignment-3/pull/3)
- Linked issue and requirement: [Issue #1: FR-02 Patient Search, with practitioner lookup as a supporting operation under FR-03](https://github.com/alvinzald/st1-assignment-3/issues/1)
- Feature branch: `feature/find-lookups`
- Changed behaviour:
  - Implemented `PatientService.find_patient()` and `PractitionerService.find_practitioner()`.
  - Both methods now return the stored object for a valid ID and raise LookupError when no matching record exists.
  - Input validation is handled by the existing data store.
- Meaningful commits:
  - [901ccc6](https://github.com/alvinzald/st1-assignment-3/commit/901ccc6b6b29fc6a586d4bede06012c1934c2f15)
  - [30ae137](https://github.com/alvinzald/st1-assignment-3/commit/30ae137e244984f6089566202474690203156813)
  - [391e948](https://github.com/alvinzald/st1-assignment-3/commit/391e9484ee4417ff794c1efdf1d9a11ea346a909)
- Test command, directory and observed result:
  - Test commands: `py main.py` `py -m pytest`
  - Directory: `project/`
  - Observed result: The application ran successfully, and all 10 tests passed (8 starter tests and 2 service tests)
  - Environment: Python 3.14.7 and pytest 9.1.1
  - Tested commit: [391e948](https://github.com/alvinzald/st1-assignment-3/commit/391e9484ee4417ff794c1efdf1d9a11ea346a909)
- Another-member reviewer: [Alvin Zaldivar](https://github.com/alvinzald)
- Human observations recorded before Copilot: [21 Oct 2026 at 14:14](https://github.com/alvinzald/st1-assignment-3/pull/3#pullrequestreview-5594525586)
- Requirement, responsibilities, test assertions and unrelated-scope checks:
  - Checked the lookup methods against Issue #1.
  - Both use the existing data store, return the original objects and raise LookupError for unknown IDs.
  - Tests cover valid and invalid inputs, trimming, case sensitivity and object identity.
  - No issues found in the implementation or tests reviewed so far.
- Key feedback:
  - No significant issues identified with the lookup implementation or tests.
  - All 10 tests passed during independent verification.
  - No code changes requested. Final documentation/scope review and Copilot comparison are still pending.
- Author response/change and verification:
  - No changes requested at this stage; no author response required. Final review pending.
- Reviewer recheck and approval: [link](https://github.com/alvinzald/st1-assignment-3/pull/3#pullrequestreview-5594525586)
- Merge outcome and SHA: [] 
- Significant Copilot assistance: [summary or none]
- Linked issue closure: [https://github.com/alvinzald/st1-assignment-3/issues/1]
- Each member updated main:
  - [x] Alvin
  - [x] Kaneez
  - [x] Noor
- Integrated verification after merge: [command, directory, result and code SHA]


- Issue 2 
PR link and title: [Implement appointment cancellation with tests](https://github.com/alvinzald/st1-assignment-3/pull/6#issue-5957874050)
- Linked issue and requirement: [Issue #2, FR-06/FR-07](https://github.com/alvinzald/st1-assignment-3/issues/2)
- Feature branch: `feature/cancel-appointment`
- Changed behaviour:
  - Cancels a SCHEDULED appointment (status CANCELLED, same object, kept in history)
  - invalid transitions and blank IDs raise ValueError, unknown IDs raise LookupError
- Meaningful commits: [f6222d3 implement appointment cancellation with tests](https://github.com/alvinzald/st1-assignment-3/pull/6/changes/f6222d3b559ddc4f2e1a36ad34a0dc48d62c864d)
- Test command, directory and observed result:
  - `py main.py` `py -m pytest`
  - Directory: ` project/`
  - Observed result: All 13 tests passed (8 starter tests and 5 service tests).
- Another-member reviewer: [Alvin Zaldivar](https://github.com/alvinzald)
- Human observations recorded before Copilot: [22 Oct 2026 at 09:37](https://github.com/alvinzald/st1-assignment-3/pull/6#issuecomment-6328083267)
- Requirement, responsibilities, test assertions and unrelated-scope checks: 
  - Reviewed against Issue #2 (FR-06 and FR-07).
  - Cancellation uses the existing data store and delegates state changes to `Appointment.cancel()`. 
  - Tests cover successful cancellation, retained history, invalid IDs and illegal state transitions. 
  - All 13 tests passed at commit 512e753.
- Key feedback:
  - No significant implementation issues identified.
- Author response/change and verification: 
  - No changes requested at this stage; no author response required. Final review pending.
- Reviewer recheck and approval: [link](https://github.com/alvinzald/st1-assignment-3/pull/6#pullrequestreview-5607143261)
- Merge outcome and SHA: [response]
- Significant Copilot assistance: [summary or none]
- Linked issue closure: [response]
- Each member updated main:
  - [ ] Alvin
  - [ ] Kaneez
  - [ ] Noor
- Integrated verification after merge: [command, directory, result and code SHA]
## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.
## PR 1 - Patient and Practitioner Lookup
- Member and task: [Noor Anwari - run the required Copilot review comparison for PR 2 (cancel_appointment and its tests)]
- Prompt/purpose and relevant issue/diff: [Handout Part H review prompt, with issue #1's criteria (FR-03, FR-02) and the PR 1 diff]
- Summary of output: [Copilot identified possible issues with ID validation, whitespace handling and missing test cases.]
- Human check against actual code, requirements and tests: [Checked services.py, data_store.py and domain.py. Found that required_text() already validates IDs and removes extra spaces. The lookup methods also do not create new records.]
- Decision — Accept / Modify / Reject: [Reject]
- Reason: [Copilot suggested changes to ID validation, but after checking the code, I found that required_text() already handles validation. The existing code meets the requirements, so I did not make any changes.]
- Verification/evidence: [Code checked against the requirements, all tests]

### PR 2 — Appointment Cancellation
Member and task: [response]
- Prompt/purpose and relevant issue/diff: [response]
- Summary of output: [response]
- Human check against actual code, requirements and tests: [response]
- Decision — Accept / Modify / Reject: [select]
- Reason: [response]
- Verification/evidence: [link and result]

## I Human versus Copilot review comparison

## PR 1 - Patient and Practitioner Lookup
- Human reviewer noticed before consulting Copilot: [ The lookup methods return the correct objects and raise LookupError for unknown IDs. The tests also cover valid and invalid IDs.]
- Copilot noticed: [ Copilot identified possible issues with ID validation, whitespace handling and missing test cases.]
- Overlap: [Both checked ID validation and whether the lookup methods work correctly.]
- What did the human reviewer notice that Copilot did not: [The datastore already uses required_text() to validate IDs.]
- What did Copilot identify that the human reviewer initially missed: [None]
- Unsupported or incorrect Copilot suggestion: [Copilot said ID validation was missing, but it is already handled by required_text() in the datastore.]
- Human judgement accepted, modified or rejected, and why: [We rejected the missing validation finding because the datastore already handles it. We accepted that additional tests could improve test coverage.]
- Which evidence justified merge approval: [The lookup methods followed the requirements, the existing tests covered the main cases, and the datastore handled ID validation.]
### PR 2 — Appointment Cancellation
- Human reviewer noticed before consulting Copilot: [response]
- Copilot noticed: [response]
- Overlap: [response]
- What did the human reviewer notice that Copilot did not: [response]
- What did Copilot identify that the human reviewer initially missed: [response]
- Unsupported or incorrect Copilot suggestion: [response or none identified with explanation]
- Human judgement accepted, modified or rejected, and why: [response]
- Which evidence justified merge approval: [response]

## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: [response]
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: [work and evidence]
- Issue refinement: [work and evidence]
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: [work and evidence]

## K Exit question

Why is a high commit count not necessarily evidence of strong contribution?
A high commit count does not always mean a strong contribution because some commits might be small changes. A member with fewer commits might have done more important or difficult tasks. So, we should look at the quality of work, completed tasks and teamwork instead of just counting commits.

[response]

## L Stage 6 formative questions

1. What is version control?

[Version control is a system that tracks changes made to files and code over time.It allows team members to work together, see who made changes, and go back to previous versions if something goes wrong. Git is an example]

2. Why is a feature branch useful?

[A feature branch is useful because it allows teams members to work on changes separately without affecting the main code.]

3. What makes a commit a good engineering commit?

[A good commit has clear changes, a meaningful message, and does not break the existing code.]

4. What is a pull request?

[A pull request is a request to review changes before merging them into the main branch.]

5. What is the purpose of code review?

[Code review helps find mistakes, improve code quality, and make sure the code works correctly before merging.]

6. What does a Git diff show?

[A git diff shows the changes made to the code, inclduing added, removed, or modified lines.]

7. What is a Definition of Done?

[A definition os done is a list of conditions that must be met before a task is considered complete.]

8. What is the appropriate role of GitHub Copilot in pull-request review?

[Github copilot helps review code by suggesting improvements and finding possible issues, but a human reviewer must still check the changes.]

9. Why should individual contribution not be judged only by commit count?

[Because commits are small changes, while others onvolve more difficult tasks. Contribution should be judged by the quality of work, completed tasks and teamwork.]

10. What is the Stage 6 engineering rule?

[The stage 6 engineering rule is to make small, clear and tested changes, review them properly, and keep evidence of the work]

## M Completion and handover

- Starting SHA: [response]
- Final Stage 6 code SHA: [response]
- Test command: [response]
- Working directory: [response]
- Observed result: [response]
- PR and another-member reviewer: [links]
- Unresolved issue or none: [none]
- Stage 7 handover status: [ready for tutor checkpoint ]
- Final submitted SHA if later than tested SHA: [response and evidence-only difference]

- [ ] Three Stage 6 service targets completed and checked.
- [ ] Original supplied tests retained and passing.
- [ ] At least two focused issues link requirements and acceptance criteria.
- [ ] Feature work reviewed by another member using the actual diff.
- [ ] Human-first review and required Copilot comparison recorded.
- [ ] Feedback resolved and approval recorded before merge.
- [ ] Everyone pulled main and integrated checks passed.
- [ ] Required activities, quiz responses and contribution notes completed.
- [ ] Only synthetic data included; confidential peer material kept out.
- [ ] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.
