"""Start/stop real wall-clock development sessions (no fabricated times)."""
import argparse
import csv
import json
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / 'evaluation' / '.active_session.json'
OUTPUT = ROOT / 'evaluation' / 'sessions.csv'
MODES = ('baseline', 'ai_assisted')

def main():
    parser = argparse.ArgumentParser(description='Track actual working time per condition')
    parser.add_argument('action', choices=['start', 'stop', 'status'])
    parser.add_argument('mode', nargs='?', choices=MODES)
    args = parser.parse_args()
    if args.action == 'status':
        print(STATE.read_text(encoding='utf-8') if STATE.exists() else 'No active session')
        return
    if args.action == 'start':
        if not args.mode:
            parser.error('start requires a mode')
        if STATE.exists():
            parser.error('A session is already running; stop it first')
        STATE.write_text(json.dumps({'mode': args.mode, 'started_at': datetime.now(timezone.utc).isoformat(), 'start_epoch': time.time()}), encoding='utf-8')
        print(f'Started {args.mode}; stop when coding and debugging are finished')
        return
    if not STATE.exists():
        parser.error('No session to stop')
    data = json.loads(STATE.read_text(encoding='utf-8'))
    minutes = round((time.time() - data['start_epoch']) / 60, 3)
    exists = OUTPUT.exists()
    with OUTPUT.open('a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['mode','started_at','ended_at','minutes'])
        if not exists:
            writer.writeheader()
        writer.writerow({'mode': data['mode'], 'started_at': data['started_at'], 'ended_at': datetime.now(timezone.utc).isoformat(), 'minutes': minutes})
    STATE.unlink()
    print(f'Saved {minutes:.3f} minutes for {data["mode"]}')

if __name__ == '__main__':
    main()
