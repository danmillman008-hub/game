/* ============================================================================
 * MISSION 08 — CURATED runtime observer agent.
 *
 * NO reflection-based "hook every method". Every hook below is selected from:
 *   ANALYSIS/MISSION_06/SCHEMAS/METHOD_CATALOG_MIMO.json  (exact signatures)
 *   ANALYSIS/RUNTIME/MISSION_07/m07_frida_stage2.js       (runtime-proven hooks)
 * Each entry carries its exact DEX signature, subsystem and overload count.
 * SQL/LiveData/URL/native events are filtered/deduplicated: only central
 * execution paths enter the unified timeline.
 *
 * Java bridge is injected by m07_frida_driver.py (REUSED VERBATIM, M07).
 * ==========================================================================*/
function emit(o) {
  try { o.pid = Process.id; o.tid = Process.getCurrentThreadId(); send(JSON.stringify(o)); }
  catch (e) { try { send('{"kind":"emit_error"}'); } catch (_) {} }
}
function safe(v) {
  if (v === null || v === undefined) return String(v);
  try { var s = v.toString(); if (s === undefined) s = String(v);
        return s.length > 700 ? s.substring(0, 700) + '...[cut]' : s; }
  catch (e) { return '<toString failed>'; }
}
function argsOf(a) { return Array.prototype.slice.call(a).map(safe); }
function dumpFields(o, max) {
  if (o === null || o === undefined) return null;
  try { var fs = o.getClass().getDeclaredFields(), out = {}, n = Math.min(fs.length, max || 20);
        for (var i = 0; i < n; i++) { var f = fs[i], nm = '?';
          try { nm = f.getName(); f.setAccessible(true); out[nm] = safe(f.get(o)); }
          catch (e) { out[nm] = '<field error>'; } } return out;
  } catch (e) { return '<dump failed>'; }
}

/* Curated hook table: [class, method, tag, subsystem, dumpThis, exact DEX signature]
   Signatures are copied verbatim from the M06 method catalog. */
