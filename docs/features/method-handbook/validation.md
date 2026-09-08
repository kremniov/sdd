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
