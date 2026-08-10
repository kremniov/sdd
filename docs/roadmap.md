# Roadmap

Direction for this plugin. Sequence, not dates. Not a task list — that is
`docs/tasks.md`.

---

## Phase 1 — Portable  *(current)*

**Objective:** the method installs into a repository that has never seen it, and
the operator can run a tier-2 feature end to end without reading this repo.

- The plugin installs and its skills resolve their own bundled files
- Adoption reads an existing docs layout instead of imposing one
- The canon can be derived from a codebase that already exists
- Verified against a bare repo, a documented repo, and a project in another language

## Phase 2 — Self-checking

**Objective:** a project that adopted the method can tell mechanically when it
has drifted from its own canon.

- A portable checker expressed in the adopting project's terms (T-2)
- `/sdd:canon` re-run reports drift as four lists: held, drifted, broken, undocumented
- Invariants carry an explicit "enforced by" or "convention" marker

## Phase 3 — Shared

**Objective:** someone who is not the author adopts it and their feedback shapes
the next version.

- Published, installable, versioned with a changelog (T-4)
- The rules carry their evidence: which came from a measurement, which from
  judgement, and what the measurement's limits were
- A second codebase's canon exists, derived by the plugin rather than by hand
