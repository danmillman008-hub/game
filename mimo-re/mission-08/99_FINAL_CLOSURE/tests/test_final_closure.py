"""Terminal-closure validation.

These tests assert *relations* between the final dossier and the committed evidence it summarises:
coverage completeness, question-closure consistency, evidence-reference integrity, offline boundary,
and the zero-runtime-claim invariant. They do not test file existence for its own sake.
"""
import csv, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
M8 = HERE.parent
REPO = M8.parent
M6 = REPO / "mission-06"
M7 = REPO / "mission-07"
M5 = REPO / "mission-05"

FACTS = json.loads((HERE / "00_BASELINE_FACTS.json").read_text())
Q = json.loads((HERE / "14_ALL_OPEN_QUESTIONS_CLOSURE.json").read_text())
EV = json.loads((HERE / "16_CONSOLIDATED_EVIDENCE_REGISTER.json").read_text())
DOMAINS = json.loads((M8 / "00_BASELINE/CANONICAL_DOMAIN_REGISTER.json").read_text())["domains"]
COV = list(csv.DictReader((HERE / "15_FINAL_COVERAGE_MATRIX.csv").open()))
OFF = list(csv.DictReader((HERE / "08_OFFLINE_CAPABILITY_MATRIX.csv").open()))
RT = list(csv.DictReader((HERE / "13_RUNTIME_TEST_MATRIX.csv").open()))

STATUSES = {"CLOSED_STATIC", "VERIFIED_RUNTIME", "BACKEND_ONLY", "PARTIALLY_CLOSED",
            "NOT_RECOVERED", "GENUINELY_UNKNOWN", "BLOCKED_BY_ENVIRONMENT", "OUT_OF_SCOPE", "SUPERSEDED"}
DOMAIN_STATUSES = {"COMPLETE", "SUBSTANTIALLY_COMPLETE", "PARTIALLY_COMPLETE",
                   "BACKEND_ONLY", "BLOCKED_BY_ENVIRONMENT", "GENUINELY_UNKNOWN"}

DELIVERABLES = [f"{n}_{name}.md" for n, name in [
    ("00", "FINAL_EXECUTIVE_SUMMARY"), ("01", "TARGET_AND_REPOSITORY_BASELINE"),
    ("02", "COMPLETE_APPLICATION_ARCHITECTURE"), ("03", "CLASS_AND_METHOD_COVERAGE"),
    ("04", "CONTENT_AND_TRACK_DELIVERY"), ("05", "LESSON_ENGINE_AND_RENDERING"),
    ("06", "INTERACTION_AND_GRADING"), ("07", "LEARNER_MODEL_AND_COMPLETION"),
    ("08", "DATABASE_AND_OFFLINE_ARCHITECTURE"), ("09", "AUTHENTICATION_LIFECYCLE"),
    ("10", "NETWORK_CLIENTS_AND_ENDPOINT_CATALOG"), ("11", "AI_TUTOR_SSE_AND_CODE_EXECUTION"),
    ("12", "ANALYTICS_SETTINGS_AND_ENTITLEMENTS"), ("13", "RUNTIME_VALIDATION"),
    ("14", "ALL_OPEN_QUESTIONS_CLOSURE"), ("15", "FINAL_COVERAGE_MATRIX"),
    ("16", "CONSOLIDATED_EVIDENCE_REGISTER"), ("17", "BACKEND_AND_ENVIRONMENT_LIMITATIONS"),
    ("18", "REPRODUCTION_AND_TOOLCHAIN"), ("19", "FINAL_ARCHITECTURE_DIAGRAMS"),
    ("20", "FINAL_CORRECTIONS_AND_HISTORICAL_RECONCILIATION")]]


# ---------------------------------------------------------------- baseline / artifact identity

def test_apk_hash_matches_the_baseline_manifest():
    manifest = json.loads((M6 / "00_BASELINE/APK_MANIFEST.json").read_text())
    assert FACTS["artifact"]["apk_sha256"] == manifest["sha256"]


def test_artifact_is_declared_absent_and_no_runtime_claim_is_made():
    assert FACTS["artifact"]["present_in_environment"] is False
    assert FACTS["runtime"]["verified_runtime_claims"] == 0
    assert FACTS["runtime"]["runtime_tests_executed"] == 0


# ---------------------------------------------------------------- coverage

