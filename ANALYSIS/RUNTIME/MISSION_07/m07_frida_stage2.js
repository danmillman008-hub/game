/*
 * MISSION 07 / STAGE 2 — live method trace of a REAL correct/incorrect answer
 * on the ORIGINAL Mimo 9.35 process. Hooks only; no APK modification.
 * Records: answer dispatch, feedback construction, LessonProgress field values,
 * Room SQL actually executed, LiveData posts, network gate, offline queue.
 */
function emit(o) { try { send(JSON.stringify(o)); } catch (e) { send('{"kind":"emit_error","e":"' + e + '"}'); } }
function safe(v) {
  if (v === null || v === undefined) return String(v);
  try { var s = v.toString(); if (s === undefined) s = String(v);
        return s.length > 800 ? s.substring(0, 800) + '...[truncated]' : s; }
  catch (e) { return '<toString failed ' + e + '>'; }
}
function argsOf(a) { return Array.prototype.slice.call(a).map(safe); }
function dumpFields(o, max) {
  if (o === null || o === undefined) return null;
  try {
    var fs = o.getClass().getDeclaredFields(), out = {}, n = Math.min(fs.length, max || 40);
    for (var i = 0; i < n; i++) {
      var f = fs[i], nm = '?';
      try { nm = f.getName(); f.setAccessible(true); out[nm] = safe(f.get(o)); }
      catch (e) { out[nm] = '<field error ' + e + '>'; }
    }
    return out;
  } catch (e) { return '<dump failed ' + e + '>'; }
}
var DUMP = {'createLessonProgress':1,'repo_createProgress':1,'queue_store':1,'isSolved':1,
            'onLessonRun':1,'lessonSolvedCorrectly':1,'lessonSolvedIncorrectly':1,
            'partialMatch':1,'wrongFeedback':1,'onValidatedInputCoroutine':1,
            'setupViewsCoroutine':1,'liveData':1,'executableValidator':1};

function hook(cls, method, tag, dumpThis) {
  try {
    var C = Java.use(cls), m = C[method];
    if (!m || !m.overloads) { emit({kind:'hook_error', tag:tag, cls:cls, method:method, error:'no overloads'}); return; }
    m.overloads.forEach(function (ov) {
      try {
        ov.implementation = function () {
          var id = tag + '#' + (++hook._n);
          var ev = {kind:'entry', tag:tag, cls:cls, method:method, id:id, args:argsOf(arguments)};
          if (dumpThis) ev.this_fields = dumpFields(this, 30);
          emit(ev);
          var ret;
          try {
            ret = ov.apply(this, arguments);
            var ex = {kind:'exit', tag:tag, cls:cls, method:method, id:id, ret:safe(ret)};
            if (DUMP[tag] && ret !== null && ret !== undefined) ex.ret_fields = dumpFields(ret);
            emit(ex);
          } catch (e) {
            emit({kind:'throw', tag:tag, cls:cls, method:method, id:id, error:safe(e)});
            throw e;
          }
          return ret;
        };
      } catch (e) { emit({kind:'hook_error', tag:tag, cls:cls, method:method, error:safe(e)}); }
    });
    emit({kind:'hook_installed', tag:tag, cls:cls, method:method, overloads:m.overloads.length});
  } catch (e) { emit({kind:'hook_error', tag:tag, cls:cls, method:method, error:safe(e)}); }
}
hook._n = 0;

