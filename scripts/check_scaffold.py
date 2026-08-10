"""Every scaffold file ships with exactly one well-formed, version-stamped fence.

The fence is what a re-run compares against in an adopting repository, and the
stamp is what it compares: a project whose stamp matches the template's is
current whatever its wording says. A file that ships without one, or with a
stamp that did not move when its guidance did, produces no error there — it
produces silence, and the project keeps a stale copy nobody is told about.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

MARKERS = {
    "CLAUDE.section.md": "sdd:method-section",
}
DEFAULT = "sdd:scaffold"

ROOT = Path("plugins/sdd/templates/project")
CEILING = json.loads(Path("plugins/sdd/.claude-plugin/plugin.json").read_text())["version"]


def parse(version):
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        return None
    return tuple(int(n) for n in version.split("."))


def committed(path):
    """The file's content at HEAD, or None outside a git tree / before its first commit."""
    try:
        out = subprocess.run(
            ["git", "show", f"HEAD:{path.as_posix()}"],
            capture_output=True, text=True, check=False,
        )
    except OSError:
        return None
    return out.stdout if out.returncode == 0 else None


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

    before = committed(path)
    was = fence(before, name) if before is not None else None
    if isinstance(was, tuple) and was[1] != region and was[0] == stamp:
        print(f"  FAIL    {path.name}: the fenced region changed and v{stamp} did not move")
        ok = False
        continue

    print(f"  OK      {path.name} ({name} v{stamp})")

sys.exit(0 if ok else 1)
