"""Check scaffold boundaries, template stamps and the migration journal.

A stamp names the template version a project received. It advances when the
guidance changes and never decreases. The journal lists structural migrations
that a comparison with the current template cannot derive."""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

MARKERS = {
    "CLAUDE.section.md": "sdd:rules",
}
DEFAULT = "sdd:scaffold"

ROOT = Path("plugins/sdd/skills/setup/templates/project")
JOURNAL = Path("plugins/sdd/skills/setup/migrations.md")
CONDITION = "**Applies when:**"
CEILING = json.loads(Path("plugins/sdd/.claude-plugin/plugin.json").read_text())["version"]


def parse(version):
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        return None
    return tuple(int(n) for n in version.split("."))


def git(*args):
    try:
        out = subprocess.run(["git", *args], capture_output=True, text=True, check=False)
    except OSError:
        return None
    return out.stdout if out.returncode == 0 else None


def baseline():
    """The revision this branch is measured against.

    A stamp fails to move in a commit, so comparing against `HEAD` sees only
    uncommitted work and is inert on the clean checkout a gate runs on. The
    branch point is the earliest revision that still contains the whole branch.
    `SDD_BASE` overrides it, for a repository whose trunk is not `main` and for
    exercising the check itself.
    """
    if os.environ.get("SDD_BASE"):
        return os.environ["SDD_BASE"]
    head = git("rev-parse", "HEAD")
    for trunk in ("main", "origin/main"):
        base = git("merge-base", trunk, "HEAD")
        if base and head and base.strip() != head.strip():
            return base.strip()
    print("  SKIP    no trunk to measure against — a stamp that stopped moving "
          "is only caught in uncommitted work (set SDD_BASE)")
    return "HEAD"


def committed(rev, path):
    """The file at `rev`, or None outside a git tree / before the file existed."""
    text = git("show", f"{rev}:{path.as_posix()}")
    if text is None and path.is_relative_to(ROOT):
        old = Path("plugins/sdd/templates/project") / path.relative_to(ROOT)
        text = git("show", f"{rev}:{old.as_posix()}")
    return text


def fence(text, name):
    """(stamp, region) for a well-formed fence, or a string naming what is wrong."""
    opener = re.compile(rf"<!-- {re.escape(name)}(?: v(\S+))? -->")
    closer = f"<!-- /{name} -->"
    opens, closes = opener.findall(text), text.count(closer)

    if not opens and not closes:
        return f"no {name} fence"
    if len(opens) != 1 or closes != 1:
        return f"{len(opens)} openers, {closes} closers — expected one of each"

    start = opener.search(text)
    end = text.index(closer)
    if start.start() > end:
        return f"{closer} comes before the opener"

    region = text[start.end():end]
    if not region.strip():
        return "the fenced region is empty"
    if not opens[0]:
        return f"the opener carries no version — expected <!-- {name} vN.N.N -->"
    if parse(opens[0]) is None:
        return f"version {opens[0]!r} is not N.N.N"
    return opens[0], region


def stamp_line(text, name):
    """(stamp, rest) for a whole-file tool stamped on one comment line."""
    stamps = re.findall(rf"^# {re.escape(name)} v(\S+)$", text, re.M)
    if len(stamps) != 1:
        return f"no {name} stamp" if not stamps else f"{len(stamps)} {name} stamps — expected one"
    if parse(stamps[0]) is None:
        return f"version {stamps[0]!r} is not N.N.N"
    return stamps[0], re.sub(rf"^# {re.escape(name)} v\S+\n", "", text, flags=re.M)


def journal(text):
    """{(version, title): [body, ...]} for every migration entry."""
    entries, version, title = {}, None, None
    for line in text.splitlines():
        if line.startswith("## "):
            version, title = line[3:].strip(), None
        elif line.startswith("### ") and version:
            title = line[4:].strip()
            entries.setdefault((version, title), []).append("")
        elif title:
            entries[(version, title)][-1] += line + "\n"
    return entries


def shape(body):
    """The first problem with an entry's condition and instructions, or None."""
    blocks = [b for b in re.split(r"\n\s*\n", body.strip()) if b]
    count = body.count(CONDITION)
    if count != 1:
        return f"states {count} conditions; it needs exactly one {CONDITION}"
    if not blocks[0].startswith(CONDITION):
        return "does not start with its condition"
    if not blocks[0][len(CONDITION):].strip():
        return "states an empty condition"
    if len(blocks) < 2:
        return "has no instructions after its condition"
    return None


ok = True
BASE = baseline()
files = sorted(p for p in ROOT.iterdir() if p.is_file())
if not files:
    print("  FAIL    no scaffold templates found")
    ok = False
for path in files:
    name = MARKERS.get(path.name, DEFAULT)
    text = path.read_text()
    read = fence if path.suffix == ".md" else stamp_line
    result = read(text, name)

    if isinstance(result, str):
        print(f"  FAIL    {path.name}: {result}")
        ok = False
        continue

    stamp, region = result
    if parse(stamp) > parse(CEILING):
        print(f"  FAIL    {path.name}: stamped v{stamp}, ahead of the plugin's own {CEILING}")
        ok = False
        continue

    before = committed(BASE, path)
    was = read(before, name) if before is not None else None
    if isinstance(was, tuple) and (parse(stamp) < parse(was[0]) or
                                   (was[1] != region and stamp == was[0])):
        print(f"  FAIL    {path.name}: v{stamp} must advance when guidance changes "
              f"and must not decrease (was v{was[0]})")
        ok = False
        continue

    print(f"  OK      {path.name} ({name} v{stamp})")

entries = journal(JOURNAL.read_text()) if JOURNAL.exists() else {}
if not JOURNAL.exists():
    print(f"  FAIL    {JOURNAL.name} is missing")
    ok = False
for (version, title), bodies in sorted(entries.items()):
    if parse(version) is None or parse(version) > parse(CEILING):
        print(f"  FAIL    {JOURNAL.name}: {title!r} at {version} is ahead of the plugin's own {CEILING}")
        ok = False
    elif len(bodies) > 1:
        print(f"  FAIL    {JOURNAL.name}: {title!r} at {version} appears {len(bodies)} times")
        ok = False
    elif problem := shape(bodies[0]):
        print(f"  FAIL    {JOURNAL.name}: {title!r} at {version} {problem}")
        ok = False

# A project updates from wherever it stands, so a structural step stays
# reachable after later releases.
gone = set(journal(committed(BASE, JOURNAL) or "")) - set(entries)
for version, title in sorted(gone):
    print(f"  FAIL    {JOURNAL.name}: {title!r} at {version} was removed — entries are append-only")
    ok = False

if ok and JOURNAL.exists():
    print(f"  OK      {JOURNAL.name}: {len(entries)} structural migrations")
sys.exit(0 if ok else 1)
