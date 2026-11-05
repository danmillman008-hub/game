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

## Full pipeline — `VERIFIED_STATIC`
`APK ASSETS → LOADER → DESERIALIZATION → MODELS → PARSER → MODULES → RENDERER → UI`.
Diagram: `DIAGRAMS/03_content_pipeline.mmd`; call graph: `CALL_GRAPHS/06_content_pipeline.json`
(40 nodes, 248 real invoke edges).

### 1. Asset discovery & locale — VERIFIED_STATIC
`ContentLocale` enum (`classes.dex` @9681384): `RU EN ES PT DE FR IT ID TR PL` with
`languageString` `ru en es pt de fr it id tr pl`.
`Lye/b;<clinit>` builds `LinkedHashMap<ContentLocale, "lessons-<lang>/tracks">` from
`"lessons-" + getLanguageString()` then `"/tracks"`.
`Lye/b.b(J)` opens `"lessons-<lang>/tracks/tutorial-<id>.json"`;
`Lye/b.d()` opens `"lessons-<lang>/tracks/tracks.json"`;
`Lye/b.c()` returns `"file:///android_asset/lessons-common/icons"`.
`Lye/d;` is a parallel loader rooted at `Context.getFilesDir()`.
M05 measured 10,298 curriculum JSON files across 10 locales, English `publishSetVersion=753`,
19 tracks, 144 sections, 1,029 tutorials, 1,947 chapters, 18,272 lessons.

### 2. Deserialization — VERIFIED_STATIC
`DefaultTrackLoader.c(InputStream):String` uses `Lka0/a.a` Charset (UTF-8),
`InputStreamReader`, `BufferedReader`, `readText()`.
`DefaultTrackLoader.a(J,I,I):JsonObject` calls `Lhb0/b.b(String, KSerializer)` and
`Lhb0/j.g/h` JSON element navigation → **`kotlinx.serialization`**.
Generated `$$serializer` classes exist for `TracksJson`, `TrackJson`, `SectionJson`,
`TutorialJson`, `Chapter`, `Lesson`, `LessonContent$Executable$File` (field names
`publishSetVersion`, `solvedContent`, `isCompleted` verified in DEX strings).
M05 exact field lists in `ANALYSIS/MISSION_05/SCHEMAS/JADX_MODEL_FIELDS.json`.

### 3. Content models — VERIFIED_STATIC
`LessonContent$Interactive{lessonModules, hardModeLessonModules}`,
`LessonContent$Executable{instructions, preselectedFileIndex, files, getHasBrowserOutput,
getHasInputConsole}`, `File{name, codeLanguage, content, solvedContent}`.
`Lesson{id,title,images,contentType,hardModeSelected}`.
`LessonContentType`: `INTERACTIVE` (14,248) / `EXECUTABLE_FILES` (4,024).

### 4. DSL parser — VERIFIED_STATIC (technology recovered in M06)
The lesson `content` field is **XML-like text**, parsed by `org.xmlpull.v1.XmlPullParser`
via `XmlPullParserFactory.newInstance()` with `setNamespaceAware(true)`.
`Lte/c.b(String):ArrayList<LessonModule>` @14378108 (400 insns) dispatches
`p → Lte/d.a`, `code → Lte/a.a`, `selection → Lte/e.a`, `img → Lte/c.a`,
`webview → Lte/g.a`, `database → Lte/b.a`; `html`/`body` and unknown tags are skipped with
`xml_parse_error_module` analytics. Full dossier: `METHOD_DOSSIERS/11_DSL_LessonParser.md`.
`Lgm/h;<clinit>` pre-extracts `<body>…</body>` with
`Regex("<\s*body[^>]*>(.*?)<\s*/\s*body>")`.

### 5. Module construction — VERIFIED_STATIC
Six `LessonModule` subclasses with exact fields
(`EVIDENCE/DISASM/ParserModule.smali.txt`, `SCHEMAS/CLASS_CATALOG_MIMO.json`):
`Paragraph{c:ArrayList}`, `Code{c:CharSequence,d:List,e:Output,f:ModuleVisibility,
g:CodeLanguage,v:String,w:List}`, `Image{c:String,d:ModuleVisibility}`,
`Webview{c:String,d:ModuleVisibility,e:WebviewType}`, `Selection{c:ArrayList}`,
`Database{c:ArrayList,d:ModuleVisibility}`.
`Interaction` subclasses: `FillTheGap{b:Z,c:List<Option>}`,
`Selection{b:Z,c:I,d:I,e:List}`, `Spell{b:Z,c:I,d:I}`,
`ValidatedInput{b:Z,c:I,d:I,e:String,f:String[]}`.
`Option{a:Z correct, b:CharSequence text, c:I startIndex, d:I endIndex}`.
`ModuleVisibility`: `ALWAYS("always")`, `CORRECT("correct")`, `WRONG("wrong")`.

### 6. Renderer selection — VERIFIED_STATIC
`Lgm/h.a(List):LessonInteractionType` @12460480 (437 insns) → 9 types:
`InteractiveWebView`, `FillTheGap`, `Spell`, `Selection`, `ValidatedInput`,
`SingleChoice`, `MultipleChoice`, `Reveal`, `None`.
`InteractiveLessonViewModel.E()` also selects `hardModeLessonModules` when hard mode is on,
and posts `Lgm/g` (type + content + bundle + index) to LiveData.

### 7. Render-item mapping — VERIFIED_STATIC
`base/c.O(LessonContent$Interactive, LessonBundle)` @10949840 (616 insns):
filters `LessonModule.a == ModuleVisibility.c (ALWAYS)`, maps
`Paragraph → jm/j(CharSequence)`, `Image → jm/i(String)`,
`Webview → jm/k(String, WebviewType)`, posts to LiveData `m`.
Feedback variants (`CORRECT`/`WRONG` modules) are revealed by `c0()`/`d0()` after a run.
Per-interaction ViewModels create `jm/x` gap items, `Lym/n` validated-input tabs,
`Lym/j` code tabs, `Lim/a`/`Lnm/e`/`Lpm/f` interaction states.

### 8. Image / asset resolution — VERIFIED_STATIC + INFERRED
`Lye/b.c()` icon base `file:///android_asset/lessons-common/icons`;
`DefaultTrackLoader.d(String)` rewrites relative image paths with `"/"` using `Ls7/a.n`.
`Lesson.images:List` from JSON. Exact resolution algorithm for all image URL shapes =
`INFERRED`, not fully decoded.

### 9. Progress-state injection — VERIFIED_STATIC
`CompletionRepository.b(Track, cont)` attaches `isCompleted` / `completedChapters` from
Room `tutorial_completions`/`chapter_completions`; `GetPathMapState` builds `Lvn/d0`
`Completed` states; `LessonBundle` carries `isChapterAlreadyCompleted`. Offline path map
screens in M05 run-002/003 still rendered local content.

### Original samples
`SAMPLES/MANIFEST.json` lists 10 byte-exact APK members with SHA-256, including a full
`tutorial-*.json` per interaction type, full `tracks.json`, `lesson-webview.js`,
`lesson-webview-fonts.js` and the shipped `spell` fixture `testdata/127-0-1.html`.
**No new content format was invented.**

### Remaining uncertainty
- `Lte/a.a` (490 insns) full interaction/option construction logic = `UNKNOWN` in detail.
- `SingleChoice`/`MultipleChoice`/`Reveal` exact dispatch predicates = `UNKNOWN`.
- `Lye/d` (filesDir) loader selection and content-update trigger = `UNKNOWN`.
- 4,257 external URL references (M05) are content strings; their offline substitution =
  `UNKNOWN`.
