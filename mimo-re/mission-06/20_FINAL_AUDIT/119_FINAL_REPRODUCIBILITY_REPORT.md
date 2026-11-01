# Mission 6 — Final Reproducibility Report

## Verdict
**Reproducible from this repository for every `VERIFIED_STATIC` claim, given the same APK.** Two
non-reproducible classes remain: (a) anything requiring the APK itself (not committed, RULE 5) and (b)
anything requiring the decompiled tree (derived metadata only is committed).

## Determinism
- Every extractor writes sorted, indented JSON/CSV; re-running on the same inputs yields identical files
  (verified by re-running `extract_class_fields.py` and `extract_parser_grammar.py` in this session).
- The test suite (21 tests) is deterministic and offline.

## Reproduction sequence (from a clean checkout + the APK)
```bash
# 0 tools
python3 -m venv /tmp/venv && /tmp/venv/bin/pip install androguard==4.1.4 pytest==9.2.0
APK="/tmp/apk/Mimo_9.35 (1).apk"

# 1 verify identity (must match)
sha256sum "$APK"    # 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
md5sum    "$APK"    # f9cef2d8029e59da3668ec1c18e21566

# 2 baseline + resources + inventory
cd mimo-re/mission-06
/tmp/venv/bin/python tools/build_baseline.py       --apk "$APK" --out 00_BASELINE
/tmp/venv/bin/python tools/extract_resources.py    --apk "$APK" --out evidence/RESOURCES.json
/tmp/venv/bin/python tools/build_class_inventory.py --apk "$APK" --out 01_APK_AND_ARCHITECTURE/06_CLASS_METHOD_INVENTORY.csv

# 3 decompile the classes the mission needs (host runs, SDK 34+)
/tmp/venv/bin/python ../mission-05/tools/decompile_apk.py --apk "$APK" \
   --classes-file /tmp/wanted_m6.txt --out /tmp/dad

# 4 grammar + DI + fields + events
/tmp/venv/bin/python tools/extract_parser_grammar.py --src /tmp/dad --json evidence/PARSER_GRAMMAR.json
/tmp/venv/bin/python tools/extract_di_graph.py       --src /tmp/dad --out  evidence/DI_GRAPH.json
/tmp/venv/bin/python tools/extract_class_fields.py   --from-csv ../mission-05/evidence/DTO_CATALOG.csv --out evidence/DTO_FIELDS.json
/tmp/venv/bin/python tools/extract_event_candidates.py --out evidence/EVENT_CANDIDATES.csv

# 5 validate
/tmp/venv/bin/python -m pytest 19_TESTS -q                       # 21 passed
/tmp/venv/bin/python -m pytest ../complete-extraction -q         # 23 passed (mission 4, untouched)
/tmp/venv/bin/python -m pytest ../mission-05/21_AUTOMATED_VALIDATION -q  # 44 passed (mission 5, untouched)
```

## Verified in this session
- `19_TESTS` → **21 passed**
- mission-04 suite → **23 passed**
- mission-05 suite → **44 passed**
- All `evidence/*.json` referenced by documents exist (test `test_evidence_files_referenced_by_docs_exist`).

## Known non-determinism / caveats
1. DAD output is decompiler-version dependent; the committed *derived* JSON is the stable artefact.
2. `/tmp` artefacts (decompiled tree, extracted `res/`, ARSC strings) are not persisted and must be
   recreated by steps 3–4.
3. ARSC type-table extraction is tooling-blocked (`Q-102`); repeating it will fail identically until a
   JVM-grade resource dump is available.

## Commit discipline applied
Both prior mission suites executed before commit; JSON validity checked; no APK, no decompiled sources, no
lesson content, no secrets committed (RULE 5); nothing outside `mimo-re/mission-06/` modified.
