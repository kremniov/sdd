# The SDD method

Status: agreed on 2026-09-08. This document describes the complete method for
users and maintainers. Skills provide the instructions for each activity.

## Purpose and roles

SDD takes a task to a verified change that the user can assess and accept.
Discussion and documents scale with unresolved decisions and the consequences
of an error.

The user sets the goal, constraints and priorities. The user approves material
decisions and integration. The agent researches, documents, implements, verifies
and opens the pull request. The agent merges after the user's explicit
permission. Implementation details within the approved constraints belong to
the agent.

Reports distinguish observed facts, assumptions and unknowns. Completion claims
include the checks that support them.

## Sources and records

| Source | Content | Update |
|---|---|---|
| User request | Current goal, constraints and permission | When the task changes |
| Ticket | Outcome, necessary context, acceptance and references | When scope or status changes |
| Product requirements and roadmap | User needs and direction | When requirements or direction change |
| Architecture canon | Current rules, component boundaries and interactions | In the PR that changes them |
| ADR | A durable decision, alternatives and consequences | With its implementation |
| Design | The agreed feature behavior and structure | Through agreed changes before merge |
| Plan | Implementation order and verification | As execution changes before merge |
| Working notes | Questions, discussion decisions and status | During work |
| Lessons | Verified project observations useful to later work | When new knowledge appears |

Project configuration supplies the paths. A direct request can start work
without a ticket. Acceptance criteria must serve the goal and preserve required
contracts and constraints. When sources conflict, identify the disagreement and
propose a resolution to the user.

Code establishes current behavior. Documents also record obligations. Either can
be wrong when they disagree. After merge, design and plan remain historical;
the canon describes the current system and ADRs preserve decision history.

## Routes

| Request | Route and result |
|---|---|
| Change code, configuration or documents | Research, approval by tier, implementation, verification, PR |
| Diagnose and fix a bug | Diagnosis, approval of the proposed change, the change route |
| Review or audit | Research and report; fixes need a separate instruction |
| Add or update a ticket | Update the queue; this does not authorize implementation |
| Adopt or update SDD | Survey, propose exact changes, apply agreed changes, verify |
| Explain or investigate | Evidence and open questions; artifacts as needed |

Before editing files intended for Git, check the current branch and identify
the integration branch from project conventions and Git state. If on `main`,
`master` or another integration branch, create a working branch first. Commit
and push only to working branches. Changes enter an integration branch through
a PR merge after explicit user permission. Use a separate worktree when
isolation is needed or requested. Preserve the user's existing changes.

Standalone operations that change files intended for Git also end with
verification, commits and PR handover. This includes documents, queue edits and
method setup. Operations within ongoing approved work use that work's step and
PR. Ignored working notes need no commit or PR. Preparing a ticket or design
does not authorize implementing its subject.

## Tiers and approvals

Assess unresolved decisions after initial research. File count does not set the
tier. Explain a higher tier by naming the decision or boundary it requires.
Reassess when new evidence changes the work.

| Tier | Unresolved work | Proposal before implementation |
|---|---|---|
| 0 | No material decision remains | Exact change, scope, assumptions and verification; wait for approval |
| 1 | One material decision | Recommended solution, scope, assumptions and verification in one message |
| 2 | A new component boundary, an invariant change, or multiple interdependent decisions | Agreed decisions, design and plan |

Tier 2 takes precedence even when a boundary or invariant change involves only
one material decision. Interdependent decisions constrain one another; sharing
a topic alone does not make them interdependent.

| Gate | User approves | Agent proceeds to |
|---|---|---|
| G1 | Scope, tier and material decisions | Implementation at tier 0; design at tier 2; combine with G2 at tier 1 |
| G2 | Design, or the tier-1 proposal | Implementation at tier 1; plan at tier 2 |
| G3 | Plan | Every approved step |
| G4 | Integration of the specific PR, with its result and review | Final ticket commit, push and merge |

Tier 1 combines G1 and G2 in one approval. Tier 0 also waits for approval of the
concrete proposal. A request to solve a problem does not confirm values or
constraints the agent selected independently. A port that has no listener now
may still belong to a stopped service. State that limit when proposing it.

Approval remains valid for the agreed scope and decision across commits, breaks
and context compaction. Implementation approval does not authorize integration.

## Research and discussion

Read the request and relevant requirements, canon, decisions and code. Read
history where it helps explain a constraint or failure. Re-read material when
it changes or is lost from context.

