---
name: tasks
description: Use when adding, editing or closing an item in the project's task queue — writing a ticket for a feature, bug, tech-debt or chore, allocating its id, updating its status, or collapsing it to Done at merge.
---

# The task queue

The queue is the "what do I pull next" list. Its path and the ticket-id prefix
come from `.sdd.yml` (`tasks:` and `ticket:`). One `key: value` per line;
everything from the first `#` is a comment; values are used verbatim. If the file
is absent, say so and stop — the project has not adopted this method
(`/sdd:setup`). If a key this skill needs is absent or empty, name the key and
ask.

A ticket states the outcome and how anyone knows it is done. It is a pickup
contract: an agent takes it, designs, plans, then executes. Reasoning, history
and option comparisons belong to the feature's `design.md`, written at pickup.

## The ticket

Write exactly these slots, in this order. Drop an optional line that has no real
content.

```markdown
#### `[T-40]` Short imperative title

**Tags:** `[feat]` `[launch]` `[api]` `[someday]`

**Outcome:** One sentence — what becomes true when this is done.

**Acceptance:**

- [ ] A checkable criterion (an observable end-state, not a step)
- [ ] …2–5 total

**Pointers:** deps: T-38 · design: <path> · code: <path>

---
```

| Slot | What closes it |
|---|---|
| Heading | `#### `, the `` `[ID]` ``, and a short imperative title |
| Tags | Their own line, below the heading |
| Outcome | The end-state in one sentence. The motivation stays out |
| Acceptance | Two to five boxes, each one tickable by observing the result |
| Pointers | Real references only. The whole line is optional |
| `---` | A thematic break closes each ticket |

Blank lines are mandatory between the heading, each `**Label:**` paragraph, and
around the `- [ ]` list. CommonMark otherwise glues `**Pointers:**` into the
acceptance list. Keep the blank line before `**Pointers:**` and around the
trailing `---`.

## Tags and ids

Tags are bracketed and live on the `**Tags:**` line, so `grep '\[api\]'` filters
the queue; `-B2` pulls in the heading. Order them **type · phase · area ·
status**.

| Group | Values |
|---|---|
| type | `[feat]` `[bug]` `[debt]` `[chore]` |
| phase | project-specific — the roadmap's phase names |
| area | project-specific — one per subsystem, several where the work is cross-cutting |
| status | `[next]` `[in-progress]` `[blocked]` `[someday]` |

Ids are stable and reused never. A new item takes the next free number with the
prefix from `.sdd.yml`. Grep the whole file to find it —
`grep -o '\[T-[0-9]*\]' <tasks> | sort -t- -k2 -n | tail -1` — and take one past
the highest. Scanning the TODO section alone is how duplicates happen: a higher
id usually sits in Done, collapsed to one line. A `deps:` reference has to
survive forever, so renumber nothing.

## Moving to Done

The Done move records the user's approval to integrate, so it comes after that
word and never before it. `/sdd:work` carries the rule.

Collapse the ticket to one line and swap the status tag for a ref tag —
`[PR #N]`, `[branch-name]` or `[commit-hash]`. Acceptance is dropped, because git
remembers. Keep the type, phase and area tags.

```markdown
- `[T-40]` `[feat]` `[launch]` `[api]` `[PR #91]` Title — one-sentence result.
```

That same commit fills the `PR:` field of any ADR the branch left as a dash. It
is the last chance: nothing after it lands on the branch.

## What a ticket leaves out

| Out of the ticket | Where it goes |
|---|---|
| Why, motivation, rationale | the feature's `design.md` |
| History — "found during X", "as we discussed" | git and the pull request carry it |
| Option comparisons | `design.md`, decided at pickup |
| Implementation narrative | the plan, at pickup |

## Example

Watery:

> …the importer rejects the whole file when one row fails validation, so a
> 10,000-row upload dies on a typo in row 3. Noticed while debugging a support
> ticket last week. **Go with option 2 = per-row outcomes**, not option 1
> (fail-fast with a better message) — users need the good rows to land, and
> partial success is what every comparable tool does. Once it lands we should
> probably revisit the batch size too, though that is a separate concern…

Ticket:

```markdown
#### `[T-39]` Partial success on bulk import

**Tags:** `[feat]` `[import]` `[next]`

**Outcome:** A bulk import applies every valid row and reports the rejected ones.

**Acceptance:**

- [ ] Valid rows are committed when others fail validation
- [ ] The response lists each rejected row with its reason
- [ ] A file where every row fails returns a non-2xx status

**Pointers:** deps: T-38

---
```

## Before saving

- Every sentence is tickable or a pointer. A line that only explains why is cut.
- Every acceptance box is an observable end-state, not a verb like "investigate".
- A new item carries the next free number, confirmed unused.
- A Done item is one line with a ref tag.
