---
name: setup
description: Use to install this spec-driven method into a repository — survey the existing docs layout, write .sdd.yml, create the missing scaffold, and add the method's rules to CLAUDE.md or AGENTS.md. Run once per project; safe to re-run.
---

# Setting Up SDD

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

Print the proposed `.sdd.yml` as an ordinary message first — the whole file,
every line, with your inference for each and a marker for what you could not
find. Only then ask whether it is right.

The operator must be able to read the file at the moment they approve it. A
question that says "the config above" is worthless when nothing was above it,
and asking through a question tool hides whatever preceded the prompt: put the
rendered YAML in the option preview so it sits inside the question itself. Ask
once, about the whole file — not one question per key.

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

## 4. Create what is missing, and offer what has moved

For each path in the config, create it from the scaffold at
`${CLAUDE_PLUGIN_ROOT}/templates/project/` **only if nothing is there**:

| Config key | Scaffold source | Notes |
|---|---|---|
| `canon` + `invariants.md` | `invariants.md` | Header and instructions only — the body comes from `/sdd:canon`. |
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
leave a placeholder in a written file. Keep the marker lines exactly as the
template carries them, version and all — `<!-- sdd:scaffold v0.3.0 -->` — they
are what a later run compares against, and a file written without them cannot be
updated. This is the rule for a file *this run creates*, whose content is the
current template. A marker placed around text that was already there is stamped
by the missing-fence rule below instead.

An empty directory does not survive git. Where you create one, add a
`.gitkeep`.

**When the file is already there.** Each of these files is two things: guidance
this plugin wrote, and a body the project wrote — its queue, its phases, its
rules. The plugin's half is fenced, which is what makes an update possible
without touching the rest, and the opening marker carries the version whose
guidance is in there.

**Compare the stamps, never the text.** Read the version on the project's
opener and the version on the template's:

- **Equal** — the region is current. Say nothing about that file, whatever its
  wording. A project that rewrote the guidance in its own terms, with its own
  ticket ids and cross-references, is not behind, and a difference in text is
  not by itself anything to report.
- **The project is behind** — read
  `${CLAUDE_PLUGIN_ROOT}/templates/project/CHANGES.md` and take the entries for
  that file above the project's version and up to the template's — the project's
  own version is excluded, the template's included, because the project already
  holds what its stamp names. Put each one to the operator on its own, in its
  own terms; on a yes, edit their region to carry what the entry describes,
  keeping their wording, their ids, their references. An entry whose substance
  their text already states needs no edit and no question — say it was already
  satisfied. Then set the stamp to the highest version whose entries were *all*
  carried or already true, which is the template's when nothing was declined.
  Stopping at the last complete version keeps the re-offer to what was actually
  refused; leaving the stamp at the bottom would re-offer accepted entries too,
  and they would then be filtered by an agent's judgement about what the text
  already says rather than by a recorded fact.
- **The project is ahead** — an older plugin is installed over a newer
  adoption. Report it and leave the file alone. Downgrading someone's guidance
  is not something to do quietly.
- **No version on the fence** — the project adopted while the markers were bare.
  The lower bound is `v0.2.0`, the version that introduced them; that is a fact,
  not a guess, so proceed from it without asking.
- **No fence at all** — the project adopted before the markers existed. Do not
  derive the boundary by matching text against the template: a header edited by
  hand will not match, and that is precisely where a wrong guess costs most.
  Show the region you would fence, ask once, and place the markers on a yes —
  **stamped `v0.2.0`, never the template's version.** What you fenced is text
  written before any of this existed; stamping it with the current version
  declares it up to date and silences every change since, permanently. The
  baseline puts the file in the *behind* branch above, where the entries it
  never received are offered.
- **Fence malformed** — opened and not closed, closed before opened, more than
  one pair, or a version that is not `N.N.N`. Report the file and the line;
  change nothing. A broken marker in someone's `tasks.md` must not cost them
  their queue.

