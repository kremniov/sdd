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
| CHANGES.md | An older managed region needs an update | Required changes and prior declines for the proposed region |
| Project rules | Loaded by the project harness | Resident constraints and routing |
| Canon | Relevant work or review | Current obligations and interactions |

Each skill keeps its templates under its own directory. Instructions link bundled resources with relative Markdown paths, resolved
from the containing instruction file. Design, plan and work own their artifact skeletons;
setup owns project scaffold and migration history. Project files use
rendered project paths and skill names. `.sdd.yml`
provides project locations. Readers split at the first colon, strip comments
from the first `#`, and use unquoted values. Directory values include a final `/`.

Setup includes the execution constraints needed before adoption: concrete
approval, one question at a time, complete proposals, direct writing, working
branches, verified commits and PR handover. Integration uses work after explicit
permission and independent review.

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

An opening marker records the version of a managed region. Equal stamps require
no edit; newer project stamps are left alone. Older stamps select CHANGES.md
entries after the project version through the template version. Bare valid
legacy markers use the documented v0.2.0 baseline. Unknown history or malformed
boundaries require user resolution.

Use the current template as the proposal basis. Refresh generic legacy prose;
preserve project requirements, terms, IDs, links and content outside the region.
Check current skills and config before carrying legacy rules as project additions.
Retain declined requirements until accepted, even when the template differs.
Show the full proposed region and apply it on approval. See ADR 0029. Advance the stamp
through fully satisfied contiguous versions. A declined entry remains pending.
On re-run, an applied later entry is recognized by meaning if an earlier decline
prevented recording it in the stamp.

A valid legacy method section can be replaced with the new rules section after
the complete replacement is shown and approved. Carry project constraints into
the proposal. Declining preserves the old section and leaves the new fence
unwritten. Report conflicts with the installed skill version. Keep one active
method section.

## Version and checks

The manifest version identifies the release. Changed scaffold guidance advances
its stamp and gains an entry in CHANGES.md in the same commit. Existing migration
entries remain available. Catalogue metadata must resolve the manifest.

`check.sh` verifies structure, references, render presence and version accounting.
It does not execute adoption. `tests/scenarios/` supplies cases for fixture
walkthroughs and agent evaluations, with their evidence classified separately.
