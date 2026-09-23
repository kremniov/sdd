---
name: work
description: Run an implementation task from research and approval through committed steps and a pull request. Also resume approved work or integrate a reviewed PR on explicit permission.
---
 # Work

## Inputs and route

Read the request and `.sdd.yml`. Use its `tasks`, `roadmap`, `canon`,
`features`, `adr`, `notes`, `verify` and `ticket` values when needed. If the
file or a required value is absent, offer `/sdd:setup`. A direct request can
replace a ticket. `<task>` in a notes file name is the ticket ID, or a short
slug of the request when there is no ticket.

Select the requested result before starting an implementation workflow:

| Request | Action |
|---|---|
| Implement a change | Follow the stages below |
| Diagnose a bug | Use `/sdd:debug`, then approve the proposed change |
| Review or audit | Report findings |
| Maintain the queue | Use `/sdd:tasks`; leave implementation unstarted |
| Adopt or update the method | Use `/sdd:setup` |
| Explain or investigate | Return evidence and open questions |

Review, audit or explanation does not permit editing files.
| Resume | Read Status below |
| Merge a PR | Read [integration.md](integration.md) |

## Branch and completion

Before creating or editing tracked files, identify the current and integration
branches from project conventions and Git state. On an integration branch
(`main`, `master` or the project equivalent), create a working branch first.
Commit and push only to working branches. Integrate through a PR merge after
explicit user permission. Use a worktree when isolation is needed or requested.
Preserve existing user changes.

Apply this rule to standalone document, queue and setup operations too. Verify
and commit their changes, then use Handover and review below. Within ongoing
approved work, include them in that work's step and PR instead of opening a
separate PR. Ignored working notes need no commit or PR. Creating a ticket or
design does not authorize implementing its subject.

## Research and approval

Read relevant requirements, roadmap, canon, decisions and code. Read history
when it helps explain a constraint. Resolve available facts before asking. When
acceptance conflicts with requirements or architecture, show the disagreement
and recommend a resolution. Code shows current behavior; a document can also
state an obligation that broken code fails to meet. A design linked from a
ticket is history after its merge; the canon and ADRs state current obligations.

A decision is material when it changes behavior, a contract, scope, an
architectural constraint or significant cost, and no ticket, canon entry or ADR
settles it. Group related questions and ask them one at a time. Prefer
`AskUserQuestion` when available.
Recommend a choice with material trade-offs. Date decisions in
`<notes>/<task>-decisions.md`. Reopen agreed choices on new evidence.

| Tier | Decision scope | Approval before implementation |
|---|---|---|
| 0 | No material decision remains | G1: exact change, scope, assumptions and verification |
| 1 | One material decision | G1 and G2 together in one message: recommended solution, scope, assumptions and verification. No design document |
| 2 | A new boundary, invariant change or multiple interdependent decisions | G1 decisions, G2 design, G3 plan |

Tier 2 takes precedence. Justify the tier by decisions, not file count. Wait for
approval of the concrete proposal, including at tier 0. The request alone does
not approve values you selected. For a selected value, state what your check of
it establishes.

Tier 2 runs `/sdd:design` after G1 and `/sdd:plan` after G2. Their artifacts go
to `<features>/<feature>/`, where `<feature>` is a short slug for the change,
agreed at G1. A new task gets a new directory. Approval persists within its
scope across commits, breaks and context compaction. G3 authorizes every planned
step through a reviewable PR.

## Execute

Update existing tickets through `/sdd:tasks` during implementation and when blocked.

For each step: implement, verify, commit all its changes, update Status, then
continue. Several commits per step are allowed; independent review need not
precede them. Use English Conventional Commits with a subject naming the change
and a body stating its reason.

For behavior checked by a test, observe its intended failure before the fix. For
other changes, use a structural check, build, worked example or manual check.
Check each change before committing and each step's result before finishing it.
Run `verify` after all code and document changes. Repeat checks after relevant
changes or unresolved concerns. Read completed output; report commands, outcomes
and omissions, limiting claims to evidence.

Update affected subsystem documents in the same PR (`/sdd:subsystem`). Check
invariants, detectors and exceptions with `/sdd:canon`. No invariant change is
normal. Write durable decisions in `adr` using
[_ADR.md](templates/_ADR.md): invariant changes, significant
trade-offs or choices whose reasons will be hard to recover. Update design and
remaining plan after agreed changes; routine corrections need no ADR.

## Stop conditions

Pause dependent work and ask when:

- different readings materially change the requested work;
- new evidence changes an agreed contract, decision or scope;
- an external party must decide or agree;
- a necessary action exceeds the permission given;
- necessary access or information is missing;
- a planned point of human participation is reached.

State evidence, effect and a recommended next action. Continue independent,
authorized work while awaiting the answer. Choose names, file placement, test
structure and formatting within agreed constraints. A commit boundary requires
no approval. Progress reports do not ask permission to continue.

## Handover and review

Complete code and documents, run final checks and review the branch yourself.
Verify and commit corrections. Confirm that the checked state matches the
committed state. Push, open the PR, report the result and stop before
integration. Tell the user that independent review is due, for example `/code-
review` in a new session. Describe the problem, resulting behavior, verification
and limitations in the PR.

Independent review is required at every tier, including documents. The user
starts it; its depth follows risk and the change. Inputs are the review request,
committed artifacts, diff and primary requirements. Exclude author-session
reasoning as the basis for conclusions. Author-side checks do not replace it.

Report behavioral defects with severity and concrete evidence. Report process
deviations separately, without defect severity or an integration verdict: name
what is missing and which check lacks a basis.

Verify, commit and push requested fixes on the same branch. Report resolved and
remaining findings and their verification. The user starts any repeat
independent review. Without integration permission, stop before merge.
Conditional permission such as "fix these findings and merge" authorizes
integration once its conditions are met. Return changed decisions or scope
to the user.

## Status

For multi-step work, keep `<notes>/<task>-status.md` outside Git. Save unfinished
work before a pause or handoff. Single-step work completed this session needs no status file.

Record branch, task, tier, approvals, completed and remaining steps, checks
and questions. Link decisions and artifacts; update after approvals and steps.

After a break or handoff, read status and current-stage instructions, check Git
state, and continue unfinished work. Reconcile conflicting evidence before
repeating a finished step. Do not copy method rules.
