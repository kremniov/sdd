---
name: debug
description: Use on any bug, test failure or unexpected behaviour, before proposing a fix — find the root cause, reproduce it in a failing test, and question the architecture once three fixes have failed. Applies at every tier, including a one-file change.
---

# Systematic debugging

Find the cause before changing anything. A fix aimed at a symptom moves the bug,
and the next person pays for it.

This applies at every tier, including a one-file change.

## 1. Investigate

- **Read the error completely** — the whole stack trace, the line numbers, the
  codes. It often names the answer.
- **Reproduce it.** Exact steps, every time. Where it will not reproduce, gather
  data instead of guessing from one occurrence.
- **Check what changed.** `git log` and `git diff` on the modules involved,
  recent schema changes, new config keys, a dependency bump.
- **Instrument the boundaries** when more than one component is in play. Log what
  enters and what leaves each one, run it once, and let the evidence name the
  boundary that breaks. Then investigate that one.
- **Trace the bad value backwards** to where it originates: what passed it in,
  and what passed it to that. Fix it at the source. A frequent shape is a zero
  value that stayed harmless until something started reading it.

## 2. Compare against what works

Find the nearest working example in the repository — the sibling handler, the
other adapter, the module that does the same thing correctly. List every
difference, the ones that "cannot matter" included. Read the reference
implementation completely; a partial reading is where the next bug comes from.

## 3. Hypothesize, then test one thing

State it in one sentence: *X is the cause, because Y*. Make the smallest change
that proves it, one variable at a time. Where it fails, form a new hypothesis
instead of stacking a second fix on the first. Where you do not understand
something, say so plainly.

## 4. Fix the cause

- **Reproduce it in a test first**, at the level the bug lives at. The red run is
  the reproduction.
- **One change.** Bundle no "while I am here" improvements with it.
- **Verify.** The new test passes, nothing else broke, and the original behaviour
  is gone. Run the commands and read the output before saying it is fixed.

## Three failed fixes means the architecture is the problem

Not a fourth attempt. The pattern is recognizable: each fix reveals fresh
coupling somewhere else, or demands a refactor to be implementable, or breaks
something new.

Stop and take it to the user as an architectural question. That is a different
conversation from a failed hypothesis.

## When there is genuinely no cause to find

Some answers are environmental, timing-dependent, or in someone else's system.
Then write down what you ruled out, implement the handling that fits — a retry, a
timeout, an error the caller can act on — and add the logging that makes the next
occurrence diagnosable.

Reach for this after the investigation, never instead of it.
