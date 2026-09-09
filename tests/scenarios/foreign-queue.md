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
