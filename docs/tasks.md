# Tasks

The "what do I pull next" queue. Format: the `managing-tasks` skill.

## TODO

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

#### `[T-4]` Publish to GitHub

**Tags:** `[chore]` `[next]`

**Outcome:** The marketplace is installable from a public GitHub repo by someone who is not the author.

**Acceptance:**

- [ ] `/plugin marketplace add <owner>/sdd` works from a clean machine
- [ ] README install instructions match the published name
- [ ] A CHANGELOG records 0.1.0

---

## Done

- `[T-1]` `[feat]` `[branch: master]` Extract the method into a portable plugin — five skills, three skeletons, a project scaffold, and a config seam.
