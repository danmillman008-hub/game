# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged) · `SERVER CONFIRMED = 0` · classification on every finding.

---

## Coverage matrix
`VERIFIED_STATIC` = DEX/bytecode or shipped asset read directly;
`VERIFIED_RUNTIME` = M04/M05 emulator observation; `VERIFIED_BOTH` = both;
`INFERRED` = named interpretation of verified bytecode; `UNKNOWN` = explicitly unresolved.
`SERVER CONFIRMED = 0`.

| # | Component | Status | Primary evidence | Residual |
|---|---|---|---|---|
| 1 | Launcher / process | `VERIFIED_BOTH` | M04 `41998643355`, M01 component graph | — |
| 2 | DI container graph | `VERIFIED_STATIC` | `Lhm/b;`, 32-arg `q.<init>`, method catalog | framework `UNKNOWN` |
| 3 | Asset loaders & locales | `VERIFIED_STATIC` | `Lye/b`, `ContentLocale`, M05 stats | `Lye/d` selection `UNKNOWN` |
| 4 | JSON deserialization | `VERIFIED_STATIC` | `tracks/b.c`, `Lhb0/b.b`, `$$serializer` classes | full DTO list `INFERRED` |
| 5 | Content models / schema | `VERIFIED_BOTH` | M05 `CONTENT_SCHEMA.json`, M06 `CLASS_CATALOG_MIMO.json` | hard-mode predicate `INFERRED` |
| 6 | DSL parser | `VERIFIED_STATIC` | `Lte/c.b`, six `Lte/*` parsers | `Lte/a.a` internals `UNKNOWN` |
| 7 | Module visibility & feedback | `VERIFIED_BOTH` | `ModuleVisibility`, `base/c.c0/d0`, M05 run-004 | `d0` booleans `UNKNOWN` |
| 8 | Renderer selection | `VERIFIED_STATIC` | `Lgm/h.a`, `InteractiveLessonViewModel.E` | 3 dispatch predicates `UNKNOWN` |
| 9 | Render-item mapping | `VERIFIED_STATIC` | `base/c.O` @10949840 | adapter internals `UNKNOWN` |
| 10 | fillTheGap validation | `VERIFIED_STATIC` | `Lim/d.E0` @12834200 | — |
| 11 | selection validation | `VERIFIED_STATIC` | `Lkm/f.b` @13243392 | choice dispatch `UNKNOWN` |
| 12 | spell validation | `VERIFIED_STATIC` | `Lpm/b.E0` | — |
| 13 | validatedInput validation | `VERIFIED_STATIC` | `Lqm/i.a` @14172860, `setupViews$2` @10985684 | `e/f` fields `UNKNOWN` |
| 14 | WebView activity messages | `VERIFIED_BOTH` | `WebViewActivityResult`, `lesson-webview.js`, M05 counts | payload mapping `INFERRED` |
| 15 | executableFiles correctness | `VERIFIED_STATIC` | `q.I` @10912932 | applicability `UNKNOWN` |
| 16 | no-interaction / reveal | `VERIFIED_STATIC` | `NonInteractiveLessonFragment`, `U()` | — |
| 17 | Run dispatcher / state machine | `VERIFIED_STATIC` | `Y`, `onLessonRun$1`, `onValidatedInputExecuted$1` | `W()` `UNKNOWN` |
| 18 | `createLessonProgress` record | `VERIFIED_STATIC` | @10063916 + Room SQL | param names `INFERRED` |
| 19 | Room queue & answer counting | `VERIFIED_STATIC` | `LessonProgressQueue` @10056956/10058920 | force-stop `UNKNOWN` |
| 20 | Offline gate | `VERIFIED_BOTH` | `NetworkUtils.a` @10174360, M05 cold start | UI propagation `UNKNOWN` |
| 21 | Chapter-end online/offline | `VERIFIED_BOTH` | `handleOfflineState$1`, M05 path screens | reward thresholds `UNKNOWN` |
| 22 | Path-map states | `VERIFIED_STATIC` | `GetPathMapState$invoke$3` @10129608 | **exact unlock rule `UNKNOWN`** |
| 23 | Keys gate | `VERIFIED_STATIC` | `CanOpenChapterWithKeys$invoke$1` @10104004 | true branch `UNKNOWN` |
| 24 | Completion attachment | `VERIFIED_STATIC` | `CompletionRepository.b` @9981172 | SQL specific DAO `INFERRED` |
| 25 | Preferences / DataStore | `VERIFIED_STATIC` | `data/local/a`, M05 storage strings | full key list `UNKNOWN` |
| 26 | Code editor / hints / preview | `VERIFIED_STATIC` | `q.F`, `Ldg/a`, `CodeLanguage` | remote runner `UNKNOWN` |
| 27 | Native libraries | `VERIFIED_STATIC` (inventory) / `VERIFIED_RUNTIME` (loads) | M05 `.so` doc, M04 run | JNI surface `UNKNOWN` |
| 28 | Network API surface | `VERIFIED_STATIC` (verbs) | M02 `HTTP_VERBS_RESOLVED.json` | bodies `UNKNOWN` |
| 29 | Analytics / workers / services | `VERIFIED_STATIC` (names) | `analytics/a`, WorkManager classes | triggers `UNKNOWN` |
| 30 | smob anti-decompilation | `VERIFIED_STATIC` (bytecode) / `INFERRED` (causal link) | `classes.dex` string + junk `const/4` | — |
| 31 | Deobfuscation | `VERIFIED_STATIC` | 173 class / 596 method hints | low-vote hints `INFERRED` |
| 32 | Call graphs | `VERIFIED_STATIC` | 9 JSON, 632 real invoke edges | — |
| 33 | Runtime correct-answer state | `UNKNOWN` | M05 runs 001–005 | no deterministic M06 replay |
| 34 | Persisted progress after answer | `UNKNOWN` | Room write path static only | private DB extraction forbidden |
| 35 | Server responses / scoring / economy | `UNKNOWN` | `SERVER CONFIRMED = 0` | deliberate scope boundary |

## Deliverable inventory
19 numbered reports · 9 `.mmd` diagrams · 9 `.mmd` + 9 `.json` call graphs ·
22 method dossiers · 82 `.smali.txt` class dumps (+ `INDEX.json`) · 12 derived evidence/disassembly/toolchain files in `EVIDENCE/`
(+ `EVIDENCE/TOOLCHAIN/` full reproducible script set) · 10 byte-exact original samples + manifest ·
`SCHEMAS/` 5 JSON files · `EVIDENCE_DATABASE.json` · `RUNTIME_EVIDENCE/` ·
`MISSION_06_REVIEW.md` · `README.md` · `00_INVESTIGATION_PLAN.md`.

## Reproducibility
`/home/user/_work/m06/venv/bin/python` + `EVIDENCE/TOOLCHAIN/m06_dex.py`,
`export_catalog.py`, `map_methods.py`, `regenerate_all.py`, `call_graphs.py` and the
`write_*.py` generators; no network needed; all reads from
`ANALYSIS/_INPUT/classes*.dex` and the unchanged original APK.
