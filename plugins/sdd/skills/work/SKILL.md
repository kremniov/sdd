---
name: work
description: Run an implementation task from research and approval through committed steps and a pull request. Also resume approved work or integrate a reviewed PR on explicit permission.
---

# Work

## Inputs and route

Read the request and `.sdd.yml`. Use its `tasks`, `roadmap`, `canon`, `features`,
`adr`, `notes`, `verify` and `ticket` values when needed. Parse one key and value
per line at the first colon; strip comments from the first `#`. If configuration
is absent, offer `/sdd:setup`. Ask for a required missing value before dependent
work. A direct request can replace a ticket.

Select the requested result before starting an implementation workflow:

| Request | Action |
|---|---|
| Implement a change | Follow the stages below |
| Diagnose a bug | Use `/sdd:debug`, then approve the proposed change |
| Review or audit | Report findings; fixes require a separate instruction |
| Maintain the queue | Use `/sdd:tasks`; leave implementation unstarted |
| Adopt or update the method | Use `/sdd:setup` |
| Explain or investigate | Return evidence and open questions |
| Resume or merge | Read Status or Integration below |

## Branch and completion

Before editing files intended for Git, identify the current and integration
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

Read the request, relevant product requirements, roadmap, canon, decisions and
code. Read history when it helps explain a constraint. Resolve available facts
before asking. When acceptance conflicts with requirements or architecture,
show the disagreement and recommend a resolution. Code shows current behavior;
a document can also state an obligation that broken code fails to meet.

Group related material questions in rounds. Recommend a choice and state the
relevant costs of real alternatives. Record dated decisions in
`<notes>/<task>-decisions.md`. Reopen agreed choices on new evidence.

| Tier | Decision scope | Approval before implementation |
|---|---|---|
| 0 | No material decision remains | G1: exact change, scope, assumptions and verification |
| 1 | One material decision | G1 and G2 together: recommended solution, scope, assumptions and verification |
| 2 | A new boundary, invariant change or related decisions | G1 decisions, G2 design, G3 plan |

Name the decision that justifies the tier; file count does not set it. Wait for
approval of the concrete proposal, including at tier 0. A currently unused port
can belong to a stopped service; state what the check establishes when proposing
its replacement. The request alone does not approve values you selected.

Tier 1 needs one combined approval. Tier 2 runs `/sdd:design` after G1 and
`/sdd:plan` after G2. Approval persists within its scope across commits and
context compaction. G3 authorizes every planned step through a reviewable PR.

## Execute

For each step: implement, verify, commit, update the Status record below, then
continue. A step can contain several commits. Commit all changes from a completed step before starting the next.
Independent review is not a prerequisite for intermediate commits. Use English
Conventional Commits with a subject naming the change and a body stating its reason.

For behavior checked by a test, observe its intended failure before the fix.
For other changes, use a structural check, build, worked example or manual check.
Run relevant checks and required `verify` checks before committing. Read their
completed output. Repeat checks after relevant changes or for unresolved concerns.
Report commands, outcomes and omissions; limit claims to the evidence obtained.

Update affected subsystem documents in the same PR (`/sdd:subsystem`). Check
invariants, detectors and exceptions with `/sdd:canon`. No invariant change is
normal. Write durable decisions in `adr` using
`${CLAUDE_PLUGIN_ROOT}/templates/_ADR.md`: invariant changes, significant trade-offs
or choices whose reasons will be hard to recover. Update design and remaining
plan after agreed changes; routine corrections need no ADR.

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
committed state. Push, open the PR, report the result and stop before integration.
Describe the problem, resulting behavior, verification and limitations in the PR.

Independent review is required at every tier, including documents. The user
starts it; its depth follows risk and the change. Inputs are the review request,
committed artifacts, diff and primary requirements. Exclude author-session
reasoning as the basis for conclusions. Author-side checks do not replace it.

Report behavioral defects with severity and concrete evidence. Report process
deviations separately, without defect severity or an integration verdict: name
what is missing and which check lacks a basis.

Verify, commit and push requested fixes on the same branch. Report resolved and
remaining findings and their verification. The user starts any repeat independent
review. Without integration permission, stop before merge. Conditional permission
such as "fix these findings and merge" authorizes Integration below once its
conditions are met. Return changed decisions or scope to the user.

## Integration

G4 is the user's explicit permission to integrate the specific PR, after review.
On permission such as "merge this PR":

1. Resolve known integration blockers and run available checks before the final
   commit. Return changes to agreed decisions or scope to the user.
2. Close its ticket through `/sdd:tasks`, if one exists. Fill missing ADR PR
   references in the same final branch commit.
3. Run required checks, push and merge subject to required project checks.
   Report the actual result.

Do not ask again for method permission to run the merge command. Implementation
approval is not merge permission. Done records approval, not a completed merge.

If merge fails, report the cause and branch state. Permission persists within
its scope: resolve technical blockers, verify and retry when ready. Missing
access or changed decisions or scope trigger Stop conditions above. If repairs
are needed after the final commit, preserve history and append verified repair
commits. Do not rewrite published history or add an empty final commit solely
to keep Done last.

## Status

Keep `<notes>/<task>-status.md` outside Git. Record branch, task, tier, approved
decisions, passed gates, current step, check results and open questions. Link
the decision log and artifacts. Update after approvals and completed steps.

After a break or handoff, read status and current-stage instructions, check Git
state, and continue unfinished work. Reconcile conflicting evidence before
repeating a finished step. Store status rather than copies of method rules.
