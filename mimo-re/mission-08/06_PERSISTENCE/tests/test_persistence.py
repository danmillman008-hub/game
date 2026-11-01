"""Schema/persistence invariants pinned to ROOM_SCHEMA.json and the recovered statements."""
import json, csv, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
S = json.loads((ROOT / "ROOM_SCHEMA.json").read_text())
K = json.loads((ROOT / "STORAGE_KEYS_SCHEMA.json").read_text())
V = json.loads((ROOT / "PERSISTENCE_TEST_VECTORS.json").read_text())
DAOMAP = list(csv.DictReader((ROOT / "ROOM_DAO_MAP.csv").open()))

TABLES = {t["name"]: t for t in S["tables"]}


def test_database_identity():
    assert S["database"] == "mimo.db"
    assert S["version"] == 2
    assert S["identity_hash"] == "2b8ab6d303d9a501bd8c8fb78d8352fc"


def test_exactly_three_tables():
    assert sorted(TABLES) == sorted(V["vectors"][0]["expect"])
    assert len(TABLES) == next(v for v in V["vectors"] if v["id"] == "V9")["expect"]


def test_primary_keys():
    assert TABLES["lesson_progress"]["pk"] == ["lesson_id", "tutorial_id"]
    assert TABLES["tutorial_completions"]["pk"] == ["tutorial_id", "track_id"]
    assert TABLES["chapter_completions"]["pk"] == ["chapter_id", "track_id"]


def test_lesson_progress_columns_complete():
    cols = TABLES["lesson_progress"]["columns"]
    assert len(cols) == 11
    for c in ["lesson_id", "tutorial_id", "tries", "attempts", "in_queue", "publish_set_version"]:
        assert c in cols


def test_outbox_delete_only_after_post():
    deletes = [r for r in DAOMAP if r["operation"].startswith("delete")]
    assert len(deletes) == 2
    assert all(r["table"] == "lesson_progress" for r in deletes)          # completion tables never deleted
    assert any("lesson_id IN" in r["sql"] for r in deletes)


def test_no_delete_statements_for_completion_tables():
    for r in DAOMAP:
        if r["table"] in ("tutorial_completions", "chapter_completions"):
            assert not r["operation"].startswith("delete"), r


def test_lookup_keys():
    track_filters = [r for r in DAOMAP if "WHERE track_id = ?" in r["sql"]]
    assert len(track_filters) == 2                                        # both completion tables
    assert sum(1 for r in DAOMAP if "lesson_id = ?" in r["sql"]) == 1


def test_no_migrations():
    vec = next(v for v in V["vectors"] if v["id"] == "V3")
    assert vec["expect"]["migration_subclasses"] == 0
    assert vec["expect"]["builder_migrations_list"] == "empty"


def test_owned_preference_files_are_app_named():
    files = {p["file"] for p in K["shared_preferences"]}
    assert files == {"mimo_prefs", "mimo_prefs_global", "mimo_dev_prefs"}
    assert all("firebase" not in f.lower() and "facebook" not in f.lower() for f in files)


def test_interacted_pointer_key_prefix():
    key = K["preference_keys"][0]
    assert key["key"] == "last_interacted_tutorial_id_<trackId>"
    assert key["type"] == "long"


def test_each_layer_has_single_writer():
    g = json.loads((ROOT / "PERSISTENCE_GRAPH.json").read_text())
    for layer in g["layers"]:
        assert isinstance(layer["writer"], str) and layer["writer"]
    assert len(g["edges"]) == 5
