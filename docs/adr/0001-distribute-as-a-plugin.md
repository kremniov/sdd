# ADR 0001 — Distribute the method as a Claude Code plugin, not a copyable starter

**Status:** accepted · **Date:** 2026-08-09

## Context

The method existed as files inside one codebase: skills under a vendored
directory, templates under a docs path, rules in that project's `CLAUDE.md`.
Moving it to a second project meant copying files and hand-editing every
cross-reference. Two consequences showed up before the extraction even started:
a fix to a template could not reach anyone who had already copied it, and the
rules could only be found by someone who knew where to look in the origin repo.

## Decision

Ship as a plugin installed from a marketplace. Skills, templates and the project
scaffold live in the plugin and are read from `${CLAUDE_PLUGIN_ROOT}`. What
lands in the adopting project is deliberately small: a `.sdd.yml` mapping, the
docs scaffold, and a section appended to `CLAUDE.md`.

## Alternatives

- **`install.sh` that copies files** — every consumer forks at install time;
  updates are manual and in practice never happen.
- **A git submodule** — inflicts submodule ergonomics on every adopter for a
  payload that is a dozen markdown files.
- **A template repository** — only works when starting a project from scratch,
  and the interesting case is adopting into a codebase that already exists.

## Consequences

Updates reach consumers through the normal plugin update path, and a template
fix is a version bump rather than a migration. Skills are namespaced
`/sdd:<name>`, which is unavoidable and slightly verbose.

The repository is a *marketplace containing one plugin*
(`.claude-plugin/marketplace.json` + `plugins/sdd/`), because a single repo
cannot be both a plugin and its own marketplace. Installation is therefore two
commands.
