"""The shipped index generator builds both indexes from ticket files."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "plugins/sdd/skills/setup/templates/project/tasks-index"

CONFIG = """canon: docs/architecture/
tasks: docs/tasks.md
tasks_done: docs/tasks-done.md
tickets: docs/tasks/
ticket: T
"""

OPEN = """---
type: feat
phase: MVP
areas: [billing]
status: next
group: Billing
---

# T-2: Recovery export

**Outcome:** A recovery export contains a consistent snapshot.
"""

DONE = """---
type: bug
status: done
closed: 2026-01-05
ref: "PR #7"
---

# T-1: Duplicate reminder emails

**Result:** A restarted worker sends each reminder once.
"""

INDEX = "# Tasks\n\n<!-- tasks:index -->\n<!-- /tasks:index -->\n"


class TasksIndex(unittest.TestCase):
    def project(self, root, tickets):
        (root / ".sdd").mkdir()
        (root / ".sdd/config.yml").write_text(CONFIG)
        (root / "docs/tasks").mkdir(parents=True)
        (root / "docs/tasks.md").write_text(INDEX)
        (root / "docs/tasks-done.md").write_text(INDEX.replace("Tasks", "Closed tasks"))
        for name, text in tickets.items():
            (root / "docs/tasks" / name).write_text(text)

    def run_index(self, root, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=root,
                              capture_output=True, text=True)

    def test_writes_open_and_closed_indexes(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.project(root, {"T-2.md": OPEN, "T-1.md": DONE})
            self.assertEqual(self.run_index(root).returncode, 0)
            index = (root / "docs/tasks.md").read_text()
            done = (root / "docs/tasks-done.md").read_text()
            self.assertIn("## Billing", index)
            self.assertIn("- [T-2](tasks/T-2.md) Recovery export · `[feat]` `[MVP]` `[billing]` `[next]`", index)
            self.assertNotIn("T-1", index)
            self.assertIn("- [T-1](tasks/T-1.md) Duplicate reminder emails · `[bug]` · PR #7", done)
            self.assertEqual(self.run_index(root, "--check").returncode, 0)

    def test_lists_ungrouped_tickets_before_groups(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            loose = OPEN.replace("group: Billing\n", "").replace("T-2: Recovery", "T-3: Loose")
            self.project(root, {"T-2.md": OPEN, "T-3.md": loose})
            self.assertEqual(self.run_index(root).returncode, 0, self.run_index(root).stderr)
            index = (root / "docs/tasks.md").read_text()
            self.assertLess(index.index("[T-3]"), index.index("## Billing"))

    def test_check_reports_a_stale_index(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.project(root, {"T-2.md": OPEN})
            self.run_index(root)
            (root / "docs/tasks/T-2.md").write_text(OPEN.replace("Recovery export", "Snapshot export"))
            result = self.run_index(root, "--check")
            self.assertEqual(result.returncode, 1)
            self.assertIn("docs/tasks.md is stale", result.stderr)
            self.assertIn("Recovery export", (root / "docs/tasks.md").read_text())

    def test_rejects_an_invalid_ticket(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.project(root, {"T-2.md": OPEN.replace("status: next", "status: soon"),
                                "T-3.md": DONE.replace("# T-1:", "# T-3:").replace("ref: \"PR #7\"\n", "")})
            result = self.run_index(root, "--check")
            self.assertEqual(result.returncode, 1)
            self.assertIn("T-2.md: status must be one of", result.stderr)
            self.assertIn("T-3.md: a done ticket needs ref", result.stderr)

    def test_rejects_scalar_areas(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.project(root, {"T-2.md": OPEN.replace("areas: [billing]", "areas: billing")})
            result = self.run_index(root, "--check")
            self.assertEqual(result.returncode, 1)
            self.assertIn("T-2.md: areas must be a list such as [a, b]", result.stderr)

    def test_rejects_an_unpadded_closing_date(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.project(root, {"T-1.md": DONE.replace("2026-01-05", "2026-1-05")})
            result = self.run_index(root, "--check")
            self.assertEqual(result.returncode, 1)
            self.assertIn("T-1.md: closed must be a date YYYY-MM-DD", result.stderr)

    def test_rejects_an_unclosed_list(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.project(root, {"T-2.md": OPEN.replace("areas: [billing]", "areas: [billing")})
            result = self.run_index(root, "--check")
            self.assertEqual(result.returncode, 1)
            self.assertIn("T-2.md: bad frontmatter line 'areas: [billing'", result.stderr)

    def test_rejects_an_unclosed_quote(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.project(root, {"T-1.md": DONE.replace('ref: "PR #7"', 'ref: "PR #7')})
            result = self.run_index(root, "--check")
            self.assertEqual(result.returncode, 1)
            self.assertIn("T-1.md: bad frontmatter line 'ref: \"PR #7'", result.stderr)

    def test_rejects_a_date_that_does_not_exist(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.project(root, {"T-1.md": DONE.replace("2026-01-05", "2026-02-30")})
            result = self.run_index(root, "--check")
            self.assertEqual(result.returncode, 1)
            self.assertIn("T-1.md: closed must be a date YYYY-MM-DD", result.stderr)

    def test_rejects_an_unknown_key(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.project(root, {"T-2.md": OPEN.replace("status: next", "status: next\nstaus: next")})
            result = self.run_index(root, "--check")
            self.assertEqual(result.returncode, 1)
            self.assertIn("T-2.md: unknown key staus", result.stderr)

    def test_rejects_an_empty_value(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.project(root, {"T-1.md": DONE.replace('ref: "PR #7"', 'ref: ""')})
            result = self.run_index(root, "--check")
            self.assertEqual(result.returncode, 1)
            self.assertIn("T-1.md: ref is empty", result.stderr)

    def test_rejects_text_that_yaml_reads_differently(self):
        cases = {
            "ref: PR #7": "an unquoted # starts a comment",
            'ref: "PR \\"7"': "a quoted value cannot contain",
            "ref: &anchor": "cannot start with",
            "ref: a: b": "cannot contain",
        }
        for value, message in cases.items():
            with self.subTest(value=value), tempfile.TemporaryDirectory() as d:
                root = Path(d)
                self.project(root, {"T-1.md": DONE.replace('ref: "PR #7"', value)})
                result = self.run_index(root, "--check")
                self.assertEqual(result.returncode, 1)
                self.assertIn(message, result.stderr)

    def test_requires_the_configured_paths(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.project(root, {"T-2.md": OPEN})
            (root / ".sdd/config.yml").write_text(CONFIG.replace("tasks_done: docs/tasks-done.md\n", ""))
            result = self.run_index(root)
            self.assertEqual(result.returncode, 1)
            self.assertIn("missing tasks_done", result.stderr)


if __name__ == "__main__":
    unittest.main()
