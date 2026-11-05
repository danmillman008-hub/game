# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**Target:** original Mimo Android 9.35 APK, SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Branch:** `arena/aebb90b7-game`, baseline `d0714b40`  
**Toolchain:** Androguard 4.1.4 in `/home/user/_work/m06/venv` over all 12 original
`ANALYSIS/_INPUT/classes*.dex`; patched read-only harness `EVIDENCE/M06_DEX_HARNESS.py`.  
`SERVER CONFIRMED = 0`. Backend services, server business logic, server databases and cloud
infrastructure are **not** reconstructed; only client-side boundaries are recorded.

> Every finding is classified `VERIFIED_STATIC`, `VERIFIED_RUNTIME`, `VERIFIED_BOTH`,
> `INFERRED` or `UNKNOWN`. Evidence fields (APK path, class/method, DEX file + code offset,
> bytecode/Smali, caller/callee, SQL, runtime log, reproduction steps) are given inline or in
> the referenced `EVIDENCE/`, `SCHEMAS/`, `CALL_GRAPHS/`, `METHOD_DOSSIERS/` artefacts.

---

## Mission outcome
M06 **closed the principal M05 correctness gaps by reading the original Dalvik bytecode**,
after JADX had produced stubs. It did **not** implement a replacement app, did not
reconstruct a backend, and did not invent a content format.

### Newly recovered (`VERIFIED_STATIC`)
1. **Answer validation is entirely client-side** and is now algorithmically specified for
   `fillTheGap`, `selection`, `spell`, `validatedInput`, WebView activity lessons and
   `executableFiles`. See `08_INTERACTION_VALIDATION.md`, `16_RECONSTRUCTED_ALGORITHMS.md`.
2. **`validatedInput` expected answer** is the substring of the shipped code block delimited
   by `startIndex`/`endIndex`; matching normalises `toLowerCase(Locale.US)` and keeps only
   letters, digits and `< > ( ) : { } , .`; exact equality → CORRECT, normalised-only equality
   → PARTIAL MATCH, otherwise INCORRECT (`Lqm/e`, `Lqm/f`, `Lqm/g`).
3. **Content pipeline is fully identified**: `AssetManager.open("lessons-<lang>/tracks/…")`
   → UTF-8 `readText` → `kotlinx.serialization` DTOs → `org.xmlpull.v1.XmlPullParser` DSL
   parser (`Lte/c`) → six `LessonModule` subclasses → `Lgm/h` interaction-type selector →
   nine renderer types → `base/c.O()` render-item mapping. See `05_CONTENT_PIPELINE.md`.
4. **`isSolvedCorrectly()` reads `tries >= 1`, not `attempts >= 1`** — a documented
   correction of M05 (`17_CORRECTIONS_AND_LIMITATIONS.md`). `createLessonProgress` maps all
   11 Room columns from `LessonBundle`, `Instant.now()`, `tries`, `attempts` and
   `publishSetVersion`; `inQueue=true`.
5. **Chapter-end answer counting** = `AnswersInChapter(correct = queued.count{isSolvedCorrectly()},
   total = queued.size)`; `getCorrectLessonsFirstTryCount` adds `attempts == 1`.
6. **Executable lesson correctness** = `userFileContents == shippedSolvedContents` by
   `ArrayList.equals` in `ExecutableLessonViewModel.I()` — so shipped `solvedContent`
   suffices for the offline correctness decision.
7. **Exact offline gate**: `NetworkUtils.a()` = `ConnectivityManager.getActiveNetwork()` +
   `hasTransport(WIFI|CELLULAR)`; `postUnsyncedLessonProgress` throws
   `NoConnectionException` with the verbatim log when offline.
8. R8 name recovery: 173 classes and 596 methods mapped from Kotlin inner-class names;
   3,133 Mimo classes / 12,851 methods / 407,242 instructions catalogued.
9. smob anti-decompilation: one `"Smob - Mod obfuscation tool v4.6 by Kirlif'"` string in
   `classes.dex`, junk `const/4` no-ops and trailing `fill-array-data-payload` inside method
   streams — the reason JADX emitted `Method not decompiled` (`INFERRED` causal link).

### Deliberately still `UNKNOWN`
Exact unlock boolean combination (`GetPathMapState$invoke$3`, 659 insns), XP/keys/coins/
streak/daily-goal award formulas and thresholds, server response bodies, full
`SingleChoice`/`MultipleChoice`/`Reveal` dispatch predicates, remote code-execution service,
`W()` partial-match feedback details, absolute scoring formula. These are listed with exact
class/method pointers in `18_OPEN_QUESTIONS.md` and the coverage matrix in `19_REVERSE_ENGINEERING_COVERAGE.md`.

### No new emulator run
M05 produced 5 runs (001–005) and M06 reused them. No new M06 runtime experiment was
warranted: the specific hypotheses were resolved deterministically from DEX, and the only
remaining runtime hypothesis (reading `lesson_progress` after a correct answer) requires
root/private-DB extraction, explicitly forbidden. See `RUNTIME_EVIDENCE/`.

### Quantities
| Metric | Value |
|---|---|
| DEX files | 12 |
| class_defs / methods indexed | 29,454 / 129,071 |
| Mimo classes / methods / instructions | 3,133 / 12,851 / 407,242 |
| xref targets / caller edges / field refs | 78,560 / 105,012 / 82,732 |
| disassembly dossiers | 82 files in `EVIDENCE/DISASM/` |
| real call graphs | 9 `.mmd` + 9 `.json` |
| diagrams | 9 |
| method dossiers | 22 |
| byte-exact original samples | 11 (`SAMPLES/MANIFEST.json`) |
| `SERVER CONFIRMED` | **0** |
