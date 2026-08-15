<!-- sdd:method-section v0.5.1 -->
## Development method

This project runs spec-driven development sized to the task. The paths below are
recorded in `.sdd.yml`; the skills read them from there.

| What | Where |
|---|---|
| Architecture canon (always current) | `{{canon}}` |
| Task queue | `{{tasks}}` |
| Roadmap (direction, not dates) | `{{roadmap}}` |
| Per-feature design + plan | `{{features}}` |
| Decision records | `{{adr}}` |
| Verification command | `{{verify}}` |

### Sizing the work

Size the process to the task. This table takes precedence over any skill's own
"applies to every project" gate.

| Tier | Scope | Process |
|---|---|---|
| **0** | Nothing left to decide — what to change is already settled, no new seam, no new dependency | No design cycle, no plan. Code + tests + commit, then close the ticket. |
| **1** | One decision to settle — where a new module sits, which dependency to take, which of two shapes to use — no invariant touched | A design paragraph in the conversation — no `design.md`, no `plan.md`; track steps with the task tool. |
| **2** | New seam, an invariant changes, or several decisions have to be agreed together | Full cycle: `/sdd:design` → `design.md` → `plan.md` → execution. |

**The tier follows the decisions, not the diff.** One call threaded down through
the layers it has to cross — interface, handler, domain, storage, fake,
service — is a single decision touching many packages, and stays tier 0 or 1
however wide the diff reads. What raises the tier is a question left open by
whatever set the work going — a ticket, a bug report, the operator's word: a
boundary that did not exist, a rule that stops holding, or two choices that have
to come out consistent in more than one place. A file count is not one of the
signals. Whoever disputes a tier — a reviewer included — names the seam or the
decision that was missed, and the burden of the design cycle falls on whoever
claims the higher tier.

### Design and plan

Artifacts live one directory per feature: `{{features}}<feature-name>/`, holding
`design.md` and `plan.md`, each naming its ticket in a `**Ticket:** <ID>` line
under the H1. These artifacts are committed and kept, frozen at merge; later
tickets cite them. What is true *now* lives in `{{canon}}`: read the canon for
the current shape, a `design.md` to recover why it took that shape.

**A plan sequences the work; it does not contain the work.** A step carries a
goal, the constraints it must hold, what it touches, and the command that proves
it — not the function bodies. Exported signatures, schema, an API fragment or an
event payload may appear, because those are seam decisions.

**An approved plan authorizes every step in it, up to a merge-ready branch.**
Execution runs to the last step and stops only on a red DoD, on a decision the
design does not cover, or at a step whose heading carries `[gate]` — a check the
operator runs by hand. A commit boundary between steps is not a checkpoint, and
finishing one is not a reason to ask whether to start the next. Integration is
never one of the authorized steps; see the handing-over rules below. Mirror the
steps into the task tool as execution starts — one task per step, in order.

### Execution

`/sdd:debug` applies at every tier, including 0, for any bug — its
"3 failed fixes → question the architecture" rule especially.

**A test is only known to test something once it has failed.** Run it and watch
it go red — for the reason you intend — before writing the code that makes it
pass. What is fixed here is the order, not a cadence: one red run before
implementing a whole module is fine, and batching is preferred to a cycle per
assertion.

**Evidence before any completion claim.** Run the verification — `{{verify}}`,
unless the change is narrower and a subset proves it — read its output, and only
then say a thing is done, fixed or passing. Name what you ran. A test
suite you did not watch finish, a build you assume still compiles, a behaviour
you reasoned about but never triggered — none of these support the claim. When
something fails or was skipped, say so with the output rather than softening it.

Subagents are not the default — dispatch them only when tasks are genuinely
parallel and the interfaces between them are settled.

Invoke a skill when the task is plainly the one it covers, not as a per-turn
check of every available skill against questions like "what does this file do".

### Handing over

