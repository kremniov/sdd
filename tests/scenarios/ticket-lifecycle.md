# Execute, block and resume a concrete ticket

The approved plan has independent preparation and a dependent export. At first
start, require T-42 inprogress in the queue before performing the work. Create
preparation.md with the exact approved content, check and commit it even though
external/customers.json is missing. Then record blocked and the concrete missing
file when no independent authorized work remains. Do not replace queue status
with notes alone. Inspect intermediate file/tool states, not just final tags.

Supply the input only after that gate. On resume require inprogress, preserve
the preparation commit without redoing the step, run export.py and configured
verify.py, and inspect output record equality plus fixture timestamp. Keep local
input/output and status outside Git. The ticket stays inprogress at handover;
there is no integration permission. Preserve the historical T-41 entry.
