# SDD v2 — design

**Ticket:** none — dogfooding is paused for this branch · **Plan:** [plan.md](plan.md)

Style: ASD-STE100. One fact or one rule per sentence. This document is the first
sample of the register the branch installs everywhere else.

## Problem

The method works. Its text does not.

**The rules are resident and too large.** `CLAUDE.section.md` is 1693 words. One
field fix grew it from 1718 to 2115 words. The harness reports a capacity of
about 150–200 instructions and spends about 50 of them itself. Every rule added
weakens the rules already there.

**The register is wrong.** Negation density, counting *not / never / no / only /
without / rather than*, is 4.0 per 100 words across the section. Ordinary
technical prose runs 1–1.5. One table cell reaches 17.9. Dense text is also the
style model for every `design.md` and `plan.md` the method produces, so the
defect copies itself.

**Five behaviours were observed over about 10 PRs in a separate project.**

| # | Behaviour | Cause |
|---|---|---|
| 1 | The agent leaves the branch unpushed and opens no PR | The text groups `push` and `gh pr create` with `git merge` and forbids all three |
| 2 | The agent stops after 2–3 plan steps with no question | "A decision the design does not cover" stretches to cover any small gap |
| 3 | The agent proposes invariants for trivial branches | The four Amend questions run before the falsifiability filter |
| 4 | Acceptance criteria override product and architectural logic | The design's input list omits the roadmap, so acceptance is the only concrete input |
| 5 | Tier 0 starts coding with no reply to the user | Tier 0 is the only sizing call the agent makes silently |

Behaviours 1 and 4 are missing rules. Behaviours 2, 3 and 5 are wording defects.

## Goal / Non-goals

**Goals.**

1. Move the execution rules from the resident file into a skill.
2. Keep a resident set of about 300 words.
3. Rewrite every shipped rule in ASD-STE100.
4. Make the gate table the frame of the method.
5. Add the two missing rules.
6. Measure the register mechanically, so it cannot drift back.

**Non-goals.**

- Output styles. Two sources claim a built-in `Concise` style; the claim is
  unverified and stays a ticket.
- Rewriting ADR 0001–0015. Invariant 11 exempts decision records: they quote old
  names on purpose.
- An eval corpus, prompt optimisation, or a critic subagent. All three are
  rejected in the handoff.
- Any change to what the method decides. Only where a rule lives, and how it
  reads.

## Decisions

| # | Decision | Rejected |
|---|---|---|
| 1 | The party who directs the work is the **user**. The other party is the **end user** | `operator`, which the harness never says, so every rule about irreversible actions needs an unwritten translation |
| 2 | One branch carries both jobs — the move and the rewrite | A move alone leaves the old register inside the skills, where it still models `design.md` |
| 3 | A new skill `/sdd:work` is the entry point | A prompt template in the scaffold; the user has to remember where it is |
| 4 | `/sdd:work` carries the whole frame: gates, tiers, blockers, handing over, review, ADR and docs triggers | A separate `/sdd:method` skill, which splits the frame across two loads |
| 5 | The gate table is the frame. The tier sets how many gates a task passes | Gates on tier 2 only, which leaves behaviour 5 unfixed |
| 6 | G1 approves the tier and the brainstorm decisions, at every tier | Tier 0 skipping G1, which is an exception rather than a rule |
| 7 | Brainstorm is a phase. Its decisions go to a file outside git, named by a new `notes:` key | Keeping them in the conversation, which `/compact` erases |
| 8 | `/sdd:design` splits into `/sdd:design` and `/sdd:plan` | One skill for two artifacts, the only ADR 0004 exception in the corpus |
| 9 | The agent pushes and opens the PR, then stops. The user runs the independent review against the PR and merges | Review before the PR, which is the behaviour that broke in the field |
| 10 | Every tier gets a branch and a PR, including tier 0 | A tier-dependent rule, which restores the fork that produced behaviour 5 |
| 11 | v2 ships a new fence, `sdd:rules`. `/sdd:setup` retires `sdd:method-section` on an explicit yes | One `CHANGES.md` entry per removed subsection; the machinery describes changes, not deletions of 80% of a region |
| 12 | `check.sh` measures length, heading depth and negation density over shipped text | All four budgets mechanically; rationale share and claim count need a reader |
| 13 | `/sdd:work` keeps one status record in memory | Memory holding the rules too, which creates a fifth source of truth |
| 14 | A `lessons.md` joins the canon | Lessons inside `design.md`, which freezes at merge and is not read again |
| 15 | The version is 1.0.0 | 0.6.0, which hides a breaking release |

