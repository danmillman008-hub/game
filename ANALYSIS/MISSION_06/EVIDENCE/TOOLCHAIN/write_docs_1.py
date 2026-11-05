import pathlib
D=pathlib.Path('/home/user/game/ANALYSIS/MISSION_06');D.mkdir(parents=True,exist_ok=True)
APK='48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a'
PRE=f'''# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**Target:** original Mimo Android 9.35 APK, SHA-256 `{APK}` (unchanged)  
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

'''
docs={}
docs['01_EXECUTIVE_SUMMARY.md']=r'''
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
| disassembly dossiers | 83 files in `EVIDENCE/DISASM/` |
| real call graphs | 9 `.mmd` + 9 `.json` |
| diagrams | 9 |
| method dossiers | 22 |
| byte-exact original samples | 11 (`SAMPLES/MANIFEST.json`) |
| `SERVER CONFIRMED` | **0** |
'''
docs['02_METHODOLOGY_AND_TOOLCHAIN.md']=r'''
## Starting state (verified)
`git status --short` clean at `d0714b40` (`MISSION 05 FINAL…`); branch
`arena/aebb90b7-game`. M05 evidence reviewed: 42 deliverables, 112 evidence entries,
`EVIDENCE/ROOM_SQL.txt`, `SCHEMAS/JADX_MODEL_FIELDS.json`, `SCHEMAS/SHIPPED_CONTENT_STATS.json`,
`EVIDENCE/RUNTIME_STATIC_MATCH.json` (MATCH-1..5), five runtime run findings.
Original APK unchanged (142,353,499 B, SHA-256 above).

## Toolchain decisions — VERIFIED_STATIC
| Tool | Status | Decision |
|---|---|---|
| `java`, `jadx`, `jadx-gui`, `apktool`, `baksmali`, `dexdump`, `aapt`, `aapt2`, `radare2`, `ghidra`, `analyzeHeadless` | absent locally | not used |
| system `pip3 install androguard` | **failed** Debian PEP 668 `externally-managed-environment` | not retried |
| `/home/user/_work/m06/venv` + `pip install androguard` | **succeeded**, 4.1.4 | primary disassembler |
| M01 `ANALYSIS/_TOOLCHAIN/dexlib.py`, `dex_bytecode.py` | available | used as independent offset/call-graph cross-check |
| M02 `ANALYSIS/DEX_BYTECODE_EVIDENCE.json` | 6,016 edges / 1,211 exact | reused, not regenerated |
| JADX archive (`ANALYSIS/DECOMPILED/getmimo_sources.tar.gz`, 2,211 `.java`) | incomplete, many `Method not decompiled` | used only for field names; **not** treated as absence of implementation |

### Exact failure/cause records (requirement)
- `pip3 install --quiet --disable-pip-version-check androguard` →
  `error: externally-managed-environment`. Cause: Debian PEP 668. Alternative: venv, succeeded.
- Harness build #1/#2 produced `xrefs=0`. Cause: `DEX.get_methods()` returns
  `MethodIdItem` (no instructions); must iterate `d.get_classes()` → `c.get_methods()`.
- Build #3 `AttributeError: 'MethodIdItem' object has no attribute 'get_instructions'`.
- Build #4 `AttributeError: 'Instruction12x' object has no attribute 'get_offset'`;
  Androguard instructions expose `get_length()`, `get_name()`, `get_operands()`, `str(i)`.
  Fix: PC accumulator + regex over `str(i)`.
- **M06 xref bug found and fixed**: the original regex
  `(L[…]+;->[^\s,]+)` truncated descriptors containing spaces, e.g.
  `h0(Ljava/util/List; Z)V`, silently dropping call edges. Fixed to
  `(L[…]+;->.*)$` capturing to end-of-line; cache rebuilt from scratch
  (corrected cache: 78,560 xref targets). All call graphs in this mission use the corrected cache.
- Operand tuple repr is unsuitable for method refs; `str(i)` contains the full
  `Lclass;->method(...)`.

## Anti-decompilation — VERIFIED_STATIC + INFERRED
DEX contains exactly one `"Smob - Mod obfuscation tool v4.6 by Kirlif'"` string in
`classes.dex` (also emitted in `<clinit>` of `Lqm/i`, `Lte/a`, `Lye/b`, `ParserModule`,
`ModuleVisibility`, `Lgm/h` and several constructors). Bytecode streams contain injected
`const/4 vN, <small int>` no-ops that clobber registers not subsequently read, plus trailing
`fill-array-data-payload` objects inside the linear instruction stream. Example
`LessonProgress.isSolvedCorrectly()` has `const/4 v3, 2` immediately overwritten by
`const/4 v3, 1`. Causal link to M05's `JADX ERROR: NullPointerException in pass: ClassModifier`
is `INFERRED`, not proven. M06 filtered/annotated these decoys when reading branches.

## Deobfuscation technique — VERIFIED_STATIC
R8 renamed most classes to single letters but Kotlin synthetic inner-class names preserve
the original outer name. For each `X$foo$N`, parse `X` and read the first `<init>` argument
(the outer instance); the modal `X` is the original class name.
- 173 class mappings in `SCHEMAS/OBFUSCATION_MAP.json` (e.g. `base/c` →
  `InteractiveLessonBaseViewModel` 14 votes, `executable/q` → `ExecutableLessonViewModel`
  46 votes, `tracks/b` → `DefaultTrackLoader`, `network/a` → `AndroidNetworkUtils`).
- 596 method mappings in `SCHEMAS/METHOD_NAME_MAP.json` from coroutine inner-class
  `invokeSuspend` bodies. **Low-vote entries are heuristic**; only manually verified
  mappings (`V`, `X`, `W`, `U`, `Y`, `H`, `h0`, `d0`, `b0`, `e0`, `f0`, …) are used as
  facts in the call graphs and dossiers.

## Evidence pipeline
`dex → class/method index → disassembly → invoke xrefs → strings → fields → state
changes → pseudocode → dossier → diagram → evidence DB entry`.
`SCHEMAS/METHOD_CATALOG_MIMO.json` (6.8 MB) and `CLASS_CATALOG_MIMO.json` (1.6 MB) hold
per-method DEX file, code offset, instruction count, access, caller/callee counts and strings.

## What was NOT done
No backend reconstruction, no fabricated server responses, no account/login/purchase/
credential work, no auth bypass, no root/private DB extraction, no TLS/pinning bypass,
no APK modification, no replacement-app implementation, no repeated UI screenshot
collection, no new workflow dispatch.
'''
docs['03_APPLICATION_ARCHITECTURE.md']=r'''
## Layered architecture — VERIFIED_STATIC + INFERRED
`DIAGRAMS/01_full_architecture.mmd`, `02_class_dependency.mmd`.

### 1. Process entry (M01/M02/M04 evidence, VERIFIED_RUNTIME)
`com.getmimo`, `versionName=9.35`, `versionCode=1792759685`, `primaryCpuAbi=arm64-v8a`.
Launcher: `.ui.SplashActivity_default` → `.ui.onboarding.intro.IntroSlidesActivity`
(M04 run `41998643355`).
`Lcom/getmimo/ui/SplashActivity;` (2 inner-class votes) → `Lcom/getmimo/ui/a;`
`SplashViewModel`; `MainActivity` (14 votes) → `Lcom/getmimo/ui/main/d;` `MainViewModel`
(35 votes).

### 2. Content layer (M06, VERIFIED_STATIC)
`Lye/b;` assets loader; `Lye/d;` filesDir loader; `tracks/b; DefaultTrackLoader`;
`tracks/c; DefaultTracksRepository`; `Lte/c;` DSL parser; `Lgm/h;` interaction mapper.
Detailed in `05_CONTENT_PIPELINE.md` and dossiers 11–14.

### 3. Domain / interactors (M06, VERIFIED_STATIC)
`interactors/path/d; GetPathMapState`, `path/c; GetPathMapDialogs`,
`chapter/a; CanOpenChapterWithKeys`, `chapter/b; CreateChapterEndScreens`,
`chapter/c; GetLessonType`, `chapter/d; GetChapterEndSuccessState`,
`chapterend/a; GetChapterEndProgressWithEtaScreenData`, `eta/a; GetTrackEta`,
`practice/c; GetPracticeTrackList`, `lesson/b;`, `lesson/CreateBrowserOutput`,
`streak/b; ObserveUserStreakInfoCache`, `aitutor/a; GetAiTutorFreemiumUsage`,
`publicprofile/a; GetPublicCodePlaygrounds`.
These are plain Kotlin use-case classes with `invoke`/`a(…, Continuation)` suspend methods —
not a separate framework. `INFERRED` from naming and constructor injection shape.

### 4. UI layer (VERIFIED_STATIC)
Mix of **Fragments + Android ViewModel/LiveData** and **Jetpack Compose + Orbit MVI**:
- `base/b; InteractiveLessonBaseFragment` + `base/c; InteractiveLessonBaseViewModel`
  (LiveData `m0`, `kotlinx.coroutines.flow.i`).
- `executable/q; ExecutableLessonViewModel` uses `org.orbitmvi.orbit` container with state
  `Lzl/z;`.
- `ui/path/map/j; PathMapViewModel` (15 votes), `ui/path/map/a; PathMapFragment`.
- `ChapterActivity` (16 votes), `ChapterViewModel` (15), `ChapterFinishedFragment`/`ViewModel`.
- `Ui/lesson/interactive/*` per-interaction fragments + viewmodels.

### 5. Persistence (VERIFIED_STATIC)
Room (269 tables per M05; DAO `Lcg/a;`), `LessonProgressQueue`,
`CompletionRepository`, `data/local/a; DataStoreUserPreferences`, SharedPreferences keys,
in-memory `LiveData`/`StateFlow`, `LessonProgressRepository` unsynced queue.
See `11_LOCAL_PERSISTENCE.md`.

### 6. DI — VERIFIED_STATIC, framework `INFERRED`
ViewModels receive a hand-rolled 13-slot container `Lhm/b;` (`a`..`m` all
`Ljava/lang/Object;`), cast at each use site:
`b.d → LessonProgressRepository`, `b.b → analytics/a`, `b.g → data/local/a`,
`b.h → mf/a filesDir`, `b.i → lesson/sound/a`. Larger constructors (e.g. `q` has 32
parameters) indicate constructor injection assembled by a DI graph (Hilt/Dagger or Koin);
the exact framework is `UNKNOWN` — no annotation processor output was decoded.

### 7. Events / callbacks / workers (VERIFIED_STATIC)
`RunButton$State`, `InteractionKeyboardButtonState`, `Lym/f` interaction events,
`mimo.activity.*` WebView bridge messages, `Lqm/b` text watcher, `LessonProgressQueue`
StateFlow, WorkManager workers (`PostVisitWorker`, `StreakWidgetRefreshWorker`,
`AccountDeleteWork`, `AsyncRequestWorker` for glance). Native callbacks via JNI — see
`14_NATIVE_LIBRARIES_AND_JNI.md`.

### Component responsibility table
| Component | Responsibility | Inputs | Outputs / state changes |
|---|---|---|---|
| `Lye/b` | asset stream lookup by locale | `ContentLocale`, id | `InputStream` |
| `tracks/b` | UTF-8 read + JSON decode | stream | `JsonObject` |
| `Lte/c` | XML DSL → modules | HTML string | `ArrayList<LessonModule>` |
| `Lgm/h` | renderer selection | modules | `LessonInteractionType` |
| `base/c` | lesson session state machine | input events | LiveData, `LessonProgress`, Room |
| `LessonProgressQueue` | answer counting + sync | `LessonProgress` | `AnswersInChapter`, Room rows |
| `GetPathMapState` | unlock/completion state | Track + completions + keys + tier | `Lvn/n` |
| `NetworkUtils` | connectivity gate | `ConnectivityManager` | Boolean |
'''
docs['04_DEPENDENCY_INJECTION_AND_COMPONENT_GRAPH.md']=r'''
## Verified dependency edges
`CALL_GRAPHS/02_class_dependency.mmd` is drawn from real `iget-object`/`invoke` operands;
`CALL_GRAPHS/*.json` list exact signatures and code offsets.

### `Lhm/b;` (13 Object slots) — VERIFIED_STATIC
`base/c;-><init>(Lhm/b;)V` stores the container in field `b`. Verified casts:
| Slot | Cast target | Used by |
|---|---|---|
| `a` | (not decoded) | `O()` |
| `b` | `Lcom/getmimo/analytics/a;` | `f0()`, `a0()`, `g0()` |
| `c` | (not decoded) | |
| `d` | `LessonProgressRepository` | `H()` |
| `e` | (not decoded) | |
| `f` | (not decoded) | |
| `g` | `Lcom/getmimo/data/local/a;` | `d0()` |
| `h` | `Lmf/a;` (filesDir `File`) | `D()` cleanup |
| `i` | `Lcom/getmimo/ui/lesson/sound/a;` | `V()` success sound |
| `j..m` | (not decoded) | |

### Constructor-injected graphs (VERIFIED_STATIC signatures)
- `InteractiveLessonBaseViewModel(Lhm/b;)`
- `InteractiveLessonFillTheGapViewModel(Lbg/a; Lhm/b; Lim/b; base/d;)`
- `InteractiveLessonSelectionViewModel(Lbg/a; Lhm/b; Lnm/f; base/d;)`
- `InteractiveLessonSpellViewModel(Lbg/a; Lhm/b; Lpm/g; base/d;)`
- `InteractiveLessonValidatedInputViewModel(Lqf/d; Lbg/a; Lhm/b; Lqm/i;)`
- `InteractiveWebViewLessonViewModel(Lhm/b;)`
- `InteractiveLessonViewModel(Lye/g; Lgm/h; awesome/b; Lnp/g; codeeditor/highlight/a;)`
- `ExecutableLessonViewModel(32 parameters incl. `Lye/g;`, `LessonProgressRepository`,
  `analytics/a;`, `Lpe/a;`, `LessonProgressQueue`, `Lqf/d;`, `Lze/a;`, `Lbg/a;`,
  `Lri/d;`, `Lmf/a;`, sound, dispatchers, `Lds/z;`, `Lcm/e;`, `interactors/path/a;`,
  `interactors/playgrounds/d;`, `Lmh/b;`, `Lkf/d;`, `Lgi/e;`, IAP, `inputconsole/a;`,
  AiTutor, `interactors/lesson/b;`, `Lep/t0;`, `codeeditor/highlight/a;`)
- `DefaultTracksRepository(Lye/e; Lfe/a;)`, `DefaultTrackLoader(...)`,
  `LessonProgressRepository(LessonProgressApi; Lye/g; Lye/c; Lnp/d; Lri/d; completion/a; Lcg/a;)`
- `ChapterViewModel(Lye/c; Lze/a; analytics/a; LessonProgressQueue; Lmf/a; SavedStateHandle;
  chapter/c; chapter/b; Lri/d; chapter/e; IAP; Lnp/d; Lce/c; data/local/a;)`
- `GetPathMapState`/`GetPathMapDialogs` take 15 collaborators (purchase repository,
  feature flags, analytics, network utils, dev-menu, path interactors…).

### DI framework — `UNKNOWN`
No `@Inject` annotation metadata, Hilt component classes or Koin module DSL were decoded in
M06. Naming/injection shape is `INFERRED` as compile-time constructor injection. Exact
framework, scopes and singleton graph = `UNKNOWN` with pointer: constructor signatures in
`SCHEMAS/METHOD_CATALOG_MIMO.json` (search `<init>`).

### Background workers / services — VERIFIED_STATIC
`PostVisitWorker`, `AccountDeleteWork`, `StreakWidgetRefreshWorker`,
`MimoStreakWidget`, `NotPremiumNotificationService`, `CustomerIOPushNotificationRegistry`,
WorkManager `CoroutineWorker` subclasses. Their triggers/periodicity were not decoded =
`UNKNOWN`.
'''
docs['05_CONTENT_PIPELINE.md']=r'''
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
`SAMPLES/MANIFEST.json` lists 11 byte-exact APK members with SHA-256, including a full
`tutorial-*.json` per interaction type, full `tracks.json`, `lesson-webview.js`,
`lesson-webview-fonts.js` and the shipped `spell` fixture `testdata/127-0-1.html`.
**No new content format was invented.**

### Remaining uncertainty
- `Lte/a.a` (490 insns) full interaction/option construction logic = `UNKNOWN` in detail.
- `SingleChoice`/`MultipleChoice`/`Reveal` exact dispatch predicates = `UNKNOWN`.
- `Lye/d` (filesDir) loader selection and content-update trigger = `UNKNOWN`.
- 4,257 external URL references (M05) are content strings; their offline substitution =
  `UNKNOWN`.
'''
docs['06_CONTENT_SCHEMA_AND_DSL.md']=r'''
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
'''
docs['07_LESSON_MODULE_RENDERING.md']=r'''
## Verified rendering chain
`base/c.O()` @10949840 (616 instructions) is the central renderer-input builder.
Steps read directly from bytecode:
1. store `D = LessonBundle`, `u = LessonContent$Interactive`.
2. `N()` resets RunButton/keyboard states (`InteractionKeyboardButtonState.b`).
3. iterate `getLessonModules()`, keep only modules whose `LessonModule.a` equals
   `ModuleVisibility.c` (`ALWAYS`) using `Lcom/google/android/recaptcha/internal/b.o(List)`.
4. for each kept module:
   - `Paragraph` → `jm/j(Lds/v.m(paragraph.c))` (join `ArrayList<CharSequence>`),
   - `Image` → `jm_i(image.c:String)`,
   - `Webview` → `jm/k(webview.c:String, webview.e:WebviewType)`.
5. post `ArrayList` of render items to LiveData `m` (`m0.l(Object)`).
6. repeat the filter for code/interaction blocks; build `Lym/n`/`Lym/j` tab models;
   call `h0(list, boolean)` → `Lym/f(v, list, boolean)` → LiveData `w`.

### Feedback-driven module visibility — VERIFIED_STATIC
`ModuleVisibility` = `ALWAYS / CORRECT / WRONG`. After a run:
- `V()` → `c0()` posts `jm/q(list,true)` when `T()` is true,
  plays success sound via `lesson/sound/a.a(true)`.
- `X()` → `d0()` posts `jm/o` copy with `solutionFeedbackWrong`, and M05 run-004
  rendered red "Try again" with the Q option disabled/grey (`VERIFIED_RUNTIME`).
Thus `visible-if="correct"`/`"wrong"` modules are revealed by LiveData state changes, not by
re-parsing the DSL. Exact filtering of `CORRECT`/`WRONG` modules in the adapter = `INFERRED`.

### Per-interaction render items (VERIFIED_STATIC)
| ViewModel | Render items | Evidence |
|---|---|---|
| fillTheGap | `jm/y(qc/a)` prose spans + `jm/x(qc/a,String,jm/w,I)` gaps built from `Option.c/d` char offsets | `FillTheGapViewModel.smali.txt` `E()` |
| validatedInput | `Lym/n(tabName,tabName,Lym/m(prefix,suffix),CodeLanguage)` and `Lym/j` | `ValidatedInputViewModel.smali.txt` `E()` |
| selection | `sm/a` option items with `b=selected`, `c=isCorrect` | `SelectionFragmentRunHandler.smali.txt` |
| spell | `cn/d(id,String,boolean)` letter tokens | `SpellFragmentRunHandler.smali.txt` |
| webview | `EmbeddedLessonWebView` + injected JS | `InteractiveWebViewLessonFragment.smali.txt` |
| no interaction | `NonInteractiveLessonFragment` → `U()` | `NonInteractiveLessonFragment.smali.txt` |

### Renderer selection (VERIFIED_STATIC)
`CALL_GRAPHS/06_content_pipeline.json`, `METHOD_DOSSIERS/12_LessonInteractionTypeSelector.md`.
Nine `LessonInteractionType` subclasses; `InteractiveLessonViewModel.E()` posts `Lgm/g` to
LiveData; `ChapterActivity` chooses the Fragment.

### Hard mode — VERIFIED_STATIC
`LessonContent$Interactive.hardModeModulesOrDefault()`, `getHasDifferentHardModeContent()`;
`InteractiveLessonViewModel.E()` recomputes `Lgm/h.a(hardModeLessonModules)` when hard mode
is enabled; `ChapterViewModel.shouldStartChapterInHardMode` (`PathMapViewModel.N`) and
DataStore `completed_hard_mode_chapters` / `KEY_HARD_MODE_COMPLETED_LESSON_IDS` persist it.

### Remaining uncertainty
- Exact RecyclerView/Compose adapter and `CodeBodyView`/`DatabaseView` drawing logic = `UNKNOWN`
  (M05 captured UI hierarchies; behavioural reconstruction does not require widget internals).
- Full `O()` (616 insns) contains additional module branches not decoded = `INFERRED`.
'''
for n,c in docs.items():
    (D/n).write_text(PRE+c.strip()+'\n',encoding='utf-8')
    print('wrote',n,len(PRE+c))
