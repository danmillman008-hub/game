"""Stage 7 semantic tests.

Two kinds of assertions:
  (a) re-derivation from committed evidence (DI_GRAPH case bodies, CSV catalogue, interceptor dumps),
  (b) cross-artifact consistency of the Stage-7 deliverables.

They do not assert that a file exists; they assert relations that the reconstruction claims.
"""
import csv, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
REPO = HERE.parent.parent                 # mimo-re/
M6 = REPO / "mission-06"
M8 = REPO / "mission-08"

DI = json.loads((M6 / "evidence/DI_GRAPH.json").read_text())
DI_CASES = {c["case"]: c["body"] for c in DI["providers"]}

CAT = json.loads((HERE / "02_ENDPOINT_CATALOG.json").read_text())
CLI = json.loads((HERE / "01_NETWORK_CLIENT_INVENTORY.json").read_text())
DIM = json.loads((HERE / "09_DI_DEPENDENCY_MAP.json").read_text())
REG = json.loads((HERE / "11_EVIDENCE_REGISTER.json").read_text())

CLIENTS = {c["id"]: c for c in CLI["clients"]}

# ---------------------------------------------------------------- (a) evidence

def test_case20_interceptor_order_is_recovered_in_the_add_sequence():
    body = DI_CASES[20]
    adds = re.findall(r"\.add\(new (\w+\.\w+|\w+)", body)
    assert adds == ["hg.e", "fh.b", "fh.a"], adds          # order, not just presence


def test_case20_timeouts_and_retry_flag():
    body = DI_CASES[20]
    assert re.search(r"_UtilJvmKt\.b\(20\)", body)
    assert re.search(r"_UtilJvmKt\.b\(30\)", body)
    assert re.search(r"\.f = 1", body)                    # retryOnConnectionFailure


def test_case108_has_no_connectivity_gate_and_longer_read():
    body = DI_CASES[108]
    assert "hg.e" not in body
    assert re.search(r"_UtilJvmKt\.b\(10\)", body) and re.search(r"_UtilJvmKt\.b\(120\)", body)
    assert "fh.a" in body and "fh.b" in body


def test_host_switch_is_a_devmenu_preference():
    body = DI_CASES[22]
    assert "sk.a" in body and ".r[2]" in body               # preference array index, not BuildConfig
    assert "https://api.mimo.org" in body and "https://api-testing.mimo.org" in body
    assert "BuildConfig" not in body


def test_shared_retrofit_uses_client_host_and_kotlinx_converter():
    body = DI_CASES[19]
    assert "ge0.p0" in body                    # Retrofit.Builder
    assert "he0.a.c(" in body                  # converter factory
    assert "this.a.v.get()" in body and "this.a.w.get()" in body


def test_dedicated_clients_pin_their_own_hosts():
    assert "https://track.customer.io" in DI_CASES[53]
    assert "https://mimoauth.getmimo.com/" in DI_CASES[87]
    assert "https://email.getmimo.com" in DI_CASES[117]


def test_auth_interceptor_is_annotation_conditional():
    d = json.loads((M8 / "05_AUTHENTICATION_CLOSURE/evidence/DEX_auth_interceptors_and_repository.json").read_text())
    calls = [c.get("target", "") for m in d["classes"]["fh.a"]["methods"]
             if m.get("name") == "intercept" for c in m.get("calls", [])]
    joined = " ".join(calls)
    assert "getAnnotation" in joined                       # per-method marker, not "every request"
    assert "Tags;->a(" in joined                           # reads the Retrofit Method tag
    assert "ku/a;->d(Z)Ljava/lang/String;" in joined       # token provider
    assert "getPath" not in joined and 'headers("Authorization")' not in joined


def test_offline_gate_throws_ioexception():
    d = json.loads((M8 / "05_AUTHENTICATION_CLOSURE/evidence/DEX_auth_interceptors_and_repository.json").read_text())
    calls = [c.get("target", "") for m in d["classes"]["hg.e"]["methods"]
             if m.get("name") == "intercept" for c in m.get("calls", [])]
    joined = " ".join(calls)
    assert "com/getmimo/network/a;->b()Z" in joined
    assert "java/io/IOException;-><init>" in joined


def test_continuation_is_not_a_result_envelope():
    omap = json.loads((M6 / "01_APK_AND_ARCHITECTURE/05_OBFUSCATION_MAP.json").read_text())
    entries = omap if isinstance(omap, list) else omap.get("entries", [])
    d70 = [e for e in entries if isinstance(e, dict) and e.get("obfuscated") == "d70.b"]
    assert d70 and "Continuation" in d70[0]["responsibility"]


# ---------------------------------------------------------------- catalogue

def test_catalogue_row_count_matches_source_csv():
    rows = list(csv.DictReader(open(REPO / "mission-05/evidence/API_CATALOG_V2.csv")))
    assert len(CAT["endpoints"]) == len(rows) == 62
    assert CAT["interface_count"] == 29


