# ADR 0017 — The gate table is the frame, and the tier sets how many gates

**Status:** accepted · **Date:** 2026-09-04 · **PR:** [#6](https://github.com/kremniov/sdd/pull/6)

## Context

The method's frame was the tier table. It said how much process a task gets, and
everything else — when the user reads something, when the agent may proceed —
was distributed through the prose around it.

Two field observations trace to that. Tier 0 was the only sizing call the agent
made silently: tier 1 and tier 2 both surface the tier because they produce an
artifact the user reads, while tier 0 produced none and the agent started coding
with no reply. And the point at which a branch is handed over was described in
three separate paragraphs, one of which grouped `push` and `gh pr create` with
`git merge` and forbade all three.

A gate table states the same method as four rows: the gate, what the user
approves, and what the agent does next. Each row is one stop, and the row for
handing over says plainly what happens there.

## Decision

The frame is a table of four gates.

| Gate | What the user approves |
|---|---|
| G1 | The tier, and the decisions of the brainstorm |
| G2 | The design |
| G3 | The plan |
| G4 | The pull request |

The tier table stands, unchanged in substance, and now says how many gates a task
passes: tier 0 passes G1 and G4, tier 1 adds G2 as a paragraph in the
conversation, and tier 2 passes all four.

G1 exists at every tier. A task with nothing left to decide has an empty
brainstorm, and G1 is then the tier alone.

G4 ends with the agent pushing the branch, opening the pull request and stopping.
Integration stays with the user (ADR 0010).

## Alternatives

- **Gates on tier 2 only.** Leaves tier 0 sizing itself silently, which is the
  behaviour this decision exists to fix.
- **A separate gate for the sizing call.** Five gates where four carry the same
  rule; G1 already stops before any work begins.
- **Gates instead of tiers.** One path for every task. The tier table was earned
  (ADR 0012) and buys down process on work that has nothing left to decide.

## Consequences

The gate number becomes the unit both parties name — "we are at G2" says what
the branch holds and what happens next. `/sdd:work` carries the table, and the
status record the agent keeps names the gate that is passed.

ADR 0012 stands. What changed is that the tier now has one consequence stated in
one place, instead of being the frame everything else hung from.
