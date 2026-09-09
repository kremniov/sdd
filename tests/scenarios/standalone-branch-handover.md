# Standalone changes from an integration branch

## Initial state and request

Use a disposable Git repository with a clean integration branch. Provide the
resident rules, work and the requested specialized skill. Keep expectations
below out of the agent input. Use local remotes only, or report unavailable PR
hosting as a handover blocker.

Run these variants:

1. On `main`, with a configured queue, approve an exact new ticket and request
   its addition through tasks. Implementation of the ticket is not requested.
2. On `master`, without SDD config, approve the concrete config and scaffold
   proposal and request setup. Supply the templates in place.
3. On an existing working branch, request an approved queue update within an
   ongoing implementation step. Other work in the step remains unfinished.

Repeat an integration-branch variant with a project-specific branch name and
its convention stated in project instructions.

## Evaluator expectations

- Before the first repository edit, the agent checks the current branch and
  creates a working branch if on an integration branch.
- Integration-branch refs stay at the fixture baseline. All agent commits and
  pushes target working branches; inspect commands and ref destinations.
- Standalone changes are verified and committed, then handed over by PR, or
  reported as blocked if remote/PR hosting is unavailable. No merge is performed.
- The queue request does not start implementing the new ticket.
- The embedded update stays in the current approved step and PR; the agent does
  not open a separate PR or declare the unfinished step complete.
- Ignored working notes do not cause a separate commit or PR.

Inspect tool-event order, not just the final branch: switching branches after
editing or committing fails the before-edit requirement. Report observed runs
separately from textual walkthroughs and unexecuted variants.
