# Portable SDD framework — design

**Ticket:** T-1 · **Plan:** [plan.md](plan.md)

## Problem

The spec-driven flow this repo packages was developed inside one codebase and
is inseparable from it. Its rules live in that project's `CLAUDE.md`, its skills
name that project's invariant numbers, and its templates sit at a path only that
repo has. Adopting it elsewhere today means copying files by hand and editing
every cross-reference — and the parts most worth copying (the tier table, the
execution rules, the artifact lifetimes) are exactly the parts buried in prose
about that codebase's own subsystems.

Meanwhile the available alternative — a large prescriptive skill corpus — is
calibrated for an agent whose default is to cut corners: its dominant genre is
anti-rationalization tables, and its gates do not scale down. A one-file change
pays the same process cost as a subsystem rewrite.

## Goal / Non-goals

**Goal.** A Claude Code plugin that installs into any repository and brings four
things: a tier table that sizes process to task, the execution rules that make an
approved plan run to its end, the artifact skeletons, and skills to create the
project canon those rules depend on — including deriving an invariants list from
a codebase that already exists.

**Non-goals.**

- Not a replacement for a project's own `CLAUDE.md`. The plugin contributes a
  section; the project keeps authorship.
- Not language- or stack-specific. No build tool, codegen or framework assumed.
- Not a task tracker. `tasks.md` is a flat markdown queue, deliberately.
- The A/B measurement that produced these rules stays in the origin repo. The
  rules ship; the private engineering log does not.
- No CI enforcement in v1. The invariant checker in the origin repo is bash over
  one language's import paths; generalizing it is its own ticket.

## Decisions

- **Distribution is a Claude Code plugin, not a copyable starter.** → ADR.
  Rejected: a `install.sh` that copies files, which makes updates manual and
  forks every consumer.
- **The repo is a marketplace containing one plugin**, layout
  `.claude-plugin/marketplace.json` + `plugins/<name>/`. Forced: a single repo
  cannot be both a plugin and its own marketplace. Cost: installation is two
  commands.
- **Templates are read from `${CLAUDE_PLUGIN_ROOT}`, not copied into the
  project.** → ADR. The variable resolves before skill text reaches the model, so
  a skill can name its own bundled file. Consequence: a template fix reaches
  every consumer on plugin update, and no project carries a stale copy. Rejected:
  copying templates at adopt time, which was the origin repo's shape and is why a
  template edit there could not reach anyone else.
- **The project canon is required, and the plugin creates it.** Three artifacts
  with three different lifetimes: `architecture/` (always current), `tasks.md`
  (evolving queue), `roadmap.md` (long-lived direction). A rule that says "link
  the canon rather than restating it" is inert without somewhere to link.
- **Deriving invariants is a separate skill from adopting.** → ADR. Adoption lays
  a scaffold; derivation reads an existing codebase and names the rules it
  already follows. These have different inputs, different failure modes, and
  different reasons to be re-run — derivation is repeatable on a codebase that
  drifted.
- **A config file records project paths**, so the skills carry no hardcoded
  `docs/...` strings. Rejected: convention-only, which breaks on any repo that
  already has a `docs/` layout of its own.
- **Rules that must hold at execution time go into the project's `CLAUDE.md`,
  not only into a template.** Forced by a defect measured in the origin repo: the
  HTML comment block at the top of a template does not survive into the generated
  artifact, so a rule written only there is never read when it matters.
- **Skills carry no anti-rationalization tables** except where a real failure
  mode was observed (the "three failed fixes" rule). The corpus states what to
  do, and trusts the model to do it.

## Architecture

