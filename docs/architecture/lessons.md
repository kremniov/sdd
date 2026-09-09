<!-- sdd:scaffold v1.1.0 -->
# Lessons

Record verified observations useful in later project work. Each entry includes
a date, the observation and an evidence or ADR reference where available.
Add newest entries first. Use `/sdd:canon` when an observation becomes a candidate
rule; link the invariant if it is accepted. Omit general advice and duplicate rules.
<!-- /sdd:scaffold -->

- **2026-09-04** — `check_scaffold.py` rejects a fence stamped ahead of
  `plugin.json`, so a version bump has to travel in the same commit as the first
  stamp that carries it, never in a later one.
- **2026-09-04** — `check_skill_refs.py` resolves a `/sdd:` name against the
  skills directory, so prose naming a skill has to land in the same commit as
  that skill's directory or after it.
