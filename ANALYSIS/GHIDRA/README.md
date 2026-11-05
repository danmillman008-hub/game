# Ghidra / REA chain — corrected run

- run 41940704898 / commit af47e90632ec622712a82531c6ebff5b5bb0b427 / 2026-11-05T00:25:54Z
- Ghidra fetch: success; coverage: success; auto analysis: success; REA doctor: success
- corrections applied: ALL 12 DEX imported (not 3); Auto Analysis ENABLED on ALL 12 DEX (no -noanalysis); full JDK 21 for REA separate from JDK 25 for Ghidra

## All-12 DEX coverage
```
DEX classes.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=36707 functions=0 image_base=00000000
DEX classes10.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=10 functions=0 image_base=00000000
DEX classes11.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=10 functions=0 image_base=00000000
DEX classes12.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=451 functions=0 image_base=00000000
DEX classes2.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=41371 functions=0 image_base=00000000
DEX classes3.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=12170 functions=0 image_base=00000000
DEX classes4.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=10 functions=0 image_base=00000000
DEX classes5.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=10 functions=0 image_base=00000000
DEX classes6.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=10 functions=0 image_base=00000000
DEX classes7.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=10 functions=0 image_base=00000000
DEX classes8.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=10 functions=0 image_base=00000000
DEX classes9.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=10 functions=0 image_base=00000000
```

