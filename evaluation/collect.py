"""Execute tests and coverage for each condition; write real measured results."""
import csv
import json
import os
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'evaluation' / 'results.csv'
MODES = ('baseline', 'ai_assisted')

def main():
    rows = []
    for mode in MODES:
        env = os.environ.copy()
        env['EVAL_MODE'] = mode
        junit = ROOT / 'evaluation' / f'{mode}_junit.xml'
        coverage = ROOT / 'evaluation' / f'{mode}_coverage.json'
        cmd = [sys.executable, '-m', 'pytest', 'tests', '-q',
               '--junitxml', str(junit), '--cov=calculator',
               '--cov-report=json:' + str(coverage), '--cov-fail-under=0']
        print('\n' + '=' * 18 + f' {mode} ' + '=' * 18, flush=True)
        completed = subprocess.run(cmd, cwd=ROOT, env=env, check=False)
        tests = failures = errors = skipped = 0
        if junit.exists():
            suite = ET.parse(junit).getroot()
            if suite.tag == 'testsuites':
                suite = suite.find('testsuite')
            tests = int(suite.get('tests', '0'))
            failures = int(suite.get('failures', '0'))
            errors = int(suite.get('errors', '0'))
            skipped = int(suite.get('skipped', '0'))
        percent = ''
        if coverage.exists():
            percent = round(json.loads(coverage.read_text(encoding='utf-8'))['totals']['percent_covered'], 2)
        rows.append({'mode': mode, 'tests_total': tests, 'tests_passed': tests - failures - errors - skipped,
                     'tests_failed': failures + errors, 'tests_skipped': skipped,
                     'coverage_percent': percent, 'pytest_exit_code': completed.returncode})
    with OUT.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f'\nWrote {OUT}')

if __name__ == '__main__':
    main()
