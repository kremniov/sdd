---
name: subsystem
description: Use to write or update an architecture document describing how one part of the system works — its seams, what crosses them, and the order that matters. Required in the same PR when a branch changed a seam a canon document describes, or when no document covers the seam it changed.
---

# Subsystem Documents

The canon has three kinds of file. `invariants.md` holds the rules,
`layout.md` says where things live, and a **subsystem document** explains how
one part actually works — the seams inside it, what crosses them, and in which
order. It is the file that keeps an agent from re-reading the code every
session, and it is the file the docs discipline means when it says "update the
architecture doc in the same PR".

Paths come from `.sdd.yml` (`canon:`).

Reading `.sdd.yml`: one `key: value` per line; the first `:` separates them and
everything from the first `#` is a comment. Values are used verbatim — no
unquoting, no variable expansion. If the file is absent, say so and stop — the
project has not adopted this method (`/sdd:setup`). If a key this skill
needs is absent or its value is empty, name the key and ask; do not fall back to
a default path, because writing to a guessed location is how a project ends up
with two task queues.

## What earns a document

One per subsystem that has **a seam worth respecting** — a boundary where
getting it wrong is a design error rather than a bug. Symptoms that one is due:

- Work in this area keeps rediscovering the same constraint by reading code.
- An invariant names it but cannot explain it in one line.
- Two modules interact in an order that is not obvious from either one.

Not one per directory, and not one per package. A subsystem with no seam gets a
line in `layout.md` instead. Ten subsystem documents in a codebase of thirty
modules means most of them are describing structure that `layout.md` already
covers.

## Shape

No fixed skeleton — a turn pipeline and a storage layer do not have the same
shape, and forcing them into shared headers produces empty sections. What every
one of them must answer:

- **What it is responsible for**, in a sentence, and what it deliberately is
  not. The "not" line is the one that settles arguments.
- **The seams**: what crosses this boundary, in which direction, and what must
  never cross it. Name the type or the function where one exists.
- **The order that matters**: what must happen before what, and what breaks when
  it does not. This is what a reader cannot recover from any single file.
- **Which invariants govern it**, by number. Link — never restate; a copy here
  and a rule there drift, and then two documents disagree.

Length follows the seam count, not the code size. A subsystem with one boundary
and a clear order is a screen. Past two screens, check whether it is two
subsystems.

## Writing one

**1. Read the code first**, then any existing document. Reading the document
first makes you edit prose rather than describe the system, and a document that
has drifted reads convincingly.

**2. Trace one real path end to end** — a request, a job, a message. The order
that matters falls out of a trace and rarely out of a file-by-file reading.

**3. Say what the code cannot.** A list of the files in the directory is not a
subsystem document: the reader can run `ls`. What they cannot get cheaply is
why the boundary is where it is, and what happens if they cross it.

**4. State what is true now.** No history, no "we used to", no "this will
later". A dated decision belongs in an ADR; a future intention belongs in the
roadmap. A subsystem document that carries either becomes a file readers must
date-check before trusting.

## Updating one

This is the common case, and it runs on the branch that changed the seam —
in the same PR, before integration.

Read the diff, then ask: does any sentence in this document contradict what
just landed? Two failure modes, both frequent:

- The document is now **wrong** — it describes the old order or the old
  boundary. Fix the sentence, not the whole file.
- The document is now **incomplete** — the branch added a seam it does not
  mention. Add it where it belongs in the flow, not as an appendix at the end.

A document that needed no change is a normal outcome; say so. Rewriting a file
because you touched the subsystem is how a canon accumulates churn without
gaining accuracy.

When a branch changed a seam and *no* document covers that subsystem, that is
the trigger to write one — the seam just proved it is worth respecting.

## Checking a document is still true

Cheap and worth doing when work in an area feels like it is fighting the docs:
take each claim and find the code that makes it true. A claim you cannot ground
is either stale or was always aspirational. Report those rather than quietly
deleting them — a claim nobody can ground may be a rule the code has silently
stopped obeying, which is a finding about the code, not about the document.
