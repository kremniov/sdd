"""Every scaffold file ships with exactly one well-formed fence.

The fence is what a re-run compares against in an adopting repository. A file
that ships without one, or with a broken one, produces no error there — it
produces silence, and the project keeps a stale copy nobody is told about.
"""

import sys
from pathlib import Path

MARKERS = {
    "CLAUDE.section.md": "sdd:method-section",
}
DEFAULT = "sdd:scaffold"

root = Path("plugins/sdd/templates/project")
ok = True
for path in sorted(root.glob("*.md")):
    name = MARKERS.get(path.name, DEFAULT)
    opener, closer = f"<!-- {name} -->", f"<!-- /{name} -->"
    text = path.read_text()
    opens, closes = text.count(opener), text.count(closer)

    if opens == 0 and closes == 0:
        print(f"  FAIL    {path.name}: no {name} fence")
        ok = False
    elif opens != 1 or closes != 1:
        print(f"  FAIL    {path.name}: {opens} openers, {closes} closers — expected one of each")
        ok = False
    elif text.index(opener) > text.index(closer):
        print(f"  FAIL    {path.name}: {closer} comes before {opener}")
        ok = False
    elif not text[text.index(opener) + len(opener):text.index(closer)].strip():
        print(f"  FAIL    {path.name}: the fenced region is empty")
        ok = False
    else:
        print(f"  OK      {path.name} ({name})")

sys.exit(0 if ok else 1)
