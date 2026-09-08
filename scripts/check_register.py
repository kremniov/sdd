"""Shipped text is measured: length, heading depth, negation density."""

import glob
import re
import sys

RESIDENT = "plugins/sdd/templates/project/CLAUDE.section.md"

# not / never / no / only / without / rather than — the set the v2 baseline used.
NEGATION = re.compile(r"\b(?:not|never|no|only|without)\b|\brather than\b", re.I)
WORD = re.compile(r"[A-Za-z][A-Za-z'-]*")
FENCE = re.compile(r"^```.*?^```", re.M | re.S)
HEADING = re.compile(r"^(#{1,6}) ", re.M)

DENSITY = 2.5
DENSITY_RESIDENT = 2.0
WORDS_SKILL = 1200
WORDS_RESIDENT = 400
DEPTH = 3


def shipped():
    return sorted(
        glob.glob("plugins/sdd/skills/*/*.md")
        + glob.glob("plugins/sdd/templates/*.md")
        + [
            p
            for p in glob.glob("plugins/sdd/templates/project/*.md")
            if not p.endswith("CHANGES.md")
        ]
    )


def measure(path):
    """Prose only: fenced blocks are examples, not instructions."""
    text = open(path).read()
    prose = FENCE.sub("", text)
    words = WORD.findall(prose)
    negations = NEGATION.findall(prose)
    density = 100 * len(negations) / len(words) if words else 0.0
    depth = max((len(h) for h in HEADING.findall(prose)), default=0)
    return len(words), density, depth


def nests(path):
    """A scaffold file the project fills carries headings as content, not structure."""
    return path.endswith("/SKILL.md") or path == RESIDENT or "/templates/_" in path


def budgets(path):
    if path == RESIDENT:
        return WORDS_RESIDENT, DENSITY_RESIDENT
    if path.endswith("/SKILL.md"):
        return WORDS_SKILL, DENSITY
    return None, DENSITY


paths = sys.argv[1:] or shipped()
ok = True
for path in paths:
    words, density, depth = measure(path)
    limit, ceiling = budgets(path)
    faults = []
    if limit and words > limit:
        faults.append(f"{words} words over {limit}")
    if density > ceiling:
        print(f"  NOTE    {path}: {density:.2f} negations per 100; review wording (signal {ceiling})")
    if nests(path) and depth > DEPTH:
        faults.append(f"heading depth H{depth} over H{DEPTH}")
    if faults:
        print(f'  FAIL    {path}: {"; ".join(faults)}')
        ok = False
    else:
        print(f"  OK      {path}: {words} words, {density:.1f} negations per 100")

sys.exit(0 if ok else 1)
