---
name: canon
description: Establish, amend or audit architectural invariants and the system map, and record verified project lessons.
---
 # Canon

For files intended for Git, follow `/sdd:work` Branch and completion before
editing and when handing over the result.

## Inputs and mode

Read the request and `.sdd.yml` values `canon`, `adr` and `tasks` as needed.
Split each line at the first colon and remove comments from the first `#`. If
configuration is absent, offer `/sdd:setup`. Ask for required missing values.

The canon directory holds `invariants.md`, `layout.md`, `lessons.md` and
subsystem documents. Code supplies evidence of behavior; requirements and
accepted decisions also supply obligations. Investigate disagreements before
changing either. Cite concrete evidence for claims, including absence.

| Mode | When | Procedure |
|---|---|---|
| Establish | The invariant list is empty | Read `${CLAUDE_PLUGIN_ROOT}/skills/canon/bootstrap.md` |
| Amend | Assess a changed branch | Use Amend below |
| Audit | The user requests a recheck or suspects stale rules | Read `${CLAUDE_PLUGIN_ROOT}/skills/canon/audit.md` |

State the mode. A review or audit reports first; changes need approval. An
existing approval for the exact canon change remains valid.

## Invariant format

```markdown
7. **Short name.** The rule and its scope.
   *Detect:* a runnable check, or an explicitly manual review question.
   *On violation:* reject the change, or agree a rule change and record an ADR.
```

A candidate must have a concrete possible violation and a material consequence.
Require evidence that it is a current rule. Repetition alone is insufficient.
Exclude generic values, duplicates and guarantees already enforced by the
language or framework. A project checker can enforce an eligible rule.

Verify that Detect covers the claimed rule. A manual detector is labeled manual;
a passing narrow checker does not prove a broader claim. Preserve numbers.
Append new entries; retain a retired entry's number, struck through and linked
to its ADR. A changed or retired rule requires agreement and an ADR. Wording
edits that preserve the rule's meaning do not require an ADR.

## Amend

Read the branch diff, relevant current code, rules and agreed decisions. Check
four questions:

- Does an existing rule stop holding?
- Does the change establish a required rule that passes the candidate filter?
- Does a detector change its coverage?
- Does an exception change the rule's scope?

No change is a normal result. State the evidence briefly and finish when all
four answers are no. Otherwise present the exact proposed edit and its basis.
Distinguish a code violation from a proposed rule change; the user decides which
to correct. Write approved changes in the same PR as the affected behavior. An
already agreed design decision need not be approved again.

Use `/sdd:subsystem` for interaction changes and update `layout.md` when the map
changes. Record a durable decision using `/sdd:work` and its ADR template.

## Lessons

Record verified project observations in `lessons.md`: runtime constraints,
observed dependency behavior or a command's unexpected effect. Use one dated
entry with evidence or an ADR link where available. Omit general advice and
copies of invariants. If a lesson becomes an agreed invariant, link its number.
