# ADR 0007 — Publish under the personal account

**Status:** accepted · **Date:** 2026-08-09 · **Supersedes:** [ADR 0006](0006-org-hosts-the-catalogue-a-person-signs-the-work.md)

## Context

ADR 0006 put the catalogue under an organization account on the argument that the marketplace identifier is the expensive thing to move, so it
should be fixed first. That reasoning weighed the cost of a future move without
weighing what the name buys on the day of publication.

Two facts settle it, and neither was in evidence when 0006 was written.

**The reach is personal.** The author has an existing audience and a wide circle
of industry contacts; a new organization account has neither. A first release
travels through the channels its author already has, and here those channels
carry a person's name.

**A later move is possible and cheap.** Moving the repository to an organization
is a decision for whenever one is worth having. ADR 0006 paid a cost now to
avoid a move that may happen anyway, which is the wrong thing to optimize.

## Decision

Publish from `kremniov/sdd`. The marketplace is named `kremniov`;
`author`, the LICENSE copyright and the README sign-off name Andrey Kremnev.

The marketplace identifier carries the author's name rather than a host's. That
survives a transfer intact: after a move to an organization the name still
states who wrote it, which stays true no matter who holds the repository.

The repository is named after the product, not after what it structurally is.
It does hold a marketplace (a repo cannot be both a plugin and its own
marketplace, so the plugin sits in `plugins/sdd/`) — but `github.com/kremniov/sdd`
is the link that gets shared and remembered, and `/sdd:` is already how every
skill is invoked. ADR 0004 and 0006 preferred a catalogue name to spare a future
second plugin its own `marketplace add`; that is the same error as 0006's,
paying a cost now against a scenario that may never arrive. If a second plugin
appears, it gets its own repository and marketplace then, and nobody using this
one is disturbed.

## Alternatives

- **An organization account** — ADR 0006's choice, superseded above.
- **A host-neutral marketplace name** (`sdd-method`) so a transfer changes
  nothing. Rejected again, and for a sharper reason than in 0006: the identifier
  appears in every install and every marketplace listing, and spending that
  placement on a name that attributes nobody is the opposite of what this
  release is for.

## Consequences

If the repository later moves to an organization, GitHub redirects the path, and
the marketplace name `kremniov` stays as an attribution rather than becoming a
stale host reference. Users who installed before the move keep working; the
README's install block is what needs updating.

A near-miss worth recording: `github.com/kremnev` is a **different person**
(`VovkaKremnev`). ADR 0006 shipped that URL in the plugin manifest as the
author's link. The correct account is `kremniov`. Any identifier that names a
person is worth resolving against the API before it is published, not typed from
memory.
