# DataStore / SharedPreferences local state

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/DataStoreUserPreferences.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC
`Lcom/getmimo/data/local/a;` = `DataStoreUserPreferences` (26 methods). Verified string
constants from DEX / M05 `EVIDENCE/STORAGE_AND_ONBOARDING_STRINGS.txt`:
`completed_hard_mode_chapters`, `KEY_HARD_MODE_COMPLETED_LESSON_IDS`,
`onboarding_user_daily_goal`, `dailyGoal`, `first_run`, `path_overview`, hard-mode flags.
`base/c;->d0()` calls `a.f(cont)` returning a Boolean and `a.p()` (clear/reset), i.e. the
wrong-feedback block reads a locally stored preference before deciding whether to show
extra feedback.

`ChapterViewModel` stores `KEY_HARD_MODE_COMPLETED_LESSON_IDS`;
`MainActivity.onCreate` reads `onboarding_user_daily_goal` / `dailyGoal`.

## Persistence architecture (VERIFIED_STATIC from M05 + M06)
Room database with 269 tables (M05), identity hashes
`08b926448d86528e697981ddd30459f7` and `2b8ab6d303d9a501bd8c8fb78d8352fc`;
`lesson_progress` 11 columns with `in_queue`; `chapter_completions`,
`tutorial_completions`; DataStore preferences; in-memory `LiveData`/`StateFlow`;
`LessonProgressQueue` unsynced rows survive process death by virtue of Room.

## Remaining uncertainty
- Exact DataStore filename, migrations and every preference key = `UNKNOWN` in detail.
- Force-stop / process-recreation restoration was not runtime-tested in M06 = `UNKNOWN`.
