---
name: brainstorming
description: Use when a tier-2 task is picked up — a new seam, an invariant that moves, or several modules moving together — to turn the ticket into an agreed design before any code. Produces the feature's design.md.
---

# Brainstorming

Turn a ticket into a design through dialogue, then write it down.

**Which tasks:** tier 2 in the `CLAUDE.md` table. Tier 1 gets a design paragraph
in the conversation; tier 0 gets none. Sizing the process to the task is the
operator's call — if the tier is unclear, ask before starting, not after.

Paths come from `.sdd.yml`: `canon:`, `tasks:`, `features:`, `adr:`. Read it
first. Without it, the project has not adopted this method — run
`/sdd:adopting-sdd`.

## Process

**1. Read the context first.** The ticket in the queue, then the canon —
`invariants.md`, `layout.md`, and the subsystem doc the work touches. Existing
decisions in the ADR directory that govern the seam. Recent commits in the
modules involved. Come to the first question already knowing what the repo does
today.

**2. Ask one question per message.** Purpose, constraints, success criteria —
what the ticket leaves open. Prefer a small set of concrete options over an open
prompt; lead with your recommendation and say why. A question whose answer you
could have found in the repo is a question you should not ask.

**3. Propose 2–3 approaches** with trade-offs, recommendation first. YAGNI
ruthlessly: strip from every approach what the ticket does not ask for. If
something outside the ticket is worth doing, name it as a separate ticket rather
than folding it in.

**4. Present the design in sections**, each scaled to its complexity — a couple
of sentences when it is straightforward. Cover the seams touched, the data model
and flow, error handling, and what proves it works. Check after each section
that it still looks right.

**5. Write the design** to `<features>/<feature-name>/design.md`, following the
skeleton at `${CLAUDE_PLUGIN_ROOT}/templates/_DESIGN.md`. Read the skeleton
rather than reproducing it from memory — the copy is what keeps the corpus
greppable. Mark decisions `→ ADR` where they outlive the feature; the merging PR
promotes them.

**6. Self-review the written design**, once, and fix inline: placeholders and
TBDs; sections that contradict each other; a requirement that reads two ways —
pick one and say it; scope that no longer fits a single plan.

**7. Ask the operator to read it** before moving to the plan. Changes come back
here; the design is what the plan executes, so it settles first.

## Designing for an existing codebase

- Explore the current structure before proposing changes, and follow the
  patterns already there. The canon is authoritative — link it rather than
  restating it in the design.
- Each unit gets one purpose, a defined interface, and independent tests. For
  each: what does it do, how is it used, what does it depend on. If a consumer
  has to read the internals, the boundary is wrong.
- Where existing code in the path of the work has a real problem — a file that
  outgrew its purpose, a tangled responsibility — include the targeted fix in the
  design, the way a careful developer improves code they are working in.
  Unrelated refactoring stays out.
- Name which invariants the work touches and which canon documents update in the
  same PR. A design that moves an invariant without saying so is not finished.

## After the design: the plan

Tier 2 continues into `<features>/<feature-name>/plan.md`, following
`${CLAUDE_PLUGIN_ROOT}/templates/_PLAN.md`. The plan sequences the work; it does
not contain it. Steps carry a goal, constraints, what they touch, and a runnable
DoD — not function bodies.

## What this is not

Not a template to fill in. If the ticket is unambiguous and the seam already
exists, say so and go straight to the work — the cost of the cycle is real and
falls on the operator's attention. The dialogue earns its place when the ticket
is genuinely open, which is the case tier 2 describes.
