# LessonBundle / LessonContent data models

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/LessonBundle.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC field tables
`Lcom/getmimo/ui/lesson/interactive/LessonBundle;` (Parcelable):
`a:J lessonId`, `b:I chapterIndex`, `c:I sectionIndex`, `d:J`, `e:J tutorialId`,
`f:J trackId`, `g:J`, `v:I tutorialVersion`, `w:I`, `x:TutorialType`, `y:ChapterType`,
`z:Z`, `A:Z`, `B:Z isPracticeProgress`, `C:Z`, `D:Integer?`, `E:String?`,
`F:LessonIdentifier`, `G:Z`, `H:I`, plus `CREATOR`, `I` (empty instance).

`LessonContent$Interactive`: `lessonModules:List`, `hardModeLessonModules:List`;
`getHasDifferentHardModeContent()`, `hardModeModulesOrDefault()`.

`LessonContent$Executable`: `instructions:String`, `preselectedFileIndex:int`, `files:List`,
`getHasBrowserOutput()`, `getHasInputConsole()`.
`LessonContent$Executable$File`: `name`, `codeLanguage`, `content`, `solvedContent`.

`Lesson`: `id:J`, `title:String`, `images:List`, `contentType:LessonContentType`,
`hardModeSelected:boolean`.
`LessonContentType` enum: `INTERACTIVE`, `EXECUTABLE_FILES`.
`TutorialType`: `Learn, MobileProject, Challenge, Quiz, GuidedProject,
GuidedProjectOptional, RecreateProject, PracticeRequired, PracticeOptional`.
`ChapterType`: `NONE, PRACTICE_LEVEL_1..3, QUIZ, CHALLENGE_DIFFICULTY_0..4`.
`CodeLanguage`: `NONE, BASH(.bash), CPP(.cpp), CSHARP(.cs), CSS(style.css),
CSV(data.csv), …` (full enum not enumerated here).

## Remaining uncertainty
- Field names for `LessonBundle` are `INFERRED` from usage in `createLessonProgress`,
  `f0`, `U()` and `toString()` strings; DEX stores only letters `a..H`.
