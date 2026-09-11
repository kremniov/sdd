"""Migration accounting must survive relocation of the bundled scaffold."""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1]
OLD = Path("plugins/sdd/templates/project")
NEW = Path("plugins/sdd/skills/setup/templates/project")


class ScaffoldMoveChecks(unittest.TestCase):
    def run_case(self, fault=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(SOURCE / NEW, root / OLD)
            manifest = Path("plugins/sdd/.claude-plugin/plugin.json")
            (root / manifest).parent.mkdir(parents=True)
            shutil.copyfile(SOURCE / manifest, root / manifest)
            for args in [("init", "-q"), ("add", "."),
                         ("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                          "-c", "commit.gpgsign=false", "-c", "core.hooksPath=/dev/null",
                          "commit", "-qm", "baseline")]:
                subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)
            (root / NEW).parent.mkdir(parents=True)
            shutil.move(root / OLD, root / NEW)
            if fault == "stamp":
                path = root / NEW / "tasks.md"
                path.write_text(path.read_text().replace("# Tasks", "# Changed guidance"))
            elif fault == "history":
                path = root / NEW / "CHANGES.md"
                text = path.read_text()
                start = text.index("## 1.1.3")
                end = text.index("## 1.1.1", start)
                path.write_text(text[:start] + text[end:])
            return subprocess.run([sys.executable, str(SOURCE / "scripts/check_scaffold.py")],
                                  cwd=root, env={**os.environ, "SDD_BASE": "HEAD"},
                                  capture_output=True, text=True)

    def test_unchanged_move_passes(self):
        result = self.run_case()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_move_cannot_hide_unstamped_change(self):
        result = self.run_case("stamp")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("did not move", result.stdout)

    def test_move_cannot_hide_removed_history(self):
        result = self.run_case("history")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("entries are append-only", result.stdout)
