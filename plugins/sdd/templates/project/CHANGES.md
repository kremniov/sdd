# Scaffold changes

`/sdd:setup` reads this file when updating managed sections. Keep it in the plugin.

Compare the project section's version with the template's. If the project is
behind, apply the intervening entries by meaning. Preserve project wording,
additions, ticket IDs and references. Different wording alone requires no update.

Each entry states the new requirement and what it replaces. Write instructions
that apply to differently worded project text. Omit diffs and quoted template
lines.

When a managed template region changes, update its version stamp and add an entry
under that version in the same commit. Omit versions with no scaffold changes.

## 1.1.3

### tasks.md

Keep Done in the final integration-preparation commit. If a later merge failure
requires repairs, allow verified repair commits after Done and preserve
published history. Use work for recovery and scoped permission. Preserve
existing queue entries and project additions.

## 1.1.1

### CLAUDE.section.md

Check the branch before editing files intended for Git. Create a working branch
when on main, master or another integration branch. Commit and push only to
working branches; integrate through a PR merge after explicit user permission.
Apply the same branch and handover rules to standalone documents, queue edits
and setup. Operations within approved work share its step and PR; ignored notes
need neither. Preserve project branch conventions and other requirements.

## 1.1.0

### CLAUDE.section.md

Route implementation, resume and integration to work; route specialized requests
to their skill. Replace the user-only merge execution wording with explicit
permission followed by agent execution. Keep implementation approval separate
from integration approval. Use evidence scoped to completed checks. Replace
mandatory test-first for every edit with the work skill's behavior-specific
verification rule. Use direct writing and useful comments without rhetorical
explanations. Preserve project-specific requirements.

### tasks.md

Use the queue skill for context, IDs and status. Done records explicit
integration permission in the final branch commit and reaches the main branch
with the work. Existing tickets and completed entries remain unchanged.

### roadmap.md

Keep objectives and ordering in the roadmap and actionable status in the queue.
Link detailed product constraints that a phase summary cannot supply. Preserve
the project's objectives and references.

### invariants.md

Require evidence and accepted obligations, concrete detection and explicit manual
detector labels. A violation does not authorize retirement. Keep stable numbers,
agreed changes and ADR references. Remove speculative starter entries while
preserving the project's actual rules and responsibility tables.

### lessons.md

Record verified observations with dates and evidence where available. Avoid
copying general advice or existing rules; link an invariant when a lesson becomes
one. Preserve existing project observations.

### docs-README.md

Describe current canon, historical designs and plans, and ignored working status.
Read requirements alongside the request; use code to investigate discrepancies.
Route process selection through work and permit direct requests without tickets.
Keep existing project paths and relevant document categories.

## 1.0.0

### lessons.md

**New file.** The canon gains a third file beside `invariants.md` and
`layout.md`. It carries what the work taught and a rule would have missed: a
runtime constraint of the stack, the real shape a dependency returns, a command
that behaves unlike its documentation. One dated line each, written on the branch
that learned it. It is the one canon file that carries dates. A project that
already keeps such notes points this file at them instead.

### invariants.md

**The guidance says the same rules in a plainer register.** Nothing about the
entry format, the stability of numbers or the detection note changed. A project
that reworded this header keeps its wording.

### roadmap.md

**The roadmap is named as an input to a design.** It carries the product logic
that a ticket's acceptance criteria only check, so the design of a feature reads
it alongside the ticket and the canon. A project whose roadmap header says this
already needs no edit.

### docs-README.md

**The guide points at `/sdd:work` for the tier table**, which left the project's
rules file at v1.0.0. It gains a row for the working-notes directory that
`.sdd.yml` now records as `notes:`, and the start-of-work reading order gains
`lessons.md`. A project that keeps its own reading order adds the lessons file
to it.

### CLAUDE.section.md

**The section keeps only the rules that hold with no skill loaded, and the rest
move to `/sdd:work`.** What stays is five things: the user integrates the branch
and the agent stops at the pull request; evidence is shown and named before any
completion claim; a test is watched failing before the code that passes it; the
writing register; the comments rules; and a line telling the agent to invoke the
skill. What leaves is
the tier table, the paths table, the artifact locations, the plan rules, the two
review scales, and the invariant, decision-record and docs triggers — all of it
now in `/sdd:work`, which is invoked when a task starts. A project that reworded
these rules keeps its own wording for the six that stay and deletes the rest,
leaving a pointer to the skill.

**The fence is named `sdd:rules`.** The old `sdd:method-section` marker names a
region that no longer describes what the plugin ships, so `/sdd:setup` offers to
retire it and writes the new fence only once that is settled. A project that
declines keeps the v0.x rules, and no second method section is ever written.

**Three rules are new.** The handing-over rule now names the pull request: the
branch is pushed and the pull request opened before the agent stops, so the user
has something to review. The sizing call is surfaced at every tier, so a task
with nothing left to decide still gets the user's word before the code. And the
register of every document the session writes is named: ASD-STE100, simplified
technical English, one fact or one rule per sentence. A project that already
states a house style for its documents keeps it.

## 0.5.1

### CLAUDE.section.md

**Closing a ticket names the skill that defines the format.** Handing over stated
when the Done move happens and what ref it carries, but not where its shape is
written, so an agent reaching that step reconstructed the format by reading the
queue's existing Done entries. The rule now points at `/sdd:tasks`, as the
neighbouring sections already point at `/sdd:canon`, `/sdd:subsystem` and
`/sdd:design` for the artifacts they govern. A project that renamed the skill or
keeps the collapse format elsewhere carries the pointer to wherever that is.