var HOOKS = [
  /* --- startup / application architecture --- */
  ['com.getmimo.App','onCreate','app_onCreate','startup',1,
   'Lcom/getmimo/App;->onCreate()V'],
  ['com.getmimo.App','attachBaseContext','app_attachBase','startup',0,
   'Lcom/getmimo/App;->attachBaseContext(Landroid/content/Context;)V'],
  /* --- main ViewModel (M06: Lcom/getmimo/ui/main/d;) --- */
  ['com.getmimo.ui.main.d','E','mainViewModel_E','architecture',1,
   'Lcom/getmimo/ui/main/d;->E(Lcom/getmimo/data/model/reward/Reward;)V'],
  ['com.getmimo.ui.main.d','F','mainViewModel_F','architecture',1,
   'Lcom/getmimo/ui/main/d;->F(Lkotlin/coroutines/jvm/internal/ContinuationImpl;)Ljava/lang/Object;'],
  ['com.getmimo.ui.main.d','G','mainViewModel_G','architecture',1,
   'Lcom/getmimo/ui/main/d;->G(Lcom/getmimo/data/model/reward/Reward;)Z'],
  ['com.getmimo.ui.main.d','H','mainViewModel_H','architecture',1,
   'Lcom/getmimo/ui/main/d;->H(Lkotlin/coroutines/jvm/internal/ContinuationImpl;)Ljava/lang/Object;'],
  ['com.getmimo.ui.main.d','I','mainViewModel_I','architecture',1,
   'Lcom/getmimo/ui/main/d;->I(Z)V'],
  /* --- bottom navigation --- */
  ['com.getmimo.ui.navigation.NavigationBar','setActive','nav_setActive','navigation',1,
   'Lcom/getmimo/ui/navigation/NavigationBar;->setActive(Len/k;)V'],
  /* --- settings / daily goal --- */
  ['com.getmimo.data.settings.a','a','settings_get','learner_state',1,
   'Lcom/getmimo/data/settings/a;->a()Lcom/getmimo/data/settings/model/Settings;'],
  ['com.getmimo.data.settings.a','h','settings_dailyGoal','gamification',1,
   'Lcom/getmimo/data/settings/a;->h(I Lkotlin/coroutines/jvm/internal/SuspendLambda;)Ljava/lang/Object;'],
  ['com.getmimo.data.settings.a','l','settings_write','learner_state',1,
   'Lcom/getmimo/data/settings/a;->l(Lcom/getmimo/data/settings/model/Settings;)V'],
  /* --- gamification: streak / rewards / keys --- */
  ['com.getmimo.data.user.streak.a','d','streak_mapResponse','gamification',0,
   'Lcom/getmimo/data/user/streak/a;->d(Lcom/getmimo/core/model/streak/UserActivityResponse; Lnp/a;)Ljava/util/ArrayList;'],
  ['com.getmimo.data.user.streak.a','f','streak_getData','gamification',1,
   'Lcom/getmimo/data/user/streak/a;->f(Lsh/k; Lkotlin/coroutines/jvm/internal/ContinuationImpl;)Ljava/lang/Object;'],
  ['com.getmimo.data.user.streak.a','h','streak_toModel','gamification',0,
   'Lcom/getmimo/data/user/streak/a;->h(Lcom/getmimo/core/model/streak/UserActivityResponse;)Lsh/b;'],
  ['com.getmimo.data.source.remote.reward.a','a','reward_confirm','gamification',1,
   'Lcom/getmimo/data/source.remote/reward/a;->a(J Ld70/b;)Ljava/lang/Object;'],
  ['com.getmimo.data.source.remote.reward.a','c','reward_retrieve','gamification',1,
   'Lcom/getmimo/data/source.remote/reward/a;->c(Ld70/b;)Ljava/lang/Object;'],
  ['com.getmimo.data.source.remote.keys.a','a','keys_fetch','progression',1,
   'Lcom/getmimo/data/source.remote/keys/a;->a(Lkotlin/coroutines/jvm/internal/ContinuationImpl;)Ljava/lang/Object;'],
  ['com.getmimo.data.source.remote.keys.a','b','keys_consume','progression',1,
   'Lcom/getmimo/data/source.remote/keys/a;->b(Lkotlin/coroutines/jvm/internal/ContinuationImpl;)Ljava/lang/Object;'],
  ['com.getmimo.data.source.remote.keys.a','c','keys_gate','progression',1,
   'Lcom/getmimo/data/source.remote/keys/a;->c()Ljava/lang/Boolean;'],
  /* --- progression / unlock decision logic --- */
  ['com.getmimo.interactors.path.d','a','pathMapState_a','progression',1,
   'Lcom/getmimo/interactors/path/d;->a(I Z Lkotlin/coroutines/jvm/internal/ContinuationImpl;)Ljava/lang/Object;'],
  ['com.getmimo.interactors.path.d','b','pathMapState_b','progression',1,
   'Lcom/getmimo/interactors/path/d;->b(J I Lvn/i0; Lkotlin/coroutines/jvm/internal/ContinuationImpl;)Ljava/lang/Object;'],
  ['com.getmimo.interactors.chapter.a','a','canOpenChapter','progression',1,
   'Lcom/getmimo/interactors/chapter/a;->a(Lkotlin/coroutines/jvm/internal/ContinuationImpl;)Ljava/lang/Object;'],
  /* --- learner state / progress queue / repository --- */
  ['com.getmimo.data.source.remote.progress.LessonProgressQueue','storeLessonProgress','queue_store','learner_state',1,
   'Lcom/getmimo/data/source.remote.progress/LessonProgressQueue;->storeLessonProgress(Lcom/getmimo/data/model/room/LessonProgress; Z Z Ld70/b;)Ljava/lang/Object;'],
  ['com.getmimo.data.source.remote.progress.LessonProgressQueue','getCorrectLessonProgressCount','queue_correctCount','gamification',1,
   'Lcom/getmimo/data/source.remote.progress/LessonProgressQueue;->getCorrectLessonProgressCount(Ld70/b;)Ljava/lang/Object;'],
  ['com.getmimo.data.source.remote.progress.LessonProgressQueue','getCorrectLessonsFirstTryCount','queue_firstTryCount','gamification',1,
   'Lcom/getmimo/data/source.remote.progress.LessonProgressQueue;->getCorrectLessonsFirstTryCount(Ld70/b;)Ljava/lang/Object;'],
  ['com.getmimo.data.source.remote.progress.LessonProgressQueue','updateCorrectAnswersCount','queue_updateCorrect','gamification',1,
   'Lcom/getmimo/data/source.remote.progress.LessonProgressQueue;->updateCorrectAnswersCount(Ld70/b;)Ljava/lang/Object;'],
  ['com.getmimo.data.source.remote.progress.LessonProgressQueue','updateLessonStreakDetector','queue_streakDetector','gamification',1,
   'Lcom/getmimo/data/source.remote.progress.LessonProgressQueue;->updateLessonStreakDetector(Lcom/getmimo/data/model/room/LessonProgress; Z)V'],
  ['com.getmimo.data.source.remote.progress.LessonProgressRepository','createLessonProgress','repo_createProgress','learner_state',1,
   'Lcom/getmimo/data/source.remote.progress.LessonProgressRepository;->createLessonProgress(Lcom/getmimo/ui/lesson/interactive/LessonBundle; Lorg/joda/time/Instant; I I)Lcom/getmimo/data/model/room/LessonProgress;'],
  ['com.getmimo.data.source.remote.progress.LessonProgressRepository','postUnsyncedLessonProgress','repo_postUnsynced','learner_state',1,
   'Lcom/getmimo/data/source.remote.progress.LessonProgressRepository;->postUnsyncedLessonProgress(Ld70/b;)Ljava/lang/Object;'],
  ['com.getmimo.data.source.remote.progress.LessonProgressRepository','moveLessonProgressFromQueue','repo_moveFromQueue','learner_state',1,
   'Lcom/getmimo/data/source.remote.progress.LessonProgressRepository;->moveLessonProgressFromQueue(Ld70/b;)Ljava/lang/Object;'],
  ['com.getmimo.data.source.remote.progress.LessonProgressApi','postProgress','api_postProgress','network',1,
   'Lcom/getmimo/data/source.remote.progress.LessonProgressApi;->postProgress(J Lcom/getmimo/data/model/progress/PostProgressRequestBody; Ld70/b;)Ljava/lang/Object;'],
  ['com.getmimo.data.model.room.LessonProgress','isSolvedCorrectly','isSolved','learner_state',1,
   'Lcom/getmimo/data/model/room/LessonProgress;->isSolvedCorrectly()Z'],
  /* --- lesson engine: shared ViewModel methods (M06/M07 proven) --- */
  ['com.getmimo.ui.lesson.interactive.base.c','O','lesson_init','lesson_engine',1,
   'Lcom/getmimo/ui/lesson/interactive/base.c;->O(Lcom/getmimo/ui/lesson/interactive/LessonBundle;)V [M07 runtime]'],
  ['com.getmimo.ui.lesson.interactive.base.c','K','lesson_bundle','lesson_engine',0,
   'Lcom/getmimo/ui/lesson/interactive/base.c;->K()Lcom/getmimo/ui/lesson/interactive/LessonBundle; [M07 runtime]'],
  ['com.getmimo.ui.lesson.interactive.base.c','U','lesson_solvedProceed','lesson_engine',1,
   'Lcom/getmimo/ui/lesson/interactive/base.c;->U(Ld70/b;)Ljava/lang/Object; [M07 runtime]'],
  ['com.getmimo.ui.lesson.interactive.base.c','H','lesson_createProgress','lesson_engine',1,
   'Lcom/getmimo/ui/lesson/interactive/base.c;->H(I I)Lcom/getmimo/data/model/room/LessonProgress; [M07 runtime]'],
  ['com.getmimo.ui.lesson.interactive.base.c','e0','lesson_storeProgress','lesson_engine',1,
   'Lcom/getmimo/ui/lesson/interactive/base.c;->e0(Lcom/getmimo/data/model/room/LessonProgress; Ld70/b;)Ljava/lang/Object; [M07 runtime]'],
  ['com.getmimo.ui.lesson.interactive.base.c','f0','lesson_trackResult','lesson_engine',1,
   'Lcom/getmimo/ui/lesson.interactive.base.c;->f0(Z Z)V [M07 runtime: false,true]'],
  ['com.getmimo.ui.lesson.interactive.base.c','V','lesson_correctExact','lesson_engine',1,
   'Lcom/getmimo/ui/lesson/interactive.base.c;->V(Ld70/b;)Ljava/lang/Object; [M07 static decode]'],
  ['com.getmimo.ui.lesson.interactive.base.c','W','lesson_correctPartial','lesson_engine',1,
   'Lcom/getmimo/ui/lesson/interactive.base.c;->W(Ld70/b;)Ljava/lang/Object; [M07 static decode]'],
  ['com.getmimo.ui.lesson.interactive.base.c','X','lesson_wrong','lesson_engine',1,
   'Lcom/getmimo/ui/lesson/interactive.base.c;->X(Ld70/b;)Ljava/lang/Object; [M07 static decode]'],
  ['com.getmimo.ui.lesson.interactive.base.c','d0','lesson_wrongFeedback','lesson_engine',1,
   'Lcom/getmimo/ui/lesson/interactive.base.c;->d0()Ljava/lang/Object; [M07 static decode]'],
  ['com.getmimo.ui.lesson.interactive.base.c','N','lesson_resetInput','lesson_engine',1,
   'Lcom/getmimo/ui/lesson/interactive.base.c;->N()V [M07 runtime]'],
  /* --- content / DSL / interaction type selection --- */
  ['te.c','b','dslParser','content',0,
   'Lte/c;->b(Ljava/lang/String;)Ljava/util/List; [M07 runtime]'],
  ['gm.h','a','interactionSelector','lesson_engine',0,
   'Lgm/h;->a(Ljava/util/List;)Lcom/getmimo/ui/lesson/interactive/LessonInteractionType; [M07 runtime]'],
  /* --- answer dispatch coroutines --- */
  ['com.getmimo.ui.lesson.interactive.base.InteractiveLessonBaseViewModel$onLessonRun$1','invokeSuspend','onLessonRunCoroutine','lesson_engine',1,
   '...$onLessonRun$1;->invokeSuspend(Ljava/lang/Object;)Ljava/lang/Object; [M07 runtime]'],
  ['im.d','E0','fillTheGapRun','lesson_engine',1,
   'Lim/d;->E0(...)Ljava/lang/Object; [M07 runtime hook]'],
  /* --- network gate / background workers --- */
  ['com.getmimo.network.a','a','net_isOnline','network',0,
   'Lcom/getmimo/network/a;->a()Z [M07 runtime]'],
  ['com.getmimo.data.source.remote.authentication.PostVisitWorker','a','postVisitWorker','background',1,
   'Lcom/getmimo/data/source.remote/authentication/PostVisitWorker;->a(Ld70/b;)Ljava/lang/Object;'],
  ['com.getmimo.ui.widget.StreakWidgetRefreshWorker','a','streakWidgetWorker','background',1,
   'Lcom/getmimo/ui/widget/StreakWidgetRefreshWorker;->a(Ld70/b;)Ljava/lang/Object;'],
  /* --- Phase 2 additions: derived ONLY from run 42042312640 evidence + M06
         method catalog. These are the missing navigation/coins/progression
         decision points, not a broad reflection sweep. --- */
  ['com.getmimo.ui.main.MainActivity','B','mainActivity_viewModel','architecture',1,
   'Lcom/getmimo/ui/main/MainActivity;->B()Lcom/getmimo/ui/main/d;'],
  ['com.getmimo.ui.main.MainActivity','onResume','mainActivity_onResume','navigation',0,
   'Lcom/getmimo/ui/main/MainActivity;->onResume()V'],
  ['com.getmimo.ui.path.map.j','G','pathMap_navigateChapter','progression',1,
   'Lcom/getmimo/ui/path/map/j;->G(J J)V'],
  ['com.getmimo.ui.path.map.j','K','pathMap_onTutorialClick','progression',1,
   'Lcom/getmimo/ui/path/map/j;->K(Lvn/i0;)V'],
  ['com.getmimo.ui.path.map.j','J','pathMap_toolbarButton','progression',1,
   'Lcom/getmimo/ui/path/map/j;->J(Lcom/getmimo/ui/path/map/PathToolbarButtonType;)V'],
  ['com.getmimo.ui.path.map.j','N','pathMap_openChapter','progression',1,
   'Lcom/getmimo/ui/path/map/j;->N(Lcom/getmimo/ui/chapter/ChapterBundle; J Lkotlin/coroutines/jvm/internal/ContinuationImpl;)Ljava/lang/Object;'],
  ['com.getmimo.ui.chapter.ChapterActivity','B','chapterActivity_viewModel','architecture',1,
   'Lcom/getmimo/ui/chapter/ChapterActivity;->B()Lcom/getmimo/ui/chapter/ChapterViewModel;'],
  ['com.getmimo.ui.chapter.ChapterActivity','G','chapterActivity_navigate','navigation',1,
   'Lcom/getmimo/ui/chapter/ChapterActivity;->G(Lcom/getmimo/ui/chapter/ChapterBundle; Z)V'],
  ['com.getmimo.data.source.remote.coins.a','a','coins_flow','gamification',1,
   'Lcom/getmimo/data/source/remote/coins/a;->a()Lua0/r;'],
  ['com.getmimo.data.source.remote.coins.a','b','coins_sync','gamification',1,
   'Lcom/getmimo/data/source/remote/coins/a;->b(Lkotlin/coroutines/jvm/internal/SuspendLambda;)Ljava/lang/Object;'],
  ['com.getmimo.core.model.coins.Coins','getCoins','coins_value','gamification',1,
   'Lcom/getmimo/core/model/coins/Coins;->getCoins()I'],
  ['com.getmimo.interactors.path.sections.a','a','sections_unlockState','progression',1,
   'Lcom/getmimo/interactors/path/sections/a;->a(Lkotlin/coroutines/jvm/internal/SuspendLambda;)Ljava/lang/Object;'],
  ['com.getmimo.interactors.path.f','a','pathCoinsState','progression',1,
   'Lcom/getmimo/interactors/path/f;->a()Lci/b;']
];

