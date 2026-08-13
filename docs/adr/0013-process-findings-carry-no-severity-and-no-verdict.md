# ADR 0013 — A process finding carries no severity and no merge verdict

**Status:** accepted · **Date:** 2026-08-13 · **PR:** —

## Context

The rules file tells a reviewer what a merge candidate looks like — green, docs
discipline satisfied, the design cycle its tier calls for — and said nothing
about how to report a shortfall. So a shortfall arrived in the only shape a
review had: a severity level and a verdict.

On two consecutive PRs the single highest finding was "no `design.md`,
therefore not merge-ready", with no functional finding anywhere in the report.
Nothing was wrong with the code, nothing would break, and no run could have gone
red — but the report's one red line was about a missing markdown file, ranked
above the bugs, which in those two runs did not exist and in the next run will.

Two things were conflated. A defect is a claim about the code that a run can
settle. A methodology deviation is a claim about how the work was produced,
which only the operator can price: they know whether the ticket was ambiguous,
whether the design happened in conversation, and whether the artifact is worth
writing after the fact. The integration rule already says the reviewer does not
hold the merge decision; the review's own output was the place that had not been
told.

## Decision

A review reports on two scales. Defects — wrong now, or wrong under an input the
code will see — carry the severity, and the highest is the review's headline. A
deviation from the method — a missing artifact, a tier the reviewer would have
judged higher, a canon file not updated — is a *process* finding: no severity
level, addressed to the operator, never a merge verdict. The reviewer names what
is missing and what it would have caught, and leaves the call.

## Alternatives

- **Keep one scale, cap process findings at the lowest severity.** Still ranks
  them against defects, and the cap is the first thing a reviewer argues past
  when the gap looks serious.
- **Have the reviewer skip methodology entirely.** Loses a real signal: a design
  cycle skipped on genuinely ambiguous work is worth hearing about, and the
  reviewer is well placed to see it from the diff.
- **Let a process finding block, but only above tier 1.** Requires the reviewer
  to settle the tier first, which is the judgement ADR 0012 just took away from
  the diff — the block would rest on the weaker of the two calls.
- **Fix it in the reviewer's prompt rather than the rules file.** The reviewer's
  independence is defined by reading the committed artifacts and nothing the
  author wrote for it (ADR 0010); guidance that lives in a prompt is guidance the
  operator has to re-supply on every run and every tool.

## Consequences

A review's headline severity now means the code, which makes the reports
comparable across runs and keeps a missing artifact from crowding out a bug. The
operator gains a decision they were already formally holding and, in practice,
were not being handed: whether a gap in the method is worth blocking on. A
reviewer that ignores the split produces a finding the operator can dismiss on a
named rule rather than by argument. This is the integration authority of ADR
0010 applied to the review's output; no invariant moves. Carried to adopting
projects by the `CHANGES.md` entry at v0.4.0.
