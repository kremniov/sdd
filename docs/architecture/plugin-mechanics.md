# Plugin mechanics

This document covers file resolution, adoption and upgrades. Workflow behavior
is in [the method](../method.md). Invariants 1–4 govern the plugin/project boundary.

## Files and loading

| File | Read when | Result |
|---|---|---|
| SKILL.md | The activity applies | Instructions for that activity |
| Skill reference | Its stated mode or condition applies | Additional procedure |
| Artifact skeleton | A design, plan or ADR is written | A project artifact, not a copied skeleton |
| Project scaffold | Adoption needs a missing file | Placeholder-substituted file with managed markers |
| Shipped tool | Adoption or an older tool stamp | A plugin-owned file in `.sdd/` |
| migrations.md | An update | Structural changes whose conditions to check |
| Project rules | Loaded by the project harness | Resident constraints and routing |
| Canon | Relevant work or review | Current obligations and interactions |

Each skill keeps its templates in its own directory. Resolve relative Markdown
links from the instruction file that contains them. Design, plan and work hold
artifact skeletons; setup holds project scaffold and structural migrations.

Project files use configured paths and skill names. Read locations from
`.sdd/config.yml`: split each line at the first colon, strip comments from the
first `#`, and use unquoted values. Directory values end in `/`. The `.sdd/`
directory holds the config and the tools that setup copies from the plugin.

A queue with a `tickets` directory keeps one file per ticket. `.sdd/tasks-index`
generates the open index `tasks` and the closed index `tasks_done` from the
ticket files, so a skill reads the open index without the closed history. The
tool reads its paths from the config and carries no project vocabulary.

Setup states the rules needed before resident instructions are installed:
concrete approval, one question at a time, complete proposals, direct writing,
working branches, verified commits and PR handover. Use work for integration
after explicit permission and independent review.

## Adoption order

1. Survey existing instructions, paths, verification and queue conventions.
2. Show the proposed config and concrete changes, including the notes ignore rule.
3. Write approved configuration before files that depend on it.
4. Create missing scaffold files and preserve existing project content.
5. Apply the approved resident section or leave a separate proposal when the
   current process is unresolved.
6. Check renders, paths, markers and ignored notes; report applied and pending work.

The invariant scaffold starts empty. Canon establishment follows adoption.
Notes use ignored files; feature and ADR directories can use tracked placeholders.

## Upgrade behavior

Compare existing managed guidance with the current template. A stamp identifies
the template version; it does not replace content review. Leave newer project
sections unchanged. For unstamped sections, compare content directly without
assigning an earlier version. A shipped tool records its version on a
`# sdd:scaffold vN.N.N` line and is replaced whole when older.

Check marker pairs and stamps. Ask about malformed or ambiguous boundaries or
stamps before editing the file. Agree the boundary and content before adding
markers to an unmanaged file.

Base the complete proposal on the current template. Preserve project requirements,
terms, IDs, links and text outside the region. Replace generic legacy prose;
check current skills and configuration before retaining old method rules as
project additions. Leave content that meets current guidance and style alone.
Show material changes and conflicts. Apply the approved replacement with the
template's stamp. On decline, leave the section and stamp unchanged. Use the
same procedure to replace a legacy `sdd:method-section` with `sdd:rules`. Keep
one active method section.

`migrations.md` lists structural changes that a template comparison cannot
derive. An entry is a `###` heading under its `##` version, then one
non-empty `**Applies when:**` condition, then the instructions. Setup checks
every condition and proposes the migrations that apply. See ADR 0032.

## Version and checks

The manifest version identifies the release. Advance a template's stamp when
its managed guidance changes; never decrease it. A structural change gains a
`migrations.md` entry in the same commit, and entries are append-only. Release
changes belong in the repository changelog. Catalogue metadata must resolve the
manifest.

`check.sh` verifies structure, references, render presence and version accounting.
It does not execute adoption. `tests/scenarios/` supplies cases for fixture
walkthroughs and agent evaluations, with their evidence classified separately.
