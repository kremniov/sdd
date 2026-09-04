# SDD v2 — plan

**Ticket:** none — dogfooding is paused for this branch · **Design:** [design.md](design.md)

## Scope

When the last step is green, the method ships as version 1.0.0: about 300 words
resident, eight skills, a rewritten scaffold, six new ADRs, one new invariant,
and a script that measures the register. Dogfooding restarts on the last step.

Left for a follow-up ticket: output styles, and an eval corpus for the register.

## Order

The register checker lands first, so every later step is measured while it is
written. `/sdd:work` lands before the resident set, because `check_skill_refs.py`
rejects a text that names a skill which does not exist. The version bump travels
with the first stamp move, because `check_scaffold.py` rejects a stamp ahead of
the plugin's own version. `/sdd:setup` lands after the scaffold it installs. The
invariants and the ADRs land after the code, because they record what did land.
The vocabulary sweep runs late: every rewritten file is written in the new
vocabulary already, so the sweep touches only the files that were not rewritten.

Steps T04 to T08 are independent of one another and may run in any order.

## Steps

### T01 — The register is measurable

**Goal:** `scripts/check_register.py` reports length, heading depth and negation
density for every shipped file.

**Constraints:** python3 only (layout responsibilities). The script is not wired
into `check.sh` yet, so the branch stays green while the corpus is rewritten.

**Touches:** `scripts/check_register.py`. Thresholds from `design.md`, Testing.

**DoD:** `python3 scripts/check_register.py` runs, exits non-zero, and names
`canon/SKILL.md` and `setup/SKILL.md` over the word budget and the corpus over
2.5 negations per 100 words. That red output is the baseline. `./scripts/check.sh`
stays green.

### T02 — `/sdd:work` carries the frame

**Goal:** one skill holds the gates, the tier table, the closed blocker list, the
handing-over rules, the review rules, and the ADR and docs triggers.

**Constraints:** ASD-STE100. Invariant 1: every path comes from `.sdd.yml`.
Invariant 7: no justification prose. The gate and tier tables are `design.md`,
Architecture, verbatim in substance. G4 says: push the branch, open the PR, stop.

**Touches:** `plugins/sdd/skills/work/SKILL.md`, `plugins/sdd/templates/_ADR.md`.
`/sdd:work` names the `_ADR.md` path, which `/sdd:design` named before.

**DoD:** `./scripts/check.sh` green. `python3 scripts/check_register.py
plugins/sdd/skills/work/SKILL.md` green.

### T03 — The resident set shrinks to five rules

**Goal:** the project's rules file carries about 300 words under a new fence.

**Constraints:** fence `<!-- sdd:rules v1.0.0 -->`. The five rules are
`design.md`, Architecture. The section starts at H2 and carries no H1. The
version bump travels here because this is the first stamp at `v1.0.0`.

**Touches:** `plugins/sdd/templates/project/CLAUDE.section.md`,
`plugins/sdd/templates/project/CHANGES.md`,
`plugins/sdd/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`.

**DoD:** `./scripts/check.sh` green, including `check_scaffold.py`.
`check_register.py` reports the section under 400 words and under 2.0.

### T04 — `/sdd:design` and its skeleton

**Goal:** the design skill produces `design.md` only, and its skeleton states how
much closes each question.

**Constraints:** the input list names the ticket, the canon, the ADRs governing
the seam, **and the roadmap** — this fixes behaviour 4. Acceptance is a check,
not a specification. `_DESIGN.md` carries one watery-against-tight pair and the
written budgets from `design.md`, The templates.

**Touches:** `plugins/sdd/skills/design/SKILL.md`,
`plugins/sdd/templates/_DESIGN.md`.

**DoD:** `./scripts/check.sh` green. `check_register.py` green on both files.

### T05 — `/sdd:plan` and its skeleton

**Goal:** a skill named after `plan.md` produces it.

**Constraints:** the skill starts at G2 and ends at G3. It states that an
approved plan authorizes every step to a merge-ready branch, and it points at the
blocker list in `/sdd:work` rather than restating it. `_PLAN.md` carries a
contrast pair.

**Touches:** `plugins/sdd/skills/plan/SKILL.md`,
`plugins/sdd/templates/_PLAN.md`.

**DoD:** `./scripts/check.sh` green — `_PLAN.md` is now named by `/sdd:plan`.
`check_register.py` green on both files.

### T06 — `/sdd:canon` and the lessons file

**Goal:** the canon skill runs the falsifiability filter before the four Amend
questions, and it maintains `lessons.md`.

**Constraints:** this fixes behaviour 3. "No invariant moved" is stated as the
expected answer. The skill holds at most 1200 words; the bootstrap procedure
moves to `plugins/sdd/skills/canon/bootstrap.md` if it does not fit.

**Touches:** `plugins/sdd/skills/canon/SKILL.md`, and a reference file if needed.

**DoD:** `./scripts/check.sh` green. `check_register.py` green on the skill
directory.

### T07 — `/sdd:subsystem` and `/sdd:debug`

