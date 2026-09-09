# Method rewrite validation

Date: 2026-09-08. Base: `b7b49f4` on `v2-method`.

## Structural checks

- `SDD_BASE=b7b49f4 ./scripts/check.sh`: passed, including 10 register tests.
- All eight skills pass the skill-creator frontmatter validator.
- `git diff --check`: passed.
- The initial register test run exposed three failures: fenced examples escaped
  the size budget, directory arguments failed, and tilde-fenced headings were
  mistaken for structure. The corrected checker passes those cases.

## Size

Counts use the same word expression on both revisions and include fenced examples.
They describe source volume, not measured token use or behavioral effectiveness.

| Scope | Base | Rewritten |
|---|---:|---:|
| Resident section | 309 | 195 |
| Skills and local references | 7464 | 4492 |
| Templates excluding migration history | 2103 | 1110 |

Migration history remains available and is included in the checker's separate
corpus report. It is not part of every invocation.

## Scenario evidence

All 18 cases have an author textual walkthrough. Six adoption states were also
operated by the author in disposable fixture repositories: fresh, existing
process, accepted update, declined update, equal-version re-run and malformed
markers. These are not independent-agent executions.

Observed runs used the installed Claude Code CLI with subscription authentication,
without API keys or third-party provider overrides. The default observed model was
`claude-sonnet-5`. Safe mode excluded inherited custom instructions; supplied
skills and synthetic fixtures defined the input. No live PR was merged or mutated.

| Case | Observation | Limit |
|---|---|---|
| Port conflict | Read the fixture, proposed 8000 with the stopped-service caveat, waited for approval; Git remained unchanged | Preapproval phase; no real network binding test |
| Three failed fixes | Read the attempts, stopped before another fix and requested evidence/options without asserting an architectural cause | Synthetic attempts; no application diagnosis |
| Fresh adoption | Created six correctly rendered files and ignored notes; parent checks confirmed markers and placeholders | Shell checks were explicitly skipped by the agent and verified separately |
| Intermediate commits | Tool events show each commit before the next file write; Git contains three step commits | Local fixture only, no PR service |
| Intermediate commits after correction | Updated status after each committed step; event order and final status verified | One rerun, not a reliability estimate |
| Merge permission, response only | Recognized G4 and described final ticket commit, checks, push and merge without another approval | No merge execution; tests reasoning only |

The first intermediate-commit run omitted the status file. The work skill now
places status update directly in the step sequence; the targeted rerun performed
it. The scenario now checks this action explicitly.

Two initial probes without file tools returned incomplete inspection statements.
They are inconclusive and excluded from successful behavior claims. They were
replaced by the port and diagnostic file-based runs above.

Raw prompts, outputs, tool-event logs and local walkthroughs remain in ignored
`docs/stuff/eval-runs/`. The versioned scenario inputs and evaluation procedure
are in `tests/scenarios/`.

## Review limits

These checks were performed from the author session. They do not replace the
independent review started by the user. Full agent-run coverage of all 18 cases,
real-project migration and actual hosted-PR integration have not been performed.

## Review correction: standalone branch handover (2026-09-08)

The user approved one Tier 1 correction: before editing files intended for Git,
leave an integration branch; commit and push only to working branches and hand
over standalone changes by PR. Embedded operations share the ongoing work.

Observed in disposable repositories with installed subscription Claude Code,
Opus medium: tasks from main and setup from master switched branches before
file edits and left integration refs unchanged. Each verified and committed on
its working branch, then reported unavailable remote/PR hosting. An embedded
queue operation stayed in the current working branch and left the parent step
unfinished, with no separate PR. Event order and final refs were inspected.
Some compound shell commands were denied; permitted tool retries completed.

These runs supplied resident, work and the selected skill explicitly. They do
not prove automatic skill discovery, hosted push/PR/merge, or behavior with a
custom integration-branch name. The fixture command true does no functional
checking. Evidence: ignored docs/stuff/eval-runs/standalone-branch-handover/.
Structural checks (SDD_BASE=fe0bd84), 10 checker tests, all eight skill validators
and diff whitespace checks passed. Scenario: standalone-branch-handover.md.

## Review correction: fixing reviewed work (2026-09-08)

The user approved a Tier 1 clarification: verify, commit and push requested fixes,
report findings and checks, and preserve scoped conditional merge permission.
Repeat independent review remains user-started.

Three response-only probes in installed subscription Claude Code (Opus medium)
recognized the expected next action: fix-only stops before integration;
fix-and-merge proceeds without another approval; an explicit repeat-review
condition waits. Work and tasks were supplied with completed fix state and no
tools. These probes do not prove edits, commits, pushes or merges. The merge
answer used an illustrative ticket result, so ticket-content preservation was
not established. A changed-scope case was checked textually only.
Evidence: ignored docs/stuff/eval-runs/review-fix-handover/.
Structural checks (SDD_BASE=34d746b), 10 checker tests, the work skill validator
and diff whitespace checks passed. Scenario: review-fix-handover.md.

## Review correction: failed merge recovery (2026-09-08)

