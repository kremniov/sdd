# ADR 0006 — The organization hosts the catalogue; a person signs the work

**Status:** superseded by [ADR 0007](0007-publish-under-the-personal-account.md) · **Date:** 2026-08-09

## Context

Publishing raised a question with no technical answer: release under a personal
GitHub account, or under an organization account with no public presence yet.

The pull in both directions is real. An early developer tool earns trust from a
named person, not a logo: an empty organization can read as a startup that may
not be there next year, which is *weaker* than an individual with a visible
history. Against that, a catalogue address is the one string users paste into
their own configuration, and moving it later costs them rather than us.

Checked before deciding: the free organization plan permits unlimited public
repositories, anonymous public reads, issues, releases, and unlimited Actions
minutes on public repos. Nothing in this project's needs sits behind a paid
tier.

## Decision

Split hosting from authorship, because they are separate facts and only one of
them is expensive to change.

- **The organization hosts** a catalogue repo, so a second plugin needs no
  second `marketplace add` from anyone, and the marketplace takes the
  organization's name.
- **A person signs.** `author` in the plugin manifest, the LICENSE copyright,
  and a short "Who made this" line in the README all name Andrey Kremnev and
  link to the personal account.

The organization here is a stable address, not a claim about headcount. Nothing
in the repository asserts a company, a team, or support commitments that a
one-person project cannot keep.

## Alternatives

- **Personal account throughout.** Strongest early trust signal, and a later
  move to an organization keeps working through GitHub's redirect — but the
  marketplace *name* stays whatever it was minted as, so every existing user
  keeps `sdd@kremnev` after the move. The redirect fixes the URL, not the
  identifier.
- **A neutral marketplace name** (`sdd-method`) on a personal repo, making a
  future move free. Rejected as too clever: the identifier then names nobody,
  which trades a small future cost for a permanent loss of attribution at the
  point users see it most often.
- **Organization branding throughout**, with the person invisible. Rejected on
  the trust argument above, and because it would be misleading — there is no
  company yet, and a README that implies one is a promise to a reader.

## Consequences

The marketplace identifier is now the expensive thing to change, and it is the
one deliberately fixed first. If the organization is ever renamed or abandoned,
existing installs break in a way a personal account would not have — accepted,
because the same risk applies to any hosted identifier and the organization is
already owned.

The README carries a personal voice and an invitation for issues. That is a
commitment: an unanswered issue tracker under a personal name reads worse than
under a logo. If the project stops being maintained, saying so in the README is
part of the deal made here.
