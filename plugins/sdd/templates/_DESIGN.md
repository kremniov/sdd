# <Feature> — design

**Ticket:** <ID> · **Plan:** [plan.md](plan.md)

<!--
Tier 2 only. Saved as <features>/<name>/design.md, where <features> is the path
in .sdd.yml.

Budgets: 1300 words, hard stop 2000. Twelve headings. One sentence of rationale
per decision.

Keep the headers below verbatim, so the corpus stays greppable. Drop a section
that has no content; rename none.

Out of a design: the architecture canon, which gets a link; pseudocode of the
implementation; and a rejected approach written past one line.
-->

## Problem

What breaks or is missing now. Observable, not aspirational. Closes at three to
six sentences, or at a table of the observed behaviours and their causes.

## Goal / Non-goals

What this change makes true, and the adjacent things it leaves alone. Closes at
two lists of three to six lines.

## Decisions

One line per locked choice: the choice, the alternative it beat, and the cost
that decided it. Closes at five to twelve lines. Mark a decision `→ ADR` where it
outlives the feature; the merging pull request writes the record.

Watery:

> We looked at several ways of handling partial failures and, after some
> discussion of what comparable tools do and what users would expect, decided
> that per-row outcomes are probably the better fit here, although fail-fast with
> a clearer message also has something going for it and may be worth revisiting.

Tight:

> Per-row outcomes, over fail-fast with a better message: a 10,000-row upload has
> to survive one bad row.

## Architecture

The seams touched, the packages added, the data model, and the flow through it.
Closes at one numbered path end to end, plus a line per seam.

## Invariants & docs

The invariants this work touches, and the canon documents that update in the same
pull request. Closes at one line each.

## Error handling

Each failure mode and what happens on it. Closes at a two-column table.

## Testing

What proves it works, and at which level. Closes at one line per level.
