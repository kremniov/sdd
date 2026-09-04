---
name: work
description: Use at the start of any development task — a ticket, a bug report, a chore, a rewrite — to size it, run its gates, and take it to a pull request. Carries the gate table, the tier table, the closed list of blockers, the review rules and the handing-over rules. Invoke it before the first edit.
---

# Working a task

This skill runs a task from pickup to a pull request. Invoke it first. The other
skills write the artifacts it calls for.

Paths come from `.sdd.yml`: `tasks:`, `roadmap:`, `canon:`, `features:`, `adr:`,
`notes:`, `verify:`, `ticket:`. One `key: value` per line; everything from the
first `#` is a comment; values are used verbatim. If the file is absent, say so
and stop — the project has not adopted this method (`/sdd:setup`). If a key this
skill needs is absent or empty, name the key and ask.

## Gates

A gate is a point where the user reads, decides and approves. Pass a gate on the
user's word, never on your own.

| Gate | What the user approves | What you do next |
|---|---|---|
| G1 | The tier, and the decisions of the brainstorm | Write the design, state the design paragraph, or start the code |
| G2 | The design | Commit the design, write the plan |
| G3 | The plan | Commit the plan, run every step in order |
| G4 | The pull request | The user merges |

## Sizing

| Tier | Scope | Gates | Artifacts |
|---|---|---|---|
| 0 | Nothing left to decide | G1, G4 | none |
| 1 | One decision to settle | G1, G2, G4 | a design paragraph in the conversation |
| 2 | A new seam, an invariant that moves, or several decisions that must agree together | G1, G2, G3, G4 | a design and a plan under `features:` |

The tier follows the decisions, not the diff. One call threaded through six
layers is one decision that touches many packages. A file count is not a signal.
Whoever claims the higher tier names the seam or the decision that was missed.

Say the tier and wait for the user's word. This is G1, and it runs at every tier.

## Phases

### Brainstorm

Read four things first: the ticket in the queue, the roadmap, the canon, and the
decision records that govern the seam. Read the recent commits in the modules
involved. Arrive at the first question knowing what the repository does today.

The ticket's acceptance criteria are a check, not a specification. The product
logic is in the roadmap and the architectural logic is in the canon. Where they
and the acceptance criteria disagree, name the disagreement and ask.

Collect the open questions. Group them. Ask them in rounds, and one round is one
message. After each round, write the decisions to
`<notes>/<feature>-decisions.md`, one line each with its date. That directory is
outside git. Stop when no open question is left. This is G1.

### Design and plan

Tier 2 runs `/sdd:design`, then writes the plan. Tier 1 states a design
paragraph in the conversation. Tier 0 writes neither.

### Execution

Take the steps in order and finish one before the next.

Run the test and watch it fail, for the reason you intend, before you write the
code that makes it pass.

Run `verify:` before each commit and read its output. One step is one commit:
Conventional Commits, English, an imperative subject, and a body that says why.

An approved plan authorizes every step in it, up to a merge-ready branch. A
commit boundary is a commit boundary and nothing else. Stop at a blocker, or at
a step whose heading carries `[gate]`.

`/sdd:debug` applies to any bug, at every tier.

### Handing over

Do these six in order before the branch leaves your hands:

1. Run `verify:` and read the output.
2. Ask the four canon questions against the finished diff (`/sdd:canon`).
3. Write an ADR for each decision marked `→ ADR`, from
   `${CLAUDE_PLUGIN_ROOT}/templates/_ADR.md` into `adr:`.
4. Update the canon document for each seam the branch changed
   (`/sdd:subsystem`). A changed seam that no document covers earns a new one.
5. Review the branch yourself against the committed artifacts.
6. Push the branch, open the pull request, and stop.

Then report the state of the branch and the findings of your own review.

The user runs the independent review against the pull request and merges.
`git merge`, `gh pr merge` and a push to the integration branch belong to the
user, at every tier and on every branch. An approved plan is a different thing
from an approved merge.

Move the ticket to Done once the user approves the merge (`/sdd:tasks`). That
commit is the last one on the branch, and it fills any ADR `PR:` field still
holding a dash.

## Blockers

Stop and ask when one of these is true:

1. Two readings of the request lead to materially different work.
2. The code or a dependency contradicts the design.
3. The change needs a contract that a party outside this repository must agree.
4. A step touches a system in a way that is irreversible.
5. A credential or an access right is missing.

Carry on through: naming, file layout, test structure, library choice inside the
agreed stack, formatting, and the end of a commit.

## Review

A merge candidate gets an independent review at every tier.

Independent is a property of the reviewer's input: the committed artifacts, the
branch diff, the design and the canon. A briefing, prompt or summary from the
session that wrote the code disqualifies the review, and a review started from
that session is that session's self-check.

A review reports on two scales. A defect — wrong now, or wrong under an input the
code will see — carries a severity, and the highest severity is the headline. A
deviation from this method carries none. Name what is missing and what it would
have caught, address it to the user, and leave the call there.

## Status

Keep one record in memory for this branch: the ticket, the tier, the branch
name, the gate that is passed, the current step, and the last decision with its
date. Update it at each gate and at each step. After a context compaction, read
it and invoke this skill again.
