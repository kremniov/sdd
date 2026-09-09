# <Feature> — plan

**Design:** [design.md](design.md)

<!--
Write beside the approved design. Keep applicable headings; omit empty sections.
Budget: at most 400 lines. Replace guidance and examples with the actual plan.
-->

## Scope

State the result delivered by this plan and link the agreed design.

## Order

Explain dependencies that determine the sequence. Identify independent steps.

## Steps

### Step N — <observable result>

**Result:** <what becomes true>

**Constraints:** <links to agreed decisions and rules>

**Touches:** <components and files>

**Check:** <command and expected result, or manual procedure, observation and owner>

<!--
Example: import valid rows despite rejected rows.
Constraints: the agreed per-row outcome contract in design.md.
Touches: the importer and result presentation.
Check: mixed-validity input imports valid rows and lists each rejected row with
its reason; required project checks pass.

A step can contain several commits. Commit the verified result before the next
step. Mark a required human action [gate] and specify what is needed.
-->

## Final verification

Run the configured verify command after code and document changes. State any
additional checks and who runs manual verification.

## Documents and decisions

Link the canon updates and ADRs required in this PR. Assign them to steps above.
