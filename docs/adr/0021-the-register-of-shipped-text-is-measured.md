# ADR 0021 — The register of shipped text is measured

**Status:** accepted · **Date:** 2026-09-04 · **PR:** [#6](https://github.com/kremniov/sdd/pull/6)

## Context

Invariant 7 says shipped text states what to do and not why to do it, and it is
enforced by a reader. Reading held the line on justification prose and held no
line at all on density.

Measured across the corpus, negation density — *not / never / no / only /
without / rather than* per 100 words — ran at 4.0 in the rules section, 3.4 in
`/sdd:canon` and 3.6 in `/sdd:subsystem`. Ordinary technical prose runs 1 to 1.5.
One table cell reached 17.9 in 28 words, and that cell governed tier 0, where an
agent then started coding with no reply to the user.

Length drifted the same way with nothing to stop it. `_DESIGN.md` named a budget
of about 1300 words; two `SKILL.md` files had passed 2100 with no budget named at
all.

These texts are also the style model for every `design.md` and `plan.md` the
method produces, so the register copies itself into the artifacts.

## Decision

The target register is ASD-STE100, simplified technical English: one fact or one
rule per sentence, active voice, present tense. It is what a rewrite aims at, and
the numbers below are how drift from it is caught. The rules section names the
register, so an agent writing any document in an adopting project has the model.

`scripts/check_register.py` measures every shipped file and `./scripts/check.sh`
fails on a breach.

| Measure | Budget |
|---|---|
| Negation density | 2.5 per 100 words of prose, per file |
| Negation density, the resident rules section | 2.0 |
| Length, a `SKILL.md` | 1200 words |
| Length, the resident rules section | 400 words |
| Heading depth, a skill or a skeleton | H3 |

Prose excludes fenced code blocks, which are examples rather than instructions.
The 2.5 threshold is where `tasks/SKILL.md` already sat, and that file was the
strongest text in the plugin.

The two budgets a script cannot decide — the share of a document spent on
rationale, and the count of claims it makes — stay written budgets in
`_DESIGN.md` and `_PLAN.md`, expressed as a closing condition per section.

Nothing is allowlisted. A file that outgrows a budget is rewritten, or split into
a reference file beside its `SKILL.md`.

`CHANGES.md` is outside the measure, on the same ground invariant 7 already puts
it outside: it reaches no project and describes what past versions replaced.

## Alternatives

- **All four budgets mechanically.** Rationale share and claim count need a
  reader; a counter for either would fire falsely and get ignored.
- **Density alone.** Length is what turned two skills into files nobody finishes,
  and it is the cheaper of the two to measure.
- **A prose linter.** Rejected in the v2 handoff: those tools find filler
  vocabulary, and this corpus is dense rather than watery.
- **An allowlist for files whose subject is prohibition.** The exemption is how
  a corpus reaches 4.0.

## Consequences

Invariant 12 states the budgets, and the check reports every file on every run,
so a rewrite has a number to work against rather than a reviewer's impression.

Splitting into reference files becomes a normal move: `/sdd:canon` keeps
bootstrap and audit beside it, and `/sdd:setup` keeps the fence machinery beside
it. A reference file is shipped text and is measured for density and depth.

The threshold is a ratchet, not a target. A file that measures 0.7 is under no
obligation to add anything.
