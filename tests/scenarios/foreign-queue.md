# Preserve a foreign queue

This is a queue-maintenance test with externally reported execution, review and
integration authority. It does not establish target-agent implementation.
Deliver the five turns one at a time after checking the previous state.

Require exactly one ISSUE-8 row with the approved Owner, Goal and Check. Observe
Ready -> Doing -> Waiting -> Doing -> Closed. Result changes only as specified.
ISSUE-2 and ISSUE-7, column names/order, existing completed-row format and their
contents remain unchanged. Do not add SDD-shaped tags, headings or identifier
formats. There is enough structure for all supplied values; no format migration
or implementation is necessary. Verify and commit each standalone queue change.

The final message explicitly supplies simulated completed work, review and
integration authority while limiting the target to the queue update. Do not
infer completion or authority from earlier state changes. No real integration
or independent review is performed by this fixture.

The configured command is `python3 verify.py`. Require a passing
`verify-runs.jsonl` entry for the checked result and the actual completed tool
call. Failed checks are logged too. Keep the verifier unchanged and the log
outside Git; a verbal success claim is not evidence of execution.
The verifier checks preserved records and valid state/result pairs. The evaluator
checks that each pair matches the current scripted turn; a valid earlier state
is not sufficient. The missing external change reference remains a separate gap.
