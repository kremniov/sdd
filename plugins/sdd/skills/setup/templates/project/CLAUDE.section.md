<!-- sdd:rules v1.1.18 -->
## Development method

Use `/sdd:work` for implementation, resuming work and authorized integration.
Use the skill that matches a specialized request: `/sdd:design`, `/sdd:plan`,
`/sdd:debug`, `/sdd:tasks`, `/sdd:canon`, `/sdd:subsystem` or `/sdd:setup`.
Project paths and the verification command are in `.sdd.yml`.

### Authorization

Permissions are granted individually. Never infer one from another:

- Review, audit or explanation does not permit editing files.
- Writing a ticket or design does not permit implementing its subject.
- Implementing a change does not permit integrating it; see Integration.

### Integration

Before creating or editing tracked files, check the branch. On `main`,
`master` or another integration branch, create a working branch first. Commit
and push only to working branches. This also applies to standalone document,
queue and setup operations. Follow `/sdd:work` Branch and completion for their
handover.

The user decides integration. Prepare and push the verified branch, open its
PR and stop. After the user's explicit permission to merge that PR, follow
`/sdd:work` for integration and execute the merge.

### Evidence

For behavior covered by an automated test, observe the test fail for the
intended reason before the change that makes it pass. Run the relevant checks
and required `{{verify}}` checks. Read completed output before claiming success.
Name commands, outcomes and skipped checks. Limit claims to the behavior
actually verified.

### Writing

Use ASD-STE100 as a readability reference: direct sentences, consistent terms
and an explicit actor. Keep conditions and prohibitions precise. Include a
reason when needed to choose the correct action; keep other decision history
in ADRs. Remove rhetoric and repeated instructions.

Code comments explain constraints left unclear by the implementation. Remove
comments that restate code. Record change history in commits and ADRs.
<!-- /sdd:rules -->
