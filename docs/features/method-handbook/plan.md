# Method handbook rewrite — plan

Status: approved 2026-09-08. Basis: [the agreed method](../../method.md).
Branch base: `v2-method` at `b7b49f4`.

## Scope

Rewrite eight skills, their references, skeletons and project scaffold from the
agreed method. Publish the English method and scenario corpus. Keep Russian
working documents outside Git. Retain the skill names and distribution platform.
Permission automation and author-started independent review are outside scope.

## Order

Commit each completed step before the next. Several commits per step are
allowed. The entry skill precedes the procedures it routes to; scaffold changes
travel with their version and migration notes. Canon and final checks follow the
complete instruction set. An approved plan authorizes execution through PR.

## Steps

### 1. Publish the method and scenarios

Write `docs/method.md`, this plan and `tests/scenarios/`. Keep one scenario per
file and execution guidance in its README. Map method provisions to owners and
checks in the working notes. Check that the English text preserves the agreed
behavior. Store run evidence in ignored `docs/stuff/eval-runs/`.

### 2. Rewrite work

Write routes, tiers, approvals, execution, intermediate commits, blockers,
status and authorized integration. Walk through tier 0–2, resume, blocker and
merge scenarios. Preserve existing referenced skill names during the transition.

### 3. Rewrite design and plan

Write the two skills and `_DESIGN.md`, `_PLAN.md`, `_ADR.md`. Read approved
brainstorm decisions as design input. Remove repeated choices and content
minimums. Support manual checks and multiple commits per step. Exercise a small
tier-2 design and plan for contract, failure and verification coverage.

### 4. Rewrite the specialized skills

Write debug, tasks, canon, subsystem and canon references. Retain necessary
ticket context. Separate broken rules from decisions to change them. Exercise
failed fixes, unchanged canon, audit violations, ticket context and subsystem
contract updates.

### 5. Rewrite adoption and scaffold

Write resident instructions, project scaffold, setup and its reference. Preserve
project additions and show concrete changes for approval. Update changed stamps,
plugin metadata and migration entries together. Exercise fresh adoption, existing
process, accepted and declined upgrades, re-run and malformed markers in isolated
scratch repositories.

### 6. Update checks and repository documentation

Keep size and depth limits; report negation frequency without failing on it.
Report full loaded text size including examples and references. Test changed
checker behavior. Update canon, ADRs, README, CHANGELOG and plugin mechanics.
Render CLAUDE.md from the new template. Keep historical ADRs and frozen artifacts.
Run the complete structural checks and inspect active rules for contradictions.

### 7. Verify and open the PR

Complete the coverage map and scenario walkthroughs. Compare old instructions
for missed constraints. Resolve conflicts with the agreed method explicitly.
Where an available harness supports isolated agent runs, record the actual input
and outcome; report unrun cases as such. These are author-side evaluations.
Run final checks and self-review, commit corrections, push and open a PR against
v2-method (or main if that branch has merged). Stop for independent review and
explicit integration permission.

## Verification

Run `./scripts/check.sh` after each step. When a changed method rule requires a
checker update, include that update and its validation in the same step. Do not
weaken checks to conceal unagreed changes. Verify the complete set after step 6.
Use `SDD_BASE=b7b49f4` for scaffold comparison against this branch's actual base.

The scenario README separates inspectable walkthrough evidence from observed
agent behavior. Russian notes are never staged. Each implementation commit names
the completed work and its reason.
