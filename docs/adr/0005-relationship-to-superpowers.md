# ADR 0005 — What we take from Superpowers, and how we say so

**Status:** accepted · **Date:** 2026-08-09

## Context

This method was developed while running [Superpowers](https://github.com/obra/superpowers)
by Jesse Vincent on a production codebase, and several of its ideas are
load-bearing here. Two skills carried its names until the 0.3.0 rename
(`brainstorming`, `systematic-debugging`), and the three-failed-fixes rule is
taken from it outright.

Before publishing, the question was asked directly: does this infringe?

Findings, measured rather than estimated:

- Superpowers is **MIT, Copyright (c) 2025 Jesse Vincent**. MIT permits copying,
  modification, distribution and commercial use; the sole condition is retaining
  the notice in copies or substantial portions.
- Comparing this plugin against the whole Superpowers corpus (84 markdown files,
  1.1M characters), the **longest identical run anywhere is 24 characters** —
  the length of an ordinary phrase. The two same-named skills score 2.6% and
  2.4% textual similarity, with longest shared runs of 6 and 7 characters
  (` YAGNI`, and a markdown table separator).
- Structures diverge: their plan sections are `Scope Check / File Structure /
  Task Right-Sizing`, ours are `Scope / Order / Steps / Verification / Docs &
  ADR`. They ship no artifact skeletons at all.

So no substantial portion is present, and the MIT notice requirement is not
triggered. Ideas and methods are not copyrightable; expression is, and none of
theirs is reproduced here.

## Decision

Attribute anyway, prominently, in the README — not because the licence compels
it but because the method's own account of itself is incomplete without naming
what it was measured against.

The attribution states three things: which ideas are theirs (an explicit named
procedure beats improvised discipline; debugging deserves its own process; three
failed fixes means the architecture), that the divergence is calibration rather
than disagreement, and that every line of text here is written from scratch.

The framing is credit, not contrast. The measured claim — that a near-constant
process cost meets a payoff scaling with ambiguity — is an argument for a dial,
not a verdict on the discipline. Positioning this as a correction of someone
else's work would be both inaccurate and graceless.

The licence line records that this is independent work, not affiliated with or
endorsed by the Superpowers project, so no reader infers a relationship that
does not exist.

## Alternatives

- **Say nothing.** Legally sufficient, and the option we rejected: the README
  argues against a class of workflow without naming the member of that class it
  was actually measured against, which reads as evasion once a reader recognizes
  the target.
- **A LICENSE-adjacent NOTICE file.** Appropriate for retained code; here it
  would overstate the relationship, since no file is a copy or a derivative.
- **Attribute only in the debug skill**, where the borrowed rule lives. Too
  narrow — the tier table, which is the centre of this method, exists because of
  a measurement run against their corpus.

## Consequences

Two claims in the README are now falsifiable and must stay true: that no file
here is a copy or derivative, and that the tier table came out of a paired
measurement. If a future version vendors a Superpowers file verbatim, the first
claim breaks and the MIT notice requirement engages — vendor deliberately or not
at all, and never by half.

The measurement itself stays in the origin repository and is not published. The
README therefore describes its shape and result without offering the log, which
is honest as long as the description does not overstate what n=3 across tiers
0–1 can support.
