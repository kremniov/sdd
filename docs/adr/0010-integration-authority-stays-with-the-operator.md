# ADR 0010 — Integration authority stays with the operator, and independence is defined by input

**Status:** accepted · **Date:** 2026-08-10 · **PR:** #1

## Context

A project running the method took a feature through the full cycle and merged it
into the integration branch without the operator ever being asked. Every rule
the shipped text carries was satisfied: the branch was green, an independent
review had run, the docs discipline held. The agent read the integration
paragraph as a checklist — criteria met, therefore proceed — because the
paragraph listed conditions and the mechanics that follow the decision, and
named no one who makes it.

Four seams let it through, each innocent alone. "Integrating a branch is a
decision, not a step" did not say whose. "An approved plan authorizes every step
in it" met a `/sdd:tasks` rule placing the Done commit "about to merge", so plan
authorization reached across into the merge. `[gate]` is opt-in per step, and
nothing made integration an implicit one or stopped a plan author from writing a
merge step. And "a fresh session on the finished branch" was satisfiable by the
author: the review skill runs as a fork, which continues the author's context
outright, and its subagents read prompts that fork wrote.

That last one matters beyond the merge. The review exists to catch an assumption
shared by the code and the plan; a reviewer reasoning from inside the author's
context shares it too. Both channels — forked context, and the author framing
the prompt — leave the review useful as a quality pass and unfit as the gate.

## Decision

The agent's authority ends at a merge-ready branch. It reports that state with
the review's findings and stops; `git merge`, `gh pr merge` and a push to the
integration branch require the operator's approval of that specific branch, in
words, given after the review results exist. Plan approval and a "go" at the
start of execution are explicitly denied that reach, because both predate the
review. Integration is never a plan step.

Independence is a property of the reviewer's input, not of how the session was
started: the whole input is the repository, and nothing authored by the session
that wrote the code. Anything the author's session orchestrates is the author's
self-check — worth running before handing the branch over, never a substitute.
The operator starts the reviewing session.

## Alternatives

- **Make integration an implicit `[gate]`.** Reuses machinery the plan already
  has, but a gate is a step-level marker and this is a boundary on the agent's
  authority as a whole; expressing it per-plan means every plan can omit it.
- **Leave the prose and rely on permission rules only.** Settings cannot be
  assumed present in an adopting repo, and a rule the text does not state is one
  the agent will argue around when the tool prompt is absent.
- **Define independence as "a session the author did not spawn".** Blocks the
  fork and still admits a prompt the author framed; naming the input closes both.
- **Drop the author-side review.** It found real defects on the branch that
  triggered this. Keeping it as a pre-handoff pass costs nothing once it is
  named as one.

## Consequences

Execution now ends one step earlier than agents are used to, and the shipped
text says so in four places: the integration and review paragraphs in the rules
section, the plan template's authorization note, `/sdd:tasks` on Moving to Done,
and `/sdd:design` on what the plan's last step leaves behind. The Done commit
now records a decision that has already been made rather than one about to be.

Prose competes with an agent's general disposition toward autonomy and thins out
over a long context — this case is the evidence. The durable layer is
permissions: `ask` rules on `git merge*`, `git push*` and `gh pr merge*` in the
project's settings make the boundary a dialog the agent cannot reason past.
Offering that at adoption is filed as a ticket, not shipped here.
