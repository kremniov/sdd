# ADR 0026 — Review fixes preserve scoped permission

**Status:** accepted · **Date:** 2026-09-08 · **PR:** [#6](https://github.com/kremniov/sdd/pull/6)

## Context

The method required verification of review fixes but left their handover and
conditional integration permission implicit.

## Decision

Verify, commit and push requested fixes on the same branch, then report resolved
and remaining findings with verification. The user starts repeat independent
review. Without integration permission, stop before merge. Permission to fix
specified findings and merge remains valid once its conditions are met; changed
decisions or scope return to the user. Clarify ADR 0022.

## Consequences

Fix instructions alone do not authorize integration. Conditional permission
requires neither a second merge approval nor an automatic repeat review.
The initial independent review remains required.
