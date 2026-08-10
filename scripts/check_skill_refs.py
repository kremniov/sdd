"""Shipped text may only name skills that exist.

A rename reaches the directories and the frontmatter in one edit and leaves the
prose behind, where a stale name is an instruction to run something absent from
`/skills`. The canon is scanned too — it claims to be always current. Frozen
artifacts and decision records quote the old names on purpose and are not.
"""

import re
import sys
from pathlib import Path

RETIRED = {
    "brainstorming": "design",
    "managing-tasks": "tasks",
    "systematic-debugging": "debug",
    "adopting-sdd": "setup",
    "deriving-canon": "canon",
}

skills = {p.name for p in Path("plugins/sdd/skills").iterdir() if p.is_dir()}
scanned = (
    sorted(Path("plugins/sdd").rglob("*.md"))
    + sorted(Path("docs").glob("*.md"))
    + sorted(Path("docs/architecture").glob("*.md"))
    + [Path("README.md"), Path("CLAUDE.md")]
)

ok = True
for path in scanned:
    for n, line in enumerate(path.read_text().splitlines(), 1):
        # The scaffold's own sentinel is `<!-- /sdd:method-section -->`.
        line = re.sub(r"<!--.*?-->", "", line)
        for name in re.findall(r"/sdd:([a-z][a-z-]*)", line):
            if name not in skills:
                print(f"  FAIL    {path}:{n} names /sdd:{name}, which is not a skill")
                ok = False
        for old, new in RETIRED.items():
            if re.search(rf"(?<![\w/-]){re.escape(old)}(?![\w-])", line):
                print(f"  FAIL    {path}:{n} names {old!r} — renamed to /sdd:{new}")
                ok = False

if ok:
    print(f"  OK      every skill named in shipped text exists ({len(skills)} skills)")
sys.exit(0 if ok else 1)
