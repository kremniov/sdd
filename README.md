# SDD — spec-driven development

A Claude Code plugin for research, concrete approvals, committed implementation
steps and user-authorized integration. Read [the method](docs/method.md) for the
complete workflow.

## Workflow

| Tier | Before implementation |
|---|---|
| 0 | Approve the exact change, assumptions and verification |
| 1 | Approve scope and the recommended solution together |
| 2 | Approve discussion decisions, then design, then plan |

Each completed step is verified and committed before the next. A step can have
several commits. The agent opens a PR and stops. The user starts independent
review at every tier. After explicit merge permission, the agent closes the
ticket in the final branch commit, pushes and merges subject to required checks.

## Skills

| Skill | Result |
|---|---|
| `/sdd:work` | Research, approvals, execution, handover, resume and authorized merge |
| `/sdd:design` | A complete design from approved decisions |
| `/sdd:plan` | Ordered steps with concrete checks |
| `/sdd:debug` | Evidence of a cause and verification of an approved fix |
| `/sdd:tasks` | Queue entries with context, outcomes and stable IDs |
| `/sdd:canon` | Invariants, system map and verified lessons |
| `/sdd:subsystem` | Current contracts and interactions |
| `/sdd:setup` | Approved configuration, scaffold and resident rules |

Reviews and explanations return findings without starting implementation.
A direct request can start work without a ticket.

## Install and adopt

```text
/plugin marketplace add kremniov/sdd
/plugin install sdd@kremniov
/sdd:setup
```

Setup surveys existing files, proposes paths and shows changes before applying
them. Existing project content is preserved. Updates use versioned semantic
changes and retain project additions. Run `/sdd:canon` to establish or audit the
invariant list after adoption.

Example `.sdd.yml`:

```yaml
canon: docs/architecture/
tasks: docs/tasks.md
roadmap: docs/roadmap.md
features: docs/features/
adr: docs/adr/
notes: docs/notes/
verify: make lint && make test
ticket: T
rules: CLAUDE.md
```

Use project paths and an actual verification command. Values are unquoted;
directory paths end in `/`. `#` starts a comment and cannot occur in a value.
Working notes stay outside Git. Rules may live in CLAUDE.md or AGENTS.md.

## Documents and checks

The canon describes the current system. ADRs record durable decisions. Designs
and plans remain historical after merge. Templates specify sufficient content
without minimum decision or sentence counts.

`./scripts/check.sh` validates the plugin's structure, references, configuration,
scaffold versions, rendered rules and instruction budgets. Skills are limited
to 1200 words and resident rules to 400, including examples. Skill and skeleton
structure stops at H3. Negation frequency is advisory. Counts do not prove
instruction clarity or agent behavior.

[Behavior scenarios](tests/scenarios/README.md) define inputs and expected actions.
Evaluation distinguishes textual walkthroughs from observed agent runs. These
checks validate the plugin; adopting projects retain their own verification.

## Attribution and license

Developed by [Andrey Kremnev](https://github.com/kremniov). The method draws on
ideas explored with [Superpowers](https://github.com/obra/superpowers), including
explicit workflows and systematic debugging. This instruction set is written
from the agreed SDD method. MIT; independent of the Superpowers project.
