# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING (Mimo Android 9.35)

**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`, 142,353,499 bytes, **unchanged**.  
**Baseline:** `d0714b40` ("MISSION 05 FINAL…") · **branch** `arena/aebb90b7-game`.  
**Method:** read-only Androguard 4.1.4 disassembly of all 12 original `classes*.dex`
+ verbatim shipped assets. No APK modification, no emulator root, no auth/purchase work,
no TLS/pinning bypass, no backend reconstruction.  
**`SERVER CONFIRMED = 0`.**

## What this mission adds
M05 left several behavioural gaps because the JADX archive had `Method not decompiled`
stubs. M06 went to the DEX bytecode and closed them:

- **`isSolvedCorrectly()` = `tries >= 1`**, not `attempts >= 1` (M05 correction).
- Exact 11-column `createLessonProgress` record construction.
- All answer validators (fillTheGap, selection, spell, validatedInput, WebView activity,
  executable `solvedContent` comparison) with pseudocode.
- XML DSL parser technology: `org.xmlpull.v1.XmlPullParserFactory`, six module parsers,
  nine renderer types.
- Exact asset locale paths, `NetworkUtils` offline gate, offline chapter-end fallback,
  `AnswersInChapter` counting formula.
- 173 R8 class mappings, 596 method hints, 12,851-method catalog, 82 full class dumps,
  9 real call graphs, 22 dossiers, 10 byte-exact original samples.

Everything still unresolved is listed with a class/method/offset pointer in
`18_OPEN_QUESTIONS.md` and the matrix in `19_REVERSE_ENGINEERING_COVERAGE.md`.
`INFERRED` and `UNKNOWN` are never presented as confirmed.

## Reports (19)
- `01_EXECUTIVE_SUMMARY.md`
- `02_METHODOLOGY_AND_TOOLCHAIN.md`
- `03_APPLICATION_ARCHITECTURE.md`
- `04_DEPENDENCY_INJECTION_AND_COMPONENT_GRAPH.md`
- `05_CONTENT_PIPELINE.md`
- `06_CONTENT_SCHEMA_AND_DSL.md`
- `07_LESSON_MODULE_RENDERING.md`
- `08_INTERACTION_VALIDATION.md`
- `09_LESSON_STATE_MACHINE.md`
- `10_LEARNING_PROGRESSION.md`
- `11_LOCAL_PERSISTENCE.md`
- `12_CODE_EDITOR_AND_EXECUTABLE_LESSONS.md`
- `13_UI_NAVIGATION_AND_RUNTIME.md`
- `14_NATIVE_LIBRARIES_AND_JNI.md`
- `15_OFFLINE_BEHAVIOR_SPECIFICATION.md`
- `16_RECONSTRUCTED_ALGORITHMS.md`
- `17_CORRECTIONS_AND_LIMITATIONS.md`
- `18_OPEN_QUESTIONS.md`
- `19_REVERSE_ENGINEERING_COVERAGE.md`

## Supporting deliverables
`01_EXECUTIVE_SUMMARY.md` · `MISSION_06_REVIEW.md` · `EVIDENCE_DATABASE.json`
(113 classified entries) · `DIAGRAMS/` (9 Mermaid) · `CALL_GRAPHS/` (9 `.mmd` + 9 `.json`,
632 real invoke edges) · `METHOD_DOSSIERS/` (22) · `EVIDENCE/` (82 `.smali.txt` dumps,
derived disassembly, toolchain, deobfuscation notes) · `SCHEMAS/` (5 JSON) ·
`SAMPLES/` (10 byte-exact APK members + `MANIFEST.json`) · `RUNTIME_EVIDENCE/`
(M05 correlation + no-new-run justification).

## Classification vocabulary
`VERIFIED_STATIC` (read from DEX/assets) · `VERIFIED_RUNTIME` (M04/M05 emulator evidence) ·
`VERIFIED_BOTH` · `INFERRED` · `UNKNOWN`.

## Reproduce
`/home/user/_work/m06/venv/bin/python` with `EVIDENCE/M06_DEX_HARNESS.py`,
`M06_EXPORT_CATALOG.py`, `M06_METHOD_NAME_MAP.py`; no network needed.
