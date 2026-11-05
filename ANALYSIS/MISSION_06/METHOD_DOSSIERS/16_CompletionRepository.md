# CompletionRepository — local completion attachment

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/CompletionRepository.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC
`Lcom/getmimo/data/source/local/completion/a;` = `CompletionRepository` (7 votes),
8 methods, constructor uses `Leg/f;` (Room database wrapper).

`b(Track, cont)` = `CompletionRepository$attachTutorialCompletionToTrack$1` @9981172,
178 instructions:
```
val rows = Room.query("SELECT ... tutorial completions WHERE trackId=?", ...)  // via Leg/a
val byTutorialId = rows.associateBy { it.getTutorialId() }
return track.copy(sections = sections.map { it.copy(tutorials = tutorials.map { t ->
    t.copy(isCompleted = byTutorialId[t.id]?.isCompleted ?: false,
           completedChapters = ..., hardMode = ...) }) })
```
Verified entities: `Lcom/getmimo/data/model/room/TutorialCompletion;` with getters
`getTutorialId()`, `isCompleted()`, `completedChapters`; Room SQL for
`chapter_completions` (PK `chapter_id,track_id`) and `tutorial_completions`
(PK `tutorial_id,track_id`) is in M05 `EVIDENCE/ROOM_SQL.txt`.

## Remaining uncertainty
- Exact Room query strings behind `Leg/a` are 269-table SQL strings catalogued by M05 but
  not re-decoded here = `INFERRED` for this specific DAO method.
- How server sync merges completions into these tables = `UNKNOWN` / server-owned boundary.
