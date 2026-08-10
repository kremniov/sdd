# Scaffold upgrade — plan

**Ticket:** T-6 · **Design:** [design.md](design.md)

## Scope

When the last step is green, the four unfenced scaffold files ship with a
`<!-- sdd:scaffold -->` region, `./scripts/check.sh` rejects a scaffold file
whose fence is missing or malformed, and `/sdd:setup` carries a fourth branch in
step 4: a path that exists and whose fenced region has moved. Executes
[design.md](design.md).

Left for a follow-up: nothing in the ticket. Deliberately not here — a command
that upgrades without a conversation, and any notion of plugin version
compatibility.

## Order

The fences come first: the check that enforces them and the skill that reads
them both need a corpus that has them. The check precedes the skill because a
malformed fence must be a build failure here before it is a runtime branch in
someone else's repository. The fixtures come last, because they exercise the
finished behaviour, and the canon update last of all — it records what became
true, and until step 4 it is not yet true.

## Steps

### Step 1 — The four scaffold files carry a fence

**Goal:** `tasks.md`, `roadmap.md`, `invariants.md` and `docs-README.md` each
carry exactly one `<!-- sdd:scaffold -->` … `<!-- /sdd:scaffold -->` pair, around
the region named in design.md §Architecture.

**Constraints:** the boundary is the one already there — guidance inside,
project-authored body outside. `CLAUDE.section.md` is not touched; it keeps
`sdd:method-section` (design.md §Decisions).

**Touches:** `plugins/sdd/templates/project/{tasks,roadmap,invariants,docs-README}.md`.

**DoD:** `./scripts/check.sh` green, and for each of the four the text outside
the fence is byte-identical to what it was before this step.

### Step 2 — The gate rejects a malformed fence

**Goal:** `scripts/check_scaffold.py` fails when a shipped scaffold file has no
fence, an unclosed fence, a closer before its opener, or more than one pair.
`CLAUDE.section.md` is checked against its own marker name.

**Constraints:** python3 only, no new dependency (layout table, Checks row).

**Touches:** `scripts/check_scaffold.py`, `scripts/check.sh`.

**DoD:** the checker run against four mutations — fence removed, closer removed,
order swapped, pair duplicated — exits non-zero on each and names the file;
`./scripts/check.sh` green on the real tree.

### Step 3 — `/sdd:setup` reads the fence and offers what moved

**Goal:** step 4 of the skill gains the branch for a path that exists: render,
locate the fence, compare, and where they differ show the diff and ask. Silent
when they agree.

**Constraints:** nothing is written without a yes (invariant 3). Only the region
between the markers is replaced. An absent fence is reported and asked about,
never derived by matching text (design.md §Decisions). A malformed fence is
reported and the file left alone (design.md §Error handling).

**Touches:** `plugins/sdd/skills/setup/SKILL.md` steps 4 and 6.

**DoD:** `./scripts/check.sh` green; the skill states each of the four outcomes
— absent, malformed, identical, differing — and the report in step 6 names what
was carried and what was declined.

### Step 4 — The canon records that the scaffold is read again

**Goal:** invariant 2, the layout responsibilities table, `layout.md` and
`plugin-mechanics.md` say what is now true.

**Constraints:** invariant 2 is amended, not replaced — its numbering is stable
(invariant 8) and ADR 0002 is not superseded (design.md §Invariants & docs).

**Touches:** `docs/architecture/invariants.md`, `docs/architecture/layout.md`,
`docs/architecture/plugin-mechanics.md`.

**DoD:** `./scripts/check.sh` green — the canon checker requires *Detect* and
*On violation* on the amended entry — and no document still claims the scaffold
is never read after adoption.

### Step 5 [gate] — A real upgrade against a project adopted at an older version

**Goal:** the behaviour is exercised end to end, by the operator, against a
repository that adopted before the fence existed.

**Constraints:** the project's queue and phases survive; only the fenced regions
change, and only after a yes.

**Touches:** nothing in this repo.

**DoD:** run `/sdd:setup` in a project adopted at 0.1.x. It reports the four
files as unfenced, proposes the boundary for each, and after the operator
accepts, `git diff` in that repository shows changes only inside the new
markers. The stale `managing-tasks` line in its `tasks.md` is gone.

## Verification

`./scripts/check.sh` for every step. Step 5 is the operator's, run in an
adopting repository rather than here — the fixtures in design.md §Testing prove
the mechanics, and only a real project proves the boundary was placed where its
content actually is.

## Docs & ADR

Step 4 carries the canon. One decision is marked `→ ADR` in design.md — the
fenced region as the upgrade mechanism — and needs an ADR before merge, written
to say plainly that it does not reverse ADR 0002.