## Architecture

### The four homes of a rule

| Home | Holds | Loaded |
|---|---|---|
| The project's rules file | About 300 words that must hold with no skill loaded | Always |
| `/sdd:work` and the other skills | Everything else | On invocation |
| The agent's memory | One status record per branch | On recall, after `/compact` |
| `scripts/check.sh` | What a script can decide | On the branch that changes the text |

A rule lives in exactly one home. The resident file names the skill; it does not
summarise it.

### The resident set

Five rules, about 300 words, under the fence `sdd:rules v1.0.0`:

1. The user integrates the branch. The agent pushes the branch, opens the PR,
   and stops.
2. Show the evidence before claiming that something works. Name what you ran.
3. Run the test and watch it fail first.
4. The comments rules.
5. Invoke `/sdd:work` when a task starts. Invoke a skill when the task is
   plainly the one it covers.

One more line states the equivalence the harness needs: the paths are in
`.sdd.yml`, and the skills read them.

Everything else leaves: the tier table, the paths table, artifact layout, plan
structure, the two review scales, and the ADR and docs triggers.

### The gates

A gate is a point where the user reads, decides and approves. The agent does not
pass a gate alone.

| Gate | What the user approves | What the agent does next |
|---|---|---|
| G1 | The tier, and the decisions of the brainstorm | Writes `design.md`, or states the design paragraph, or starts the code |
| G2 | `design.md`, or the design paragraph | Commits `design.md`, writes `plan.md` |
| G3 | `plan.md` | Commits `plan.md`, runs every task in order |
| G4 | The PR | Merges — the user does this |

| Tier | Gates | Artifacts |
|---|---|---|
| 0 | G1, G4 | none |
| 1 | G1, G2, G4 | a design paragraph in the conversation |
| 2 | G1, G2, G3, G4 | `design.md`, `plan.md` |

The tier table itself is unchanged. ADR 0012 stands: the tier follows the
decisions, not the diff.

### Blockers

`/sdd:work` carries a closed list. The agent stops when one of these is true:

1. Two readings of the request lead to materially different work.
2. The code or a dependency contradicts the design.
3. The change needs a contract that a party outside this repository must agree.
4. A step touches a system in a way that is not reversible.
5. A credential or an access right is missing.

The agent does not stop for: naming, file layout, test structure, library choice
inside the agreed stack, formatting, or a commit boundary. This list replaces "a
decision the design does not cover" and fixes behaviour 2.

### The skills

| Skill | Artifact | New in v2 |
|---|---|---|
| `work` | the session | yes — carries the frame |
| `design` | `design.md` | rewritten |
| `plan` | `plan.md` | yes — split from `design` |
| `tasks` | the queue | rewritten |
| `canon` | `invariants.md`, `layout.md`, `lessons.md` | rewritten |
| `subsystem` | a subsystem document | rewritten |
| `debug` | none | rewritten |
| `setup` | `.sdd.yml` and the scaffold | rewritten, plus the migration |

`SKILL.md` holds at most 1200 words. A skill that needs more puts the surplus in
a reference file in its own directory and names it. `/sdd:setup` uses this for
the fence machinery.

### Configuration

`.sdd.yml` gains one key.

| Key | Value | Purpose |
|---|---|---|
| `notes` | `docs/notes/` | Working notes outside git: the decisions log, prompts |

`/sdd:setup` proposes the matching `.gitignore` line and asks before writing it.
The decisions log is `<notes>/<feature>-decisions.md`.

### The scaffold