function hookOne(h) {
  var cls = h[0], method = h[1], tag = h[2], subsystem = h[3], dumpThis = h[4], sig = h[5];
  try {
    var C = Java.use(cls), m = C[method];
    if (!m || !m.overloads) { emit({kind:'hook_error', tag:tag, cls:cls, method:method, error:'no overloads'}); return; }
    var loader = '';
    try { loader = safe(C.class.getClassLoader()); } catch (e) { loader = '<unknown>'; }
    emit({kind:'hook_installed', tag:tag, cls:cls, method:method, subsystem:subsystem,
          signature:sig, overloads:m.overloads.length, class_loader:loader});
    m.overloads.forEach(function (ov, oi) {
      try {
        ov.implementation = function () {
          var id = tag + '#' + (++hookOne._n);
          var ev = {kind:'entry', tag:tag, cls:cls, method:method, subsystem:subsystem,
                    signature:sig, overload:oi, id:id, args:argsOf(arguments)};
          if (dumpThis) ev.this_fields = dumpFields(this, 18);
          emit(ev);
          var ret;
          try {
            ret = ov.apply(this, arguments);
            emit({kind:'exit', tag:tag, cls:cls, method:method, subsystem:subsystem, id:id,
                  ret:safe(ret), ret_fields:(ret && typeof ret === 'object') ? dumpFields(ret, 12) : null});
          } catch (e) {
            emit({kind:'throw', tag:tag, cls:cls, method:method, subsystem:subsystem, id:id, error:safe(e)});
            throw e;
          }
          return ret;
        };
      } catch (e) { emit({kind:'hook_error', tag:tag, method:method, overload:oi, error:safe(e)}); }
    });
  } catch (e) { emit({kind:'hook_error', tag:tag, cls:cls, method:method, error:safe(e)}); }
}
hookOne._n = 0;

