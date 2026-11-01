"""Reference models for the Mission-8 learner model.

Re-implements the *recovered* behaviour (counter updates, completion flag, queue transitions, DTO mapping)
and asserts PROGRESS_TEST_VECTORS.json. A pass proves the reconstruction is internally consistent with the
evidence; it is not evidence of runtime behaviour.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
V = json.loads((ROOT / "PROGRESS_TEST_VECTORS.json").read_text())
PUBLISH_SET_VERSION = 753


def build_progress(*, tries, attempts, started="T0", now="T1", publish_set_version=PUBLISH_SET_VERSION):
    return {"inQueue": True, "tries": tries, "attempts": attempts,
            "publishSetVersion": publish_set_version, "startedAt": started, "completedAt": now}


def ordering_anomaly(started, now):
    return now < started          # comparable strings in the vectors


def apply_verdict(verdict, c_before, d_before):
    d = d_before + 1
    if verdict == "CORRECT":
        return (0 if c_before is True else 1), d, False          # V
    if verdict == "PARTIAL":
        return (0 if c_before is True else 1), d, False          # W (same shape)
    if verdict == "INCORRECT":
        return 0, d, True                                        # X
    if verdict == "PROCEED":
        return (1 if c_before is True else 0), d, c_before       # U
    raise ValueError(verdict)


def solved(tries):
    return tries >= 1


def queue_apply(op, rows):
    """Rows are dicts with id + in_queue. Returns (rows_after, posted_ids)."""
    rows = [dict(r) for r in rows]
    if op == "store":
        return rows + [{"id": max([r["id"] for r in rows], default=0) + 1, "in_queue": 1}], []
    if op == "move":
        for r in rows:
            if r["in_queue"] == 1:
                r["in_queue"] = 0
        return rows, []
    if op == "post":
        posted = [r["id"] for r in rows]
        return [], posted
    if op == "clear":
        return [r for r in rows if r["in_queue"] != 1], []
    raise ValueError(op)


def in_queue(rows):
    return [r["id"] for r in rows if r["in_queue"] == 1]


def answers_in_chapter(rows):
    return {"answeredCorrectly": sum(1 for r in rows if solved(r["tries"])), "answeredTotal": len(rows)}


def first_try_count(rows):
    return sum(1 for r in rows if solved(r["tries"]) and r["attempts"] == 1)


def test_identity_is_two_part():
    for vec in V["identity"]["vectors"]:
        ident, key = vec["identifier"], vec["row_key"]
        assert key == {"lessonId": ident["lessonId"], "tutorialId": ident["tutorialId"]}
        assert vec["chapter_stored"] is False           # chapterId is not persisted
    assert V["identity"]["progress_pk"] == ["lesson_id", "tutorial_id"]


def test_two_chapters_share_one_row():
    a = {"trackId": 12, "tutorialId": 1001, "chapterId": 77, "lessonId": 9001}
    b = dict(a, chapterId=78)
    key = lambda i: (i["lessonId"], i["tutorialId"])
    assert key(a) == key(b)


def test_new_progress_vectors():
    for vec in V["new_progress"]["vectors"]:
        p = build_progress(tries=vec["tries"], attempts=vec["attempts"], started=vec["startedAt"], now=vec["now"])
        assert p["inQueue"] is True
        assert p["publishSetVersion"] == vec["expected"]["publishSetVersion"]


def test_ordering_guard_does_not_block_write():
    for vec in V["ordering_guard"]["vectors"]:
        assert ordering_anomaly(vec["startedAt"], vec["now"]) is True
        assert vec["entity_built"] is True


def test_counter_vectors():
    for vec in V["counter_update"]["vectors"]:
        tries, attempts, c_after = apply_verdict(vec["verdict"], vec["C_before"], vec["d_before"])
        assert tries == vec["expected"]["tries"], vec
        assert attempts == vec["expected"]["attempts"], vec
        if "C_after" in vec["expected"]:
            assert c_after == vec["expected"]["C_after"], vec


def test_tries_is_a_flag_not_a_counter():
    tries, attempts, _ = apply_verdict("CORRECT", False, 0)
    assert (tries, attempts) == (1, 1)
    tries2, attempts2, _ = apply_verdict("CORRECT", False, 1)   # re-answering in same session
    assert (tries2, attempts2) == (1, 2)                        # tries stays 1, attempts grows
    assert tries2 <= 1


def test_completion_flag_vectors():
    for vec in V["completion_flag"]["vectors"]:
        assert solved(vec["tries"]) is vec["solved"]


def test_queue_vectors():
    for vec in V["queue"]["vectors"]:
        rows_after, posted = queue_apply(vec["op"], vec["rows_before"])
        if vec["op"] == "post":
            assert rows_after == vec["rows_after"]
            assert posted == vec["posted"]
        else:
            assert rows_after == vec["rows_after"], vec


def test_queue_store_then_move_then_post():
    rows, _ = queue_apply("store", [])
    assert in_queue(rows) == [1]
    rows, _ = queue_apply("move", rows)
    assert in_queue(rows) == []
    assert rows[0]["in_queue"] == 0
    rows_after, posted = queue_apply("post", rows)
    assert rows_after == [] and posted == [1]


def test_clear_only_removes_pending():
    for vec in V["queue"]["vectors"]:
        if vec["op"] != "clear":
            continue
        rows_after, _ = queue_apply("clear", vec["rows_before"])
        assert [r["id"] for r in rows_after] == [4]


def test_retrieval_vectors():
    for vec in V["retrieval"]["vectors"]:
        assert in_queue(vec["rows"]) == vec["visible"]


def test_answers_in_chapter_vectors():
    for vec in V["answers_in_chapter"]["vectors"]:
        assert answers_in_chapter(vec["rows"]) == vec["expected"]


def test_first_try_vectors():
    for vec in V["first_try_count"]["vectors"]:
        assert first_try_count(vec["rows"]) == vec["expected"]


def test_version_change_does_not_invalidate():
    for vec in V["version_change"]["vectors"]:
        stored = vec["row_publishSetVersion"]
        current = vec["bundle_publishSetVersion"]
        assert stored != current
        assert vec["row_unchanged"] is True
        assert vec["resent_value"] == stored


def test_wire_mapping_covers_all_fields():
    dto = set(V["wire_mapping"]["dto_fields"])
    assert dto == {"lessonId", "completedAt", "startedAt", "tries", "tutorialVersion",
                   "trackId", "publishSetVersion", "attempts", "isPracticeProgress"}
    entity_fields = {f["name"] for f in json.loads((ROOT / "LESSON_PROGRESS_FIELD_MAP.json").read_text())["fields"]}
    assert {"lessonId", "tutorialId", "tries", "attempts", "inQueue"} <= entity_fields
    assert "tutorialId" not in dto          # grouping key, not a body field


def test_deliverables_exist():
    required = ["LESSON_PROGRESS_COMPLETE.md", "LESSON_PROGRESS_FIELD_MAP.json",
                "PROGRESS_REPOSITORY_IMPLEMENTATION.md", "PROGRESS_REPOSITORY_CALL_GRAPH.json",
                "COMPLETION_REPOSITORY_IMPLEMENTATION.md", "COMPLETION_STATE_MACHINE.json",
                "PROGRESS_KEY_AND_VERSIONING.md", "INQUEUE_IMPLEMENTATION.md",
                "LEARNER_FIELD_ACCESS_GRAPH.json", "PROGRESSION_IMPLEMENTATION.md",
                "PROGRESS_TEST_VECTORS.json", "LEARNER_MODEL_OPEN_QUESTIONS.md"]
    missing = [f for f in required if not (ROOT / f).exists()]
    assert not missing, missing
