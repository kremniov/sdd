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
