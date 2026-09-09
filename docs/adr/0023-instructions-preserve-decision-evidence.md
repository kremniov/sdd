# ADR 0023 — Instructions preserve decision evidence

**Status:** accepted · **Date:** 2026-09-08 · **PR:** [#6](https://github.com/kremniov/sdd/pull/6)

## Context

Removing all context loses constraints, while repetition counts and failed-fix
counts do not prove architectural conclusions.

## Decision

Keep context needed to choose correctly. Read approved discussion decisions
before design. Templates use sufficient-content questions without minimum
counts. Canon distinguishes behavior from accepted obligations; three failed
fixes trigger discussion, not a diagnosis. Amend ADRs 0003 and 0015.

## Consequences

Invariants 6 and 7 require evidence and useful conditions. Historical
explanation stays in decision records; necessary rationale may remain with an
action.
