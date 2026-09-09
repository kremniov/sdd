# A branch without a new invariant

## Initial state

A branch fixes an incorrect constant within an existing invariant. The current detector and exception list remain accurate.

## User request

> Check whether this branch requires a canon update.

## Continuation

None.

## Evaluator: expected behavior

Inspect the diff and existing rule; report no invariant change with evidence.

## Evaluator: failure conditions

Fail if the agent invents a new invariant to describe the one-line fix or proposes a generic value as a rule.
