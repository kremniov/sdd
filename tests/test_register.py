"""Observable register checker behavior; use temporary instruction files."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CHECKER = Path(__file__).resolve().parents[1] / "scripts/check_register.py"

class RegisterChecks(unittest.TestCase):
    def run_case(self, content, name="SKILL.md"):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / name
            path.write_text(content)
            return subprocess.run([sys.executable, str(CHECKER), str(path)],
                                  capture_output=True, text=True)

    def test_negation_is_advisory(self):
        result = self.run_case("# Rule\nNever do this. Do not do that.\n")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("NOTE", result.stdout)

    def test_skill_budget_counts_fenced_examples(self):
        result = self.run_case("# Example\n```text\n" + "word " * 1201 + "\n```\n")
        self.assertNotEqual(result.returncode, 0, result.stdout)

    def test_skill_budget_counts_tilde_examples(self):
        result = self.run_case("# Example\n~~~text\n" + "word " * 1201 + "\n~~~\n")
        self.assertNotEqual(result.returncode, 0, result.stdout)

    def test_real_deep_heading_fails(self):
        self.assertNotEqual(self.run_case("#### Deep\nText.\n").returncode, 0)

    def test_heading_in_example_is_not_structure(self):
        result = self.run_case("# Example\n```markdown\n#### Ticket\n```\n")
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_tilde_fence_heading_is_not_structure(self):
        result = self.run_case("# Example\n~~~markdown\n#### Ticket\n~~~\n")
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_directory_arguments_reach_references(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "SKILL.md").write_text("# Skill\nShort.\n")
            (root / "audit.md").write_text("# Audit\nDetails.\n")
            result = subprocess.run([sys.executable, str(CHECKER), folder],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("audit.md", result.stdout)

    def test_missing_input_fails(self):
        result = subprocess.run([sys.executable, str(CHECKER), "/missing/sdd/skill.md"],
                                capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)

if __name__ == "__main__":
    unittest.main()
