---
name: tasks
description: Add, clarify or close tickets in the project queue, preserving context, stable IDs and the agreed integration status.
---
 # Tasks

Before creating or editing tracked files, follow `/sdd:work` Branch and
completion before editing and when handing over the result.

## Inputs and scope

Read the request and the `.sdd/config.yml` values `tasks`, `tasks_done`,
`tickets` and `ticket`. If the config or a required value is absent, or the
project still has `.sdd.yml`, offer `/sdd:setup`.

When `tickets` is set, each ticket is a file `<tickets><ID>.md`, and
`.sdd/tasks-index` generates two indexes from these files: `tasks` lists open
tickets and `tasks_done` lists closed tickets. Read the open index to find work
and dependencies. Read `tasks_done` only when the request concerns closed work.
Read a ticket file when the request concerns that ticket. Never edit an index
by hand.

When `tickets` is absent, the queue is the single file `tasks`. Preserve its
fields, structure, labels, ID conventions and completed entries. Map method
states to project statuses. If required content or a state has no unambiguous
representation, propose a concrete addition and agree it before changing the
format. `/sdd:setup` can convert this queue to ticket files.

Give a new ticket the next number after the highest existing ID: the ticket
file names, or every entry of a single-file queue, including completed entries.
Use the configured prefix. Never reuse or renumber IDs. Preserve valid
dependency references. A request to file a task does not authorize
implementation. Use `/sdd:work` for approval of proposed edits and for
integration timing.

## Write a ticket

Write the ticket file in this shape. Keep blank lines between fields and around
lists. Omit Context or Pointers when unnecessary.

```markdown
---
type: feat
phase: launch
areas: [billing]
status: next
group: Billing
---

# T-40: Recovery export

**Outcome:** A recovery export contains a consistent restorable snapshot.

**Context:** The export supports disaster recovery, so cross-record consistency
is required. Implementation choices remain open.

**Acceptance:**

- [ ] Restoring the export preserves the recorded relationships
- [ ] An incomplete export is reported as failed

**Pointers:** requirements: <source> · deps: T-38
```

The frontmatter is a restricted subset of YAML: one `key: value` per line, only
the keys below, a list as `[a, b]`, and a value in double quotes when it
contains `#` or `: `, starts with punctuation, or is a YAML keyword such as
`yes` or `null`. A quoted value contains no `"` or backslash. `.sdd/tasks-index`
rejects anything outside this subset and reads every value as text. A YAML
parser reads the same text, but can type a bare number or the closing date.

| Key | Value |
|---|---|
| `type` | `feat`, `bug`, `debt` or `chore` |
| `phase` | A project phase; optional |
| `areas` | Project area names; optional |
| `status` | `next`, `in-progress`, `blocked`, `someday` or `done` |
| `group` | The index heading while the ticket is open; optional |
| `closed` | The closing date, `YYYY-MM-DD`; closed tickets only |
| `ref` | The PR, branch or commit that closes the ticket; closed tickets only |

A title is a short noun phrase that names the work or, for a bug, the symptom,
such as `Duplicate reminder emails`. The Outcome states the target behavior;
the title does not restate it. State the outcome and observable acceptance.
Include the reason or constraint when omitting it would change the task. Link
primary requirements, dependencies and existing code. There is no minimum
criterion count. Leave execution steps for a plan and unsettled implementation
choices for discussion at pickup.

When starting or resuming implementation, set an existing ticket to
`in-progress` or the project equivalent. Include the update in the current
step's implementation commit. Set `blocked` or its project equivalent when an
obstacle prevents continuing the task and no independent authorized work
remains. A blocked part alone does not block the whole ticket. Keep details in
working notes; those notes do not replace the ticket status. Leave closing to
integration. Update an existing ticket; these transitions do not require
creating one.

After each change to a ticket file, run `.sdd/tasks-index` and commit the
indexes with the ticket files.

## Close a ticket

Close after explicit permission to integrate its branch, before merge, as part
of `/sdd:work` Integration. Keep the ticket file, its title, its body and its
other frontmatter keys, `group` included. Set `status: done`, `closed` and
`ref`, and add a Result field after the title:

```markdown
# T-40: Recovery export

**Result:** A recovery export produces a consistent snapshot. See `docs/architecture/export.md`.
```

State the resulting behavior in one or two sentences with its change and
document references. Review history stays in the PR; record a lesson in
`lessons.md` and a decision in an ADR. In a single-file queue, preserve the
project's completed-entry format, retaining the ID, result and a change
reference.

Use a PR, branch or commit reference that exists. In the same final branch
commit, fill missing PR references in its ADRs. A closed ticket on the branch
records integration approval; report actual merge separately. Do not close on
plan approval or merely because implementation checks passed. Resolve known
merge blockers before this commit. If merge later fails, follow `/sdd:work`
Integration: verified repair commits may follow the closing commit; preserve
the published history.

## Check the edit

When `tickets` is set, run `.sdd/tasks-index --check`. Check new IDs against
all tickets, retain necessary context and real references, and inspect the
rendered Markdown structure. A closed ticket must identify its result and
change. Report what changed.
