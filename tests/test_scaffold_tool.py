"""A shipped tool is scaffold: its whole-file stamp moves with its content."""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1]
ROOT = Path("plugins/sdd/skills/setup/templates/project")
TOOL = ROOT / "tasks-index"


class ScaffoldToolChecks(unittest.TestCase):
    def run_case(self, edit=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(SOURCE / ROOT, root / ROOT)
            journal = Path("plugins/sdd/skills/setup/migrations.md")
            shutil.copyfile(SOURCE / journal, root / journal)
            manifest = Path("plugins/sdd/.claude-plugin/plugin.json")
            (root / manifest).parent.mkdir(parents=True)
            shutil.copyfile(SOURCE / manifest, root / manifest)
            for args in [("init", "-q"), ("add", "."),
                         ("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                          "-c", "commit.gpgsign=false", "-c", "core.hooksPath=/dev/null",
                          "commit", "-qm", "baseline")]:
                subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)
            if edit:
                path = root / TOOL
                path.write_text(edit(path.read_text()))
            return subprocess.run([sys.executable, str(SOURCE / "scripts/check_scaffold.py")],
                                  cwd=root, env={**os.environ, "SDD_BASE": "HEAD"},
                                  capture_output=True, text=True)

    def test_unchanged_tool_passes(self):
        result = self.run_case()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("tasks-index (sdd:scaffold v", result.stdout)

    def test_changed_tool_needs_a_new_stamp(self):
        result = self.run_case(lambda text: text + "\n# changed\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("tasks-index: v1.2.0 must advance", result.stdout)

    def test_tool_needs_a_stamp(self):
        result = self.run_case(lambda text: text.replace("# sdd:scaffold v", "# scaffold v"))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("tasks-index: no sdd:scaffold stamp", result.stdout)


if __name__ == "__main__":
    unittest.main()
