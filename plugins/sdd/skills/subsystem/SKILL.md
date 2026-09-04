---
name: subsystem
description: Use to write or update the architecture document for one part of the system — its seams, what crosses them, and the order that matters. Required in the same pull request when a branch changed a seam a document describes, or changed a seam no document covers.
---

# Subsystem documents

A subsystem document explains how one part of the system works: the seams inside
it, what crosses them, and in which order. It sits in `canon:` beside
`invariants.md`, which holds the rules, and `layout.md`, which says where things
live.

This is the file that saves an agent from re-reading the code every session, and
the file the docs discipline means by "update the architecture document in the
same pull request".

Paths come from `.sdd.yml` (`canon:`). One `key: value` per line; everything from
the first `#` is a comment; values are used verbatim. If the file is absent, say
so and stop — the project has not adopted this method (`/sdd:setup`). If a key
this skill needs is absent or empty, name the key and ask.

## What earns a document

One per subsystem that has a seam worth respecting — a boundary where getting it
wrong is a design error rather than a bug. Three symptoms that one is due:

- Work in this area keeps rediscovering the same constraint by reading code.
- An invariant names it and cannot explain it in one line.
- Two modules interact in an order that neither of them shows.

A subsystem with no seam gets a line in `layout.md` instead. Ten documents in a
codebase of thirty modules means most of them describe structure `layout.md`
already covers.

## Shape

There is no fixed skeleton: a turn pipeline and a storage layer have different
shapes, and shared headers produce empty sections. Every document answers four
things.

| Question | What closes it |
|---|---|
| What is it responsible for | One sentence, and one more saying what it deliberately is not. The second sentence settles arguments |
| What are the seams | What crosses this boundary, in which direction, and what must stay on its side. Name the type or the function |
| What order matters | What happens before what, and what breaks otherwise. This is what a reader cannot recover from any single file |
| Which invariants govern it | By number, as links. A copy here and a rule there drift into two documents that disagree |

Length follows the seam count, not the code size. One boundary and a clear order
is a screen. Past two screens, check whether this is two subsystems.

## Writing one

1. **Read the code first**, then any existing document. Reading the document
   first makes you edit prose instead of describing the system, and a document
   that has drifted reads convincingly.
2. **Trace one real path end to end** — a request, a job, a message. The order
   that matters falls out of a trace and rarely out of a file-by-file reading.
3. **Say what the code cannot.** A list of the files in the directory is what
   `ls` prints. What a reader cannot get cheaply is why the boundary sits where
   it does, and what happens on crossing it.
4. **State what is true now.** A dated decision belongs in an ADR, a lesson in
   `lessons.md`, and a future intention in the roadmap.

## Updating one

This is the common case. It runs on the branch that changed the seam, in the same
pull request, before integration.

Read the diff, then ask whether any sentence in this document contradicts what
landed. Two failure modes, both frequent:

- The document is **wrong**: it describes the old order or the old boundary. Fix
  the sentence, and leave the rest of the file alone.
- The document is **incomplete**: the branch added a seam it omits. Add it where
  it belongs in the flow, rather than as an appendix.

A document that needed no change is a normal outcome. Say so.

Where a branch changed a seam and no document covers that subsystem, that is the
trigger to write one: the seam has just proved it is worth respecting.

## Checking one is still true

Worth doing when work in an area feels like it is fighting the documents. Take
each claim and find the code that makes it true. Report a claim you cannot ground
rather than deleting it: it may name a rule the code has silently stopped
obeying, which is a finding about the code.
