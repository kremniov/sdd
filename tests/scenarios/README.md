# Method scenarios

These cases test decisions and actions, not exact wording. Each file separates
initial state and user input from evaluator expectations. They are English,
versioned inputs for comparing instruction revisions.

## Procedure

1. Create a disposable repository with the case's stated files and history.
   Use synthetic data and local remotes. Never use a live project for mutations.
2. Supply the target agent the candidate skills, resident rules, initial state
   and user messages. Keep evaluator sections out of its input.
3. Deliver continuation messages only at the point the case specifies.
4. Record messages, commands, changed files, commits and pauses. Compare these
   with the evaluator section; judge equivalent behavior equally.
5. Save the revision, harness/model, inputs, result and evidence paths under
   ignored `docs/stuff/eval-runs/<run>/`. Report pass, fail or not run per case.

A textual walkthrough checks whether instructions support each expected action.
Label it `walkthrough`; it is not an observed agent run. Automated structure and
word counts do not establish scenario success. Author-side evaluations do not
replace the independent review started by the user.

Track missing actions, unnecessary approval requests, invented decisions,
retained context, artifact completeness and loaded instruction size. Keep the
same fixture and messages when comparing revisions.

For commit scenarios, inspect tool-event order as well as Git history: separate
commits made after all edits do not prove step-by-step execution. Verify status
files after completed steps. Response-only probes cannot establish file changes,
commits or actual merge behavior; label their conclusions accordingly.
