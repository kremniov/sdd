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

echo "vocabulary"
targets=(plugins README.md CLAUDE.md docs/architecture docs/roadmap.md docs/tasks.md)
if grep -rniE '\boperators?\b' --include='*.md' "${targets[@]}" >/dev/null 2>&1; then
  grep -rniE '\boperators?\b' --include='*.md' "${targets[@]}" | sed 's/^/  /'
  note FAIL "the party directing the work is the user (ADR 0016)"
else
  note OK "no 'operator' outside the decision records and the frozen designs"
fi

echo "bundled paths"
python3 - <<'PYCODE' || fail=1
import re, sys
from pathlib import Path
bundle = Path('plugins/sdd').resolve()
ROOT = '${CLAUDE_PLUGIN_ROOT}/'
ok = True
for source in Path('plugins/sdd/skills').rglob('*.md'):
    if 'templates' in source.parts:
        continue  # Template links resolve in the adopting project.
    text = source.read_text()
    refs = []
    for ref in re.findall(r'\]\(([^)]+)\)', text):
        if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', ref) or ref.startswith('#'):
            continue
        path = ref.split('#', 1)[0]
        base = bundle if path.startswith(ROOT) else source.parent
        refs.append((ref, base / path.removeprefix(ROOT)))
    bare = re.sub(r'\]\([^)]+\)', '', text)
    refs += [(ROOT + ref, bundle / ref.rstrip('.'))
             for ref in re.findall(r'\$\{CLAUDE_PLUGIN_ROOT\}/([A-Za-z0-9_./-]+)', bare)]
    for ref, target in refs:
        # Only the plugin directory is installed; a link out of it is dead for users.
        if target.resolve() != bundle and bundle not in target.resolve().parents:
            print(f'  FAIL    {ref} leaves the plugin bundle (from {source})'); ok = False
        elif target.exists():
            print(f'  OK      {ref} (from {source})')
        else:
            print(f'  FAIL    {ref} (from {source})'); ok = False
sys.exit(0 if ok else 1)
PYCODE

echo "portability"
python3 scripts/check_portability.py || fail=1

echo "register"
python3 scripts/check_register.py || fail=1

echo "checker tests"
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py' || fail=1

echo "every shipped skeleton is reachable"
python3 - <<'PY' || fail=1
import glob, os, sys
refs = ''.join(open(f).read() for f in glob.glob('plugins/sdd/skills/*/SKILL.md'))
ok = True
for t in sorted(glob.glob('plugins/sdd/skills/*/templates/_*.md')):
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
if '<!-- sdd:dogfooding-paused -->' in open('CLAUDE.md').read():
    print('  SKIP    dogfooding paused — invariant 9 is not in force'); sys.exit(0)
tpl = open('plugins/sdd/skills/setup/templates/project/CLAUDE.section.md').read()
missing = {k for k in re.findall(r'\{\{(\w+)\}\}', tpl) if k not in cfg}
if missing:
    print(f'  FAIL    .sdd.yml lacks keys the scaffold needs: {sorted(missing)}'); sys.exit(1)
rendered = re.sub(r'\{\{(\w+)\}\}', lambda m: cfg[m.group(1)], tpl)
if rendered.strip() in open('CLAUDE.md').read():
    print('  OK      dogfooded section is in sync'); sys.exit(0)
print('  FAIL    CLAUDE.md has drifted from the scaffold — re-render it'); sys.exit(1)
PY

echo "scaffold fences"
python3 scripts/check_scaffold.py || fail=1

echo "section nests"
if grep -m1 '^#' plugins/sdd/skills/setup/templates/project/CLAUDE.section.md | grep -q '^## '; then
  if grep -q '^# ' plugins/sdd/skills/setup/templates/project/CLAUDE.section.md; then
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
for f in glob.glob('plugins/sdd/skills/setup/templates/project/*.md'):
    unknown = {k for k in re.findall(r'\{\{(\w+)\}\}', open(f).read()) if k not in cfg}
    if unknown:
        print(f'  FAIL    {f}: placeholders with no .sdd.yml key: {sorted(unknown)}'); ok = False
    else:
        print(f'  OK      {f}')
sys.exit(0 if ok else 1)
PY

echo "placeholders"
stray='^[^`]*\{\{(canon|tasks|roadmap|features|adr|verify|ticket|rules)\}\}[^`]*$'
if grep -rnE --exclude-dir=templates "$stray" plugins/sdd/skills >/dev/null 2>&1; then
  grep -rnE --exclude-dir=templates "$stray" plugins/sdd/skills | sed 's/^/  /'
  note FAIL "skills must not carry {{placeholders}} — those belong in templates/project/"
else
  note OK "no stray placeholders in skills"
fi

echo
[ "$fail" -eq 0 ] && echo "checks passed" || echo "CHECKS FAILED"
exit "$fail"
