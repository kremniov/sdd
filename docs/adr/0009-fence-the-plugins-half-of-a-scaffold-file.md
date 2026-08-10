# ADR 0009 — The plugin's half of a scaffold file is fenced, so a correction can reach a project that already adopted

**Status:** accepted · **Date:** 2026-08-10

## Context

ADR 0002 split the files this plugin ships in two. Artifact skeletons are read
in place from `${CLAUDE_PLUGIN_ROOT}`, so a fix reaches every consumer on
update. Scaffold files are copied into a repository at adoption and belong to
the project from then on — deliberately, because a project must be able to write
its own tickets into its own queue without the plugin having opinions about
them.

The second half of that split had no return path. In 0.1.3 six pre-rename skill
names were corrected; two of them — `managing-tasks` in `tasks.md` and in the
docs guide — were already sitting in files copied into an adopting project,
where they still read as an instruction to run a skill that does not exist.
Nothing shipped afterwards could reach them, and nothing told the operator they
were there.

The rules section never had this problem: it is fenced in
`<!-- sdd:method-section -->`, so a re-run of `/sdd:setup` renders the template,
diffs the stored section, and asks. Four files had no such fence, so the same
step correctly left them alone.

## Decision

Each scaffold file carries exactly one `<!-- sdd:scaffold -->` …
`<!-- /sdd:scaffold -->` pair around the region the plugin authored. A re-run of
`/sdd:setup` renders the template, compares only that region, and where it
differs shows the diff and asks; on a yes it replaces what is between the
markers and nothing else. Everything outside the fence is the project's and is
not read, not diffed, and not written.

The fence records a boundary that was already there. Every one of these files
was already two things — guidance the plugin wrote, and a body the project
writes — and the markers only make that split machine-readable.

## Alternatives

- **Record the adopted version in `.sdd.yml`** — knows *that* the versions
  diverged, not *where*. The older template is not on disk to diff against, and
  comparing the current template to a project's file reports every legitimate
  edit as a difference.
- **Hash each copied file at adoption** — distinguishes "the project edited
  this" from "the plugin moved", but fails on the file that matters most:
  `tasks.md` stops matching its hash the moment the first ticket lands.
- **Unify the marker name across all five files** — tidier, and it would orphan
  every `sdd:method-section` marker already written into a project. That is the
  exact failure this decision exists to prevent.
- **Derive the boundary by matching the template's text** in a file that has no
  fence — the first adopting project had already hand-edited the docs guide, so
  the match would fail precisely where a wrong guess costs most. The skill asks
  instead.

## Consequences

**This does not reverse ADR 0002.** Skeletons are still read and never copied;
the scaffold is still copied and owned by the project. What changes is that the
copy is no longer unreachable: the template is read once more, as a comparand
rather than a source. The shape will read as a partial reversal to anyone who
meets it later, which is why it is written down here.

Invariant 2 gains that second read, and its *Detect* now requires a
well-formed fence — `scripts/check_scaffold.py`, which rejects a scaffold file
whose fence is missing, unclosed, inverted, duplicated, or empty. The layout
responsibilities row and `plugin-mechanics.md` changed with it.

The cost lands on projects: two lines of HTML comment in four files. Projects
that adopted before this exists have no fence at all, and a re-run has to ask
them once where the boundary goes — a one-time conversation per repository, and
the alternative was guessing.