def test_every_row_keeps_source_provenance():
    for e in CAT["endpoints"]:
        assert e["dex"] in ("classes.dex", "classes2.dex")
        assert e["verb"] in {"GET", "POST", "PATCH", "PUT", "DELETE"}
        assert e["path"].startswith("/")


def test_medium_confidence_verbs_are_exactly_six():
    medium = [e for e in CAT["endpoints"] if e["verb_confidence"] == "INFERRED_MEDIUM"]
    assert len(medium) == 6


def test_client_distribution_sums_to_catalogue():
    assert sum(CAT["by_client"].values()) == 62
    assert CAT["by_client"]["shared_retrofit"] == 52
    assert CAT["by_client"]["third_party_sdk"] == 6


def test_only_five_hosts_appear_and_all_are_evidenced():
    hosts = {e["origin"] for e in CAT["endpoints"]}
    assert hosts == {"https://api.mimo.org", "https://track.customer.io",
                     "https://mimoauth.getmimo.com/", "https://email.getmimo.com", "sdk-managed"}


def test_every_endpoint_client_exists_in_inventory():
    for e in CAT["endpoints"]:
        assert e["client"] in {"shared_retrofit", "preview_long_timeout", "customerio",
                               "mimo_auth", "email_click", "third_party_sdk"}


def test_per_endpoint_auth_is_not_asserted():
    for e in CAT["endpoints"]:
        assert e["auth"]["per_endpoint"] == "NOT_CAPTURED_IN_COMMITTED_EVIDENCE"


# ---------------------------------------------------------------- clients / DI

def test_main_client_record_matches_evidence():
    c1 = CLIENTS["C1_authenticated_okhttp"]
    assert c1["di_case"] == 20
    assert [i["class"] for i in c1["interceptors"]] == ["hg.e", "fh.b", "fh.a"]
    assert c1["connect_timeout_s"] == 20 and c1["read_timeout_s"] == 30


def test_long_timeout_client_excludes_gate():
    c3 = CLIENTS["C3_long_timeout_client"]
    assert "hg.e" not in [i["class"] for i in c3["interceptors"]]
    assert (c3["connect_timeout_s"], c3["read_timeout_s"]) == (10, 120)


def test_di_tokens_are_the_ones_used_by_case_bodies():
    for token, desc in DIM["tokens"].items():
        if token.endswith("()"):
            continue
        assert f"this.a.{token}.get()" in " ".join(DI_CASES[c] for c in (19, 53, 81, 87, 108, 113, 117, 20))


def test_host_switch_documented_as_two_literals_only():
    hs = DIM["host_switch"]
    assert hs["production"] == "https://api.mimo.org"
    assert hs["testing"] == "https://api-testing.mimo.org"


def test_negative_findings_cover_the_dangerous_absences():
    joined = " ".join(CLI["negative_findings"]).lower()
    for needle in ("authenticator", "cache", "certificatepinner", "logging"):
        assert needle in joined


# ---------------------------------------------------------------- evidence register

REQUIRED_FIELDS = {"id", "mission", "phase", "domain", "claim", "status", "apk_sha256", "dex_sha256",
                   "dex", "class_method", "source_path", "dex_offset_or_instruction", "line",
                   "fields_annotations", "excerpt_fingerprint", "tool", "reproduction", "supporting_ids",
                   "confidence", "limitations", "open_questions", "evidence_path", "artifact_scope"}


def test_register_records_carry_the_required_fields():
    assert REG["record_count"] == len(REG["records"]) == 12
    for r in REG["records"]:
        assert REQUIRED_FIELDS <= set(r), REQUIRED_FIELDS - set(r)


def test_register_apk_hash_matches_baseline_manifest():
    manifest = json.loads((M6 / "00_BASELINE/APK_MANIFEST.json").read_text())
    for r in REG["records"]:
        assert r["apk_sha256"] == manifest["sha256"]


def test_no_credentials_or_token_values_in_artifacts():
    for p in HERE.glob("*.json"):
        txt = p.read_text()
        assert "eyJ" not in txt                              # JWT prefix
        assert not re.search(r"Bearer\s+[A-Za-z0-9._-]{20,}", txt)
    for p in HERE.glob("*.md"):
        txt = p.read_text()
        assert not re.search(r"Bearer\s+[A-Za-z0-9._-]{20,}", txt)


def test_no_server_behaviour_is_asserted_as_client_fact():
    for r in REG["records"]:
        low = r["claim"].lower()
        assert "server returns" not in low and "backend does" not in low


def test_statuses_are_from_the_evidence_model():
    allowed = {"VERIFIED_STATIC", "VERIFIED_RUNTIME", "VERIFIED_EXPERIMENTAL",
               "INFERRED", "UNKNOWN", "NOT_RECOVERED", "BLOCKED"}
    for r in REG["records"]:
        assert r["status"] in allowed
