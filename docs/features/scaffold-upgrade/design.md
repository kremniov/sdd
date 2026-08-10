# Scaffold upgrade — design

**Ticket:** T-6 · **Plan:** [plan.md](plan.md)

## Problem

Five files are copied into a repository at adoption and never read again
(ADR 0002, deliberately: the project owns them from then on). A correction made
here after that reaches nobody.

This is measured, not anticipated. Six pre-rename skill names were fixed in
0.1.3; two of them — `managing-tasks` in `tasks.md` and in `docs-README.md` —
sat in files already copied into an adopting project, where they still read as
an instruction to run a skill that does not exist. Nothing shipped since can
reach them, and nothing tells the operator they are there.

`/sdd:setup` re-run already solves this for the largest of the five. The rules
section is fenced in `<!-- sdd:method-section -->`, so a re-run renders the
template afresh, diffs it against what is stored, and asks. The other four have
no such fence, so step 4 sees a file that exists and, correctly under the
additive rule, leaves it alone.

## Goal / Non-goals

**Goal.** A project that adopted an older version can see what the plugin has
changed in the scaffold since, and take the changes it wants — without a
re-render touching what the project has written into those files.

**Non-goals.**

- Not automatic. Nothing is rewritten without the operator seeing the diff and
  saying yes, per invariant 3.
- Not a version negotiation. There is no compatibility matrix and no migration
  script; the unit is a diff the operator reads.
- Not a seventh skill. This is a mode of `/sdd:setup`, which already holds the
  config, renders the same templates, and is documented re-runnable.
- Does not touch the artifact skeletons. `_DESIGN.md`, `_PLAN.md` and `_ADR.md`
  are read from the plugin and have never had this problem.

## Decisions

- **The plugin's region in each scaffold file is fenced by a marker pair.** →
  ADR. `<!-- sdd:scaffold -->` … `<!-- /sdd:scaffold -->`. A re-run renders the
  template and compares only what is inside. Rejected: recording the adopted
  version in `.sdd.yml`, which says *that* the versions diverged but not *where*
  — the older template is not on disk to diff against, and comparing the current
  template to a project's file reports every legitimate edit as a difference.
  Also rejected: hashing the copied files at adoption, which fails on the file
  that matters most — `tasks.md` differs from its template the moment the first
  ticket lands.
  This drops the ticket's first acceptance criterion, which named the version
  stamp as the mechanism. That criterion was written before the scaffold files
  were read closely; it guessed at how, and the how turned out to be worse than
  the alternative. What it was reaching for — a re-run that knows what moved —
  is delivered by the fence, and more precisely.
- **The marker fences guidance, not content.** Each scaffold file already splits
  in two: text the plugin authors, and a body the project authors. The marker
  records a boundary that is already there rather than inventing one.
- **The rules section keeps `<!-- sdd:method-section -->`.** It is already
  written into every project that has adopted, and a re-run recognises it. The
  two names carry two meanings: a section appended into a file the project owns,
  versus a file the plugin created. Rejected: unifying the name, which would
  make every deployed marker unrecognised — the exact failure this ticket exists
  to fix.
- **An unmarked file is never rewritten.** Where a re-run finds a scaffold file
  with no markers — every project adopted before this change — it renders the
  template, shows the operator the region it believes is the plugin's, and asks
  once. Deriving the boundary by matching text is rejected: `docs-README.md` in
  the first adopting project was already hand-edited, so a match would fail
  exactly where the stakes are highest. Follows invariant 3.
- **Upgrading is a mode of `/sdd:setup`, selected from state, not invocation.**
  Following `/sdd:canon`, which picks bootstrap, amend or audit the same way. A
  `/sdd:upgrade` alongside `/sdd:setup` would make "which do I run on a live
  project" ambiguous for something that happens once per plugin release.

## Architecture

The seam is unchanged: `.sdd.yml` gains no key. What changes is that four
scaffold files carry a fence, and `/sdd:setup` gains a fourth thing it can do
with a path that already exists.

Marker placement, one region per file:

| File | Inside the fence | Outside |
|---|---|---|
| `tasks.md` | title and the format line | `## TODO` onward — the queue |
| `roadmap.md` | the three framing paragraphs above `---` | the phases |
| `invariants.md` | title, the source-of-truth note, the HTML guidance block | the numbered rules, the layer table |
| `docs-README.md` | the whole file as shipped | anything the project appends after |
| rules section | already fenced as `sdd:method-section` | the rest of the project's file |

**Flow on a re-run.** For each of the four, in step 4 of the skill, where the
path exists:

1. Render the template from `${CLAUDE_PLUGIN_ROOT}/templates/project/`.
2. Find the fence in the project's file. Absent → report, show the rendered
   region, ask where the boundary goes, and place the markers on a yes.
3. Compare the fenced region to the rendered one. Identical → say nothing.
4. Different → show the diff and ask. On a yes, replace only what is between the
   markers.

Step 3 is the common case and must be silent: a re-run against a current project
should report "nothing to carry", not five paragraphs of agreement.

## Invariants & docs

This moves a rule, which is what makes it tier 2.

- **Invariant 2** says the scaffold is "written into the repo once, at
  adoption". Half of that stops being true: it is now also read at a re-run, to
  compare. The entry needs the second half stated, not deleted.
- **The layout responsibilities table** carries `Project scaffold … must NOT be
  read at any time other than adoption`. That row moves.
- **`layout.md`** states "Nothing under `templates/project/` is ever read after
  adoption; nothing under `templates/` directly is ever copied." The first clause
  changes; the second is untouched and is the half that matters for ADR 0002.
- **ADR 0002** is not superseded. It decided that skeletons are read rather than
  copied, and the scaffold is copied on purpose. This change does not reverse
  that; it adds the missing return path. The new ADR says so explicitly, because
  the shape will otherwise read as a partial reversal.
- `plugin-mechanics.md` describes what crosses the plugin/project boundary and
  gains the re-run direction.

## Error handling

- **Fence opened but not closed**, or closed before it opens: report the file
  and line, change nothing. A malformed fence in someone's `tasks.md` must not
  cost them their queue.
- **Two fences in one file:** same — report, touch nothing. Silently picking the
  first is how a project loses the second.
- **The project edited inside the fence:** indistinguishable from a stale
  region, and the diff is shown either way. The operator decides; the skill says
  plainly that a yes discards what is in there now.
- **A scaffold file the config names is missing entirely:** unchanged behaviour
  — create it from the template, as at adoption.
- **The rendered region is empty** because a template lost its markers: refuse
  and report. Replacing a region with nothing is never the intent.

## Testing

No runtime. What proves it works is a set of fixture repositories the check
script builds and a re-run is exercised against:

1. A project adopted at the current version — re-run reports nothing to carry.
2. A project whose fenced region is one version behind — the diff is exactly the
   changed lines, and the body outside the fence is byte-identical afterwards.
3. A project with a ticket queue in `tasks.md` — the queue survives an accepted
   upgrade of the header above it.
4. A project with no markers at all — nothing is written without an answer.
5. A malformed fence — reported, file unchanged.

Case 3 is the one that matters: it is the acceptance criterion the ticket states
in the negative, and the failure it guards against is silent.

Mechanically, `./scripts/check.sh` gains a check that every scaffold file ships
with exactly one well-formed fence — the corpus-level version of the same rule.
