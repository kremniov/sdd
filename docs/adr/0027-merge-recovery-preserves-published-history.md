# ADR 0027 — Merge recovery preserves published history

**Status:** accepted · **Date:** 2026-09-08 · **PR:** [#6](https://github.com/kremniov/sdd/pull/6)

## Context

Integration can fail after the final Done commit is published. Keeping Done
literally last would require rewriting history or adding an artificial commit.

## Decision

Resolve known blockers and run available checks before the final commit. After
merge failure, report the cause and branch state. Permission persists within
its scope: resolve technical blockers, verify and retry when ready. Changed
agreed decisions or scope return to the user. Verified repair commits may follow
Done; preserve published history. Amend the final-commit rule in ADR 0022.

## Consequences

Done still records integration approval, not completed integration. Its commit
is normally last, with a narrow exception for recovery. No empty final commit
or history rewrite is needed solely to preserve that order.
