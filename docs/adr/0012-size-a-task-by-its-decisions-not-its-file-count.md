# ADR 0012 — Size a task by the decisions it forces, not the files it touches

**Status:** accepted · **Date:** 2026-08-13 · **PR:** —

## Context

The tier table listed three signals for tier 2: a new seam, an invariant that
changes, or several modules moving together. Two of them require judgement about
the design; the third is a count, and a count is available from `git diff`
without reading anything.

That asymmetry decided which signal got used. In a layered codebase, a single
read threaded from the API interface down through handler, domain, storage, the
test fake and the service crosses six or seven packages while opening no
boundary at all — the query already existed and was simply wired up. An external
reviewer, reading only the rules file and the commits, sized two such changes as
tier 2 from the numstat and then reasoned as though the tier had been given,
concluding both were not merge-ready for want of a `design.md`.

The tier exists to buy down ambiguity. A change whose three states and three
responses are already named in the ticket's acceptance criteria has none left to
buy, whatever its diff looks like.

## Decision

All three rows are scoped by what has to be decided. Tier 0 is nothing left to
decide, the ticket already naming the change; tier 1 is one decision to settle;
tier 2's third signal reads "several decisions have to be agreed together". The tier
follows the decisions, not the diff: one call crossing every layer it has to
cross is one decision touching many packages. What raises the tier is a question
the ticket does not already answer — a boundary that did not exist, a rule that
stops holding, or two choices that have to come out consistent in more than one
place. A file count is stated as not being a signal. Whoever disputes a tier
names the seam or the decision that was missed, and the burden falls on whoever
claims the higher tier.

## Alternatives

- **Keep the signal, add "layers do not count" as an exception.** The
  mechanically-checkable signal stays first in the reader's reach and the
  exception is the thing that gets skipped; exceptions lose to counters.
- **Drop the third signal entirely.** Loses the real case it covers — work that
  genuinely forces several choices to line up before any of them can be coded.
- **Give the tier a numeric threshold (packages, lines).** Makes the wrong
  reading official and rewards splitting a diff rather than clarifying a design.
- **Let the author's declared tier be final.** Removes the reviewer's ability to
  say a design cycle was skipped, which is a real failure the review should
  catch.
- **Size by ticket ambiguity alone, with no structural signal.** Too soft to
  settle a disagreement; a new seam is worth a design even when the author finds
  the ticket clear.

## Consequences

The tier can no longer be computed, only argued — which is the point, and it
means a sizing dispute costs a paragraph naming the seam instead of a numstat.
Ambiguity is now a property of the ticket rather than of the change's shape, so
a wide but decided diff runs tier 0 or 1 and a one-file change that opens a
boundary runs tier 2, as the tier-independence of the ADR trigger already
implied. No invariant moves. The wording is carried by `CHANGES.md` at v0.4.0,
so a project that reworded the section gets the change described rather than
overwritten (ADR 0011).
