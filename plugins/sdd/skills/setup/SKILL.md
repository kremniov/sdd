---
name: setup
description: Adopt or update SDD by mapping project paths, proposing exact scaffold changes and preserving existing project instructions.
---
 # Setup

## Run setup

Survey first and obtain approval of the concrete changes before writing them.
Compare existing process instructions with the installed method; show conflicts
before replacing them. Apply an already approved proposal without asking again.
Discuss related questions together, asking one at a time. Prefer
`AskUserQuestion` when available. Show complete proposed managed sections without
placeholders for omitted text.

Use ASD-STE100 as a readability reference: direct sentences, consistent terms
and an explicit actor. Preserve precise conditions; remove rhetoric and repetition.

Before editing files for Git, check the branch. Create a working branch when on
main, master or another integration branch. Preserve user changes; use a worktree
when isolation is needed. Verify and commit completed steps, then push and open
a PR. Report completed checks and limitations. Stop for user-started independent
review; merge requires separate explicit permission and `/sdd:work` Integration.

## Survey

Read the request, root rules files, docs layout, verification configuration,
ticket conventions and any existing `.sdd.yml`. Record actual paths before
asking. Inspect existing content and managed markers before writing files.

Prefer existing project locations. Show the complete proposed config and the
concrete file changes together for approval. Approval of paths alone does not
approve replacing a process.

## Configuration

Use one unquoted `key: value` per line. The first colon separates the key; the
first `#` starts a comment. Values cannot contain `#` and quotes are not
removed. Directory values end in `/`. `ticket` is the prefix alone, without a
trailing hyphen. `verify` is a command that exits non-zero when a required check
fails.

Example locations, replaced with the project's own:

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

Explain inferred values and ask for required unknowns. Show the notes storage
policy and proposed ignore entry. Notes must stay outside Git; do not create a
tracked placeholder there. If the selected directory already contains tracked
files, propose a separate untracked location rather than untracking user files.

After approval, write `.sdd.yml`. For an existing config, show the exact diff
before applying it. Keep unrelated keys and project content.

## Scaffold

Read the [project templates](templates/project/). Create files only where absent.
Substitute config values for placeholders and retain the template's markers and
version.

| Destination | Source |
|---|---|
| `canon` + `invariants.md` | `invariants.md` |
| `canon` + `lessons.md` | `lessons.md` |
| `tasks` | `tasks.md` |
| `roadmap` | `roadmap.md` |
| Parent of `canon`, if not the repository root and no README exists | `docs-README.md` |
| `features`, `adr` | Create missing directories; use a tracked placeholder if needed |
| `notes` | Create the ignored directory with the approved ignore rule |

For an existing README without markers, propose necessary targeted corrections.
Adding a managed section requires separate approval of its boundary and content.

For existing managed files, follow Update existing guidance below.

## Resident rules

Read [CLAUDE.section.md](templates/project/CLAUDE.section.md) and render it
using the config. The destination is `rules`.

| Existing state | Action |
|---|---|
| No rules file | Create a project title and the approved section |
| File without a process or managed section | Append the approved section; preserve existing content |
| Managed or legacy `sdd:method-section` | Follow Update existing guidance below |
| Different existing process | Show conflicts and write the proposal to `<rules>.sdd-section` if approved; let the user choose integration |

A user can adopt config and scaffold while leaving resident rules pending.
Report that limited state and the unresolved process choice.

## Update existing guidance

Locate the managed region: `sdd:rules` for resident rules, `sdd:scaffold` for
other files, or the legacy `sdd:method-section`. Check marker pairs and stamps.
If boundaries or stamps are malformed or ambiguous, ask before editing that
file. For a file without markers, agree the boundary and content before adding
a managed section. Leave a section newer than the installed template unchanged
and report the version mismatch. A missing stamp requires no assumed baseline.

Compare the region with the current template. Preserve project requirements,
terms, IDs and links; replace generic legacy prose. Check current skills and
configuration before treating old method rules as project additions. Leave
content that already meets the current guidance and writing style alone.

Show the complete proposed replacement and material changes, including process
conflicts. After approval, replace only that region and use the template's stamp.
On decline, leave the region and stamp unchanged. Replace a legacy
`sdd:method-section` with `sdd:rules` through this same procedure. Keep one active
method section and preserve everything outside the approved boundary.

## Verify and report

Check rendered paths, unresolved placeholders, marker pairs, version stamps and
ignored notes. Compare changes with the approved proposal and confirm existing
project content is preserved. Report created, changed, skipped, declined and
pending items. Re-running should leave satisfied entries alone.

For an empty invariant list, offer `/sdd:canon` to establish it. For an existing
list, offer its audit mode. Identify obsolete references and propose
corrections; an unreferenced file remains the user's file.
