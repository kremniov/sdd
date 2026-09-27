"""The structural migration journal stays well-formed and append-only."""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1]
SETUP = Path("plugins/sdd/skills/setup")
JOURNAL = SETUP / "migrations.md"


class MigrationChecks(unittest.TestCase):
    def run_case(self, edit=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(SOURCE / SETUP, root / SETUP)
            manifest = Path("plugins/sdd/.claude-plugin/plugin.json")
            (root / manifest).parent.mkdir(parents=True)
            shutil.copyfile(SOURCE / manifest, root / manifest)
            for args in [("init", "-q"), ("add", "."),
                         ("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                          "-c", "commit.gpgsign=false", "-c", "core.hooksPath=/dev/null",
                          "commit", "-qm", "baseline")]:
                subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)
            if edit:
                path = root / JOURNAL
                path.write_text(edit(path.read_text()))
            return subprocess.run([sys.executable, str(SOURCE / "scripts/check_scaffold.py")],
                                  cwd=root, env={**os.environ, "SDD_BASE": "HEAD"},
                                  capture_output=True, text=True)

    def test_journal_passes(self):
        result = self.run_case()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("migrations.md", result.stdout)

    def test_entry_needs_a_condition(self):
        result = self.run_case(lambda text: text.replace("**Applies when:**", "**When:**", 1))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("'Configuration in `.sdd/`' at 1.2.0 states 0 conditions", result.stdout)

    def test_condition_is_not_empty(self):
        result = self.run_case(lambda text: text.replace(
            "**Applies when:** the config sets `tickets` and `.sdd/tasks-index` is missing.",
            "**Applies when:**"))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("'Index tool' at 1.2.0 states an empty condition", result.stdout)

    def test_entry_states_one_condition(self):
        result = self.run_case(lambda text: text + "\n**Applies when:** always.\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("'Index tool' at 1.2.0 states 2 conditions", result.stdout)

    def test_condition_comes_first(self):
        result = self.run_case(lambda text: text.replace(
            "### Index tool\n", "### Index tool\n\nCopy the tool.\n"))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("'Index tool' at 1.2.0 does not start with its condition", result.stdout)

    def test_entry_has_instructions(self):
        def drop_instructions(text):
            return text[:text.index("Copy `tasks-index`")]
        result = self.run_case(drop_instructions)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("'Index tool' at 1.2.0 has no instructions", result.stdout)

    def test_titles_are_unique_within_a_version(self):
        result = self.run_case(lambda text: text + "\n### Index tool\n\n**Applies when:** always.\n\nDo it.\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("'Index tool' at 1.2.0 appears 2 times", result.stdout)

    def test_entry_cannot_be_ahead_of_the_plugin(self):
        result = self.run_case(lambda text: text + "\n## 999.0.0\n\n### Future\n\n**Applies when:** never.\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ahead of the plugin", result.stdout)

    def test_entries_are_append_only(self):
        def drop_first(text):
            start = text.index("\n### ")
            end = text.index("\n### ", start + 1)
            return text[:start] + text[end:]
        result = self.run_case(drop_first)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("append-only", result.stdout)


if __name__ == "__main__":
    unittest.main()
