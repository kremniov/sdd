"""Every invariant entry carries its detection and its consequence."""

import re
import sys

PATH = "docs/architecture/invariants.md"
text = open(PATH).read()

body = text.split("## Layout responsibilities")[0]
entries = re.findall(
    r"^(\d+)\. \*\*(.+?)\*\*(.*?)(?=^\d+\. \*\*|\Z)", body, re.S | re.M
)

if not entries:
    print(f"  FAIL    {PATH}: no numbered invariants found")
    sys.exit(1)

ok = True
for number, name, rest in entries:
    missing = [tag for tag in ("*Detect:*", "*On violation:*") if tag not in rest]
    if missing:
        print(f'  FAIL    #{number} "{name.rstrip(".")}" lacks {" and ".join(missing)}')
        ok = False

numbers = [int(n) for n, _, _ in entries]
if numbers != list(range(1, len(numbers) + 1)):
    print(f"  FAIL    numbering is not 1..n without gaps: {numbers}")
    ok = False

if re.search(r"^(?!\s*\*).*\b(?:rules?|checks?|invariants?) #?\d+[-–]", body, re.M | re.I):
    print("  FAIL    an enforcement summary spanning several rules — put it on each rule")
    ok = False

if ok:
    print(f"  OK      {len(entries)} invariants, each with detect + consequence")

sys.exit(0 if ok else 1)
