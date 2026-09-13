"""Template stamps and boundaries remain checked after scaffold relocation."""
import os
import re
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
            elif fault == "downgrade":
                path = root / NEW / "tasks.md"
                path.write_text(re.sub(r"v[0-9]+\.[0-9]+\.[0-9]+", "v0.0.0", path.read_text(), count=1))
            elif fault == "ahead":
                path = root / NEW / "tasks.md"
                path.write_text(re.sub(r"v[0-9]+\.[0-9]+\.[0-9]+", "v999.0.0", path.read_text(), count=1))
            elif fault == "boundary":
                path = root / NEW / "tasks.md"
                path.write_text(path.read_text().replace("<!-- /sdd:scaffold -->", ""))
            return subprocess.run([sys.executable, str(SOURCE / "scripts/check_scaffold.py")],
                                  cwd=root, env={**os.environ, "SDD_BASE": "HEAD"},
                                  capture_output=True, text=True)

    def test_unchanged_move_passes(self):
        result = self.run_case()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_move_cannot_hide_unstamped_change(self):
        result = self.run_case("stamp")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must advance", result.stdout)

    def test_stamp_cannot_decrease(self):
        result = self.run_case("downgrade")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must not decrease", result.stdout)

    def test_stamp_cannot_exceed_plugin_version(self):
        result = self.run_case("ahead")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ahead of the plugin", result.stdout)

    def test_missing_boundary_fails(self):
        result = self.run_case("boundary")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("0 closers", result.stdout)