**Goal:** both skills read in the new register.

**Constraints:** `/sdd:debug` keeps the three-failed-fixes threshold, which
invariant 7 exempts. Its rationalization table is a table of rules, not of
excuses, or it goes.

**Touches:** `plugins/sdd/skills/subsystem/SKILL.md`,
`plugins/sdd/skills/debug/SKILL.md`.

**DoD:** `./scripts/check.sh` green. `check_register.py` green on both files.

### T08 — `/sdd:tasks`

**Goal:** the queue skill reads in the new register and keeps its contrast pair.

**Constraints:** the ticket slots and the Done collapse format do not change.
Only the prose does.

**Touches:** `plugins/sdd/skills/tasks/SKILL.md`.

**DoD:** `./scripts/check.sh` green. `check_register.py` green on the file.

### T09 — `/sdd:setup` and the migration

**Goal:** adoption installs v1.0.0, and a re-run offers to retire
`sdd:method-section`.

**Constraints:** the retirement is shown in full and applied only on an explicit
yes. A declined retirement writes no new fence and reports that the project runs
v0.x rules. Two method sections in one file are never written. The `notes:` key
is added to the config, with the `.gitignore` line proposed and asked. The fence
machinery moves to `plugins/sdd/skills/setup/reference.md`.

**Touches:** `plugins/sdd/skills/setup/SKILL.md`,
`plugins/sdd/skills/setup/reference.md`, `scripts/check_config.py`.

**DoD:** `./scripts/check.sh` green, `check_config.py` accepts `notes`.
`check_register.py` green on `SKILL.md`.

### T10 — The rest of the scaffold

**Goal:** every scaffold file reads in the new register and carries its `v1.0.0`
stamp, and `lessons.md` exists.

**Constraints:** ADR 0011 — a stamp that moves needs a `CHANGES.md` entry in the
same commit, written as a described change and never as a diff.

**Touches:** `plugins/sdd/templates/project/lessons.md` (new), `invariants.md`,
`tasks.md`, `roadmap.md`, `docs-README.md`, `CHANGES.md`.

**DoD:** `./scripts/check.sh` green, including `check_scaffold.py`.
`check_register.py` green on `templates/project/`.

### T11 — The vocabulary sweep

**Goal:** no shipped file outside the ADR directory says `operator`.

**Constraints:** ADR 0001–0015 keep their wording — invariant 11 exempts decision
records. The check is added here and must go red before the sweep.

**Touches:** `docs/architecture/*.md`, `README.md`, `docs/roadmap.md`,
`docs/tasks.md`, `scripts/check.sh`.

**DoD:** the new grep in `check.sh` runs red before the sweep and green after.
`./scripts/check.sh` green.

### T12 — The invariants and the ADRs

**Goal:** the canon records what this branch changed.

**Constraints:** invariant 8 — append, never renumber. Invariants 2, 3 and 4 are
reworded; invariant 12 is new. Six ADRs, numbered 0016 to 0021, subjects from
`design.md`, Invariants & docs. ADR 0019 amends ADR 0004. ADR 0017 leaves ADR
0012 standing.

**Touches:** `docs/architecture/invariants.md`, `layout.md`,
`plugin-mechanics.md`, `docs/adr/0016-*.md` to `docs/adr/0021-*.md`.

**DoD:** `./scripts/check.sh` green, including `check_canon.py`. Every new ADR
has title, status, date, context, decision, consequences.

### T13 — The register check becomes a gate

**Goal:** `check.sh` fails when shipped text misses a budget.

**Constraints:** the thresholds are the ones in `design.md`, Testing. Nothing is
allowlisted; a file that cannot meet the budget is rewritten or split.

**Touches:** `scripts/check.sh`, `CHANGELOG.md`, `README.md`.

**DoD:** `./scripts/check.sh` green with the register check wired in.

### T14 — Dogfooding restarts

**Goal:** this repository runs the method it ships.

**Constraints:** invariant 9 — `CLAUDE.md` is a render of the template, never an
edit. The paused marker goes. `.sdd.yml` gains `notes: docs/stuff/`, which this
repository already ignores.

**Touches:** `CLAUDE.md`, `.sdd.yml`.

**DoD:** `./scripts/check.sh` green, and the "own CLAUDE.md matches the template"
check reports OK rather than SKIP.

### T15 — Manual verification

**Goal:** adoption and migration are observed, not reasoned about.

**Constraints:** run in a separate clone under the scratchpad, never in this
worktree — a worktree shares refs and config with its repository.

**Touches:** nothing in this repository. The findings go in the PR body.

**DoD:** the four scenarios in `design.md`, Testing, each run and each reported
with its output.

## Verification

`./scripts/check.sh` after every step, and again at the end with the register
check wired in. The four manual scenarios of T15. The PR body carries both.

## Docs & ADR

`invariants.md`, `layout.md` and `plugin-mechanics.md` update in T12.
`CHANGELOG.md` and `README.md` update in T13. ADRs 0016 to 0021 are written in
T12; their `PR:` fields are filled in the last commit on the branch.
