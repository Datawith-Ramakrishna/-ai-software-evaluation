import os
import sys
from pathlib import Path

MODE = os.environ.get("EVAL_MODE", "baseline")
if MODE not in {"baseline", "ai_assisted"}:
    raise RuntimeError("EVAL_MODE must be baseline or ai_assisted")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / MODE))
