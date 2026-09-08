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
    return repo


def clean_env():
    env = os.environ.copy()
    for key in ('ANTHROPIC_API_KEY', 'ANTHROPIC_AUTH_TOKEN', 'ANTHROPIC_BASE_URL',
                'CLAUDE_CODE_USE_BEDROCK', 'CLAUDE_CODE_USE_VERTEX', 'CLAUDE_CODE_USE_FOUNDRY'):
        env.pop(key, None)
    return env


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('name', help='Scenario name, or fixture name with --fixture-only')
    parser.add_argument('--fixture-only', action='store_true')
    parser.add_argument('--execute', action='store_true', help='Start a subscription Claude Code run')
    parser.add_argument('--model', choices=['sonnet', 'opus'], default='sonnet')
    parser.add_argument('--timeout', type=int, default=300)
    args = parser.parse_args()
    if args.timeout <= 0 or not re.fullmatch(r'[a-z0-9-]+', args.name):
        parser.error('Use a positive timeout and a fixture/scenario name')
    if args.fixture_only and args.execute:
        parser.error('--fixture-only cannot execute an agent')
    scenario = None if args.fixture_only else json.loads((BASE / 'scenarios' / (args.name + '.json')).read_text())
    if args.execute and scenario.get('blocked'):
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
    hashes = {str(p.relative_to(bundle)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(bundle.rglob('*')) if p.is_file()}
    meta = {'state': 'prepared', 'judgment': 'not run', 'fixture': name, 'repo': str(repo),
            'source_revision': git(REPO, 'rev-parse', 'HEAD'),
            'source_status': git(REPO, 'status', '--short'), 'plugin_sha256': hashes,
            'baseline': git(repo, 'rev-parse', 'HEAD'), 'model_requested': args.model,
            'effort': 'medium', 'mode': 'explicit-instructions', 'timeout_seconds': args.timeout}
    save(evidence / 'metadata.json', meta)
    shutil.copyfile(Path(__file__), evidence / 'runner.py')
    print(json.dumps({'repo': str(repo), 'evidence': str(evidence)}), flush=True)
    if not args.execute:
        return
    env = clean_env()
    try:
        cfg = dict(scenario.get('render_config', {}))
        config = repo / '.sdd.yml'
        if config.exists():
            for line in config.read_text().splitlines():
                line = line.split('#', 1)[0]
                if ':' in line:
                    key, value = line.split(':', 1)
                    cfg[key.strip()] = value.strip()
        system = ('Use actual tools in this disposable repository. Keep mutations inside it. '
                  'No remote or PR service is available; report that limitation at handover. '
                  'Do not use other agents. Read bundled references when instructed.\n')
        sources = ([bundle / 'templates/project/CLAUDE.section.md'] if scenario['resident'] else [])
        sources += [bundle / 'skills' / skill / 'SKILL.md' for skill in scenario['skills']]
        for source in sources:
            text = source.read_text().replace('${CLAUDE_PLUGIN_ROOT}', str(bundle))
            text = re.sub(r'\{\{(\w+)\}\}', lambda m: cfg.get(m[1], m[0]), text)
            system += '\n' + text
        (evidence / 'system.txt').write_text(system)
        (evidence / 'input.txt').write_text(scenario['prompt'])
        command = ['claude', '-p', '--model', args.model, '--effort', 'medium',
                   '--safe-mode', '--restricted', '--strict-mcp-config', '--no-session-persistence',
                   '--tools', 'Read,Write,Edit,Glob,Grep,Bash', '--allowedTools',
                   'Read,Write,Edit,Glob,Grep,Bash(git *),Bash(true),Bash(python3 verify.py),Bash(pwd),Bash(ls *)',
                   '--permission-mode', 'acceptEdits', '--add-dir', str(bundle),
                   '--system-prompt', system, '--output-format', 'stream-json', '--verbose']
        save(evidence / 'command.json', command)
        preflight = [['claude', 'auth', 'status'], ['claude', '--version']]
        save(evidence / 'preflight-commands.json', preflight)
        with (evidence / 'preflight-stderr.txt').open('w') as stderr:
            result = subprocess.run(preflight[0], env=env, text=True, stdout=subprocess.PIPE,
                                    stderr=stderr, timeout=30, check=True)
            auth = json.loads(result.stdout)
            meta['auth_method'] = auth.get('authMethod')
            if meta['auth_method'] != 'claude.ai':
                raise RuntimeError('Claude subscription authentication required')
            result = subprocess.run(preflight[1], env=env, text=True, stdout=subprocess.PIPE,
                                    stderr=stderr, timeout=30, check=True)
            meta['cli_version'] = result.stdout.strip()
        with (evidence / 'events.jsonl').open('w') as stdout, (evidence / 'stderr.txt').open('w') as stderr:
            process = subprocess.Popen(command, cwd=repo, env=env, stdin=subprocess.PIPE,
                                       stdout=stdout, stderr=stderr, text=True, start_new_session=True)
            try:
                process.communicate(scenario['prompt'], timeout=args.timeout)
                meta.update(state='finished', exit_code=process.returncode, judgment='unassessed')
            except (subprocess.TimeoutExpired, KeyboardInterrupt) as error:
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                meta.update(state=type(error).__name__, judgment='incomplete')
    except Exception as error:
        meta.update(state='error', error=str(error), judgment='incomplete')
        raise
    finally:
        meta.update(final_branch=git(repo, 'branch', '--show-current'),
                    final_status=git(repo, 'status', '--short'))
        (evidence / 'history.txt').write_text(git(repo, 'log', '--all', '--format=fuller', '--stat'))
        shutil.make_archive(str(evidence / 'final-repository'), 'gztar', root_dir=root, base_dir='repo')
        save(evidence / 'metadata.json', meta)
    if meta['state'] != 'finished' or meta.get('exit_code') != 0:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
