"""Every plugin the marketplace lists must resolve to a real plugin manifest.

`metadata.pluginRoot` is prepended only to a source without a leading `./`; a
`./`-prefixed source resolves against the marketplace root instead. Both forms
parse, so a manifest that no installation can follow is otherwise green.
"""

import json
import os
import sys
from pathlib import Path

market = json.loads(Path(".claude-plugin/marketplace.json").read_text())
root = market.get("metadata", {}).get("pluginRoot", ".")

ok = True
for entry in market.get("plugins", []):
    name, source = entry["name"], entry["source"]
    base = source if source.startswith("./") else os.path.join(root, source)
    manifest = Path(os.path.normpath(os.path.join(base, ".claude-plugin/plugin.json")))
    if not manifest.is_file():
        print(f"  FAIL    {name}: source {source!r} resolves to {manifest}, which does not exist")
        via = "the marketplace root" if source.startswith("./") else f"pluginRoot {root!r}"
        print(f"          resolved via {via}")
        ok = False
        continue
    plugin = json.loads(manifest.read_text())
    version = plugin.get("version")
    if plugin.get("name") != name:
        print(f"  FAIL    {name}: {manifest} names a different plugin")
        ok = False
    else:
        print(f"  OK      {name} -> {manifest.parent.parent} ({version})")

sys.exit(0 if ok else 1)
