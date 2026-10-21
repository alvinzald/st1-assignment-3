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
  - [ ] If the patient is registered, looking up their ID returns that same stored patient.
  - [ ] A valid ID that is not registered raises `LookupError`.
  - [ ] A blank, or non-text ID raises `ValueError`.
  - [ ] `PractitionerService.find_practitioner` follows the same three rules for practitioners.
- Scope: 
  - Included: 
    - `PatientService.find_patient`, `PractitionerService.find_practitioner` and their tests in `tests/test_services.py`.
  - Not included: 
    - searching by name, login or password rules, changes to `data_store.py` or `domain.py` and `cancel_appointment`.
- Definition of Done: 
  - [ ] Code is merged into main using a Pull Request.
  - [ ] There is a test for every acceptance criterion and they all pass.
  - [ ] The starter tests still pass.
  - [ ] A teammate has reviewed the code and all feedback is fixed.
  - [ ] Evidence is written in the Stage 6 file.
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
  - [ ] Cancelling a `SCHEDULED` appointment sets its status to `CANCELLED` and returns the same appointment object.
  - [ ] The cancelled appointment can still be found by its ID with status `CANCELLED` (history is kept).
  - [ ] Cancelling a `CANCELLED` or `COMPLETED` appointment raises `ValueError` and leaves its status unchanged.
  - [ ] An unknown appointment ID raises `LookupError`.
  - [ ] A blank or invalid ID raises `ValueError`.
- Scope:
  - Included:
    - AppointmentService.cancel_appointment and its tests in tests/test_services.py.
  - Not included:
    - deleting appointments, setting the status directly in the service, a cancel option in the menu, rescheduling, and changes to booking or conflict checking.
- Definition of Done:
  - [ ] Code is merged into main using a Pull Request.
  - [ ] There is a test for every acceptance criterion and they all pass.
  - [ ] Booking and conflict tests still pass.
  - [ ] A teammate has reviewed the code and all feedback is fixed.
  - [ ] Evidence is written in the Stage 6 file.
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
- Reviewer recheck and approval: [link]
- Merge outcome and SHA: [response]
- Significant Copilot assistance: [summary or none]
- Linked issue closure: [response]
- Each member updated main: [member and confirmation]
- Integrated verification after merge: [command, directory, result and code SHA]


- Issue 2 
PR link and title: [response]
- Linked issue and requirement: Issue #1, 
- Feature branch: [response]
- Changed behaviour: [response]
- Meaningful commits: [links]
- Test command, directory and observed result: [response]
- Another-member reviewer: [response]
- Human observations recorded before Copilot: [link and time]
- Requirement, responsibilities, test assertions and unrelated-scope checks: [response]
- Key feedback: [response]
- Author response/change and verification: [response]
- Reviewer recheck and approval: [link]
- Merge outcome and SHA: [response]
- Significant Copilot assistance: [summary or none]
- Linked issue closure: [response]
- Each member updated main: [member and confirmation]
- Integrated verification after merge: [command, directory, result and code SHA]
## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.
## PR 1 - Patient and Practitioner Lookup
- Member and task: [response]
- Prompt/purpose and relevant issue/diff: [response]
- Summary of output: [response]
- Human check against actual code, requirements and tests: [response]
- Decision — Accept / Modify / Reject: [select]
- Reason: [response]
- Verification/evidence: [link and result]

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
- Human reviewer noticed before consulting Copilot: [response]
- Copilot noticed: [response]
- Overlap: [response]
- What did the human reviewer notice that Copilot did not: [response]
- What did Copilot identify that the human reviewer initially missed: [response]
- Unsupported or incorrect Copilot suggestion: [response or none identified with explanation]
- Human judgement accepted, modified or rejected, and why: [response]
- Which evidence justified merge approval: [response]
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

[response]

## L Stage 6 formative questions

1. What is version control?

[response]

2. Why is a feature branch useful?

[response]

3. What makes a commit a good engineering commit?

[response]

4. What is a pull request?

[response]

5. What is the purpose of code review?

[response]

6. What does a Git diff show?

[response]

7. What is a Definition of Done?

[response]

8. What is the appropriate role of GitHub Copilot in pull-request review?

[response]

9. Why should individual contribution not be judged only by commit count?

[response]

10. What is the Stage 6 engineering rule?

[response]

## M Completion and handover

- Starting SHA: [response]
- Final Stage 6 code SHA: [response]
- Test command: [response]
- Working directory: [response]
- Observed result: [response]
- PR and another-member reviewer: [links]
- Unresolved issue or none: [response]
- Stage 7 handover status: [ready for tutor checkpoint / unresolved work]
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
