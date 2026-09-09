# ADR 0024 — Budgets do not prove behavior

**Status:** accepted · **Date:** 2026-09-08 · **PR:** [#6](https://github.com/kremniov/sdd/pull/6)

## Context

The old negation gate could reject precise prohibitions and ignored examples in
its word limits. It did not detect workflow errors.

## Decision

Keep size and heading limits. Count full text for size, including examples.
Report negation frequency as advisory and include reference volume in reporting.
Validate behavior with versioned scenarios. Replace the density gate in ADR
0021.

## Consequences

Invariant 12 separates structural checks, textual walkthroughs and observed
agent runs. Scenario results must state their evidence type.
