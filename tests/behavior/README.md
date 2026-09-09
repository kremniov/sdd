# Behavioral fixtures

`fixtures/` stores synthetic starting files and ordered baseline commits as JSON.
Optional `refs` create initial local branches; `working_files` supply ignored
status or other uncommitted initial state after those commits.
The runner creates a fresh Git repository for each preparation. Existing runs
are never reset or reused as inputs.

`scenarios/` stores target-agent prompts, instruction selection and links to
criteria in `tests/scenarios/`. Criteria are saved with evidence but are not sent
to the target agent. A scenario can contain ordered `turns`. Each has a target `prompt`, an evaluator
`gate`, and optional external input `files`. Gates are not sent to the agent.
The runner executes exactly one turn per invocation.

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
plugin snapshot and hashes. Each executed `turn-NN/` saves inputs, raw events, errors, Git history and the
final repository archive, including untracked working notes.
Keep evidence when removing temporary working directories.

Execution requires local Claude Code authenticated with `claude.ai`. The runner
removes API credentials and third-party provider overrides from its child
environment and refuses other authentication methods. It uses Sonnet medium by
default; Opus is an explicit option. It does not invoke the paid API directly.
The timeout terminates the CLI process group and preserves partial evidence.

The default mode supplies selected instructions explicitly. `mode: plugin`
loads the candidate through `--plugin-dir`, renders its resident rules into the
fixture, and retains the built-in system prompt. It omits `--safe-mode` and
does not inject skill bodies. Inspect tool events to establish actual skill
loading; plugin availability alone is insufficient. User/project settings and
hooks are disabled. Managed policies and any remaining ambient customization
are not controlled by the fixture; inspect initialization events for interference.
No mode establishes hosted merge behavior.
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

The six additional scenarios below cover the previously identified gaps.
Do not count fixture preparation as observed behavioral success.

The CLI flags follow the installed `claude --help` and the official
[CLI reference](https://code.claude.com/docs/en/cli-reference) and
[headless usage](https://code.claude.com/docs/en/headless) documentation.

## Advance a conversation

Prepare without calling Claude:

```sh
python3 tests/behavior/runner/run.py discover-work
```

Use the printed evidence directory to run the prepared first turn:

```sh
python3 tests/behavior/runner/run.py --continue-run <evidence-directory> --turn 1 --execute
```

After inspecting the completed first turn against the next turn's gate:

```sh
python3 tests/behavior/runner/run.py --continue-run <evidence-directory> --turn 2 --approve-gate --execute
```

Omit `--execute` to preview the prompt and gate without supplying external files
or calling Claude. `--approve-gate` records the evaluator's decision to supply
that scripted message; it is not a method gate sent to the target agent. Do not
advance if the observed proposal exceeds the approval scripted in the next turn.
Record the discrepancy and adjust the scenario separately.

Multi-turn scenarios use `--session-id` and then `--resume` with the same saved
UUID. Claude therefore persists session data in its local storage. The runner
keeps raw events and repository snapshots per turn; it does not delete Claude's
session store. Temporary repositories must remain available for continuation.
Reusing a turn number, skipping a turn or overwriting an attempted turn is refused.
After an error, keep evidence and start a new run. Candidate plugin files and
scenario inputs come from the saved run, not the current checkout.

## Six coverage gaps

The new `discover-work`, `debug-custom-verify`, `foreign-queue`,
`ticket-lifecycle`, `interrupted-step` and `merge-without-review` scenarios
have dedicated evaluator documents. Preparation and CLI-stub tests check the
fixtures and runner; live behavioral evaluation remains a separate step.

The four current cases that previously configured `true` now run
`python3 verify.py`: discover-work checks matching port references, foreign-queue
checks preserved rows and state/result consistency, interrupted-step requires
all final files, and merge-without-review checks export content. Each invocation
logs its observed inputs and pass/fail result to ignored `verify-runs.jsonl`.
Compare those records with actual tool events and scenario criteria; the log
alone does not prove the intended state transition or an approved port choice.
Historical fixtures retain their original verification commands.
