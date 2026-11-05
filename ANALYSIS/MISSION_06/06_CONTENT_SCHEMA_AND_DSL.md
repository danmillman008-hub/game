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

## Serialization contracts — VERIFIED_STATIC + M05 reused
Root of a tutorial file is `{"tutorial": {...}}` (M05 correction; naive `chapters` lookup
fails). `tracks.json` root is `TracksJson{publishSetVersion, tracks:List<TrackJson>}`.
`TrackJson{id, version, title, descriptionContent, isNew, isHidden, iconBanner,
sections:List<SectionJson>}`; `SectionJson{name, description, tutorialIds:List<Long>,
startIndex, endIndex}`; M05 verified all 144 English sections satisfy
`endIndex-startIndex+1 == len(tutorialIds)`.

`TutorialJson{id, version, type, codeLanguage, title, descriptionContent, chapters}`;
`Chapter{id,title,type,isCompleted,lessons}`;
`Lesson{id,title,images,contentType,hardModeSelected}` plus either
`content` (interactive DSL string) or `executableContent`.

### Executable contract (VERIFIED_STATIC)
```
executableContent : {
  instructions        : String,
  preselectedFileIndex: Int,
  hasVisualOutput     : Boolean,
  files               : [ { name:String, codeLanguage:CodeLanguage,
                           content:String, solvedContent:String } ],
  hints               : [ ... ]
}
```
M05 verified all 4,024 `executableContent` objects have
`instructions,preselectedFileIndex,hasVisualOutput,files,hints`.
`executable_files` is **not** a shipped key; the correct key is `executableContent`.
`solvedContent` is used by `ExecutableLessonViewModel.I()` as the answer key (M06).

### DSL tag vocabulary (VERIFIED_STATIC from DEX strings + M05 corpus)
Tags: `p`, `code`, `content`, `text`, `option`, `interaction`, `interactions`,
`selection`, `output`, `webview`, `img`, `database`, `html`, `body`, `strong`, `br`.
Attributes: `visible-if` (`always|correct|wrong`), `correct` (`true|false`),
`isDefault`, `startIndex`, `endIndex`, `value`, `type`, `version`, `style`, `codelang`,
`name`, `src`, `interaction` (`unlock|embedded|…`).
M05 counts: `text` 369,108; `code` 94,981; `p` 46,388; `option` 44,225;
`content` 41,221; `interaction` 11,729; `selection` 7,356; `output` 5,784;
`webview` 930; `visible-if wrong` 19,101 / `always` 18,869 / `correct` 173;
`correct false` 27,762 / `true` 7,356; `mimo.activity.*` correct 217, wrong 217,
completed 90.

### Interaction model mapping (VERIFIED_STATIC)
| DSL | Kotlin model | Answer representation |
|---|---|---|
| `<interaction type="fillTheGap">` + `<option correct="true">` | `Interaction$FillTheGap.c : List<Option>` | ordered list of `Option.a==true` tokens |
| `<interaction type="validatedInput" startIndex endIndex/>` | `Interaction$ValidatedInput{c,d,e,f}` | `code.subSequence(startIndex,endIndex)` |
| `<interaction type="selection" …>` | `Interaction$Selection{c,d,e}` | `SelectionItem{a:Z,b:CharSequence}` / `sm/a{b,c}` |
| `<interaction type="spell" startIndex endIndex/>` | `Interaction$Spell{c,d}` | code substring, letter sequence |
| `<webview version style interaction content>` | `LessonModule$Webview` + `WebviewType` | `mimo.activity.*` messages |
| `<database>` | `LessonModule$Database` | SQL playground |
| no interaction | `LessonInteractionType.None/Reveal` | `U()` auto-advance |

### WebView bridge (VERIFIED_STATIC, M05)
`assets/lesson-webview.js` injects
`MimoLesson.postMessage(JSON.stringify({documentID, kind, …}))` with kinds
`gesture / activity / focus / height / ready`; no scoring formula in JS.
`WebViewActivityResult` enum constants: `mimo.activity.correct`, `mimo.activity.wrong`,
`mimo.activity.completed`.

### Schemas delivered
`SCHEMAS/CONTENT_SCHEMA_M06.json` (this mission's consolidated contract),
`SCHEMAS/CLASS_CATALOG_MIMO.json`, `SCHEMAS/METHOD_CATALOG_MIMO.json`,
`SCHEMAS/OBFUSCATION_MAP.json`, `SCHEMAS/METHOD_NAME_MAP.json`,
plus M05 `SCHEMAS/JADX_MODEL_FIELDS.json` and `SHIPPED_CONTENT_STATS.json` (unchanged).

### Remaining uncertainty
- `Interaction$ValidatedInput.e:String` and `f:String[]` semantics = `UNKNOWN`.
- Full `Tag`/`Attribute` enum ordinal tables = `UNKNOWN`.
- Hard-mode alternate content selection predicate = `INFERRED`.