## Control flow / function report
```
=== PROGRAM classes.dex language=Dalvik:LE:32:DEX_KitKat functions=54530 symbols=681976 memory_blocks=3 ===
-- target namespace inventory (all matching symbols, capped) --
  SYM EXTERNAL.dex-3774::android::view::MotionEvent::getXPrecision @EXTERNAL:000009f1
  SYM EXTERNAL.dex-5161::android::widget::ProgressBar::setProgress @EXTERNAL:00000f58
  SYM EXTERNAL.dex-5162::android::widget::ProgressBar::setProgressBackgroundTintList @EXTERNAL:00000f59
  SYM EXTERNAL.dex-5163::android::widget::ProgressBar::setProgressDrawable @EXTERNAL:00000f5a
  SYM EXTERNAL.dex-5164::android::widget::ProgressBar::setProgressTintList @EXTERNAL:00000f5b
  SYM EXTERNAL.dex-31571::com::getmimo::data::source::remote::progress::CompletionApi::getLastInteractedTrack @EXTERNAL:0000143a
  SYM EXTERNAL.dex-31572::com::getmimo::data::source::remote::progress::CompletionApi::getTrackCompletion @EXTERNAL:0000143b
  SYM EXTERNAL.dex-31573::com::getmimo::data::source::remote::progress::LessonProgressApi::postProgress @EXTERNAL:0000143c
  SYM EXTERNAL.dex-35596::com::getmimo::ui::leaderboard::LeaderboardResultItemState::a @EXTERNAL:0000144e
  SYM EXTERNAL.dex-35597::com::getmimo::ui::leaderboard::LeaderboardResultItemState::b @EXTERNAL:0000144f
  SYM EXTERNAL.dex-35598::com::getmimo::ui::leaderboard::LeaderboardResultItemState::c @EXTERNAL:00001450
  SYM EXTERNAL.dex-35599::com::getmimo::ui::leaderboard::LeaderboardResultItemState::e @EXTERNAL:00001451
  SYM EXTERNAL.dex-35600::com::getmimo::ui::leaderboard::LeaderboardResultItemState::f @EXTERNAL:00001452
  SYM EXTERNAL.dex-35601::com::getmimo::ui::leaderboard::LeaderboardResultItemState::g @EXTERNAL:00001453
  SYM EXTERNAL.dex-35602::com::getmimo::ui::leaderboard::LeaderboardResultItemState::h @EXTERNAL:00001454
  SYM EXTERNAL.dex-39302::com::getmimo::ui::streaks::ArcProgressView::setProgress @EXTERNAL:00001465
  SYM EXTERNAL.dex-39303::com::getmimo::ui::streaks::DailySparksGoalProgressView::setSparkProgress @EXTERNAL:00001466
  SYM EXTERNAL.dex-39305::com::getmimo::ui::streaks::bottomsheet::StreakBottomSheetViewModel$fetchProfileData$1::<init> @EXTERNAL:00001467
  SYM EXTERNAL.dex-39316::com::getmimo::ui::streaks::bottomsheet::a::<init> @EXTERNAL:00001468
  SYM EXTERNAL.dex-39317::com::getmimo::ui::streaks::bottomsheet::a::w0 @EXTERNAL:00001469
  SYM EXTERNAL.dex-39376::com::getmimo::ui::widget::StreakWidgetRefreshWorker$doWork$1::<init> @EXTERNAL:00001484
  SYM EXTERNAL.dex-39709::com::google::android::gms::tasks::TaskCompletionSource::<init> @EXTERNAL:0000158b
  SYM EXTERNAL.dex-39710::com::google::android::gms::tasks::TaskCompletionSource::getTask @EXTERNAL:0000158c
  SYM EXTERNAL.dex-39711::com::google::android::gms::tasks::TaskCompletionSource::setException @EXTERNAL:0000158d
  SYM EXTERNAL.dex-39712::com::google::android::gms::tasks::TaskCompletionSource::setResult @EXTERNAL:0000158e
  SYM EXTERNAL.dex-39713::com::google::android::gms::tasks::TaskCompletionSource::trySetException @EXTERNAL:0000158f
  SYM EXTERNAL.dex-39714::com::google::android::gms::tasks::TaskCompletionSource::trySetResult @EXTERNAL:00001590
  SYM EXTERNAL.dex-45155::gt::d::setProgress @EXTERNAL:00001967
  SYM EXTERNAL.dex-51137::kotlinx::coroutines::d::invokeOnCompletion @EXTERNAL:000022a6
  SYM EXTERNAL.dex-57189::ra0::b1::invokeOnCompletion @EXTERNAL:00002649
  SYM string_data::_does_not_match_a_known_view_type_in_LeaderboardAdapter! @0000159c
  SYM string_data::_fetch_completion_handlers. @00001610
  SYM string_data::$updatedLessonProgress @0000206c
  SYM string_data::(()_=>_{_____const_id_=_'mimo-android-completion-badge-style';_____if_(document.getElementById(id))_return;_____const_style_=_document.createElement('style');_____style.id_=_id;_____style.textContent_=_`_________.cm-completionIcon-text_{_flex-shrink:_0;_}_________.cm-completionIcon-text::after_{_____________display:_inline-block;_____________transform:_scale(0.5);_____________transform-origin:_left_center;_________}_____`;_____document.head.appendChild(style);_})() @000022c8
  SYM string_data::()Lcom/getmimo/core/model/streak/Streak; @000024a8
  SYM string_data::()Lcom/getmimo/data/model/leaderboard/Leaderboard; @000024e8
  SYM string_data::()Lcom/getmimo/data/model/leaderboard/LeaderboardUserResult; @000024ec
  SYM string_data::()Lcom/getmimo/data/model/publicprofile/ProfileLeaderboardInfo; @000024f4
  SYM string_data::(III)Lcom/getmimo/data/model/leaderboard/LeaderboardLeague; @0000270c
  SYM string_data::(JLjava/lang/String;ILjava/lang/String;I)Lcom/getmimo/data/model/reward/Reward; @00002a10
  SYM string_data::(Lcom/getmimo/core/model/streak/Streak;Lcom/getmimo/core/model/streak/Streak;Ljava/util/List;)V @00003010
  SYM string_data::(Lcom/getmimo/data/model/leaderboard/Leaderboard;)V @0000309c
  SYM string_data::(Lcom/getmimo/data/model/leaderboard/LeaderboardUserResult;Z)V @000030a0
  SYM string_data::(Lcom/getmimo/data/model/reward/Reward;)V @000030ac
  SYM string_data::(Lcom/getmimo/data/model/room/LessonProgress;Z)V @000030b0
  SYM string_data::(Lcom/getmimo/data/model/room/LessonProgress;ZZLd70/b;)Ljava/lang/Object; @000030b4
  SYM string_data::(Lcom/getmimo/data/source/remote/progress/LessonProgressApi;Lye/g;Lye/c;Lnp/d;Lri/d;Lcom/getmimo/data/source/local/completion/a;Lcg/a;)V @000030e4
  SYM string_data::(Lcom/getmimo/ui/lesson/interactive/LessonBundle;Lorg/joda/time/Instant;II)Lcom/getmimo/data/model/room/LessonProgress; @0000310c
  SYM string_data::(Ljava/lang/String;Ljava/lang/Integer;Ljava/lang/Integer;Ljava/lang/String;)Lcom/getmimo/core/model/streak/UserActivity; @00003350
  SYM string_data::(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;ZJIIIIIZLcom/getmimo/data/model/publicprofile/ProfileLeaderboardInfo;Ljava/util/List;Lcom/getmimo/core/model/inapp/Subscription$Type;)V @000033cc
  SYM string_data::(Lra0/y;)Lcom/getmimo/core/model/coins/Coins; @00003638
  SYM string_data::(Lra0/y;)Lcom/getmimo/data/model/leaderboard/LeaderboardUserResult; @0000365c
  SYM string_data::(Lvn/p;ILcom/getmimo/core/model/coins/Coins;Lvn/r;Z)Lvn/q; @00003770
  SYM string_data::(Lze/a;Lcom/getmimo/data/source/remote/progress/LessonProgressRepository;)V @000037e8
  SYM string_data::,_activeStreakLength= @00003b5c
  SYM string_data::,_bestStreak= @00003c94
  SYM string_data::,_coins= @00003eb8
  SYM string_data::,_createLessonProgressWhenSwiping= @00003fb4
```

