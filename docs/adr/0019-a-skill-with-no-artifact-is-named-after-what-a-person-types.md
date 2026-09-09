# ADR 0019 — A skill with no artifact is named after what a person types

**Status:** accepted · **Date:** 2026-09-04 · **PR:** [#6](https://github.com/kremniov/sdd/pull/6)

## Context

ADR 0004 names a skill after the artifact or subject it works on. It carried one
stated exception, `debug`, kept because it has no artifact and is what a person
with a failing test would type.

Two things now press on that rule. The method needs an entry point — a skill
invoked when a task starts, which sizes the work, runs the brainstorm and carries
the frame (ADR 0018). It produces no artifact. And `/sdd:design` produced two,
`design.md` and `plan.md`, which was the only place in the corpus where one skill
owned two artifacts.

## Decision

The rule becomes: name a skill after the artifact it works on, and where it has
none, after what a person would type.

Two changes follow.

`/sdd:work` is the entry point. It is invoked when a task starts and carries the
gates, the tiers, the blockers, the review rules and the handing-over rules.

`/sdd:design` splits into `/sdd:design` and `/sdd:plan`, one artifact each. The
boundary between them is gate G2, where the user reads the design, so the split
also matches the point at which a session most often ends.

The plugin ships eight skills: `work`, `design`, `plan`, `tasks`, `canon`,
`subsystem`, `debug` and `setup`.

## Alternatives

- **A prompt template in the scaffold instead of an entry skill.** Answers the
  same need and requires the user to remember where the file is.
- **`/sdd:ticket`.** Named after an artifact, and collides with `/sdd:tasks`,
  which writes tickets.
- **`/sdd:feature`.** Named after the directory it creates, which tier 0 and a
  bug report never create.
- **Keep one design skill.** Fewer files, and it leaves the exception in ADR
  0004 that this branch is amending anyway.

## Consequences

ADR 0004 is amended, not retired: skills are still named after what they work on,
and `debug` stops being an exception because the rule now covers it.

`work` is a verb, like `debug`. Both are what someone types when they have a task
and no artifact yet.

The description of every skill carries the full weight of selection, and there
are now eight of them competing. `/sdd:work` says in its description that it is
invoked before the first edit, because a skill that loads after the code is being
written carries rules that arrive too late.

`./scripts/check.sh` resolves every `/sdd:` reference against the directory
listing, so a name that lands in prose before its directory fails the gate.
