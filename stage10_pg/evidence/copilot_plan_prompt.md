# Prompt

Goal: add appointment rescheduling only to our existing SmartCare.
Use RES-01 to RES-06, with RES-05-R2 session visibility.
Only SCHEDULED targets may move. Preserve the same appointment,
ID and participant objects. Reject unknown IDs, invalid times
and another SCHEDULED same-practitioner/time conflict.
Exclude the target itself; permit a valid same-time no-op.
Failures must not mutate state. Release the old slot on success;
lookup and ordered listing must show the new time in this session.
Use the current domain, service and SmartCareDataStore contracts.
Expected code: domain.py, services.py, tests/test_rescheduling.py.
Reuse the existing conflict helper and datetime validation.
No storage/schema/repository redesign, notifications, billing,
authentication, patient self-service, recurring appointments,
external packages/frameworks or unrelated participant changes.
Keep cancellation/history and all correct common tests unchanged.
Use synthetic data only. No console extension is required.
First inspect the repository and propose a plan ONLY. List each
step, requirement, reason, affected file and verification case.
Do not edit files or execute commands until I approve the plan.
After approval, implement only the approved scope and tests.
Request review before expanding scope. Do not weaken assertions.
Summarise actual changed files, test commands/results and concerns.
Stop for human review; do not commit, merge or deploy autonomously.