# Changelog

Notable changes to the `sdd` plugin. Versions follow the `version` field in
`plugins/sdd/.claude-plugin/plugin.json` — Claude Code only updates an installed
copy when that number rises.

## 0.2.0

A correction to the scaffold can now reach a project that already adopted.

- Each scaffold file carries a `<!-- sdd:scaffold -->` fence around the region
  the plugin authored. A re-run of `/sdd:setup` renders the template, compares
  only that region, and offers the difference. The queue, the phases and the
  rules below the fence are never read, diffed or written (ADR 0009).
- A project adopted before the fence existed is asked once where the boundary
  goes, never guessed at — the first adopting project had already hand-edited
  the file a guess would have had to match.
- `./scripts/check.sh` rejects a scaffold file whose fence is missing,
  unclosed, inverted, duplicated or empty, and now scans `docs/architecture/`
  for retired skill names — it was carrying five.

## 0.1.3

- The tier table told every adopting project to run `brainstorming`, a skill
  renamed to `/sdd:design` before the first release. Five more pre-rename names
  survived in the scaffold and the README — including two in files copied into
  a repository, where a correction here would never have reached them.
- `./scripts/check.sh` resolves every `/sdd:` reference in shipped text against
  the skills directory and rejects a retired name. Recorded as invariant 11.

## 0.1.2

- `/sdd:canon` holds a claim that something is *missing* to the same standard as
  a claim that a rule holds. An audit recorded a gap that did not exist — it
  read an absent import as an absent call, though both sides sat in one package
  — and the false gap became a canon entry, then a ticket, then someone's
  afternoon. A hole must now be located: the file and line where the thing would
  be, shown not to have it.
- `/sdd:canon` audit runs each entry's *Detect* where it is runnable and reports
  what it printed.

## 0.1.1

Everything here came out of the first adoption into a repository that already
ran a different method.

- `/sdd:setup` prints the proposed `.sdd.yml` before asking to approve it.
  "Ask once, as a single message" was read as "ask through the question tool",
  which hid the file the question was about — the operator was approving a
  config they had not seen.
- `/sdd:setup` covers replacing an existing process section, which the operator
  can choose and the skill did not describe: what survives a change of
  methodology, showing the deletion before making it, the superseding ADR, and
  the dangling references the previous method leaves in the project's docs.
- `/sdd:setup` names what taking the config without the rules section costs —
  the skills run, but the execution rules are not in context while code is
  written.
- `/sdd:setup` reports the predecessor's now-unreferenced files, and picks its
  closing next-step from whether the canon already holds rules.
- The plugin manifest's `$schema` points at `claude-code-plugin-manifest.json`,
  which exists. The previous URL 404ed, so no editor was validating the file.
- `/sdd:canon` audit handles a list inherited from another method: the rules are
  sound but carry no *Detect* or *On violation*, and the audit proposes those
  rather than rewriting the rule.
- `/sdd:canon` audit reports **Drifted** as its own list. It was a note under
  Held, and a rule whose entry lies is not in the same state as one described
  correctly — it is the finding an audit exists for.
- `/sdd:canon` audit routes what it finds that is not an invariant — dead
  packages, leaks, a declared dependency with no code — to `/sdd:tasks` instead
  of leaving it in the transcript.

## 0.1.0

First public release. The method had been running inside a working codebase for
months; this is the extraction of it into something installable elsewhere.

### The method

- **Tier table** sizing process to the task: tier 0 codes, tier 1 gets a design
  paragraph, tier 2 gets the full cycle. Takes precedence over any skill's own
  "applies to every project" gate.
- **Execution rules** appended to a project's `CLAUDE.md` (or `AGENTS.md`): an
  approved plan authorizes every step in it, `[gate]` marks the operator's
  checks, a test must be watched failing, evidence precedes any completion
  claim, a merge candidate gets an independent review, and the ticket moves to
  Done as the last commit on the branch.
- **Three artifact lifetimes** kept apart: the canon is always current, decision
  records are append-only, per-feature design and plan are frozen at merge.

### Skills

- `/sdd:setup` — surveys an existing repository, writes `.sdd.yml`, creates only
  what is missing, appends the rules section behind a marker it recognizes on a
  re-run. Never overwrites a file it did not write.
- `/sdd:canon` — bootstrap, amend or audit the architectural invariants. Each
  entry carries how a violation is detected and what happens when one is found.
- `/sdd:subsystem` — write and keep the architecture document for one part of a
  system.
- `/sdd:design` — an ambiguous ticket into a design, then a plan. Names the ADR
  skeleton's path, since a project file cannot resolve one itself.
- `/sdd:tasks` — the ticket format and id allocation for the queue.
- `/sdd:debug` — root cause before fix; three failed fixes means the
  architecture.

### Skeletons

`_DESIGN.md`, `_PLAN.md` and `_ADR.md` are read from the installed plugin rather
than copied into a project, so a fix to a skeleton reaches every consumer on
update.

### Config

`.sdd.yml` at the project root is the only thing crossing the boundary between
plugin and project: `canon`, `tasks`, `roadmap`, `features`, `adr`, `verify`,
`ticket`, `rules`. Values may not contain `#`; directory paths end in `/`.
