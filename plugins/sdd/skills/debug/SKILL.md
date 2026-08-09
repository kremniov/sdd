---
name: debug
description: Use on any bug, test failure or unexpected behaviour, before proposing a fix — find the root cause first, reproduce it in a failing test, and question the architecture once three fixes have failed.
---

# Systematic Debugging

Find the cause before changing anything. A fix aimed at a symptom moves the bug
rather than removing it, and the next person pays for it.

This applies at every tier, including a one-file change.

## 1. Investigate

- **Read the error completely** — the whole stack trace, the line numbers, the
  codes. It often names the answer.
- **Reproduce it.** Exact steps, every time. If it will not reproduce, gather
  data; do not guess from one occurrence.
- **Check what changed.** `git log` / `git diff` on the modules involved, recent
  schema changes, new config keys, a dependency bump.
- **Instrument the boundaries** when more than one component is in play. Log what
  enters and what leaves each one, run it once, and let the evidence say which
  boundary breaks. Then investigate that one.
- **Trace the bad value backwards** to where it originates — what passed it in,
  and what passed it to that. Fix it at the source. A frequent shape: a zero
  value that was harmless until something started reading it.

## 2. Compare against what works

Find the nearest working example in the repo — the sibling handler, the other
adapter, the module that does the same thing correctly. List every difference,
including the ones that "cannot matter". Read the reference implementation
completely rather than skimming it.

## 3. Hypothesize, then test one thing

State it in one sentence: *X is the cause, because Y*. Make the smallest change
that would prove it, one variable at a time. If it does not work, form a new
hypothesis — do not stack another fix on top of it. When you do not understand
something, say so plainly instead of proceeding as if you do.

## 4. Fix the cause

- **Reproduce it in a test first**, at the level the bug lives at — the
  test-first rule in the project's rules file, where the red run is the
  reproduction itself.
- **One change.** No "while I'm here" improvements bundled in.
- **Verify**: the new test passes, nothing else broke, and the original
  behaviour is actually gone. Run the commands and read the output before saying
  it is fixed.

**Three failed fixes means the architecture is the problem.** Not a fourth
attempt. The pattern is recognizable: each fix reveals fresh coupling somewhere
else, or demands a refactor to be implementable, or breaks something new. Stop
and take it to the operator as an architectural question — that is a different
conversation from a failed hypothesis.

## Rationalizations that mean stop

| Thought | What is actually true |
|---|---|
| "Quick fix now, investigate later" | The first fix sets the shape. Later never comes. |
| "It's probably X, let me change it" | Seeing a symptom is not understanding a cause. |
| "Let me change these two things and rerun" | Then you cannot tell which one mattered. |
| "Too simple to need this" | Simple bugs have causes too, and finding them is quick. |
| "No time for the process" | Guess-and-check is slower, and it is how three fixes fail. |
| "One more attempt" (after two) | Three failures is the architecture, not the hypothesis. |
| "The reference is long, I'll adapt it" | Partial understanding is where the next bug comes from. |

## When there is genuinely no cause to find

Sometimes the answer is environmental, timing-dependent, or in someone else's
system. Then: write down what you ruled out, implement the handling that fits
(retry, timeout, an error the caller can act on), and add the logging that would
make the next occurrence diagnosable. Reach for this only after the
investigation is done — most "no root cause" is an investigation that stopped
early.
