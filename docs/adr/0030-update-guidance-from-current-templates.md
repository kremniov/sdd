# 0030. Update guidance from current templates

Date: 2026-09-13
Status: Accepted

## Context

ADR 0011 introduced version-by-version migration to preserve project wording.
ADR 0029 changed the proposal basis to current templates, but retained the
baseline, migration journal and partial-version accounting. Those mechanisms
are unnecessary for an approved replacement that preserves project requirements.

## Decision

Setup compares existing guidance directly with the current template. Preserve
project requirements, terms, IDs and links; replace generic legacy prose.
Show the complete proposal and material conflicts before replacing a region.
On decline, leave the region and stamp unchanged.

Keep marker boundaries and template stamps. Leave newer project sections
unchanged; inspect unstamped sections without assigning a historical baseline.
Matching stamps do not replace content review. Stamp approved replacements with
the template version. Leave satisfied content alone on re-run.

Put the update procedure in setup itself. Remove reference.md, the bundled
CHANGES.md and checks that require migration entries or contiguous application.
Retain checks for markers, stamp syntax, release ceiling and version progression.

This replaces ADR 0011's migration procedure and ADR 0029's migration accounting.
ADR 0020's legacy replacement safeguards remain in the unified setup procedure.

## Consequences

An update needs the current section and current template, not the release chain.
There is no persistent refusal registry or mandatory re-offer procedure.
Git and the repository changelog retain history. Structural checks do not prove
preservation of project requirements; scenario review assesses that behavior.
