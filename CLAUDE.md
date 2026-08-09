# SDD plugin

This repository ships the method it uses. Changes here are dogfooded before
they are published.

<!-- sdd:method-section -->
## Development method

This project runs spec-driven development sized to the task. The paths below are
recorded in `.sdd.yml`; the skills read them from there.

| What | Where |
|---|---|
| Architecture canon (always current) | `docs/architecture/` |
| Task queue | `docs/tasks.md` |
| Roadmap (direction, not dates) | `docs/roadmap.md` |
| Per-feature design + plan | `docs/features/` |
| Decision records | `docs/adr/` |
| Verification command | `./scripts/check.sh` |

### Process tiers

The design cycle costs roughly the same regardless of task size, while its
payoff scales with how ambiguous the task is. Size the process to the task —
this table takes precedence over any skill's own "applies to every project" gate.

| Tier | Scope | Process |
|---|---|---|
| **0** | One file, no new seam, no new dependency | No brainstorming, no plan. Code + tests + commit, then close the ticket. |
| **1** | New file or module, no invariant touched | A design paragraph in the conversation — no `design.md`, no `plan.md`; track steps with the task tool. |
| **2** | New seam, an invariant changes, or several modules move together | Full cycle: `brainstorming` → `design.md` → `plan.md` → execution. |

Artifacts live one directory per feature: `docs/features/<feature-name>/`, holding
`design.md` and `plan.md`. Both name their ticket in a `**Ticket:** <ID>` line
under the H1 — the directory is named after the feature, so that line is the
only thing making the artifact resolvable back to the queue. These artifacts are
committed and kept, frozen at merge; later tickets cite them. What is true *now*
lives in `docs/architecture/`: read the canon for the current shape, a `design.md` to
recover why it took that shape.

**A plan sequences the work; it does not contain the work.** A step carries a
goal, the constraints it must hold, what it touches, and the command that proves
it — not the function bodies. Exported signatures, schema, an API fragment or an
event payload may appear, because those are seam decisions; an implementation
written out ahead of time is a draft made when least is known, and it reaches
execution looking like an agreed commitment rather than a guess.

**An approved plan authorizes every step in it.** Execution runs to the last
step and stops only on a red DoD, on a decision the design does not cover, or at
a step whose heading carries `[gate]` — a check the operator runs by hand. A
commit boundary between steps is not a checkpoint, and finishing one is not a
reason to ask whether to start the next. Mirror the steps into the task tool as
execution starts — one task per step, in order — so progress is readable without
reading the diff.

`systematic-debugging` applies at every tier, including 0, for any bug — its
"3 failed fixes → question the architecture" rule especially.

**A test is only known to test something once it has failed.** Run it and watch
it go red — for the reason you intend — before writing the code that makes it
pass. Green looks the same whether the code is right or the assertion never ran:
a mock swallowed the call, the field checked is not the field written, the case
table is empty. What is fixed here is the order, not a cadence: one red run
before implementing a whole module is fine, and batching is preferred to a cycle
per assertion.

**Evidence before any completion claim.** Run the verification — `./scripts/check.sh`,
unless the change is narrower and a subset proves it — read its output, and only
then say a thing is done, fixed or passing. Name what you ran. A test
suite you did not watch finish, a build you assume still compiles, a behaviour
you reasoned about but never triggered — none of these support the claim. When
something fails or was skipped, say so with the output rather than softening it.

**Integrating a branch is a decision, not a step.** Before merging: the branch
is green, the independent review below has passed, and the docs discipline below
is satisfied. Moving the ticket to Done with a `[PR #N]` ref is then the **last
commit on the branch** — it records that the work shipped, so it cannot precede
the review that decides whether it does. Merge preserving history; squash only
for a named reason. Never merge on red or pending checks.

**A merge candidate gets an independent review — at every tier, no exceptions.**
A fresh session on the finished branch, not the one that wrote it: an author's
self-check is a different procedure and its quality tracks how worn the session
is. This catches a class of defect no amount of up-front process does — a wrong
assumption shared by the code and the plan that produced it survives
brainstorming, design, and the author's own review, because each of them reasons
from that assumption.

Subagents are not the default — dispatch them only when tasks are genuinely
parallel and the interfaces between them are settled.

Invoke a skill when the task is plainly the one it covers. A per-turn check of
every available skill against questions like "what does this file do" is a tax
with no return.

### Architectural invariants

See `docs/architecture/invariants.md` — the canonical list. These rules apply to all
work; other documents link there rather than restating them. Each entry carries
how a violation is detected and what happens when one is found, so the list is
readable as a review procedure and not only as prose.

The list grows one line at a time, on the branch that earned the line. Before
integrating, ask the four questions in `/sdd:deriving-canon` against the
finished diff: did a listed rule stop being true, did this branch establish one,
did a checker change, did an exception move? Most branches answer no to all
four — that is the expected answer, not a failure to look. A rule that moves or
retires needs an ADR; a rule merely being written down for the first time does
not.

### Significant decisions

`docs/adr/` holds one decision per file (why we chose X). Read the relevant one
before reworking a seam it governs.

An ADR is written in the PR that merges the work, alongside the canon update
below — the architecture doc records what is now true, the ADR why it was
chosen. Not at design time: before the code exists a decision is still an
intention. Write one when the decision outlives the feature — an invariant
moves, a non-obvious trade-off is taken, or the resulting shape will invite
someone to "fix" it back. The trigger is tier-independent; a one-file Tier 0
change can earn an ADR and a Tier 2 feature can earn none.

The skeleton ships with the `sdd` plugin; `/sdd:brainstorming` names its path.
Follow an existing file in `docs/adr/` when one is there.

### Docs discipline

Before finishing a development branch, if the work changed a seam documented in
`docs/architecture/`, update that file in the same PR — `/sdd:documenting-subsystems`
carries the procedure. Keep the architecture layer current so agents read it
instead of re-reading code. When a branch changed a seam that no document
covers, that is the trigger to write one, not a reason to skip the step.

Check all three requirements — the canon update, the ADR trigger, and the
invariant questions above — against the finished diff, before the branch is
integrated. None of them follows from how the work was planned: a branch that
ran the full design cycle can still land without the ADR its own decision
earned, and a design that promised to move an invariant does not always turn out
to have moved it.

### Comments

A comment carries the constraint that gives the code its current shape — why a
value is persisted only after the operation is confirmed, why two calls sit in
one transaction, why a step runs outside the loop around it. Nothing else.

**Say what the code cannot.** A comment that restates the signature, the
identifier, or a rule already written in the canon is deletion-safe by
construction: "resolves a skill by name" above `resolve_skill_by_name`, or
"keeping this narrow — see invariant 12" above the thing invariant 12 already
governs, are both the reader looking at the same fact twice. Naming the caller
ages worst of all — the caller moves and the comment lies.

**Volume is the symptom.** A block longer than the code under it, or one line
above every member of a type, means the comment is describing what is visible
rather than what is not. A doc line on a public identifier that a reader outside
the module genuinely needs is not in that count.

**No history.** No "used to", "instead of", "we removed X" — the commit, the PR
and the ADR are dated and read in order; a comment is not, so it ages into a
state the reader has to reconstruct.

**The default for any edit, review fix included, is no new comment.** A fix does
not entitle its line to one. Add one only where the corrected shape invites
re-breaking, and one line naming the constraint is the budget.

Test before saving: cover the comment and reread the code. If a competent reader
does not stumble, delete it.

<!-- /sdd:method-section -->
