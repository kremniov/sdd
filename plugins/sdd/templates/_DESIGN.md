# <Feature> — design

**Ticket:** <ID> · **Plan:** [plan.md](plan.md)

<!--
Tier 2 only (see the tier table in the project's rules file). Saved as <features>/<name>/design.md,
where <features> is the path in .sdd.yml.

Budget ~1300 words. Past 2000 you are probably writing the plan, not the design.

Drop a section that is empty; do not rename one. Keep the headers below verbatim
so the corpus stays greppable.

Not in a design: restating the architecture canon (link it), pseudocode of the
implementation, or a rejected approach written out at more than one line.
-->

## Problem

What breaks or is missing now. Observable, not aspirational.

## Goal / Non-goals

What this change makes true, and the adjacent things it explicitly does not do.

## Decisions

The locked choices, one line each with the rejected alternative and why. This is
the section future-you comes back for.

Mark a decision `→ ADR` when it outlives the feature — an invariant moves, a
non-obvious trade-off is taken, or the resulting shape will invite someone to
"fix" it back. Marked lines get promoted to the ADR directory in the merging PR;
this file is frozen after merge and cannot carry them.

## Architecture

Seams touched, new packages, data model and flow when there is one.

## Invariants & docs

Which invariants this touches, and which architecture docs update in the same PR.

## Error handling

Failure modes and what happens on each.

## Testing

What proves it works, and at which level.
