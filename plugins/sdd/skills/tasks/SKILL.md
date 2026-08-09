---
name: tasks
description: Use when adding, editing, or closing an item in the project's task queue — writing a ticket for a feature, bug, tech-debt or chore, allocating its id, updating its status, or collapsing it to Done at merge.
---

# The Task Queue

The task queue is the "what do I pull next" list. Its path and the ticket-id
prefix are in `.sdd.yml` (`tasks:` and `ticket:`); read them before editing.

Reading `.sdd.yml`: one `key: value` per line; the first `:` separates them and
everything from the first `#` is a comment. Values are used verbatim — no
unquoting, no variable expansion. If the file is absent, say so and stop — the project has not
adopted this method (`/sdd:setup`). If a key this skill needs is absent
or its value is empty, name the key and ask; do not fall back to a default path,
because writing to a guessed location is how a project ends up with two task
queues.


A **ticket** states the outcome and how you'll know it's done — nothing else.
Reasoning, history, and option-comparisons live in the feature's `design.md`,
written when the task is picked up. A ticket is a pickup contract, not a design
doc: an agent takes it → runs brainstorming → design → plan.

## The ticket

Write exactly these slots, in this order. Omit optional lines when they have no
real content — never pad.

```markdown
#### `[T-40]` Short imperative title

**Tags:** `[feat]` `[launch]` `[api]` `[someday]`

**Outcome:** One sentence — what becomes true when this is done.

**Acceptance:**

- [ ] A checkable criterion (an observable end-state, not a step)
- [ ] …2–5 total

**Pointers:** deps: T-38 · design: <path> · code: <path>   ← only real ones, whole line optional

---
```

- **Heading** — `#### ` + the `` `[ID]` `` + a short imperative title. Tags go on
  their own `**Tags:**` line below, not inline.
- **Outcome** — the end-state in one sentence, not the motivation.
- **Acceptance** — 2–5 boxes. Each is something you can tick by observing the
  result. If you can't check it, it's not acceptance — it's a wish or a step.
- **`---`** — a thematic break closes each ticket and separates it from the next.

**Blank lines are mandatory** between the heading, each `**Label:**` paragraph,
and around the `- [ ]` list — CommonMark otherwise glues `**Pointers:**` into the
acceptance list. Keep the blank line **before** `**Pointers:**` (it closes the
acceptance list) and blank lines around the trailing `---`.

## Tags and IDs

Tags are bracketed and live on the ticket's `**Tags:**` line for grep-filtering
(`grep '\[api\]'`; add `-B2` to pull in the heading). Order:
**type · phase · area · status**.

| Group | Values |
|---|---|
| type | `[feat]` `[bug]` `[debt]` `[chore]` |
| phase | project-specific — the roadmap's phase names |
| area | project-specific — one per subsystem, added as needed; cross-cutting → several |
| status | `[next]` `[in-progress]` `[blocked]` `[someday]` |

**IDs are stable and never reused.** New items take the next free number with the
prefix from `.sdd.yml`. To find it, grep the whole file — `grep -o '\[T-[0-9]*\]'
<tasks> | sort -t- -k2 -n | tail -1` — and take one past the highest. Scanning
only the TODO section is the way duplicates happen: a higher id usually sits in
Done, collapsed to one line. A `deps:` reference must survive forever, so never
renumber.

## Moving to Done

Once the branch is reviewed and about to merge — not before, see the integration
rule in the project's rules file (`rules:` in `.sdd.yml`) — **collapse the ticket to one line** and swap the status tag
for a ref tag (`[PR #N]` / `[branch-name]` / `[commit-hash]`). Acceptance is
dropped — git remembers. Keep type/phase/area tags.

```markdown
- `[T-40]` `[feat]` `[launch]` `[api]` `[PR #91]` Title — one-sentence result.
```

## Leave out — and where it goes instead

Each of these is what makes a ticket "watery". Cut it from the ticket:

| Don't put in the ticket | Put it here instead |
|---|---|
| Why / motivation / rationale | the feature's `design.md` |
| History ("found during X", "as we discussed") | nowhere — git and the PR carry it |
| Option comparisons, "go with approach 2" | `design.md`, decided at pickup |
| Implementation narrative | the plan, at pickup |

## Example: before → after

**Watery:**

> …the importer rejects the whole file when one row fails validation, so a
> 10,000-row upload dies on a typo in row 3. Noticed while debugging a support
> ticket last week. **Go with option 2 = per-row outcomes**, not option 1
> (fail-fast with a better message) — users need the good rows to land, and
> partial success is what every comparable tool does…

**Ticket:**

```markdown
#### `[T-39]` Partial success on bulk import

**Tags:** `[feat]` `[import]` `[next]`

**Outcome:** A bulk import applies every valid row and reports the rejected ones, instead of failing the whole file.

**Acceptance:**

- [ ] Valid rows are committed when others fail validation
- [ ] The response lists each rejected row with its reason
- [ ] A file where every row fails still returns a non-2xx status

**Pointers:** deps: T-38

---
```

## Self-check before saving

- Could every sentence be ticked or pointed to? If a line only explains *why*,
  delete it.
- Is each acceptance box observable (an end-state), not a verb ("investigate",
  "consider")?
- New item: did you take the next free number and confirm it's unused?
- Done: collapsed to one line with a ref tag?
