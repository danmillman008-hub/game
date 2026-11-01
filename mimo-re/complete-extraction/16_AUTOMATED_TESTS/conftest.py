import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
FIX = ROOT / "05_LESSON_DSL" / "fixtures"

def load_fixture(name):
    return json.loads((FIX / name).read_text(encoding="utf-8"))
