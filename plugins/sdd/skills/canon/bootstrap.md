# Bootstrap a canon

Run this when `invariants.md` holds no rules yet. It costs hours and reads the
codebase.

## 1. Read the code, not the docs

Ignore the existing architecture prose on the first pass. It may describe an
intention the code abandoned. Where the two disagree the code is the fact, and
the disagreement is a finding worth reporting.

Cover, in this order:

| What | What to look for |
|---|---|
| The shape | Top-level directories, the module graph, the entry points. What depends on what, and what conspicuously does not |
| The boundaries | Where a layer stops. A directory that imports narrowly among neighbours that import widely is a rule someone enforces by hand |
| The repeated pattern | The same construction in five places is a convention; in twenty, an invariant. Read enough instances to tell which |
| What a machine checks | Lint config, CI steps, custom scripts, codegen, hooks. Read the checker: its real coverage is routinely narrower or wider than the docs claim |
| What the tests assert about structure | An architecture test, an import-cycle check, a golden file of the public API |
| The exceptions | A rule followed in 19 places and broken in the 20th. Find out which one is the mistake, and ask where that is unclear |

For a large codebase, sample: the entry points, the two or three busiest modules,
the newest module for the current convention, and the oldest for what changed.

## 2. Draft

Run every candidate through the falsifiability filter in `SKILL.md`, Amend.

Cut to fifteen before presenting. Rank them: mechanically enforced first, then
those whose violation is a bug, then the rest. List the cut candidates in one
line each underneath, so the user can pull one back.

## 3. Confirm

Present the candidates as a numbered list, one line each, in file order, marking
which ones a machine enforces. Ask the user to strike what they disagree with and
to name what is missing. They hold the rules that live only in their head, which
is what this exercise is for.

Flag these three apart from the list:

- **Contradictions** — the code does X here and not-X there.
- **Code and doc disagreements** found despite step 1.
- **Rules that look like accidents** rather than decisions.

## 4. Write

Fill the body of the `invariants.md` that adoption placed under `canon:`, in the
entry format. Where that file is absent, the project has not adopted this method:
run `/sdd:setup` instead of creating it here.

`layout.md` says where things live: a directory map with one line of purpose
each, the entry points, and where a newcomer starts reading. A reader who wants a
file listing runs `ls`.

Both files state what is true now. History belongs in an ADR.

## 5. When there is nothing to find

A codebase can hold no discernible rules: too new, too small, or inconsistent
enough that any statement would be a wish. Say so and write nothing. A
speculative list gets linked, cited and defended in review as though someone had
observed it.

The honest output is a short note in `invariants.md` saying the canon is not yet
established, plus two or three rules worth adopting deliberately as the codebase
grows.