## run.log tail
```
INFO  IMPORTING: file:///home/runner/work/game/game/ANALYSIS/_INPUT/classes9.dex (HeadlessAnalyzer)  
INFO  Using Loader: Dalvik Executable (DEX) (ProgramLoader)  
INFO  Using Language/Compiler: Dalvik:LE:32:DEX_KitKat:default (ProgramLoader)  
INFO  Using Library Search Path: [., /bin, /lib, /lib64, /lib/x86_64-linux-gnu, /lib/aarch64-linux-gnu, /usr/bin, /usr/lib, /usr/X11R6/bin, /usr/X11R6/lib, /usr/java/packages/lib, /usr/lib64] (ProgramLoader)  
INFO  IMPORTING: Loaded 0 additional files (HeadlessAnalyzer)  
WARN  Analyzer 'Apply Data Archives' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Basic Constant Reference Analyzer' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Data Reference' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Call Convention ID' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Decompiler Switch Analysis' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Embedded Media' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Non-Returning Functions - Discovered' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Demangler GNU' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Reference' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Source Language Support' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Create Address Tables' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Call-Fixup Installer' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Call-Fixup Installer' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Disassemble Entry Points' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Subroutine References' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'External Entry References' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Subroutine References' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Shared Return Calls' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Shared Return Calls' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Stack' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'ASCII Strings' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Variadic Function Signature Override' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Function ID' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
INFO  ANALYZING all memory and code: file:///home/runner/work/game/game/ANALYSIS/_INPUT/classes9.dex (HeadlessAnalyzer)  
INFO  REPORT: Analysis succeeded for file: file:///home/runner/work/game/game/ANALYSIS/_INPUT/classes9.dex (HeadlessAnalyzer)  
INFO  REPORT: Execute script: MimoControlFlow.java  (HeadlessAnalyzer)  
INFO  SCRIPT: /home/runner/work/game/game/ANALYSIS/_TOOLCHAIN/ghidra_scripts/MimoControlFlow.java (HeadlessAnalyzer)  
INFO  MimoControlFlow.java> === PROGRAM classes9.dex language=Dalvik:LE:32:DEX_KitKat functions=3 symbols=69 memory_blocks=3 ===
-- target namespace inventory (all matching symbols, capped) --
  [target_symbols_shown=0]
-- target function control flow (real Dalvik instructions) --
SCANNED_FUNCS=3 BRANCH_INSNS_FIRST_8000_FUNCS=0 INVOKE_INSNS_FIRST_8000_FUNCS=3 PATH_MAP_FUNCS_DUMPED=0 SCORING_FUNCS_DUMPED=0 INSTRUCTIONS_SHOWN=0
 (GhidraScript)  
INFO  ANALYZING changes made by post scripts: file:///home/runner/work/game/game/ANALYSIS/_INPUT/classes9.dex (HeadlessAnalyzer)  
INFO  REPORT: Post-analysis succeeded for file: file:///home/runner/work/game/game/ANALYSIS/_INPUT/classes9.dex (HeadlessAnalyzer)  
INFO  /classes9.dex: file created (runner) (LocalFileSystem)  
INFO  REPORT: Save succeeded for: /classes9.dex (Mimo935Analysis:/classes9.dex) (HeadlessAnalyzer)  
INFO  REPORT: Import succeeded (HeadlessAnalyzer)  
auto_headless_exit=0
JAVA_HOME(REA)=/opt/hostedtoolcache/Java_Temurin-Hotspot_jdk/21.0.13-9/x64
JDK25_HOME(Ghidra)=/opt/hostedtoolcache/Java_Temurin-Hotspot_jdk/25.0.5-8/x64
java --list-modules | grep jdk.compiler:
jdk.compiler@21.0.13
rea_doctor_exit=0
{"healthy":true,"environment_healthy":false,"scope":{"mode":"explicit","clients":[],"providers":["jadx"],"skill":false,"target":null},"scope_checks":[{"name":"node","ok":true,"classification":"healthy","detail":"22.23.4","details":{"runtime":"node","version":"22.23.4"}},{"name":"jadx","ok":true,"classification":"healthy","detail":"JADX MCP bridge JAR validated at /home/runner/work/_temp/jadx-headless-mcp.jar; its path is recorded for agent registrations. This checks configuration, not whether a selected APK fits in the worker's memory.","details":{"operation_timeout_ms":120000}}],"informational_checks":[{"name":"host","ok":true,"classification":"healthy","detail":"ubuntu 24.04"},{"name":"hopper","ok":false,"classification":"missing_analysis_engine","remediation":"Run rea setup to install Hopper, or set HOPPER_LAUNCHER_PATH."},{"name":"ghidra","ok":true,"classification":"healthy","detail":"/home/runner/work/_temp/ghidra_dist/ghidra_12.2_PUBLIC"},{"name":"ghidra-platform","ok":true,"classification":"healthy","detail":"linux"},{"name":"ghidra-architecture","ok":true,"classification":"healthy","detail":"x64"},{"name":"ghidra-installation","ok":true,"classification":"healthy","detail":"/home/runner/work/_temp/ghidra_dist/ghidra_12.2_PUBLIC/Ghidra/application.properties"},{"name":"ghidra-version","ok":false,"classification":"config_drift","detail":"12.2; accepted releases are 12.1.x (verified build 12.1.4)","remediation":"Install a Ghidra 12.1.x release (verified with 12.1.4), or update REA for another Ghidra line."},{"name":"ghidra-headless","ok":true,"classification":"healthy","detail":"/home/runner/work/_temp/ghidra_dist/ghidra_12.2_PUBLIC/support/analyzeHeadless"},{"name":"ghidra-native_decompiler","ok":true,"classification":"healthy","detail":"/home/runner/work/_temp/ghidra_dist/ghidra_12.2_PUBLIC/Ghidra/Features/Decompiler/os/linux_x86_64/decompile reports elf x86_64, which matches linux/x64"},{"name":"ghidra-java","ok":false,"classification":"config_drift","detail"```
