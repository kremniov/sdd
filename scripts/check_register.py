"""Check instruction size/depth and report advisory negation frequency."""

import re
import sys
from pathlib import Path

RESIDENT = Path("plugins/sdd/templates/project/CLAUDE.section.md")
NEGATION = re.compile(r"\b(?:not|never|no|only|without)\b|\brather than\b", re.I)
WORD = re.compile(r"[A-Za-z][A-Za-z'-]*")
HEADING = re.compile(r"^(#{1,6}) ", re.M)
WORDS_SKILL = 1200
WORDS_RESIDENT = 400
DEPTH = 3


def prose_only(text):
    lines = []
    marker = None
    width = 0
    for line in text.splitlines():
        fence = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            if fence and fence[1][0] == marker and len(fence[1]) >= width and not fence[2].strip():
                marker = None
            continue
        if fence:
            marker, width = fence[1][0], len(fence[1])
            continue
        lines.append(line)
    return "\n".join(lines)


def shipped():
    return sorted(set(Path("plugins/sdd/skills").rglob("*.md")) |
                  set(Path("plugins/sdd/templates").rglob("*.md")))


def measure(path):
    text = path.read_text()
    prose = prose_only(text)
    words = len(WORD.findall(prose))
    density = 100 * len(NEGATION.findall(prose)) / words if words else 0.0
    depth = max((len(h) for h in HEADING.findall(prose)), default=0)
    return len(WORD.findall(text)), words, density, depth


def is_resident(path):
    return path.name == RESIDENT.name and path.parent.name == "project"


def main(args=None):
    args = sys.argv[1:] if args is None else args
    paths = set()
    if args:
        for arg in args:
            path = Path(arg)
            if not path.exists():
                print(f"  FAIL    missing input: {path}")
                return 1
            paths.update(path.rglob("*.md") if path.is_dir() else [path])
    else:
        paths.update(shipped())
    if not paths:
        print("  FAIL    no Markdown inputs")
        return 1
    ok = True
    totals = {}
    for path in sorted(paths):
        total, prose, density, depth = measure(path)
        totals[path] = total
        limit = WORDS_RESIDENT if is_resident(path) else WORDS_SKILL if path.name == "SKILL.md" else None
        faults = []
        if limit and total > limit:
            faults.append(f"{total} total words over {limit}")
        structured = path.name == "SKILL.md" or is_resident(path) or path.name.startswith("_")
        if structured and depth > DEPTH:
            faults.append(f"heading depth H{depth} over H{DEPTH}")
        if faults:
            print(f'  FAIL    {path}: {"; ".join(faults)}')
            ok = False
        else:
            print(f"  OK      {path}: {total} total words, {prose} prose words, {density:.2f} negations per 100")
        signal = 2.0 if is_resident(path) else 2.5
        if density > signal:
            print(f"  NOTE    {path}: negation frequency exceeds review signal {signal}; inspect wording")
    if not args:
        for skill in sorted(Path("plugins/sdd/skills").glob("*/SKILL.md")):
            full = sum(total for path, total in totals.items() if path.is_relative_to(skill.parent))
            print(f"  SIZE    {skill.parent.name}: {full} words including all local references")
        print(f"  SIZE    corpus: {sum(totals.values())} words including examples and migration history")
        print("  NOTE    reference totals are potential loads, not a measured session; counts do not prove clarity")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
