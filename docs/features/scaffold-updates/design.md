# Scaffold updates — design

**Ticket:** T-7 · **Plan:** [plan.md](plan.md)

## Problem

The fence from T-6 tells a re-run *where* the plugin's half of a scaffold file
ends. It does not tell it *what* is inside. The `Different` branch of
`/sdd:setup` step 4 therefore reads any textual difference as staleness and
offers to replace the region wholesale, warning that a yes discards whatever is
there.

The first upgrade against a real prior adoption showed the assumption behind
that branch is false. The project had rewritten the plugin's guidance in its own
terms — its own ticket-id convention, its own cross-references, its own phrasing
of the same rules — and the fence now surrounds *that* text. Nothing
distinguishes it from a region that has genuinely fallen behind. The next re-run
would offer to overwrite deliberate wording, and the operator would be answering
a question the skill cannot pose honestly: it does not know what it would be
taking away.

The failure is worse than a bad prompt. A project that answers yes loses its own
prose; a project that learns to answer no stops receiving corrections. Either
way the fence stops delivering the thing it was built for.

## Goal / Non-goals

Make a re-run able to say what changed in the plugin's guidance since this
project last took it, and apply that change to the project's wording rather than
in place of it.

Not in scope: shipping template history, or any ability to reconstruct what the
region looked like at an earlier version. Not in scope: touching anything
outside a fence, or the `no fence` and `malformed` branches, which T-6 settled.
Not in scope: making the update non-interactive — every carry is still the
operator's yes.

## Decisions

- **The version stamp lives in the opening marker**, `<!-- sdd:scaffold v0.3.0 -->`,
  not in `.sdd.yml`. Rejected: one stamp per project — the files are updated
  independently and a declined carry must leave its own file behind without
  lying about the rest. `→ ADR`
- **A template's stamp is the version in which that region last changed**, not
  the current plugin version. Rejected: stamping every file on every release —
  it would make every file look stale at every upgrade, which is the same
  false positive in a new coat.
- **Equal stamps end the comparison**: the region is current, whatever its text
  says. This is the whole of acceptance criterion 1 — a difference is the
  project's edit, and the plugin has nothing to say about it. `→ ADR`
- **What is offered comes from a shipped change log**, `templates/project/CHANGES.md`,
  which describes each change in its own terms. Rejected: diffing the rendered
  template against the project's text — that reproduces exactly the comparison
  that fails today.
- **A fence with no stamp is read as `v0.2.0`**, the version that introduced the
  fence. It is a true lower bound rather than a guess, so nothing needs asking.
- **A declined carry does not advance the stamp**, so it is offered again on the
  next run. Rejected: recording the refusal — a second mechanism to store state
  in someone's file, to avoid re-asking a question that is cheap to re-ask.

## Architecture

Three pieces, one seam.

**The stamp.** `check_scaffold.py` already requires exactly one well-formed
fence per scaffold file. The opener grows an optional-in-form, mandatory-in-fact
version: `<!-- sdd:scaffold v0.3.0 -->` and, for the rules section,
`<!-- sdd:method-section v0.3.0 -->`. The closer stays bare — it carries no
information and a second copy of the version is a second thing to get wrong.

**The change log.** `templates/project/CHANGES.md` holds one section per
version, and under it one entry per scaffold file that changed in that version.
An entry says what the guidance now says and what it replaced, in prose an agent
can apply to text that is worded differently. It is not a diff: a diff against
the template is meaningless to a project whose region shares no sentences with
it. Versions with no scaffold change get no section.

**The skill.** Step 4's `Different` branch is replaced by a stamp comparison.
Project stamp equal to the template's: silence. Behind it: read the entries
between the two, present each on its own, and on a yes edit the project's region
to carry that change — preserving the project's wording, its ticket ids, its
cross-references. On a no, or where the project's text already says what the
entry describes, leave the region alone. The stamp advances only when every
entry for the file has been carried or found already satisfied.

Step 5 (the rules section) follows the same comparison rather than keeping its
own diff-and-ask branch, so there is one mechanism and not two.

Flow, for one file: read the project's opener → parse the stamp, defaulting to
`0.2.0` → compare with the template's opener → equal, or a list of entries →
one question per entry → edits inside the fence → rewrite the opener with the
template's version, if and only if the list was exhausted.

## Invariants & docs

Invariant 2 governs the scaffold and is amended: a fence must carry a version,
and the comparison is stamp-first. Its *Detect* clause gains the stamp
requirement, which `check_scaffold.py` enforces.

No invariant moves; the rule that the scaffold is read only to compare is the
same rule, made executable. The layout table's scaffold row is amended for the
change log.

ADR 0011 is owed for the two lines marked above. It stands beside ADR 0009
rather than superseding it: the fence answers *where*, the stamp answers *what
changed*, and 0009 rejected a bare version stamp only as a replacement for the
fence.

## Error handling

A stamp that does not parse as a version is a malformed fence: report the file
and the line, change nothing. Same treatment as the other malformations, and for
the same reason — a broken marker must not cost anyone their queue.

A project stamp ahead of the template's means an older plugin is installed over
a newer adoption. Say so and stop for that file; downgrading someone's guidance
is not a thing this skill does silently.

A change-log entry naming a version that no template stamp reaches is a gate
failure in this repository, not a runtime condition: it means a release
described a change it did not ship.

## Testing

`check_scaffold.py` grows three cases: every opener carries a parsable version,
no version exceeds the plugin's own, and every version named in `CHANGES.md`
matches the stamp of the file it names. A fourth check compares each fenced
region against `HEAD` and fails when the region changed without its stamp
advancing — the one failure mode that produces silence downstream rather than
an error.

Behaviour lands where a checker cannot reach: against the project whose fenced
regions hold its own prose. The carry must land and the wording must survive.
That is an operator step, and the plan marks it `[gate]`.
