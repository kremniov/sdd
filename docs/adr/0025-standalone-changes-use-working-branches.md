# ADR 0025 — Standalone changes use working branches

**Status:** accepted · **Date:** 2026-09-08 · **PR:** [#6](https://github.com/kremniov/sdd/pull/6)

## Context

Standalone queue and setup procedures ended with reports, leaving their Git
handover implicit. A direct commit or push to an integration branch can trigger
CI before the user has accepted the change.

## Decision

Check the branch before editing files intended for Git. Create a working branch
when on main, master or another integration branch. Commit and push only to
working branches; integrate by PR merge after explicit permission. Standalone
operations use the same handover. Operations within approved work share its step
and PR. Ignored working notes are outside this sequence. Clarify ADR 0022.

## Consequences

Even a standalone queue edit produces a reviewable PR. Work owns the sequence;
resident rules retain the branch constraint and specialized skills reference it.
Working-branch pushes and PRs can still trigger CI under project configuration.
