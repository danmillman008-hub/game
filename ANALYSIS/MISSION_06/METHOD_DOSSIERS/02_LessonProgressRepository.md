# LessonProgressRepository & createLessonProgress

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/LessonProgressRepository.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC — exact record construction
`Lcom/getmimo/data/source/remote/progress/LessonProgressRepository;->createLessonProgress(
 Lcom/getmimo/ui/lesson/interactive/LessonBundle; Lorg/joda/time/Instant; I I)
 Lcom/getmimo/data/model/room/LessonProgress;`  
`classes.dex` code_offset `10063916`, 44 instructions.

Pseudocode recovered from the `invoke-direct/range` register map:
```
fun createLessonProgress(bundle, startedAt, tries, attempts): LessonProgress {
    val completedAt = Instant()                       // now
    if (Instant().isBefore(startedAt))                // guard, logged, not thrown
        logError("CreateLessonProgress: completedAt date (" + now +
                 ") is before startedAt date (" + startedAt + ")")
    return LessonProgress(
        lessonId          = bundle.a,                 // long
        completedAt       = completedAt,
        startedAt         = startedAt,
        tries             = tries,                    // 3rd arg
        tutorialId        = bundle.e,                 // long
        tutorialVersion   = bundle.v,                 // int
        trackId           = bundle.f,                 // long
        publishSetVersion = tracksRepository.c(),     // current shipped publish set
        attempts          = attempts,                 // 4th arg
        isPracticeProgress= bundle.B,                 // boolean
        inQueue           = true                      // const/4 v15,1
    )
}
```
`LessonProgress` constructor signature `(J Instant Instant I J I J J I Z Z)V` and 11 getters
are in `EVIDENCE/DISASM/LessonProgress.smali.txt`. Room SQL (M05 `EVIDENCE/ROOM_SQL.txt`)
confirms columns and composite PK `(lesson_id, tutorial_id)`.

## Callers — VERIFIED_STATIC
`base/c;->H(I I)` @10948948 passes `(tries, attempts)`; `ExecutableLessonViewModel.E()`
@10913380 also calls it with `state.zl/z` fields.

## Other methods (verified)
`addOrUpdateLessonProgressInQueue(List, Z, cont)` (62 insns) — Room upsert;
`clearLessonProgressQueue` (36), `getAllLessonProgressInQueue` (22),
`moveLessonProgressFromQueue` (26) — clears `in_queue`;
`postUnsyncedLessonProgress` (44) — **offline gate**, see dossier `18_NetworkUtils.md`;
`toProgressList` (76), `toLessonProgressSyncResult` (14), `fetchTrackCompletionForFavoriteTracks` (239).

## Client-side boundary
`LessonProgressApi` Retrofit interface is only referenced; no response bodies, no server logic
were reconstructed. `SERVER CONFIRMED = 0`.

## Remaining uncertainty
- Argument names `tries`/`attempts` are `INFERRED` from constructor order and getter names;
  DEX has no parameter names for these two ints.
- `isBefore` vs `isAfter` of joda `Lld0/c;->h` = `INFERRED` (guard message names the condition).