def test_coverage_covers_all_45_domains_and_none_else():
    assert len(DOMAINS) == 45
    assert {d["id"] for d in DOMAINS} == {r["domain_id"] for r in COV}
    names = {d["id"]: d["domain"] for d in DOMAINS}
    for r in COV:
        assert r["domain"] == names[r["domain_id"]], r


def test_every_domain_status_is_terminal_and_justified():
    for r in COV:
        assert r["terminal_status"] in DOMAIN_STATUSES, r
        assert r["evidence_anchor"].strip(), r
        assert r["note"].strip(), r


def test_product_critical_domains_are_at_least_substantially_complete():
    rank = {"COMPLETE": 3, "SUBSTANTIALLY_COMPLETE": 2, "PARTIALLY_COMPLETE": 1}
    critical = ["D-03", "D-05", "D-09", "D-10", "D-11", "D-14", "D-17", "D-18", "D-19", "D-20", "D-43"]
    by = {r["domain_id"]: r["terminal_status"] for r in COV}
    for d in critical:
        assert rank.get(by[d], 0) >= 2, (d, by[d])


# ---------------------------------------------------------------- questions

def test_question_families_are_all_present():
    assert Q["count"] == len(Q["questions"]) == 91
    fam = {}
    for q in Q["questions"]:
        fam[q["family"]] = fam.get(q["family"], 0) + 1
    assert fam == {"canonical": 39, "mission8-A": 10, "Stage2": 4, "Stage3": 6,
                   "Stage4": 8, "B": 13, "stage7": 10, "out-of-register": 1}, fam


def test_every_canonical_question_is_present_verbatim():
    reg = json.loads((M8 / "00_BASELINE/CANONICAL_OPEN_QUESTION_REGISTER.json").read_text())["questions"]
    mine = {q["id"]: q["question"] for q in Q["questions"]}
    for r in reg:
        assert r["id"] in mine, r["id"]
        assert mine[r["id"]].strip() == r["question"].strip(), r["id"]


def test_question_statuses_are_valid_and_distributed_as_declared():
    for q in Q["questions"]:
        assert q["final_status"] in STATUSES, q
        assert q["final_answer"].strip(), q["id"]
    dist = {}
    for q in Q["questions"]:
        dist[q["final_status"]] = dist.get(q["final_status"], 0) + 1
    assert dist == Q["status_distribution"], (dist, Q["status_distribution"])


def test_no_question_is_closed_without_evidence_except_negatives_backend_and_out_of_scope():
    exempt = {"CLOSED_STATIC", "BACKEND_ONLY", "OUT_OF_SCOPE"}
    for q in Q["questions"]:
        if q["final_status"] in ("PARTIALLY_CLOSED", "NOT_RECOVERED",
                                 "GENUINELY_UNKNOWN", "BLOCKED_BY_ENVIRONMENT"):
            assert q["what_would_close_it"] or q["evidence"] or q["final_status"] == "NOT_RECOVERED", q["id"]
        if q["final_status"] == "CLOSED_STATIC" and q["id"] not in exempt:
            assert q["evidence"].strip(), q["id"]


def test_blocked_questions_are_exactly_the_artifact_dependent_ones():
    blocked = {q["id"] for q in Q["questions"] if q["final_status"] == "BLOCKED_BY_ENVIRONMENT"}
    assert blocked == {"Q-05", "Q-40", "A7", "A-01", "B-1", "B-9", "B-11", "B-12"}, blocked


# ---------------------------------------------------------------- evidence register

def test_evidence_register_shape():
    assert EV["count"] == len(EV["records"]) == 23
    fields = set(EV["schema_fields"])
    assert len(fields) == 16
    for r in EV["records"]:
        assert fields <= set(r), set(r) ^ fields
        assert r["apk_sha256"] == FACTS["artifact"]["apk_sha256"]


def test_evidence_refs_resolve_to_real_files():
    missing = []
    for r in EV["records"]:
        ref = r["artifact_ref"]
        cand = [REPO / ref, M8 / ref.replace("mission-08/", "")]
        if not any(p.exists() for p in cand):
            missing.append(ref)
    assert not missing, missing


# ---------------------------------------------------------------- offline boundary

def test_offline_matrix_expresses_a_real_boundary():
    yes = [r for r in OFF if r["offline_interaction"] == "yes"]
    no = [r for r in OFF if r["offline_interaction"] == "no"]
    assert len(OFF) == 18
    assert len(yes) >= 8 and len(no) >= 4
    # the boundary must be drawn at progression, not at content
    by = {r["feature"]: r for r in OFF}
    assert by["open a lesson"]["offline_interaction"] == "yes"
    assert by["see completion / next chapter unlocked"]["offline_interaction"] == "no"
    assert "completion" in by["see completion / next chapter unlocked"]["reconnection_dependency"].lower()


