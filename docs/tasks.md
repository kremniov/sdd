# Tasks

The "what do I pull next" queue. Format: `/sdd:tasks`.

## TODO

#### `[T-5]` Per-package adoption in a monorepo

**Tags:** `[feat]` `[someday]`

**Outcome:** A monorepo can adopt the method per package, each with its own canon and queue, instead of one config at the root.

**Acceptance:**

- [ ] `.sdd.yml` resolution finds the nearest config, not only the repo root
- [ ] Adoption asks which scope it is installing into when several packages exist
- [ ] A skill invoked inside a package reads that package's paths

---

#### `[T-7]` A fenced region the project rewrote must not be offered for replacement

**Tags:** `[fix]` `[next]`

**Outcome:** A re-run tells a project what changed in the template since, rather than offering to overwrite the wording that project chose.

**Context:** Found by the T-6 gate. The first upgraded project had rewritten the plugin's guidance in its own terms — its own ticket-id convention, its own cross-references — and the fence now holds that text. The skill's `Different` branch cannot tell "this region is stale" from "this project customized it", so the next re-run will offer to replace prose that is deliberate. The design assumed a fenced region equals the rendered template; that assumption is false the moment a project edits inside the fence, which is the normal case for anyone who adopted before the fence existed.

**Acceptance:**

- [ ] A region that differs from the template is not, by itself, grounds to propose replacing it
- [ ] What the re-run offers is what changed in the template between two versions, not the template's current full text
- [ ] Adoption records the version it wrote, so "between two versions" has a lower bound (the alternative rejected in ADR 0009 — rejected as a *replacement* for the fence, not as a companion to it)
- [ ] Verified against a project whose fenced region is its own prose: the correction lands, the wording survives

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

**Acceptance:**

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

- `[T-6]` `[feat]` `[branch: feat/scaffold-upgrade]` Bring an adopted scaffold up to a newer plugin version — the fence, the gate that enforces it, ADR 0009. Gate run against a real prior adoption; the defect it surfaced is T-7.
- `[T-4]` `[chore]` `[branch: main]` Publish to GitHub — public at `kremniov/sdd`, marketplace `kremniov`, plugin `sdd` 0.1.0.
- `[T-1]` `[feat]` `[branch: master]` Extract the method into a portable plugin — five skills, three skeletons, a project scaffold, and a config seam.
