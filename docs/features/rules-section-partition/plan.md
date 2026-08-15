# Rules section partition — plan

**Ticket:** T-11 · **Design:** [design.md](design.md)

## Scope

`CLAUDE.section.md` ends the branch partitioned by phase of work, with the
authority triad collapsed into one account and justifications stripped, carrying
no fewer rules than it does on `main`. The stamp moves to v0.5.0 with a
`CHANGES.md` entry, `CLAUDE.md` is re-rendered, invariant 7 is amended to cover
the scaffold, and both ADRs are written. `layout.md`'s stale description of the
re-run comparison is corrected in the same branch.

Left for a follow-up: T-9, the carry of everything from v0.2.0 onward into the
prior adoption, which runs against the section this branch produces.

## Order

The inventory is built before any edit, because an inventory derived from the
finished text proves nothing about what the text lost. The move runs before the
collapse so that its diff is verifiable as a pure rearrangement — once wording
changes in the same commit, nothing distinguishes a moved rule from a dropped
one. Version, stamp and change log follow the text they describe. Canon and
decision records come last because they cite the finished shape.

## Steps

### Step 1 — The rules on `main` are enumerated

**Goal:** a numbered list of every rule the section currently states, each citing
the paragraph it came from.

**Constraints:** built from `git show main:...`, not from the working tree.
Produces no repository change — it is the instrument the later steps are measured
against, and it lives in the scratchpad until it is reported.

**Touches:** nothing under version control.

**DoD:** the list exists; its count is reported; every paragraph of the section
on `main` has contributed at least one entry or is explicitly marked as carrying
no rule.

### Step 2 — The section is partitioned by phase, wording untouched

**Goal:** `### Sizing the work`, `### Design and plan`, `### Execution`,
`### Handing over` replace `### Process tiers`, with every paragraph moved under
the phase it belongs to and none rewritten.

**Constraints:** a pure rearrangement — no paragraph's text changes in this step.
`Architectural invariants`, `Significant decisions`, `Docs discipline` and
`Comments` keep their content.

**Touches:** `plugins/sdd/templates/project/CLAUDE.section.md`.

**DoD:** the sorted non-heading lines of the section before and after are
identical — `diff <(git show main:… | sort) <(sort …)` shows only the heading
lines. `check_scaffold.py` fails on the unmoved stamp at this point; that is
expected and closes in step 4.

### Step 3 — The triad is one account and justifications are gone

**Goal:** integration, independent review and the two scales become one account
under `Handing over`; across the section, an explanation of why a rule exists is
removed and a clause naming what does not satisfy a rule is kept, stated as a
rule.

**Constraints:** every entry from step 1 survives. No rule is weakened or
re-litigated. A rule that cannot be stated without its justification is reworded
until it can; where that fails it keeps the prose and the case is named in the
report rather than resolved by declaring the prose essential.

**Touches:** `plugins/sdd/templates/project/CLAUDE.section.md`.

**DoD:** each numbered entry from step 1 maps to a line in the new text, the
mapping written out in full; the word count of the section and of the former
triad reported against 2115 and 517.

### Step 4 — The change is stamped, versioned and described

**Goal:** the fence reads v0.5.0, `plugin.json` reads 0.5.0, `CHANGES.md` has a
0.5.0 entry, `CLAUDE.md` is re-rendered.

**Constraints:** the entry describes the result as guidance a differently-worded
section can be rearranged to match, with no quoted template text (ADR 0011).
`CLAUDE.md` is generated from the template, never edited (invariant 9).

**Touches:** `CLAUDE.section.md`, `CHANGES.md`,
`plugins/sdd/.claude-plugin/plugin.json`, `CLAUDE.md`.

**DoD:** `./scripts/check.sh` passes.

### Step 5 — `layout.md` describes the comparison that exists

**Goal:** the paragraph saying a re-run diffs the fenced region against the
template is replaced by the stamp comparison, and the heading structure it
describes matches the file after step 2.

**Constraints:** `layout.md` says where things are; invariant 2 and ADR 0011 say
what must hold — link, do not restate.

**Touches:** `docs/architecture/layout.md`.

**DoD:** `./scripts/check.sh` passes; no occurrence of the old description
remains — `grep -n 'diffs that region' docs/architecture/layout.md` is empty.

### Step 6 — The decisions are recorded and invariant 7 is amended

**Goal:** an ADR for the phase partition and an ADR for the editorial rule; entry
7 in `invariants.md` extended from skills to shipped text generally, with a
detect that names the editorial test.

**Constraints:** ADR numbers sequential from the directory's highest, `PR:` left
as a dash until the number exists. Invariant 7 keeps its number (invariant 8);
its existing exception for the `/sdd:debug` threshold survives.

**Touches:** `docs/adr/00NN-*.md` ×2, `docs/architecture/invariants.md`.

**DoD:** `./scripts/check.sh` passes, including `check_canon.py` on the amended
entry.

## Verification

`./scripts/check.sh` gates every step from 4 onward. The inventory mapping from
step 3 is the branch's own gate and goes in the PR body, where the operator reads
it against the diff — no automated check reaches "a rule survived", and the last
branch shipped with an unrun `[gate]` rather than pausing on one, so this one is
placed where it is actually read.

## Docs & ADR

`docs/architecture/invariants.md` (entry 7) and `docs/architecture/layout.md`
update in this PR. Three design decisions are marked `→ ADR`; the second and
third are one editorial rule and become a single record, so two ADRs are due.
