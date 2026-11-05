# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged) · `SERVER CONFIRMED = 0` · classification on every finding.

---

## Corrections — VERIFIED_STATIC (M06 bytecode corrects M05)
| # | M05 statement | M06 correction | Evidence |
|---|---|---|---|
| C-1 | `LessonProgress.isSolvedCorrectly()` = `attempts >= 1` | **`tries >= 1`**; `classes.dex` @9913532 uses `iget … ->tries I`. `tries` is the solved flag (`V()` → 1, `X()` → 0); `attempts` is the submission counter `base/c.d` | `METHOD_DOSSIERS/04_LessonProgress_isSolvedCorrectly.md`, `EVIDENCE/DISASM/LessonProgress.smali.txt` |
| C-2 | "no scoring formula found" | Chapter-end **local** counting formula recovered: `AnswersInChapter(count{isSolvedCorrectly}, queued.size)` and `count{isSolvedCorrectly && attempts==1}`. Absolute XP/keys/streak awards still `UNKNOWN` | `METHOD_DOSSIERS/03_LessonProgressQueue.md` |
| C-3 | Interaction types ~6 | **9** `LessonInteractionType` constants including `SingleChoice`, `MultipleChoice`, `Reveal`, `None` | `METHOD_DOSSIERS/12_LessonInteractionTypeSelector.md` |
| C-4 | DSL parsed by "unknown parser" | **`org.xmlpull.v1.XmlPullParser`** via `XmlPullParserFactory` | `METHOD_DOSSIERS/11_DSL_LessonParser.md` |
| C-5 | `validatedInput` matching `UNKNOWN` | normaliser + 3-way result fully recovered | `METHOD_DOSSIERS/08_ValidatedInput.md` |
| C-6 | `solvedContent` sufficiency questioned | `q.I()` compares user file contents to shipped `solvedContent` by `List.equals` → **sufficient for correctness decision** | `METHOD_DOSSIERS/10_ExecutableLessonViewModel.md` |
| C-7 | JADX stubs suggested missing implementations | Stubs are caused by smob-injected junk `const/4` and trailing `fill-array-data-payload`; real implementations exist in DEX (`INFERRED` causal link) | `02_METHODOLOGY_AND_TOOLCHAIN.md` |
| C-8 | `NetworkUtils` inferred from strings | Exact `hasTransport(WIFI|CELLULAR)` gate recovered | `METHOD_DOSSIERS/18_NetworkUtils.md` |

## Toolchain/QA corrections made during M06
- `EVIDENCE/TOOLCHAIN/m06_dex.py` xref regex truncated descriptors containing spaces; fixed to `(L…->.*)$`;
  cache rebuilt (78,560 xref targets). All call graphs use the corrected cache.
- `callers()` returns 4-tuples `(caller, opcode, offset, dex)`; early scripts assumed 2.
- `class_fields.get(c)` may be `None` on library classes.
- `METHOD_CATALOG_MIMO.json` / `CLASS_CATALOG_MIMO.json` and the **first 18**
  disassembly headers were generated before the xref fix; their caller/callee *count*
  headers are stale. The `EVIDENCE/DISASM/*.smali.txt` instruction bodies are unaffected.
  `CALL_GRAPHS/*.json` were regenerated from the corrected cache and are authoritative.
- `METHOD_NAME_MAP.json` low-vote entries are heuristic; call graphs show only manually
  verified semantic names.
- `EVIDENCE/TOOLCHAIN/export_disasm2.py` reported `MISSING ExecuteFilesResponse` / `ExecuteLessonResponse`
  semantic labels — this is absence of a *name hint*, not proof the classes are absent.
- `LessonProgressDao` dump has 0 methods (interface); Room SQL is the authoritative evidence.
- `strings_by_method` scans only method string constants; absence of `runFiles` or
  `System.loadLibrary` in that index is **not** proof of absence.

## Known limitations — explicit
1. **No new emulator run.** Local sandbox has no emulator/ADB/SDK/Java/KVM; M05 already ran
   5 experiments. Repeating the 24-tap chain without deterministic replay was explicitly
   ruled out. M06 runtime claims reuse M05 evidence, clearly labelled.
2. **No private data extraction.** No root, no `/data/data/com.getmimo/databases` read, no
   TLS/pinning bypass, no credential/account/purchase/auth work.
3. **No server reconstruction.** `SERVER CONFIRMED = 0`; no response bodies, no backend
   business logic, no server DB, no cloud infra.
4. **No APK modification.** Original APK SHA unchanged; all DEX/assets read-only.
5. **Truncated transcripts.** Long coroutines (`Lye/b.a`, `Lye/d`, `DefaultTracksRepository.i`,
   `GetPathMapState$invoke$3`, `DefaultTrackLoader$getExecutableLesson$2`, `Lhg/e.intercept`,
   `X/W/d0/e0`) were printed partially in terminal scratch dumps; **full bodies are saved**
   in `EVIDENCE/DISASM/*.smali.txt` and `EVIDENCE/*_DISASM.txt`. Interpretations that depend
   on the undecoded remainder are marked `INFERRED`/`UNKNOWN`.
6. **JADX archive incomplete** (2,211 `.java`, many `Method not decompiled`); used only for
   cross-checked field names.

## What remains UNKNOWN (exact pointers)
`18_OPEN_QUESTIONS.md` and `19_REVERSE_ENGINEERING_COVERAGE.md` list each with class,
method, DEX offset and why it is unresolved.
