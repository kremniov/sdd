<!-- sdd:scaffold v1.1.14 -->
# Project documents

| Path | Content and maintenance |
|---|---|
| `{{canon}}` | Current invariants, system map, subsystem interactions and verified lessons. Update affected claims in the same PR as the behavior |
| `{{adr}}` | Durable decisions and their reasons. Preserve history |
| `{{roadmap}}` | Product direction and objectives; link detailed requirements |
| `{{tasks}}` | Outcomes, necessary context, acceptance, dependencies and status |
| `{{features}}` | Agreed designs and plans; historical after merge |
| `{{notes}}` | Ignored decision logs and task status files for working context |

Start with the request and relevant requirements, then the applicable invariants,
system map, subsystem document and lessons. Inspect code to establish behavior
and investigate disagreements with obligations.

Use `/sdd:work` to select the route and approvals. `/sdd:design` and `/sdd:plan`
write tier-2 artifacts. `/sdd:canon` and `/sdd:subsystem` maintain current
architecture. A direct request can start work without a ticket.
<!-- /sdd:scaffold -->
