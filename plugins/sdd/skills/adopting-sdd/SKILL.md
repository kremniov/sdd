---
name: adopting-sdd
description: Use to install this spec-driven method into a repository — detect the existing docs layout, write .sdd.yml, create the missing scaffold, and add the rules section to CLAUDE.md. Run once per project; safe to re-run.
---

# Adopting SDD

Install the method into this repository. **Additive only:** never overwrite a
file you did not write, never reformat one that already exists. Anything you
would have changed is reported to the operator instead.

## 1. Survey what is already here

Do this before asking anything. Look for, and record the actual paths:

- `CLAUDE.md` (or `AGENTS.md`) at the root, and whether it already describes a
  development process.
- A docs directory, and inside it anything resembling: architecture notes, a
  decision log, a task list, a roadmap, per-feature specs.
- The verification command: read `Makefile`, `package.json` scripts,
  `justfile`, `Taskfile.yml`, CI workflow files. What does this project run to
  know it is green?
- The ticket-id convention already in use, if any — grep existing issues,
  branch names, commit messages for a prefix like `T-`, `ABC-`, `#`.
- Whether the repo has a git history worth reading (a fresh `git init` and a
  five-year-old codebase need different treatment in step 5).

## 2. Confirm the map

Present what you found as the proposed `.sdd.yml`, with your inference for each
line and a marker for what is missing. Ask once, as a single message — not one
question per key.

Prefer what exists over the default. A project with `documentation/adr/` keeps
that path; do not relocate anyone's docs.

```yaml
# .sdd.yml — where this project keeps the artifacts the method uses.
canon:    docs/architecture/
tasks:    docs/tasks.md
roadmap:  docs/roadmap.md
features: docs/features/
adr:      docs/adr/
verify:   make lint && make test
ticket:   T
```

Rules for the values: directory paths end in `/`; `verify` is a shell command
that exits non-zero on failure; `ticket` is the id prefix without a number.

## 3. Write the config

Write `.sdd.yml` at the repo root. If one already exists, show the diff you
propose and change nothing without a yes.

## 4. Create only what is missing

For each path in the config, create it from the scaffold at
`${CLAUDE_PLUGIN_ROOT}/templates/project/` **only if nothing is there**:

| Config key | Scaffold source | Notes |
|---|---|---|
| `canon` + `invariants.md` | `invariants.md` | Header and instructions only — the body comes from `/sdd:deriving-canon`. |
| `tasks` | `tasks.md` | |
| `roadmap` | `roadmap.md` | |
| `features` | — | Create the empty directory. |
| `adr` | — | Create the empty directory. |
| docs root `README.md` | `docs-README.md` | The three-lifetimes table. Only if the docs root has no README. |

Substitute every `{{key}}` placeholder with the value from `.sdd.yml`. Do not
leave a placeholder in a written file.

An empty directory does not survive git. Where you create one, add a
`.gitkeep`.

## 5. Add the rules to CLAUDE.md

The rules must live in `CLAUDE.md` rather than only in this skill: they have to
be in context at execution time, and a skill is loaded only when something
triggers it.

Read `${CLAUDE_PLUGIN_ROOT}/templates/project/CLAUDE.section.md`, substitute the
placeholders, and:

- **No `CLAUDE.md`:** create it with this section, preceded by a one-line title
  naming the project.
- **`CLAUDE.md` exists, no process section:** append the section at the end.
  Touch nothing above it.
- **`CLAUDE.md` exists and already describes a process:** do not merge them
  yourself. Show the operator what the section would add, name the specific
  conflicts with what is already written, and let them decide. A silently
  merged process file is worse than two visible ones.

If the project uses `AGENTS.md` instead, write there.

## 6. Report

State plainly:

- what was created, by path;
- what was left alone because it already existed;
- anything you could not infer and guessed at;
- the next step: `/sdd:deriving-canon` to populate `invariants.md`, which is
  empty until it runs.

## Re-running

Safe. A second run re-surveys, reports what is now present, and creates only
what is still missing. It never rewrites a file it finds — including one an
earlier run of itself wrote, which by then may have been edited by hand.
