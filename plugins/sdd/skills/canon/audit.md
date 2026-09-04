# Audit a canon

Run this when the list is suspected stale. It costs hours and reads the codebase.

Read the code first and the list second. Reading the list first is how a reader
talks themselves into seeing rules that have lapsed.

Where an entry's *Detect* is runnable, run it and report what it printed. That is
the cheapest evidence in the procedure, and the only kind the user can check
without re-reading the code behind you.

## Report four lists, and write nothing without confirmation

| List | Meaning |
|---|---|
| Held | Still true, and described accurately |
| Drifted | The rule holds; its entry lies. A *Detect* naming a checker that has since grown or been replaced, an *On violation* promising an alert that is a log line, a header calling the list hand-checked while three checkers enforce parts of it |
| Broken | The code disobeys. State how many violations and whether they cluster. Broken in one new module is a regression; broken in nine is a rule that expired unrecorded |
| Undocumented | Rules the code now holds that the list omits |

The user decides each one. A rule the code stopped obeying may mean the code
regressed, and only they can say which. Retiring a rule that was merely being
violated launders a bug into a policy.

## An inherited list

A list that came from another method drifts in a way of its own. Its rules are
usually sound and carry no *Detect* and no *On violation*, because whatever wrote
them asked for neither. Propose the two missing lines per entry and leave the
rule alone.

Where you cannot say how a violation would surface, say that. The answer is worth
more than a plausible sentence, because it usually names the rule nobody has been
enforcing.

## The other harvest

An audit reads the whole codebase, so it finds things that are not invariants: a
package with no files, a dependency declared and never used, a task that outlives
what started it. Keep them out of the four lists and out of the conversation,
which ends when the session does. Name them in a short section of their own and
offer to file them through `/sdd:tasks`.
