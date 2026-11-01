import json
import sys
from pathlib import Path

HANDOFF = Path(__file__).resolve().parent.parent
DATA = HANDOFF / "data"
sys.path.insert(0, str(HANDOFF / "tools"))


def load(name):
    with open(DATA / name, encoding="utf-8") as fh:
        return json.load(fh)