Resolve questions from available project evidence before asking the user. A
material question changes behavior, a contract, scope, an architectural
constraint or significant cost. Group related questions in one round. Recommend
a solution and state the relevant cost of real alternatives. Reopen an agreed
decision when new evidence requires it.

Record dated decisions in the working log. Present the resulting decisions for
approval when the material questions are resolved.

## Design and plan

Read the agreed decision log and its source constraints. Prepare a complete
design for G2. Present sections separately when the user requests that process.

| Design content | What answers it |
|---|---|
| Problem and goal | Observed problem and required result |
| Scope | Included work and adjacent work likely to be included by mistake |
| Decisions | Choice and the constraint that determined it |
| Structure | Contracts, data, interactions and important ordering |
| Failures and transition | Failure handling, recovery, compatibility and rollout where affected |
| Verification and documents | Evidence of success and documents to update |

End a section when its question is answered. Omit empty sections. There is no
minimum number of decisions or sentences. Retain a detail if deleting it leaves
a material choice open or prevents verification.

A plan gives each step an observable result, constraints, affected parts and a
check. Link contracts from the design. Agree a new material choice there first.
Keep function bodies out of the plan. Order steps by dependencies and identify
independent steps.

A step can contain several commits. Verify and commit every completed step
before starting the next. Do not accumulate the whole plan as an uncommitted
diff or wait for independent review to make intermediate commits.

An automated check states a command and expected result. A manual check states
the procedure, expected observation and person who runs it. Verify the complete
branch after all changes, including documentation.

## Execution and stops

Run the approved scope to completion. For each step: implement, verify, commit,
continue. Progress reports do not request permission to continue.

Pause dependent work and ask when:

- different readings materially change the requested work;
- new evidence requires changing an agreed contract, decision or scope;
- an external party must decide or agree;
- a necessary action exceeds the permission given;
- required access or information is missing;
- a planned point of human participation is reached.

State the evidence, effect and recommended action. Continue independent,
authorized work while awaiting an answer. Choose naming, file placement, test
structure and formatting within the agreed constraints yourself.

Update the design and remaining plan after an agreed decision changes. Record a
durable architectural choice in an ADR. A typo correction or reordering of
independent steps does not require an ADR.

## Verification and diagnosis

Before a bug fix, reproduce the failure or collect observations that can test a
hypothesis. Distinguish a failed hypothesis from a failed fix. Investigate the
error, recent changes and the path of incorrect data. Use the smallest experiment
that distinguishes a hypothesis. Evaluate a previous fix before adding another.

For behavior covered by an automated test, observe that test fail for the
intended reason before implementing the fix. For changes without that behavior,
use an appropriate structural check, build, worked example or manual observation.
Do not invent a test solely to satisfy a process step.

After three failed fixes, stop the series and present the attempts, evidence
and options to the user. Reconsidering the architecture is an option; the count
does not establish the cause.

Check the affected change before committing and the step's result before
finishing it. Run the project's required checks after all code and document
changes. A commit alone does not require the full suite again. Repeat a check
after a relevant change or while a concern remains unresolved. Report
commands, results and omissions. A partial check supports a partial claim.

## Canon, ADRs and lessons

The canon contains invariants, a system map and subsystem documents. A candidate
invariant must have an identifiable violation and a material consequence.
Repetition alone does not establish an invariant.

Each invariant states the rule, how a violation is detected and what to do.
Label a manual check as manual. Preserve numbers. Agree changes or retirement
with the user and record them in an ADR.

On a changed branch, check affected claims, new required rules, changed checks
and exceptions. No canon change is a normal result. To establish a canon,
inspect code and available obligations, then present evidence and candidates.
Keep unconfirmed proposals out of the current rules.

An audit compares each rule with code and checks. Report held, inaccurately
described, broken and undocumented rules. Widespread violations do not authorize
retiring a rule. Subsystem documents explain responsibility, contracts,
interactions and ordering. Update them in the same PR as the behavior. A file
inventory belongs in the map.

Write an ADR for a decision that remains important after the task: an invariant
change, a significant trade-off or a choice whose reason is hard to recover.
Lessons record verified project observations, without duplicating rules or
general advice.

## Review and integration

Plan steps are committed before handover. Run final checks and self-review.
Verify and commit resulting corrections. Confirm the checked state matches the
commits, push the branch, open the PR and report its state. Stop before integration.

The PR describes the problem, resulting behavior, verification and limitations.
Independent review is required at every tier, including document changes. The
user starts it. Its depth follows the risk and contents of the change. Inputs
are the review request, committed artifacts, diff and primary requirements.
Author-session reasoning is not supplied as the basis for conclusions.
Self-review does not replace independent review.

