<!-- sdd:rules v1.1.0 -->
## Development method

Use `/sdd:work` for implementation, resuming work and authorized integration.
Use the skill that matches a specialized request: `/sdd:design`, `/sdd:plan`,
`/sdd:debug`, `/sdd:tasks`, `/sdd:canon`, `/sdd:subsystem` or `/sdd:setup`.
A review or explanation does not authorize changes. Project paths and the
verification command are in `.sdd.yml`.

### Integration

The user decides integration. Prepare and push the verified branch, open its
PR and stop. After the user's explicit permission to merge that PR, follow
`/sdd:work` Integration and execute the merge. Approval of implementation is
not permission to merge or push to the integration branch.

### Evidence

Run the relevant checks and required `{{verify}}` checks. Read completed output
before claiming success. Name commands, outcomes and skipped checks. Limit
claims to the behavior actually verified.

### Writing

Use ASD-STE100 as a readability reference: direct sentences, consistent terms
and an explicit actor. Keep conditions and prohibitions precise. Include a
reason when needed to choose the correct action; keep other decision history
in ADRs. Remove rhetoric and repeated instructions.

Code comments explain constraints left unclear by the implementation. Remove
comments that restate code. Record change history in commits and ADRs.
<!-- /sdd:rules -->
