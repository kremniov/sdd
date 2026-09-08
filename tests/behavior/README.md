# Behavioral fixtures

`fixtures/` stores synthetic starting files and ordered baseline commits as JSON.
The runner creates a fresh Git repository for each preparation. Existing runs
are never reset or reused as inputs.

`scenarios/` stores target-agent prompts, instruction selection and links to
criteria in `tests/scenarios/`. Criteria are saved with evidence but are not sent
to the target agent. Keep subsequent user approvals explicit when adding a
multi-turn scenario; the current runner executes one prompt only.

## Prepare and run

From the repository root:

```sh
python3 tests/behavior/runner/run.py port-files
python3 tests/behavior/runner/run.py adoption-accepted --fixture-only
python3 tests/behavior/runner/run.py port-files --execute --model sonnet --timeout 300
```

Preparation does not invoke Claude. Each command creates a unique
`/tmp/sdd-behavior-*` directory and an evidence directory with the same name under
ignored `docs/stuff/eval-runs/`. Preparation saves the fixture, scenario, runner,
plugin snapshot and hashes. Execution also saves inputs, raw events, errors,
Git history and the final repository archive, including untracked working notes.
Keep evidence when removing temporary working directories.

Execution requires local Claude Code authenticated with `claude.ai`. The runner
removes API credentials and third-party provider overrides from its child
environment and refuses other authentication methods. It uses Sonnet medium by
default; Opus is an explicit option. It does not invoke the paid API directly.
The timeout terminates the CLI process group and preserves partial evidence.

The runner supplies selected instructions explicitly. It does not establish
resident-to-skill discovery, interactive continuation or hosted merge behavior.
CLI tool permissions are not an operating-system sandbox. Run only synthetic,
reviewed fixtures in the controlled local environment. Permission denials and
CLI errors are evidence to assess, not automatic method failures.

No exit code establishes a behavioral pass. Compare events, file states and
commit order with the linked criteria. Record pass, fail, incomplete or not run,
with the actions that support the judgment. Repeated runs use current plugin
files; metadata records the revision, dirty state and exact plugin hashes.

## Preserved cases

| Fixture | Origin and use |
|---|---|
| port-files | Port replacement approval; explicit work instructions |
| debug-files | Three failed fixes; explicit debug instructions |
| committed-steps, committed-steps-status | Intermediate commits and status; separate historical inputs |
| tasks-main, setup-master, tasks-embedded | Standalone branch protection and embedded queue edits |
| verify-frequency | Multiple commits within one step; final full verification |
| ticket-status | Archived baseline; execution blocked until initial conditions are repaired |
| fresh-adoption | Reconstructed empty input for the previous agent run |
| adoption-fresh, adoption-existing-process, adoption-accepted, adoption-declined, adoption-rerun, adoption-malformed | Reconstructed author-walkthrough inputs; prepare only |

Nine fixtures were recovered from their first Git commits. Seven had no baseline
commit and were reconstructed from the original harnesses, excluding generated
outputs. Each fixture records its provenance. Adoption stamp values preserve
historical inputs; `adoption-rerun` is not a current-version no-op test.

The recovered `verify-frequency` check used literal backslash-n text. Its saved
input now uses newline characters as required by the approved fixture design.
The ticket-status prompt claimed preparation was complete without matching
artifacts and left the export action unspecified. Its baseline remains archived;
it must not be treated as a complete lifecycle test.

Before testing remaining gaps, extend these inputs for discovery, custom verify,
foreign queue conventions, concrete status transitions, interrupted steps and
merge permission without review. Do not count fixture preparation as those tests.

The CLI flags follow the installed `claude --help` and the official
[CLI reference](https://code.claude.com/docs/en/cli-reference) and
[headless usage](https://code.claude.com/docs/en/headless) documentation.