## 0.5.0

### CLAUDE.section.md

**The section is partitioned by phase of work.** `### Process tiers` had become
where a rule landed when no heading claimed it — tiers, artifact locations, plan
rules, the test-first rule, evidence, integration, review, subagents and skill
invocation all sat under it, 64% of the section. It is replaced by four
headings — sizing the work, design and plan, execution, handing over — and every
rule moves under the phase in which it applies. A project that has reordered or
renamed these rules keeps its own arrangement; what to carry is the principle
that a rule's home is the phase it governs, so that the next rule added has an
obvious place and no heading becomes the default sink.

**A rule ships without its justification.** Prose explaining why a rule exists no
longer travels with it: the cost-versus-ambiguity argument for sizing, the
account of why an implementation written early reads as a commitment, the list of
ways a green test can be empty, the mechanism by which a forked review inherits
its author's context, the reason a process finding ranked as a defect inverts a
report. What stays — stated as a rule, not as an account of the incident that
produced it — is every clause naming what does *not* satisfy a rule: a commit
boundary is not a checkpoint, an approved plan and a "go" are not the user's
approval, the author's conversation is not input, a suite you did not watch
finish is not evidence. The test for a sentence is whether removing it changes
what someone may do. It was applied to the whole section, the standing
subsections on invariants, decisions, docs discipline and comments included, so
that no part of the shipped text is exempt from the rule it states.

**A rule that gets disobeyed is reworded, not annotated.** When a rule fails to
hold, sharpen its wording until the wrong reading is unavailable; do not add
prose arguing for it. The three paragraphs on integration, review and finding
severity had accumulated 517 words stating one principle from three sides, each
addition made after an incident, and in each case what actually closed the hole
was the rewording rather than the argument beside it. They are now one account of
who decides what, in 345 words, with every rule kept.

## 0.4.0

### CLAUDE.section.md

**The tier's third signal stopped naming modules.** It read "several modules
move together", and of the three signals it was the only one a reader could
settle from `git diff` alone — so it won over the two that need judgement, and
any change threaded down through a layered architecture counted as tier 2. It
now names several decisions that have to be agreed together. A paragraph under
the table says the tier follows the decisions rather than the diff: one call
crossing interface, handler, domain, storage, fake and service is one decision
touching many packages; what raises the tier is a question the ticket does not
answer — a boundary that did not exist, a rule that stops holding, two choices
that must come out consistent in more than one place. A file count is named as
not being a signal, and a tier dispute has to name the seam or the decision that
was missed, with the burden on whoever claims the higher tier.

**All three rows now read in the same terms, not just the third.** Tiers 0 and 1
were scoped by file shape — "one file" and "a new file or module" — so a change
that edits several existing files without adding a module or a seam matched no
row at all, and the paragraph above could not place it. Tier 0 is now nothing
left to decide — what to change already settled, by whatever set the work going,
since the method does not require a ticket for every change; tier 1 is one
decision to settle, with a new module, a new dependency or a choice between two
shapes as examples of such a decision rather than as the criterion.

**A review now has two scales, and process findings sit on the second.** The
guidance told a reviewer that a merge candidate has docs discipline satisfied
and said nothing about reporting a shortfall, so a missing `design.md` arrived
carrying a defect's severity and a "not merge-ready" verdict — ranked above the
bugs found in the same pass. Defects keep the severity scale. A deviation from
the method — a missing artifact, a tier the reviewer would have judged higher, a
canon file not updated — is a process finding with no severity level, addressed
to the user, and never a merge verdict, on the same ground the integration
rule already stands on: the reviewer does not hold that decision either.

**Merge-ready is a list the agent owes, not one a reader scores.** With the two
scales in place the old wording still contradicted them: merge-ready was defined
as green, docs discipline satisfied and independently reviewed, so anyone holding
that list could compute "not merge-ready" from a methodology gap — the verdict
the new rule forbids. The list is now named as what the agent owes before handing
over. Falling short of it means finishing the work; where that is no longer
possible — an artifact that would be written after the fact, a tier under
dispute — the agent reports the gap and hands the branch over regardless, since
holding it back takes the user's call away from them.

## 0.3.0

### CLAUDE.section.md

**Integration became the user's decision, explicitly.** The rule previously
said "integrating a branch is a decision, not a step" and listed the criteria —
green, reviewed, docs discipline satisfied — without naming who decides. An
agent holding all the criteria read that as a procedure to execute, and merged.
The guidance now has to say: the agent's authority ends at a merge-ready branch,
which it reports together with the review's findings; `git merge`, `gh pr merge`
and a push to the integration branch wait for the user's word on that
specific branch, given after the review results exist. Approving a plan and
saying "go" at the start of execution are named as *not* carrying that
authority, because both come before the review.

**Plan authorization is bounded at the same place.** "An approved plan authorizes
every step in it" now ends "up to a merge-ready branch", and says integration is
never one of the authorized steps. Without the bound, an authorized last step
that closes the ticket carries the merge along with it.

**The Done commit records a decision instead of anticipating one.** It is still
the last commit on the branch; what changed is that it comes after the user
approves, not after the review.

**Independence is now a property of the reviewer's input.** "A fresh session on
the finished branch" was satisfiable from inside the author's own session — a
forked review continues the author's context outright, and even a subagent that
starts clean reads a prompt the author framed. The requirement is that the
reviewer's input is the committed artifacts and nothing else — no prompt,
briefing or summary from the session that wrote the code, whose conversation is
not input — and that the user starts that session. An author-side review is
still worth running before handing the branch over; it does not replace this
one.
