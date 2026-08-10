#!/usr/bin/env bash
# Structural checks for the plugin. Run before publishing a version.
set -uo pipefail
cd "$(dirname "$0")/.."
fail=0
note() { printf '  %-7s %s\n' "$1" "$2"; [ "$1" = FAIL ] && fail=1; return 0; }

echo "manifests"
for f in .claude-plugin/marketplace.json plugins/sdd/.claude-plugin/plugin.json; do
  if python3 -c "import json,sys; json.load(open('$f'))" 2>/dev/null; then
    note OK "$f parses"
  else
    note FAIL "$f does not parse"
  fi
done

echo "marketplace sources resolve"
python3 scripts/check_marketplace.py || fail=1
if command -v claude >/dev/null 2>&1; then
  if claude plugin validate . >/dev/null 2>&1; then
    note OK "claude plugin validate passes"
  else
    claude plugin validate . 2>&1 | sed 's/^/          /'
    note FAIL "claude plugin validate rejects the manifest"
  fi
else
  note SKIP "claude not on PATH — schema unvalidated"
fi

echo "skills"
python3 - <<'PY' || fail=1
import re, os, glob, sys
ok = True
found = glob.glob('plugins/sdd/skills/*/SKILL.md')
if not found:
    print('  FAIL    no skills found'); sys.exit(1)
for f in sorted(found):
    d = os.path.basename(os.path.dirname(f))
    m = re.match(r'^---\n(.*?)\n---\n', open(f).read(), re.S)
    if not m:
        print(f'  FAIL    {d}: no frontmatter'); ok = False; continue
    fm = dict(re.findall(r'^([\w-]+):\s*(.+)$', m.group(1), re.M))
    if fm.get('name') != d:
        print(f'  FAIL    {d}: name is {fm.get("name")!r}, must match directory'); ok = False
    elif not fm.get('description'):
        print(f'  FAIL    {d}: empty description'); ok = False
    elif len(fm['description']) > 1536:
        print(f'  FAIL    {d}: description over 1536 chars'); ok = False
    else:
        print(f'  OK      {d}')
sys.exit(0 if ok else 1)
PY

echo "skill references"
python3 scripts/check_skill_refs.py || fail=1

echo "bundled paths"
python3 - <<'PY' || fail=1
import re, os, glob, sys
ok = True
for f in glob.glob('plugins/sdd/skills/*/SKILL.md'):
    for ref in re.findall(r'\$\{CLAUDE_PLUGIN_ROOT\}/([A-Za-z0-9_./-]+)', open(f).read()):
        p = os.path.join('plugins/sdd', ref.rstrip('.'))
        if os.path.exists(p):
            print(f'  OK      {ref}')
        else:
            print(f'  FAIL    {ref} (from {f})'); ok = False
sys.exit(0 if ok else 1)
PY

echo "portability"
python3 scripts/check_portability.py || fail=1

echo "every shipped skeleton is reachable"
python3 - <<'PY' || fail=1
import glob, os, sys
refs = ''.join(open(f).read() for f in glob.glob('plugins/sdd/skills/*/SKILL.md'))
ok = True
for t in sorted(glob.glob('plugins/sdd/templates/_*.md')):
    name = os.path.basename(t)
    if name in refs:
        print(f'  OK      {name} is referenced by a skill')
    else:
        print(f'  FAIL    {name} ships but no skill names its path'); ok = False
sys.exit(0 if ok else 1)
PY

echo ".sdd.yml is well-formed"
python3 scripts/check_config.py || fail=1

echo "canon entries are complete"
python3 scripts/check_canon.py || fail=1

echo "own CLAUDE.md matches the template"
python3 - <<'PY' || fail=1
import re, sys
cfg = {}
for line in open('.sdd.yml'):
    line = line.split('#')[0].strip()
    if ':' in line:
        k, v = line.split(':', 1); cfg[k.strip()] = v.strip()
tpl = open('plugins/sdd/templates/project/CLAUDE.section.md').read()
missing = {k for k in re.findall(r'\{\{(\w+)\}\}', tpl) if k not in cfg}
if missing:
    print(f'  FAIL    .sdd.yml lacks keys the scaffold needs: {sorted(missing)}'); sys.exit(1)
rendered = re.sub(r'\{\{(\w+)\}\}', lambda m: cfg[m.group(1)], tpl)
if rendered.strip() in open('CLAUDE.md').read():
    print('  OK      dogfooded section is in sync'); sys.exit(0)
print('  FAIL    CLAUDE.md has drifted from the scaffold — re-render it'); sys.exit(1)
PY

echo "section nests"
if grep -m1 '^#' plugins/sdd/templates/project/CLAUDE.section.md | grep -q '^## '; then
  if grep -q '^# ' plugins/sdd/templates/project/CLAUDE.section.md; then
    note FAIL "CLAUDE.section.md has an H1 — it is appended into someone's file"
  else
    note OK "CLAUDE.section.md starts at H2 and has no H1"
  fi
else
  note FAIL "CLAUDE.section.md must start with an H2 heading"
fi

echo "scaffold renders"
python3 - <<'PY' || fail=1
import re, glob, sys
cfg = {}
for line in open('.sdd.yml'):
    line = line.split('#')[0].strip()
    if ':' in line:
        k, v = line.split(':', 1); cfg[k.strip()] = v.strip()
ok = True
for f in glob.glob('plugins/sdd/templates/project/*.md'):
    unknown = {k for k in re.findall(r'\{\{(\w+)\}\}', open(f).read()) if k not in cfg}
    if unknown:
        print(f'  FAIL    {f}: placeholders with no .sdd.yml key: {sorted(unknown)}'); ok = False
    else:
        print(f'  OK      {f}')
sys.exit(0 if ok else 1)
PY

echo "placeholders"
stray='^[^`]*\{\{(canon|tasks|roadmap|features|adr|verify|ticket|rules)\}\}[^`]*$'
if grep -rnE "$stray" plugins/sdd/skills >/dev/null 2>&1; then
  grep -rnE "$stray" plugins/sdd/skills | sed 's/^/  /'
  note FAIL "skills must not carry {{placeholders}} — those belong in templates/project/"
else
  note OK "no stray placeholders in skills"
fi

echo
[ "$fail" -eq 0 ] && echo "checks passed" || echo "CHECKS FAILED"
exit "$fail"