Never widen the region, and never replace one wholesale. What a re-run offers is
a described change, applied to what is there — the full text of the current
template is the answer to a question nobody asked.

## 5. Add the rules to the rules file

The rules must live in the project's rules file rather than only in this skill: they have to
be in context at execution time, and a skill is loaded only when something
triggers it.

The target file is the one recorded as `rules:` in `.sdd.yml` — `CLAUDE.md` by
default, `AGENTS.md` where the project uses that. Set that key in step 3 from
what step 1 found, so a later run does not have to re-derive it.

Read `${CLAUDE_PLUGIN_ROOT}/templates/project/CLAUDE.section.md` and substitute
the placeholders. The text is wrapped in `<!-- sdd:method-section vN.N.N -->`
markers — keep them, version included; they are how a re-run recognizes its own
work and knows which version's rules are in force. Then, in order:

- **The file already contains a `sdd:method-section` marker:** a previous run
  wrote it. Do not append, and do not diff it against the rendered text. Compare
  the stamps and carry the described changes, exactly as in step 4 — this
  section is the one an adopting project is most likely to have adapted, and it
  is the one where an overwrite costs the most.
- **No such file:** create it with this section, preceded by a one-line title
  naming the project.
- **The file exists, no process section:** append the section at the end. Touch
  nothing above it.
- **The file exists and already describes a process** — under any heading
  (`How we work`, `Conventions`, `Workflow`, `Development`): do not merge them
  yourself. Write the rendered section to `<file>.sdd-section` beside it, show
  the operator the specific conflicts with what is already written, and let them
  decide. A silently merged process file is worse than two visible ones.

**When the operator answers that instead: replace what is there.** That
decision is theirs and it overrides the branch above, but it is still a deletion
from a file you did not write, so it is bounded. Replace the process section
only. A rules file that describes a method also carries things that are not the
method — this project's own conventions, its paths, a rule it earned once and
wrote down — and those survive any change of methodology; carry them across and
say which ones you kept. Show what you are removing, in full, before removing
it. And a method that was itself a recorded decision does not just disappear:
the superseding ADR is owed in this same change, naming the record it retires.

A replaced method leaves references behind. Its skill paths and command names
are cited from the project's own docs, and those citations are now dangling —
find them, propose each fix, and let the operator see the list. Its files stay
where they are: unreferenced is not the same as unwanted, and deleting someone's
previous method is not a step this skill takes.

Leaving the section out is a legitimate choice and often the right first one:
the config and the scaffold alone let someone try the skills against their
existing process. Name what it costs when you offer it. The skills still run,
but the rules that make an approved plan run to its end, that put evidence
before a completion claim, and that send a merge candidate to an independent
review are only in effect while they are in context — and a skill loads on a
trigger, long after the code is being written. Until the section lands, what is
installed is the artifacts, not the method.

## 6. Report

State plainly:

- what was created, by path;
- what was left alone because it already existed;
- what the scaffold has changed since this project adopted, by version: which
  described changes were carried, which were declined and will be offered again,
  which were already satisfied by the project's own wording, and which files
  were left alone because they have no fence. Nothing to carry is worth one
  line, not silence — the operator asked, and "already current" is the answer;
- anything you could not infer and guessed at;
- whether the rules section landed in the rules file — and if it did not, that
  the method is not yet in force, and what remains to be decided;
- what a previous method left behind that nothing references any more, by path,
  so the operator can decide about it while it is still visible;
- the next step, which depends on what the canon already holds. An empty
  `invariants.md` means `/sdd:canon` to establish one. A populated one means
  `/sdd:canon` in audit mode — this project has rules already, and the question
  is whether they are still true, not what they should be.

## Re-running

Safe. A second run re-surveys, reports what is now present, and creates only
what is still missing. It never rewrites a file it finds — including one an
earlier run of itself wrote, which by then may have been edited by hand. The
one thing it changes in an existing file is a described change carried inside a
fence, on a yes, into the wording that is already there.
