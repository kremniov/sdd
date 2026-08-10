# Scaffold updates — plan

**Ticket:** T-7 · **Design:** [design.md](design.md)

## Scope

When the last step is green, every scaffold file ships a version-stamped fence,
`templates/project/CHANGES.md` describes what changed per version per file, and
`/sdd:setup` compares stamps instead of text — silent when they match, offering
described changes when they do not. Executes `design.md`.

Left for a follow-up: nothing carried over from T-7's acceptance. The permission
rules of T-8 are unrelated and stay out.

## Order

The stamp has to exist before anything can compare it, and the checker has to
exist before the stamp can be trusted to stay correct — so: markers, then gate,
then change log, then the skill that reads both. The operator gate runs last
because it exercises the skill against a real repository.

## Steps

### Step 1 — Every scaffold fence carries a version

**Goal:** the five scaffold files open with `<!-- sdd:scaffold v0.2.0 -->` (and
`<!-- sdd:method-section v0.3.0 -->` for the rules section), each stamp naming
the version in which that region last changed.

**Constraints:** invariant 2 — one well-formed fence per file. The closer stays
bare. `CLAUDE.section.md` last changed in 0.3.0 (the integration rule); the
other four last changed in 0.2.0, when the fence was introduced.

**Touches:** `plugins/sdd/templates/project/*.md`, opener lines only.

**DoD:** `git diff` shows one changed line per file and nothing else;
`./scripts/check.sh` is red on `check_scaffold.py`, which does not yet know
about versions — read the failure and confirm it is the expected one.

### Step 2 — The gate enforces the stamp

**Goal:** `check_scaffold.py` requires a parsable version on every opener, no
version above the plugin's own, and fails when a fenced region changed against
`HEAD` without its stamp advancing.

**Constraints:** the checker reads `plugins/sdd/.claude-plugin/plugin.json` for
the ceiling. python3 only, no new dependency (layout table, `Checks`). The
`HEAD` comparison must be inert outside a git tree rather than an error.

**Touches:** `scripts/check_scaffold.py`.

**DoD:** `./scripts/check.sh` green. Then four mutations, each run from a clean
tree, each exiting 1 with the intended message: a stamp removed, a stamp
misspelled, a stamp above the plugin version, a region edited without a bump.
Restore after each.

### Step 3 — The change log ships

**Goal:** `templates/project/CHANGES.md` exists, with a 0.3.0 section holding
one entry for `CLAUDE.section.md` describing the integration-authority change
in terms a differently-worded region can absorb.

**Constraints:** entries describe the change, never quote the template as the
thing to install — a project's region shares no sentences with it. No version
section without a matching stamp somewhere in the scaffold.

**Touches:** `plugins/sdd/templates/project/CHANGES.md`,
`scripts/check_scaffold.py` for the cross-check.

**DoD:** `./scripts/check.sh` green; a mutation adding a 0.4.0 section that no
stamp reaches exits 1.

### Step 4 — The skill compares stamps

**Goal:** step 4's `Different` branch and step 5's diff-and-ask branch are
replaced by the one stamp comparison from the design, including the `0.2.0`
default, the ahead-of-template refusal, and the rule that a declined carry
leaves the stamp behind.

**Constraints:** invariant 3 — nothing is written without a yes. Invariant 1 —
no project path in the instructions. The skill states that a difference in text
is not, by itself, anything to report.

**Touches:** `plugins/sdd/skills/setup/SKILL.md` steps 4, 5 and 6 (the report
line about what the scaffold changed), `docs/architecture/invariants.md`
(invariant 2 and the layout table), `docs/adr/0011-*.md`,
`plugins/sdd/.claude-plugin/plugin.json` version, `docs/tasks.md`.

**DoD:** `./scripts/check.sh` green, including the skill-reference and
portability checks over the rewritten prose.

### Step 5 — Carry the change into a real prior adoption `[gate]`

**Goal:** a re-run against the project whose fenced regions hold its own prose
carries the 0.3.0 integration change and leaves that prose standing.

**Constraints:** the operator runs this; the diff is the evidence.

**DoD:** in the resulting diff — the rules section reflects the new integration
rule, the project's own wording elsewhere in the fence is untouched, the stamps
advanced only on files that were carried, and no line below a closing marker
moved.

## Verification

`./scripts/check.sh`, plus the mutation runs named in steps 2 and 3, plus the
operator gate in step 5.

## Docs & ADR

`docs/architecture/invariants.md` — invariant 2 and the layout table, in step 4.
ADR 0011 for the two design decisions marked `→ ADR`: the stamp on the marker,
and equal stamps ending the comparison.
