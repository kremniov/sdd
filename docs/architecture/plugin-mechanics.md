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
| CHANGES.md | An older managed region needs an update | Proposed semantic edits, not a template overwrite |
| Project rules | Loaded by the project harness | Resident constraints and routing |
| Canon | Relevant work or review | Current obligations and interactions |

Skills resolve bundled paths through `${CLAUDE_PLUGIN_ROOT}`. Project files use
rendered project paths and skill names, not that plugin variable. `.sdd.yml`
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

Present each proposed change in the project's wording and apply it on approval.
Keep IDs, links, additions and content outside the region. Advance the stamp
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
