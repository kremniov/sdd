# ADR 0016 — The party who directs the work is the user

**Status:** accepted · **Date:** 2026-09-04 · **PR:** [#6](https://github.com/kremniov/sdd/pull/6)

## Context

Every shipped file called that party the **operator**. The word was chosen to
separate the person running the session from the end user of the software being
built, and it did that job.

The harness system prompt says **user** everywhere and says operator nowhere. Its
own rules about confirming irreversible or outward-facing actions are written
about the user. This method writes the same rules about the operator and expects
them to land on the same rails, so each reading costs an unwritten translation
step — and it costs most on the rules that matter most.

Field observation 1 supports this. An agent left branches unpushed and opened no
pull request, and the leading explanation was that the text grouped `push` with
`git merge`. The integration rule also used a word the model does not hold
natively, while a harness rule about confirmation sat next to it in the native
one.

## Decision

The party who directs the work is the **user**. Where the other party needs a
name, it is the **end user**.

The rename covers every shipped file: skills, artifact skeletons, the project
scaffold, the change log, the canon, the roadmap, the queue and the README.

Two kinds of file are exempt, on the ground invariant 11 already states for
retired skill names. Decision records quote the vocabulary of their own date on
purpose, so ADR 0001 to ADR 0015 keep the word. Feature designs and plans are
frozen at merge and keep it too.

## Alternatives

- **Keep `operator` and state the equivalence once in the resident set.** The
  translation then happens once instead of every reading — but it still happens,
  and it consumes a line of the smallest budget in the method.
- **Keep `operator` in shipped text and use `user` in conversation.** Leaves the
  two vocabularies unreconciled in the one place a reader would look.
- **Introduce a third word for both.** Costs the rename and gains nothing the
  harness already understands.

## Consequences

`./scripts/check.sh` greps for the word across shipped text, the canon and the
README, and fails on it. The exemption is expressed as the paths it does not
scan, so a decision record needs no marker.

The word appears in fifteen accepted ADRs and in four frozen feature designs.
A reader meeting it there is reading a record of what was decided when, which is
what those files are for.
