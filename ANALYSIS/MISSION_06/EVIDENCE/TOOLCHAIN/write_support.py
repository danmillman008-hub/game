import json,pathlib,hashlib
R=pathlib.Path('/home/user/game/ANALYSIS/MISSION_06');A=pathlib.Path('/home/user/game/ANALYSIS')
APK='48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a'
DB=json.loads((R/'EVIDENCE_DATABASE.json').read_text())
# ---------- consolidated content schema ----------
schema=dict(
 document='MISSION 06 — consolidated shipped content & DSL contract (no invented format)',
 apk_sha256=APK,classification='VERIFIED_STATIC',
 derived_from=['../MISSION_05/SCHEMAS/CONTENT_SCHEMA.json','../MISSION_05/SCHEMAS/SHIPPED_CONTENT_STATS.json',
              'SCHEMAS/CLASS_CATALOG_MIMO.json','EVIDENCE/MODEL_FACTS.txt','EVIDENCE/DSL_PARSER_DISASM.txt',
              'SAMPLES/MANIFEST.json'],
 note='Every key below appears verbatim in original APK assets or as a DEX string/field name. No new content format was authored.',
 shipped_english_v753=dict(publishSetVersion=753,asset_root='assets/lessons-<locale>/tracks/',
   locales=['ru','en','es','pt','de','fr','it','id','tr','pl'],
   curriculum_json_files_all_locales=10298,tracks=19,sections=144,tutorials=1029,chapters=1947,
   lessons=18272,duplicate_lesson_ids=0,
   section_invariant='endIndex-startIndex+1 == len(tutorialIds), holds for all 144 sections',
   content_type_counts=dict(interactive=14248,executableFiles=4024),
   executable_content_required_keys=['instructions','preselectedFileIndex','hasVisualOutput','files','hints']),
 json_contract=dict(
   tracks_json_root='TracksJson{publishSetVersion:Long, tracks:List<TrackJson>}',
   track_json='TrackJson{id:Long, version:Int, title:String, descriptionContent:String, isNew:Boolean, isHidden:Boolean, iconBanner:String?, sections:List<SectionJson>}',
   section_json='SectionJson{name:String, description:String, tutorialIds:List<Long>, startIndex:Int, endIndex:Int}',
   tutorial_root='{"tutorial": TutorialJson}  (NOT a bare chapters array)',
   tutorial_json='TutorialJson{id:Long, version:Int, type:TutorialType, codeLanguage:CodeLanguage, title:String, descriptionContent:String, chapters:List<Chapter>}',
   chapter='Chapter{id:Long, title:String, type:ChapterType, isCompleted:Boolean, lessons:List<Lesson>}',
   lesson='Lesson{id:Long, title:String, images:List<String>, contentType:LessonContentType, hardModeSelected:Boolean}',
   lesson_content_interactive='LessonContent$Interactive{lessonModules:List<String>, hardModeLessonModules:List<String>} + getHasDifferentHardModeContent()/hardModeModulesOrDefault()',
   lesson_content_executable='LessonContent$Executable{instructions:String, preselectedFileIndex:Int, files:List<File>, hints:List, getHasBrowserOutput(), getHasInputConsole()}',
   executable_file='LessonContent$Executable$File{name:String, codeLanguage:CodeLanguage, content:String, solvedContent:String}',
   not_a_key='executable_files is NOT a shipped key; use executableContent'),
 dsl=dict(technology='org.xmlpull.v1.XmlPullParser via XmlPullParserFactory.newInstance(), setNamespaceAware(true)',
   entry_method='Lte/c;->b(Ljava/lang/String;)Ljava/util/ArrayList; @14378108, 400 instructions',
   body_regex='<\\s*body[^>]*>(.*?)<\\s*/\\s*body>',
   tags=['p','code','content','text','option','interaction','interactions','selection','output','webview','img','database','html','body','strong','br'],
   attributes=['visible-if','correct','isDefault','startIndex','endIndex','value','type','version','style','codelang','name','src','interaction'],
   dispatch={'p':'Lte/d.a → LessonModule$Paragraph','code':'Lte/a.a → LessonModule$Code',
     'selection':'Lte/e.a → LessonModule$Selection','img':'Lte/c.a → LessonModule$Image',
     'webview':'Lte/g.a → LessonModule$Webview','database':'Lte/b.a → LessonModule$Database',
     'html/body/unknown':'skip + xml_parse_error_module'},
   module_visibility=['ALWAYS("always")','CORRECT("correct")','WRONG("wrong")'],
   parser_module=['CODE','PARAGRAPH','SELECTION'],
   interactions=['FillTheGap{c:List<Option>}','Selection{c,d,e}','Spell{c,d}','ValidatedInput{c,d,e,f}'],
   option='Option{a:Boolean isCorrect, b:CharSequence text, c:Int startIndex, d:Int endIndex}',
   module_fields=dict(Paragraph='c:ArrayList',Code='c,d,e,f,g,v,w',Image='c,d',Webview='c,d,e',Selection='c:ArrayList',Database='c,d'),
   renderer_types=['interactive_webview','fill_the_gap','spell','selection','validated_input','single_choice','multiple_choice','slide','reveal','none'],
   webview_bridge='MimoLesson.postMessage(JSON.stringify({documentID, kind, ...})); kinds gesture/activity/focus/height/ready; no answer evaluation in JS',
   webview_activity_results=['mimo.activity.correct','mimo.activity.wrong','mimo.activity.completed'],
   corpus_tag_counts=dict(text=369108,code=94981,p=46388,option=44225,content=41221,interaction=11729,
     selection=7356,output=5784,webview=930,visible_if_wrong=19101,visible_if_always=18869,
     visible_if_correct=173,correct_false=27762,correct_true=7356,activity_correct=217,activity_wrong=217,activity_completed=90)),
 enums=dict(TutorialType=['Learn','MobileProject','Challenge','Quiz','GuidedProject','GuidedProjectOptional','RecreateProject','PracticeRequired','PracticeOptional'],
   ChapterType=['NONE','PRACTICE_LEVEL_1','PRACTICE_LEVEL_2','PRACTICE_LEVEL_3','QUIZ','CHALLENGE_DIFFICULTY_0..4'],
   LessonContentType=['INTERACTIVE','EXECUTABLE_FILES'],
   ContentLocale=['RU','EN','ES','PT','DE','FR','IT','ID','TR','PL'],
   CodeLanguage_examples=['BASH','CPP','CSHARP','CSS','CSV','HTML','JAVA','JAVASCRIPT','KOTLIN','PYTHON','SQL']),
 original_samples='SAMPLES/MANIFEST.json — 11 byte-exact APK members with SHA-256',
 unknown=['Tag/Attribute enum ordinal tables','Interaction$ValidatedInput.e:String and f:String[] semantics','hard-mode alternate content predicate','full Lte/a.a 490-instruction construction'])
