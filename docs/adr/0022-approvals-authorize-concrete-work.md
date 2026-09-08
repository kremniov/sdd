# ADR 0022 — Approvals authorize concrete work

**Status:** accepted · **Date:** 2026-09-08 · **PR:** —

## Context

The previous rules separated tier-1 approvals, allowed uncommitted plan completion, and described merge as an action only the user performs.

## Decision

Tier 0 waits for a concrete proposal. Tier 1 combines G1 and G2. Commit every completed step before the next; multiple commits per step are allowed. Independent review remains required at every tier. The user authorizes integration and the agent executes it after the final ticket commit. Amend ADRs 0010, 0017 and 0018.

## Consequences

The method distinguishes approval from execution. Resident text routes requests; work owns the full sequence. Invariant 4 follows this distribution.
