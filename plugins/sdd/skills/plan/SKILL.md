---
name: plan
description: Use after gate G2 on a tier-2 task, to sequence an agreed design into plan.md — ordered steps, each with a goal, its constraints, what it touches, and a runnable definition of done. Ends at gate G3, where the user approves it.
---

# The plan

`plan.md` sequences the work. It does not contain the work. `/sdd:work` carries
the gates, the blockers and the handing-over rules.

Write it once `design.md` is settled and committed. Tier 2 only.

Paths come from `.sdd.yml`: `features:` and `verify:`. One `key: value` per line;
everything from the first `#` is a comment; values are used verbatim. If the file
is absent, say so and stop — the project has not adopted this method
(`/sdd:setup`). If a key this skill needs is absent or empty, name the key and
ask.

## Writing it

1. Read the committed `design.md`. The plan executes it and re-decides nothing.
2. Write `<features>/<feature-name>/plan.md` from
   `${CLAUDE_PLUGIN_ROOT}/templates/_PLAN.md`. Read the skeleton in place.
3. Make one step one commit, or one tight group of commits. Order the steps and
   say what forces the order.
4. Ship each module with its tests in the same step.
5. Name the blockers this work is likely to meet, from the list in `/sdd:work`.
6. Ask the user to read it. This is G3.

## What a step carries

| Part | Content |
|---|---|
| Goal | The observable change, in one sentence |
| Constraints | The invariants and design decisions this step holds, linked |
| Touches | Packages and files, with the signatures or schema it introduces |
| DoD | A command, and what its output must show |

A definition of done is runnable. A test name, a lint target, a migration that
applies and rolls back — something a machine decides. A step whose DoD is the
whole suite writes the `verify:` command.

A step carries exported signatures and types, schema, an API fragment, an event
payload shape, or a config key, because each of those is a seam decision. Keep
one where deleting it leaves a question about a seam open. Cut one that only
saves typing.

A step carries no function bodies. It names what becomes true, under which
constraints, and how that gets checked.

## Gates inside a plan

A commit boundary is a commit boundary. Append `[gate]` to the heading of a step
that genuinely needs the user's hands, and that step alone pauses.

## The last step

The last step leaves a merge-ready branch. Integration is never a step, and
approval given at G3 reaches nowhere near it. `/sdd:work` carries what happens
from there.

## Budgets

| Measure | Budget |
|---|---|
| Length | one screen per step; 400 lines for the file |
| Headings | one per step |
| Rationale | the Order section, and nowhere else |
