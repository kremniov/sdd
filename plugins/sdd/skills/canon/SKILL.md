---
name: canon
description: Use to establish, amend or audit the architectural invariants — write down the rules a codebase already holds, add one when a merging branch moved a seam or changed a checker, or re-check the list against code that has drifted. Ask before integrating any branch.
---

# The Invariants Canon

Write down the rules this codebase already follows, so later work can link them
instead of rediscovering them. The canon is **observed, not invented**: an
invariant is a rule the code obeys today and that a reviewer would push back on
breaking.

Paths come from `.sdd.yml` (`canon:`).

Reading `.sdd.yml`: one `key: value` per line; the first `:` separates them and
everything from the first `#` is a comment. Values are used verbatim — no
unquoting, no variable expansion. If the file is absent, say so and stop — the
project has not adopted this method (`/sdd:setup`). If a key this skill
needs is absent or its value is empty, name the key and ask; do not fall back to
a default path, because writing to a guessed location is how a project ends up
with two task queues.

## Which mode

| Mode | When | Cost |
|---|---|---|
| **Bootstrap** | `invariants.md` has no rules yet | Hours. Reads the codebase. |
| **Amend** | A branch about to merge moved a seam | Minutes. Reads one diff. |
| **Audit** | The canon is suspected stale | Hours. Reads the codebase against the list. |

Pick from the state, not from the invocation: an empty list means bootstrap; an
uncommitted or unmerged diff in hand means amend; an explicit request to
re-check means audit. Say which mode you are in before starting.

Amend is the common case by an order of magnitude. A canon grows one line at a
time, on the branch that earned the line.

## The entry format

Every invariant is a numbered entry with three parts, in this order:

```markdown
7. **Short name.** What must hold, stated so a reviewer can decide whether a
   diff violates it. One to three sentences.
   *Detect:* how to see a violation — a command, a grep, a review question.
   *On violation:* what happens — reject, or open an ADR to move the rule.
```

The two italic lines are not decoration. An agent reading this file is deciding
one of three things: whether its own diff violates the rule, how hard to push in
review, and whether a new line is owed. *Detect* answers the first, *On
violation* the second, and both together tell it whether the rule is a wall or a
default.

Write *Detect* as something runnable when a checker exists — `make lint`, a test
name, a grep — and as the question a reviewer asks when it does not. A rule
whose *Detect* is only a question is a convention; say so plainly rather than
implying a rigour that is absent. **The enforcement note lives on the rule, not
in a summary at the end of the file.** A footer saying "rules 12–14 are checked
mechanically" goes stale the first time a checker grows, and nothing catches it.

**Numbers are stable.** Other documents cite them. Append; never renumber. A
retired rule keeps its number and is struck through with one line saying which
ADR retired it — a gap in the numbering is cheaper than a citation that now
points at a different rule.

## Bootstrap

### 1. Read the code, not the docs

Deliberately ignore existing architecture prose on the first pass — it may
describe an intention the code abandoned. Where the two disagree, the code is
the fact, and the disagreement is itself a finding worth reporting.

Cover, in this order:

- **The shape.** Top-level directories, the module graph, entry points. What
  depends on what, and what conspicuously does not.
- **The boundaries.** Where does a layer stop? A directory that imports narrowly
  while its neighbours import widely is usually a rule someone enforces by hand.
- **The repeated pattern.** The same construction in five places is a
  convention; in twenty, an invariant. Read enough instances to tell which.
- **What is checked mechanically.** Lint config, CI steps, custom scripts,
  codegen, pre-commit hooks. A rule with a checker is the strongest kind and
  belongs at the top of the list. Read the checker itself: what it actually
  covers is routinely narrower or wider than what the docs claim.
- **What the tests assert about structure** rather than behaviour — an
  architecture test, an import-cycle check, a golden file of the public API.
- **The exceptions.** A rule followed in 19 places and broken in the 20th: find
  out which is the mistake. Ask if it is not obvious.

For a large codebase, sample rather than read everything: the entry points, the
two or three busiest modules, the newest module (it shows the current
convention) and the oldest (it shows what changed).

### 2. Draft

A good invariant is **falsifiable and load-bearing**. Test each candidate:

- Could I point at a diff that violates it? If not, it is a value, not a rule.
- Would breaking it be a bug, or just unusual? Only the first is an invariant.
- Is it a consequence of another rule already listed? Drop it — a canon of forty
  derived rules is not read.
- Does the language or framework already enforce it? Then it is filler.

**Cut to fifteen before presenting, not after.** Rank: mechanically enforced
first, then those whose violation is a bug, then the rest. Present at most
fifteen, and list the cut candidates in one line each underneath so the operator
can pull one back. A canon nobody finishes reading is not consulted in the
review where it would have mattered.

### 3. Confirm

Present the candidates as a numbered list, one line each, in file order, marking
which are mechanically enforced. Ask the operator to strike what they disagree
with and name what is missing — they know the rules that live only in their
head, which is what this exercise is for.

Flag separately, never folded into the list:

- **Contradictions** — the code does X here and not-X there.
- **Code/doc disagreements** found despite step 1.
- **Rules that look like accidents** rather than decisions.

### 4. Write

Fill the body of the `invariants.md` that adoption placed under `canon`, in the
entry format above. If that file is absent the project has not been adopted —
run `/sdd:setup` rather than creating it here.

`layout.md` says where things live: a directory map with one line of purpose
each, the entry points, and where a newcomer starts reading. Not a file listing
— a reader who wants files runs `ls`.

Both files state what is true now. No history, no "we used to" — that belongs in
an ADR.

### 5. When there is nothing to find

A codebase can genuinely have no discernible rules: too new, too small, or
inconsistent enough that any statement would be a wish. Say so and write
nothing. A speculative list is worse than an empty one — it gets linked, cited,
and defended in review as if it had been observed.

The honest output is a short note in `invariants.md` saying the canon is not yet
established, plus two or three rules worth adopting deliberately as the codebase
grows.

## Amend

Runs against a branch that is finished and about to merge — the same moment the
docs discipline and the ADR trigger are checked, and for the same reason: before
the code exists a rule is an intention, and a design that promised to move an
invariant does not always turn out to have moved it.

**1. Read the diff, then ask the four questions.** Not the design, not the plan
— the diff. What actually landed is the only evidence that a rule changed.

- **Did a rule on the list stop being true?** The diff is the exception that
  breaks it. Either the diff is wrong, or the rule moved — and which one is the
  operator's call, never yours. This is the only branch that can retire a rule,
  and it needs an ADR.
- **Did the diff establish a rule that is now load-bearing?** A new seam whose
  whole point is that callers must not cross it; a constraint that, once broken,
  reintroduces the bug this branch fixed. Apply the falsifiability tests above
  before proposing it.
- **Did a checker change?** A new lint rule or CI step either enforces an
  existing entry — update its *Detect* — or enforces nothing on the list, which
  is a rule someone codified without writing down.
- **Did a rule's exception list change?** Narrowing or widening an exemption
  changes the rule as surely as rewording it.

If all four are no, say so and stop. Most branches earn no line. Saying "no
invariant moved" is a real answer and the common one — do not manufacture an
entry to justify having looked.

**2. Propose the exact text**, in the entry format, as a diff against the file.
One line each for what changes and why the branch earned it.

**3. Write it after the operator agrees**, in the same commit as the code or
the ADR it belongs to — never as a standalone docs commit. A canon entry
separated from the change that caused it loses the only evidence a later reader
has for why the rule exists.

An entry that moves or retires an existing rule needs an ADR in the same PR.
Adding a rule the code already followed does not: nothing changed, it was merely
unwritten.

## Audit

Read the code first, the existing list second — same discipline as bootstrap,
because reading the list first is how you talk yourself into seeing rules that
have quietly lapsed.

Report three lists and write nothing without confirmation:

- **Held** — still true. Note where *Detect* has drifted from what the checker
  now does.
- **Broken** — the code no longer obeys. State how many violations and whether
  they cluster; a rule broken in one new module is a regression, a rule broken
  in nine is a rule that expired without anyone recording it.
- **Undocumented** — rules the code now holds that the list does not carry.

The operator decides each. A rule the code stopped obeying may mean the code
regressed, not that the rule expired, and only they can say which — retiring a
rule that was merely being violated launders a bug into a policy.