The user approved resolving known blockers before the final commit, retaining
scoped permission after failure and allowing verified repair commits after Done
without rewriting published history solely for order.

Three response-only probes in installed subscription Claude Code (Opus medium)
selected retry after service recovery, verified repair commits and retry for a
mechanical path correction, and discussion for a contract conflict. Published
history was preserved in all proposed actions. The service-recovery answer also
added an overly broad stop condition for future content errors; the explicit
mechanical-repair case continued correctly. Multi-turn consistency is unproven.
No tools, edits, commits, push or merge were executed. Initial preparation before
Done was checked textually only. Evidence: ignored
`docs/stuff/eval-runs/failed-merge-recovery/`.
Structural checks (SDD_BASE=b94cc50), 10 checker tests, work/tasks validators and
diff whitespace checks passed. Scenario: failed-merge-recovery.md.

## Review correction: verification frequency (2026-09-08)

The user approved removing mandatory full verify before each intermediate
commit. Affected changes and completed steps retain their checks; full verify
runs after all changes and repeats for relevant changes or unresolved concerns.

Observed in installed subscription Claude Code (Opus medium): an approved
two-step document plan produced three separate commits, each after content
inspection. The first step completed before the second began. Full verify ran
once, after all three files existed, and passed. Tool order, invocation log and
Git history were inspected. No remote/PR operation was available. A later
relevant-change case was checked textually only. The evaluated paragraph was
then shortened without changing conditions to fit the skill budget; final
wording received semantic review and structural validation.
Evidence: ignored docs/stuff/eval-runs/verification-frequency/.
Structural checks (SDD_BASE=143a39c), 10 checker tests, the work validator and
diff whitespace checks passed. Scenario: verification-frequency.md.

## Review correction: ticket execution status (2026-09-08)

The user approved existing-ticket updates at execution start, blocking and
resumption. Work calls tasks; tasks distinguishes a blocked part from a blocked
whole task. Notes do not replace queue status; no ticket is required for direct
work and Done remains tied to integration.

Validation was delegated to a cheaper background agent (gpt-5.6-luna), using
installed subscription Claude Code Sonnet medium for the fixture. One observed
session changed next to blocked on missing access and committed the queue edit.
It also disputed missing preparation artifacts in the fixture, so this is only
evidence of a blocked update, not a complete lifecycle pass. The resume attempt
hung without evidence and was interrupted. Start/resume transitions, independent
continuation, no-ticket work, Done gating and step-order preservation were
reviewed textually only. No hosted PR or merge was executed.
Evidence: ignored docs/stuff/eval-runs/ticket-status/.
Structural checks (SDD_BASE=d01b507), 10 checker tests, work/tasks validators
and diff whitespace checks passed. Scenario: ticket-status-transitions.md.

## Review corrections: remaining text edits (2026-09-08)

The user approved eight separate commits: preserve queue conventions; prioritize
tier 2; define working-note storage and status timing; require approval of changed
decisions; distinguish invariant wording edits from rule changes; shorten the
CHANGES introduction; adopt the current lessons introduction; finish editorial
cleanup. Russian working documents were updated outside Git.

Validation is limited to author-side text review and local structural checks.
`SDD_BASE=2e59e19 ./scripts/check.sh` passed, including the 10 checker tests.
All eight skill frontmatter validators and `git diff --check` passed. Work uses
1199 words against its 1200-word limit. Editorial skill reflow was checked for
word preservation, apart from the approved breaks clarification and tasks
deduplication. Existing lesson entries and migration history were preserved.

No Claude Code sessions or behavioral evaluations were run for this batch, as
requested. The previously recorded evidence limits remain; behavioral testing
is deferred until after these text corrections.

## Reusable behavioral inputs (2026-09-08)

Added `tests/behavior/`: 16 baseline fixtures, ten scenario records (nine
executable and one blocked), and a preparation/explicit-execution runner. Nine
baselines came from first Git commits; seven were reconstructed from historical
harness inputs because their repositories had no commits. Historical adoption
walkthrough fixtures remain preparation-only. Criteria stay in `tests/scenarios/`.

Each preparation creates an independent temporary repository and preserves its
inputs and candidate plugin snapshot under ignored `docs/stuff/eval-runs/`.
Execution requires an explicit flag and local Claude subscription authentication.
The runner supplies instructions explicitly and supports one prompt; it does not
close discovery, continuation or actual merge coverage gaps.

Offline checks: four new unit tests passed (all baseline trees, isolation,
ordered history/file modes, scenario references, and verifier positive/negative
content). A CLI preparation of port-files succeeded without starting Claude.
`SDD_BASE=cb12b7f ./scripts/check.sh` passed, including 14 unit tests.
No model sessions were run. The execution and timeout paths have not been
validated with a live Claude process.

The verification-frequency input now uses real newlines instead of literal
backslash-n escapes. The ticket-status baseline is preserved but its scenario
is blocked pending concrete preparation/export inputs. These fixture repairs
are not evidence of a change in agent behavior.

