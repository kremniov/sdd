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
