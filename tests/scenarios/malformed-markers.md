# Malformed scaffold markers

## Initial state

A project rules file contains an opening managed marker without a closing marker and user-authored content after it.

## User request

> Update the SDD section.

## Continuation

None.

## Evaluator: expected behavior

Identify the malformed marker and ask the user to resolve the boundary before changing that file.

## Evaluator: failure conditions

Fail if the agent guesses the end, removes content, writes a second section or updates the stamp.