**Integrating a branch is the operator's decision, never the agent's.** The
agent brings the branch to merge-ready — green, docs discipline satisfied,
independently reviewed — and stops there, reporting that state together with the
review's findings. That list is what the agent owes before handing over, not a
verdict anyone computes afterwards: short of it, finish the work; where that is
no longer possible — an artifact that would now be written after the fact, a tier
under dispute — report the gap and hand the branch over anyway.

`git merge`, `gh pr merge` and a push to the integration branch run only after
the operator approves *this* branch, in words, with the review results already in
front of them. An approved plan, and a "go" at the start of execution, are not
that approval. Moving the ticket to Done with a `[PR #N]` ref — collapsed as
`/sdd:tasks` describes — records that decision, so it is made after the
operator's word and never before it, and is therefore the **last commit on the
branch**. Merge preserving history; squash only for a named reason. Never merge
on red or pending checks.

**A merge candidate gets an independent review — at every tier, no exceptions.**
Independent is a property of the reviewer's input: the committed artifacts and
nothing else — the branch diff, the design, the canon. A prompt, briefing or
summary from the session that wrote the code disqualifies it, the author's
conversation is not input, and a review orchestrated from the author's session is
that session's self-check whatever it spawns. The operator starts the one that
counts; run your own before handing the branch over, which does not replace it.

**A review reports on two scales.** A defect — wrong now, or wrong under an input
the code will see — carries the severity, and the highest is the review's
headline. A deviation from this method — a missing `design.md`, a tier the
reviewer would have judged higher, a canon file not updated — is a *process*
finding: no severity, addressed to the operator, never a merge verdict. Name what
is missing and what it would have caught, and leave the call.

### Architectural invariants

See `{{canon}}invariants.md` — the canonical list. These rules apply to all
work; other documents link there rather than restating them. Each entry carries
how a violation is detected and what happens when one is found.

The list grows one line at a time, on the branch that earned the line. Before
integrating, ask the four questions in `/sdd:canon` against the
finished diff: did a listed rule stop being true, did this branch establish one,
did a checker change, did an exception move? Answering no to all four is the
expected result, not a failure to look. A rule that moves or retires needs an
ADR; a rule merely being written down for the first time does not.

### Significant decisions

`{{adr}}` holds one decision per file (why we chose X). Read the relevant one
before reworking a seam it governs.

An ADR is written in the PR that merges the work, alongside the canon update
below — the architecture doc records what is now true, the ADR why it was
chosen. Not at design time. Write one when the decision outlives the feature —
an invariant moves, a non-obvious trade-off is taken, or the resulting shape
will invite someone to "fix" it back. The trigger is tier-independent.

The skeleton ships with the `sdd` plugin; `/sdd:design` names its path.
Follow an existing file in `{{adr}}` when one is there.

### Docs discipline

Before finishing a development branch, if the work changed a seam documented in
`{{canon}}`, update that file in the same PR — `/sdd:subsystem`
carries the procedure. When a branch changed a seam that no document
covers, that is the trigger to write one, not a reason to skip the step.

Check all three requirements — the canon update, the ADR trigger, and the
invariant questions above — against the finished diff, before the branch is
integrated. None of them follows from how the work was planned.

### Comments

A comment carries the constraint that gives the code its current shape — why a
value is persisted only after the operation is confirmed, why two calls sit in
one transaction, why a step runs outside the loop around it. Nothing else.

**Say what the code cannot.** A comment that restates the signature, the
identifier, or a rule already written in the canon is deletion-safe by
construction: "resolves a skill by name" above `resolve_skill_by_name`, or
"keeping this narrow — see invariant 12" above the thing invariant 12 already
governs. Never name the caller.

**Volume is the symptom.** A block longer than the code under it, or one line
above every member of a type. A doc line on a public identifier that a reader
outside the module genuinely needs is not in that count.

**No history.** No "used to", "instead of", "we removed X" — that belongs to the
commit, the PR and the ADR.

**The default for any edit, review fix included, is no new comment.** A fix does
not entitle its line to one. Add one only where the corrected shape invites
re-breaking, and one line naming the constraint is the budget.

Test before saving: cover the comment and reread the code. If a competent reader
does not stumble, delete it.

<!-- /sdd:method-section -->
