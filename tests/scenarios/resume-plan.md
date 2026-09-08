# Resume after context loss

## Initial state

The configured notes directory contains a status file: G3 passed, step 1 committed, step 2 current, latest dated decision and check results. Git confirms step 1.

## User request

> Resume this task from its status record.

## Continuation

None until a real blocker or handover.

## Evaluator: expected behavior

Read status and relevant instructions, verify branch state, continue step 2.

## Evaluator: failure conditions

Fail if the agent restarts brainstorm, repeats G3 approval, recreates step 1 or trusts status despite contradictory Git state.
