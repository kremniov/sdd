---
name: deriving-canon
description: Use to build or refresh a project's architecture canon — read the codebase and write down the invariants it already holds, plus where things live. Run after adopting-sdd, or again when the code has drifted from the docs.
---

# Deriving the Canon

Write down the rules this codebase already follows, so that later work can link
them instead of rediscovering them. The canon is **observed, not invented**: an
invariant here is a rule the code obeys today and that a reviewer would push
back on breaking.

Paths come from `.sdd.yml` (`canon:`).

Reading `.sdd.yml`: one `key: value` per line; the first `:` separates them and
everything from the first `#` is a comment. Values are used verbatim — no
unquoting, no variable expansion. If the file is absent, say so and stop — the project has not
adopted this method (`/sdd:adopting-sdd`). If a key this skill needs is absent
or its value is empty, name the key and ask; do not fall back to a default path,
because writing to a guessed location is how a project ends up with two task
queues.


Two outputs, both under `canon`:

- `invariants.md` — the rules. The canonical list; other documents link it.
- `layout.md` — where things live, and what each part owns.

## 1. Read the code, not the docs

Deliberately ignore any existing architecture prose on the first pass — it may
describe an intention the code abandoned. Where the two disagree, the code is
the fact and the disagreement is itself a finding worth reporting.

Cover, in this order:

- **The shape.** Top-level directories, the module/package graph, entry points.
  What depends on what, and what conspicuously does not.
- **The boundaries.** Where does a layer stop? Look for a directory that imports
  narrowly while its neighbours import widely — that asymmetry is usually a rule
  someone is enforcing by hand.
- **The repeated pattern.** The same construction in five places is a
  convention; in twenty, an invariant. Read enough instances to tell which.
- **What is checked mechanically.** Lint config, CI steps, custom scripts,
  codegen, pre-commit hooks. A rule with a checker behind it is the strongest
  kind of invariant and belongs at the top of the list.
- **What the tests assert about structure** rather than behaviour — an
  architecture test, an import-cycle check, a golden file of the public API.
- **The exceptions.** A rule followed in 19 places and broken in the 20th: find
  out which is the mistake. Ask if it is not obvious.

For a large codebase, sample rather than read everything: the entry points, the
two or three busiest modules, the newest module (it shows the current
convention) and the oldest (it shows what changed).

## 2. Draft the invariants

Each candidate gets a bold name and a statement of what must hold, phrased so a
reviewer can decide whether a diff violates it. State the mechanism that
enforces it when one exists; where nothing checks it, say so — that marks it a
convention, and a convention that matters is a candidate for a checker.

A good invariant is **falsifiable and load-bearing**. Test each candidate:

- Could I point at a diff that violates it? If not, it is a value, not a rule.
- Would breaking it be a bug, or just unusual? Only the first is an invariant.
- Is it a consequence of another rule already on the list? Then drop it — a
  canon of forty derived rules is not read.

Prefer eight rules that decide review arguments to thirty that describe the
code. Restating what the language or framework already enforces is filler.

**Cut to fifteen before presenting, not after.** Draft as many candidates as the
evidence supports, then rank them: mechanically enforced rules first, then the
ones whose violation would be a bug, then the rest. Present at most fifteen. The
surplus is not discarded silently — list the cut candidates in one line each
under the proposal, so the operator can pull one back. A canon nobody finishes
reading is not consulted in the review where it would have mattered.

## 3. Confirm with the operator

Present the candidates as a numbered list, one line each, in the order you would
put them in the file, and say which are mechanically enforced. Ask the operator
to strike what they disagree with and name what is missing — they know the rules
that live only in their head, which is exactly what this exercise is for.

Flag separately, and do not fold into the list:

- **Contradictions** — the code does X here and not-X there.
- **Code/doc disagreements** found despite step 1.
- **Rules you suspect are accidents** rather than decisions.

## 4. Write the canon

Write into the `invariants.md` that adoption already placed under `canon` —
it carries the header and the instructions, and you are filling its body. Keep
its shape: the numbered list, then the per-layer table where the codebase has
layers. **Numbers are stable** — other documents cite them, so append new rules
at the end rather than renumbering.

If that file is absent, the project has not been adopted; run
`/sdd:adopting-sdd` first rather than creating the file here.

`layout.md` says where things live: a directory map with one line of purpose
each, the entry points, and where a newcomer should start reading. Not a file
listing — a reader who wants files runs `ls`.

Both files state what is true now. No history, no "we used to" — that belongs in
an ADR.

## 5. When there is nothing to find

A codebase can genuinely have no discernible rules: too new, too small, or
inconsistent enough that any statement would be a wish. Say so plainly and write
nothing. A speculative invariants list is worse than an empty one — it gets
linked, cited, and defended in review as if it had been observed.

The honest output in that case is a short note in `invariants.md` saying the
canon is not yet established, and a suggestion of the two or three rules worth
adopting deliberately as the codebase grows.

## Re-running

This skill is repeatable and expected to be re-run when the code has drifted.
On a re-run, read the existing `invariants.md` **after** the code pass, then
report three lists: rules still held, rules the code no longer obeys, and rules
now present that are undocumented. Do not silently rewrite the file — a rule
that the code stopped obeying may mean the code regressed, not that the rule
expired, and only the operator can say which.
