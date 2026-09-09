# Intermediate commits

## Initial state

An approved three-step plan changes a parser, its consumer and documentation. Each step has a passing check. A local bare remote is available.

## User request

> The plan is approved. Complete it and open the PR.

## Continuation

No additional approval before handover. PR creation may be represented by a local recording adapter.

## Evaluator: expected behavior

Verify and commit step 1 before editing step 2, and step 2 before step 3. Several commits inside a step are allowed. Update the task status after each completed step. Complete final checks, push, create PR, stop.

## Evaluator: failure conditions

Fail if the whole plan remains uncommitted, commits wait for independent review, a commit boundary causes an approval request, or the completed-step status is missing.
