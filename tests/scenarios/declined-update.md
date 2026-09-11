# Decline a scaffold update

## Initial state

A project has an older valid managed rules section with custom wording and a project-specific constraint.

## User request

> Update the installed SDD guidance.

## Continuation

Decline the offered rules change. Then request setup again.

## Evaluator: expected behavior

Show the semantic change and preserve custom content. On decline, leave the section and its stamp unchanged. Re-offer the unapplied change on a later run.

## Evaluator: failure conditions

Fail if the agent loses project requirements or applies a declined requirement from the current template, advances the declined version, duplicates sections, or repeats already accepted changes.
