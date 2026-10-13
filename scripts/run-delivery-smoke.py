"""Ten preregistered Codex exec branches; standard library; no retries.

prepare is model-free. run accepts exactly one branch and refuses repeats.
Raw evidence stays outside the repository. Authentication is never printed.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

COMMIT = '66230436b59d899ed924aaf4e93ef45a267d39a1'
SKILL_HASH = '3f72c7a402e18015b09685c565571303a881e91def04a24536352d41ff210f23'
BRANCHES = [g + str(n) for g in 'ABCDE' for n in (1, 2)]
MODEL = 'gpt-6.1-sol'
REASONING = 'medium'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def write(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def inventory(work):
    return {str(p.relative_to(work)).replace('\\', '/'): sha(p.read_bytes())
            for p in sorted(work.rglob('*')) if p.is_file()}

def prepare(repo, base):
    assert not base.exists(), 'Do not overwrite an existing experiment'
    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo).decode().strip()
    assert head == COMMIT
    assert not subprocess.check_output(['git', 'status', '--porcelain'], cwd=repo).strip()
    skill = (repo / 'SKILL.md').read_bytes()
    assert sha(skill) == SKILL_HASH
    spec_bytes = (repo / 'tests/research-delivery-near-pairs.md').read_bytes()
    spec = spec_bytes.decode('utf-8')
    groups = re.findall(r'共同输入：`([^`]+)`', spec)
    variants = dict(re.findall(r'- ([A-E][12]) 精确追加：`([^`]+)`', spec))
    assert len(groups) == 5 and sorted(variants) == BRANCHES
    base.mkdir(parents=True)
    records = {}
    codex = shutil.which('codex')
    assert codex
    for b in BRANCHES:
        work = base / 'work' / b
        home = base / 'homes' / b
        logs = base / 'logs' / b
        for p in (work, home, logs):
            p.mkdir(parents=True)
        target = work / '.agents/skills/physics-to-math-research'
        target.mkdir(parents=True)
        (target / 'SKILL.md').write_bytes(skill)
        shutil.copytree(repo / 'references', target / 'references')
        shutil.copyfile(Path.home() / '.codex/auth.json', home / 'auth.json')
        # Fresh home excludes global skills, rules, agents, plugins, MCP and memories.
        (home / 'config.toml').write_text('[windows]\nsandbox = "elevated"\n', encoding='utf-8')
        prompt = groups['ABCDE'.index(b[0])] + variants[b]
        assert prompt == groups['ABCDE'.index(b[0])] + variants[b]
        (logs / 'prompt.txt').write_text(prompt, encoding='utf-8')
        assert sha((target / 'SKILL.md').read_bytes()) == SKILL_HASH
        assert not (work / 'tests').exists()
        records[b] = {'prompt': prompt, 'prompt_sha256': sha(prompt.encode()),
                      'state': 'NOT RUN', 'before': inventory(work)}
    manifest = {'run_id': base.name, 'prepared_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'tested_commit': COMMIT, 'skill_version': '0.2.5', 'skill_sha256': SKILL_HASH,
                'spec_sha256': sha(spec_bytes), 'driver_sha256': sha(Path(__file__).read_bytes()),
                'model_requested': MODEL, 'reasoning_requested': REASONING, 'codex': codex,
                'branches': records, 'conditions': 'Fresh CODEX_HOME; native project skill discovery; workspace-write; approval never; no retries'}
    write(base / 'manifest.json', manifest)
    print(json.dumps({'self_check': 'PASS', 'branches': len(records), 'driver_sha256': manifest['driver_sha256']}, indent=2))

def run(base, branch):
    mp = base / 'manifest.json'
    m = json.loads(mp.read_text(encoding='utf-8'))
    assert sha(Path(__file__).read_bytes()) == m['driver_sha256'], 'Frozen driver changed'
    r = m['branches'][branch]
    assert r['state'] == 'NOT RUN', 'No automatic retry permitted'
    if branch != 'A1':
        assert m['branches']['A1'].get('gate_verified') is True, 'A1 must be externally verified first'
    work, home, logs = [base / folder / branch for folder in ('work', 'homes', 'logs')]
    assert inventory(work) == r['before']
    assert sha((logs / 'prompt.txt').read_bytes()) == r['prompt_sha256']
    cmd = [m['codex'], '-a', 'never', 'exec', '--skip-git-repo-check', '--ignore-user-config',
           '--ignore-rules', '-C', str(work), '-s', 'workspace-write', '-m', MODEL,
           '-c', 'model_reasoning_effort="' + REASONING + '"',
           '-c', 'windows.sandbox="elevated"', '--json', '--color', 'never',
           '-o', str(logs / 'answer.md'), '-']
    env = os.environ.copy()
    env['CODEX_HOME'] = str(home)
    # Do not use inherited project/app credentials or instruction injection.
    for key in list(env):
        if key.startswith(('CODEX_', 'OPENAI_', 'AZURE_OPENAI_')) and key != 'CODEX_HOME':
            del env[key]
    r.update(state='STARTED', started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), command=cmd)
    write(mp, m)
    with (logs / 'events.jsonl').open('wb') as out, (logs / 'stderr.txt').open('wb') as err:
        try:
            proc = subprocess.run(cmd, input=r['prompt'].encode('utf-8'), stdout=out, stderr=err,
                                  cwd=work, env=env, timeout=600)
            r['exit_code'] = proc.returncode
            r['state'] = 'EXECUTED' if proc.returncode == 0 else 'EXECUTION_ERROR'
        except subprocess.TimeoutExpired:
            r.update(state='TIMEOUT', exit_code=None)
    r['ended_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    r['after'] = inventory(work)
    r['file_changes'] = {k: v for k, v in r['after'].items() if r['before'].get(k) != v}
    r['deleted_files'] = sorted(set(r['before']) - set(r['after']))
    events = []
    for line in (logs / 'events.jsonl').read_text(encoding='utf-8', errors='replace').splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    r['usage'] = [e.get('usage') for e in events if e.get('type') == 'turn.completed']
    r['skill_loading'] = 'REQUIRES_TRACE_REVIEW'
    write(mp, m)
    print(json.dumps({'branch': branch, 'state': r['state'], 'exit_code': r['exit_code'],
                      'usage': r['usage'], 'file_changes': r['file_changes']}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['prepare', 'run'])
    parser.add_argument('--repo', type=Path)
    parser.add_argument('--base', type=Path, required=True)
    parser.add_argument('--branch', choices=BRANCHES)
    args = parser.parse_args()
    if args.action == 'prepare':
        prepare(args.repo, args.base)
    else:
        run(args.base, args.branch)
