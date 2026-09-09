# Audit a canon

Read each rule, its detector, the relevant code and primary obligations. Run
runnable detectors and inspect their scope. For manual detectors, answer the
review question with concrete evidence. Record sampling limits and checks that
could not run.

| Finding | Meaning |
|---|---|
| Held | The rule and its description match the evidence |
| Drifted | The obligation holds, but its description or detector is inaccurate |
| Broken | Code violates the rule; give locations and consequences |
| Undocumented | Evidence supports a current rule missing from the list |

Apply the candidate filter in `SKILL.md` to undocumented rules. A high violation
count does not authorize retirement. Present correction or rule-change options
to the user. Change the canon only after agreement.

For an inherited list, preserve supported rules and propose missing Detect or
On violation fields. State uncertainty where enforcement cannot be established.
Keep unrelated maintenance findings in a separate report section; offer to file
them through `/sdd:tasks`. Do not start those tasks during an audit.
