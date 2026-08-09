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
rules:    CLAUDE.md
```

Rules for the values, all four load-bearing:

- **`canon`, `features` and `adr` must end in `/`.** The scaffold concatenates
  them with a filename — `{{canon}}invariants.md`. A value without the slash
  renders as `docs/architectureinvariants.md` into the project's own rules file,
  silently. Add the slash yourself if the operator omits it, and say that you
  did.
- `tasks` and `roadmap` are file paths, not directories.
- `verify` is a shell command that exits non-zero on failure. A `:` inside it is
  fine — only the first one separates key from value.
- `ticket` is the id prefix without a number or separator (`T`, not `T-`).
- **No value may contain a `#`.** Everything from the first `#` is a comment,
  and quoting does not rescue it — the readers are deliberately simple and do
  not unquote. A project that numbers tickets `#41` uses a letter prefix here
  and keeps the `#` in its own prose; a verify command that needs a `#` goes
  into a script the command calls.

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
| docs guide | `docs-README.md` | The three-lifetimes table. See the placement rule below. |

**Where the docs guide goes.** Its home is the parent directory of `canon` — for
`canon: docs/architecture/` that is `docs/README.md`. Two refusals, both
absolute: never write it to the repository root, where it would compete with the
project's own README; and never write it where a README already exists. When the
parent of `canon` is the repository root, skip this file entirely and say so —
the guide is a convenience, and no project needs it badly enough to have its
front page displaced.

Substitute every `{{key}}` placeholder with the value from `.sdd.yml`. Do not
leave a placeholder in a written file.

An empty directory does not survive git. Where you create one, add a
`.gitkeep`.

## 5. Add the rules to the rules file

The rules must live in the project's rules file rather than only in this skill: they have to
be in context at execution time, and a skill is loaded only when something
triggers it.

The target file is the one recorded as `rules:` in `.sdd.yml` — `CLAUDE.md` by
default, `AGENTS.md` where the project uses that. Set that key in step 3 from
what step 1 found, so a later run does not have to re-derive it.

Read `${CLAUDE_PLUGIN_ROOT}/templates/project/CLAUDE.section.md` and substitute
the placeholders. The text is wrapped in `<!-- sdd:method-section -->` markers —
keep them, they are how a re-run recognizes its own work. Then, in order:

- **The file already contains `<!-- sdd:method-section -->`:** a previous run
  wrote it. Do not append. Diff the stored section against the freshly rendered
  one and, if they differ, show the operator the difference and ask — the
  divergence may be their edit, which you must not discard.
- **No such file:** create it with this section, preceded by a one-line title
  naming the project.
- **The file exists, no process section:** append the section at the end. Touch
  nothing above it.
- **The file exists and already describes a process** — under any heading
  (`How we work`, `Conventions`, `Workflow`, `Development`): do not merge them
  yourself. Write the rendered section to `<file>.sdd-section` beside it, show
  the operator the specific conflicts with what is already written, and let them
  decide. A silently merged process file is worse than two visible ones.

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
