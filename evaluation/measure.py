
"""Track real development sessions for AI vs non-AI evaluation."""

import argparse
import csv
import json
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVALUATION_DIR = ROOT / "evaluation"

STATE = EVALUATION_DIR / ".active_session.json"
OUTPUT = EVALUATION_DIR / "sessions.csv"

MODES = ("baseline", "ai_assisted")


def main():
    parser = argparse.ArgumentParser(
        description="Track real development time"
    )

    parser.add_argument(
        "action",
        choices=("start", "stop", "status")
    )

    parser.add_argument(
        "mode",
        nargs="?",
        choices=MODES
    )

    args = parser.parse_args()

    EVALUATION_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    if args.action == "status":
        if STATE.exists():
            print(STATE.read_text(encoding="utf-8"))
        else:
            print("No active session")
        return

    if args.action == "start":
        if args.mode is None:
            parser.error("start requires a mode")

        if STATE.exists():
            parser.error("A session is already running")

        session = {
            "mode": args.mode,
            "started_at": datetime.now(
                timezone.utc
            ).isoformat(),
            "start_epoch": time.time()
        }

        STATE.write_text(
            json.dumps(session),
            encoding="utf-8"
        )

        print(f"Started {args.mode}")
        return

    if not STATE.exists():
        parser.error("No active session to stop")

    data = json.loads(
        STATE.read_text(encoding="utf-8")
    )

    if data.get("mode") not in MODES:
        parser.error("Invalid session mode")

    start_epoch = data.get("start_epoch")

    if not isinstance(start_epoch, (int, float)):
        parser.error("Invalid session start time")

    minutes = round(
        max(0, time.time() - start_epoch) / 60,
        3
    )

    file_exists = OUTPUT.exists()

    with OUTPUT.open(
        "a",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "mode",
                "started_at",
                "ended_at",
                "minutes"
            ]
        )

        if not file_exists or OUTPUT.stat().st_size == 0:
            writer.writeheader()

        writer.writerow({
            "mode": data["mode"],
            "started_at": data["started_at"],
            "ended_at": datetime.now(
                timezone.utc
            ).isoformat(),
            "minutes": minutes
        })

    STATE.unlink()

    print(
        f"Saved {minutes:.3f} minutes "
        f"for {data['mode']}"
    )


if __name__ == "__main__":
    main()
