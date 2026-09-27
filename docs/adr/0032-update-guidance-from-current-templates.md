# 0032. Update guidance from current templates

Date: 2026-09-27
Status: Accepted
PR: #12

## Context

ADR 0011 introduced version-by-version migration to preserve project wording.
ADR 0029 changed the proposal basis to current templates, but kept the
baseline, the migration journal for every stamp and partial-version
accounting. Every template edit needed a journal entry, and most entries only
repeated the prose change that a comparison with the current template shows.
Some changes cannot come from such a comparison: in 1.2.0 the configuration
moved into `.sdd/`, the queue split into ticket files and setup installed a
tool.

## Decision

Setup compares existing guidance directly with the current template. Preserve
project requirements, terms, IDs and links; replace generic legacy prose.
Show the complete proposal and material conflicts before replacing a region.
On decline, leave the region and stamp unchanged.

Keep marker boundaries and template stamps. Leave newer project sections
unchanged; inspect unstamped sections without assigning a historical baseline.
Matching stamps do not replace content review. Stamp approved replacements with
the template version. Leave satisfied content alone on re-run.

`setup/migrations.md` lists only structural changes. Each entry states the
condition under which it applies, so setup checks conditions rather than
versions. Entries are append-only. The update procedure lives in setup itself;
`reference.md` and the bundled `CHANGES.md` are removed.

This replaces ADR 0011's migration procedure and ADR 0029's migration
accounting. ADR 0020's legacy replacement safeguards remain in the unified
setup procedure.

## Alternatives

- **Keep the per-stamp journal.** An entry told a heavily reworded project what
  changed, but every template edit paid for it, and most entries described
  prose that the current template already shows.
- **Remove the journal entirely.** A moved file, a content conversion or an
  installed tool has no representation in a template region, so an update would
  miss it.

## Consequences

An update needs the current section, the current template and the structural
migrations. There is no persistent refusal registry or mandatory re-offer
procedure. Git and the repository changelog retain history. Structural checks
do not prove preservation of project requirements; scenario review assesses
that behavior.