/* Room/SQLite: record EXACT SQL actually executed, filtered to Mimo DB. */
function hookSQL() {
  try {
    var D = Java.use('android.database.sqlite.SQLiteDatabase');
    ['execSQL','insert','insertWithOnConflict','insertOrThrow','replace','replaceOrThrow',
     'update','updateWithOnConflict','delete','rawQueryWithFactory','rawQuery',
     'beginTransaction','beginTransactionNonExclusive','beginTransactionWithListener',
     'beginTransactionWithListenerNonExclusive','setTransactionSuccessful','endTransaction',
     'compileStatement','query','queryWithFactory'].forEach(function (mn) {
      var m = D[mn];
      if (!m || !m.overloads) return;
      m.overloads.forEach(function (ov) {
        try {
          ov.implementation = function () {
            var p = '';
            try { p = safe(this.getPath()); } catch (e) { p = '<no path>'; }
            var a = argsOf(arguments);
            var interesting = p.indexOf('mimo') >= 0 ||
              a.join(' ').match(/lesson_progress|chapter_completions|tutorial_completions|room_master_table/);
            if (interesting) emit({kind:'sql', method:mn, db_path:p, args:a});
            return ov.apply(this, arguments);
          };
        } catch (e) { emit({kind:'hook_error', tag:'sql', method:mn, error:safe(e)}); }
      });
    });
    emit({kind:'hook_installed', tag:'sql', cls:'android.database.sqlite.SQLiteDatabase'});
  } catch (e) { emit({kind:'hook_error', tag:'sql', error:safe(e)}); }
  // Room executes compiled statements through SQLiteStatement; record those too.
  try {
    var ST = Java.use('android.database.sqlite.SQLiteStatement');
    ['execute','executeInsert','executeUpdateDelete','simpleQueryForLong','simpleQueryForString'].forEach(function (mn) {
      var m = ST[mn];
      if (!m || !m.overloads) return;
      m.overloads.forEach(function (ov) {
        try {
          ov.implementation = function () {
            emit({kind:'sql_statement', method:mn, args:argsOf(arguments),
                  this_fields:dumpFields(this, 8)});
            return ov.apply(this, arguments);
          };
        } catch (e) { emit({kind:'hook_error', tag:'sql_statement', method:mn, error:safe(e)}); }
      });
    });
    emit({kind:'hook_installed', tag:'sql_statement', cls:'android.database.sqlite.SQLiteStatement'});
  } catch (e) { emit({kind:'hook_error', tag:'sql_statement', error:safe(e)}); }
}

/* LiveData / MutableLiveData posts: feedback + progress state objects. */
function hookLiveData() {
  ['androidx.lifecycle.m0', 'androidx.lifecycle.MutableLiveData'].forEach(function (cn) {
    try {
      var C = Java.use(cn);
      ['l','k','setValue','postValue'].forEach(function (mn) {
        var m = C[mn];
        if (!m || !m.overloads) return;
        m.overloads.forEach(function (ov) {
          try {
            ov.implementation = function () {
              var v = arguments[0];
              try {
                var cn2 = v === null ? 'null' : v.getClass().getName();
                if (cn2.indexOf('com.getmimo') >= 0 || cn2.indexOf('jm.') >= 0 ||
                    cn2.indexOf('LessonProgress') >= 0 || cn2.indexOf('java.lang.Boolean') >= 0) {
                  emit({kind:'liveData', cls:cn, method:mn, value_class:cn2,
                        value:safe(v), fields:dumpFields(v, 40), this_fields:dumpFields(this, 10)});
                }
              } catch (e) { /* never break the app */ }
              return ov.apply(this, arguments);
            };
          } catch (e) { emit({kind:'hook_error', tag:'liveData', cls:cn, method:mn, error:safe(e)}); }
        });
      });
    } catch (e) { emit({kind:'hook_error', tag:'liveData', cls:cn, error:safe(e)}); }
  });
}

