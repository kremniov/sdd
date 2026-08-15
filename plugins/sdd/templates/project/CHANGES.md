# Scaffold changes

What changed inside the plugin's half of each scaffold file, one section per
version. This file is never written into a project; `/sdd:setup` reads it.

A re-run compares the version stamped on a project's fence with the one stamped
on the template's, and where the project is behind, it carries the entries in
between. It carries what they *describe*, into the project's own wording — a
project that phrased the same guidance in its own terms, with its own ticket ids
and cross-references, is not stale, and the template's current text is not the
answer for it.

So an entry states what the guidance now requires and what it replaced, in prose
that can be applied to text worded differently. No diffs and no quoted template
lines: both are instructions to overwrite, which is the failure this file
exists to end.

A version whose release changed no scaffold file gets no section. A file whose
region changes gets its stamp moved to that version and an entry here, in the
same commit — the gate fails otherwise.

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
boundary is not a checkpoint, an approved plan and a "go" are not the operator's
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
to the operator, and never a merge verdict, on the same ground the integration
rule already stands on: the reviewer does not hold that decision either.

**Merge-ready is a list the agent owes, not one a reader scores.** With the two
scales in place the old wording still contradicted them: merge-ready was defined
as green, docs discipline satisfied and independently reviewed, so anyone holding
that list could compute "not merge-ready" from a methodology gap — the verdict
the new rule forbids. The list is now named as what the agent owes before handing
over. Falling short of it means finishing the work; where that is no longer
possible — an artifact that would be written after the fact, a tier under
dispute — the agent reports the gap and hands the branch over regardless, since
holding it back takes the operator's call away from them.

## 0.3.0

### CLAUDE.section.md

**Integration became the operator's decision, explicitly.** The rule previously
said "integrating a branch is a decision, not a step" and listed the criteria —
green, reviewed, docs discipline satisfied — without naming who decides. An
agent holding all the criteria read that as a procedure to execute, and merged.
The guidance now has to say: the agent's authority ends at a merge-ready branch,
which it reports together with the review's findings; `git merge`, `gh pr merge`
and a push to the integration branch wait for the operator's word on that
specific branch, given after the review results exist. Approving a plan and
saying "go" at the start of execution are named as *not* carrying that
authority, because both come before the review.

**Plan authorization is bounded at the same place.** "An approved plan authorizes
every step in it" now ends "up to a merge-ready branch", and says integration is
never one of the authorized steps. Without the bound, an authorized last step
that closes the ticket carries the merge along with it.

**The Done commit records a decision instead of anticipating one.** It is still
the last commit on the branch; what changed is that it comes after the operator
approves, not after the review.

**Independence is now a property of the reviewer's input.** "A fresh session on
the finished branch" was satisfiable from inside the author's own session — a
forked review continues the author's context outright, and even a subagent that
starts clean reads a prompt the author framed. The requirement is that the
reviewer's input is the committed artifacts and nothing else — no prompt,
briefing or summary from the session that wrote the code, whose conversation is
not input — and that the operator starts that session. An author-side review is
still worth running before handing the branch over; it does not replace this
one.
