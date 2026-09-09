#!/usr/bin/env python3
"""Prepare an isolated fixture; run Claude Code only with --execute."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import tempfile
import uuid

BASE = Path(__file__).resolve().parents[1]
REPO = BASE.parents[1]


def save(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], text=True).strip()


def safe_path(root, name):
    path = root / name
    if Path(name).is_absolute() or '..' in Path(name).parts or '.git' in Path(name).parts:
        raise ValueError(f'Invalid fixture path: {name}')
    return path


def prepare(fixture, root):
    repo = root / 'repo'
    repo.mkdir()
    git(repo, 'init', '-q', '-b', fixture['branch'])
    for key, value in [('user.name', 'SDD fixture'), ('user.email', 'fixture@example.invalid'),
                       ('commit.gpgsign', 'false'), ('core.hooksPath', '/dev/null')]:
        git(repo, 'config', key, value)
    for commit in fixture['commits']:
        for name in commit.get('delete', []):
            safe_path(repo, name).unlink()
        for name, content in commit['files'].items():
            path = safe_path(repo, name)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
            path.chmod(0o755 if name in commit.get('executable', []) else 0o644)
        git(repo, 'add', '.')
        git(repo, 'commit', '-q', '--allow-empty', '-m', commit['message'])
    for name, revision in fixture.get('refs', {}).items():
        git(repo, 'branch', name, revision)
    for name, content in fixture.get('working_files', {}).items():
        path = safe_path(repo, name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    return repo


def clean_env():
    env = os.environ.copy()
    for key in ('ANTHROPIC_API_KEY', 'ANTHROPIC_AUTH_TOKEN', 'ANTHROPIC_BASE_URL',
                'CLAUDE_CODE_USE_BEDROCK', 'CLAUDE_CODE_USE_VERTEX', 'CLAUDE_CODE_USE_FOUNDRY'):
        env.pop(key, None)
    return env


def config_values(repo, scenario):
    cfg = dict(scenario.get('render_config', {}))
    config = repo / '.sdd.yml'
    if config.exists():
        for line in config.read_text().splitlines():
            line = line.split('#', 1)[0]
            if ':' in line:
                key, value = line.split(':', 1)
                cfg[key.strip()] = value.strip()
    return cfg


def render(text, cfg, bundle):
    text = text.replace('${CLAUDE_PLUGIN_ROOT}', str(bundle))
    return re.sub(r'\{\{(\w+)\}\}', lambda m: cfg.get(m[1], m[0]), text)


def instructions(repo, bundle, scenario):
    system = ('Use actual tools in this disposable repository. Keep mutations inside it. '
              'No hosted remote or PR service is available. Only a fixture-provided local '
              'simulation may be used if present; report its limits. Do not use other agents.\n')
    if scenario.get('mode') == 'plugin':
        return system
    sources = ([bundle / 'templates/project/CLAUDE.section.md'] if scenario['resident'] else [])
    sources += [bundle / 'skills' / skill / 'SKILL.md' for skill in scenario['skills']]
    return system + ''.join('\n' + render(p.read_text(), config_values(repo, scenario), bundle) for p in sources)


def command_for(repo, bundle, scenario, meta, turn_number, system):
    plugin = scenario.get('mode') == 'plugin'
    tool_list = 'Read,Write,Edit,Glob,Grep,Bash' + (',Skill' if plugin else '')
    allowed = 'Read,Write,Edit,Glob,Grep,Bash(git *),Bash(true),Bash(python3 *),Bash(pwd),Bash(ls *)'
    if plugin:
        allowed += ',Skill'
    command = ['claude', '-p', '--model', meta['model_requested'], '--effort', 'medium',
               '--restricted', '--strict-mcp-config', '--tools', tool_list,
               '--allowedTools', allowed, '--permission-mode', 'acceptEdits',
               '--add-dir', str(bundle), '--output-format', 'stream-json', '--verbose']
    if plugin:
        command += ['--plugin-dir', str(bundle), '--setting-sources', '',
                    '--settings', '{"disableAllHooks":true}', '--append-system-prompt', system]
    else:
        command += ['--safe-mode', '--system-prompt', system]
    if scenario.get('turns'):
        command += ['--session-id' if turn_number == 1 else '--resume', meta['session_id']]
    else:
        command += ['--no-session-persistence']
    return command


def capture(repo, destination, meta):
    meta.update(final_branch=git(repo, 'branch', '--show-current'),
                final_status=git(repo, 'status', '--short'))
    (destination / 'history.txt').write_text(git(repo, 'log', '--all', '--format=fuller', '--stat'))
    shutil.make_archive(str(destination / 'final-repository'), 'gztar', root_dir=repo.parent, base_dir='repo')
    save(destination / 'metadata.json', meta)


def run_turn(repo, bundle, scenario, meta, turn, number, destination):
    system = instructions(repo, bundle, scenario)
    (destination / 'system.txt').write_text(system)
    (destination / 'input.txt').write_text(turn['prompt'])
    command = command_for(repo, bundle, scenario, meta, number, system)
    save(destination / 'command.json', command)
    env = clean_env()
    try:
        preflight = [['claude', 'auth', 'status'], ['claude', '--version']]
        save(destination / 'preflight-commands.json', preflight)
        with (destination / 'preflight-stderr.txt').open('w') as stderr:
            result = subprocess.run(preflight[0], env=env, text=True, stdout=subprocess.PIPE,
                                    stderr=stderr, timeout=30, check=True)
            auth = json.loads(result.stdout)
            meta['auth_method'] = auth.get('authMethod')
            if meta['auth_method'] != 'claude.ai':
                raise RuntimeError('Claude subscription authentication required')
            result = subprocess.run(preflight[1], env=env, text=True, stdout=subprocess.PIPE,
                                    stderr=stderr, timeout=30, check=True)
            meta['cli_version'] = result.stdout.strip()
        with (destination / 'events.jsonl').open('w') as stdout, (destination / 'stderr.txt').open('w') as stderr:
            process = subprocess.Popen(command, cwd=repo, env=env, stdin=subprocess.PIPE,
                                       stdout=stdout, stderr=stderr, text=True, start_new_session=True)
            try:
                process.communicate(turn['prompt'], timeout=meta['timeout_seconds'])
                meta.update(state='finished', exit_code=process.returncode, judgment='unassessed')
            except (subprocess.TimeoutExpired, KeyboardInterrupt) as error:
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                meta.update(state=type(error).__name__, judgment='incomplete')
        if meta['state'] == 'finished':
            events = [json.loads(line) for line in (destination / 'events.jsonl').read_text().splitlines() if line.strip()]
            result = next((e for e in reversed(events) if e.get('type') == 'result'), {})
            meta['result_subtype'] = result.get('subtype')
            if meta['exit_code'] != 0 or result.get('is_error') or result.get('subtype') != 'success':
                meta.update(state='error', judgment='incomplete')
    except Exception as error:
        meta.update(state='error', error=str(error), judgment='incomplete')
    finally:
        capture(repo, destination, meta)
    return meta['state'] == 'finished'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('name', nargs='?', help='Scenario name, or fixture name with --fixture-only')
    parser.add_argument('--fixture-only', action='store_true')
    parser.add_argument('--execute', action='store_true', help='Start one subscription Claude Code turn')
    parser.add_argument('--model', choices=['sonnet', 'opus'], default='sonnet')
    parser.add_argument('--timeout', type=int, default=300)
    parser.add_argument('--continue-run', type=Path, help='Existing evidence directory; uses its saved inputs')
    parser.add_argument('--turn', type=int, default=1)
    parser.add_argument('--approve-gate', action='store_true', help='Evaluator checked the previous turn against the gate')
    args = parser.parse_args()
    if args.timeout <= 0 or args.turn < 1:
        parser.error('Use a positive timeout and turn number')
    if args.fixture_only and (args.execute or args.continue_run):
        parser.error('--fixture-only prepares a new repository without execution')
    if args.continue_run:
        evidence = args.continue_run.resolve()
        if args.name:
            parser.error('Continuation uses its saved scenario; omit name')
        scenario = json.loads((evidence / 'scenario.json').read_text())
        meta = json.loads((evidence / 'metadata.json').read_text())
        repo = Path(meta['repo'])
        root = repo.parent
        if not (repo / '.git').is_dir():
            parser.error('Temporary repository is missing; cannot continue')
        expected = meta.get('completed_turn', 0) + 1
        if args.turn != expected:
            parser.error(f'Next turn is {expected}')
        if args.turn > 1 and not args.approve_gate:
            parser.error('Inspect the gate and previous evidence, then use --approve-gate')
        hashes = {str(p.relative_to(root / 'plugin')): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in sorted((root / 'plugin').rglob('*')) if p.is_file()}
        if hashes != meta['plugin_sha256']:
            parser.error('Candidate plugin changed since preparation; start a fresh run')
        meta['timeout_seconds'] = args.timeout
    else:
        if not args.name or not re.fullmatch(r'[a-z0-9-]+', args.name) or args.turn != 1:
            parser.error('Provide a scenario name and start with turn 1')
        scenario = None if args.fixture_only else json.loads((BASE / 'scenarios' / (args.name + '.json')).read_text())
        if scenario and args.execute and scenario.get('blocked'):
            parser.error(scenario['blocked'])
        name = args.name if scenario is None else scenario['fixture']
        fixture = json.loads((BASE / 'fixtures' / (name + '.json')).read_text())
        root = Path(tempfile.mkdtemp(prefix='sdd-behavior-'))
        repo = prepare(fixture, root)
        evidence = REPO / 'docs/stuff/eval-runs' / root.name
        evidence.mkdir(parents=True)
        save(evidence / 'fixture.json', fixture)
        if scenario:
            save(evidence / 'scenario.json', scenario)
            shutil.copyfile(REPO / scenario['expectations'], evidence / 'expectations.md')
        bundle = root / 'plugin'
        shutil.copytree(REPO / 'plugins/sdd', bundle)
        shutil.copytree(bundle, evidence / 'plugin')
        if scenario and scenario.get('mode') == 'plugin':
            resident = render((bundle / 'templates/project/CLAUDE.section.md').read_text(), config_values(repo, scenario), bundle)
            with (repo / 'CLAUDE.md').open('a') as f:
                f.write('\n' + resident)
            git(repo, 'add', 'CLAUDE.md')
            git(repo, 'commit', '-qm', 'fixture: install candidate resident instructions')
        hashes = {str(p.relative_to(bundle)): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in sorted(bundle.rglob('*')) if p.is_file()}
        meta = {'state': 'prepared', 'judgment': 'not run', 'fixture': name, 'repo': str(repo),
                'source_revision': git(REPO, 'rev-parse', 'HEAD'), 'source_status': git(REPO, 'status', '--short'),
                'plugin_sha256': hashes, 'baseline': git(repo, 'rev-parse', 'HEAD'),
                'model_requested': args.model, 'effort': 'medium', 'mode': (scenario or {}).get('mode', 'explicit'),
                'timeout_seconds': args.timeout, 'session_id': str(uuid.uuid4()), 'completed_turn': 0}
        save(evidence / 'metadata.json', meta)
        shutil.copyfile(Path(__file__), evidence / 'runner.py')
    print(json.dumps({'repo': str(repo), 'evidence': str(evidence)}), flush=True)
    if scenario is None:
        return
    if scenario.get('blocked') and args.execute:
        parser.error(scenario['blocked'])
    turns = scenario.get('turns') or [{'prompt': scenario['prompt']}]
    if args.turn > len(turns):
        parser.error('No such turn')
    turn = turns[args.turn - 1]
    destination = evidence / f'turn-{args.turn:02}'
    if destination.exists():
        parser.error('This turn already has evidence; preserve it and prepare a fresh run')
    if not args.execute:
        print(json.dumps({'turn': args.turn, 'gate': turn.get('gate'), 'prompt': turn['prompt']}))
        return
    destination.mkdir()
    save(destination / 'turn.json', turn)
    # External input is supplied only after the evaluator explicitly advances.
    for name, content in turn.get('files', {}).items():
        path = safe_path(repo, name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    success = run_turn(repo, root / 'plugin', scenario, meta, turn, args.turn, destination)
    if success:
        meta['completed_turn'] = args.turn
    save(evidence / 'metadata.json', meta)
    if not success:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
