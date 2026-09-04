---
name: setup
description: Use to install this spec-driven method into a repository — survey the existing docs layout, write .sdd.yml, create the missing scaffold, and put the resident rules into CLAUDE.md or AGENTS.md. Run once per project, and safe to re-run.
---

# Setting up

Install the method into this repository. Adoption is additive: overwrite no file
you did not write, and reformat none that already exists. Report anything you
would have changed, and let the user decide.

## 1. Survey what is here

Do this before asking anything, and record the actual paths.

- `CLAUDE.md` or `AGENTS.md` at the root, and whether it already describes a
  development process.
- A docs directory, and anything inside it resembling architecture notes, a
  decision log, a task list, a roadmap, or per-feature specs.
- The verification command. Read `Makefile`, `package.json` scripts, `justfile`,
  `Taskfile.yml`, the CI workflows. What does this project run to know it is
  green?
- The ticket-id convention already in use. Grep issues, branch names and commit
  messages for a prefix such as `T-`, `ABC-` or `#`.
- Whether the repository has a git history worth reading. A fresh `git init` and
  a five-year-old codebase need different treatment in step 5.

## 2. Confirm the map

Print the proposed `.sdd.yml` as an ordinary message first — the whole file,
every line, with your inference for each key and a marker on what you could not
find. Then ask whether it is right, once, about the whole file.

The user has to be able to read the file at the moment they approve it. Put the
rendered YAML inside the question itself, in the option preview.

Prefer what exists over the default. A project with `documentation/adr/` keeps
that path.

```yaml
# .sdd.yml — where this project keeps the artifacts the method uses.
canon:    docs/architecture/
tasks:    docs/tasks.md
roadmap:  docs/roadmap.md
features: docs/features/
adr:      docs/adr/
notes:    docs/notes/
verify:   make lint && make test
ticket:   T
rules:    CLAUDE.md
```

| Key | Rule |
|---|---|
| `canon`, `features`, `adr`, `notes` | End in `/`. The scaffold concatenates them with a filename, so `docs/architecture` renders as `docs/architectureinvariants.md` into the project's own rules file, silently. Add the slash yourself and say that you did |
| `tasks`, `roadmap` | File paths |
| `verify` | A shell command that exits non-zero on failure. A `:` inside it is fine; only the first one separates key from value |
| `ticket` | The id prefix alone — `T`, never `T-` |
| any | No `#`. Everything from the first one is a comment, and quoting rescues nothing: the readers are deliberately simple. A project that numbers tickets `#41` uses a letter prefix here |

`notes` holds working notes that stay out of git: the decisions log a brainstorm
writes, and prompts. Propose the matching `.gitignore` line, show it, and write
it on a yes.

## 3. Write the config

Write `.sdd.yml` at the repository root. Where one exists, show the diff you
propose and change nothing without a yes.

## 4. Create what is missing

For each path in the config, create it from
`${CLAUDE_PLUGIN_ROOT}/templates/project/` **where nothing is there**.

| Config key | Scaffold source | Notes |
|---|---|---|
| `canon` + `invariants.md` | `invariants.md` | Header only. `/sdd:canon` writes the body |
| `canon` + `lessons.md` | `lessons.md` | Header only |
| `tasks` | `tasks.md` | |
| `roadmap` | `roadmap.md` | |
| `features`, `adr`, `notes` | — | Create the empty directory with a `.gitkeep`, because git drops an empty one |
| docs guide | `docs-README.md` | Goes in the parent directory of `canon`. Two refusals, both absolute: never the repository root, and never where a README exists. Where the parent of `canon` is the root, skip the file and say so |

Substitute every `{{key}}` with the value from `.sdd.yml`, and leave no
placeholder in a written file. Keep the marker lines exactly as the template
carries them, version included. They are what a later run compares against, and a
file written without them can never be updated.

**Where the file is already there**, compare the version stamps and carry the
described changes. `${CLAUDE_PLUGIN_ROOT}/skills/setup/reference.md` holds that
procedure and every branch of it.

## 5. Put the rules in the rules file

The target is the file recorded as `rules:` in `.sdd.yml`. Read
`${CLAUDE_PLUGIN_ROOT}/templates/project/CLAUDE.section.md`, substitute the
placeholders, and keep the `<!-- sdd:rules vN.N.N -->` markers.

These rules hold in a session where nobody invoked a skill, which is why they are
resident. The rest of the method is in `/sdd:work`.

| What you find | What you do |
|---|---|
| An `sdd:rules` fence | A previous run wrote it. Compare stamps and carry the described changes — `reference.md` |
| An `sdd:method-section` fence | The v0.x rules. Retire them — `reference.md` |
| No such file | Create it with this section, under a one-line title naming the project |
| The file exists with no process section | Append the section at the end. Touch nothing above it |
| The file exists and describes a process | Write the rendered section to `<file>.sdd-section` beside it, show the specific conflicts, and let the user decide. Two visible process files beat one silently merged |

Leaving the section out is a legitimate first choice, and often the right one:
the config and the scaffold alone let someone try the skills against their
existing process. Say what it costs. The rules that keep integration with the
user, that put evidence before a completion claim, and that make a test fail
first are in force only while they are in context. Until the section lands, what
is installed is the artifacts.

## 6. Report

State plainly:

- what was created, by path;
- what was left alone because it existed;
- what the scaffold changed since this project adopted, by version: which
  described changes were carried, which were declined and get offered again,
  which the project's own wording already satisfied, and which files have no
  fence. Nothing to carry is worth one line;
- anything you could not infer and guessed at;
- whether the rules section landed, and if it did not, that the method is not in
  force and what remains to be decided;
- what a previous method left behind that nothing references, by path;
- the next step. An empty `invariants.md` means `/sdd:canon` to establish one. A
  populated one means `/sdd:canon` in audit mode.

## Re-running

Safe. A second run re-surveys, reports what is now present, and creates only what
is still missing. It rewrites no file it finds, including one an earlier run of
itself wrote. The one thing it changes inside an existing file is a described
change, carried inside a fence, on a yes.
