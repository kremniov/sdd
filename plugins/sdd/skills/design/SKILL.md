---
name: design
description: Write a complete tier-2 design from approved discussion decisions and submit it for G2 approval.
---
 # Design

For files intended for Git, follow `/sdd:work` Branch and completion before
editing and when handing over the result.

## Inputs

Use `/sdd:work` for scope, approval and stop conditions. Begin after G1. Read
`.sdd.yml` for `features`, `notes`, `tasks`, `roadmap`, `canon` and `adr`. Split
each line at its first colon and remove comments from the first `#`. If
configuration is absent, offer `/sdd:setup`. Ask for required missing values.

Read the approved `<notes>/<task>-decisions.md`, the request or ticket, relevant
product requirements, roadmap, canon, ADRs and code. A task without a ticket
uses the request. If approved decisions are missing from the log, recover them
from the conversation and record them; ask about decisions that cannot be
recovered.

Identify disagreements between acceptance, requirements, constraints and code.
Present new evidence that changes an agreed decision to the user before relying
on the change. Keep settled choices unless that evidence requires reopening
them.

## Write and submit

1. Read `${CLAUDE_SKILL_DIR}/templates/_DESIGN.md` in place.
2. Write `<features>/<task>/design.md`. State the observed problem, required
   result, scope, decisions, contracts, interactions, failures and verification.
3. Link governing invariants and existing contracts. Name documents that need
   updates. Mark durable decisions `→ ADR`; `/sdd:work` records them with the work.
4. Check for missing decisions, conflicting sections and scope beyond the
   request. Retain a detail when deleting it leaves a material choice open or
   prevents verification. Omit empty sections.
5. Present the complete document at G2. Discuss it section by section only when
   the user requests that process. Apply feedback and wait for approval.
6. Commit the approved design. Continue with `/sdd:plan` when the task includes
   that phase. For design alone, hand over the approved artifact through
   `/sdd:work`; leave implementation unstarted.

Use current project patterns within agreed constraints. Include a local
structural correction when the change requires it; propose unrelated refactoring
as separate work.

## Content budget

Aim for at most 1300 words, with a 2000-word ceiling and at most 12 headings.
These are upper bounds, not content targets. State a choice and its decisive
constraint briefly. Include additional evidence when needed to assess it. There
is no minimum sentence or decision count. Keep detailed existing contracts at
their source and link them.
