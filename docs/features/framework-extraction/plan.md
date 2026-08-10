# Portable SDD framework — plan

**Ticket:** T-1 · **Design:** [design.md](design.md)

## Scope

When the last step is green, this repo is a Claude Code marketplace
holding one plugin that installs into any repository, brings five skills, three
artifact templates, and a project scaffold. Executes [design.md](design.md).

Left for follow-up tickets: a portable invariant checker (the origin repo's is
bash over one language's import paths), a roadmap-authoring skill, and publishing to GitHub.

## Order

The plugin manifest and config schema come first — every skill references the
config, so its shape must be settled before any skill is written. Templates
precede the skills that read them. `adopting-sdd` precedes `deriving-canon`
because the latter reads the config the former writes. The verification steps
run last and are the only gates.

## Steps

### Step 1 — The repo is a valid marketplace with an empty plugin

**Goal:** `/plugin marketplace add <local path>` succeeds and lists one plugin.

**Touches:** `.claude-plugin/marketplace.json`, `plugins/sdd/.claude-plugin/plugin.json`,
`.gitignore`, `LICENSE`.

**DoD:** both JSON files parse; `plugin.json` carries `name`, `version`,
`description`, `author`, `license`.

### Step 2 — Config schema and the three artifact templates

**Goal:** `_DESIGN.md`, `_PLAN.md`, `_ADR.md` ship de-projected — no invariant
numbers, no build commands, no language.

**Touches:** `plugins/sdd/templates/`, `.sdd.yml` schema documented in the
plugin README.

**DoD:** a grep for the origin's vocabulary over `templates/` is empty.

### Step 3 — The project scaffold, including the CLAUDE.md rules section

**Goal:** the files `adopting-sdd` writes into a project exist as templates: the
rules section, the docs README with the three-lifetimes table, and stubs for
`invariants.md`, `tasks.md`, `roadmap.md`.

**Touches:** `plugins/sdd/templates/project/`.

**DoD:** the rules section carries all eight rules named in design.md
§Architecture, and names no project-specific path outside `${config}`.

### Step 4 — `managing-tasks` and `systematic-debugging`

**Goal:** the two skills that carry over with the least change, de-projected and
config-driven.

**DoD:** neither names a path not read from `.sdd.yml`.

### Step 5 — `brainstorming`

**Goal:** the tier-2 entry point, reading the canon paths from config and the
skeleton from `${CLAUDE_PLUGIN_ROOT}`.

**DoD:** references `${CLAUDE_PLUGIN_ROOT}/templates/_DESIGN.md`.

### Step 6 — `adopting-sdd`

**Goal:** detect an existing docs layout, write `.sdd.yml`, create only missing
scaffold, append the rules section to `CLAUDE.md`, never overwrite.

**DoD:** the skill states the additive rule explicitly and reports what it
declined to touch.

### Step 7 — `deriving-canon`

**Goal:** read a codebase, propose the invariants it already holds, write
`architecture/invariants.md` + `layout.md` on confirmation. Re-runnable.

**DoD:** the skill refuses to write a speculative list when the codebase shows
no discernible rules.

### Step 8 — README and this repo's own canon

**Goal:** the repo explains itself to someone who has never seen it, and holds
the canon its own skills produce.

### Step 9 [gate] — Adoption into a bare repo

**DoD:** scaffold appears, `.sdd.yml` valid, `CLAUDE.md` created.

### Step 10 [gate] — Adoption into a repo that already has docs

**DoD:** nothing overwritten; config points at what exists.

### Step 11 [gate] — Adoption into a project in another language

**DoD:** no assumption from the origin's stack surfaces.

### Step 12 [gate] — `deriving-canon` against the origin repo

**DoD:** recovers the layering rules from code alone, without reading
`invariants.md`.

## Verification

Steps 9–12 run by the operator (me, in this autonomous run) against real
repositories. Static checks: every skill's frontmatter parses, every
`${CLAUDE_PLUGIN_ROOT}` path resolves to a file that exists, no skill names a
hardcoded project path.

## Docs & ADR

Three decisions marked `→ ADR` in design.md: plugin-not-starter, templates read
from plugin root, derivation separate from adoption.
