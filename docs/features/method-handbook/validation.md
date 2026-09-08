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
