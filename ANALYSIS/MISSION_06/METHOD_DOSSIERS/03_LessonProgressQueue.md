# LessonProgressQueue — local answer counting

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/LessonProgressQueue.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC
`Lcom/getmimo/data/source/remote/progress/LessonProgressQueue;`, `classes.dex`.
Fields: `devMenuStorage Lze/a;`, `lessonProgressRepository`, `_answersInChapter Lua0/o;`
(MutableStateFlow), `answersInChapter` Flow.

### `storeLessonProgress(LessonProgress, Z, Z, cont)` @10058920, 136 insns
```
if (devMenuStorage.e()) return                  // dev-menu "disable progress" override
lessonProgressRepository.addOrUpdateLessonProgressInQueue(listOf(progress), bool, cont)
updateCorrectAnswersCount(cont)
if (progress.attempts != 1) ... else updateLessonStreakDetector(progress, bool)
```
### `updateCorrectAnswersCount(cont)` @10056956, 123 insns
```
val queued = repo.getAllLessonProgressInQueue()
val correct = queued.count { it.isSolvedCorrectly() }
_answersInChapter.emit(AnswersInChapter(correct, queued.size))
```
### `getCorrectLessonProgressCount` @10057692 = `queued.count{isSolvedCorrectly()}`
### `getCorrectLessonsFirstTryCount` @10058148 = `queued.count{isSolvedCorrectly() && attempts == 1}`
### `storeAndPostAllLessonProgress` @10058624
`repo.moveLessonProgressFromQueue()` → `repo.postUnsyncedLessonProgress()`.

These are the **only** chapter-end scoring formulas recovered from real bytecode; M05 left
scoring/thresholds `UNKNOWN`. `isSolvedCorrectly()` is `tries >= 1` (see dossier 04), not
`attempts >= 1`.

## Remaining uncertainty
- How `AnswersInChapter(correct,total)` is converted into XP / keys / coins / chapter-end
  success type is **not** in this class → `UNKNOWN`, likely server-owned
  (`GetChapterEndSuccessState`, `ChapterFinishedSuccessType`).
- `updateLessonStreakDetector` body (10 insns) delegates to another class; exact streak algorithm
  `UNKNOWN`.
