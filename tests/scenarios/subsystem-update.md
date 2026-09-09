# Update a changed interaction

## Initial state

A branch changes the order between durable write and event publication. The subsystem document still describes the old order. The intended order is agreed.

## User request

> Update the subsystem document to match this change.

## Continuation

Approve the concrete edit proposal before changes.

## Evaluator: expected behavior

Trace the code path, correct the ordering and its contract, retain unrelated content and link governing invariants.

## Evaluator: failure conditions

Fail if the agent copies a file inventory, appends contradictory text without correcting the old claim, or rewrites unrelated sections.
