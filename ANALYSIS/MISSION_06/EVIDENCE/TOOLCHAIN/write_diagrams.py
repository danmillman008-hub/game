import pathlib
D=pathlib.Path('/home/user/game/ANALYSIS/MISSION_06/DIAGRAMS');D.mkdir(parents=True,exist_ok=True)
H='''%% MISSION 06 — original Mimo 9.35 architecture, reconstructed from DEX bytecode.
%% APK sha256 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
%% Classification of each node is in the corresponding numbered report and EVIDENCE_DATABASE.json.
%% Solid edges = VERIFIED_STATIC invoke/field xref; dashed = INFERRED or client-side boundary.
'''
files={
'01_full_architecture.mmd':H+'''flowchart TB
  subgraph APK["APK assets (shipped, offline)"]
    A1["assets/lessons-&lt;locale&gt;/tracks/tracks.json<br/>v753, 19 tracks"]
    A2["assets/lessons-&lt;locale&gt;/tracks/tutorial-&lt;id&gt;.json<br/>1029 tutorials / 18272 lessons"]
    A3["assets/lesson-webview.js<br/>assets/lessons-common/icons"]
    A4["classes*.dex × 12<br/>29454 classes / 129071 methods"]
    A5["lib/*.so × 12 (arm64-v8a)"]
  end
  subgraph LOAD["Content layer"]
    L1["Lye/b; AssetsTracksLoader<br/>AssetManager.open"]
    L2["Lye/d; local-files variant"]
    L3["tracks/b; DefaultTrackLoader<br/>UTF-8 readText + kotlinx.serialization"]
    L4["tracks/c; DefaultTracksRepository<br/>loadTrackWithChapters"]
    L5["Lte/c; DSL LessonParser<br/>XmlPullParserFactory"]
    L6["Lte/a,d,e,b,f,g module parsers"]
  end
  subgraph DOMAIN["Domain / interactors"]
    D1["LessonContent$Interactive<br/>lessonModules / hardModeLessonModules"]
    D2["LessonBundle (Parcelable)<br/>ids + tutorial/chapter type"]
    D3["Lgm/h; LessonInteractionType mapper<br/>9 renderer types"]
    D4["GetPathMapState / CompletionRepository<br/>CanOpenChapterWithKeys"]
    D5["LessonProgressQueue / LessonProgressRepository"]
  end
  subgraph UI["UI layer (Fragments / ViewModels / Orbit MVI)"]
    U1["MainActivity / SplashActivity_default"]
    U2["PathMapFragment + PathMapViewModel"]
    U3["ChapterActivity + ChapterViewModel"]
    U4["InteractiveLessonFragment + InteractiveLessonViewModel"]
    U5["base/c; InteractiveLessonBaseViewModel"]
    U6["per-interaction ViewModels<br/>fillTheGap, selection, spell, validatedInput, webview"]
    U7["NonInteractiveLessonFragment"]
    U8["ExecutableLessonViewModel (q)<br/>CodeEditViewModel / CodePlayground"]
    U9["ChapterFinishedViewModel / screens"]
  end
  subgraph STORE["Local persistence"]
    S1["Room lesson_progress (in_queue)"]
    S2["Room chapter_completions / tutorial_completions"]
    S3["DataStore / SharedPreferences<br/>hard mode, first run, daily goal"]
    S4["in-memory StateFlow / LiveData"]
    S5["LessonProgressQueue (unsynced)"]
  end
  subgraph EXT["Client-side boundary (NOT reconstructed)"]
    X1["Retrofit LessonProgressApi POST progress"]
    X2["runFiles / code execution endpoints"]
    X3["user / streak / keys / ETA endpoints"]
    X4["AiTutor / analytics / Remote Config"]
  end
  A1 --> L1 --> L3 --> L4 --> D1
  A2 --> L1
  A3 -.-> U6
  A4 -.-> LOAD
  A4 -.-> DOMAIN
  A4 -.-> UI
  A5 -.-> U1
  D1 --> L5 --> L6 --> D1
  D1 --> D3 --> U4 --> U5 --> U6
  D2 --> U5
  U1 --> U2 --> U3 --> U4
  U3 --> U9
  U4 --> U8
  U5 --> D5 --> S1 --> S5
  D4 --> S1
  D4 --> S2
  D4 --> S3
  D4 --> S4
  S5 -.->|"networkUtils.a() gate"| X1
  U8 -.-> X2
  U9 -.-> X3
  U6 -.-> X4
  U5 -.-> X4
''',
'02_class_dependency.mmd':H+'''flowchart LR
  DI["Lhm/b; DI container<br/>13 Object slots"]
  DI --> VM["base/c; InteractiveLessonBaseViewModel"]
  VM --> REPO["LessonProgressRepository"]
  VM --> QUEUE["LessonProgressQueue"]
  VM --> ANALYTICS["analytics/a;"]
  VM --> SOUND["lesson/sound/a;"]
  VM --> PREFS["data/local/a; DataStore prefs"]
  VM --> FILES["mf/a; filesDir"]
  REPO --> API["LessonProgressApi (Retrofit)"]
  REPO --> DAO["cg/a; LessonProgressDao"]
  REPO --> TRACKS["tracks/c; DefaultTracksRepository"]
  REPO --> COMPLETION["completion/a; CompletionRepository"]
  REPO --> NET["network/a; NetworkUtils"]
  DAO --> ROOM["Room lesson_progress"]
  QUEUE --> DEVMENU["ze/a; dev menu storage"]
  VM --> BUNDLE["LessonBundle (Parcelable)"]
  VM --> CONTENT["LessonContent$Interactive"]
  CONTENT --> MODULES["LessonModule sealed classes"]
  VM --> BASEFRAG["base/b; InteractiveLessonBaseFragment"]
  BASEFRAG --> CHILD["fillthegap/a, selection/a, spell/a,<br/>validatedinput(Lqm/d), webview/c"]
  CHILD --> VM
  BASEFRAG --> RUN["RunButton / InteractionKeyboard"]
  VM --> LIVEDATA["m0 LiveData + kotlinx StateFlow"]
  VM --> COROUTINE["ra0/z; coroutine launchers"]
''',
'03_content_pipeline.mmd':H+'''flowchart TD
  A["APK assets/lessons-&lt;locale&gt;/tracks/"] --> B["ContentLocale enum<br/>ru en es pt de fr it id tr pl"]
  B --> C["Lye/b;&lt;clinit&gt; builds<br/>locale → 'lessons-&lt;lang&gt;/tracks'"]
  C --> D{"which file?"}
  D -->|"tracks.json"| E["Lye/b;-&gt;d() AssetManager.open"]
  D -->|"tutorial-&lt;id&gt;.json"| F["Lye/b;-&gt;b(J) AssetManager.open"]
  E --> G["DefaultTrackLoader.a(J,I,I)<br/>BufferedReader UTF-8 readText"]
  F --> G
  G --> H["kotlinx.serialization Json.decodeFromString<br/>TracksJson / TutorialJson / LessonContent DTO"]
  H --> I["string field 'content' = XML-like lesson DSL"]
  I --> J["Lte/c;-&gt;b(String)<br/>XmlPullParserFactory.newInstance()<br/>setNamespaceAware(true)"]
  J --> K{"START_TAG name"}
  K -->|p| K1["Lte/d;-&gt;a → LessonModule$Paragraph"]
  K -->|code| K2["Lte/a;-&gt;a → LessonModule$Code<br/>interactions/options/output"]
  K -->|selection| K3["Lte/e;-&gt;a → LessonModule$Selection"]
  K -->|img| K4["Lte/c;-&gt;a → LessonModule$Image"]
  K -->|webview| K5["Lte/g;-&gt;a → LessonModule$Webview"]
  K -->|database| K6["Lte/b;-&gt;a → LessonModule$Database"]
  K -->|html/body/unknown| K7["skip + xml_parse_error_module"]
  K1 --> L["List&lt;LessonModule&gt; with ModuleVisibility<br/>ALWAYS / CORRECT / WRONG"]
  K2 --> L
  K3 --> L
  K4 --> L
  K5 --> L
  K6 --> L
  L --> M["Lgm/h;-&gt;a(List) → LessonInteractionType<br/>9 possible renderer types"]
  M --> N["InteractiveLessonViewModel.E()<br/>Lgm/g state → LiveData"]
  N --> O["base/c;-&gt;O() filters ALWAYS modules,<br/>jm/j paragraph, jm/i image, jm/k webview"]
  O --> P["RecyclerView / Compose renderer<br/>+ CodeBodyView / DatabaseView"]
''',
'04_lesson_execution.mmd':H+'''flowchart TD
  START["ChapterActivity → InteractiveLessonFragment"] --> BUNDLE["LessonBundle (Parcelable)<br/>lessonId, chapterIndex, tutorialId,<br/>trackId, tutorialType, chapterType,..."]
  BUNDLE --> VM["InteractiveLessonViewModel.E()"]
  VM --> TYPE["Lgm/h.a(lessonModules)<br/>LessonInteractionType"]
  TYPE --> CHOOSE{"type"}
  CHOOSE -->|"FillTheGap"| V1["fillthegap/a;"]
  CHOOSE -->|"Selection / SingleChoice / MultipleChoice"| V2["selection/a;"]
  CHOOSE -->|"Spell"| V3["spell/a;"]
  CHOOSE -->|"ValidatedInput"| V4["Lqm/d;"]
  CHOOSE -->|"InteractiveWebView"| V5["webview/c;"]
  CHOOSE -->|"None / Reveal"| V6["nointeraction/a;"]
  V1 --> SETUP["base/c;-&gt;O() initialiseViewModel<br/>module visibility filter → render items"]
  V2 --> SETUP
  V3 --> SETUP
  V4 --> SETUP
  V5 --> SETUP
  V6 --> SETUP
  SETUP --> INPUT["user edits tokens / types code / taps options"]
  INPUT --> RUN["Run button → Fragment E0()"]
  RUN --> BOOL["boolean isCorrect"]
  BOOL --> Y["base/c;-&gt;Y(isCorrect)<br/>guard LiveData f == TRUE"]
  Y --> COR["onLessonRun$1.invokeSuspend"]
  COR -->|"true"| VC["V() lessonSolvedCorrectly"]
  COR -->|"false"| XC["X() lessonSolvedIncorrectly"]
  VC --> FB["solutionFeedbackCorrect + sound.a(true)"]
  XC --> FW["d0() showWrongFeedbackBlock<br/>solutionFeedbackWrong / Try again"]
  VC --> H["H(tries, attempts) → createLessonProgress"]
  XC --> H
  H --> E0["e0() storeLessonProgressInMemory<br/>→ LessonProgressQueue → Room"]
  VC --> NAV["e LiveData = chapterIndex<br/>→ next lesson / chapter end"]
''',
'05_interaction_validation.mmd':H+'''flowchart TD
  subgraph FTG["fillTheGap"]
    F1["Interaction$FillTheGap.c List&lt;Option&gt;<br/>Option{isCorrect,text,startIndex,endIndex}"]
    F1 --> F2["correctTokens = options.filter{isCorrect}<br/>in content order"]
    F1 --> F3["state.c = user-filled tokens"]
    F3 --> F4["selected = state.c.filter{it.b}"]
    F4 --> F5{"selected.size == correctTokens.size<br/>AND every selected[i].text == correctTokens[i].text"}
    F5 -->|yes| OK["Y(true)"]
    F5 -->|no| NO["Y(false)"]
  end
  subgraph SEL["selection / single / multiple choice"]
    S1["Lsm/a;{b=selected, c=isCorrect}"] --> S2["Lkm/f;-&gt;b(list) = list.all{ it.b == it.c }"]
    S2 --> OK
    S2 --> NO
  end
  subgraph SPL["spell"]
    P1["state.c answer tokens vs state.b expected tokens"] --> P2{"size equal AND every<br/>token.a string equal"}
    P2 --> OK
    P2 --> NO
  end
  subgraph VIN["validatedInput"]
    V1["Lqm/d;-&gt;E() extracts expected =<br/>code.subSequence(startIndex,endIndex)"] --> V2["user text stored in field S by Lqm/b;"]
    V2 --> V3["Lqm/i;-&gt;a(String) normalize:<br/>toLowerCase(Locale.US); keep letters/digits<br/>and &lt; &gt; ( ) : { } , ."]
    V1 --> V3
    V3 --> V4{"normalize(user)==normalize(expected)?"}
    V4 -->|no| V5["Lqm/g; INCORRECT"]
    V4 -->|yes| V6{"user.equals(expected)?"}
    V6 -->|yes| V7["Lqm/e; CORRECT"]
    V6 -->|no| V8["Lqm/f; PARTIAL MATCH (user,expected)"]
    V5 --> V9["base/c;-&gt;Z(result)"]
    V7 --> V9
    V8 --> V9
    V9 --> V10["onValidatedInputExecuted$1 after delay(300)"]
    V10 -->|"Lqm/e"| VC2["V()"]
    V10 -->|"Lqm/f"| WC["W(partial) lessonSolvedCorrectlyWithPartialMatch"]
    V10 -->|"Lqm/g"| XC2["X()"]
  end
  OK --> ON["onLessonRun$1"]
  NO --> ON
''',
'06_progression_state_machine.mmd':H+'''stateDiagram-v2
  [*] --> Locked: path map item Lvn/e0
  Locked --> Unlocked: previous REQUIRED tutorial completed<br/>(GetPathMapState$invoke$3 walks backwards<br/>over last required item)
  Locked --> UnlockedButNoKeys: Lvn/h0 (pro chapter &amp; zero keys)
  UnlockedButNoKeys --> Unlocked: CanOpenChapterWithKeys / keys &gt; 0
  Unlocked --> InChapter: ChapterActivity
  InChapter --> LessonShown: InteractiveLessonViewModel.E()
  LessonShown --> WrongAnswer: X() lessonSolvedIncorrectly
  WrongAnswer --> LessonShown: retry (a0() lesson_reset)
  LessonShown --> CorrectAnswer: V() lessonSolvedCorrectly
  CorrectAnswer --> ProgressRecorded: H(tries=1,attempts=d)<br/>createLessonProgress → Room in_queue=1
  ProgressRecorded --> NextLesson: LiveData e = chapterIndex
  NextLesson --> LessonShown
  NextLesson --> ChapterEnd: last lesson
  ChapterEnd --> Completed: Lvn/d0 / chapter_completions
  Completed --> Unlocked: next tutorial in section
  note right of Locked
    VERIFIED_STATIC: state classes and dispatch in
    GetPathMapState$invoke$3 (659 insns @10129608).
    Exact boolean combination of isCompleted /
    hasProgress / proTier / keys is UNKNOWN.
  end note
''',
'07_persistence_flow.mmd':H+'''flowchart TD
  A["V()/X()/U()/W()"] --> B["base/c;-&gt;H(tries,attempts)"]
  B --> C["LessonProgressRepository.createLessonProgress<br/>LessonBundle + startedAt + tries + attempts"]
  C --> D["LessonProgress(11 fields)<br/>lessonId, completedAt=now, startedAt,<br/>tries, tutorialId, tutorialVersion, trackId,<br/>publishSetVersion, attempts,<br/>isPracticeProgress, inQueue=true"]
  D --> E["base/c;-&gt;e0() guard field M"]
  E --> F["LessonProgressQueue.storeLessonProgress"]
  F --> G{"devMenuStorage.e() ?"}
  G -->|"true (dev override)"| H["return, no write"]
  G -->|false| I["LessonProgressRepository.addOrUpdateLessonProgressInQueue"]
  I --> J["Room DAO → lesson_progress<br/>PK(lesson_id,tutorial_id)"]
  J --> K["updateCorrectAnswersCount()<br/>AnswersInChapter(correct=count isSolvedCorrectly,<br/>total=queued.size) → _answersInChapter StateFlow"]
  K --> L{"attempts == 1 ?"}
  L -->|yes| M["updateLessonStreakDetector"]
  J --> N["storeAndPostAllLessonProgress() on chapter end"]
  N --> O["moveLessonProgressFromQueue() → in_queue=0"]
  O --> P["postUnsyncedLessonProgress()"]
  P --> Q{"NetworkUtils.a()<br/>WIFI or CELLULAR transport?"}
  Q -->|false| R["log 'No internet connection, not posting unsynced lesson progress'<br/>throw NoConnectionException<br/>rows stay in Room"]
  Q -->|true| S["POST /v1/tutorials/{id}/progress (client boundary only)"]
  S --> T["sync result → chapter_completions / tutorial_completions"]
''',
'08_code_execution.mmd':H+'''flowchart TD
  A["lesson JSON executableContent<br/>instructions, preselectedFileIndex,<br/>hasVisualOutput, files[{name,codeLanguage,<br/>content,solvedContent}], hints"] --> B["DefaultTrackLoader$getExecutableLesson$2"]
  B --> C["LessonContent$Executable$File"]
  C --> D["ExecutableLessonViewModel (q)<br/>Orbit MVI container zl/z state"]
  D --> E["CodeEditViewModel / CodePlayground<br/>CodeFile{name, content}"]
  E --> F["user edits / Run"]
  F --> G["q;-&gt;I() executeLessonAndStoreProgress"]
  G --> H["userContents = files.map{getContent()}"]
  G --> I["solvedContents = executable.files.map{getSolvedContent()}"]
  H --> J{"userContents.equals(solvedContents) ?"}
  I --> J
  J -->|false| K["Ldm/h error state + IncorrectSolutionException"]
  J -->|true| L["q;-&gt;E() doOnLessonCorrectlySolved<br/>createLessonProgress(tries,attempts)"]
  L --> M["LessonProgressQueue → Room"]
  F --> N["q;-&gt;K() updateCodeExecutionState"]
  N --> O["client-side browser preview:<br/>Ldg/a; shipped HTML template<br/>lesson-webview.js bridge"]
  F -.->|"hasVisualOutput / external runner"| P["POST /v1/code/runfiles (client boundary only)"]
  K --> Q["retry / hints: q;-&gt;F() substitutes<br/>style.css / index.html / script.py / script.js<br/>from static Lcm/b maps"]
  note right of J
    VERIFIED_STATIC: q-&gt;I @10912932 compares
    ArrayList&lt;String&gt;.equals. Shipped solvedContent
    therefore suffices for the offline correctness check.
    Remote execution result handling is a client-side boundary.
  end note
''',
'09_offline_architecture.mmd':H+'''flowchart TB
  subgraph LOCAL["Fully local (works offline)"]
    A["APK assets curriculum v753<br/>10,298 JSON / 10 locales"]
    B["AssetManager.open + XmlPullParser + kotlinx.serialization"]
    C["lesson rendering, Run button, all 4+ interaction validators"]
    D["validatedInput normalizer / solvedContent comparison"]
    E["Room lesson_progress writes, in_queue=1"]
    F["AnswersInChapter StateFlow / streak detector"]
    G["DataStore prefs: hard mode, first run, onboarding"]
    H["lesson-webview.js + shipped HTML/CSS/JS assets"]
  end
  subgraph GATE["Client-side blocking gates"]
    I["NetworkUtils.a(): ConnectivityManager<br/>getActiveNetwork + hasTransport(WIFI|CELLULAR)"]
    J["LessonProgressRepository.postUnsyncedLessonProgress<br/>offline → NoConnectionException"]
    K["ChapterFinishedViewModel$handleOfflineState$1<br/>→ handleChapterAlreadyCompletedState (R)"]
    L["CanOpenChapterWithKeys / Lvn/h0 UnlockedButNoKeys"]
    M["M05 run-004/005: 'Connect to the internet to progress further'<br/>with local lesson content still visible"]
  end
  subgraph REMOTE["NOT reconstructed (server-owned boundary)"]
    N["POST progress sync / chapter &amp; tutorial completion"]
    O["runFiles remote code execution"]
    P["streak, XP, keys, coins, daily goal, ETA, rewards"]
    Q["AiTutor, Remote Config, analytics"]
  end
  A --> B --> C --> D --> E --> F
  G --> C
  H --> C
  F --> I
  I -->|false| J
  I -->|false| K
  I -.->|true| N
  L -.-> P
  M -.-> P
  K -.-> O
  Q -.-> C
  note right of GATE
    SERVER CONFIRMED = 0. No response bodies, no server
    business logic, no server DB in this mission.
  end note
''',
}
for n,c in files.items():
    (D/n).write_text(c,encoding='utf-8')
    print('wrote',n,len(c))
