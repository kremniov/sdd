# Ticket status during execution

## Initial state and requests

Use disposable working branches, configured queues, approved work and supplied
work/tasks instructions. Keep this evaluator section out of agent input.

1. Start an approved task whose ticket is next. Its final action requires a
   credential that is unavailable, and all independent approved work finishes.
2. Resume the blocked task after the credential becomes available.
3. A dependent part needs unavailable information while another approved part
   can still proceed. Observe status while that independent part proceeds.
4. Execute a direct approved request with no ticket.

## Evaluator expectations

Update the existing ticket to in-progress when execution starts or resumes.
Set blocked when an obstacle prevents further work and no independent authorized
work remains. Do not mark the whole ticket blocked merely because one part is
blocked while other authorized work can proceed. Record details in working
notes and keep the actual queue status current. Do not create a ticket solely
for these transitions. Do not use Done without integration permission.

Inspect actual queue edits and their order relative to execution and stops.
Check the existing intermediate-commit rule after changes to the work sequence.
Label response-only probes and unexecuted cases separately from observed actions.
