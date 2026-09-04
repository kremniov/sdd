<!-- sdd:scaffold v1.0.0 -->
# Docs guide

Organized so an agent loads *how the system is now* cheaply, and leaves the
codebase unread. Three lifetimes, kept apart.

| Path | Lifetime | Purpose |
|---|---|---|
| `{{canon}}` | **always current** | How the system is built now. Read this first. Updated in the same pull request that changes the seam it describes. |
| `{{adr}}` | append-only | One decision per file: why we chose X. Added when an invariant or a significant trade-off changes. |
| `{{roadmap}}` | long-lived | Direction: phases and objectives, in sequence. Updated rarely, when the direction shifts. |
| `{{tasks}}` | evolving | The "what is next" queue, one ticket per actionable item. Format: `/sdd:tasks`. |
| `{{features}}<name>/` | frozen at merge | Per-feature `design.md` and `plan.md`, tier 2 only. A dated record of how the feature was reasoned into being. Durable consequences fold into the canon, which holds current truth. |
| `{{notes}}` | working, outside git | Decision logs from a brainstorm, prompts, scratch. |

Three more places earn a mention once a project has them. They are conventions,
and this method generates none of them:

| Path | Lifetime | Purpose |
|---|---|---|
| product analyses | long-lived | What a feature area must do for its users, and why — scenarios, requirement axes, the boundary of the thing. Written before the technical design and cited from it. The question is "what and for whom"; `design.md` answers "how". |
| strategy and vision | long-lived | Direction above the roadmap: what the product is becoming. Rarely read during a change, and occasionally binding on one — an invariant may require that the architecture keep a door named here open. |
| vendored contracts | reference | Pinned third-party specs integrated against: a vendor API description or schema, copied for offline reference. The project's own contracts live elsewhere. |

Anything that fits none of these rows is scratch. Give it one directory, name it
so a reader sees it is scratch, and cite it from no document that is canon.

## Start-of-work reading order

1. `{{canon}}invariants.md` — the rules.
2. `{{canon}}layout.md` — where things live.
3. The subsystem document for the area.
4. `{{canon}}lessons.md` — what earlier work learned here.

## New features

`/sdd:work` carries the tier table, which says which artifacts a task needs. For
tier 2, the shape of `design.md` and `plan.md` is the skeletons the `sdd` plugin
ships.

**The one added rule:** where a feature changed a seam the canon describes,
update that file in the same pull request. Otherwise the architecture layer
drifts, and agents fall back to re-reading code, which this structure exists to
prevent.
<!-- /sdd:scaffold -->