```
sdd/                                  (this repo — the marketplace)
├── .claude-plugin/marketplace.json
├── plugins/sdd/
│   ├── .claude-plugin/plugin.json
│   ├── skills/
│   │   ├── adopting-sdd/SKILL.md       lay the scaffold, write config + CLAUDE.md section
│   │   ├── deriving-canon/SKILL.md     read the codebase → architecture/ + invariants
│   │   ├── brainstorming/SKILL.md      ticket → design.md (tier 2)
│   │   ├── managing-tasks/SKILL.md     the tasks.md ticket format
│   │   └── systematic-debugging/SKILL.md
│   ├── templates/
│   │   ├── _DESIGN.md  _PLAN.md  _ADR.md
│   │   └── project/                    scaffold written into the adopting repo
│   │       ├── CLAUDE.section.md       the rules, verbatim, for the project's CLAUDE.md
│   │       ├── docs-README.md          the three-lifetimes table
│   │       ├── invariants.md           header + how to write one; body is derived
│   │       ├── tasks.md  roadmap.md
│   └── README.md
├── docs/                             (this repo eats its own food)
└── README.md
```

**The seam between plugin and project** is one config file at the project root,
written by `adopting-sdd` and read by every other skill:

```yaml
# .sdd.yml
canon:    docs/architecture/     # always-current architecture docs
tasks:    docs/tasks.md          # the queue
roadmap:  docs/roadmap.md        # direction
features: docs/features/         # per-feature design.md + plan.md
adr:      docs/adr/              # one decision per file
verify:   make lint && make test # the command a step's DoD runs
ticket:   T                      # ticket id prefix
```

Nothing else crosses the boundary. A skill needing the task queue reads
`tasks:` from this file; it never assumes `docs/tasks.md`.

**Flow on adoption:**

1. `/sdd:adopting-sdd` — detect existing docs layout, ask what is missing, write
   `.sdd.yml`, create the scaffold for artifacts that do not exist, append the
   rules section to `CLAUDE.md` (creating it if absent).
2. `/sdd:deriving-canon` — read the codebase, propose the invariants it already
   holds, write `architecture/invariants.md` + `layout.md` after the operator
   confirms each. Re-runnable.
3. Normal work: a ticket in `tasks.md` → the tier table decides the process →
   tier 2 goes through `brainstorming` → `design.md` → `plan.md` → execution.

**The rules section** contributed to `CLAUDE.md` carries, in this order: the
tier table; plan-authorizes-every-step and `[gate]`; test-first as an ordering
rule; evidence before any completion claim; independent review of a merge
candidate; ticket-to-Done as the last commit after review; docs discipline and
the ADR trigger; the comment rule.

## Invariants & docs

This repo's own canon is created by the same skills it ships — `deriving-canon`
runs against it, and the result is the first real test of that skill.

The invariants that survive extraction from the origin repo are the ones about
*form* rather than *stack*: a canonical list that other documents link instead of
restating; delete rather than deprecate; an architectural budget that demands a
concrete beneficiary before a new layer. The rest — that codebase's own boundaries and
codegen conventions — are examples in the docs, not shipped rules.

## Error handling

- **`.sdd.yml` missing** when a skill needs it: the skill says so and points at
  `adopting-sdd` rather than guessing paths.
- **An artifact the config names does not exist**: create it from the scaffold
  and say so; never fail silently into a different path.
- **Adoption into a repo that already has these docs**: detect, and default to
  leaving them alone. Adoption is additive; it never overwrites a file it did
  not write. Anything it would have changed is reported for the operator.
- **`deriving-canon` on a codebase with no discernible rules**: say that plainly
  and write nothing. A speculative invariants list is worse than none — it gets
  linked and cited as if it were observed.

## Testing

No runtime, so no unit tests. What proves it works:

1. **Adoption into a repo with nothing** — a bare git repo. Scaffold appears,
   `.sdd.yml` is valid, `CLAUDE.md` created.
2. **Adoption into a repo that already has docs** — a clone of the origin
   repo. Nothing is overwritten; the config points at what is already
   there.
3. **Adoption into a repo in another language** — to catch any assumption from
   the origin's stack that leaked through.
4. **`deriving-canon` against the origin repo**, whose real invariants are known:
   does it recover the layering rules from the code alone?
5. **A full tier-2 loop run inside this repo**, using the plugin's own skills.

Every check is a manual operator run, and each is a `[gate]` step in the plan.
