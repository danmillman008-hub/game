"""Validator tests: the content-pack validator and the ESQ bank builder/validator.

These exercise the real tools the README tells authors to use — no existence-only tests.
"""
from __future__ import annotations

import csv
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import pytest

MIMO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MIMO / "content-templates/mimo-offline/validator"))
sys.path.insert(0, str(MIMO / "content-templates/epm-question-bank/tools"))

import validate_pack  # noqa: E402
import validate_bank  # noqa: E402
import build_esq  # noqa: E402

CONTENT = MIMO / "content"
TEMPLATES = MIMO / "content-templates"


def build_bank(csv_path: Path, out: Path) -> Path:
    """Drive the real builder the way its CLI does: read rows → build → write the .esq ZIP."""
    rows = build_esq.read_rows(csv_path)
    manifest, paper, answers = build_esq.build(
        rows,
        package_id="ir.mimo.test.pack",
        title="بانک آزمون تست",
        year=2026,
        subject="English (Konkur-style)",
    )
    build_esq.write_package(out, manifest, paper, answers, 2026)
    return out


def codes(pack: Path) -> set[str]:
    problems = validate_pack.check_pack(pack)
    return {p["code"] for p in problems}


@pytest.fixture()
def copy_pack(tmp_path):
    def _copy(name: str) -> Path:
        dst = tmp_path / name
        shutil.copytree(TEMPLATES / "mimo-offline" / name, dst)
        return dst
    return _copy


# ---------------------------------------------------------------- content packs
def test_shipped_packs_are_valid():
    for name in ("demo", "example-content-pack", "blank-content-pack"):
        pack = CONTENT / name if (CONTENT / name).is_dir() else TEMPLATES / "mimo-offline" / name
        assert validate_pack.check_pack(pack) == [], f"{name} should validate"


def test_missing_tutorial_file_is_reported(copy_pack):
    pack = copy_pack("example-content-pack")
    (pack / "tutorial-1001.json").unlink()
    assert "E007" in codes(pack)


def test_interaction_outside_code_is_reported(copy_pack):
    pack = copy_pack("example-content-pack")
    tutorial = json.loads((pack / "tutorial-1001.json").read_text(encoding="utf-8"))
    lesson = tutorial["chapters"][0]["lessons"][0]
    lesson["body"] = (
        '<code codelang="js" version="2" name="x"><content>let x = 1;</content>'
        '<interactions><interaction type="validatedInput" startIndex="40" endIndex="60"/></interactions></code>'
    )
    (pack / "tutorial-1001.json").write_text(json.dumps(tutorial, ensure_ascii=False), encoding="utf-8")
    problems = validate_pack.check_pack(pack)
    assert [p for p in problems if p["code"] == "E015"]


def test_selection_without_correct_item_is_reported(copy_pack):
    pack = copy_pack("example-content-pack")
    tutorial = json.loads((pack / "tutorial-1001.json").read_text(encoding="utf-8"))
    lesson = tutorial["chapters"][0]["lessons"][0]
    lesson["body"] = '<selection question="q"><item value="1">a</item><item value="2">b</item></selection>'
    (pack / "tutorial-1001.json").write_text(json.dumps(tutorial, ensure_ascii=False), encoding="utf-8")
    assert {"E016"} <= codes(pack)


def test_duplicate_lesson_and_unknown_tag_are_reported(copy_pack):
    pack = copy_pack("blank-content-pack")
    tutorial = json.loads((pack / "tutorial-1001.json").read_text(encoding="utf-8"))
    lesson = tutorial["chapters"][0]["lessons"][0]
    lesson["body"] = "<p>سلام</p><mystery>ناشناخته</mystery>"
    tutorial["chapters"][0]["lessons"].append(dict(lesson))
    (pack / "tutorial-1001.json").write_text(json.dumps(tutorial, ensure_ascii=False), encoding="utf-8")
    found = codes(pack)
    assert {"E011", "E014"} <= found


