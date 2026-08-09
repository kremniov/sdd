# SDD — spec-driven development, sized to the task

A Claude Code plugin. It brings a way of working that scales its own cost to the
ambiguity of the job, rather than charging full price for a one-line change.

## Why this exists

Prescriptive agent workflows tend to share two flaws. They are calibrated for a
model whose default is to cut corners, so their dominant genre is
anti-rationalization — tables of excuses, red-flag blocks, hard gates that fire
on "every project regardless of perceived simplicity". And their cost is roughly
constant while their payoff scales with how open the task is, so a one-file fix
pays the same eight round-trips as a subsystem rewrite.

This one starts from the opposite premise. The design cycle is expensive and
worth it exactly when the task is genuinely ambiguous; the operator's attention
is the scarce resource; and the rules that actually earn their place are few
enough to state without a catalogue of ways to disobey them.

It was extracted from a working codebase where it had been running for months,
after a paired A/B comparison of the full cycle against no cycle at all on
matched tickets.

## What you get

**A tier table** that decides how much process a task gets:

| Tier | Scope | Process |
|---|---|---|
| 0 | One file, no new seam | Code + tests + commit. |
| 1 | New file or module, no invariant touched | A design paragraph in the conversation. |
| 2 | New seam, an invariant moves, several modules together | `brainstorming` → `design.md` → `plan.md` → execution. |

**Execution rules** that make the process finish. An approved plan authorizes
every step in it, so execution runs to the end and pauses only at a step marked
`[gate]`. A plan sequences work rather than containing it. A test is only known
to test something once it has failed. Evidence before any completion claim. The
ticket moves to Done *after* the review, as the last commit — because it records
that the work shipped.

**Five skills:**

| Skill | For |
|---|---|
| `adopting-sdd` | Install the method into a repository. Run once. |
| `deriving-canon` | Read the codebase, write down the invariants it already holds. |
| `brainstorming` | Turn an ambiguous ticket into an agreed design. Tier 2. |
| `managing-tasks` | The ticket format for the queue. |
| `systematic-debugging` | Root cause before fix; three failed fixes means the architecture. |

**Three artifact skeletons** — `_DESIGN.md`, `_PLAN.md`, `_ADR.md` — read from
the plugin, so a fix to a skeleton reaches every project that installed it.

## Install

```
/plugin marketplace add kremnev/sdd
/plugin install sdd@kremnev-sdd
```

Then, in the repository you want to adopt it:

```
/sdd:adopting-sdd
```

It surveys what your project already has, proposes a `.sdd.yml` mapping, creates
only what is missing, and appends the rules section to your `CLAUDE.md` (or
`AGENTS.md` — whichever you use). It never overwrites or reformats a file it did
not write: where it would change something, it shows you and asks. Re-running is
safe — the section it writes is fenced in a marker it recognizes as its own.

Then populate the canon:

```
/sdd:deriving-canon
```

This reads your codebase and proposes the architectural rules it already
follows, for you to confirm. On an established codebase this is the step that
pays for itself — it turns rules living in one person's head into something a
reviewer and an agent can both cite.

## The seam

One file at your repo root. Every skill reads it; nothing else crosses the
boundary between the plugin and your project.

```yaml
# .sdd.yml
canon:    docs/architecture/    # always-current architecture docs
tasks:    docs/tasks.md         # the "what's next" queue
roadmap:  docs/roadmap.md       # direction: sequence, not dates
features: docs/features/        # per-feature design.md + plan.md
adr:      docs/adr/             # one decision per file
verify:   make lint && make test
ticket:   T                     # ticket id prefix
rules:    CLAUDE.md             # the file the method's rules live in
```

Paths are yours. A project with `documentation/decisions/` keeps that path —
adoption reads your layout rather than imposing one.

## Three lifetimes

The structure exists so an agent can load *how the system is now* cheaply,
instead of re-deriving it from code every session. Keeping the three apart is
what makes that work:

- **Always current** — the canon. Updated in the same PR that changes the seam
  it describes.
- **Append-only** — decision records. Why we chose X, dated, never edited.
- **Frozen at merge** — per-feature design and plan. How the feature was
  reasoned into being. Durable consequences get folded into the canon; the
  artifact stays as the record of why.

The canon tells you the current shape. A `design.md` tells you why it took that
shape. An ADR tells you what was rejected and at what cost.

## What this is not

Not a task tracker — the queue is flat markdown on purpose. Not a CI gate —
nothing here fails your build; `scripts/check.sh` checks this plugin, not your
project. Not stack-specific — no language, build tool or
framework is assumed. And not a substitute for your own `CLAUDE.md`: the plugin
contributes a section, you keep authorship of the file.

## Checks

`./scripts/check.sh` validates the manifests and the skill frontmatter, checks
that every bundled path a skill names exists *and* that every shipped skeleton is
named by some skill, verifies this repo's own `CLAUDE.md` still matches the
scaffold it ships, and greps for origin-project vocabulary that would break
portability.

## License

MIT.
