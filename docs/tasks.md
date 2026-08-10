# Tasks

The "what do I pull next" queue. Format: the `managing-tasks` skill.

## TODO

#### `[T-5]` Per-package adoption in a monorepo

**Tags:** `[feat]` `[someday]`

**Outcome:** A monorepo can adopt the method per package, each with its own canon and queue, instead of one config at the root.

**Acceptance:**

- [ ] `.sdd.yml` resolution finds the nearest config, not only the repo root
- [ ] Adoption asks which scope it is installing into when several packages exist
- [ ] A skill invoked inside a package reads that package's paths

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

- `[T-4]` `[chore]` `[branch: main]` Publish to GitHub — public at `kremniov/sdd`, marketplace `kremniov`, plugin `sdd` 0.1.0.
- `[T-1]` `[feat]` `[branch: master]` Extract the method into a portable plugin — five skills, three skeletons, a project scaffold, and a config seam.
