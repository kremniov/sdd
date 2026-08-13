# ADR 0015 — A rule ships without its justification, and a disobeyed rule is reworded

**Status:** accepted · **Date:** 2026-08-13 · **PR:** —

## Context

Three paragraphs in the rules section — integration, independent review, finding
severity — had grown to 517 words stating one principle about who holds which
decision. Each was written after an incident: an agent merged without the
operator's word; a review run from the author's own session was treated as
independent; a missing `design.md` was reported as the highest-severity finding
and blocked a merge. Each incident added both a sharper rule and a paragraph
explaining why the rule exists.

Only one of the two did any work. The merge hole closed when "integrating a
branch is a decision, not a step" became "is the operator's decision, never the
agent's". The severity hole closed when the two scales were named. In both cases
the explanation beside the rule was already there in spirit, and the agent had
read past it — because an explanation is something to agree with, while a rule is
something to obey.

Invariant 7 already forbade this prose in skills, and said nothing about the
scaffold, which is the text that ships to every project and loads on every
request.

## Decision

An explanation of why a rule exists does not ship. A clause naming what does
*not* satisfy a rule does, written as a rule rather than as an account of the
incident that produced it — "an approved plan and a `go` are not that approval",
not "an agent holding every criterion read the list as a procedure and merged".
The test for a sentence is whether deleting it changes what someone may do.

When a rule fails to hold, the response is to reword it until the wrong reading
is unavailable, never to add prose arguing for it. Invariant 7 is extended from
skills to all shipped text, keeping its number and its existing exception.

## Alternatives

- **Keep a justification wherever an incident produced one.** This is the rule
  that grew the section; every paragraph in it qualified under that test.
- **Keep justifications but cap them at a sentence.** A cap prices the prose
  without asking whether it does anything, and the sentence that survives is the
  one hardest to cut, not the one that changes behaviour.
- **Move the reasoning to the ADRs and link it from the rule.** The links are the
  cost this avoids: a rule that needs a click to be understood is a rule that was
  not stated. The ADRs hold the reasoning; the rules file does not point at it.
- **Drop the negative clauses too, for consistency.** They are what the observed
  failures were made of — every incident was a reading the bare rule allowed.

## Consequences

The rules section states more rules in fewer words, and a future incident
produces a rewrite of the rule that failed rather than a paragraph beside it,
which bounds the growth this repository was measuring. The reasoning is not lost:
the ADR corpus is where a decision's why lives and is dated, and this file is one
of them. Rules become harder to write — a rule that cannot be stated without its
justification is not yet stated as a rule — which is the intended cost. Invariant
7 changes scope and cites this record; its `/sdd:debug` threshold exception
survives, being a rule and not an argument.