def test_progress_upload_is_deferred_not_offline_impossible():
    row = next(r for r in OFF if r["feature"] == "progress upload")
    assert row["offline_interaction"] == "deferred"
    assert "outbox" in row["offline_persistence"].lower()


# ---------------------------------------------------------------- runtime matrix

def test_runtime_matrix_is_honest():
    assert len(RT) == 16
    for r in RT:
        assert r["result"] == "NOT EXECUTED", r
        assert r["reason"].strip(), r


# ---------------------------------------------------------------- cross-artifact consistency

def test_network_numbers_match_stage7_artifacts():
    cat = json.loads((M8 / "07_NETWORKING/02_ENDPOINT_CATALOG.json").read_text())
    cli = json.loads((M8 / "07_NETWORKING/01_NETWORK_CLIENT_INVENTORY.json").read_text())
    assert FACTS["networking"]["endpoints"] == cat["endpoint_count"] == 62
    assert FACTS["networking"]["interfaces"] == cat["interface_count"] == 29
    c1 = next(c for c in cli["clients"] if c["id"] == "C1_authenticated_okhttp")
    assert FACTS["networking"]["interceptor_order"] == [i["class"] for i in c1["interceptors"]]


def test_content_numbers_match_stage2_and_mission6():
    facts = FACTS["content"]
    assert (facts["tracks"], facts["tutorials"], facts["chapters"], facts["lessons"]) == (19, 1029, 1947, 18272)
    assert facts["publish_set_version"] == 753
    fields = json.loads((M6 / "evidence/CONTENT_MODEL_FIELDS.json").read_text())
    assert "publishSetVersion" in {f["name"] for f in fields["com.getmimo.data.content.model.track.TracksJson"]["fields"]}


def test_persistence_numbers_match_stage6():
    schema = json.loads((M8 / "06_PERSISTENCE/ROOM_SCHEMA.json").read_text())
    assert FACTS["persistence"]["database"] == schema["database"] == "mimo.db"
    assert FACTS["persistence"]["schema_version"] == schema["version"] == 2
    assert FACTS["persistence"]["identity_hash"] == schema["identity_hash"]
    assert FACTS["persistence"]["tables"] == [t["name"] for t in schema["tables"]]


def test_inventory_counts_match_the_mission_metrics():
    m = json.loads((M8 / "16_FINAL_AUDIT/03_MISSION08_METRICS.json").read_text())
    inv = FACTS["inventory"]
    for k_src, k_dst in [("class_defs", "class_defs"), ("edges", "edges"), ("call_sites", "call_sites"),
                         ("orphan_lambdas", "orphan_lambdas"), ("renamed_app", "renamed_app"),
                         ("decompiled_java", "decompiled_java"), ("invalid_java", "invalid_java")]:
        assert inv[k_dst] == m[k_src], k_dst


# ---------------------------------------------------------------- corrections & documents

def test_all_corrections_are_registered():
    reg = (M8 / "00_BASELINE/HISTORICAL_FINDINGS_RECONCILIATION.md").read_text()
    for cid in ["C-14", "C-15", "C-16", "C-17", "C-18", "C-19", "C-20"]:
        assert cid in reg, cid
    doc = (HERE / "20_FINAL_CORRECTIONS_AND_HISTORICAL_RECONCILIATION.md").read_text()
    for cid in ["C-21", "C-22", "C-23", "C-24"]:
        assert cid in doc, cid


def test_every_deliverable_exists_and_cites_committed_evidence():
    for name in DELIVERABLES:
        p = HERE / name
        assert p.exists(), name
        text = p.read_text()
        assert re.search(r"(mission-0[4-8]/|Stage[ -]?[0-9A-Z]|[0-9]{2}_[A-Z][A-Z0-9_]+)", text), name


def test_no_secrets_or_credentials_in_the_package():
    pat = re.compile(r"(eyJ[A-Za-z0-9_-]{10,}|Bearer\s+[A-Za-z0-9._-]{20,}|DAHL_API_KEY|sk-[A-Za-z0-9]{20,})")
    for p in list(HERE.glob("*.md")) + list(HERE.glob("*.json")) + list(HERE.glob("*.csv")):
        assert not pat.search(p.read_text()), p.name
