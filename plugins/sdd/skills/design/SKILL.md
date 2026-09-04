---
name: design
description: Use on a tier-2 task, after gate G1, to turn the agreed decisions into design.md — the problem, the locked choices, the seams touched, the failure modes and what proves the work. Ends at gate G2, where the user reads it.
---

# The design

`design.md` states what gets built and why it takes that shape. `/sdd:work`
carries the gates, the tiers and the blockers. This skill writes one artifact.

Tier 2 writes this file. Tier 1 states a design paragraph in the conversation.
Tier 0 writes neither.

Paths come from `.sdd.yml`: `features:`, `canon:`, `adr:`, `roadmap:`, `tasks:`.
One `key: value` per line; everything from the first `#` is a comment; values are
used verbatim. If the file is absent, say so and stop — the project has not
adopted this method (`/sdd:setup`). If a key this skill needs is absent or empty,
name the key and ask.

## Inputs

Read all five before the first sentence.

| Input | What it settles |
|---|---|
| The ticket in `tasks:` | The outcome, and how it gets checked |
| The roadmap | The product logic, and the phase this work belongs to |
| `invariants.md` and the subsystem document for the area | The rules the work must hold |
| The decision records that govern the seam | Why the current shape is what it is |
| The recent commits in the modules involved | What the code does today |

Acceptance criteria are a check, not a specification. The product logic lives in
the roadmap and the architectural logic lives in the canon. Where either
disagrees with the acceptance criteria, name the disagreement and ask.

## Writing it

1. Propose two or three approaches. Lead with your recommendation. Give each one
   line of cost. Strip from every approach what the ticket leaves out, and name
   anything else worth doing as a separate ticket.
2. Present the design one section at a time, each scaled to what is open. Check
   after each section that it still looks right.
3. Write `<features>/<feature-name>/design.md` from
   `${CLAUDE_PLUGIN_ROOT}/templates/_DESIGN.md`. Read the skeleton in place.
4. Mark a decision `→ ADR` where it outlives the feature. `/sdd:work` writes
   those records at handing over.
5. Read the written design once and fix inline: placeholders, sections that
   contradict each other, a requirement that reads two ways, and scope past one
   plan.
6. Ask the user to read it. This is G2, and changes come back here.

## In an existing codebase

Follow the patterns the code already holds. Link the canon: a rule stated in two
files becomes two rules that drift.

Give each unit one purpose, one interface and its own tests. A consumer that has
to read the internals has met a boundary in the wrong place.

Where code in the path of the work has a real problem — a file past its purpose,
a tangled responsibility — put the targeted fix in the design. Unrelated
refactoring is a separate ticket.

Name the invariants the work touches and the canon documents that update in the
same pull request. A branch that changes a seam no document covers writes one
(`/sdd:subsystem`).

## Budgets

| Measure | Budget |
|---|---|
| Words | 1300, hard stop 2000 |
| Headings | 12 |
| Rationale | one sentence per decision |

Scale each section to what the ticket leaves open: two sentences where the answer
is plain, a real argument where it is not. The cost of the cycle falls on the
user's attention, so spend it on the open questions and leave the settled
headers short.
