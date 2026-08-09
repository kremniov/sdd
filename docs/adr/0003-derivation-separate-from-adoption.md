# ADR 0003 — Deriving the canon is a separate skill from adopting the method

**Status:** accepted · **Date:** 2026-08-09

## Context

Adoption needs the project to have an architecture canon: the rules say "link
the canon rather than restating it", which is inert without somewhere to link.
The obvious move is to have the adoption skill produce one.

But the two jobs differ in every dimension that matters. Adoption takes the
repo's *layout* as input and writes a scaffold; it is mechanical, runs once, and
is safe to automate. Derivation takes the repo's *code* as input and produces
claims about what rules it holds; it requires reading judgement, it is wrong in
interesting ways, and its output must be confirmed line by line by someone who
knows the project.

They also expire differently. Adoption is done once. Derivation is worth
re-running whenever the code has drifted from what the canon says — on an
established codebase, repeatedly.

## Decision

Two skills. `adopting-sdd` lays the scaffold, writes `.sdd.yml`, and creates
`invariants.md` as a header with instructions and an empty body.
`deriving-canon` fills that body, and is documented as re-runnable.

`deriving-canon` refuses to write a speculative list. When a codebase shows no
discernible rules, the honest output is a note saying the canon is not yet
established.

## Alternatives

- **One skill doing both** — a long skill whose second half needs an entirely
  different mode of work, and which cannot be re-run without redoing adoption.
- **Ship a generic invariants list** — the rules that matter are the ones this
  codebase actually holds; a generic list is filler that gets cited as if it
  were observed.

## Consequences

Adoption ends with a canon file that is deliberately empty, and its final report
must say so and point at the next skill. That hand-off is the cost.

The refusal path matters more than it looks: an invented invariant does not
merely fail to help — it gets linked from designs and defended in review as if
someone had checked it.
