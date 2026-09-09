# ADR 0018 — The rules file keeps what holds with no skill loaded; the rest moves into a skill

**Status:** accepted · **Date:** 2026-09-04 · **PR:** [#6](https://github.com/kremniov/sdd/pull/6)

## Context

Invariant 4 said that execution-time rules live in the project's rules file,
because a skill loads on a trigger and the rules have to be in context while the
code is being written.

That reading grew the resident text to 1693 words. One field fix added 397 more.
The harness reports a capacity of roughly 150 to 200 instructions and spends
about 50 of them itself, so every rule added there weakens the rules already
there — including the ones that were added for the same reason.

The reading was also too wide. Most of what sat in the file was needed at a
specific moment of a specific task: the tier table at pickup, the plan rules
after a design, the review scales at handing over. A skill invoked when the task
starts is in context for all of them.

## Decision

The project's rules file carries what must hold in a session where nobody invoked
a skill. That is five things: the user integrates the branch and the agent stops
at the pull request; evidence is shown and named before a completion claim; a
test is watched failing before the code that passes it; the comments rules; and
a line saying to invoke `/sdd:work` when a task starts.

Everything else moves into `/sdd:work`: the gate table, the tier table, the
artifact locations, the plan rules, the blockers, the review scales, and the
invariant, decision-record and docs triggers.

Each rule has one home. The resident file names the skill and does not summarise
it.

Invariant 4 is reworded from "execution-time rules live in the rules file" to "a
rule holds where it is loaded", with the test being whether the rule still has to
hold with no skill loaded.

## Alternatives

- **Keep everything resident.** The measured cost is a diluted instruction
  budget and a section that grows with every fix.
- **A separate `/sdd:method` skill, with `/sdd:work` as a thin dispatcher.**
  Splits the frame across two loads to no benefit; the frame is read at once.
- **Distribute the rules across the skills that use them.** Leaves no single
  place where the method can be read whole.
- **Put the rules in the agent's memory.** Memory becomes a fourth home for
  them, and a fourth text that drifts from the other three.

## Consequences

The resident section drops from 1693 words to 268, and its negation density from
3.5 to 1.5.

The method now depends on `/sdd:work` being invoked. The resident set says to
invoke it, and the agent keeps one status record in memory naming the branch, the
gate and the current step, so a context compaction ends in re-invoking the skill
rather than in continuing without it.

Skill text that a compaction drops is a real risk and the reason the resident set
exists at all. What stays resident is chosen so that a session that loses the
skill still cannot merge a branch, still cannot claim a green run it did not
watch, and still knows what to load.
