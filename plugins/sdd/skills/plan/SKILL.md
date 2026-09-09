---
name: plan
description: Sequence an approved tier-2 design into verifiable implementation steps and submit the plan for G3 approval.
---
 # Plan

For files intended for Git, follow `/sdd:work` Branch and completion before
editing and when handing over the result.

## Inputs

Begin after G2 with the approved, committed design. `/sdd:work` owns execution,
stop conditions and integration. Read `features` and `verify` from `.sdd.yml`.
Split each line at the first colon and remove comments from the first `#`. If
configuration is absent, offer `/sdd:setup`. Ask for required missing values.

Read the design and `${CLAUDE_PLUGIN_ROOT}/templates/_PLAN.md` in place. Return
a new material decision to the user and update the design before planning its
implementation.

## Write and submit

Write `<features>/<task>/plan.md`. Explain dependencies that determine the order
and identify independent steps. Each step ends in a coherent, checkable result.
A step can contain several commits. Its changes must be verified and committed
before the next step; `/sdd:work` enforces that execution sequence.

| Field | Content |
|---|---|
| Result | Observable change |
| Constraints | Links to design decisions and governing rules |
| Touches | Affected components and files |
| Check | Command and expected output, or manual procedure, expected observation and person who runs it |

Ship behavior and its tests in the same step. Link contracts from the design.
Include enough interface detail to locate the work; leave function bodies out.
Name likely blockers from `/sdd:work`. Mark a required human action with
`[gate]` and state what the user must provide. A commit boundary is not a gate.

Put branch-wide verification after all code and document changes. Use the
configured `verify` command and name any additional checks. Identify required
canon updates and ADRs so they are complete before the final check.

Read the finished plan for missing dependencies, vague checks and decisions that
belong in the design. Present the whole plan at G3. After approval, commit it
and continue through `/sdd:work` if execution is in scope. Otherwise hand over
the approved plan through `/sdd:work` without starting implementation.

## Content budget

Use at most 400 lines as the planning budget. Keep each step brief enough to
assess its result and verification together. Explain ordering in the Order
section and link decision rationale from the design. Empty sections are omitted.
