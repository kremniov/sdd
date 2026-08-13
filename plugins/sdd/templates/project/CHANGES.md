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
