# Architectural invariants

Canonical list. These rules apply to all work in this repository. Any change
that violates one is a regression and requires an explicit, documented invariant
change — open an ADR under `docs/adr/`.

This is the single source of truth. `CLAUDE.md` and feature designs **link
here**; they do not restate them.

1. **The plugin knows no project paths.** A skill reads every project location
   from `.sdd.yml`. A hardcoded `docs/...` inside `plugins/sdd/skills/` is a
   defect — it is what makes a method unportable. Checked by `scripts/check.sh`.
2. **Templates are read, never copied.** Skills point at
   `${CLAUDE_PLUGIN_ROOT}/templates/...`; adoption does not copy a skeleton into
   the project (ADR 0002). Every referenced path must exist — checked by
   `scripts/check.sh`.
3. **Adoption is additive.** No skill overwrites or reformats a file it did not
   write in this run. Where it would change something that exists, it reports
   and asks. A method that rearranges someone's repository on first contact does
   not get a second run.
4. **Execution-time rules live in the project's `CLAUDE.md`.** Not in a skeleton
   comment, which does not survive into the generated artifact, and not only in
   a skill, which loads on a trigger (ADR 0002).
5. **Nothing from the origin codebase leaks in.** No stack, vendor, or
   domain terms in skills or templates — the method is language-agnostic and any
   example that is not generic is a bug. Checked by `scripts/check.sh`.
6. **The canon is observed, never invented.** `deriving-canon` writes only rules
   the code actually holds, and writes nothing when there are none (ADR 0003). A
   speculative invariant is worse than a missing one: it gets cited as if it had
   been checked.
7. **Skills state what to do, not how not to disobey.** No anti-rationalization
   tables, no red-flag blocks, no "regardless of perceived simplicity" gates —
   with one exception, the "three failed fixes" rule in `systematic-debugging`,
   which is kept because that failure mode was observed rather than imagined.
8. **Invariant numbers are stable.** Documents cite them. Append; never
   renumber.

## Layout responsibilities

| Part | Location | Owns | Must NOT |
|---|---|---|---|
| Marketplace | `.claude-plugin/` | the catalogue entry pointing at the plugin | contain the plugin itself |
| Plugin manifest | `plugins/sdd/.claude-plugin/` | name, version, metadata | anything a skill reads at runtime |
| Skills | `plugins/sdd/skills/<name>/` | one job each, config-driven | hardcode a project path, or carry `{{placeholders}}` |
| Templates | `plugins/sdd/templates/` | artifact skeletons | reference the origin project |
| Project scaffold | `plugins/sdd/templates/project/` | what adoption writes into a repo | be read at any time other than adoption |
| Checks | `scripts/check.sh` | the structural gate | require a language runtime beyond python3 |
