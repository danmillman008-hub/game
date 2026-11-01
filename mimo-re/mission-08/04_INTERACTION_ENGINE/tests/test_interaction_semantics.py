"""Source-derived reference models for the Mission-8 interaction engine.

These tests re-implement the *recovered* algorithms and assert the behaviour recorded in
SOURCE_DERIVED_TEST_VECTORS.json. They are semantic tests of the reconstruction, NOT runtime
observations of the app: a passing test proves the reference model matches the evidence, nothing more.
"""
import json
import pathlib
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
VECTORS = json.loads((ROOT / "SOURCE_DERIVED_TEST_VECTORS.json").read_text())

KEEP = set("<>():{},.")

# --- qm.i.a(String) -------------------------------------------------------
def normalise(text: str) -> str:
    # java: toLowerCase(Locale.US), keep Character.isLetterOrDigit(c) or c in KEEP
    out = []
    for ch in text.lower():
        if ch.isalnum() or ch in KEEP:
            out.append(ch)
    return "".join(out)


def validated_verdict(user: str, expected: str) -> str:
    # InteractiveLessonValidatedInputFragment.setupViews
    if normalise(user) != normalise(expected):
        return "INCORRECT"          # qm.g
    if user == expected:
        return "CORRECT"            # qm.e
    return "PARTIAL"                # qm.f


def selection_verdict(items) -> str:
    # nm.b.E0
    if not items:
        return "INCORRECT"
    selected = [i for i in items if i["selected"]]
    correct = [i for i in items if i["correct"]]
    if len(selected) != len(correct):
        return "INCORRECT"
    return "CORRECT" if all(i["selected"] == i["correct"] for i in items) else "INCORRECT"


def ordered_verdict(selected, expected) -> str:
    # im.d.E0 (fill the gap) and pm.b.E0 (spell)
    if len(selected) != len(expected):
        return "INCORRECT"
    return "CORRECT" if selected == expected else "INCORRECT"


def rendered(visibility: str, verdict: str) -> bool:
    # ModuleVisibility {ALWAYS, CORRECT, WRONG} evaluated at render time
    return {"ALWAYS": True, "CORRECT": verdict == "CORRECT", "WRONG": verdict == "INCORRECT"}[visibility]


def solved(tries: int) -> bool:
    # LessonProgress.isSolvedCorrectly(): tries >= 1
    return tries >= 1


# --- tests ---------------------------------------------------------------
def test_normaliser_vectors():
    for v in VECTORS["normaliser"]["vectors"]:
        assert normalise(v["input"]) == v["expected"], v


def test_normaliser_drops_whitespace_and_quotes():
    assert normalise('a = "b";') == "ab"
    assert normalise("A\nB\tC") == "abc"


def test_validated_input_vectors():
    for v in VECTORS["validated_input_verdict"]["vectors"]:
        assert validated_verdict(v["user"], v["expected"]) == v["verdict"], v


def test_partial_only_when_raw_differs_but_normalised_matches():
    assert validated_verdict("Hello  World", "Hello World") == "PARTIAL"
    assert validated_verdict("hello world", "Hello World") == "PARTIAL"
    assert validated_verdict("hello world!", "Hello World") == "PARTIAL"
    assert validated_verdict("Hello", "Hello World") == "INCORRECT"


def test_only_validated_input_has_a_partial_path():
    # qm.f is constructed at exactly one site in the dex (validated input fragment)
    outcomes = {validated_verdict("a", "b"), validated_verdict("a", "a"), validated_verdict("A", "a")}
    assert outcomes == {"INCORRECT", "CORRECT", "PARTIAL"}
    assert selection_verdict([{"text": "a", "correct": True, "selected": True}]) in {"CORRECT", "INCORRECT"}
    assert ordered_verdict([], ["a"]) == "INCORRECT"


def test_selection_vectors():
    for v in VECTORS["selection_verdict"]["vectors"]:
        assert selection_verdict(v["items"]) == v["verdict"].split(" ")[0], v


def test_selection_requires_exact_set():
    items = [{"text": "a", "correct": True, "selected": False},
             {"text": "b", "correct": True, "selected": True}]
    assert selection_verdict(items) == "INCORRECT"
    items[0]["selected"] = True
    assert selection_verdict(items) == "CORRECT"


def test_fill_the_gap_and_spell_vectors():
    for v in VECTORS["fill_the_gap_verdict"]["vectors"]:
        assert ordered_verdict(v["selected"], v["expected"]) == v["verdict"], v
    v = VECTORS["spell_verdict"]["vectors"][0]
    assert ordered_verdict(v["selected"], v["expected"]) == v["verdict"]


def test_fill_the_gap_is_positional():
    assert ordered_verdict(["a", "b"], ["b", "a"]) == "INCORRECT"


def test_visibility_vectors():
    for v in VECTORS["module_visibility"]["vectors"]:
        assert rendered(v["visibility"], v["verdict"]) is v["rendered"], v


def test_selection_cannot_be_gated():
    # structural: no visibility field in the Selection model, no visible-if in te.e vocabulary
    data = json.loads((ROOT / "SIX_MODULE_VARIANTS.json").read_text())
    sel = next(m for m in data["modules"] if m["variant"] == "Selection")
    assert all(f["role"] != "visibility gate" for f in sel["fields"])
    assert data["visibility_summary"]["without"] == ["Selection"]
    assert len(data["modules"]) == 6


def test_progress_completion_vectors():
    for v in VECTORS["progress_completion"]["vectors"]:
        assert solved(v["tries"]) is v["solved"], v


def test_grading_is_client_side_for_every_interactive_type():
    import csv
    with open(ROOT / "GRADING_OWNERSHIP_MATRIX.csv") as fh:
        rows = list(csv.DictReader(fh))
    interactive = [r for r in rows if "Executable" not in r["interaction_type"]]
    assert len(interactive) >= 7
    for r in interactive:
        assert r["ownership"] in {"client", "hybrid"}, r
        if r["ownership"] == "client":
            assert "http" not in r["grading_site"].lower()


def test_state_machine_invariants_present():
    sm = json.loads((ROOT / "INTERACTION_STATE_MACHINE.json").read_text())
    ids = {i["id"] for i in sm["invariants"]}
    assert {"INV-1", "INV-2", "INV-3", "INV-4"} <= ids
    targets = {(t["from"], t["to"]) for t in sm["transitions"]}
    assert ("SUBMITTED", "CORRECT") in targets
    assert ("SUBMITTED", "INCORRECT") in targets
    assert ("SUBMITTED", "PARTIALLY_CORRECT") in targets


def test_every_deliverable_exists():
    required = ["INTERACTION_MODULES_COMPLETE.md", "SIX_MODULE_VARIANTS.json",
                "MODULE_VISIBILITY_IMPLEMENTATION.md", "INTERACTION_CLASS_MAP.csv",
                "INTERACTION_METHOD_MAP.csv", "INTERACTION_INPUT_FLOW.json",
                "GRADING_OWNERSHIP_MATRIX.csv", "GRADING_IMPLEMENTATION.md",
                "OUTPUT_TYPE_SCHEMA.json", "OUTPUT_PRODUCER_CONSUMER_GRAPH.json",
                "FEEDBACK_ENGINE_COMPLETE.md", "INTERACTION_STATE_MACHINE.json",
                "INTERACTION_END_TO_END_TRACES.md", "SOURCE_DERIVED_TEST_VECTORS.json",
                "INTERACTION_UNKNOWN_BEHAVIORS.md"]
    missing = [f for f in required if not (ROOT / f).exists()]
    assert not missing, missing
