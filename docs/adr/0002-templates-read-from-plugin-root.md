# ADR 0002 — Artifact skeletons are read from the plugin, not copied into the project

**Status:** accepted · **Date:** 2026-08-09

## Context

In the origin repo the skeletons lived at a project path and each artifact was
written by copying one. That shape has a defect that was measured rather than
predicted: the HTML comment block at the top of the plan skeleton — where the
execution rules were written — **does not survive into the generated artifact**.
A rule that must be read at execution time was therefore written in the one
place guaranteed not to be read then. The fix in the origin repo was to
duplicate those rules into `CLAUDE.md`.

A copied skeleton has a second failure mode: it ages independently in every
project, so a correction to the shape of a design document cannot reach the
projects that already have one.

## Decision

Skeletons ship in the plugin and are read in place via
`${CLAUDE_PLUGIN_ROOT}/templates/`. The skill instructs the model to read the
skeleton when writing the artifact. Nothing is copied at adoption time.

Rules that must hold *during execution* go into the project's `CLAUDE.md`
through the scaffold section — never only into a skeleton comment.

## Alternatives

- **Copy at adopt time** — the origin repo's shape; every project drifts, and no
  fix propagates.
- **Copy on first use, then leave alone** — the same drift, deferred, and now
  unpredictable across projects.
- **Rules only in the skeleton comment** — demonstrably unread at the moment
  they apply.

## Consequences

A skeleton fix reaches every consumer on plugin update. A project cannot
customize a skeleton without forking the plugin — accepted, because the
skeletons are deliberately generic and the greppability of a consistent corpus
is part of what they are for.

`${CLAUDE_PLUGIN_ROOT}` resolves before skill text reaches the model, so this
works inside skill instructions but cannot be passed as a literal to a tool that
runs later.
