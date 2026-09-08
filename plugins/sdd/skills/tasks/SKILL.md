---
name: tasks
description: Add, clarify or close entries in the project queue, preserving context, stable IDs and the agreed integration status.
---

# Tasks

For files intended for Git, follow `/sdd:work` Branch and completion before
editing and when handing over the result.

## Inputs and scope

Read the request and `.sdd.yml` values `tasks` and `ticket`. Split each line at
the first colon and remove comments from the first `#`. If configuration is
absent, offer `/sdd:setup`. Ask for required missing values.

Read the whole queue, including completed entries, before choosing an ID. Follow
project ID conventions; for a new queue, use the configured prefix and increasing
numbers. Never reuse or renumber IDs. Preserve valid dependency references. A request to file a task does not authorize implementation.
Use `/sdd:work` for approval of proposed edits and for integration timing.

## Write a ticket

Preserve an existing queue's fields, structure, labels and ID conventions,
including completed entries. Map method states to project statuses. If required
content or a state has no unambiguous representation, propose a concrete addition
and agree it before changing the format.

For a new queue, use the following shape and tag conventions. Keep blank lines
between fields and around lists. Omit Context or Pointers when unnecessary.

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

For a new queue, order tags by type, phase, area and status. Use `[feat]`, `[bug]`, `[debt]` or
`[chore]` for type; use project phase and area names. Status is `[next]`,
`[in-progress]`, `[blocked]` or `[someday]`.

Use the project status equivalent to `[in-progress]` when execution starts or
resumes, and to `[blocked]` when an
obstacle prevents continuing the task and no independent authorized work remains.
A blocked part alone does not block the whole ticket. Keep details in working
notes; those notes do not replace the queue status. Leave Done to integration.
Update an existing ticket; these transitions do not require creating one.

## Close a ticket

Close after explicit permission to integrate its branch, before merge, as part
of `/sdd:work` Integration. Preserve the project's completed-entry format,
retaining the ID, result and a change reference. For a queue using this skill's
format, collapse the entry to one line in Done, newest first. Keep type, phase
and area; drop acceptance and replace the status tag with the reference.

```markdown
- `[T-40]` `[feat]` `[PR #91]` Add a recovery export — produces a consistent snapshot.
```

Use a PR, branch or commit reference that exists. In the same final branch
commit, fill missing PR references in its ADRs. Done on the branch records
integration approval; report actual merge separately. Do not close on plan
approval or merely because implementation checks passed. Resolve known merge
blockers before this commit. If merge later fails, follow `/sdd:work` Integration:
verified repair commits may follow Done; preserve the published history.

## Check the edit

Check IDs against the full queue, retain necessary context and real references,
and inspect the rendered Markdown structure. A completed entry must identify
its result and change. Report what changed without starting the queued work.
