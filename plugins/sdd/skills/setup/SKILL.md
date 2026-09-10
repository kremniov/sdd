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
concrete file changes together for approval. Approval of paths alone is not approval to replace a process.

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

Read `${CLAUDE_PLUGIN_ROOT}/templates/project/`. Create files only where absent.
Substitute config values for placeholders and retain the template's markers and
version. Do not copy `CHANGES.md` into the project.

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

For existing managed files, read
`${CLAUDE_PLUGIN_ROOT}/skills/setup/reference.md` and follow its version
procedure. Preserve everything outside the managed region. Ask about unknown or
ambiguous boundaries before editing that file.

## Resident rules

Read `${CLAUDE_PLUGIN_ROOT}/templates/project/CLAUDE.section.md` and render it
using the config. The destination is `rules`.

| Existing state | Action |
|---|---|
| No rules file | Create a project title and the approved section |
| File without a process or managed section | Append the approved section; preserve existing content |
| Managed section | Follow the version procedure in `reference.md` |
| Old `sdd:method-section` | Follow the retirement procedure in `reference.md` |
| Different existing process | Show conflicts and write the proposal to `<rules>.sdd-section` if approved; let the user choose integration |

Check malformed or duplicate markers before selecting a row. Keep one active
method section. A user can adopt config and scaffold while leaving resident
rules pending. Report that limited state and the unresolved process choice.

## Verify and report

Check rendered paths, unresolved placeholders, marker pairs, version stamps and
ignored notes. Compare changes with the approved proposal and confirm existing
project content is preserved. Report created, changed, skipped, declined and
pending items. Re-running should leave satisfied entries alone.

For an empty invariant list, offer `/sdd:canon` to establish it. For an existing
list, offer its audit mode. Identify obsolete references and propose
corrections; an unreferenced file remains the user's file.