A cheap background agent checked the runner as an author-side check. Its
preflight evidence finding was corrected: inputs and commands are saved before
authentication, and preflight stderr is retained without storing the auth profile.
This check does not replace independent method review.
A local CLI stub then simulated an authentication failure; inputs, commands,
preflight stderr and the final repository archive were all retained. The stub
did not invoke Claude Code or a model.

## Six coverage-gap scenarios prepared (2026-09-09)

Added discover-work, debug-custom-verify, foreign-queue, ticket-lifecycle,
interrupted-step and merge-without-review fixtures and evaluator criteria.
The catalog now contains 22 fixtures and 16 scenario records, one of which is
the blocked historical ticket-status input. The replacement ticket-lifecycle
provides concrete preparation, missing input and a working export verifier.

The runner now supports normal plugin loading and manually selected conversation
turns. It uses a persistent session ID and resumes it; each invocation executes
one turn. A next turn requires an evaluator gate acknowledgment. External input
changes are recorded separately from agent actions. Each turn retains raw output
and a repository archive; continuation checks the saved plugin hashes.

Local checks cover all baseline trees, clean initial state, ordered history,
ignored working notes, plugin command construction, continuation authority,
external input timing, stubbed success/error/timeout, actual fixture failure and
fix, preparation without input, export with input, and local merge rejection
before a synthetic review receipt followed by a real local fast-forward.
These are harness/fixture checks, not observed agent behavior. No live Claude
Code or paid API runs were started in this preparation step. Plugin discovery
and actual conversational continuation remain unvalidated with a live agent.

The foreign queue case supplies external work/review facts and checks queue
maintenance only. The merge case simulates the PR service and independent review
receipt; it does not validate hosted PR checks, remote push or actual independent
review. Existing method instructions were not changed.

Validation completed: nine offline fixture/runner tests passed;
`SDD_BASE=ea248b0 ./scripts/check.sh` passed with 19 unit tests. CLI preparation
of all six scenarios succeeded without calling Claude, including resident
rendering with no unresolved placeholders. A cheap background agent performed
a read-only consistency check of the six final scenarios and reported no
concrete mismatches. This author-side check is not independent method review.

## Opus 5 behavioral evaluation (2026-09-09)

Ran all six new scenarios against 50945b9: 13 completed target turns using
claude-opus-5, medium, local Claude Code 2.1.263 with claude.ai authentication.
Each multi-turn case resumed its original session. Raw result events and
repository archives were checked; no direct paid API or hosted Git action was
used. These are author-side evaluations, not independent method review.

| Scenario | Observed result and limits |
|---|---|
| discover-work | Loaded the candidate work skill; approved change committed on a working branch. Status note omitted. |
| debug-custom-verify | Reproduced failure, applied the exact fix and passed the project command. Evaluator advanced before the recorded work-loading gate; full protocol not passed. |
| foreign-queue | Preserved fields, existing rows and all five state operations. Closure input omitted an external change reference; target reported that gap. |
| ticket-lifecycle | Preparation verified and committed before blocking. First edit preceded inprogress, failing the scenario ordering criterion; resume not run. |
| interrupted-step | Preserved alpha; verified/committed beta before gamma edits; updated status and ran final check. |
| merge-without-review | Retained permission and merged locally after receipt, but also attempted merge before review; simulator rejected it. Configured true omitted. |

Port and debug runs omitted required working status; debug explicitly claimed a
tier-0 exception. Merge called verify: true no command, although it is configured
as a no-op. The merge gate checked unchanged master but did not explicitly reject
an attempted merge, so it failed to separate agent restraint from simulator
enforcement. These findings require discussion before instruction or fixture edits.

Restricted-mode permission denials were recovered through simpler commands.
The cheap merge evaluator exhausted its own limit after target execution; the
root reviewed saved evidence without repeating the run. Temporary repo paths
were later unavailable, but archives preserved refs and file states.

Raw evidence and the detailed classification are under ignored
`docs/stuff/eval-runs/opus-five-behavior-20260909/assessment.md`; per-case directories
are indexed there. No runner, scenario or method instruction was changed in
response, and no behavioral run was repeated. Independent review and integration
remain outstanding.

## Status creation sequencing correction (2026-09-09)

User approved moving status creation to the approval sequence. Work now creates
the ignored status file at first approval, before edits, across all tiers. The
Status section retains contents and update/resume instructions without repeating
the creation rule. English method and ignored Russian handbook are aligned.
Ticket ordering, merge prerequisites, runner and scenarios are unchanged.

Work remains within the 1200-word limit. Structural/frontmatter checks validate
the edit; no live behavioral repeat is claimed for this correction.

## Ticket start and resume sequencing correction (2026-09-09)

User approved updating an existing ticket before the first implementation edit
and before resuming blocked implementation. Work routes these transitions to
tasks; tasks defines the project status mapping and allows the update to share
the step's implementation commit. Research before implementation is not this
trigger. English method and ignored Russian handbook are aligned.

Block conditions, ticket creation rules and integration permission are unchanged.
This text correction has structural/frontmatter validation only; the previously
withheld live resume turn has not been run, and no behavior improvement is claimed.
