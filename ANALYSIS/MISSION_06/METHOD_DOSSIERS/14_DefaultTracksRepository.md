# DefaultTracksRepository — track/tutorial/chapter loading

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/DefaultTracksRepository.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC
`Lcom/getmimo/data/content/tracks/c;` = `DefaultTracksRepository` (7 votes).
Constructor `(Lye/e; Lfe/a;)V`. Methods:
`a(J,I,I,cont)` 25, `b(J,I,I,cont)` 25, `c()J` 18 (current `publishSetVersion`),
`d(J,cont)` 226 (load single `TrackJson`), `e(J,cont)` 86,
`f(List,cont)` 102, `g(cont)` 69 (5 callers), `h(cont)` 86 (3 callers),
`i(J,cont)` 409 (`loadTrackWithChapters$1`).

`i(J)` reads `TrackJson` via `d(J)`, then maps:
```
Track(id, version, title, descriptionContent, isNew, isHidden, iconBanner, sections)
```
For each `SectionJson` it reads `getName()`, `getDescription()`, `getTutorialIds()`,
resolves each tutorial id through the loader, and builds `Chapter` / `Tutorial` models
with `isCompleted` flags from `CompletionRepository`. It excludes a set of `TutorialType`s
(`GuidedProject`, `MobileProject`, `Quiz`, `RecreateProject`, `GuidedProjectOptional`)
from the chapter-loading path — `INFERRED` exact reason.
`c()` is called by `LessonProgressRepository.createLessonProgress` to stamp
`publishSetVersion`.

## Callers — VERIFIED_STATIC
`PathMapViewModel`, `GetPathMapState`, `ChapterViewModel`, `LessonProgressRepository`,
`GetPracticeTrackList`.

## Remaining uncertainty
- Complete 409-instruction `i()` state machine not decoded line-by-line = `UNKNOWN` in detail.
- Caching/invalidation policy between asset JSON and Room completion state = `UNKNOWN`.
