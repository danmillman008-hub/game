/*
 * MISSION 07 — Frida instrumentation of the ORIGINAL Mimo 9.35 process.
 * Stage 1: (a) prove Java-level hooking works, (b) directly invoke recovered
 * pure/static methods with CONTROLLED inputs and record real return values,
 * (c) install entry/exit hooks for the rest of the mission.
 * No APK modification, no fake server responses, no credentials.
 */
function emit(o) { try { send(JSON.stringify(o)); } catch (e) { send('{"kind":"emit_error","e":"' + e + '"}'); } }
function safe(v) {
  if (v === null || v === undefined) return String(v);
  try {
    var s = v.toString();
    if (s === undefined) s = String(v);
    if (s.length > 600) s = s.substring(0, 600) + '...[truncated]';
    return s;
  } catch (e) { return '<toString failed: ' + e + '>'; }
}
function argsOf(a) { return Array.prototype.slice.call(a).map(safe); }

function hookAll(cls, method, tag) {
  try {
    var C = Java.use(cls);
    var m = C[method];
    if (!m || !m.overloads) { emit({kind:'hook_error', tag:tag, cls:cls, method:method, error:'no overloads'}); return; }
    m.overloads.forEach(function (ov) {
      try {
        ov.implementation = function () {
          var id = tag + '#' + (++hookAll._n);
          emit({kind:'entry', tag:tag, cls:cls, method:method, id:id,
                overload: ov.argumentTypes ? ov.argumentTypes.map(function(t){return t.className;}).join(',') : '?',
                args:argsOf(arguments)});
          var ret;
          try {
            ret = ov.apply(this, arguments);
            emit({kind:'exit', tag:tag, cls:cls, method:method, id:id, ret:safe(ret)});
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
hookAll._n = 0;

Java.perform(function () {
  emit({kind:'ready', android: Java.androidVersion, arch: Process.arch,
        ptr: Process.pointerSize, pid: Process.id,
        vm: Java.vm ? Java.vm.getVersion ? Java.vm.getVersion() : 'n/a' : 'n/a'});

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
    function mk(text, selected, correct) { return A.$new(text, selected, correct, false); }
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

  /* ---------- 5. DSL parser Lte/c.b(String) on controlled DSL -------------- */
  try {
    var P = Java.use('te.c');
    var parser = P.$new(null, null, null, null, null, null);
    var samples = [
      ['only_paragraph', '<html><body><p>Hello <strong>world</strong></p></body></html>'],
      ['paragraph_and_code', '<html><body><p>Intro</p><code version="2" codelang="html" name="index.html" visible-if="always"><content><text value="&lt;h1&gt;Hi&lt;/h1&gt;" /></content></code></body></html>'],
      ['unknown_tag', '<html><body><foo>a</foo><p>ok</p></body></html>'],
      ['malformed', '<p>unclosed']
    ];
    samples.forEach(function (s) {
      try {
        var out = parser.b(s[1]);
        emit({kind:'call', experiment:'E5_dsl_parser', cls:'te.c', method:'b',
              case_name:s[0], input:s[1], size:out === null ? -1 : out.size(),
              ret:safe(out)});
      } catch (e) { emit({kind:'call_error', experiment:'E5_dsl_parser', case_name:s[0], error:safe(e)}); }
    });
  } catch (e) { emit({kind:'experiment_error', experiment:'E5_dsl_parser', error:safe(e)}); }

  /* ---------- 6. interaction selector Lgm/h.a(List) ---------------------- */
  try {
    var GH = Java.use('gm.h'), AL2 = Java.use('java.util.ArrayList');
    var empty = AL2.$new();
    emit({kind:'call', experiment:'E6_interaction_selector', cls:'gm.h', method:'a',
          case_name:'empty_list', ret:safe(GH.a(empty))});
  } catch (e) { emit({kind:'experiment_error', experiment:'E6_interaction_selector', error:safe(e)}); }

  /* ---------- 7. hooks for live method tracing --------------------------- */
  var B = 'com.getmimo.ui.lesson.interactive.base.c';
  [['Y','onLessonRun'], ['V','lessonSolvedCorrectly'], ['X','lessonSolvedIncorrectly'],
   ['U','lessonSolvedAndProceed'], ['W','partialMatch'], ['H','createLessonProgress'],
   ['b0','storeAnswerText'], ['c0','solutionFeedback'], ['d0','wrongFeedback'],
   ['e0','storeProgressInMemory'], ['f0','trackLessonResult'], ['a0','lessonReset'],
   ['O','initialiseViewModel'], ['N','resetInputState']].forEach(function (x) { hookAll(B, x[0], x[1]); });

  hookAll('com.getmimo.data.source.remote.progress.LessonProgressRepository', 'createLessonProgress', 'repo_createProgress');
  hookAll('com.getmimo.data.source.remote.progress.LessonProgressRepository', 'postUnsyncedLessonProgress', 'repo_postUnsynced');
  hookAll('com.getmimo.data.source.remote.progress.LessonProgressQueue', 'storeLessonProgress', 'queue_store');
  hookAll('com.getmimo.data.source.remote.progress.LessonProgressQueue', 'updateCorrectAnswersCount', 'queue_count');
  hookAll('com.getmimo.data.source.remote.progress.LessonProgressQueue', 'storeAndPostAllLessonProgress', 'queue_postAll');
  hookAll('com.getmimo.network.a', 'a', 'net_isOnline');
  hookAll('qm.i', 'a', 'normalizer');
  hookAll('km.f', 'b', 'selectionValidator');
  hookAll('te.c', 'b', 'dslParser');
  hookAll('gm.h', 'a', 'interactionSelector');
  hookAll('com.getmimo.ui.lesson.interactive.base.InteractiveLessonBaseViewModel$onLessonRun$1', 'invokeSuspend', 'onLessonRunCoroutine');
  hookAll('com.getmimo.ui.lesson.interactive.base.InteractiveLessonBaseViewModel$onValidatedInputExecuted$1', 'invokeSuspend', 'onValidatedInputCoroutine');
  hookAll('com.getmimo.ui.lesson.interactive.validatedinput.InteractiveLessonValidatedInputFragment$setupViews$2', 'invokeSuspend', 'setupViewsCoroutine');
  hookAll('com.getmimo.ui.lesson.executable.q', 'I', 'executableValidator');
  hookAll('com.getmimo.ui.lesson.executable.q', 'E', 'executableProgress');
  hookAll('im.d', 'E0', 'fillTheGapRun');
  hookAll('pm.b', 'E0', 'spellRun');
  hookAll('km.c', 'E0', 'selectionRun');
  hookAll('om.d', 'E0', 'selectionRun2');
  hookAll('mm.b', 'E0', 'selectionRun3');
  hookAll('com.getmimo.data.model.room.LessonProgress', 'isSolvedCorrectly', 'isSolved');

  emit({kind:'done', hooks: hookAll._n});
});
