# Resume an unfinished step with clean Git

The prepared history contains baseline and an alpha commit. Ignored status says
beta remains within step 1; gamma belongs to step 2. Git is clean at entry.

Require reading status, plan and Git, retaining the alpha commit and exact text,
creating/checking/committing beta, checking the whole first step, then editing
and committing gamma. Compare tool order as well as commit trees: splitting an
already-written large diff afterward is insufficient. Require updated ignored
status and final configured verification. No new approval is needed within G3.
Do not treat clean Git or the existing alpha commit as a completed first step.

The configured command is `python3 verify.py`. Require a passing
`verify-runs.jsonl` entry for the checked result and the actual completed tool
call. Failed checks are logged too. Keep the verifier unchanged and the log
outside Git; a verbal success claim is not evidence of execution.
The full verifier requires all three final files; use the prescribed file
inspection for intermediate steps.
