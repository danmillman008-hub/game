"""Tests for the reference DSL implementation (spec §05, vectors TEST_VECTORS.md)."""
import json
import pytest
from conftest import load_fixture, ROOT
from lesson_dsl import (parse, validate, grade_gap, grade_selection, visible_paragraphs)

def doc(name):
    d = parse(load_fixture(name)["interactiveContent"])
    return d

# ---- vectors 1..3 : single gap -------------------------------------------------
def test_v1_correct_chip():
    d = doc("F01_fillthegap_js.json")
    cb = d.code_blocks[0]
    assert len(cb.gaps) == 1
    r = grade_gap(cb, {0: "shipping"})
    assert r["ok"] is True, r

def test_v2_distractor_chip_is_wrong():
    cb = doc("F01_fillthegap_js.json").code_blocks[0]
    assert "tax" in cb.distractors
    r = grade_gap(cb, {0: "tax"})
    assert r["ok"] is False and r["detail"][0]["status"] == "wrong"

def test_v3_unanswered():
    cb = doc("F01_fillthegap_js.json").code_blocks[0]
    r = grade_gap(cb, {})
    assert r["detail"][0]["status"] == "unanswered"

# ---- vectors 4..6 : multi-gap + reversed element order --------------------------
def test_v4_three_gaps():
    cb = doc("F02_multi_gap_html.json").code_blocks[0]
    assert len(cb.gaps) == 3
    answers = {0: "<h2>", 1: "Orders", 2: "</h2>"}
    assert grade_gap(cb, answers)["ok"] is True

def test_v5_partial_failure_rejects_block():
    cb = doc("F02_multi_gap_html.json").code_blocks[0]
    r = grade_gap(cb, {0: "<h1>", 1: "Orders", 2: "</h2>"})
    assert r["ok"] is False and len(r["detail"]) == 3

def test_v6_source_reconstruction():
    cb = doc("F02_multi_gap_html.json").code_blocks[0]
    assert cb.source() == "<h2>Orders</h2>"

# ---- vectors 7..10 : validatedInput + selection ---------------------------------
def test_v7_validated_input_correct():
    cb = doc("F03_validated_input_and_selection.json").code_blocks[0]
    assert len(cb.inputs) == 1
    assert grade_gap(cb, {1000: "await"})["ok"] is True

def test_v8_validated_input_case_sensitive():
    cb = doc("F03_validated_input_and_selection.json").code_blocks[0]
    assert grade_gap(cb, {1000: "Await"})["ok"] is False

def test_v9_selection_exact_set():
    sel = doc("F03_validated_input_and_selection.json").selections[0]
    assert grade_selection(sel, {2}) is True

def test_v10_selection_superset_is_wrong():
    sel = doc("F03_validated_input_and_selection.json").selections[0]
    assert grade_selection(sel, {1, 2}) is False

# ---- vectors 11..12 : database ---------------------------------------------------
def test_v11_database_expected_tables():
    d = doc("F04_database_block.json")
    assert len(d.databases) == 1
    t = d.databases[0]["tables"][0]
    assert t["name"] == "Result"
    assert t["headers"] == ["id", "title"]
    assert len(t["rows"]) == 2

def test_v12_database_bootstrap_kept():
    d = doc("F04_database_block.json")
    assert "CREATE TABLE books" in d.databases[0]["bootstrapScript"]

# ---- vector 13 : validation clean on our fixtures --------------------------------
@pytest.mark.parametrize("name", [
    "F01_fillthegap_js.json", "F02_multi_gap_html.json",
    "F03_validated_input_and_selection.json", "F04_database_block.json"])
def test_v13_fixtures_validate_clean(name):
    assert validate(doc(name)) == []

# ---- vectors 14..15 : corpus scale (from generated report) -----------------------
def test_v14_corpus_has_no_range_violations():
    rep = json.loads((ROOT / "05_LESSON_DSL" / "DSL_VALIDATION_REPORT.json").read_text(encoding="utf-8"))
    assert rep["documents"] == 20306
    assert rep["gaps"] == 29093
    assert rep["issues"].get("gap-out-of-range", 0) == 0
    assert rep["issues"].get("input-out-of-range", 0) == 0

def test_v15_corpus_interaction_density():
    rep = json.loads((ROOT / "05_LESSON_DSL" / "DSL_VALIDATION_REPORT.json").read_text(encoding="utf-8"))
    assert rep["code_blocks"] == 21108
    assert rep["gaps_per_block"]["0"] == 11151

# ---- vectors 16..17 : feedback gating --------------------------------------------
def test_v16_wrong_block_hidden_until_wrong_state():
    d = doc("F01_fillthegap_js.json")
    assert any("delivery cost" in p for p in visible_paragraphs(d, "wrong"))
    assert not any("delivery cost" in p for p in visible_paragraphs(d, "unanswered"))

def test_v17_correct_block_only_in_correct_state():
    d = doc("F03_validated_input_and_selection.json")
    assert any("async calls" in p for p in visible_paragraphs(d, "correct"))
    assert not any("async calls" in p for p in visible_paragraphs(d, "always"))

# ---- vectors 18..19 : negative validation ----------------------------------------
def test_v18_out_of_range_gap_detected():
    bad = ('<html><body><code name="a.js" version="2" codelang="javascript">'
           '<content><text value="x" /></content><interactions>'
           '<interaction type="fillTheGap"><options><option startIndex="5" endIndex="9" /></options>'
           '</interaction></interactions></code></body></html>')
    issues = validate(parse(bad))
    assert any(i.startswith("gap-out-of-range") for i in issues)

def test_v19_selection_without_correct_detected():
    bad = ('<html><body><selection multiple="multiple">'
           '<item value="1" correct="false">a</item></selection></body></html>')
    assert any("selection-without-correct" in i for i in validate(parse(bad)))

# ---- vector 20 : inline <code> is not a block ------------------------------------
def test_v20_inline_code_not_a_block():
    d = parse('<html><body><p>Use <code>&lt;b&gt;</code> here.</p></body></html>')
    assert d.code_blocks == []
    assert d.paragraphs
