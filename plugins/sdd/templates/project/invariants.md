# Architectural invariants

Canonical list. These rules apply to all work, every feature. Any change that
violates one is an architectural regression and requires an explicit, documented
invariant change — open an ADR under `{{adr}}`.

This is the single source of truth for the invariants. The rules file and feature
designs **link here**; they do not restate them.

<!--
Populate this list with `/sdd:deriving-canon`, which reads the codebase and
proposes the rules it already holds. An invariant is a rule the code obeys
today and that a reviewer would push back on breaking — not an aspiration.

Each entry: a bold name, then what must hold, stated so a reviewer can decide
whether a diff violates it. Name the mechanism that enforces it where one
exists; a rule nothing checks is a convention, and worth marking as such.
-->

1. **<Name>.** <What must hold.>
2. …

## Per-layer responsibilities

Where the codebase has layers, state what each owns and what it must not do —
the "must not" column is what makes the table usable in review.

| Layer | Location | Owns | Must NOT |
|---|---|---|---|
| | | | |
