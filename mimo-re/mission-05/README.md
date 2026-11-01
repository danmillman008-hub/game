# Mimo — Mission 5 (reverse engineering, phase 5)

Specification-only reverse engineering of `com.getmimo` **9.35** (versionCode 1792759685), built on the
frozen mission-04 extraction. No clone, no app, no binary mutation, no proprietary content reproduced.

**Start reading here:** [`MISSION_05_REPORT.md`](MISSION_05_REPORT.md) →
[`22_FINAL_AUDIT/FINAL_AUDIT.md`](22_FINAL_AUDIT/FINAL_AUDIT.md) → [`report.html`](report.html)

## What changed in this phase
| # | Discovery | Where |
|---|---|---|
| 1 | The lesson parser is obfuscated `te.a`–`te.g`, **outside** `com.getmimo` — the `lessonparser` package holds only models | `04_CONTENT_AND_DSL/DSL_GRAMMAR.md` |
| 2 | The DSL is HTML-shaped with **29 tags** (`Tag` ordinals 0–28) | `04_CONTENT_AND_DSL/`, `evidence/TAG_ENUM.json` |
| 3 | Validated-input grading normalises (lowercase; keep letters/digits/`<`/`.`) and has a **partial-match** outcome applied after a **300 ms** delay | `06_ASSESSMENT_AND_EVALUATION/ASSESSMENT_SPEC.md` |
| 4 | `tries` is a **0/1 correctness flag**, not a counter (`isSolvedCorrectly() { tries >= 1 }`) | `09_PROGRESS_AND_GAMIFICATION/PROGRESS_MODEL.md` |
| 5 | The local DB is a **transmit buffer**: 3 tables, no migrations, rows deleted after server ack | `11_LOCAL_DATA_AND_SYNC/DB_SCHEMA_AND_DATAFLOW.md` |
| 6 | **62 endpoints** with verbs, bodies, bindings and **34 response DTOs** recovered | `10_NETWORK_AND_API/` |
| 7 | Native payload identified; `libyrf.so` drives an obfuscated `bin.ghost` blocking dialog | `16_NATIVE_AND_EXECUTION/NATIVE_REPORT.md` |

## Layout
| Directory | Content |
|---|---|
| `00_BASELINE_AUDIT/`, `01_TOOLCHAIN_AND_ENVIRONMENT/`, `02_ANDROID_STATIC_ANALYSIS/` | start state, toolchain, decompilation coverage |
| `03_APPLICATION_ARCHITECTURE/`, `18_SYSTEM_GRAPH/` | architecture status, unified graph (JSON + Mermaid + DOT) |
| `04_CONTENT_AND_DSL/` | grammar, AST/JSON Schema |
| `05_LESSON_RUNTIME/`, `06_ASSESSMENT_AND_EVALUATION/` | runtime state machine, grading algorithms |
| `07_LEARNER_MODEL_AND_PEDAGOGY/`, `09_PROGRESS_AND_GAMIFICATION/` | pedagogy status, progress model |
| `08_UI_AND_INTERACTION/`, `12_AI_TUTOR/`, `13_AUTH_AND_SUBSCRIPTIONS/`, `14_REMOTE_CONFIG/`, `15_ANALYTICS/`, `16_NATIVE_AND_EXECUTION/`, `17_RUNTIME_VALIDATION/`, `20_VERSION_AND_LOCALE_DIFFS/` | per-domain reports and explicit status records |
| `10_NETWORK_AND_API/`, `11_LOCAL_DATA_AND_SYNC/` | API + DTO catalogues, schema and data flow |
| `19_INDEPENDENT_SPECIFICATIONS/` | E1 (content), E2 (runtime+assessment), E5 (progress+sync) |
| `21_AUTOMATED_VALIDATION/` | 29 artifact tests + results |
| `22_FINAL_AUDIT/` | two-dimension completion audit |
| `evidence/` | all machine-readable data (CSV/JSON) with dex hashes and manifests |
| `tools/` | four deterministic CLI tools |
| `MISSION_05_REPORT_FA.md` | Persian summary (خلاصه فارسی) |

## Reproduce
```bash
python3 -m venv /tmp/venv && /tmp/venv/bin/pip install androguard==4.1.4 pytest
# APK → /tmp/x (classes*.dex + assets) must exist first; decompiled output stays outside the repo
/tmp/venv/bin/python tools/decompile_apk.py --dex-dir /tmp/x --out /tmp/dad \
  --filter 'Lcom/getmimo' --inventory evidence/CLASS_INVENTORY_APP.csv \
  --manifest evidence/DECOMPILE_MANIFEST_APP.json
/tmp/venv/bin/python tools/extract_annotations_v2.py --dex-dir /tmp/x \
  --csv evidence/ANNOTATIONS_V2.csv.gz.gz --json evidence/ANNOTATIONS_V2.json
/tmp/venv/bin/python tools/build_api_catalog_v2.py --annotations evidence/ANNOTATIONS_V2.csv \
  --csv evidence/API_CATALOG_V2.csv --json evidence/API_CATALOG_V2.json
/tmp/venv/bin/python tools/build_dto_catalog.py
python -m pytest 21_AUTOMATED_VALIDATION -q
```

## Evidence discipline
Nine-label set (`VERIFIED_STATIC`, `VERIFIED_RUNTIME`, `VERIFIED_EXPERIMENTAL`, `INFERRED_HIGH`,
`INFERRED_MEDIUM`, `INFERRED_LOW`, `UNKNOWN`, `BLOCKED`, `NOT_APPLICABLE`). **No claim in this mission is
runtime-verified** — the environment has no device, emulator or adb. 26 open items are tracked in
`evidence/UNRESOLVED_REGISTER.csv`, each with what would close it.
