<!-- sdd:scaffold v1.0.0 -->
# Lessons

What the work taught and a rule would have missed: a runtime constraint of the
stack, the real shape a dependency returns, a command that behaves unlike its
documentation.

One line each, newest first, with its date and the ADR where there is one. Add a
line on the branch that learned it (`/sdd:canon`).

This is the one canon file that carries dates. `invariants.md` and `layout.md`
state what is true now.

A lesson that hardens into a rule earns an invariant, and its line then names
that number.
<!-- /sdd:scaffold -->

- **2026-09-04** — `check_scaffold.py` rejects a fence stamped ahead of
  `plugin.json`, so a version bump has to travel in the same commit as the first
  stamp that carries it, never in a later one.
- **2026-09-04** — `check_skill_refs.py` resolves a `/sdd:` name against the
  skills directory, so prose naming a skill has to land in the same commit as
  that skill's directory or after it.
