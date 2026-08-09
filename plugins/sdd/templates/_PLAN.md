# <Feature> — plan

**Ticket:** <ID> · **Design:** [design.md](design.md)

<!--
Tier 2 only (see the tier table in the project's rules file). Saved as <features>/<name>/plan.md,
where <features> is the path in .sdd.yml. Written after design.md is settled;
this file sequences the work, it does not re-decide it.

**Approving this plan authorizes every step in it.** Execution stops only on a
red DoD, on a decision the design does not cover, or at a step marked `[gate]` —
a check the operator runs by hand. Anything else is a step, not a question.

**Mirror the steps into the task tool** at the start of execution: one task per
step, in order, marked in-progress when it starts and completed when its DoD is
green. The plan is the contract; the task list is where its progress is readable
while the branch is being written.

**No implementation bodies.** A step names what must become true, under which
constraints, and how that is checked — not the code that gets there. Writing the
implementation twice fixes it at the moment least is known about it, and the
first version arrives at execution looking like an agreed commitment.

What a step MAY carry, because these are interface decisions rather than a
draft: exported signatures and types, schema, an API fragment, an event payload
shape, a config key. Rule of thumb: if deleting it would leave a question about
a seam unanswered, keep it; if it would only save typing, cut it.

Budget: one screen per step. A plan past ~400 lines is describing code.

Keep the headers verbatim so the corpus stays greppable.
-->

## Scope

One paragraph: what ships when the last step is green, and the design.md it
executes. Name what is deliberately left for a follow-up ticket.

## Order

Why the steps run in this order — the dependency that forces it (a migration
before the code that reads it, a seam before its callers). Say if steps are
independent and may be parallelized.

## Steps

Repeat per step. Number them; a step is a commit, or a tight group of commits.
A commit boundary is not a checkpoint — append `[gate]` to the heading of a step
that genuinely needs the operator, and only that step pauses.

### Step N — <what becomes true>

**Goal:** the observable change, one sentence.

**Constraints:** the invariants and prior decisions this step must hold, one
line each. Link the design.md decision or the invariant rather than restating
the reasoning.

**Touches:** packages and files, with the exported signatures or schema this
step introduces or changes.

**DoD:** the command that proves it, and what its output must show. A test name,
a lint target, a migration that applies and rolls back — something runnable, not
"works correctly". A step whose DoD is the whole suite writes the `verify:`
command from `.sdd.yml`.

## Verification

The gate for the branch as a whole: the `verify:` command from `.sdd.yml`, plus
anything this branch needs beyond it, and the manual check if any (naming who
runs it).

## Docs & ADR

Which architecture docs update in the same PR, and which design.md decisions
were marked `→ ADR` and therefore need one written before merge.