Java.perform(function () {
  emit({kind:'ready', android:Java.androidVersion, arch:Process.arch, ptr:Process.pointerSize,
        pid:Process.id, frida_vm:'attached'});
  try {
    var all = Java.enumerateLoadedClassesSync();
    var mimo = all.filter(function(n){ return n.indexOf('com.getmimo')===0; });
    emit({kind:'call', experiment:'S2_loaded_classes', total_loaded:all.length,
          mimo_loaded:mimo.length,
          room_classes:mimo.filter(function(n){return n.indexOf('room')>=0||n.indexOf('Dao')>=0;}).slice(0,80),
          lesson_classes:mimo.filter(function(n){return n.indexOf('lesson')>=0;}).slice(0,80)});
  } catch(e) { emit({kind:'experiment_error', experiment:'S2_loaded_classes', error:safe(e)}); }

  /* ---------- 1. validatedInput normalizer: controlled input truth table ---- */
  var CASES = [
    ['exact', 'D'], ['case_upper', 'D'], ['case_lower', 'd'],
    ['leading_ws', '  D'], ['trailing_ws', 'D  '], ['both_ws', '  D  '],
    ['repeated_ws', 'D   O   G'], ['internal_ws', 'D O G'],
    ['punctuation_allowed', '<button>Hi:</button>{a,b.c}'],
    ['punctuation_disallowed', 'a+b-c=d;e/f"g\'h!i?j@k#l$m%n^o&p*q'],
    ['digits', 'A1b2C3'], ['empty', ''], ['only_ws', '   '],
    ['unicode_accent', 'Café'], ['unicode_turkish', 'İstanbul ı I i'],
    ['unicode_german', 'Straße ÄÖÜ ß'], ['unicode_cjk', '你好'],
    ['emoji', 'D🐶'], ['tab_newline', 'D\tO\nG'],
    ['allowed_all', '< > ( ) : { } , .'], ['disallowed_all', '-_=+;!?@#$%^&*']
  ];
  try {
    var Q = Java.use('qm.i');
    CASES.forEach(function (c) {
      try {
        var r = Q.a(c[1]);
        emit({kind:'call', experiment:'E1_normalizer', cls:'qm.i', method:'a',
              case_name:c[0], input:c[1], ret:r, ret_len:r === null ? -1 : r.length});
      } catch (e) { emit({kind:'call_error', experiment:'E1_normalizer', case_name:c[0], error:safe(e)}); }
    });
  } catch (e) { emit({kind:'experiment_error', experiment:'E1_normalizer', error:safe(e)}); }

  /* ---------- 2. selection validator: constructed sm/a objects ------------- */
  try {
    var A = Java.use('sm.a'), F = Java.use('km.f'), AL = Java.use('java.util.ArrayList');
    var JS = Java.use('java.lang.String');
    function mk(text, selected, correct) { return A.$new(JS.$new(text), selected, correct, false); }
    function run(name, items) {
      var list = AL.$new();
      items.forEach(function (i) { list.add(mk(i[0], i[1], i[2])); });
      var r = F.b(list);
      emit({kind:'call', experiment:'E2_selection_validator', cls:'km.f', method:'b',
            case_name:name, items:items.map(function(i){return {text:i[0], selected:i[1], correct:i[2]};}), ret:r});
    }
    run('empty', []);
    run('one_match_true_true', [['Q', true, true]]);
    run('one_mismatch_true_false', [['Q', true, false]]);
    run('one_mismatch_false_true', [['Q', false, true]]);
    run('one_false_false', [['Q', false, false]]);
    run('three_all_match', [['A', true, true], ['B', false, false], ['C', true, true]]);
    run('three_one_wrong', [['A', true, true], ['B', true, false], ['C', true, true]]);
    run('three_one_missing', [['A', true, true], ['B', false, true], ['C', true, true]]);
  } catch (e) { emit({kind:'experiment_error', experiment:'E2_selection_validator', error:safe(e)}); }

  /* ---------- 3. LessonProgress.isSolvedCorrectly() on real objects -------- */
  try {
    var LP = Java.use('com.getmimo.data.model.room.LessonProgress');
    var INS = Java.use('org.joda.time.Instant');
    [-1, 0, 1, 2, 5].forEach(function (t) {
      [-1, 0, 1, 3].forEach(function (att) {
        var o = LP.$new(151403, INS.$new(), INS.$new(), t, 904, 2, 1, 753, att, false, true);
        emit({kind:'call', experiment:'E3_isSolvedCorrectly', cls:'LessonProgress',
              method:'isSolvedCorrectly', tries:t, attempts:att, ret:o.isSolvedCorrectly(),
              tostring:safe(o)});
      });
    });
  } catch (e) { emit({kind:'experiment_error', experiment:'E3_isSolvedCorrectly', error:safe(e)}); }

  /* ---------- 4. offline gate NetworkUtils.a()/b() with real Context ------- */
  try {
    var AT = Java.use('android.app.ActivityThread');
    var app = AT.currentApplication();
    var NU = Java.use('com.getmimo.network.a');
    var nu = NU.$new(app);
    emit({kind:'call', experiment:'E4_network_gate', cls:'com.getmimo.network.a',
          method:'a', context:safe(app), ret:nu.a()});
    emit({kind:'call', experiment:'E4_network_gate', cls:'com.getmimo.network.a',
          method:'b', context:safe(app), ret:nu.b()});
  } catch (e) { emit({kind:'experiment_error', experiment:'E4_network_gate', error:safe(e)}); }

  /* ---------- 5. DSL parser Lte/c.b(String) on a LIVE DI instance ---------- */
  try {
    var samples = [
      ['only_paragraph', '<html><body><p>Hello <strong>world</strong></p></body></html>'],
      ['paragraph_and_code', '<html><body><p>Intro</p><code version="2" codelang="html" name="index.html" visible-if="always"><content><text value="&lt;h1&gt;Hi&lt;/h1&gt;" /></content></code></body></html>'],
      ['selection', '<html><body><p>Pick</p><selection multiple="multiple"><item value="1" correct="true">Yes</item><item value="2" correct="false">No</item></selection></body></html>'],
      ['unknown_tag', '<html><body><foo>a</foo><p>ok</p></body></html>'],
      ['malformed', '<p>unclosed']
    ];
    var found = 0;
    Java.choose('te.c', {
      onMatch: function (parser) {
        found++;
        samples.forEach(function (sp) {
          try {
            var out = parser.b(sp[1]);
            emit({kind:'call', experiment:'E5_dsl_parser', cls:'te.c', method:'b',
                  case_name:sp[0], input:sp[1], size:out === null ? -1 : out.size(),
                  ret:safe(out), parser_fields:dumpFields(parser, 20)});
          } catch (e) { emit({kind:'call_error', experiment:'E5_dsl_parser', case_name:sp[0], error:safe(e)}); }
        });
      },
      onComplete: function () {
        if (!found) emit({kind:'experiment_error', experiment:'E5_dsl_parser',
                          error:'no live te.c instance in heap at attach time'});
      }
    });
  } catch (e) { emit({kind:'experiment_error', experiment:'E5_dsl_parser', error:safe(e)}); }

  /* ---------- 6. interaction selector Lgm/h.a(List) ---------------------- */
  try {
    var GH = Java.use('gm.h'), AL2 = Java.use('java.util.ArrayList');
    var empty = AL2.$new();
    emit({kind:'call', experiment:'E6_interaction_selector', cls:'gm.h', method:'a',
          case_name:'empty_list', ret:safe(GH.a(empty))});
  } catch (e) { emit({kind:'experiment_error', experiment:'E6_interaction_selector', error:safe(e)}); }

  var B = 'com.getmimo.ui.lesson.interactive.base.c';
  [['Y','onLessonRun'], ['V','lessonSolvedCorrectly'], ['X','lessonSolvedIncorrectly'],
   ['U','lessonSolvedAndProceed'], ['W','partialMatch'], ['H','createLessonProgress'],
   ['b0','storeAnswerText'], ['c0','solutionFeedback'], ['d0','wrongFeedback'],
   ['e0','storeProgressInMemory'], ['f0','trackLessonResult'], ['a0','lessonReset'],
   ['O','initialiseViewModel'], ['N','resetInputState'], ['I','cleanup'], ['S','feedbackCondition'],
   ['P','feedbackSuspend'], ['i0','awaitBrowserOutput'], ['K','getLessonBundle']].forEach(function(x){ hook(B,x[0],x[1],true); });

  hook('com.getmimo.data.source.remote.progress.LessonProgressRepository','createLessonProgress','repo_createProgress',true);
  hook('com.getmimo.data.source.remote.progress.LessonProgressRepository','postUnsyncedLessonProgress','repo_postUnsynced',true);
  hook('com.getmimo.data.source.remote.progress.LessonProgressQueue','storeLessonProgress','queue_store',true);
  hook('com.getmimo.data.source.remote.progress.LessonProgressQueue','updateCorrectAnswersCount','queue_count',true);
  hook('com.getmimo.data.source.remote.progress.LessonProgressQueue','storeAndPostAllLessonProgress','queue_postAll',true);
  hook('com.getmimo.network.a','a','net_isOnline',false);
  hook('com.getmimo.network.a','b','net_isOnline_b',false);
  hook('qm.i','a','normalizer',false);
  hook('km.f','b','selectionValidator',false);
  hook('te.c','b','dslParser',false);
  hook('gm.h','a','interactionSelector',false);
  hook('com.getmimo.ui.lesson.interactive.base.InteractiveLessonBaseViewModel$onLessonRun$1','invokeSuspend','onLessonRunCoroutine',true);
  hook('com.getmimo.ui.lesson.interactive.base.InteractiveLessonBaseViewModel$onValidatedInputExecuted$1','invokeSuspend','onValidatedInputCoroutine',true);
  hook('com.getmimo.ui.lesson.interactive.validatedinput.InteractiveLessonValidatedInputFragment$setupViews$2','invokeSuspend','setupViewsCoroutine',true);
  hook('com.getmimo.ui.lesson.executable.q','I','executableValidator',false);
  hook('im.d','E0','fillTheGapRun',true);
  hook('pm.b','E0','spellRun',true);
  hook('km.c','E0','selectionRun',true);
  hook('om.d','E0','selectionRun2',true);
  hook('mm.b','E0','selectionRun3',true);
  hook('com.getmimo.data.model.room.LessonProgress','isSolvedCorrectly','isSolved',true);
  hookSQL();
  hookLiveData();
  emit({kind:'done', hooks:hook._n});
});
