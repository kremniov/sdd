# <Feature> — design

**Source:** <ticket or user request reference>

<!--
Write under the configured features directory. Keep applicable headings below;
omit empty sections. Aim for at most 1300 words, ceiling 2000, at most 12 headings.
There is no minimum content count. Replace this guidance with the actual design.
Link existing contracts and invariants rather than duplicating them.
-->

## Problem and goal

Describe the observed problem and required result. End when the reader can tell
what must change and how the outcome serves the request.

## Scope

State included work. Name adjacent work only where it could be included by mistake.

## Decisions

State each agreed choice and its decisive constraint. Mark a durable choice
`→ ADR`. Include rejected alternatives when their cost explains the choice.

Example: preserve valid import rows when another row fails. A rejected row must
not discard the valid portion of the upload.

## Structure and contracts

Describe changed boundaries, inputs, outputs, data and interactions. State
ordering when it affects correctness. Link unchanged contracts.

## Failures and transition

Describe failure handling and recovery. Include compatibility and rollout when
the change affects them. Omit topics outside the change.

## Verification and documents

State how to prove the result and relevant failure behavior. Name the affected
invariants, subsystem documents and durable decisions to record.
