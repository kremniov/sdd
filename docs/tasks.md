# Tasks

The "what do I pull next" queue. Format: `/sdd:tasks`.

## TODO

#### `[T-11]` Give the rules section somewhere for growth to go

**Tags:** `[debt]` `[next]`

**Outcome:** The scaffold's method section states the same rules in fewer words, arranged so a new rule has a home other than `### Process tiers`.

**Context:** Measured at 2115 words after T-10, up from 1718 — 23% growth from one field fix. `### Process tiers` holds 1351 of those words and long ago stopped being about tiers: tiers, plan rules, the test-first rule, evidence, integration, review, subagents and when to invoke a skill all live under it, because nothing else claims them. The heaviest cluster is integration (221 w), independent review (161 w) and the two scales (135 w) — 24% of the section stating one principle about who holds which decision, from three sides, each paragraph earned by a separate incident. Every rule is load-bearing; the arrangement is not.

**Acceptance:**

- [ ] No rule currently in the section is dropped, weakened, or moved into a skill
- [ ] The three authority paragraphs are one account of who decides what, materially shorter than the 517 words they replace
- [ ] Headings partition the section so a new rule has an obvious home that is not the tier table's
- [ ] The stamp moves and `CHANGES.md` describes the result as guidance, so a project that reworded the section can carry it rather than take the new text

---

#### `[T-5]` Per-package adoption in a monorepo

**Tags:** `[feat]` `[someday]`

**Outcome:** A monorepo can adopt the method per package, each with its own canon and queue, instead of one config at the root.

**Acceptance:**

- [ ] `.sdd.yml` resolution finds the nearest config, not only the repo root
- [ ] Adoption asks which scope it is installing into when several packages exist
- [ ] A skill invoked inside a package reads that package's paths

---

#### `[T-9]` Run the stamp comparison against a real prior adoption

**Tags:** `[chore]` `[next]`

**Outcome:** The carry is known to work in the field, not only against the checkers.

**Context:** T-7's fourth acceptance criterion, unmet at merge — plan step 5 is a `[gate]` and the branch shipped without it. Everything mechanical is enforced by `check_scaffold.py`; what no checker reaches is whether an agent, handed a `CHANGES.md` entry and a region worded in the project's own terms, edits the wording instead of replacing it. The first re-run also exercises the v0.2.0 baseline path, since the adopting project's fences predate the stamp.

**Acceptance:**

- [ ] `/sdd:setup` re-run against the project whose fenced regions hold its own prose
- [ ] The 0.3.0 integration change lands; that project's wording, ids and cross-references survive
- [ ] Stamps advance only on files where a carry happened, and nothing below a closing marker moves
- [ ] What the run got wrong, if anything, is filed rather than fixed in place

---

#### `[T-8]` Adoption offers permission rules for the integration commands

**Tags:** `[feat]` `[next]`

**Outcome:** A project that adopts the method can have the operator's merge
decision enforced by a permission prompt, not only by prose an agent may reason
past.

**Context:** ADR 0010 records why the prose exists and why it is not enough — a
text rule competes with the agent's own disposition toward autonomy and thins
out over a long context. `ask` rules on `git merge*`, `git push*` and
`gh pr merge*` in the project's `.claude/settings.json` make integration a
dialog the agent cannot skip.

The trade-off to settle first: prefix matching does not see the target branch,
so `git push*` catches pushing a feature branch too — which the agent is
supposed to do, before the review, to open the PR at all. Either accept the
friction, since `ask` is a prompt and not a refusal, or reach for a hook that
inspects the refspec. Decide it in the ticket rather than mid-implementation.

**Acceptance:**

- [ ] The feature-branch push question is settled one way and the reason is
      written down
- [ ] `/sdd:setup` proposes the rules and shows their exact JSON before asking
- [ ] Declining is a first-class answer; adoption completes either way
- [ ] An existing `permissions` block is extended, never replaced, and a rule
      already present is not duplicated
- [ ] The final report says whether the rules landed

---

#### `[T-2]` Portable structural checker for adopting projects

**Tags:** `[feat]` `[next]`

**Outcome:** A project that adopted the method can check its own canon rules mechanically, the way `scripts/check.sh` checks this repo.

**Acceptance:**

- [ ] The check is expressed in the project's own terms, not this repo's
- [ ] It runs from the `verify:` command in `.sdd.yml` or alongside it
- [ ] It reports which invariants have a checker and which are conventions

---

#### `[T-3]` Roadmap-authoring skill

**Tags:** `[feat]` `[someday]`

**Outcome:** A skill that turns a direction discussion into roadmap phases with objectives and gates, and keeps the roadmap out of ticket territory.

**Acceptance:**

- [ ] Produces phases with an objective and a closing gate each
- [ ] Refuses to write items that are tickets in disguise
- [ ] Names which roadmap items have tickets in the queue and which do not

---

## Done

- `[T-10]` `[bug]` `[PR #2]` A reviewer sizes by seam and cannot block on a missing artifact — the tier's signals name decisions instead of modules, and a methodology gap is reported to the operator rather than ranked with the defects.
- `[T-7]` `[fix]` `[PR #1]` Compare fence stamps instead of fenced text — the version on the marker, `CHANGES.md` as described changes, ADR 0011. Merged with the field gate outstanding; that is T-9.
- `[T-6]` `[feat]` `[branch: feat/scaffold-upgrade]` Bring an adopted scaffold up to a newer plugin version — the fence, the gate that enforces it, ADR 0009. Gate run against a real prior adoption; the defect it surfaced is T-7.
- `[T-4]` `[chore]` `[branch: main]` Publish to GitHub — public at `kremniov/sdd`, marketplace `kremniov`, plugin `sdd` 0.1.0.
- `[T-1]` `[feat]` `[branch: master]` Extract the method into a portable plugin — five skills, three skeletons, a project scaffold, and a config seam.
