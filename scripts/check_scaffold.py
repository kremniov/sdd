"""Every scaffold file ships with exactly one well-formed, version-stamped fence.

The fence is what a re-run compares against in an adopting repository, and the
stamp is what it compares: a project whose stamp matches the template's is
current whatever its wording says. A file that ships without one, or with a
stamp that did not move when its guidance did, produces no error there — it
produces silence, and the project keeps a stale copy nobody is told about.
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

MARKERS = {
    "CLAUDE.section.md": "sdd:method-section",
}
DEFAULT = "sdd:scaffold"
CHANGES = "CHANGES.md"
BASELINE = (0, 2, 0)

ROOT = Path("plugins/sdd/templates/project")
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
    base = git("merge-base", "main", "HEAD")
    head = git("rev-parse", "HEAD")
    if base and head and base.strip() != head.strip():
        return base.strip()
    return "HEAD"


def committed(rev, path):
    """The file at `rev`, or None outside a git tree / before the file existed."""
    return git("show", f"{rev}:{path.as_posix()}")


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


def logged(text):
    """{(version, filename)} — every entry declared in the change log."""
    entries, version = set(), None
    for line in text.splitlines():
        if line.startswith("## "):
            version = line[3:].strip()
        elif line.startswith("### ") and version:
            entries.add((version, line[4:].strip()))
    return entries


ok = True
stamps = {}
BASE = baseline()
for path in sorted(ROOT.glob("*.md")):
    if path.name == CHANGES:
        continue
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
    if isinstance(was, tuple) and was[1] != region and was[0] == stamp:
        print(f"  FAIL    {path.name}: the fenced region changed and v{stamp} did not move")
        ok = False
        continue

    stamps[path.name] = stamp
    print(f"  OK      {path.name} ({name} v{stamp})")

entries = logged((ROOT / CHANGES).read_text())
for version, filename in sorted(entries):
    if filename not in stamps:
        print(f"  FAIL    {CHANGES}: {version} names {filename}, which is not a scaffold file")
        ok = False
    elif parse(version) is None or parse(version) > parse(stamps[filename]):
        print(f"  FAIL    {CHANGES}: {filename} has an entry for {version}, past its v{stamps[filename]}")
        ok = False

for filename, stamp in sorted(stamps.items()):
    if parse(stamp) > BASELINE and (stamp, filename) not in entries:
        print(f"  FAIL    {CHANGES}: nothing describes what changed in {filename} at v{stamp}")
        ok = False

# A project upgrades from wherever it stands, not from the last release, so an
# entry stays reachable long after the stamp it describes has been passed.
gone = logged(committed(BASE, ROOT / CHANGES) or "") - entries
for version, filename in sorted(gone):
    print(f"  FAIL    {CHANGES}: the {version} entry for {filename} was removed — entries are append-only")
    ok = False

if ok:
    print(f"  OK      {CHANGES} accounts for every stamp past v{'.'.join(map(str, BASELINE))}")
sys.exit(0 if ok else 1)
