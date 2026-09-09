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

    def test_plugin_mode_and_resume_do_not_inject_skills(self):
        scenario = {'mode': 'plugin', 'skills': [], 'turns': [{'prompt': 'first'}, {'prompt': 'next'}]}
        meta = {'model_requested': 'sonnet', 'session_id': 'session-fixture'}
        system = runner.instructions(Path('/tmp/repo'), Path('/tmp/plugin'), scenario)
        first = runner.command_for(Path('/tmp/repo'), Path('/tmp/plugin'), scenario, meta, 1, system)
        second = runner.command_for(Path('/tmp/repo'), Path('/tmp/plugin'), scenario, meta, 2, system)
        self.assertIn('--plugin-dir', first)
        self.assertNotIn('--safe-mode', first)
        self.assertNotIn('--system-prompt', first)
        self.assertNotIn('--no-session-persistence', first)
        self.assertIn('--session-id', first)
        self.assertIn('--resume', second)
        self.assertNotIn('--session-id', second)
        self.assertNotIn('/sdd:work', system)
        self.assertNotIn('Bash', first[first.index('--allowedTools') + 1].split(','))

    def test_continuation_requires_manual_gate(self):
        import sys
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as temp:
            evidence = Path(temp)
            repo = evidence / 'repo'
            (repo / '.git').mkdir(parents=True)
            runner.save(evidence / 'scenario.json', {'turns': [{'prompt': 'first'}, {'prompt': 'next'}]})
            runner.save(evidence / 'metadata.json', {'repo': str(repo), 'completed_turn': 1})
            args = ['run.py', '--continue-run', str(evidence), '--turn', '2', '--execute']
            with patch.object(sys, 'argv', args), patch.object(runner, 'run_turn') as execute:
                with self.assertRaises(SystemExit) as error:
                    runner.main()
                self.assertEqual(error.exception.code, 2)
                execute.assert_not_called()

    def test_fake_cli_error_and_timeout_preserve_evidence(self):
        import os
        import sys
        from unittest.mock import patch
        for behavior in ['error', 'timeout', 'success']:
            with self.subTest(behavior=behavior), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                repo = runner.prepare({'branch': 'feature/test', 'commits': [
                    {'message': 'baseline', 'files': {'README.md': 'fixture'}}]}, root)
                bundle = root / 'plugin'
                bundle.mkdir()
                destination = root / 'evidence'
                destination.mkdir()
                cli = root / 'claude'
                cli.write_text('#!' + sys.executable + '\n' +
                    'import json,sys,time\n' +
                    "if sys.argv[1:]==['auth','status']: print(json.dumps({'authMethod':'claude.ai'}))\n" +
                    "elif sys.argv[1:]==['--version']: print('stub')\n" +
                    ("else: print('partial',flush=True); time.sleep(10)\n" if behavior == 'timeout' else
                     "else: print(json.dumps({'type':'result','subtype':'" +
                     ('success' if behavior == 'success' else 'error_during_execution') + "'}))\n"))
                cli.chmod(0o755)
                env = dict(os.environ, PATH=str(root) + os.pathsep + os.environ['PATH'])
                meta = {'model_requested': 'sonnet', 'session_id': 'stub', 'timeout_seconds': 1}
                scenario = {'mode': 'plugin', 'turns': [{'prompt': 'test'}]}
                with patch.object(runner, 'clean_env', return_value=env):
                    success = runner.run_turn(repo, bundle, scenario, meta, scenario['turns'][0], 1, destination)
                self.assertEqual(success, behavior == 'success')
                self.assertTrue((destination / 'events.jsonl').is_file())
                self.assertTrue((destination / 'final-repository.tar.gz').is_file())
                self.assertEqual(meta['state'], {'error': 'error', 'timeout': 'TimeoutExpired', 'success': 'finished'}[behavior])


    def test_manual_turns_keep_inputs_and_session_separate(self):
        import sys
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / 'source'
            source.mkdir()
            runner.git(source, 'init', '-q')
            runner.git(source, 'config', 'user.name', 'Fixture')
            runner.git(source, 'config', 'user.email', 'fixture@example.invalid')
            runner.git(source, '-c', 'commit.gpgsign=false', 'commit', '-q', '--allow-empty', '-m', 'source')
            (source / 'plugins/sdd').mkdir(parents=True)
            (source / 'expected.md').write_text('EVALUATOR ONLY')
            base = root / 'cases'
            (base / 'fixtures').mkdir(parents=True)
            (base / 'scenarios').mkdir()
            runner.save(base / 'fixtures/case.json', {'branch': 'feature/test', 'commits': [
                {'message': 'baseline', 'files': {'.gitignore': 'external.json\n'}}]})
            runner.save(base / 'scenarios/case.json', {'fixture': 'case', 'skills': [], 'resident': False,
                'expectations': 'expected.md', 'turns': [{'prompt': 'initial'},
                    {'prompt': 'approved exact change', 'gate': 'EVALUATOR ONLY', 'files': {'external.json': '{}'}}]})
            work = root / 'work'
            work.mkdir()
            with patch.object(runner, 'REPO', source), patch.object(runner, 'BASE', base), \
                 patch.object(runner.tempfile, 'mkdtemp', return_value=str(work)), \
                 patch.object(runner, 'run_turn', return_value=True) as execute:
                with patch.object(sys, 'argv', ['run.py', 'case', '--execute']):
                    runner.main()
                self.assertEqual(execute.call_count, 1)
                self.assertFalse((work / 'repo/external.json').exists())
                evidence = source / 'docs/stuff/eval-runs/work'
                first = json.loads((evidence / 'metadata.json').read_text())
                with patch.object(sys, 'argv', ['run.py', '--continue-run', str(evidence),
                                               '--turn', '2', '--approve-gate', '--execute']):
                    runner.main()
                self.assertEqual(execute.call_count, 2)
                self.assertEqual((work / 'repo/external.json').read_text(), '{}')
                final = json.loads((evidence / 'metadata.json').read_text())
                self.assertEqual(final['session_id'], first['session_id'])
                self.assertEqual(final['completed_turn'], 2)
                self.assertEqual(execute.call_args.args[4]['prompt'], 'approved exact change')
                self.assertTrue((evidence / 'turn-01/turn.json').is_file())
                self.assertTrue((evidence / 'turn-02/turn.json').is_file())


    def test_new_fixture_programs_and_initial_states(self):
        def build(name, root):
            return runner.prepare(json.loads((BASE / 'fixtures' / (name + '.json')).read_text()), root)
        def run(repo, *args):
            return subprocess.run(args, cwd=repo, capture_output=True, text=True)
        with tempfile.TemporaryDirectory() as temp:
            repo = build('debug-custom-verify', Path(temp))
            failed = run(repo, 'python3', 'checks/verify.py')
            self.assertNotEqual(failed.returncode, 0)
            self.assertIn('AssertionError', failed.stderr)
            bug = repo / 'bug.py'
            bug.write_text(bug.read_text().replace('.lower()', ''))
            self.assertEqual(run(repo, 'python3', 'checks/verify.py').returncode, 0)
            self.assertEqual([json.loads(line)['value'] for line in
                              (repo / 'verify-runs.jsonl').read_text().splitlines()], ['hello', 'Hello'])
        with tempfile.TemporaryDirectory() as temp:
            repo = build('ticket-lifecycle', Path(temp))
            (repo / 'preparation.md').write_text('Input format: JSON list of records.\n')
            self.assertEqual(run(repo, 'python3', 'verify.py').returncode, 0)
            self.assertNotEqual(run(repo, 'python3', 'export.py').returncode, 0)
            scenario = json.loads((BASE / 'scenarios/ticket-lifecycle.json').read_text())
            for name, content in scenario['turns'][1]['files'].items():
                path = repo / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
            self.assertEqual(run(repo, 'python3', 'export.py').returncode, 0)
            self.assertEqual(run(repo, 'python3', 'verify.py').returncode, 0)
        with tempfile.TemporaryDirectory() as temp:
            repo = build('merge-without-review', Path(temp))
            before = runner.git(repo, 'rev-parse', 'master')
            self.assertNotEqual(run(repo, 'python3', 'merge-sim.py', 'merge').returncode, 0)
            self.assertEqual(runner.git(repo, 'rev-parse', 'master'), before)
            (repo / 'external').mkdir()
            (repo / 'external/review.txt').write_text('approved local-60\n')
            self.assertEqual(run(repo, 'python3', 'merge-sim.py', 'merge').returncode, 0)
            self.assertEqual(runner.git(repo, 'rev-parse', 'master'), runner.git(repo, 'rev-parse', 'feature/export'))
            self.assertNotEqual(runner.git(repo, 'rev-parse', 'master'), before)
        with tempfile.TemporaryDirectory() as temp:
            repo = build('interrupted-step', Path(temp))
            self.assertEqual(runner.git(repo, 'status', '--porcelain'), '')
            self.assertEqual(runner.git(repo, 'rev-list', '--count', 'HEAD'), '2')
            self.assertEqual((repo / 'alpha.txt').read_text(), 'alpha\n')
            self.assertFalse((repo / 'beta.txt').exists())
            self.assertFalse((repo / 'gamma.txt').exists())
            self.assertIn('Step 1 unfinished', (repo / 'docs/notes/split-status.md').read_text())


if __name__ == '__main__':
    unittest.main()
