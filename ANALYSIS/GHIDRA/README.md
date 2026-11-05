# Ghidra / REA chain — corrected run

- run 41940117221 / commit 610eb1c91e78777aec2adcc3af80c27ba1b836fd / 2026-11-05T00:19:35Z
- Ghidra fetch: success; coverage: success; auto analysis: success; REA doctor: success
- corrections applied: ALL 12 DEX imported (not 3); Auto Analysis ENABLED (no -noanalysis); full JDK 21 for REA separate from JDK 25 for Ghidra

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
-- namespace inventory (path map / chapter finished / progress) --
  SYM EXTERNAL.dex-3774::android::view::MotionEvent::getXPrecision @EXTERNAL:000009f1
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
  SYM EXTERNAL.dex-50988::kotlin::coroutines::jvm::internal::BaseContinuationImpl::invokeSuspend @EXTERNAL:00002211
  SYM string_data::_does_not_match_a_known_view_type_in_LeaderboardAdapter! @0000159c
  SYM string_data::$updatedLessonProgress @0000206c
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
  SYM string_data::,_currentStreakState= @00004020
  SYM string_data::,_dailyGoalCoinReward= @0000404c
  SYM string_data::,_dailyGoalCoinsReward= @00004050
  SYM string_data::,_dailyGoalRewardCoins= @00004054
  SYM string_data::,_dailyStreakDataList= @00004060
  SYM string_data::,_daysUntilNextWeekReward= @00004088
  SYM string_data::,_formattedSparks= @0000435c
  SYM string_data::,_hasFetchedLeaderboardAlready= @0000440c
  SYM string_data::,_invitationSubscriptionRewardDays= @000045c8
  SYM string_data::,_isStreakGoalReached= @0000471c
  SYM string_data::,_leaderboardChapterEndState= @000047ec
  SYM string_data::,_leaderboardFirstPlaceCount= @000047f0
  SYM string_data::,_leaderboardInfo= @000047f4
  SYM string_data::,_leaderboardSecondPlaceCount= @000047f8
  SYM string_data::,_leaderboardSize= @000047fc
  SYM string_data::,_leaderboardThirdPlaceCount= @00004800
```

## run.log tail
```
  505a0c60  const_4 v5,0x1
  505a0c62  invoke_static 0xc6da,v7
  505a0c68  const_4 v5,0x3
  505a0c6a  goto 0x505a0cbe
  505a0c6c  const_4 v5,0x6
  505a0c6e  const_string v5,0x9453
  505a0c72  move_object v3,v5
  505a0c74  invoke_static 0xf15a,v3
  505a0c7a  const_4 v5,0x3
  505a0c7c  const_4 v5,0x0
  505a0c7e  move v3,v5
  505a0c80  return_object v3
  505a0c82  const_4 v5,0x3
  505a0c84  invoke_static 0xc6da,v7
  505a0c8a  const_4 v5,0x6
  505a0c8c  iget_object v7,[v3:0x8b5]
  505a0c90  const_4 v5,0x6
  505a0c92  iget_object v7,[v7:0x8ee]
  505a0c96  const_4 v5,0x2
  505a0c98  if_eqz v7,0x505a0cbc
  505a0c9c  const_4 v5,0x7
  505a0c9e  iput_boolean v2,[v3:0x8b4]
  505a0ca2  const_4 v5,0x2
  505a0ca4  iget_object v1,[v3:0x8b6]
  505a0ca8  const_4 v5,0x3
  505a0caa  invoke_virtual 0x9dbd,v7,v1,v3
  505a0cb0  move_result_object v5
  505a0cb2  move_object v3,v5
  505a0cb4  if_ne v3,v0,0x505a0cbc
  505a0cb8  const_4 v5,0x6
  505a0cba  return_object v0
  505a0cbc  const_4 v5,0x2
  505a0cbe  sget_object v3,0xa878
  505a0cc2  const_4 v5,0x1
  505a0cc4  return_object v3
  [instructions_shown=45]
SCANNED_FUNCS=54530 BRANCH_INSNS=5678 INVOKE_INSNS=0 DUMPED_FUNCS=40 INSTRUCTIONS_SHOWN=1887
 (GhidraScript)  
INFO  ANALYZING changes made by post scripts: file:///home/runner/work/game/game/ANALYSIS/_INPUT/classes.dex (HeadlessAnalyzer)  
INFO  REPORT: Post-analysis succeeded for file: file:///home/runner/work/game/game/ANALYSIS/_INPUT/classes.dex (HeadlessAnalyzer)  
INFO  /classes.dex: file created (runner) (LocalFileSystem)  
INFO  REPORT: Save succeeded for: /classes.dex (Mimo935Analysis:/classes.dex) (HeadlessAnalyzer)  
INFO  REPORT: Import succeeded (HeadlessAnalyzer)  
auto_headless_exit=0
JAVA_HOME(REA)=/opt/hostedtoolcache/Java_Temurin-Hotspot_jdk/21.0.13-9/x64
JDK25_HOME(Ghidra)=/opt/hostedtoolcache/Java_Temurin-Hotspot_jdk/25.0.5-8/x64
java --list-modules | grep jdk.compiler:
jdk.compiler@21.0.13
rea_doctor_exit=0
{"healthy":true,"environment_healthy":false,"scope":{"mode":"explicit","clients":[],"providers":["jadx"],"skill":false,"target":null},"scope_checks":[{"name":"node","ok":true,"classification":"healthy","detail":"22.23.4","details":{"runtime":"node","version":"22.23.4"}},{"name":"jadx","ok":true,"classification":"healthy","detail":"JADX MCP bridge JAR validated at /home/runner/work/_temp/jadx-headless-mcp.jar; its path is recorded for agent registrations. This checks configuration, not whether a selected APK fits in the worker's memory.","details":{"operation_timeout_ms":120000}}],"informational_checks":[{"name":"host","ok":true,"classification":"healthy","detail":"ubuntu 24.04"},{"name":"hopper","ok":false,"classification":"missing_analysis_engine","remediation":"Run rea setup to install Hopper, or set HOPPER_LAUNCHER_PATH."},{"name":"ghidra","ok":true,"classification":"healthy","detail":"/home/runner/work/_temp/ghidra_dist/ghidra_12.2_PUBLIC"},{"name":"ghidra-platform","ok":true,"classification":"healthy","detail":"linux"},{"name":"ghidra-architecture","ok":true,"classification":"healthy","detail":"x64"},{"name":"ghidra-installation","ok":true,"classification":"healthy","detail":"/home/runner/work/_temp/ghidra_dist/ghidra_12.2_PUBLIC/Ghidra/application.properties"},{"name":"ghidra-version","ok":false,"classification":"config_drift","detail":"12.2; accepted releases are 12.1.x (verified build 12.1.4)","remediation":"Install a Ghidra 12.1.x release (verified with 12.1.4), or update REA for another Ghidra line."},{"name":"ghidra-headless","ok":true,"classification":"healthy","detail":"/home/runner/work/_temp/ghidra_dist/ghidra_12.2_PUBLIC/support/analyzeHeadless"},{"name":"ghidra-native_decompiler","ok":true,"classification":"healthy","detail":"/home/runner/work/_temp/ghidra_dist/ghidra_12.2_PUBLIC/Ghidra/Features/Decompiler/os/linux_x86_64/decompile reports elf x86_64, which matches linux/x64"},{"name":"ghidra-java","ok":false,"classification":"config_drift","detail"```
