# ADR 0011 — Compare scaffold versions, not scaffold text

**Status:** accepted · **Date:** 2026-08-10 · **PR:** —

## Context

ADR 0009 fenced the plugin's half of each scaffold file so a re-run could update
it without touching the project's queue, phases or rules. It considered a
version stamp at the time and rejected it — as a *replacement* for the fence,
because a stamp alone says nothing about where the plugin's text ends.

The first upgrade against a real prior adoption showed what the fence alone does
not settle. The project had rewritten the guidance in its own terms — its own
ticket-id convention, its own cross-references, its own phrasing of the same
rules — and the fence now surrounded that. The skill compared the region against
the rendered template, found it different, and would have offered to replace it,
warning that a yes discards whatever is there. Nothing in the region tells stale
from customized, so the skill was posing a question it could not answer itself:
it did not know what it would be taking away.

Both answers are losses. Yes destroys deliberate wording. No, learned once,
stops the project from ever receiving a correction.

## Decision

The comparison is between versions, not texts. The opening marker carries the
version in which that region last changed — `<!-- sdd:scaffold v0.3.0 -->` — and
a re-run compares the project's stamp with the template's. Equal stamps end the
comparison: the region is current whatever it says, and a difference in wording
is the project's edit, about which the plugin has nothing to report.

Where the project is behind, what it is offered is the entries in
`templates/project/CHANGES.md` between the two versions — each describing what
the guidance now requires and what it replaced, in prose applicable to text
worded differently. The carry edits the project's wording to hold the change;
it never installs the template's text. A declined entry leaves the stamp
behind, so it is offered again.

## Alternatives

- **Diffing the region against the rendered template.** This is the current
  behaviour and the defect: a project whose region shares no sentences with the
  template produces a diff of everything.
- **One stamp per project, in `.sdd.yml`.** Files are carried independently and
  a decline must leave one file behind without lying about the rest.
- **Stamping every scaffold file at every release.** Every file would look stale
  at every upgrade — the same false positive with a version number on it.
- **Shipping the template's history so the region could be reconstructed.** Buys
  a three-way merge at the cost of carrying every past version of five files
  forever, to serve a case the change log describes in a paragraph.
- **Recording declines in the project's file.** A second piece of state in
  someone else's document, to avoid re-asking a cheap question.

## Consequences

Invariant 2 now requires a stamped fence and states that the comparison is
stamp-first. `check_scaffold.py` enforces five things: a parsable version on
every opener, no version ahead of the plugin's own, a stamp that moves whenever
its region changes against the branch point, a change-log entry for every stamp
past the `v0.2.0` baseline, and no entry ever removed.

The last two both follow from where a project upgrades *from*. It is wherever
that project stands, not the last release — so an entry describing a change at
`v0.3.0` is still the thing a `v0.2.0` project needs after the file has moved on
to `v0.5.0`, and the log only ever grows.

The cost lands on this repository, not on adopters: changing a word inside a
fence now obliges a version bump and a written entry saying what changed and
why. That is the intended friction — the entry is the only thing an adopting
project can act on without being handed someone else's prose.

Projects adopted while the markers were bare are read as `v0.2.0`, a true lower
bound rather than a guess. Projects adopted before markers existed keep the
`no fence` branch from ADR 0009 unchanged.
