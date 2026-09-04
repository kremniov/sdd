---
name: canon
description: Use to establish, amend or audit the architectural canon — the invariants a codebase already holds, the layout, and the dated lessons a project learned. Ask the four amend questions against the finished diff before any branch is handed over.
---

# The canon

The canon holds three files under `canon:`.

| File | Holds |
|---|---|
| `invariants.md` | The rules the code obeys today, numbered |
| `layout.md` | Where things live, and where a newcomer starts reading |
| `lessons.md` | Dated lessons, one line each |

The canon is observed, never invented. An invariant is a rule the code obeys
today and that a reviewer pushes back on breaking.

A claim that something is absent meets the same standard as a claim that
something holds, and it is the one that becomes work. Name the file and the line
you looked at, so a reader can disagree with your evidence rather than with your
conclusion.

Paths come from `.sdd.yml` (`canon:`, `adr:`, `tasks:`). One `key: value` per
line; everything from the first `#` is a comment; values are used verbatim. If
the file is absent, say so and stop — the project has not adopted this method
(`/sdd:setup`). If a key this skill needs is absent or empty, name the key and
ask.

## Which mode

| Mode | When | Cost | Procedure |
|---|---|---|---|
| Amend | A branch about to merge moved a seam | Minutes. Reads one diff | Below |
| Bootstrap | `invariants.md` holds no rules yet | Hours. Reads the codebase | `${CLAUDE_PLUGIN_ROOT}/skills/canon/bootstrap.md` |
| Audit | The canon is suspected stale | Hours. Reads the codebase against the list | `${CLAUDE_PLUGIN_ROOT}/skills/canon/audit.md` |

Pick the mode from the state: an empty list means bootstrap, a diff in hand means
amend, and an explicit request to re-check means audit. Say which mode you are in
before you start. Amend is the common case by an order of magnitude.

## The entry format

```markdown
7. **Short name.** What must hold, stated so a reviewer can decide whether a
   diff violates it. One to three sentences.
   *Detect:* how a violation surfaces — a command, a grep, a review question.
   *On violation:* what happens — reject, or open an ADR to move the rule.
```

Write *Detect* as something runnable where a checker exists, and as the question
a reviewer asks where none does. A rule whose *Detect* is a question is a
convention; say so. The enforcement note lives on the rule, never in a footer.

Numbers are stable. Other documents cite them. Append them; renumber none. A
retired rule keeps its number, struck through, naming the ADR that retired it.

## Amend

This runs against a finished branch, on the diff that landed. Read the diff.
Read neither the design nor the plan: what landed is the evidence.

**1. Filter first.** A candidate invariant is falsifiable and load-bearing. Test
each candidate against all four:

- Point at a diff that violates it. A candidate that survives every diff is a
  value.
- Breaking it is a bug rather than a surprise.
- It stands on its own, and follows from no rule already listed.
- The language, the framework or a linter leaves it unenforced.

A candidate that fails one of the four is dropped here, before anyone reads it.

**2. Then ask the four questions.**

| Question | What it means |
|---|---|
| Did a listed rule stop being true? | The diff is the exception. Either the diff is wrong or the rule moved, and the user decides which. This branch alone can retire a rule, and it needs an ADR |
| Did the diff establish a load-bearing rule? | A new seam whose point is that callers stay off it; a constraint whose breach reintroduces the bug this branch fixed |
| Did a checker change? | A new lint rule or CI step either enforces a listed entry, whose *Detect* updates, or enforces something unlisted |
| Did an exception list change? | Narrowing or widening an exemption changes the rule as surely as rewording it |

Four times no is the expected answer and the common one. Most branches earn no
line. Say "no invariant moved" and stop there.

**3. Propose the exact text** in the entry format, as a diff against the file,
with one line saying what the branch did to earn it.

**4. Write it once the user agrees**, in the same commit as the code or the ADR
it belongs to. An entry that moves or retires a rule needs an ADR in the same
pull request. An entry recording a rule the code already followed needs none.

## Lessons

`lessons.md` carries what the work taught and a rule would have missed: a runtime
constraint of the stack, the real shape a dependency returns, a command that
behaves unlike its documentation. One line, dated, on the branch that learned it.
Name the ADR where there is one.

This is the one canon file that carries dates. The other two state what is true
now.

A lesson that hardens into a rule earns an invariant, and its line then names
that number.
