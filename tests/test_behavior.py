"""Offline checks for reproducible fixtures; never starts an agent."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

BASE = Path(__file__).resolve().parent / 'behavior'
spec = importlib.util.spec_from_file_location('behavior_runner', BASE / 'runner/run.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class BehaviorFixturesTest(unittest.TestCase):
    def test_all_baselines_reproduce_independently(self):
        for path in sorted((BASE / 'fixtures').glob('*.json')):
            with self.subTest(fixture=path.stem), tempfile.TemporaryDirectory() as temp:
                data = json.loads(path.read_text())
                roots = [Path(temp) / 'first', Path(temp) / 'second']
                repos = []
                for root in roots:
                    root.mkdir()
                    repos.append(runner.prepare(data, root))
                self.assertEqual(runner.git(repos[0], 'rev-parse', 'HEAD^{tree}'),
                                 runner.git(repos[1], 'rev-parse', 'HEAD^{tree}'))
                for repo in repos:
                    self.assertEqual(runner.git(repo, 'branch', '--show-current'), data['branch'])
                    self.assertEqual(runner.git(repo, 'status', '--porcelain'), '')
                    self.assertEqual(runner.git(repo, 'remote'), '')
                (repos[0] / 'run-result.txt').write_text('changed')
                self.assertFalse((repos[1] / 'run-result.txt').exists())

    def test_ordered_history_and_file_modes(self):
        data = {'branch': 'feature/test', 'commits': [
            {'message': 'first', 'files': {'old.txt': 'first', 'check.sh': 'exit 0\n'}, 'executable': ['check.sh']},
            {'message': 'second', 'files': {'new.txt': 'second'}, 'delete': ['old.txt']}]}
        with tempfile.TemporaryDirectory() as temp:
            repo = runner.prepare(data, Path(temp))
            self.assertEqual(runner.git(repo, 'show', 'HEAD~1:old.txt'), 'first')
            self.assertFalse((repo / 'old.txt').exists())
            self.assertTrue((repo / 'check.sh').stat().st_mode & 0o111)
            self.assertEqual(runner.git(repo, 'log', '--reverse', '--format=%s'), 'first\nsecond')

    def test_scenarios_resolve_without_evaluator_input(self):
        for path in (BASE / 'scenarios').glob('*.json'):
            data = json.loads(path.read_text())
            self.assertTrue((BASE / 'fixtures' / (data['fixture'] + '.json')).is_file())
            self.assertTrue((BASE.parents[1] / data['expectations']).is_file())
            self.assertTrue(data.get('prompt') or data.get('blocked'))
            for skill in data['skills']:
                self.assertTrue((BASE.parents[1] / 'plugins/sdd/skills' / skill / 'SKILL.md').is_file())

    def test_verify_fixture_accepts_newlines_and_rejects_wrong_content(self):
        data = json.loads((BASE / 'fixtures/verify-frequency.json').read_text())
        with tempfile.TemporaryDirectory() as temp:
            repo = runner.prepare(data, Path(temp))
            for name in ['alpha', 'beta', 'gamma']:
                (repo / (name + '.md')).write_text(name + '\n')
            self.assertEqual(subprocess.run(['python3', 'verify.py'], cwd=repo, capture_output=True).returncode, 0)
            events = (repo / 'verify-runs.jsonl').read_text().splitlines()
            self.assertEqual([json.loads(line) for line in events], [['alpha.md', 'beta.md', 'gamma.md']])
            (repo / 'beta.md').write_text('wrong\n')
            self.assertNotEqual(subprocess.run(['python3', 'verify.py'], cwd=repo, capture_output=True).returncode, 0)


if __name__ == '__main__':
    unittest.main()
