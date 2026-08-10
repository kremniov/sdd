# ADR 0004 — Skills are named after what they work on, not what they do

**Status:** accepted · **Date:** 2026-08-09

## Context

The first six skills inherited gerund names from the corpus this method was
written to replace: `adopting-sdd`, `deriving-canon`, `documenting-subsystems`,
`brainstorming`, `managing-tasks`, `systematic-debugging`. Listed together the
set had three problems.

`adopting-sdd` repeated the plugin name that already prefixes every invocation —
`/sdd:adopting-sdd`. The names mixed two genres: `brainstorming` and
`systematic-debugging` name an activity, while `adopting`/`deriving`/
`documenting` are commands. And the longest were three words for skills invoked
often.

Naming is cheap to change only before publication. Afterwards every adopting
project's rules file carries the old names, and a rename breaks their pointers.

## Decision

Name a skill after the artifact or subject it works on: `setup`, `canon`,
`subsystem`, `design`, `tasks`, `debug`.

The namespace supplies the verb-like reading — `/sdd:canon` is understood as
"the SDD canon skill" — so the name carries the object instead. An agent
searching for a skill searches by subject ("the invariants need a line") more
often than by verb.

Because the names are short, the frontmatter `description` becomes the only
selection signal. Each one states its trigger — when to reach for the skill —
rather than paraphrasing the name.

The marketplace takes the account name, the plugin is `sdd`. The account appears
once, in `marketplace add`; the identifiers seen repeatedly stay short.
*(The marketplace was later renamed `kremniov` — see [ADR 0007](0007-publish-under-the-personal-account.md).
The skill names decided here are unaffected.)*
The repository is a catalogue (`claude-plugins`), not one plugin's repo, so a
second plugin needs no second `marketplace add` from every user.

## Alternatives

- **Keep the gerunds, fix only the stutter** — leaves two genres in one list.
- **`rootcause` instead of `debug`** — more precise about the procedure, less
  likely to be found by someone with a failing test.
- **The account name as the plugin name too** — repeats a token at every
  invocation to no benefit; the marketplace already carries the identity.

## Consequences

Six invocations are one word each after the namespace. `debug` is the one name
that is a verb, kept because it has no artifact and is what a person searching
would type.

Descriptions now carry the full weight of skill selection and must be maintained
as the trigger changes — a description that drifts silently stops the skill from
being found. `scripts/check.sh` enforces only their presence and length; whether
one still describes the right moment needs a reader.
