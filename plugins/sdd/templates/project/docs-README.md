<!-- sdd:scaffold v0.2.0 -->
# Docs guide

Organized so an agent can load *how the system is now* cheaply, without
re-reading the codebase. Three lifetimes — don't mix them.

| Path | Lifetime | Purpose |
|---|---|---|
| `{{canon}}` | **always current** | How the system is built now. Read this first. Updated in the same PR that changes the seam it describes. |
| `{{adr}}` | append-only | One decision per file (why we chose X). Added when an invariant or a significant trade-off changes. |
| `{{roadmap}}` | long-lived | Direction: phases and objectives, sequence rather than dates. Updated rarely, when direction shifts. |
| `{{tasks}}` | evolving | The "what's next" queue — one ticket per actionable item. Format: `/sdd:tasks`. |
| `{{features}}<name>/` | frozen at merge | Per-feature `design.md` + `plan.md` (tier 2 only). A dated record of how the feature was reasoned into being; durable consequences are folded into the canon, which is where current truth lives. |

Three more places earn a mention once a project has them. They are conventions,
not artifacts this method generates:

| Path | Lifetime | Purpose |
|---|---|---|
| product analyses | long-lived | What a feature area must do for its users and why — scenarios, requirement axes, where the boundary of the thing is. Written before the technical design and cited from it. The question is "what and for whom"; `design.md` answers "how". |
| strategy / vision | long-lived | Direction above the roadmap: what the product is becoming. Rarely read during a change, occasionally binding on one — an invariant may require that architecture not close a door named here. |
| vendored contracts | reference | Pinned third-party specs integrated against — a vendor's API description or schema, copied for offline reference. Not the project's own contracts. |

Anything that fits none of these rows is scratch. Give it one directory, name it
so nobody mistakes it for canon, and never cite it from a document that is.

## Start-of-work reading order

1. `{{canon}}invariants.md` — the rules.
2. `{{canon}}layout.md` — where things live.
3. The relevant subsystem doc under `{{canon}}`.

## New features

Which artifacts a task needs at all is the tier table in the project's rules file. For tier 2,
the shape of `design.md` and `plan.md` is the skeletons the `sdd` plugin ships.

**The one added rule:** if a feature changed a seam described in the canon,
update that file in the same PR. Otherwise the architecture layer drifts and
agents fall back to re-reading code — which this structure exists to prevent.
<!-- /sdd:scaffold -->