Java.perform(function () {
  HOOKS.forEach(hookOne);

  /* --- ONE lifecycle hook gives the whole navigation graph (all activities) --- */
  try {
    var AT = Java.use('android.app.ActivityThread'), app = AT.currentApplication();
    emit({kind:'env', tag:'application', subsystem:'startup',
          application_class:app === null ? 'null' : app.getClass().getName(), fields:dumpFields(app, 16)});
    var CB = Java.use('android.app.Application$ActivityLifecycleCallbacks');
    var LC = Java.registerClass({ name:'m08.LifecycleCallbacks', implements:[CB], methods:{
      onActivityCreated:function(a,b){ emit({kind:'nav', tag:'activity_created', subsystem:'navigation', activity:a.getClass().getName(), bundle:safe(b)}); },
      onActivityStarted:function(a){ emit({kind:'nav', tag:'activity_started', subsystem:'navigation', activity:a.getClass().getName()}); },
      onActivityResumed:function(a){ emit({kind:'nav', tag:'activity_resumed', subsystem:'navigation', activity:a.getClass().getName()}); },
      onActivityPaused:function(a){ emit({kind:'nav', tag:'activity_paused', subsystem:'navigation', activity:a.getClass().getName()}); },
      onActivityStopped:function(a){ emit({kind:'nav', tag:'activity_stopped', subsystem:'navigation', activity:a.getClass().getName()}); },
      onActivitySaveInstanceState:function(a,b){ emit({kind:'nav', tag:'activity_save_state', subsystem:'navigation', activity:a.getClass().getName()}); },
      onActivityDestroyed:function(a){ emit({kind:'nav', tag:'activity_destroyed', subsystem:'navigation', activity:a.getClass().getName()}); }
    }});
    app.registerActivityLifecycleCallbacks(LC.$new());
    emit({kind:'hook_installed', tag:'activity_lifecycle', subsystem:'navigation',
          signature:'android.app.Application$ActivityLifecycleCallbacks', overloads:7});
  } catch (e) { emit({kind:'hook_error', tag:'activity_lifecycle', error:safe(e)}); }

  /* --- Room SQL: mimo.db ONLY, transaction boilerplate removed --- */
  try {
    var D = Java.use('android.database.sqlite.SQLiteDatabase');
    ['execSQL','insert','insertWithOnConflict','insertOrThrow','update','updateWithOnConflict',
     'delete','rawQuery','rawQueryWithFactory','compileStatement'].forEach(function (mn) {
      var m = D[mn]; if (!m || !m.overloads) return;
      m.overloads.forEach(function (ov) {
        try { ov.implementation = function () {
          var p = ''; try { p = safe(this.getPath()); } catch (e) { p = ''; }
          var a = argsOf(arguments);
          if (p.indexOf('mimo.db') >= 0 || a.join(' ').match(/lesson_progress|chapter_completions|tutorial_completions/))
            emit({kind:'sql', method:mn, subsystem:'database', db_path:p, args:a});
          return ov.apply(this, arguments);
        }; } catch (e) { emit({kind:'hook_error', tag:'sql', method:mn, error:safe(e)}); }
      });
    });
    emit({kind:'hook_installed', tag:'sql', subsystem:'database', cls:'SQLiteDatabase',
          signature:'filtered to mimo.db / progress tables; transactions excluded'});
  } catch (e) { emit({kind:'hook_error', tag:'sql', error:safe(e)}); }

  /* --- LiveData: state CHANGES only (dedupe by class+value) --- */
  var lastLD = {}, ldCount = 0;
  try {
    var LD = Java.use('androidx.lifecycle.m0');
    ['l','k'].forEach(function (mn) {
      var m = LD[mn]; if (!m || !m.overloads) return;
      m.overloads.forEach(function (ov) {
        try { ov.implementation = function () {
          var v = arguments[0], vc = v === null ? 'null' : v.getClass().getName(), sv = safe(v);
          var key = mn + '|' + vc;
          if (lastLD[key] !== sv && ldCount < 300) {
            lastLD[key] = sv; ldCount++;
            emit({kind:'liveData', method:mn, subsystem:'state', value_class:vc,
                  value:sv, fields:dumpFields(v, 12)});
          }
          return ov.apply(this, arguments);
        }; } catch (e) { emit({kind:'hook_error', tag:'liveData', method:mn, error:safe(e)}); }
      });
    });
    emit({kind:'hook_installed', tag:'liveData', subsystem:'state', cls:'androidx.lifecycle.m0',
          signature:'l(T)/k(T), deduplicated state changes only'});
  } catch (e) { emit({kind:'hook_error', tag:'liveData', error:safe(e)}); }

  /* --- Network boundary: deduplicated URLs only --- */
  var seenURL = {}, urlCount = 0;
  function net(tag, url, extra) {
    var k = tag + '|' + url;
    if (seenURL[k] || urlCount > 200) return;
    seenURL[k] = 1; urlCount++;
    emit({kind:'net', tag:tag, subsystem:'network', url:url, extra:safe(extra)});
  }
  try {
    var OK = Java.use('okhttp3.OkHttpClient');
    OK.newCall.overloads.forEach(function (ov) {
      try { ov.implementation = function (req) {
        var u = ''; try { u = safe(req.url()); } catch (e) { u = safe(req); }
        net('okhttp_newCall', u, req); return ov.apply(this, arguments);
      }; } catch (e) { emit({kind:'net_probe', tag:'okhttp_missing', error:safe(e)}); }
    });
    emit({kind:'hook_installed', tag:'okhttp_newCall', subsystem:'network', cls:'okhttp3.OkHttpClient'});
  } catch (e) { emit({kind:'net_probe', tag:'okhttp_missing', error:safe(e)}); }
  try {
    var U = Java.use('java.net.URL');
    U.openConnection.overloads.forEach(function (ov) {
      try { ov.implementation = function () {
        net('url_openConnection', safe(this), ''); return ov.apply(this, arguments);
      }; } catch (e) { emit({kind:'hook_error', tag:'url_openConnection', error:safe(e)}); }
    });
    emit({kind:'hook_installed', tag:'url_openConnection', subsystem:'network', cls:'java.net.URL'});
  } catch (e) { emit({kind:'hook_error', tag:'url_openConnection', error:safe(e)}); }

  /* --- Media / native boundaries: dedupe --- */
  var seenLib = {};
  try {
    var SY = Java.use('java.lang.System');
    SY.loadLibrary.overloads.forEach(function (ov) {
      try { ov.implementation = function (n) {
        var s = safe(n); if (!seenLib[s]) { seenLib[s] = 1;
          emit({kind:'native', tag:'loadLibrary', subsystem:'media', library:s}); }
        return ov.apply(this, arguments);
      }; } catch (e) { emit({kind:'hook_error', tag:'loadLibrary', error:safe(e)}); }
    });
  } catch (e) { emit({kind:'hook_error', tag:'loadLibrary', error:safe(e)}); }
  try {
    var WV = Java.use('android.webkit.WebView');
    WV.addJavascriptInterface.overloads.forEach(function (ov) {
      try { ov.implementation = function (obj, name) {
        emit({kind:'media', tag:'js_interface', subsystem:'media', name:safe(name),
              object_class:obj === null ? 'null' : obj.getClass().getName(),
              object_fields:dumpFields(obj, 12)});
        return ov.apply(this, arguments);
      }; } catch (e) { emit({kind:'hook_error', tag:'js_interface', error:safe(e)}); }
    });
    emit({kind:'hook_installed', tag:'js_interface', subsystem:'media', cls:'android.webkit.WebView'});
  } catch (e) { emit({kind:'hook_error', tag:'js_interface', error:safe(e)}); }

  /* --- one structural inventory event --- */
  try {
    var all = Java.enumerateLoadedClassesSync(), groups = {};
    ['okhttp3','retrofit2','com.getmimo','androidx.work','app.rive','com.google.firebase',
     'kotlinx.coroutines','androidx.room','androidx.datastore','androidx.fragment'].forEach(function (g) {
      groups[g] = all.filter(function (c) { return c.indexOf(g) === 0; }).length; });
    emit({kind:'env', tag:'class_inventory', subsystem:'architecture', total:all.length, groups:groups,
          api_classes:all.filter(function (c) { return /com\.getmimo\/.*[Aa]pi/.test(c); }).slice(0, 40)});
  } catch (e) { emit({kind:'hook_error', tag:'class_inventory', error:safe(e)}); }

  /* --- Runtime DI container: the LIVE App object (attach happens after
         onCreate, so Java.choose is how the real graph is observed). --- */
  ['com.getmimo.App','com.getmimo.ui.main.d','com.getmimo.ui.path.map.j',
   'com.getmimo.data.source.remote.progress.LessonProgressQueue'].forEach(function (cn) {
    var found = 0;
    try {
      Java.choose(cn, {
        onMatch: function (o) {
          if (found++ < 2) emit({kind:'di', tag:'live_instance', subsystem:'architecture',
                                cls:cn, fields:dumpFields(o, 26), identity:safe(o)});
        },
        onComplete: function () {
          emit({kind:'di', tag:'instance_scan', subsystem:'architecture', cls:cn, count:found});
        }
      });
    } catch (e) { emit({kind:'hook_error', tag:'di_choose', cls:cn, error:safe(e)}); }
  });

  /* --- Learner-state WRITES: only Mimo preference keys discovered in run
         42042312640. Gives the storage half of a scoring claim. --- */
  try {
    var ED = Java.use('android.app.SharedPreferencesImpl$EditorImpl');
    ['putString','putInt','putBoolean','putLong','putFloat'].forEach(function (mn) {
      var m = ED[mn]; if (!m || !m.overloads) return;
      m.overloads.forEach(function (ov) {
        try { ov.implementation = function () {
          var k = safe(arguments[0]);
          if (/local_coins|user_settings|favorite_tracks|daily|goal|streak|coins/i.test(k)) {
            emit({kind:'prefs_write', subsystem:'learner_state', method:mn, key:k,
                  value:safe(arguments[1]), editor:safe(this)});
          }
          return ov.apply(this, arguments);
        }; } catch (e) { emit({kind:'hook_error', tag:'prefs_write', method:mn, error:safe(e)}); }
      });
    });
    emit({kind:'hook_installed', tag:'prefs_write', subsystem:'learner_state',
          cls:'android.app.SharedPreferencesImpl$EditorImpl',
          signature:'filtered to Mimo learner-state keys'});
  } catch (e) { emit({kind:'hook_error', tag:'prefs_write', error:safe(e)}); }

  emit({kind:'ready', subsystem:'observer', hooks:HOOKS.length, agent:'m08_agent.js'});
});
