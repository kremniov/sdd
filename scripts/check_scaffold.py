"""Check scaffold boundaries and template stamps against the base revision."""

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


ok = True
BASE = baseline()
for path in sorted(ROOT.glob("*.md")):
    name = MARKERS.get(path.name, DEFAULT)
    text = path.read_text()
    result = fence(text, name)

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
    was = fence(before, name) if before is not None else None
    if isinstance(was, tuple) and (parse(stamp) < parse(was[0]) or
                                 (was[1] != region and parse(stamp) == parse(was[0]))):
        print(f"  FAIL    {path.name}: v{stamp} must advance when guidance changes and must not decrease")
        ok = False
        continue

    print(f"  OK      {path.name} ({name} v{stamp})")

if not list(ROOT.glob("*.md")):
    print("  FAIL    no scaffold templates found")
    ok = False
sys.exit(0 if ok else 1)
