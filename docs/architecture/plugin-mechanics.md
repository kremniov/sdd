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
| CHANGES.md | An older managed region needs an update | Changes to assess for the proposed region |
| Project rules | Loaded by the project harness | Resident constraints and routing |
| Canon | Relevant work or review | Current obligations and interactions |

Each skill keeps its templates in its own directory. Resolve relative Markdown
links from the instruction file that contains them. Design, plan and work hold
artifact skeletons; setup holds project scaffold and migration history.

Project files use configured paths and skill names. Read locations from
`.sdd.yml`: split each line at the first colon, strip comments from the first
`#`, and use unquoted values. Directory values end in `/`.

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

An opening marker records the version of a managed region. Equal stamps require
no edit; newer project stamps are left alone. Older stamps select CHANGES.md
entries after the project version through the template version. Bare valid
legacy markers use the documented v0.2.0 baseline. Unknown history or malformed
boundaries require user resolution.

Base the proposal on the current template. Replace generic legacy prose;
preserve project requirements, terms, IDs, links and text outside the region.
Check current skills and config before treating legacy rules as project additions.
Keep declined requirements unchanged until accepted. Show the complete proposed
region and apply it after approval. See ADR 0029.

Advance the stamp through consecutive versions whose entries are all satisfied.
Leave declined entries pending. On re-run, recognize applied entries by meaning
when an earlier decline prevented advancing the stamp.

For a valid legacy method section, show the complete replacement and preserve
project constraints. Replace it after approval. On decline, keep the old section
and leave the new fence unwritten. Report conflicts with the installed skills.
Keep one active method section.

## Version and checks

The manifest version identifies the release. Changed scaffold guidance advances
its stamp and gains an entry in CHANGES.md in the same commit. Existing migration
entries remain available. Catalogue metadata must resolve the manifest.

`check.sh` verifies structure, references, render presence and version accounting.
It does not execute adoption. `tests/scenarios/` supplies cases for fixture
walkthroughs and agent evaluations, with their evidence classified separately.
