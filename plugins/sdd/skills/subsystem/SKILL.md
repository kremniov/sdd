---
name: subsystem
description: Describe a subsystem's contracts and interactions, or update that document when a branch changes its behavior.
---

# Subsystem document

For files intended for Git, follow `/sdd:work` Branch and completion before
editing and when handing over the result.

## Inputs

Read the request and `canon` from `.sdd.yml`. Split each line at the first colon
and remove comments from the first `#`. If configuration is absent, offer
`/sdd:setup`. Ask for a required missing value.

Read the relevant code, existing document, governing invariants, accepted
requirements and branch diff. Use `/sdd:work` for proposed-change approval.
A request to check a document produces findings; it does not authorize fixes.

## Write or update

Trace a real interaction end to end. Explain:

- responsibility and any exclusion needed to prevent misunderstanding;
- contracts, data and direction across component boundaries;
- ordering that affects correctness and the consequence of breaking it;
- governing invariants, linked by number.

Write under `canon`. Choose a structure that fits the subsystem. Keep existing
contracts at their source and link them. Put a file inventory in `layout.md`.
Create a separate document when interactions or constraints need explanation
beyond that map; document count alone does not determine this need.

On an existing document, correct claims the change makes wrong and add relevant
missing interactions. Preserve unrelated content. Update in the same PR as the
behavior. A branch that changes an undocumented interaction creates its document.
No document change is a normal result when the claims remain accurate.

State current behavior and obligations. Record historical choices in ADRs,
verified observations in `lessons.md`, and future objectives in the roadmap.

## Verify

Ground each changed claim in code or an accepted contract. Check that the old
and new text do not contradict each other. If code and an obligation disagree,
report the discrepancy before replacing the obligation with current behavior.
For a requested audit, report unsupported claims and evidence without editing.
