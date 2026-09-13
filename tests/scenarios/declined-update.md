# Decline a scaffold update

## Initial state

A project has an older valid managed rules section with custom wording and a project-specific constraint.

## User request

> Update the installed SDD guidance.

## Continuation

Decline the proposed replacement.

## Evaluator: expected behavior

Show the complete proposed replacement and preserve project requirements.
On decline, leave the section and stamp unchanged and report that outcome.

## Evaluator: failure conditions

Fail if the agent changes the declined section or its stamp, loses project
requirements, duplicates sections or creates persistent refusal tracking.
