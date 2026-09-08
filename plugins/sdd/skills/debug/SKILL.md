---
name: debug
description: Investigate a bug or failed check, test causal hypotheses and verify an approved fix. Stop a series after three failed fixes to discuss the evidence.
---

# Debug

## Scope

Read the request, observed failure, relevant code, checks and recent changes.
If the request is diagnosis only, return findings without implementing a fix.
For a requested fix, use `/sdd:work` to approve the concrete change before editing
project files. Investigation does not require an implementation decision first.

## Investigate

Reproduce the failure or collect observations that can distinguish its cause.
Read the full error and trace the incorrect value through relevant boundaries.
Compare with a working path where one exists. Collect temporary diagnostics in
a disposable environment; project instrumentation is a proposed change.

State a hypothesis and the evidence for it. Choose the smallest experiment that
can distinguish it from alternatives. Evaluate the result before the next
experiment. A rejected hypothesis is not itself a failed fix.

When reproduction is intermittent or unavailable, state what is known and what
additional observation is needed. Environmental or external behavior is a
possible cause, not a reason to invent one. Propose handling only when the
observations support it.

## Fix and verify

Present the concrete fix, assumptions and verification through `/sdd:work`.
After approval, observe an appropriate test fail for the intended reason before
the fix. For changes without testable behavior, use a suitable structural or
manual check. Keep unrelated improvements outside the fix.

Check that the reproduction is resolved and run relevant regression checks and
required project checks. Report the commands, completed results and remaining
uncertainty. Commit the verified fix as part of its step.

After three failed fixes, stop the series. Report the attempts, evidence and
options to the user before another fix. Architecture reassessment is an option;
the count alone does not establish an architectural cause. Use `/sdd:work` stop
conditions when new evidence changes an agreed decision or access is missing.
