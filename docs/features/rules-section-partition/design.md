# Rules section partition — design

**Ticket:** T-11 · **Plan:** [plan.md](plan.md)

## Problem

`CLAUDE.section.md` is 2115 words, up from 1718 before T-10 — 23% growth from
one field fix. 1351 of those words sit under `### Process tiers`, which holds
tiers, artifact locations, plan rules, the test-first rule, evidence,
integration, review, the two scales, subagents and when to invoke a skill. It
stopped being about tiers some time ago; it is where a rule lands when nothing
else claims it, which is a property of the heading structure, not of any rule.

Inside it, integration (221 w), independent review (161 w) and the two scales
(135 w) state one principle — who holds which decision — from three sides. Each
was written on a separate incident, each restates the others' ground, and none
can be deleted because each also carries rules the others do not.

The file ships to every adopting project and loads on every request there.

## Goal / Non-goals

**Goal:** the same rules, arranged so a new rule has an obvious home, and stated
without the prose that accumulated around them.

**Non-goals.** No rule is dropped, weakened, or re-litigated — this is an
editorial pass, not a review of the method. Nothing moves into a skill:
invariant 4 requires execution-time rules to be in the rules file, and a skill
loads on a trigger. `README.md`'s condensed table is not the subject.

The `Comments`, `Architectural invariants`, `Significant decisions` and `Docs
discipline` subsections were initially held out of the editorial pass. Reversed
during execution, on the operator's decision: the invariant this work amends
applies to all shipped text, so exempting four subsections would have merged a
canon rule that this repository's own scaffold breaks. Their rules are held
fixed; only their justifications go.

## Decisions

- **Partition by phase of work** — sizing, design and plan, execution, handing
  over — rather than by actor or by artifact. The agent always knows which phase
  it is in, so "where does this rule go" has an answer that does not need
  arguing. Actor-based lands ~70% under "what the agent owes" and reproduces the
  present problem under a new heading; artifact-based strands the test-first and
  evidence rules, which govern no document. → ADR
- **A rule ships without its justification.** An explanation of why a rule exists
  does not ship; a clause naming what does *not* satisfy the rule does, written
  as a rule rather than as an account of the incident that produced it. "A plan
  approved and a `go` at execution do not carry that authority" is the rule's
  boundary; "an agent holding every criterion read the list as a procedure and
  merged" is decoration on it. → ADR
- **A disobeyed rule is reworded, not annotated.** When a rule fails to hold, the
  response is to sharpen its wording until the wrong reading is unavailable, not
  to add prose arguing for it. Observed on this repo: the merge-without-approval
  hole closed when "integrating a branch is a decision, not a step" became "is
  the operator's decision, never the agent's" — the rationale added beside it did
  no work. Rejected: keeping justifications wherever an incident produced them,
  which is the rule that grew the section in the first place. → ADR
- **The authority triad becomes one account** under `Handing over`, covering
  merge-ready, who decides integration, what independence means, and the two
  scales. Target ~280 words against 517, with every rule preserved.
- **`layout.md` is corrected in the same branch.** It still describes the re-run
  as diffing the fenced region against the template; since T-7 the comparison is
  between version stamps. It is stale against invariant 2 and ADR 0011, and it
  describes the file this ticket restructures.

## Architecture

The section's headings become: intro and path table, then `Sizing the work`,
`Design and plan`, `Execution`, `Handing over`, then the existing
`Architectural invariants`, `Significant decisions`, `Docs discipline`,
`Comments`. Subagents and skill-invocation move under `Execution`.

The fence is the seam that carries this to adopting projects. The region changes,
so the stamp moves to v0.5.0 and `plugin.json` follows; `CHANGES.md` gets a
0.5.0 entry describing the result as guidance, not as replacement text, so a
project holding its own wording can rearrange rather than overwrite (ADR 0011).
`CLAUDE.md` is re-rendered from the template (invariant 9).

## Invariants & docs

- **Invariant 2** — the stamp must move with the region; `check_scaffold.py`
  enforces it and the `CHANGES.md` accounting.
- **Invariant 4** — the constraint that keeps every rule in this file.
- **Invariant 7** — currently scoped to skills ("state what to do, not how not to
  disobey"). The second and third decisions extend that scope to the scaffold and
  give it an editorial test. Amend the entry in place, keeping its number
  (invariant 8), citing the new ADR.
- **Invariant 9** — re-render `CLAUDE.md`; `check.sh` fails on drift.
- `docs/architecture/layout.md` — the stale stamp/diff description above.

## Error handling

A rule that cannot be stated without its justification is not yet stated as a
rule; it gets reworded until it is. Where that fails, it keeps the explanation
and the failure is named in the branch report rather than hidden by declaring the
prose essential — the inventory below makes such a case visible instead of
letting it pass as a word count.

## Testing

`./scripts/check.sh` is the gate: fence well-formed, stamp moved and not ahead of
the plugin, `CHANGES.md` accounting complete, `CLAUDE.md` in sync, every `/sdd:`
reference resolving, no placeholder leakage.

Beyond it, a **rule inventory**: every rule in the pre-change section, enumerated
from `main`, mapped to the line that carries it afterwards. This is what
distinguishes an editorial pass from a rewrite, and no automated check reaches
it. Word count is reported as evidence, not as a target — a shorter section that
lost a rule fails.
