"""Mission-06 semantic tests.

These validate *consistency between evidence, documents and derived artefacts* - not file existence.
Every test names the claim it protects and fails if a document drifts from the extracted evidence.
"""
import csv
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
M5 = ROOT.parent / "mission-05"


def load(p):
    return json.loads((ROOT / p).read_text(encoding="utf-8"))


def docs():
    return [p for p in ROOT.rglob("*.md") if p.is_file()]


# --- evidence ↔ artefacts -------------------------------------------------
def test_evidence_files_referenced_by_docs_exist():
    missing = []
    for p in docs():
        for m in re.finditer(r"(?:\.\./)?(evidence/[A-Za-z0-9_./-]+\.(?:json|csv|gz))", p.read_text(encoding="utf-8")):
            ref = m.group(1)
            base = ROOT if not m.group(0).startswith("..") else ROOT.parent
            if not (base / ref).exists() and not (M5 / ref.replace("mission-05/", "")).exists():
                missing.append((p.name, ref))
    assert not missing, f"dangling evidence references: {missing[:5]}"


def test_tag_mapping_covers_all_29_tags_with_contiguous_ordinals():
    rows = list(csv.DictReader((ROOT / "03_DSL_AND_RUNTIME/24_DSL_TAG_MAPPING.csv").open(encoding="utf-8")))
    assert len(rows) == 29
    assert [int(r["ordinal"]) for r in rows] == list(range(29))
    enum = {c["name"] for c in load("../mission-05/evidence/TAG_ENUM.json")["constants"]}
    assert {r["enum"] for r in rows} == enum, "CSV enum set diverges from Tag.<clinit>"


def test_every_grammar_consumer_is_a_te_parser():
    g = load("evidence/PARSER_GRAMMAR.json")
    classes = {c["class"] for c in g["classes"]}
    for c in g["classes"]:
        assert re.fullmatch(r"te\.[a-g]", c["class"]), c["class"]
        for m in c["methods"]:
            if not m.get("tag"):
                continue
            assert m["tag"] in classes or re.fullmatch(r"te\.[a-g]", m["tag"])


def test_grammar_requires_tags_are_lowercase_literals():
    g = load("evidence/PARSER_GRAMMAR.json")
    for c in g["classes"]:
        for m in c["methods"]:
            for r in m["requires"]:
                # tag literals are mostly lowercase, but the DSL really uses camelCase
                # (collapsibleLines); only forbid spaces and uppercase-initial XML names
                assert " " not in r["tag"] and r["tag"][0].islower(), r


# --- AST schema -----------------------------------------------------------
def test_ast_schema_refs_resolve():
    s = load("03_DSL_AND_RUNTIME/19_AST_SCHEMA.json")
    defs = set(s["$defs"])
    refs = set(re.findall(r"#/\$defs/([A-Za-z]+)", json.dumps(s)))
    assert refs <= defs, refs - defs
    assert "Module" in defs and len(s["$defs"]["Interaction"]["properties"]["type"]["enum"]) == 4


def test_ast_interaction_offsets_documented_as_content_slices():
    s = load("03_DSL_AND_RUNTIME/19_AST_SCHEMA.json")
    assert "Code.content" in s["$defs"]["Interaction"]["properties"]["startIndex"]["description"]


# --- grading --------------------------------------------------------------
def test_grading_vectors_match_documented_filter():
    fx = load("111_TEST_FIXTURES/grading_vectors.json")
    norm = lambda s: re.sub(r"[^a-z0-9<.]", "", s.lower())
    for v in fx["vectors"]:
        assert norm(v["raw"]) == v["normalised_raw"], v
        assert norm(v["expected"]) == v["normalised_expected"], v
        assert (v["normalised_raw"] == v["normalised_expected"]) == v["normalised"], v
        assert (v["raw"] == v["expected"]) == v["exact"], v


def test_documented_false_positive_exists_in_vectors():
    fx = load("111_TEST_FIXTURES/grading_vectors.json")
    hazards = [v for v in fx["vectors"] if v["normalised"] and not v["exact"]]
    assert any("my_var" == v["raw"] for v in hazards)


# --- state machine --------------------------------------------------------
def test_state_machine_transitions_reference_known_states():
    m = load("05_LEARNER_MODEL/38_PROGRESS_STATE_TRANSITIONS.json")["exercise_machine"]
    states = set(m["states"])
    for t in m["transitions"]:
        assert t["from"] in states
        for target in t["to"].split("|"):
            assert target in states, target


def test_no_pass_threshold_or_mastery_state_claimed():
    m = load("05_LEARNER_MODEL/38_PROGRESS_STATE_TRANSITIONS.json")["exercise_machine"]
    blob = json.dumps(m).lower()
    assert "mastery" not in blob and "threshold" not in m["states"]


