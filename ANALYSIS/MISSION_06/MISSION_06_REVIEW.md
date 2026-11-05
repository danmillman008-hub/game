# MISSION 06 — FINAL REVIEW

## Acceptance criteria
| Criterion | Status |
|---|---|
| 19 numbered reports | ✅ `01_…` … `19_…` |
| ≥9 architecture diagrams | ✅ 9 Mermaid in `DIAGRAMS/` |
| Real call graphs from xrefs | ✅ 9 `.mmd` + 9 `.json`, 632 real invoke edges |
| Method dossiers with fields/state/callers/callees | ✅ 22 |
| Original samples preserved | ✅ 10 byte-exact APK members + SHA-256 manifest |
| Targeted runtime evidence | ✅ M05 correlation + explicit no-new-run justification (no repeat screenshots) |
| Evidence DB with classification + evidence fields | ✅ 113 entries |
| Coverage matrix per component/state/flow | ✅ `19_REVERSE_ENGINEERING_COVERAGE.md`, 35 rows |
| Scripts/toolchain with exact failure records | ✅ `02_METHODOLOGY_AND_TOOLCHAIN.md`, `EVIDENCE/TOOLCHAIN/` |
| M05 doc-by-doc evidence review | ✅ `17_CORRECTIONS_AND_LIMITATIONS.md` C-1..C-8 + `SCHEMAS/CONTENT_SCHEMA_M06.json` |
| No backend / server reconstruction | ✅ `SERVER CONFIRMED = 0` everywhere |
| Root/private DB/auth bypass forbidden | ✅ none performed |
| Original APK unchanged | ✅ SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` |

## Classification totals (EVIDENCE_DATABASE.json)
{
 "VERIFIED_STATIC": 90,
 "VERIFIED_RUNTIME": 5,
 "VERIFIED_BOTH": 5,
 "INFERRED": 2,
 "UNKNOWN": 11
}

## Headline corrections to M05
1. `LessonProgress.isSolvedCorrectly()` reads **`tries`**, not `attempts`.
2. `validatedInput` matching is a client-side normalizer, not an opaque server check.
3. `executableFiles` correctness compares user code to shipped `solvedContent`.
4. Lesson DSL is XML parsed by `XmlPullParser`, not an unknown custom parser.
5. Nine interaction types, not six.

## Deliberately unresolved (not failures)
Correct-answer runtime UI, persisted row after answer, server response bodies, absolute
XP/keys/coins/streak/daily-goal formulas, exact unlock boolean combination, full
`SingleChoice`/`MultipleChoice`/`Reveal` dispatch, `W()` and `d0()` details, remote code
execution, native JNI surface. Each has an exact pointer in `18_OPEN_QUESTIONS.md`.

## QA performed
- `EVIDENCE_DATABASE.json` parses; all referenced workspace file paths resolve.
- All 82 disassembly dumps + both catalogs regenerated with corrected xref cache.
- All 9 call-graph JSONs parse and each edge has `caller`, `callee`, `opcode`.
- All 10 samples match the APK member bytes (SHA-256 in `MANIFEST.json`).
- `SCHEMAS/*.json` parse; `CONTENT_SCHEMA_M06.json` keys are verbatim shipped/DEX strings.
- Original APK SHA-256 unchanged; `ANALYSIS/_INPUT/classes*.dex` untouched.
- `ANALYSIS/EVIDENCE_INDEX.json` extended with `mission_06_append` without mutating the
  336 M01–M04 entries or the M02/M05 appends.

## Bottom line
M06 reconstructed **how the client actually validates answers, records progress, renders
shipped lessons and behaves offline**, from real bytecode, with every uncertain point
labelled. It did not invent a backend, a content format, or a scoring formula.
