# <Feature> — plan

**Ticket:** <ID> · **Design:** [design.md](design.md)

<!--
Tier 2 only. Saved as <features>/<name>/plan.md, next to the design it executes.

Budgets: one screen per step, 400 lines for the file. One heading per step.
Rationale belongs in Order and nowhere else.

Keep the headers below verbatim, so the corpus stays greppable.

Approving this plan authorizes every step in it, up to a merge-ready branch.
Integration is never a step. /sdd:work carries the rules for both.
-->

## Scope

What ships when the last step is green, and the design it executes. Name what is
left for a follow-up ticket. Closes at one paragraph.

## Order

What forces this sequence — the dependency, the checker, the migration that has
to land before the code that reads it. Say which steps are independent. Closes at
one paragraph.

## Steps

### Step N — <what becomes true>

**Goal:** the observable change, in one sentence.

**Constraints:** the invariants and design decisions this step holds. Link them.
One line each.

**Touches:** packages and files, with the exported signatures or schema this step
introduces.

**DoD:** the command that proves it, and what its output must show.

Watery:

> Refactor the importer so that it handles rows more gracefully, add the
> necessary tests, and make sure everything still works as expected afterwards.
> This is the biggest step and it will probably need care around the existing
> batching logic, which we should look at while we are in there.

Tight:

> **Goal:** a failing row leaves the other rows imported.
> **Constraints:** invariant 4; the per-row outcome decision in design.md.
> **Touches:** the importer's row loop — `import(rows)` returns one outcome per
> row.
> **DoD:** the partial-failure test passes; the `verify:` command is green.

## Verification

The gate for the branch as a whole: the `verify:` command, anything this branch
needs beyond it, and the manual check if there is one, naming who runs it.

## Docs & ADR

Which canon documents update in the same pull request, and which design decisions
marked `→ ADR` need a record written before the merge.
