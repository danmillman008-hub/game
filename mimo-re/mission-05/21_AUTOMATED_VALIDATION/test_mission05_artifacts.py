"""MISSION-05 automated validation.

These tests do not test Mimo. They test **this mission's evidence artifacts** — that the claims
written in the reports are backed by machine-readable data, that the data is internally consistent,
and that no proprietary material leaked into the repository.

Run: python -m pytest mimo-re/mission-05/21_AUTOMATED_VALIDATION -q
"""
from __future__ import annotations

import csv
import gzip
import json
import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]          # mimo-re/mission-05
REPO = ROOT.parents[1]                                       # repository root
EV = ROOT / "evidence"

REQUIRED_DOC_SECTIONS = ["## Scope", "## Method", "## Sources", "## Evidence labels",
                         "## Limitations", "## Unresolved", "## Reproduction"]


def load_csv(name):
    path = EV / name
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


# ---------------------------------------------------------------- API catalogue


def test_api_catalogue_has_62_endpoints():
    rows = load_csv("API_CATALOG_V2.csv")
    assert len(rows) == 62


def test_api_verbs_are_from_the_five_known_set():
    rows = load_csv("API_CATALOG_V2.csv")
    assert {r["verb"] for r in rows} == {"GET", "POST", "PATCH", "DELETE", "PUT"}


def test_retrofit_body_rule_is_never_violated():
    """Retrofit forbids @Body on GET/DELETE; a violation would falsify the verb assignment."""
    rows = load_csv("API_CATALOG_V2.csv")
    bad = [r["path"] for r in rows
           if r["verb"] in ("GET", "DELETE") and "BODY" in r["param_bindings"]]
    assert bad == [], f"verb assignment inconsistent with Retrofit rules: {bad}"


def test_every_path_is_absolute_and_has_a_response_type():
    rows = load_csv("API_CATALOG_V2.csv")
    for r in rows:
        assert r["path"].startswith("/"), r
        assert r["response_type"], f"missing response type for {r['path']}"


def test_path_placeholders_match_declared_path_params():
    """Every {placeholder} in a path must have a PATH binding with the same name."""
    rows = load_csv("API_CATALOG_V2.csv")
    for r in rows:
        placeholders = set(re.findall(r"\{(\w+)\}", r["path"]))
        bound = {b.split(":")[2] for b in r["param_bindings"].split(";")
                 if b and b.split(":")[1] == "PATH"}
        assert placeholders <= bound, f"{r['path']}: {placeholders - bound} unbound"


# ---------------------------------------------------------------- annotations


def test_parameter_annotations_are_cleanly_parsed():
    """Mission-04 emitted 162 garbage rows; the corrected pass must contain no control-char keys."""
    rows = load_csv("ANNOTATIONS_V2.csv.gz")
    params = [r for r in rows if r["scope"] == "parameter"]
    assert len(params) == 105
    for r in params:
        for key in json.loads(r["elements"] or "{}"):
            assert key.isprintable(), f"garbage annotation key {key!r}"


def test_annotation_scopes_are_exhaustive():
    rows = load_csv("ANNOTATIONS_V2.csv.gz")
    assert {r["scope"] for r in rows} == {"class", "field", "method", "parameter"}


# ---------------------------------------------------------------- DSL


def test_tag_enum_is_complete_and_ordered():
    data = json.load(open(EV / "TAG_ENUM.json", encoding="utf-8"))
    assert data["count"] == 29
    ordinals = [c["ordinal"] for c in data["constants"]]
    assert ordinals == list(range(29))
    names = {c["name"] for c in data["constants"]}
    for required in {"CODE", "CONTENT", "INTERACTIONS", "INTERACTION", "OUTPUT", "TABLE",
                     "COLLAPSIBLE_LINES", "OPTION", "SELECTION", "WEBVIEW", "DATABASE"}:
        assert required in names


def test_ast_schema_is_valid_json_schema_shape():
    doc = (ROOT / "04_CONTENT_AND_DSL" / "AST_AND_MODELS.md").read_text(encoding="utf-8")
    block = doc.split("```json", 1)[1].split("```", 1)[0]
    schema = json.loads(block)
    assert schema["$schema"].startswith("https://json-schema.org/")
    assert "Module" in schema["$defs"] and "Option" in schema["$defs"]


# ---------------------------------------------------------------- DTO / graph / progress


def test_dto_catalogue_rows_are_typed():
    rows = load_csv("DTO_CATALOG.csv")
    assert len(rows) >= 50
    for r in rows:
        assert r["dto"].startswith("L") and r["dto"].endswith(";")
        int(r["n_fields"])


def test_system_graph_edges_reference_existing_nodes():
    g = json.load(open(ROOT / "18_SYSTEM_GRAPH" / "system_graph.json", encoding="utf-8"))
    ids = {n["id"] for n in g["nodes"]}
    for edge in g["edges"]:
        assert edge["from"] in ids and edge["to"] in ids, edge
        assert edge["evidence"] in {"VERIFIED_STATIC", "INFERRED_HIGH", "INFERRED_MEDIUM",
                                    "INFERRED_LOW", "VERIFIED_RUNTIME", "UNKNOWN"}


def test_progress_semantics_are_documented_where_the_code_says_so():
    """Guard against a regression to mission-04's wrong model (tries == a counter)."""
    doc = (ROOT / "09_PROGRESS_AND_GAMIFICATION" / "PROGRESS_MODEL.md").read_text(encoding="utf-8")
    assert "0/1 correctness flag" in doc
    assert "tries >= 1" in doc


# ---------------------------------------------------------------- document hygiene


@pytest.mark.parametrize("doc", sorted(p for p in ROOT.rglob("*.md")
                                       if p.name not in {"README.md", "API_ENDPOINTS_TABLE.md"}))
def test_report_has_all_required_sections(doc):
    text = doc.read_text(encoding="utf-8")
    missing = [s for s in REQUIRED_DOC_SECTIONS if s not in text]
    assert missing == [], f"{doc.relative_to(ROOT)} missing {missing}"


def test_no_decompiled_sources_or_binaries_in_mission05():
    """RULE 6: decompiled Java, DEX and native libraries must never be committed by this mission.

    Scope note: `ttac-4.3.6.apk` sits at the repository root and predates this mission; it is
    recorded in the final audit as a pre-existing hygiene issue rather than silently deleted
    (RULE 2 forbids touching prior artifacts).
    """
    offenders = [str(p.relative_to(ROOT)) for p in ROOT.rglob("*")
                 if p.is_file() and p.suffix.lower() in {".apk", ".dex", ".so", ".java"}]
    assert offenders == [], f"proprietary/binary material staged: {offenders[:5]}"


def test_preexisting_root_apk_is_reported_not_deleted():
    legacy = REPO / "ttac-4.3.6.apk"
    audit = (ROOT / "22_FINAL_AUDIT" / "FINAL_AUDIT.md")
    if legacy.exists():
        assert audit.exists(), "pre-existing APK must be reported in the final audit"
        assert "ttac-4.3.6.apk" in audit.read_text(encoding="utf-8")


def test_mission4_artifacts_are_untouched():
    """RULE 2: the frozen mission-04 deliverable must remain present and complete."""
    frozen = REPO / "mimo-re" / "complete-extraction"
    assert (frozen / "README.md").exists()
    assert len(list(frozen.iterdir())) >= 18
