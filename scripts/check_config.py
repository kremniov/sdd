"""Validate .sdd.yml against the parsing rules the skills document."""

import sys

REQUIRED = ("canon", "tasks", "roadmap", "features", "adr", "notes", "verify", "ticket", "rules")
DIRS = ("canon", "features", "adr", "notes")

ok = True
seen = {}

for n, raw in enumerate(open(".sdd.yml"), 1):
    stripped = raw.strip()
    if not stripped or stripped.startswith("#"):
        continue
    if ":" not in raw:
        print(f"  FAIL    line {n}: no key separator")
        ok = False
        continue
    key, rest = raw.split(":", 1)
    key = key.strip()
    if "#" in rest:
        print(f'  FAIL    {key}: value contains "#", so it is truncated at the comment')
        ok = False
    value = rest.split("#")[0].strip()
    if not value:
        print(f"  FAIL    {key}: empty value")
        ok = False
    elif value[0] in "\"'":
        print(f"  FAIL    {key}: quoted values are not unquoted by the readers")
        ok = False
    seen[key] = value

for key in DIRS:
    if key in seen and not seen[key].endswith("/"):
        print(f'  FAIL    {key}: must end in "/" — it is concatenated with a filename')
        ok = False

for key in REQUIRED:
    if key not in seen:
        print(f"  FAIL    missing key: {key}")
        ok = False

if ok:
    print(f"  OK      {len(seen)} keys, all well-formed")

sys.exit(0 if ok else 1)
