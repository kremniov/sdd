# Plugin mechanics

How the plugin reaches a project, and when each kind of file is read. This is
the seam the whole method rests on: get the timing wrong and a skill points at a
path the model cannot resolve.

Governed by invariants 1, 2 and 4.

## Responsibility

This document covers what crosses the boundary between the plugin and an
adopting repository, and in what order. It does not cover what the skills say —
that is each skill's own text.

## The three read moments

| Read at | What | Resolved by |
|---|---|---|
| Skill invocation | `templates/_DESIGN.md`, `_PLAN.md`, `_ADR.md` | `${CLAUDE_PLUGIN_ROOT}`, substituted into skill text before the model sees it |
| Adoption, once | `templates/project/*` | the skill, which substitutes `{{placeholders}}` from `.sdd.yml` and writes the result into the repo |
| Re-run, to compare | `templates/project/*` | the skill, which compares the version stamped on the template's fence against the project's |
| Every session | the project's rules file and canon | the project, as ordinary files |

The distinction between the first two rows is the one that gets broken. Both are
"templates" in the directory listing; they are opposites in lifecycle. An
artifact skeleton is read in place, every time an artifact is written, and never
lands in the project. A scaffold file lands in the project once, and from then
on the project owns it.

The second and third rows are the same files read for opposite purposes, and the
difference is what keeps the copy safe. At adoption the template is the source
and produces the file. At a re-run it is not a source at all: the plugin's half
of each scaffold file sits between `<!-- sdd:scaffold vN.N.N -->` markers, and
the re-run compares the two stamps, never the two texts. Where the project is
behind, it offers what `CHANGES.md` records between the two versions, one entry
at a time, to be carried into the project's own wording; where the stamps match
it offers nothing. Everything outside the fence is the project's — its queue,
its phases, its rules — and is not read, not compared, and not written. Nothing
is replaced without an answer (ADR 0009, ADR 0011).

## What must never cross

**`${CLAUDE_PLUGIN_ROOT}` never appears in a file written into the project.** It
is substituted into *skill text* at invocation; a project file containing it is
a literal string the model cannot resolve. This is why the rules section cannot
name the ADR skeleton's path and instead names the skill that can.

**A project path never appears in a skill's instructions.** Skills read
locations from `.sdd.yml`. The illustrative config block in `/sdd:setup` is
not an instruction and is the one exemption.

## The order that matters

1. `/sdd:setup` writes `.sdd.yml` **first** — every later skill reads it, and
   a skill that runs before it has no paths.
2. Scaffold files are written only where nothing exists. Adoption is additive by
   invariant 3, so an existing file always wins over the scaffold.
3. The rules section is appended **last**, because it renders paths from the
   config written in step 1.
4. `/sdd:canon` runs after adoption, never before: it fills the body of an
   `invariants.md` that adoption placed. It does not create the file.

Breaking this order does not fail loudly. It produces a project configured
against paths that do not exist, which surfaces one session later as a skill
writing to the wrong place.

## Versioning

`plugins/sdd/.claude-plugin/plugin.json` carries an explicit `version`. Without
a bump, installed copies do not update — a fix to a skill or a skeleton reaches
nobody. Bump it in the same commit as the change that earns it.
