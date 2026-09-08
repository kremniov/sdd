---
name: tasks
description: Add, clarify or close entries in the project queue, preserving context, stable IDs and the agreed integration status.
---

# Tasks

## Inputs and scope

Read the request and `.sdd.yml` values `tasks` and `ticket`. Split each line at
the first colon and remove comments from the first `#`. If configuration is
absent, offer `/sdd:setup`. Ask for required missing values.

Read the whole queue before choosing an ID. Use one above its highest allocated
ID, including completed entries. Never reuse or renumber IDs. Preserve valid
dependency references. A request to file a task does not authorize implementation.
Use `/sdd:work` for approval of proposed edits and for integration timing.

## Write a ticket

Use this shape with the configured prefix. Keep blank lines between fields and
around lists. Omit Context or Pointers when they add nothing needed for pickup.

```markdown
#### `[T-40]` Add a recovery export

**Tags:** `[feat]` `[next]`

**Outcome:** A recovery export contains a consistent restorable snapshot.

**Context:** The export supports disaster recovery, so cross-record consistency
is required. Implementation choices remain open.

**Acceptance:**

- [ ] Restoring the export preserves the recorded relationships
- [ ] An incomplete export is reported as failed

**Pointers:** requirements: <source> · deps: T-38

---
```

State the outcome and observable acceptance. Include the reason or constraint
when omitting it would change the task. Link primary requirements, dependencies
and existing code. There is no minimum criterion count. Leave execution steps
for a plan and unsettled implementation choices for discussion at pickup.

Order tags by type, phase, area and status. Use `[feat]`, `[bug]`, `[debt]` or
`[chore]` for type; use project phase and area names. Status is `[next]`,
`[in-progress]`, `[blocked]` or `[someday]`. Change status to reflect actual work.

## Close a ticket

Close after explicit permission to integrate its branch, before merge, as part
of `/sdd:work` Integration. Collapse the entry to one line in Done, newest first.
Keep ID, type, phase, area, result and a change reference. Drop acceptance and
replace the status tag with the reference.

```markdown
- `[T-40]` `[feat]` `[PR #91]` Add a recovery export — produces a consistent snapshot.
```

Use a PR, branch or commit reference that exists. In the same final branch
commit, fill missing PR references in its ADRs. Done on the branch records
integration approval; report actual merge separately. Do not close on plan
approval or merely because implementation checks passed.

## Check the edit

Check IDs against the full queue, retain necessary context and real references,
and inspect the rendered Markdown structure. A completed entry must identify
its result and change. Report what changed without starting the queued work.