def test_missing_local_asset_is_reported(copy_pack):
    pack = copy_pack("blank-content-pack")
    tutorial = json.loads((pack / "tutorial-1001.json").read_text(encoding="utf-8"))
    tutorial["chapters"][0]["lessons"][0]["body"] = '<p><img src="assets/not-there.png" alt="x"/></p>'
    (pack / "tutorial-1001.json").write_text(json.dumps(tutorial, ensure_ascii=False), encoding="utf-8")
    assert "E019" in codes(pack)


def test_validator_cli_exit_codes(tmp_path):
    cli = TEMPLATES / "mimo-offline/validator/validate_pack.py"
    ok = subprocess.run([sys.executable, str(cli), str(CONTENT / "demo")], capture_output=True, text=True)
    assert ok.returncode == 0 and "معتبر" in ok.stdout
    bad = subprocess.run([sys.executable, str(cli), str(tmp_path / "nope")], capture_output=True, text=True)
    assert bad.returncode == 3


def test_persian_error_messages_are_present(copy_pack):
    pack = copy_pack("example-content-pack")
    (pack / "tutorial-1001.json").unlink()
    problems = validate_pack.check_pack(pack)
    assert problems
    persian = re.compile(r"[\u0600-\u06FF]")
    assert all(p["remedy"] and persian.search(p["message"]) and persian.search(p["remedy"]) for p in problems)


# ---------------------------------------------------------------- EPM bank
def test_example_csv_builds_a_valid_package(tmp_path):
    csv_path = TEMPLATES / "epm-question-bank/data/example-questions.csv"
    out = build_bank(csv_path, tmp_path / "bank.esq")
    with zipfile.ZipFile(out) as zf:
        manifest = json.loads(zf.read("manifest.json"))
    assert manifest["schemaVersion"] == "1.0"
    validate_bank.problems.clear()
    validate_bank.validate_structure(out)
    assert validate_bank.problems == []


def test_builder_rejects_five_options_and_bad_answer(tmp_path):
    csv_text = (TEMPLATES / "epm-question-bank/data/example-questions.csv").read_text(encoding="utf-8")
    header, *rows = csv_text.splitlines()

    # a fifth option arrives as an extra column; the builder must refuse rather than silently drop it
    five = tmp_path / "five.csv"
    five.write_text("\n".join([header, rows[0] + ",E"]) + "\n", encoding="utf-8")
    with pytest.raises(SystemExit):
        build_bank(five, tmp_path / "bad.esq")

    # an invalid answer letter must be refused
    record = next(csv.DictReader([header, rows[0]]))
    record["correct"] = "X"
    bad = tmp_path / "bad-answer.csv"
    with bad.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(record))
        writer.writeheader()
        writer.writerow(record)
    with pytest.raises(SystemExit):
        build_bank(bad, tmp_path / "bad2.esq")


def test_validator_flags_three_option_question(tmp_path):
    csv_path = TEMPLATES / "epm-question-bank/data/example-questions.csv"
    out = build_bank(csv_path, tmp_path / "ok.esq")
    # rewrite the package so question 1 has only three options
    with zipfile.ZipFile(out) as zf:
        files = {n: zf.read(n) for n in zf.namelist()}
    paper_key = next(k for k in files if k.startswith("papers/"))
    paper = json.loads(files[paper_key])
    paper["units"][0]["questions"][0]["options"] = paper["units"][0]["questions"][0]["options"][:3]
    files[paper_key] = json.dumps(paper, ensure_ascii=False).encode()
    broken = tmp_path / "broken.esq"
    with zipfile.ZipFile(broken, "w") as zf:
        for name, data in files.items():
            zf.writestr(name, data)
    validate_bank.problems.clear()
    validate_bank.validate_structure(broken)
    assert any("۴ گزینه" in p for p in validate_bank.problems)


def test_every_question_has_exactly_one_correct_answer(tmp_path):
    csv_path = TEMPLATES / "epm-question-bank/data/example-questions.csv"
    out = build_bank(csv_path, tmp_path / "bank.esq")
    with zipfile.ZipFile(out) as zf:
        answers = [json.loads(zf.read(n)) for n in zf.namelist() if n.startswith("answers/")]
    for block in answers:
        for entry in block["answers"].values():
            assert entry["correctOption"] in {"A", "B", "C", "D"}
