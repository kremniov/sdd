# Changelog

Notable changes to the `sdd` plugin. Versions follow the `version` field in
`plugins/sdd/.claude-plugin/plugin.json` — Claude Code only updates an installed
copy when that number rises.

## 1.1.5

- Update an existing ticket when execution starts, blocks or resumes. Keep the
  ticket in progress while independent authorized work can continue; working
  notes retain details without replacing queue status.

## 1.1.4

- Check each committed change and completed step with appropriate checks; run
  the full required suite after all changes, repeating it when relevant changes
  or unresolved concerns require it rather than for every intermediate commit.

## 1.1.3

- Resolve known integration blockers before the final ticket commit. Preserve
  scoped merge permission after failure and allow verified repair commits after
  Done without rewriting published history just to restore commit order.

## 1.1.2

- Verify, commit, push and report review fixes on the same branch. Keep repeat
  review user-started and honor conditional merge permission within its scope.

## 1.1.1

- Check the branch before edits and keep direct commits and pushes off integration
  branches, including standalone document, queue and setup operations.
- Hand over standalone changes through a PR; operations within approved work
  share its step and PR.

## 1.1.0

- Rewrite the skills and scaffold from the agreed method in `docs/method.md`.
- Require a concrete tier-0 proposal and combine tier-1 scope and design approval.
- Commit each verified plan step before the next; allow several commits per step.
- Execute merge on the user's explicit permission after the final ticket commit.
- Preserve ticket context and approved design inputs. Remove minimum content quotas.
- Treat widespread invariant violations and failed-fix counts as evidence to
  investigate, not proof that architecture must change.
- Make negation frequency advisory, count examples in size budgets and report
  reference volume. Add checker tests and versioned behavioral scenarios.
- Preserve project additions in scaffold updates and keep task status in ignored notes.

## 1.0.0

The method moves out of your `CLAUDE.md` and into a skill, and every rule is
rewritten in a plain register.

- **The resident rules drop from 1693 words to 268.** What stays is what must
  hold in a session where nobody invoked a skill: the user integrates the
  branch, evidence precedes a completion claim, a test is watched failing first,
  the comments rules, and a line naming the skill to invoke (ADR 0018).
- **`/sdd:work` carries the method.** The gate table, the tier table, the closed
  list of blockers, the review rules and the handing-over rules. Invoke it when
  a task starts.
- **Four gates are the frame; the tier says how many a task passes** (ADR 0017).
  Tier 0 passes G1 and G4, so a task with nothing left to decide still gets your
  word before the code.
- **G4 ends with "push the branch, open the pull request, and stop".** The rule
  that was missing: agents were bringing branches to merge-ready and leaving
  them unpushed, so there was nothing to review.
- **A design reads the roadmap.** Acceptance criteria are a check, not a
  specification, and the product logic lives in the roadmap.
- **`/sdd:design` splits into `/sdd:design` and `/sdd:plan`** (ADR 0019), one
  artifact each, with gate G2 between them.
- **`/sdd:canon` runs the falsifiability filter before the amend questions**, and
  states that four times no is the expected answer. It gains `lessons.md`, the
  one canon file that carries dates.
- **The party who directs the work is the user, not the operator** (ADR 0016).
  Accepted decision records and frozen feature designs keep the old word.
- **The register is measured** (ADR 0021, invariant 12). `check_register.py`
  fails the build on a file past 2.5 negations per 100 words, past its word
  budget, or nested past H3. The corpus averaged 4.0 before this release.
- **`.sdd.yml` gains `notes:`** — where a brainstorm writes its decisions, out
  of git.
- **Adoption can retire the old rules section** (ADR 0020). A project on the
  `sdd:method-section` fence is shown the whole region, told what replaces it,
  and asked once. A decline changes nothing and is offered again.

## 0.5.1

- The handing-over rule names `/sdd:tasks` as what shapes the Done line. It
  stated when the ticket moves and what ref it carries, but not where the
  collapse format is written, so an agent closing a ticket reconstructed it by
  reading the queue's existing entries — the one rule in the section requiring
  an artifact edit without a pointer to the skill that owns it.

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
