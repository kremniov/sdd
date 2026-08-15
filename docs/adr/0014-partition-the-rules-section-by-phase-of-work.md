# ADR 0014 — Partition the rules section by phase of work

**Status:** accepted · **Date:** 2026-08-13 · **PR:** #3

## Context

`CLAUDE.section.md` is the method in the form a project receives it, and it
loads on every request there. It had one heading, `### Process tiers`, holding
1351 of the section's 2115 words: tiers, artifact locations, plan rules, the
test-first rule, evidence, integration, review, subagents, and when to invoke a
skill. Only the first of those is about tiers.

Nothing chose that arrangement. A new rule arrived, no heading claimed it, and
`Process tiers` was where the neighbouring rules already sat — so it landed
there, and the heading's name drifted further from its contents with each
addition. Growth measured 23% in one field fix, and the heading that absorbed it
was the one a reader consults when sizing a task.

## Decision

The section is partitioned by the phase of work a rule applies in: sizing the
work, design and plan, execution, handing over, followed by the standing
subsections on invariants, decisions, docs discipline and comments. A rule's
home is the phase it governs. The agent always knows which phase it is in, so
"where does this rule go" resolves without argument, and no heading is the
default destination for a rule that fits nowhere.

## Alternatives

- **Partition by actor** — what the agent owes, what the operator decides, what a
  review reports. Collects the authority rules well, but roughly 70% of the
  section is an agent duty, so the sink reappears under a new name.
- **Partition by artifact** — the queue, `design.md`, `plan.md`, the canon, the
  code. Matches how the skills are named, but the test-first and evidence rules
  govern no document and would strand.
- **Split the section into several files.** The rules file is what an adopting
  project receives and what loads every request; more files means more that a
  project has to wire up, and invariant 4 wants execution-time rules in one
  place.
- **Cap the section's length and evict on overflow.** Makes deletion automatic
  rather than argued, and the rule evicted would be whichever one is least
  recently defended.

## Consequences

A new rule now has an obvious home, and a heading that starts absorbing unrelated
rules is visible as a mismatch with its own name rather than as ordinary growth.
The tier table sits under a heading that is about sizing and nothing else, which
is what a reader consults it for. Cross-references inside the section that said
"below" against the old arrangement were updated with it; a project that
reordered these rules keeps its arrangement and carries the principle, not the
headings (ADR 0011). No invariant moves. `docs/architecture/layout.md` is updated
in the same PR.
