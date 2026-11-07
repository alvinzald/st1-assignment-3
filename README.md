# Software Technology 1 Assignment 3

One group repository and one evolving SmartCare application.

SmartCare is a Python-based appointment management application developed incrementally from Stage 6 onwards, following the SmartCare A3 Requirements Baseline 2026, Revision 2. The application supports patient and practitioner registration, appointment booking, cancellation, lookup, filtering and sorting. Stage 10 added appointment rescheduling, and Stage 11 added responsible AI assurance and regression tests as postgraduate work.

## Group index

- Group and tutorial: Wed 4:30 - 6:30 Group 6
- Member names, GitHub usernames and UG/PG cohorts:
  - Member 1: Noor Anwari, [nooranwari](https://github.com/nooranwari), UG
  - Member 2: Alvin Zaldivar, [alvinzald](https://github.com/alvinzald), PG
  - Member 3: Kaneez Fiza, [u3327559](https://github.com/u3327559), UG
- Shared repository URL: [https://github.com/alvinzald/st1-assignment-3](https://github.com/alvinzald/st1-assignment-3)
- Latest completed and integrated PG stage: Stage 11 ([PR #14](https://github.com/alvinzald/st1-assignment-3/pull/14)).
- Next stage: Stage 12 final release. UG members may work from the protected Stage 9 common checkpoint.
- Verified common Stage 9 SHA: `299607323d5258b6c5a1c1af86cd94726abe7e16`
- Integrated Stage 10 SHA: `8785aa5ca9195677d47ec87461e1d5dec8279c8b` ([PR #13](https://github.com/alvinzald/st1-assignment-3/pull/13))
- Integrated and tested Stage 11 SHA: `15b4833659840e7ce8f81fb461b0eefdcd98a4ab` ([PR #14](https://github.com/alvinzald/st1-assignment-3/pull/14))
- Test commands, working directory and observed results:
  - Working directory: `project/`
  - Protected common tests: `python -m pytest -q --ignore=tests/test_assurance.py --ignore=tests/test_rescheduling.py` — 37 passed
  - Stage 10 rescheduling tests: `python -m pytest -q tests/test_rescheduling.py` — 13 passed
  - Stage 11 assurance tests: `python -m pytest -q tests/test_assurance.py` — 2 passed
  - Full integrated suite: `python -m pytest -q` — 52 passed
- Review limitation: Stage 10 and Stage 11 were self-reviewed and tested by the responsible PG student. Independent review by another person was not obtained; this is recorded in the stage evidence.
- Final submitted SHA: Obtain the latest `main` SHA at Stage 12 release using `git rev-parse HEAD`. Later documentation-only commits are separate from the tested Stage 11 code SHA above.

Do not include student IDs, private peer ratings, credentials or personal contact details in this README.

## Complete package and stage sequence

All Assignment 3 materials were provided at the beginning, including the Overview, Git/GitHub Group Guide, Stage 6–12 handouts, SmartCare starter, activity/evidence records and assessment instructions.

Development follows the stage sequence, with each applicable stage integrated, verified and documented before progressing.

UG: 6 → 7 → 8 → 9 → 12

PG: 6 → 7 → 8 → 9 → 10 → 11 → 12

Stages 6–9 established the common SmartCare application:
- Stage 6: Implemented core service operations and established the team development workflow.
- Stage 7: Added domain and service tests to verify functional requirements.
- Stage 8: Diagnosed and corrected defects, added regression tests and performed bounded refactoring.
- Stage 9: Implemented appointment queries, service listing and interactive console integration.

Stages 10 and 11 are PG-only extensions:
- Stage 10: Added guarded appointment rescheduling through `Appointment.reschedule()` and `AppointmentService.reschedule_appointment()`. The feature supports valid appointment moves, scheduling conflict prevention, identity preservation and current-session visibility. Human review resulted in corrected method signatures and additional boundary tests. The changes were merged and passed integrated testing; independent approval was not obtained.
- Stage 11: Reviewed the application and Copilot-assisted work for correctness, privacy, dependencies, architecture and test quality. Added two assurance tests covering rescheduling followed by cancellation and patient lookup isolation across data stores. No production defect was confirmed and no production code changes were required. The changes were merged and all 52 tests passed on the integrated code. Independent approval was not obtained.

Stage 12 covers the final release, including verification of the integrated application, documentation, source ZIP and submitted Git SHA.

The group maintains one repository and one evolving `project/` directory throughout development. Previous tests, evidence records and Git history are retained.

As this is a mixed UG/PG group, the verified Stage 9 common SHA is preserved so undergraduate members can complete Stage 12 independently of the postgraduate extensions. UG participation in Stages 10 and 11 is voluntary.

GitHub Copilot was used in PyCharm for Stage 10 implementation assistance and a read-only Stage 11 assurance audit. Significant AI suggestions, human decisions and limitations are documented in the corresponding stage evidence records.

## Application and evidence

- [Application setup and commands](project/README.md)
- [Stage 6 activities and evidence](stage06/stage06_activities_and_evidence.md)
- [Stage 7 activities and evidence](stage07/stage07_activities_and_evidence.md)
- [Stage 8 activities and evidence](stage08/stage08_activities_and_evidence.md)
- [Stage 9 activities and evidence](stage09/stage09_activities_and_evidence.md)
- [Stage 10 PG activities and evidence](stage10_pg/stage10_activities_and_evidence.md)
- [Stage 11 PG activities and evidence](stage11_pg/stage11_activities_and_evidence.md)
- [Stage 12 activities and evidence](stage12/stage12_activities_and_evidence.md)

Git commands run from the repository root. Application commands run from `project/`:

```sh
cd project
python main.py
python -m pytest
cd ..
```

To run the PG extension and assurance tests separately:

```sh
cd project
python -m pytest -q tests/test_rescheduling.py
python -m pytest -q tests/test_assurance.py
cd ..
```

Development and testing have been performed using Python 3.14.7 and pytest 8.3.5. The application uses an in-memory data store, so appointment information is retained only during the current program session.

Use synthetic data only. All significant AI-assisted changes must be reviewed, verified and documented in the corresponding stage evidence records.