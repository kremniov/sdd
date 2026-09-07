# SDD — spec-driven development, sized to the task

A Claude Code plugin. It brings a way of working that scales its own cost to the
ambiguity of the job, rather than charging full price for a one-line change.

## Why this exists

Prescriptive agent workflows tend to share one structural flaw: their cost is
roughly constant while their payoff scales with how open the task is. A one-file
fix pays the same eight round-trips as a subsystem rewrite. They are also
calibrated for a model whose default is to cut corners, so a large share of
their text is anti-rationalization — tables of excuses, red-flag blocks, gates
that fire on "every project regardless of perceived simplicity" — which spends
attention on compliance rather than on the problem.

Neither is a criticism of the discipline itself; see Prior art below for what
this is built on. It is an argument that the discipline needs a dial.

This one starts from that premise. The design cycle is expensive and
worth it exactly when the task is genuinely ambiguous; the user's attention
is the scarce resource; and the rules that actually earn their place are few
enough to state without a catalogue of ways to disobey them.

It was extracted from a working codebase where it had been running for months,
after a paired A/B comparison of the full cycle against no cycle at all on
matched tickets.

## What you get

**Four gates** where you read, decide and approve, and the agent stops:

| Gate | What you approve | What the agent does next |
|---|---|---|
| G1 | The tier, and the decisions of the brainstorm | Designs, or starts the code |
| G2 | The design | Commits it, writes the plan |
| G3 | The plan | Commits it, runs every step |
| G4 | The pull request | You merge |

**A tier table** that decides how many gates a task passes:

| Tier | Scope | Gates |
|---|---|---|
| 0 | Nothing left to decide, no new seam | G1, G4 |
| 1 | One decision to settle, no invariant touched | G1, G2 as a paragraph, G4 |
| 2 | New seam, an invariant moves, several decisions agreed together | all four, with `design.md` and `plan.md` |

**Execution rules** that make the process finish. An approved plan authorizes
every step in it, so execution runs to the end and pauses only at a step marked
`[gate]`. A plan sequences work rather than containing it. A test is only known
to test something once it has failed. Evidence before any completion claim. The
ticket moves to Done *after* the review, as the last commit — because it records
that the work shipped.

**Eight skills**, named after what they work on:

| Skill | For |
|---|---|
| `/sdd:work` | Run a task from pickup to a pull request. Invoked first; carries the gates, the tiers, the blockers and the handing-over rules. |
| `/sdd:setup` | Install the method into a repository. Run once. |
| `/sdd:canon` | Establish, amend or audit the architectural canon. |
| `/sdd:subsystem` | Write and keep the architecture doc for one part of the system. |
| `/sdd:design` | Turn an ambiguous ticket into an agreed design. Tier 2. |
| `/sdd:plan` | Sequence an agreed design into ordered, checkable steps. Tier 2. |
| `/sdd:tasks` | The ticket format for the queue. |
| `/sdd:debug` | Root cause before fix; three failed fixes means the architecture. |

**About 270 words in your `CLAUDE.md`** — what must hold in a session where
nobody invoked a skill. The method itself lives in `/sdd:work`, so the rules
that are needed at one moment of one task stop competing for context in every
other session.

**Three artifact skeletons** — `_DESIGN.md`, `_PLAN.md`, `_ADR.md` — read from
the plugin, so a fix to a skeleton reaches every project that installed it.

## Install

```
/plugin marketplace add kremniov/sdd
/plugin install sdd@kremniov
```

Then, in the repository you want to adopt it:

```
/sdd:setup
```

It surveys what your project already has, proposes a `.sdd.yml` mapping, creates
only what is missing, and appends the rules section to your `CLAUDE.md` (or
`AGENTS.md` — whichever you use). It never overwrites or reformats a file it did
not write: where it would change something, it shows you and asks. Re-running is
safe — the section it writes is fenced in a marker it recognizes as its own.

Then populate the canon:

```
/sdd:canon
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
notes:    docs/notes/           # working notes, kept out of git
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

`./scripts/check.sh` validates the manifests and the skill frontmatter, resolves
the marketplace's plugin source to a real plugin manifest, checks that every
bundled path a skill names exists *and* that every shipped skeleton is named by
some skill, verifies this repo's own `CLAUDE.md` still matches the scaffold it
ships, and matches skills and templates against stack vocabulary that would
break portability.

It also measures the register of every shipped file. The register is ASD-STE100,
simplified technical English: one fact or one rule per sentence, active voice,
present tense. The budgets that detect drift from it are at most 2.5 negations
per 100 words, 1200 words for a `SKILL.md`, 400 for the rules section, and no
heading past H3. The corpus this replaced measured 4.0.

## Prior art

This method owes its shape to [Superpowers](https://github.com/obra/superpowers)
by Jesse Vincent (MIT) — a genuinely good corpus, and the one we ran against for
months before writing anything of our own. Several of its ideas are load-bearing
here: that a coding agent benefits from an explicit, named procedure rather than
improvised discipline; that debugging deserves a process of its own; and the
rule that three failed fixes means the architecture is the problem, not the
fourth fix. That last one is theirs, and it has earned its place more than once.

What changed is calibration, not disagreement. Superpowers is built for an agent
whose default is to cut corners, so its dominant register is
anti-rationalization — tables of excuses, red-flag blocks, gates that fire on
every project regardless of size. Running it on a real codebase, we measured the
cost: three small tickets, each done twice — once with the full cycle, once
without — in separate worktrees and separate sessions. The full cycle took 18
round-trips of the user's attention against 3, and about 1000 lines of
process artifact per ticket, with no difference in the result that would repay
it. A blind reviewer comparing the diffs still preferred the planned arm every
time, for a different reason each time.

That is a small sample on small work, and it says nothing about the tier where
the cycle plainly earns its keep — no ticket in it moved an invariant or several
modules at once. Which is the finding: the cost is near-constant while the
payoff scales with ambiguity, so the discipline needs a dial rather than a
verdict. That dial is the tier table, and everything here follows from it.

So: thank you, and full credit. The text in this plugin is written from scratch
— no file here is a copy or a derivative of a Superpowers file — but the
thinking started there, and pretending otherwise would be poor manners.

## Who made this

Built by [Andrey Kremnev](https://github.com/kremniov). The method was developed
and run for months on a production codebase before any of it was extracted here — every rule in it survived contact with a real codebase, and the
ones that did not are the reason the tier table exists.

Issues and pull requests welcome. If you adopt it and something does not fit
your project, that is worth an issue: the seam between the plugin and a
repository is the part most likely to be wrong for a codebase I have never seen.

## License

MIT. Independent work; not affiliated with or endorsed by the Superpowers
project.
