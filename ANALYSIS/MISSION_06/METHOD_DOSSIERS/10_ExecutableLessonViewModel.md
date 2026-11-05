# ExecutableLessonViewModel (Orbit MVI) — offline solution check

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/ExecutableLessonViewModel.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC — M05 code-execution boundary resolved
`Lcom/getmimo/ui/lesson/executable/q;` = `ExecutableLessonViewModel` (46 inner-class votes).
Constructor takes 32 injected dependencies; state class `Lzl/z;`; MVI container
`Lorg/orbitmvi/orbit/…`. 9 methods.

### `q;->I(Ldm/i; LessonBundle; ArrayList; LessonContent$Executable; Z)Ldm/i` @10912932, 114 insns
**This is the answer validator for `executableFiles` lessons.**
```
val userContents    = codeFiles.map { it.getContent() }          // ArrayList<String>
val solvedContents  = executable.files.map { it.getSolvedContent() }  // shipped
if (userContents == solvedContents) return currentState          // CORRECT
else {
    // Ldm/g(emptyList) + Ldm/h(...) error state
    log(IncorrectSolutionException())
    return Ldm/h(...)                                            // INCORRECT
}
```
The comparison is `ArrayList.equals()` on **exact strings**, in file order. Therefore the
shipped `solvedContent` field alone is sufficient to decide correctness offline; no remote
code execution is required for that decision. M05 asked whether `solvedContent` suffices —
answer: **yes for the correctness check** (`VERIFIED_STATIC`).

### `q;->E(container)LlessonProgress` @10913380, 57 insns
`createLessonProgress(bundle, state.h(startedAt), tries, state.e(attempts))`, where
`tries` uses `if (state.f) 1 else min(...)` — exact condition `INFERRED`.

### `q;->F(Lym/h; Lzl/z;)V` @~10913600, 248 insns — local hints
For `TutorialType.GuidedProject`, maps the selected file name
`style.css / index.html / script.py / script.js` to static maps `Lcm/b.a..d` keyed by
lessonId, extracts identifiers and emits `Lep/v`, `Lep/y` hint/highlight events.

### `q;->J(...)` (118 insns) builds `Lbe/n0` analytics with
`ExecutableLessonRunResult`, `lessonId`, `tutorialId`, `tutorialVersion`, `trackId`,
`duration` (`Seconds.secondsBetween(startedAt, now)`), `attempts`, file dump or
`"Lesson passed"`.
### `q;->K(x10/b, cont)` = `updateCodeExecutionState` (Orbit intent).
### `q;->H(Lo70/m;)` returns a coroutine Job; `q;->G()` 12 insns.

## Boundary — NOT reconstructed
`POST /v1/code/runfiles` and `/v1/tutorials/{id}/runFiles` are Retrofit endpoints referenced
by the client; **no server response bodies, no server business logic** were reconstructed.
Browser preview is local: `Ldg/a;<clinit>` contains a shipped HTML template with
`<link rel="stylesheet" href="style.css">` and `<script src="script.js">`.

## Remaining uncertainty
- Whether `q->I` is used for *all* executable lessons or only for guided-project variants
  = `UNKNOWN` (callers: 1, from an MVI reducer not fully decoded).
- SQL / HTML / CSS / JS exercise execution via an external runner remains a client-side
  boundary = `UNKNOWN` on the server side.