Behavioral defects carry severity and evidence. Report process deviations
separately: what is absent and which check lacks its required basis. They carry
no defect severity. The user decides integration.

Verify, commit and push requested fixes on the same branch. Report resolved and
remaining findings and their verification. The user starts any repeat independent
review. Stop before merge without integration permission. If the user already
authorized "fix these findings and merge", proceed to integration once the stated
conditions are met. Return changes to agreed decisions or scope to the user.

After explicit permission such as "merge this PR", resolve known integration
blockers and run available checks before the final commit. Close the ticket in
that commit, fill missing ADR PR references, run required checks and push. Then
merge subject to required project checks and report the result. The method
requires no second permission for the merge command. Skip ticket closure if
there is no ticket. Done on the working branch records integration approval;
it reaches the integration branch with the change. Confirm actual merge separately.

If merge fails, report the cause and branch state. Permission remains valid
within its approved scope. Resolve technical blockers, verify and retry when
ready; stop dependent work for missing access or changes to agreed decisions or
scope. If repairs become necessary after the final commit, preserve history and
append verified repair commits. This is an exception to Done being last: do not
rewrite published history or add an empty final commit solely to restore that
order.

## Queue

A ticket has a stable ID, short title, outcome and checkable acceptance criteria.
Include context when omitting it loses the reason or a constraint. Link primary
requirements, dependencies and code. Ticket creation need not settle the
implementation. Criteria scale with the outcome; execution order belongs in a
plan when one is required.

Preserve an existing queue's fields, structure, labels, ID conventions and
completed-entry format. Map method states to project statuses. If required
content or a state cannot be expressed unambiguously, propose a concrete addition
and agree it before changing the format. Use the skill's format for a new queue.

Check the whole queue, including completed entries, before allocating an ID.
Never reuse IDs. For an existing ticket, set in-progress when execution starts
or resumes. Set blocked when an obstacle prevents continuing the task and no
independent authorized work remains. A blocked part alone does not block the
whole ticket. Working notes retain details but do not replace the queue status.
These transitions do not require creating a ticket. Done records integration
approval as described above. A completed entry keeps the result and change
reference.

## Adoption and updates

Survey documents, active instructions, ticket conventions and verification.
Show the path configuration and concrete changes. Preserve the project's
structure unless the user chooses otherwise. Create missing files and apply
approved changes. Present process conflicts before replacing instructions.
Choose the working-notes location and storage policy explicitly.

Compare managed-section versions on updates. Carry changes by meaning while
preserving project additions. Equal versions require no change. Report ambiguous
boundaries, malformed markers and unknown versions. Show a replacement section
in full and apply it with approval. Report applied, skipped and declined changes
and unresolved conflicts. Re-running must not duplicate completed changes.

## Resuming work

Keep one status file per task in the configured notes directory. Record the
branch, task, tier, approved decisions, passed gates, current step, check results
and open questions. Link artifacts and the decision log.

After a break, read the status and current-stage instructions, check the branch
state and continue unfinished work. Do not copy method rules into status. Use
the same state check when another agent takes over.

## Instruction quality and validation

Shipped artifacts in this plugin are English. Use ASD-STE100 as a readability
reference: direct sentences, consistent terms and an explicit actor. Keep
negation when it states the constraint most precisely. Omit rhetorical questions,
metaphors and rule-origin stories from working instructions.

A rule specifies an action, condition, authority boundary or result. Keep a
reason when it is needed to choose the correct action; put other decision
history in ADRs or method-development records. Code comments explain constraints
that the implementation leaves unclear. Remove comments that restate code.

A skill states its trigger, inputs, actions, result and stopping conditions.
One skill owns the overall procedure. Specialized skills have enough inputs for
standalone use. Resident text contains rules needed without a skill and routing.
Templates specify sufficient content. Examples resolve actual ambiguity.
References have explicit loading conditions.

Length and heading depth have budgets. Negation frequency is a review signal.
Counters do not establish clarity or correctness. Cut repetitions, rhetoric and
unnecessary transitions before details that affect action or verification.

Validate scenarios against expected actions and allowed stops. Record omissions,
unnecessary questions, invented decisions, context retention, artifact quality
and loaded instruction size. Distinguish a textual walkthrough from an observed
agent run. Map method rules to instruction owners and checks. During rewrites,
compare the old set at the end for useful constraints that were missed. Resolve
conflicts in this document before changing its derived instructions.