| File | Change |
|---|---|
| `CLAUDE.section.md` | Replaced. New fence name `sdd:rules`, stamped `v1.0.0` |
| `lessons.md` | New. Dated project lessons, one line each |
| `invariants.md` | Rewritten header |
| `tasks.md`, `roadmap.md`, `docs-README.md` | Rewritten guidance, stamps move to `v1.0.0` |
| `CHANGES.md` | One `v1.0.0` section per file |

### The templates

`_DESIGN.md` and `_PLAN.md` each gain a contrast pair — watery against tight —
because `tasks/SKILL.md` proves that a pair steers format better than a rule
does. Each section header states how much closes the question, not which topics
to cover. `_ADR.md` keeps its shape.

Written budgets, which no script decides:

| Artifact | Words | Headings | Rationale |
|---|---|---|---|
| `design.md` | 1300, hard stop 2000 | 12 | One sentence per decision |
| `plan.md` | one screen per step | one per step | Only in the Order section |

## Invariants & docs

| Invariant | Change | Needs an ADR |
|---|---|---|
| 2 | Gains the fence-retirement path | yes |
| 3 | Gains one bounded exception: a fence the plugin wrote, retired on an explicit yes | yes |
| 4 | Rewritten. Only a rule that must hold with no skill loaded stays resident | yes |
| 12 | New. Shipped text is measured; `check.sh` decides | yes |

ADRs written on this branch:

| # | Subject |
|---|---|
| 0016 | The user, not the operator |
| 0017 | The gate table is the frame; the tier sets the gate count |
| 0018 | Execution rules move to a skill; invariant 4 moves with them |
| 0019 | A skill with no artifact is named after what a person types; `design` splits |
| 0020 | Retiring a scaffold fence, and the bound on the exception to invariant 3 |
| 0021 | The register is measured |

ADR 0019 amends ADR 0004. ADR 0017 cites ADR 0012 and leaves it standing.

Canon documents that update in the same PR: `invariants.md`, `layout.md`,
`plugin-mechanics.md`. Repository documents: `README.md`, `CHANGELOG.md`,
`docs/roadmap.md`, `docs/tasks.md`.

The branch ends by restarting dogfooding: it removes the
`<!-- sdd:dogfooding-paused -->` marker and renders `CLAUDE.md` from the new
template.

## Error handling

| Failure | Response |
|---|---|
| A project declines the fence retirement | `/sdd:setup` leaves the old section, writes no new fence, and reports that the project runs v0.x rules. Two method sections in one file are never written |
| A project is on `v0.2.0` with a bare stamp | Unchanged. The lower bound holds, and the retirement question is asked once |
| A project has no fence at all | Unchanged. `/sdd:setup` shows the region and asks |
| The density check fails on a rule whose substance is a prohibition | The threshold is per file, not per sentence. The best existing file already meets it |
| `/compact` drops the skill text | The resident set names `/sdd:work`. The status record names the gate that is passed |
| A skill exceeds 1200 words | The check fails. The surplus moves to a reference file |

## Testing

`scripts/check.sh` gains one script, `check_register.py`, over every shipped
file — skills, reference files, templates and the scaffold.

| Measure | Threshold | Why this number |
|---|---|---|
| Negation density | 2.5 per 100 words, per file | `tasks/SKILL.md` measures 2.5 today and is the strongest file in the plugin |
| Negation density, resident section | 2.0 per 100 words | It is the text that is always loaded |
| `SKILL.md` length | 1200 words | The two longest files today are 2196 and 2242 |
| Resident section length | 400 words | The target is 300 |
| Heading depth | H3 | Deeper nesting is how the section became a sink |

The existing checks keep running. `check_skill_refs.py` gets the new skill names.
`check_config.py` gets the `notes` key.

Manual verification, in a separate clone, because it writes to a repository:

1. Adopt into an empty repository. Every scaffold file appears, stamped `v1.0.0`.
2. Adopt into a repository holding `sdd:method-section v0.5.1`. The retirement is
   offered, shown in full, and applied only on a yes.
3. Decline the retirement. Nothing changes, and the report says so.
4. Re-run against a project already at `v1.0.0`. Nothing is offered.
