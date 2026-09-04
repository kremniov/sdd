# Carrying a scaffold change

Each scaffold file is two things: guidance this plugin wrote, and a body the
project wrote — its queue, its phases, its rules. The plugin's half is fenced,
and the opening marker carries the version whose guidance is inside.

## Compare the stamps, never the text

Read the version on the project's opener and the version on the template's.

| Stamps | What you do |
|---|---|
| Equal | The region is current, whatever its wording. Say nothing about that file. A project that rewrote the guidance in its own terms, with its own ticket ids and cross-references, is current |
| The project is behind | Read `${CLAUDE_PLUGIN_ROOT}/templates/project/CHANGES.md`. Take the entries for that file above the project's version and up to the template's — the project already holds what its own stamp names. Put each entry to the user on its own, in its own terms. On a yes, edit their region to carry what the entry describes, keeping their wording, their ids and their references. An entry their text already states is satisfied: say so and move on. Then set the stamp to the highest version whose entries were all carried or already true |
| The project is ahead | An older plugin is installed over a newer adoption. Report it and leave the file alone |
| No version on the fence | The project adopted while the markers were bare. The lower bound is `v0.2.0`, the version that introduced them. That is a fact, so proceed from it |
| No fence at all | The project adopted before the markers existed. Show the region you would fence and ask once. Place the markers on a yes, stamped `v0.2.0`. Today's version would declare the file up to date and silence every change since. Derive the boundary by asking: matching text against the template fails on a hand-edited header, which is where a wrong guess costs most |
| Malformed | Opened and not closed, closed before opened, more than one pair, or a version that is not `N.N.N`. Report the file and the line, and change nothing. A broken marker in someone's `tasks.md` puts their queue at risk |

Keep the region exactly where it is. What a re-run offers is a described change,
applied to the text that is there. The full text of the current template answers
a question nobody asked.

Stopping at the last complete version keeps the re-offer to what was actually
refused. Leaving the stamp at the bottom would re-offer accepted entries too, and
they would then be filtered by an agent's judgement about what the text already
says rather than by a recorded fact.

## Retiring the v0.x rules section

A project adopted before v1.0.0 carries an `<!-- sdd:method-section -->` fence.
That region holds the whole method: the tier table, the artifact locations, the
plan rules, the review scales, and the invariant, decision-record and docs
triggers. Version 1.0.0 keeps five rules resident and moves the rest into
`/sdd:work`, so the region is replaced rather than updated.

This is the one deletion adoption makes, and it is bounded:

1. Show the whole region, in full, before touching it.
2. Say what replaces it: the rendered `sdd:rules` section, plus `/sdd:work` for
   everything else.
3. Ask once.
4. On a yes, replace that region and nothing else. A rules file that describes a
   method also carries things that are not the method — this project's own
   conventions, its paths, a rule it earned once and wrote down. Carry those
   across into the new region and say which lines you kept.
5. On anything else, leave the region alone and leave the `sdd:rules` fence unwritten.
   Report that the project runs the v0.x rules while the installed skills expect
   the v1 frame, and offer the question again on the next run.

Two method sections in one file are never written.

A replaced method leaves references behind. Its skill paths and command names are
cited from the project's own docs, and those citations now dangle. Find them,
propose each fix, and show the user the list. The files stay where they are:
unreferenced is a different thing from unwanted.
