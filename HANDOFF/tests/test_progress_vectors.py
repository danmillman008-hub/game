"""Layer-B reference: reproduce data/progress_vectors.json exactly (HANDOFF/05)."""

import pytest

import reference_engine as re
from conftest import load

P = load("progress_vectors.json")


@pytest.mark.parametrize("vec", P["identity"]["vectors"], ids=lambda v: str(v["row_key"]["lessonId"]))
def test_identity_ignores_chapter(vec):
    ident, key = vec["identifier"], vec["row_key"]
    assert key == {"lessonId": ident["lessonId"], "tutorialId": ident["tutorialId"]}
    assert "chapterId" not in key
    assert vec["chapter_stored"] is False


def test_persisted_key_is_two_columns():
    assert P["identity"]["progress_pk"] == ["lesson_id", "tutorial_id"]
    assert P["identity"]["lesson_identifier_parts"] == 5


def test_creation_rule():
    vec = P["new_progress"]["vectors"][0]
    assert vec["expected"]["inQueue"] is True
    assert vec["expected"]["publishSetVersion"] == 753
    assert vec["tries"] == 0 and vec["attempts"] == 0


def test_ordering_guard_builds_entity_anyway():
    vec = P["ordering_guard"]["vectors"][0]
    assert vec["now"] < vec["startedAt"]
    assert vec["entity_built"] is True and vec["reported"] is True


@pytest.mark.parametrize("vec", P["counter_update"]["vectors"],
                         ids=lambda v: f"{v['verdict']}-C{v['C_before']}-d{v['d_before']}")
def test_counter_update(vec):
    got = re.apply_submission(vec["verdict"], None if vec["C_before"] == "null" else vec["C_before"],
                              vec["d_before"])
    for field, expected in vec["expected"].items():
        assert got[field] == expected, f"{field}: {got[field]} != {expected}"


@pytest.mark.parametrize("vec", P["completion_flag"]["vectors"], ids=lambda v: f"tries{v['tries']}")
def test_completion_flag(vec):
    assert re.is_solved(vec["tries"]) is vec["solved"]


def test_tries_is_a_flag_not_a_counter():
    """Repeated correct submissions never grow `tries` beyond 1 (04 §6)."""
    tries, c = 1, False
    for d in range(0, 4):
        out = re.apply_submission("CORRECT", c, d)
        tries, c = out["tries"], out["C_after"]
        assert tries in (0, 1)
    assert tries == 1


def test_store():
    vec = P["queue"]["vectors"][0]
    assert re.queue_store(vec["rows_before"], 1) == vec["rows_after"]


def test_move():
    vec = P["queue"]["vectors"][1]
    assert re.queue_move(vec["rows_before"]) == vec["rows_after"]


def test_post_deletes_everything_posted():
    vec = P["queue"]["vectors"][2]
    rows, posted = re.queue_post(vec["rows_before"])
    assert rows == vec["rows_after"] and posted == vec["posted"]


def test_clear_keeps_non_pending_rows():
    vec = P["queue"]["vectors"][3]
    assert re.queue_clear(vec["rows_before"]) == vec["rows_after"]


def test_retrieval_only_pending():
    vec = P["retrieval"]["vectors"][0]
    assert re.pending(vec["rows"]) == vec["visible"]


def test_answers_in_chapter():
    vec = P["answers_in_chapter"]["vectors"][0]
    assert re.answers_in_chapter(vec["rows"]) == vec["expected"]


def test_first_try_count():
    assert re.first_try_count(P["first_try_count"]["vectors"][0]["rows"]) == 1


def test_version_change_is_not_compared():
    vec = P["version_change"]["vectors"][0]
    row = vec["row_publishSetVersion"]
    assert vec["bundle_publishSetVersion"] != row
    assert vec["row_unchanged"] is True and vec["resent_value"] == row


def test_wire_mapping_has_nine_fields():
    fields = P["wire_mapping"]["dto_fields"]
    assert len(fields) == 9
    assert "inQueue" not in fields and "lessonId" in fields


@pytest.mark.parametrize("tries,expected", [([0, 0, 0], False), ([1, 1, 0], False), ([1, 1, 1], True)])
def test_local_completion_add04(tries, expected):
    assert re.local_completion(tries) is expected
