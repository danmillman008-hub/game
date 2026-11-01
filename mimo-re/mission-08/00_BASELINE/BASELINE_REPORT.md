# Mission 8 — Phase 0 Baseline Report

**Date:** 2026-11-01  
**Continues from:** `b95f56da1a16dd09167ae0ef7ec251dedd6b216e` (Mission-7 final commit, verified on the remote)  
**Branch:** `arena/ecb8af07-game`  
**Mode:** reconstruction only — no clone, no repackaging analysis, no runtime execution claimed.

---

## 1. What is actually on disk (measured, not remembered)

| Artefact | Path | Measured |
|---|---|---|
| authorised APK (user's modified 9.35 build) | `/tmp/apk/Mimo_9.35 (1).apk` | 142,353,499 bytes |
| dex set | `/tmp/x/*.dex` | **12 dex**, 687 MB unpacked |
| decompiled Java (DAD) | `/tmp/dad/**/*.java` | **3,284 files**, 17 MB |
| decoded resources | `/tmp/res` | 25 MB |
| full ARSC decode | `/tmp/arsc_full.json`, `/tmp/strings_by_id.json` | present |
| python env | `/tmp/venv` | androguard 4.1.4, pytest 9.2.0 |
| mission-04 | `mimo-re/complete-extraction/` | frozen |
| mission-05 | `mimo-re/mission-05/` | frozen |
| mission-06 | `mimo-re/mission-06/` | 191 files |
| mission-07 | `mimo-re/mission-07/` | **190 files / 7,192,046 bytes** |

Nothing in `mission-04…07` was opened for writing during Stage A. `WORKSPACE_INTEGRITY.json` pins per-file
sizes and `sha256[:16]` for every file in those trees, so a later accidental edit is detectable.

## 2. Class universe (from the Mission-7 registers, re-read not recomputed)

| Register | Rows |
|---|---|
| `01_CLASS_UNIVERSE/02_COMPLETE_CLASS_INVENTORY.csv` | **29,454** |
| `01_CLASS_UNIVERSE/03_METHOD_INVENTORY.csv` | **15,087** |
| `01_CLASS_UNIVERSE/04_DEEP_INVESTIGATION_QUEUE.csv` | **2,178** |

Cross-check performed in this stage (`tools/dex_inspect.py --queue-csv … --coverage`):

* all **2,178** queue classes exist in the dex set (0 missing) — the queue is not stale,
* **1,119** have a `.java` file, **1,059 (48.6 %)** do **not** — those are DEX-only and can only be
  investigated at instruction level.

## 3. Registers rebuilt from the artefacts

`tools/build_canonical_registers.py` regenerates every Mission-7 count instead of quoting the reports:

| Register | Result |
|---|---|
| `CANONICAL_OPEN_QUESTION_REGISTER.json` | **39** questions, one status each, 8-value vocabulary |
| status distribution | `CLOSED_STATIC 14`, `PARTIALLY_CLOSED 11`, `NOT_RECOVERED 7`, `GENUINELY_UNKNOWN 3`, `BACKEND_ONLY 2`, `BLOCKED_BY_ENVIRONMENT 2` (= 39) |
| `CANONICAL_DOMAIN_REGISTER.json` | **45** domains (40 inherited + 5 newly separated), one classification each |
| domain distribution | `FULLY_RECONSTRUCTED 24`, `SUBSTANTIALLY_RECONSTRUCTED 9`, `PARTIALLY_RECONSTRUCTED 7`, `NOT_INVESTIGATED 5` |
| evidence reference resolution | **39/39** Mission-7 evidence stems resolve to real files |
| `runtime_executed` for every domain | `NONE` — no execution evidence exists anywhere |

The Mission-7 report's `17/12/4/3/3/2 = 41` is **not reproducible**; see `HISTORICAL_COUNT_AUDIT.md` and
`HISTORICAL_FINDINGS_RECONCILIATION.md` (R-01 … R-04).

## 4. Regression suites (unchanged, re-run)

| Suite | Result |
|---|---|
| mission-4 `complete-extraction/16_AUTOMATED_TESTS` | 23 passed |
| mission-5 `mission-05/21_AUTOMATED_VALIDATION` | 44 passed |
| mission-6 `mission-06/19_TESTS` | 21 passed |
| mission-7 `mission-07/20_TESTS` | 15 passed |

Details, commands and caveats: `REGRESSION_TEST_RESULTS.md`.

## 5. Toolchain verdict

Absent: `java`, `jadx`, `apktool`, `aapt2`, `readelf`, `objdump`, `dot`, `mmdc`, `adb`, `emulator`.
Present and verified in this stage: `decompile_apk.py` (T-01), `dex_inspect.py` (T-08),
`build_canonical_registers.py` (T-09). Everything else is present-but-not-re-run (T-02…T-07), with its mission-7
outputs still on disk. Full inventory and failure profile: `EXISTING_TOOL_STATUS.json`.

The decompiler is the binding constraint: **DAD produces nothing for 48.6 % of the queue** and, in the cases
tested, produced nothing for exactly the classes that matter most for behaviour questions
(`ku.a` token provider, `ri.a` network callback, `AuthenticationFragment`). Mission-8 therefore treats
*"decompiled"* as one source and *"DEX instruction stream"* as another, and records which one each claim rests on.

## 6. What Stage A deliberately did not do

* did not re-run the Mission-4…7 extraction pipelines (their inputs exist, so this stays possible; re-running
  them now would spend the budget on reproducing known counts),
* did not repair anything inside Mission-7,
* did not upgrade any status to runtime-verified (there is no runtime),
* did not re-derive the 62-row endpoint catalogue (still flagged, see `T-06`).

## 7. Verification commands

```bash
cd mimo-re/mission-08
/tmp/venv/bin/python tools/build_canonical_registers.py            # rebuild all registers
/tmp/venv/bin/python tools/dex_inspect.py --dex-dir /tmp/x \
    --queue-csv ../mission-07/01_CLASS_UNIVERSE/04_DEEP_INVESTIGATION_QUEUE.csv \
    --src-dir /tmp/dad --coverage --out /tmp/cov.json               # 2178 / 1119 / 1059
```

## 8. Stage-A acceptance

| Criterion | State |
|---|---|
| workspace audit | done (`WORKSPACE_INTEGRITY.json`) |
| prior suites re-run without weakening | done (103 tests green) |
| findings/evidence/domains/questions reconciled | done (R-01…R-09) |
| every Mission-7 count recalculated from registers | done (`HISTORICAL_COUNT_AUDIT.md`) |
| one canonical ID register, one status per question | done (39 rows) |
| one classification per domain, 45 domains | done (45 rows) |