(R/'SCHEMAS/CONTENT_SCHEMA_M06.json').write_text(json.dumps(schema,indent=1,ensure_ascii=False),encoding='utf-8')
# ---------- directory READMEs ----------
(R/'EVIDENCE/README.md').write_text('''# MISSION 06 — EVIDENCE

All files here are derived **read-only** from the 12 original `ANALYSIS/_INPUT/classes*.dex`
and the unchanged APK (SHA-256 `%s`).

| Path | Content |
|---|---|
| `DISASM/` | %d verbatim Androguard 4.1.4 class disassemblies + `INDEX.json`; every method header carries DEX file, code offset, instruction count, corrected caller/callee counts and xref lists |
| `VALIDATION_RAW_DISASM.txt` | long-method answer-validator disassembly (fillTheGap, selection, spell, validatedInput) |
| `VALIDATEDINPUT_SETUP_DISASM.txt` | `setupViews$2`, `Lqm/d.E`, `qm/i.a` normalizer |
| `ALGORITHM_DIGEST.txt` | progress queue, completion, path-banner, network, chapter-end, executable-lesson methods |
| `DSL_PARSER_DISASM.txt` | `Lte/c`, `Lte/a..g`, `Lgm/h` disassembly |
| `MODEL_FACTS.txt`, `PARSER_AND_STATE_FACTS.txt` | recovered field/enum/state tables |
| `PATH_STATE_DISASM.txt` | `GetPathMapState$invoke$3`, `Lcc/b.y` |
| `INTERACTION_SELECTOR_DISASM.txt` | `Lgm/h.a` and related |
| `DEX_STRING_INDEX.txt` | 565-line string-constant index (content/network/native/executable) |
| `DEOBFUSCATION_NOTES.md` | R8 name recovery, smob decoys, method-name-map caveats |
| `M06_DEX_HARNESS.py`, `M06_EXPORT_CATALOG.py`, `M06_METHOD_NAME_MAP.py` | reproducible toolchain (Androguard venv required) |

`SERVER CONFIRMED = 0`. No server responses, no private app databases, no emulator
screenshots were added here. Runtime evidence from M05 is cross-referenced in
`RUNTIME_EVIDENCE/` and `EVIDENCE_DATABASE.json`.
'''%(APK,json.loads((R/'EVIDENCE/DISASM/INDEX.json').read_text())['files']),encoding='utf-8')
(R/'EVIDENCE/DEOBFUSCATION_NOTES.md').write_text('''# R8 name recovery and anti-decompilation notes

## VERIFIED_STATIC
R8 renamed most application classes to single letters (`base/c`, `executable/q`, `Lye/b`,
`Lte/c`, `Lqm/i`). Kotlin synthetic inner classes retain the original outer class name, so:

1. Enumerate every class with `$` in its name.
2. Take `X$foo$N` → `X` (original semantic stem).
3. Read the first `<init>` parameter — the outer instance type — to get the obfuscated class.
4. The modal `X` across all inner classes of that outer is the recovered name.

173 mappings in `SCHEMAS/OBFUSCATION_MAP.json` (e.g. `executable/q` →
`ExecutableLessonViewModel`, 46 votes). 596 method hints in
`SCHEMAS/METHOD_NAME_MAP.json` come from coroutine inner-class names such as
`lessonSolvedCorrectly$1`; **low-vote entries are heuristic**, and only manually verified
names are used as facts in call graphs/dossiers.

## Smob anti-decompilation — VERIFIED_STATIC bytecode / INFERRED causal link
`classes.dex` contains exactly one string
`Smob - Mod obfuscation tool v4.6 by Kirlif'`, emitted via `const-string` in many
`<clinit>`/constructor bodies. Method streams also contain injected `const/4 vN, <junk>`
no-ops that clobber registers not subsequently read, and trailing
`fill-array-data-payload` objects in the linear decode. Example:
`LessonProgress.isSolvedCorrectly()` @9913532 has `const/4 v3, 2` immediately overwritten
by `const/4 v3, 1`. M05's JADX `Method not decompiled` / `JADX ERROR: NullPointerException
in pass: ClassModifier` plausibly results from these decoys (`INFERRED`, not proven).
M06 filtered them before reading branches and booleans.

## Known caveats
- `METHOD_NAME_MAP.json` votes=1 is a hint, not exact-name proof.
- `export_disasm2.py` reported `MISSING ExecuteFilesResponse` / `ExecuteLessonResponse`
  labels — absence of a *name hint*, not proof the class/API is absent.
- `LessonProgressDao.smali.txt` has 0 methods because it is an interface; Room SQL in
  `../MISSION_05/EVIDENCE/ROOM_SQL.txt` is authoritative.
- `DEX_STRING_INDEX.txt` scans method string constants only; absence of `runFiles` or
  `System.loadLibrary` is **not** proof of absence.
- All 82 dumps and both catalogs were regenerated with the corrected xref cache
  (descriptors containing spaces preserved; 78,560 xref targets).
''',encoding='utf-8')
(R/'CALL_GRAPHS/README.md').write_text('''# MISSION 06 — REAL CALL GRAPHS

Nine `.mmd` diagrams + nine `.json` machine-readable graphs. Every edge is an actual
`invoke-*` xref extracted from the 12 original DEX files with Androguard 4.1.4 and the
**corrected** xref cache (78,560 targets / 105,012 caller edges). BFS from the listed root
methods, bounded depth and node count; bounds and roots are recorded in each `.json`.

| File | Root | Nodes | Edges |
|---|---|---|---|
'''+''.join('| `%s` | %s | %d | %d |\n'%(
 f.name,json.loads(f.read_text())['title'],json.loads(f.read_text())['node_count'],json.loads(f.read_text())['edge_count'])
 for f in sorted((R/'CALL_GRAPHS').glob('*.json')))+'''
Node labels use only manually verified semantic method names; heuristic low-vote names from
`SCHEMAS/METHOD_NAME_MAP.json` are deliberately not displayed as fact. Each `.json` node also
carries DEX file, code offset and instruction count where available.
''',encoding='utf-8')
(R/'DIAGRAMS/README.md').write_text('''# MISSION 06 — ARCHITECTURE DIAGRAMS (Mermaid)

| File | Subject |
|---|---|
| `01_full_architecture.mmd` | whole client: APK assets → loaders → domain → UI → Room → client-side boundary |
| `02_class_dependency.mmd` | real DI/class dependency edges |
| `03_content_pipeline.mmd` | locale → AssetManager → JSON → XmlPullParser → modules → renderer |
| `04_lesson_execution.mmd` | lesson lifecycle from `LessonBundle` to progress |
| `05_interaction_validation.mmd` | five independent answer validators |
| `06_progression_state_machine.mmd` | Locked / Unlocked / UnlockedButNoKeys / Completed |
| `07_persistence_flow.mmd` | `LessonProgress` → Room `in_queue` → sync gate |
| `08_code_execution.mmd` | `solvedContent` comparison vs remote runner boundary |
| `09_offline_architecture.mmd` | local-capable vs client-side blocked vs server-owned |

Solid edges = `VERIFIED_STATIC` xref/field relation; dashed = `INFERRED` or client-side
boundary. `SERVER CONFIRMED = 0`.
''',encoding='utf-8')
(R/'METHOD_DOSSIERS/README.md').write_text('''# MISSION 06 — METHOD DOSSIERS

22 dossiers. Each gives the obfuscated signature, recovered semantic name, DEX file and
code offsets, constructor/field tables, verified implementation behaviour, real caller and
callee lists, output/state changes and an explicit **Remaining uncertainty** section.

| # | Dossier | Core claim |
|---|---|---|
| 01 | InteractiveLessonBaseViewModel | 33-method session state machine, `Y/V/X/U/H/e0/f0` |
| 02 | LessonProgressRepository | exact 11-column `createLessonProgress` |
| 03 | LessonProgressQueue | `AnswersInChapter` counting formula |
| 04 | LessonProgress.isSolvedCorrectly | **`tries >= 1`**, M05 correction |
| 05 | FillTheGap | ordered exact-string answer comparison |
| 06 | Selection | `list.all{ selected == isCorrect }` |
| 07 | Spell | letter-by-letter exact comparison |
| 08 | ValidatedInput | normalizer + 3-way Correct/Partial/Incorrect |
| 09 | WebViewLesson | `mimo.activity.*` client-side completion |
| 10 | ExecutableLessonViewModel | `solvedContent` `List.equals` check |
| 11 | DSL_LessonParser | `XmlPullParserFactory` dispatch |
| 12 | LessonInteractionTypeSelector | nine renderer types |
| 13 | AssetLoaders | exact locale asset paths |
| 14 | DefaultTracksRepository | `loadTrackWithChapters` |
| 15 | GetPathMapState | path-map state classes; exact unlock rule `UNKNOWN` |
| 16 | CompletionRepository | Room completion attachment |
| 17 | ChapterFinishedViewModel | offline fallback `handleOfflineState$1` |
| 18 | NetworkUtils | `hasTransport(WIFI|CELLULAR)` gate |
| 19 | CanOpenChapterWithKeys | keys gate |
| 20 | DataStoreUserPreferences | local preference state |
| 21 | LessonBundle_and_LessonContent | verified field tables |
| 22 | BaseFragment_and_NonInteractive | UI wiring / auto-advance |

Classification on every section. `SERVER CONFIRMED = 0`.
''',encoding='utf-8')
(R/'SAMPLES/README.md').write_text('''# MISSION 06 — ORIGINAL SHIPPED SAMPLES

`MANIFEST.json` lists 11 **byte-exact copies of original APK members** with source APK path,
byte size and SHA-256. Nothing was authored, rewritten or reconstructed. The APK is unchanged.

| File | APK member | Why |
|---|---|---|
| `ORIGINAL_fillTheGap.json` | `assets/lessons-en/tracks/tutorial-4589.json` | `fillTheGap` + `validatedInput` lesson |
| `ORIGINAL_validatedInput.json` | same tutorial (second copy) | explicit validatedInput example |
| `ORIGINAL_selection.json` | `tutorial-2307.json` | `<selection>` and `correct="true/false"` |
| `ORIGINAL_webview.json` | `tutorial-3144.json` | `<webview version=…>` |
| `ORIGINAL_hardModeContent.json` | `tutorial-2346.json` | `hardModeContent` alternate modules |
| `ORIGINAL_executableContent.json` | `tutorial-3042.json` | full `executableContent` incl. `solvedContent` |
| `ORIGINAL_assets_lessons-en_tracks_tracks.json` | `tracks.json` (v753) | full shipped track index |
| `ORIGINAL_assets_lesson-webview.js` | `assets/lesson-webview.js` | WebView↔native bridge |
| `ORIGINAL_assets_lesson-webview-fonts.js` | `assets/lesson-webview-fonts.js` | injected font loader |
| `ORIGINAL_assets_testdata_127-0-1.html` | `assets/testdata/127-0-1.html` | shipped `spell` interaction fixture |

Smallest matching English v753 tutorial was chosen per interaction type. The v753 English
curriculum sample set contains no `spell` tag, so the shipped testdata fixture is used for
that interaction; it is still an original APK member. `assets/testdata/test-tracks.json`
is a `publishSetVersion=52` fixture, not the shipped v753 curriculum — it is not presented
as such here. See `../MISSION_05/SAMPLES/README.txt` for M05's additional samples.
''',encoding='utf-8')
# ---------- runtime evidence ----------
RT=R/'RUNTIME_EVIDENCE';RT.mkdir(exist_ok=True)
(RT/'README.md').write_text('''# MISSION 06 — RUNTIME EVIDENCE

**No new emulator experiment was run in M06.** This directory contains explicit
cross-references to the five M05 GitHub Actions runs and the static↔runtime hypothesis
correlation, plus the justification.

Local sandbox has no emulator, ADB, Android SDK, Java or KVM. Runtime host/device facts in
this repository come only from M04/M05 GitHub Actions runs; M06 is a read-only DEX/static
reconstruction. `SERVER CONFIRMED = 0`.

| File | Content |
|---|---|
| `M06_HYPOTHESIS_CORRELATION.md` | which M05 runtime observation corroborates which M06 static method, with classification |
| `NO_NEW_RUN_JUSTIFICATION.md` | why a repeat run was neither warranted nor permitted |

Referenced M05 artefacts (unchanged): `../MISSION_05/RUNTIME/RUN_42002808217_FINDINGS.md`,
`RUN_42003884423_FINDINGS.md`, `RUN_42006697783_FINDINGS.md`,
`../MISSION_05/EVIDENCE/RUNTIME_STATIC_MATCH.json`, `../MISSION_05/SAMPLES/`.
''',encoding='utf-8')
(RT/'M06_HYPOTHESIS_CORRELATION.md').write_text('''# M06 static methods ↔ M05 runtime observations

Classification: `VERIFIED_BOTH` only where a M05 observation and M06 bytecode both exist.
No M06 screenshot/log is presented as newly captured.

| # | M06 `VERIFIED_STATIC` method | M05 `VERIFIED_RUNTIME` observation | Classification | Reproduction |
|---|---|---|---|---|
| 1 | `Lye/b.b(J)` opens `lessons-<lang>/tracks/tutorial-<id>.json` | `42003884423` STEP-24 rendered tutorial-904 lesson 151403 ("Guess the letter"); `42006697783` rendered offline track 274 AI/ChatGPT lessons | `VERIFIED_BOTH` | M05 `RUNTIME/RUN_42003884423_FINDINGS.md`, `RUN_42006697783_FINDINGS.md`, `EVIDENCE/RUNTIME_STATIC_MATCH.json` MATCH-1/3/4/5 |
| 2 | `LessonContent$Executable` + `solvedContent` shipped in APK | `42003884423` OFFLINE-03 rendered tutorial-2199 lesson 63259 executable lesson | `VERIFIED_BOTH` | MATCH-2, `SAMPLES/runtime_matched_executable_lesson_63259.json` |
| 3 | `base/c.X()` → `d0()` wrong-feedback block | `42005358012` wrong answer → red "Try again", Q disabled/grey, `Continue` → code editor | `VERIFIED_BOTH` | M05 `RUNTIME/RUN_42003884423_FINDINGS.md` / run-004 archive notes; STEP screenshots in M05 |
| 4 | `NetworkUtils.a()` `hasTransport(WIFI|CELLULAR)` gate; `postUnsyncedLessonProgress` offline guard | `42002808217` cold start with `Active default network: none`, `NetworkUnknown`/`UnknownHostException` for analytics, no FATAL/ANR; first three offline XMLs byte-identical to online | `VERIFIED_BOTH` | M05 `RUNTIME/RUN_42002808217_FINDINGS.md` |
| 5 | `ChapterFinishedViewModel$handleOfflineState$1` → local already-completed state | M05 run-002/003 path screen "Connect to the internet to progress further" while local lesson content remained visible | `VERIFIED_BOTH` | M05 `RUNTIME/RUN_42002808217_FINDINGS.md` |
| 6 | `Lqm/i.a` normalizer / `lim/d.E0` / `Lkm/f.b` / `Lpm/b.E0` / `q.I` answer validators | **No correct answer or offline answer was ever submitted** in M05 runs 001–005 | `VERIFIED_STATIC` only | `UNKNOWN` for correct-answer runtime state |
| 7 | `LessonProgressQueue.storeLessonProgress` → Room `lesson_progress` `in_queue=1` | **No private DB read** was permitted; no persisted-progress-after-answer observation | `VERIFIED_STATIC` only | `UNKNOWN` for persisted row |

## Explicitly NOT claimed
- No M06 emulator screenshots, XML dumps, logcat, `dumpsys` or device state were collected.
- No server response body was observed. `SERVER CONFIRMED = 0`.
- No offline reconnect was demonstrated (`svc wifi enable`/`svc data enable` did not
  restore connectivity in M05 runs 002/003).
''',encoding='utf-8')
(RT/'NO_NEW_RUN_JUSTIFICATION.md').write_text('''# Why M06 deliberately ran no new emulator experiment

1. **Local capability** — the sandbox has no emulator, ADB, Android SDK, Java or KVM.
   Runtime host facts in this repository come from GitHub Actions (M03/M04/M05).
2. **Hypotheses resolved statically** — the specific M06 questions (which field
   `isSolvedCorrectly` reads; what `createLessonProgress` writes; how each interaction
   validates; whether `solvedContent` suffices; what the offline gate is) are decidable
   from DEX bytecode and were answered `VERIFIED_STATIC`. A screenshot cannot prove a
   register read.
3. **Standing constraint** — M05 established that the only way to reach an answer screen
   is the deterministic exact 24-tap chain of run `42003884423`; a repeat without that
   exact replay was ruled out. Repeating UI screenshots was explicitly excluded.
4. **The one remaining runtime hypothesis** — reading `lesson_progress` after a correct
   answer — requires root / private app-database extraction, which is forbidden.
5. **Backend boundary** — server response bodies, scoring/economy awards and remote code
   execution were deliberately out of scope; no workflow dispatch was made.

Therefore M06 reused M05 runs 001–005 with explicit `VERIFIED_RUNTIME` / `VERIFIED_BOTH`
classification in `M06_HYPOTHESIS_CORRELATION.md` and recorded the correct-answer state,
persisted-progress-after-answer and server responses as `UNKNOWN` in
`../18_OPEN_QUESTIONS.md`. `SERVER CONFIRMED = 0`.
''',encoding='utf-8')
# ---------- main README ----------
files=sorted(p.name for p in R.glob('*.md'))
(R/'README.md').write_text('''# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING (Mimo Android 9.35)

**APK:** `@@APK@@`, 142,353,499 bytes, **unchanged**.  
**Baseline:** `d0714b40` ("MISSION 05 FINAL…") · **branch** `arena/aebb90b7-game`.  
**Method:** read-only Androguard 4.1.4 disassembly of all 12 original `classes*.dex`
+ verbatim shipped assets. No APK modification, no emulator root, no auth/purchase work,
no TLS/pinning bypass, no backend reconstruction.  
**`SERVER CONFIRMED = 0`.**

## What this mission adds
M05 left several behavioural gaps because the JADX archive had `Method not decompiled`
stubs. M06 went to the DEX bytecode and closed them:

- **`isSolvedCorrectly()` = `tries >= 1`**, not `attempts >= 1` (M05 correction).
- Exact 11-column `createLessonProgress` record construction.
- All answer validators (fillTheGap, selection, spell, validatedInput, WebView activity,
  executable `solvedContent` comparison) with pseudocode.
- XML DSL parser technology: `org.xmlpull.v1.XmlPullParserFactory`, six module parsers,
  nine renderer types.
- Exact asset locale paths, `NetworkUtils` offline gate, offline chapter-end fallback,
  `AnswersInChapter` counting formula.
- 173 R8 class mappings, 596 method hints, 12,851-method catalog, 82 full class dumps,
  9 real call graphs, 22 dossiers, 11 byte-exact original samples.

Everything still unresolved is listed with a class/method/offset pointer in
`18_OPEN_QUESTIONS.md` and the matrix in `19_REVERSE_ENGINEERING_COVERAGE.md`.
`INFERRED` and `UNKNOWN` are never presented as confirmed.

## Reports (19)
'''+''.join('- `%s`\n'%f for f in files if f[:2].isdigit() and f!='00_INVESTIGATION_PLAN.md')+'''
## Supporting deliverables
`01_EXECUTIVE_SUMMARY.md` · `MISSION_06_REVIEW.md` · `EVIDENCE_DATABASE.json`
(113 classified entries) · `DIAGRAMS/` (9 Mermaid) · `CALL_GRAPHS/` (9 `.mmd` + 9 `.json`,
622 real invoke edges) · `METHOD_DOSSIERS/` (22) · `EVIDENCE/` (82 `.smali.txt` dumps,
derived disassembly, toolchain, deobfuscation notes) · `SCHEMAS/` (5 JSON) ·
`SAMPLES/` (11 byte-exact APK members + `MANIFEST.json`) · `RUNTIME_EVIDENCE/`
(M05 correlation + no-new-run justification).

## Classification vocabulary
`VERIFIED_STATIC` (read from DEX/assets) · `VERIFIED_RUNTIME` (M04/M05 emulator evidence) ·
`VERIFIED_BOTH` · `INFERRED` · `UNKNOWN`.

## Reproduce
`/home/user/_work/m06/venv/bin/python` with `EVIDENCE/M06_DEX_HARNESS.py`,
`M06_EXPORT_CATALOG.py`, `M06_METHOD_NAME_MAP.py`; no network needed.
'''.replace('@@APK@@',APK),encoding='utf-8')
# ---------- review ----------
(R/'MISSION_06_REVIEW.md').write_text('''# MISSION 06 — FINAL REVIEW

## Acceptance criteria
| Criterion | Status |
|---|---|
| 19 numbered reports | ✅ `01_…` … `19_…` |
| ≥9 architecture diagrams | ✅ 9 Mermaid in `DIAGRAMS/` |
| Real call graphs from xrefs | ✅ 9 `.mmd` + 9 `.json`, 622 real invoke edges |
| Method dossiers with fields/state/callers/callees | ✅ 22 |
| Original samples preserved | ✅ 11 byte-exact APK members + SHA-256 manifest |
| Targeted runtime evidence | ✅ M05 correlation + explicit no-new-run justification (no repeat screenshots) |
| Evidence DB with classification + evidence fields | ✅ 113 entries |
| Coverage matrix per component/state/flow | ✅ `19_REVERSE_ENGINEERING_COVERAGE.md`, 35 rows |
| Scripts/toolchain with exact failure records | ✅ `02_METHODOLOGY_AND_TOOLCHAIN.md`, `EVIDENCE/M06_*.py` |
| M05 doc-by-doc evidence review | ✅ `17_CORRECTIONS_AND_LIMITATIONS.md` C-1..C-8 + `SCHEMAS/CONTENT_SCHEMA_M06.json` |
| No backend / server reconstruction | ✅ `SERVER CONFIRMED = 0` everywhere |
| Root/private DB/auth bypass forbidden | ✅ none performed |
| Original APK unchanged | ✅ SHA-256 `%s` |

## Classification totals (EVIDENCE_DATABASE.json)
%s

## Headline corrections to M05
1. `LessonProgress.isSolvedCorrectly()` reads **`tries`**, not `attempts`.
2. `validatedInput` matching is a client-side normalizer, not an opaque server check.
3. `executableFiles` correctness compares user code to shipped `solvedContent`.
4. Lesson DSL is XML parsed by `XmlPullParser`, not an unknown custom parser.
5. Nine interaction types, not six.

## Deliberately unresolved (not failures)
Correct-answer runtime UI, persisted row after answer, server response bodies, absolute
XP/keys/coins/streak/daily-goal formulas, exact unlock boolean combination, full
`SingleChoice`/`MultipleChoice`/`Reveal` dispatch, `W()` and `d0()` details, remote code
execution, native JNI surface. Each has an exact pointer in `18_OPEN_QUESTIONS.md`.

## QA performed
- `EVIDENCE_DATABASE.json` parses; all referenced workspace file paths resolve.
- All 82 disassembly dumps + both catalogs regenerated with corrected xref cache.
- All 9 call-graph JSONs parse and each edge has `caller`, `callee`, `opcode`.
- All 11 samples match the APK member bytes (SHA-256 in `MANIFEST.json`).
- `SCHEMAS/*.json` parse; `CONTENT_SCHEMA_M06.json` keys are verbatim shipped/DEX strings.
- Original APK SHA-256 unchanged; `ANALYSIS/_INPUT/classes*.dex` untouched.
- `ANALYSIS/EVIDENCE_INDEX.json` extended with `mission_06_append` without mutating the
  336 M01–M04 entries or the M02/M05 appends.

## Bottom line
M06 reconstructed **how the client actually validates answers, records progress, renders
shipped lessons and behaves offline**, from real bytecode, with every uncertain point
labelled. It did not invent a backend, a content format, or a scoring formula.
'''%(APK,json.dumps(DB['classification_counts'],indent=1)),encoding='utf-8')
# ---------- append to global evidence index (preserve existing verbatim) ----------
GI=A/'EVIDENCE_INDEX.json';g=json.loads(GI.read_text())
g['mission_06_append']=dict(
 document='MISSION 06 — deep client reverse engineering (M01–M05 entries preserved verbatim)',
 database='ANALYSIS/MISSION_06/EVIDENCE_DATABASE.json',
 classification_vocabulary=dict(VERIFIED_STATIC='read directly from DEX bytecode / verbatim shipped APK assets',
   VERIFIED_RUNTIME='observed in M04/M05 GitHub Actions emulator evidence (cross-referenced)',
   VERIFIED_BOTH='both of the above',INFERRED='named interpretation of verified bytecode',
   UNKNOWN='insufficient evidence; no claim made'),
 server_confirmed=0,
 counts=dict(total=DB['total'],**DB['classification_counts']),
 evidence=[dict(id=e['id'],claim=e['claim'],classification=e['classification'],
   topic=e['topic'],source_path=e['evidence'].get('file') or e['evidence'].get('dir') or
   e['evidence'].get('method_signature') or 'ANALYSIS/MISSION_06/',
   method_signature=e['evidence'].get('method_signature'),
   dex=e['evidence'].get('dex'),code_offset=e['evidence'].get('code_offset')) for e in DB['entries']],
 note='M06 adds 113 entries. The original 336 M01–M04 entries, mission_02_append and mission_05_append are unchanged. No new emulator run; runtime claims explicitly cross-reference M05.')
GI.write_text(json.dumps(g,indent=1,ensure_ascii=False),encoding='utf-8')
print('wrote support files; index append',len(g['mission_06_append']['evidence']))
