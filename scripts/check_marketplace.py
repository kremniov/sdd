"""Every plugin the marketplace lists must resolve to a real plugin manifest.

A string source is resolved from the marketplace root and must start with `./`
(ADR 0008). `claude plugin validate` accepts any well-formed path, so a source
that points nowhere passes the schema and fails only at install.
"""

import json
import os
import sys
from pathlib import Path

market = json.loads(Path(".claude-plugin/marketplace.json").read_text())

ok = True
if "pluginRoot" in market.get("metadata", {}):
    print("  FAIL    metadata.pluginRoot is not applied to string sources — see ADR 0008")
    ok = False

for entry in market.get("plugins", []):
    name, source = entry["name"], entry["source"]
    if not isinstance(source, str):
        print(f"  OK      {name}: non-string source, resolved by Claude Code")
        continue
    if not source.startswith("./"):
        print(f"  FAIL    {name}: source {source!r} must start with './' to pass schema validation")
        ok = False
        continue
    manifest = Path(os.path.normpath(os.path.join(source, ".claude-plugin/plugin.json")))
    if not manifest.is_file():
        print(f"  FAIL    {name}: source {source!r} resolves to {manifest}, which does not exist")
        ok = False
        continue
    plugin = json.loads(manifest.read_text())
    if plugin.get("name") != name:
        print(f"  FAIL    {name}: {manifest} names {plugin.get('name')!r}")
        ok = False
    else:
        print(f"  OK      {name} -> {manifest.parent.parent} ({plugin.get('version')})")

sys.exit(0 if ok else 1)
