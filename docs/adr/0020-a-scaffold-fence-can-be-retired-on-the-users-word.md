# ADR 0020 — A scaffold fence can be retired, once, on the user's word

**Status:** accepted · **Date:** 2026-09-04 · **PR:** —

## Context

Invariant 3 makes adoption additive: no skill overwrites or reformats a file it
did not write in this run. ADR 0009 fenced the plugin's half of each scaffold
file so a correction could reach a project that already adopted, and ADR 0011
made the comparison a version comparison, carried as a described change into the
project's own wording.

That machinery describes changes. Version 1.0.0 does not change the rules
section — it replaces it. The region held 1693 words of method; the new one holds
268 and points at `/sdd:work` for the rest. A change-log entry saying "delete
about 80% of this region" is not a described change applied to text worded
differently, and eight entries saying it one subsection at a time is the same
deletion with more clicks.

Leaving the old region in place is worse. The installed skills expect the v1
frame, and a project would then hold two descriptions of the method in one file.

## Decision

A fence this plugin wrote in an earlier version, whose whole region a major
version replaces, may be retired. The retirement is bounded to five steps:

1. Show the whole region, in full, before touching it.
2. Name what replaces it.
3. Ask once.
4. On a yes, replace that region and nothing else, carrying across whatever in
   it was the project's own — its conventions, its paths, a rule it earned once
   and wrote down — and say which lines were kept.
5. On anything else, leave the region alone, write no new fence, and report that
   the project runs the old rules while the installed skills expect the new
   frame. Offer the question again on the next run.

Two method sections in one file are never written.

Version 1.0.0 retires `sdd:method-section` and introduces `sdd:rules`. The new
fence name is what makes the two states distinguishable: a project holding the
old marker is recognisably pre-1.0.0, whatever its wording.

## Alternatives

- **One change-log entry per removed subsection.** Eight yes answers for one
  decision, and each entry would describe a deletion, which the change log is
  written not to do.
- **A `replacement` entry kind in the change log.** Puts the same behaviour
  behind a general mechanism, which invites its use where a described change
  would have done.
- **Keep the old fence name and shrink the region.** Nothing in the file then
  says which method it holds, and a project that declined would be indistinct
  from one that had never been asked.
- **Leave old adoptions alone entirely.** The skills would carry rules the
  project's file contradicts.

## Consequences

Invariant 2 gains the retirement path and invariant 3 gains its one exception,
stated with its bound. Nothing else adoption touches is ever deleted.

The cost lands on this repository at every major version: retiring a region
means naming the new fence, writing the entry, and carrying the branch in
`/sdd:setup`. That friction is the point — it makes a replacement a decision
someone records rather than a diff someone applies.

A project that declines keeps a working repository. Its scaffold files, its
queue and its canon are untouched, and only the rules section stays behind.
