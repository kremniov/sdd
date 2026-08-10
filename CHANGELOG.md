# Changelog

Notable changes to the `sdd` plugin. Versions follow the `version` field in
`plugins/sdd/.claude-plugin/plugin.json` — Claude Code only updates an installed
copy when that number rises.

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
