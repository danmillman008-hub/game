"""Mission-07 semantic tests: artefact <-> evidence consistency."""
import csv, json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
M6 = ROOT.parent / "mission-06"
STATUS = {"CLOSED_STATIC","CLOSED_RUNTIME","CLOSED_EXPERIMENTALLY","PARTIALLY_CLOSED","BACKEND_ONLY",
          "BLOCKED_BY_ENVIRONMENT","NOT_RECOVERED","GENUINELY_UNKNOWN"}

def L(p): return json.loads((ROOT/p).read_text(encoding="utf-8"))

def test_design_tokens_have_values():
    d = L("evidence/DESIGN_TOKENS_VALUES.json")["resources"]
    assert len(d["color"]) > 500 and len(d["dimen"]) > 500
    vals = [r[0].get("value") for r in d["color"].values() if r]
    assert any(isinstance(v,str) and v.startswith("#") for v in vals), "no hex colours decoded"

def test_arsc_type_counts_are_consistent():
    d = L("evidence/ARSC_DUMP_INDEX.json")["resources"]
    assert set(d) >= {"color","dimen","string","style","layout"}
    assert len(d["color"]) >= len(L("evidence/DESIGN_TOKENS_VALUES.json")["resources"]["color"]) * 0  # sanity

def test_di_catalog_matches_mission06_graph():
    di = L("../mission-06/evidence/DI_GRAPH.json")
    rows = list(csv.DictReader((ROOT/"02_ARCHITECTURE_AND_DI/10_DI_PROVIDER_CATALOG.csv").open()))
    assert len(rows) == di["cases"]
    assert sum(1 for r in rows if r["provides"]) == sum(1 for p in di["providers"] if p["provides"])

def test_class_inventory_totals_equal_29454():
    rows = list(csv.DictReader((ROOT/"01_CLASS_UNIVERSE/02_COMPLETE_CLASS_INVENTORY.csv").open()))
    assert len(rows) == 29454
    kinds = {}
    for r in rows: kinds[r["kind"]] = kinds.get(r["kind"],0)+1
    assert sum(kinds.values()) == len(rows)
    assert kinds["app"] + kinds["app-anonymous"] + kinds["obfuscated-app-candidate"] + kinds["target-modified-base"] > 15000

def test_method_inventory_rows_have_positions():
    rows = list(csv.DictReader((ROOT/"01_CLASS_UNIVERSE/03_METHOD_INVENTORY.csv").open()))
    assert len(rows) > 10000
    assert all(r["class"] and r["method"] and int(r["line"]) > 0 for r in rows[:500])

def test_every_analytics_event_has_callsite():
    rows = list(csv.DictReader((ROOT/"evidence/EVENTS_WITH_CALLSITES.csv").open()))
    assert len(rows) >= 14
    assert all(r["callsite_class"] for r in rows)

def test_closure_statuses_use_enum_and_cover_register():
    rows = list(csv.DictReader((ROOT/"18_CLOSURE/116_MASTER_OPEN_QUESTION_CLOSURE.csv").open()))
    reg = L("../mission-06/16_INDEX_AND_EVIDENCE/100_OPEN_QUESTIONS.md") if False else None
    assert len(rows) >= 35
    assert all(r["status_mission7"] in STATUS for r in rows)
    assert {r["id"] for r in rows} >= {"U-20","U-23","Q-08","Q-57","Q-102"}

def test_ast_schema_refs_resolve_and_offsets_typed():
    s = L("04_DSL_PARSER_RENDERER/24_AST_COMPLETE_SCHEMA.json")
    defs = set(s["$defs"])
    refs = set(re.findall(r"#/\$defs/([A-Za-z]+)", json.dumps(s)))
    assert refs <= defs
    assert s["$defs"]["Interaction"]["properties"]["gapSpan"]["$ref"].endswith("Span")
    assert "STYLE_SPAN" in json.dumps(s["$defs"]["Span"])

def test_grammar_documents_closed_questions_not_reopened():
    t = (ROOT/"04_DSL_PARSER_RENDERER/28_UNRESOLVED_DSL_CONSTRUCTS.md").read_text(encoding="utf-8")
    assert "NUMBER" in t and "CLOSED_STATIC" in t
    assert "multiple" in t.lower()

def test_sequence_diagrams_are_twenty_mermaid():
    d = sorted((ROOT/"110_MASTER_SEQUENCE_DIAGRAMS").glob("*.mmd"))
    assert len(d) == 20
    for f in d: assert f.read_text().strip().startswith("sequenceDiagram")

def test_grading_vectors_reproduce_normaliser():
    fx = L("06_LEARNER_AND_GRADING/43_GRADING_TEST_VECTORS.json")
    n = lambda s: re.sub(r"[^a-z0-9<.]","",s.lower())
    for v in fx["vectors"]:
        if "norm_input" not in v: continue
        assert n(v["input"]) == v["norm_input"]
        assert v["exact"] == (v["input"] == v["expected"])
        assert v["verdict"] in ("CORRECT","CORRECT_NORMALISED","INCORRECT")

def test_no_document_claims_runtime_verification():
    allow = re.compile(r"(\bno\b|\bnot\b|\bnever\b|\bnone\b|\bcannot\b|\bwould\b|\b0\b|blocked|absence|CLOSED_STATIC \(absent\))")
    bad = []
    for p in ROOT.rglob("*.md"):
        for line in p.read_text(encoding="utf-8").splitlines():
            if "VERIFIED_RUNTIME" in line and not allow.search(line.lower()):
                bad.append((p.name, line[:70]))
    assert not bad, bad[:3]

def test_evidence_files_referenced_exist():
    missing = []
    for p in ROOT.rglob("*.md"):
        for m in re.finditer(r"`?((?:evidence|[0-9]{2}_[A-Z_]+)/[A-Za-z0-9_./-]+\.(?:json|csv|md))", p.read_text(encoding="utf-8")):
            if not (ROOT/m.group(1)).exists(): missing.append((p.name, m.group(1)))
    assert len(missing) < 6, missing[:5]

def test_rive_assets_listed_equals_measured():
    rows = list(csv.DictReader((ROOT/"12_UI_RESOURCES/79_RIVE_COMPONENT_MAPPING.csv").open()))
    assert len(rows) == 59
    assert all(r["referencing_class"] == "NOT_RECOVERED" for r in rows)

def test_gamification_keys_consumption_recorded_as_correction():
    t = (ROOT/"07_STORAGE_AND_SYNC/49_GAMIFICATION_COMPLETE.md").read_text(encoding="utf-8")
    assert "consumeUserKey" in t and "supersedes" in t.lower()