# --- DTO / schema consistency --------------------------------------------
def test_schemas_properties_are_backed_by_extracted_fields():
    dto = load("evidence/DTO_FIELDS.json")
    checked = 0
    for sch in (ROOT / "50_REQUEST_RESPONSE_SCHEMAS").glob("*.schema.json"):
        s = json.loads(sch.read_text(encoding="utf-8"))
        cls = s["x-evidence"]["class"]
        fields = {f["name"] for f in dto[cls]["fields"]}
        assert set(s["properties"]) <= fields, (sch.name, set(s["properties"]) - fields)
        checked += 1
    assert checked >= 12


def test_content_model_lesson_identifier_has_five_long_parts():
    d = load("evidence/CONTENT_MODEL_FIELDS.json")["com.getmimo.data.content.model.track.LessonIdentifier"]
    names = {f["name"]: f["type"] for f in d["fields"]}
    for k in ("trackId", "trackVersion", "tutorialId", "chapterId", "lessonId"):
        assert names[k] == "long"
    assert len([f for f in d["fields"] if f["type"] == "long"]) == 5


def test_executable_file_carries_solution():
    d = load("evidence/CONTENT_MODEL_FIELDS.json")["com.getmimo.data.content.model.track.LessonContent$Executable$File"]
    assert "solvedContent" in {f["name"] for f in d["fields"]}


# --- network claims -------------------------------------------------------
def test_verb_counts_in_docs_match_catalogue():
    rows = list(csv.DictReader((M5 / "evidence/API_CATALOG_V2.csv").open(encoding="utf-8")))
    from collections import Counter
    c = Counter(r["verb"] for r in rows)
    assert (c["GET"], c["POST"], c["PATCH"], c["PUT"], c["DELETE"]) == (28, 24, 4, 2, 4), c
    t = (ROOT / "07_NETWORK/52_ENDPOINT_BINDING.md").read_text(encoding="utf-8")
    assert "PATCH" in t and "PUT" in t
    assert "4 `@PATCH`" in t and "2 `@PUT`" in t


def test_base_urls_documented_consistently():
    t = (ROOT / "07_NETWORK/47_BASE_URL_AND_ENVIRONMENTS.md").read_text(encoding="utf-8")
    assert "https://api.mimo.org" in t and "api-testing.mimo.org" in t
    assert "wss://api.mimo.org/v1/run/socket" in t


# --- integrity / runtime discipline --------------------------------------
def test_no_document_claims_runtime_verification():
    # Any sentence mentioning the label must be a negation/limitation statement.
    allow = re.compile(r"(\bno\b|\bnot\b|\bnever\b|\bnone\b|\bcannot\b|\bwould\b|\b0\b|blocked|upgrade|unblock|صفر|هیچ)")
    offenders = []
    for p in docs():
        for line in p.read_text(encoding="utf-8").splitlines():
            if "VERIFIED_RUNTIME" in line and not allow.search(line.lower()):
                offenders.append((p.name, line.strip()[:90]))
    assert not offenders, offenders[:5]


def test_integrity_watermark_count_matches_baseline():
    base = load("00_BASELINE/APK_MANIFEST.json")
    assert base["sha256"].startswith("48ce1740")
    doc = (ROOT / "14_SECURITY/91_INTEGRITY_AND_TAMPERING.md").read_text(encoding="utf-8")
    assert "11,543" in doc
    assert "YOUAREFINISHED" in doc


# --- diagrams / specs -----------------------------------------------------
def test_twenty_sequence_diagrams_are_mermaid():
    diag = sorted((ROOT / "107_SYSTEM_SEQUENCE_DIAGRAMS").glob("*.mmd"))
    assert len(diag) == 20
    for d in diag:
        first = d.read_text(encoding="utf-8").strip().splitlines()[0]
        assert first.strip() == "sequenceDiagram", d.name


def test_fifteen_specs_each_have_must_sections():
    specs = sorted((ROOT / "17_INDEPENDENT_SPECS").glob("*.md"))
    assert len(specs) == 15
    for s in specs:
        assert "## MUST" in s.read_text(encoding="utf-8"), s.name


def test_open_questions_register_labels_are_valid_enum():
    t = (ROOT / "16_INDEX_AND_EVIDENCE/100_OPEN_QUESTIONS.md").read_text(encoding="utf-8")
    labels = {"VERIFIED_STATIC", "VERIFIED_RUNTIME", "VERIFIED_EXPERIMENTAL", "INFERRED", "UNKNOWN", "NOT_RECOVERED", "BLOCKED", "INFERRED (kept)"}
    for line in t.splitlines():
        if line.startswith("| Q-") or line.startswith("| U-"):
            assert line.rstrip("| ").split("|")[-1].strip() in labels, line


def test_evidence_db_paths_exist():
    db = load("16_INDEX_AND_EVIDENCE/99_EVIDENCE_DB.json")
    for k, v in db.items():
        p = v["path"]
        base = ROOT
        assert (base / p).exists(), (k, p)
        assert v["label"] in {"VERIFIED_STATIC","VERIFIED_RUNTIME","VERIFIED_EXPERIMENTAL","INFERRED","UNKNOWN","NOT_RECOVERED","BLOCKED"}
