# MISSION 07 — 02 LIVE INSTRUMENTATION AND HOOK INVENTORY

**Status:** `VERIFIED_RUNTIME`. Source: `ANALYSIS/RUNTIME/MISSION_07/m07_frida_stage2.js`
(291 lines), `m07_frida_driver.py`, `FRIDA/java_bridge_frida17.js`,
`TRACES/STAGE3_ONLINE.jsonl`, `STAGE4_ONLINE.jsonl`, `STAGE4_OFFLINE.jsonl`,
`FRIDA/STAGE*_DRIVER.log`.

## Bridge and attach
```
frida==17.25.2 · frida-tools==14.11.0 · Python 3.14.4
frida-server-17.25.2-android-x86_64 (44,889,284 B xz -> 172,034,312 B ELF)
host-side persistent `adb shell /data/local/tmp/frida-server`
driver: pidof com.getmimo -> frida-ps -U -> get_usb_device().attach(pid)
        (3 retries, restart server between them)
agent: (function(){ <frida_tools/bridges/java.js> ;
         Object.defineProperty(globalThis,"Java",{value:bridge}); })();
       + m07_frida_stage2.js
```
Both online and offline sessions emitted `driver_start`, `attached`,
`bridge_loaded`, `ready`, `done`, `driver_done`. `script_error` no longer occurs
after the bridge was added. `Java.enumerateLoadedClassesSync()`:
36,825 loaded classes, 85 `com.getmimo.*` classes.

## Hook inventory (42 `hook_installed` records)
41 Java hooks plus the SQL layer. Tags and measured entry/exit counts in the
stage-4 online trace (117 entries / 117 exits):

| Hook tag | Class / method | stage-4 entries | what it proves |
|---|---|---|---|
| `net_isOnline` / `net_isOnline_b` | `com.getmimo.network.a.a/b` | 72 / 62 | connectivity checked on nearly every screen |
| `getLessonBundle` | `base/c.K()` | 50 | real `LessonBundle` values (see 03) |
| `repo_postUnsynced` | `LessonProgressRepository.postUnsyncedLessonProgress` | 2 online, 1 offline | offline throws `NoConnectionException` |
| `dslParser` | `te.c.b(String)` | 8 | real DSL parse during startup |
| `interactionSelector` | `gm.h.a(List)` | 6 | lesson-type decisions |
| `initialiseViewModel` | `base/c.O(LessonBundle)` | 6 | ViewModel init with parsed modules |
| `lessonSolvedAndProceed` | `base/c.U()` | 4 | non-interactive slide auto-completion |
| `createLessonProgress` | `base/c.H(int,int)` | 2 | constructed `LessonProgress` |
| `repo_createProgress` | `LessonProgressRepository.createLessonProgress` | 2 | 11-column mapping at runtime |
| `storeProgressInMemory` | `base/c.e0()` | 2 | Room/queue insert |
| `queue_store` | `LessonProgressQueue.storeLessonProgress` | 6 | queue behaviour |
| `queue_count` | `LessonProgressQueue` count | 4 | queue size |
| `isSolved` | `LessonProgress.isSolvedCorrectly()` | 4 | `tries>=1` |
| `trackLessonResult` | `base/c.f0(boolean,boolean)` | 2 | observed `f0(false, true)` |
| `resetInputState` | `base/c.N()` | 2 | input-state reset |
| `onLessonRun`, `lessonSolvedCorrectly`, `lessonSolvedIncorrectly`, `partialMatch`, `wrongFeedback`, `solutionFeedback`, `feedbackCondition`, `awaitBrowserOutput`, executable/fillTheGap/spell/selection `onRun` | hooks installed, **zero entries** | 0 | no native validator dispatch occurred: the only answer attempted was a WebView letter tap, handled inside JS |
| `sql` | `android.database.sqlite.SQLiteDatabase` (expanded method list) | 5,222 online / 1,394 offline | 1,067 online `mimo.db` SQL events |
| `sql_statement` | `android.database.sqlite.SQLiteStatement` | 1,735 online / 245 offline | Room compiled-statement execution |
| `liveData` | `androidx.lifecycle.m0.l/k` | 38 online / 4 offline | Boolean + `AuthenticationStep` values |

One `hook_error`: `androidx.lifecycle.MutableLiveData` is not present on the
app class path (R8 minifies it to `androidx.lifecycle.m0`); the `m0` hook still
installed and emitted 38 events. So the failed `MutableLiveData` hook is a
naming artefact, not a missing capability.

## Direct invocation experiments (per session)
53 `call` records online, 58 offline. E1 normalizer 21 cases, E2 selection
validator 8 cases, E3 `isSolvedCorrectly` 20 cases, E4 network gate 2 cases,
E5 DSL parser 0 online / 5 offline, E6 interaction selector 1 case,
`S2_loaded_classes` 1. Offline E5 succeeded because `Java.choose('te.c')`
found a live DI-created parser instance **after** app restart; at initial
online attach none existed (`experiment_error`). This is a real runtime
observation, not a failure of the parser.

## What was NOT instrumented
No Xposed/LSPosed, no JVMTI, no native/JNI hooks, no `strace`, no heap dump,
no `WebView.addJavascriptInterface` hook, no `System.loadLibrary` hook. See
`13_NATIVE_RUNTIME_FINDINGS.md`.

## Stage 6 — hooks attached at the answer moment (`VERIFIED_RUNTIME`, run `42033599909`)
Because onboarding restarts the app process, stage 6 waited for
`EXPERIMENTS/S6_LESSON_READY` (written by `m07_answer_driver.py` when the
classified lesson appears) and only then attached Frida. Result:
`TRACES/STAGE6_ONLINE.jsonl` has 32 `entry` / 32 `exit`, 14 `liveData`,
138 `sql`, 24 `sql_statement`, 73 `call`, 42 `hook_installed`; events run
13:19:50–13:21:09, i.e. **across the 13:20:08 answer**. Hook tag counts:
`getLessonBundle` 26, `isSolved` 6, `queue_store` 6, `lessonSolvedAndProceed` 4,
`createLessonProgress` 2, `repo_createProgress` 2, `storeProgressInMemory` 2,
`trackLessonResult` 2, `queue_count` 4, `dslParser` 4,
`interactionSelector` 2, `initialiseViewModel` 2, `resetInputState` 2.
Still **zero** entries for `onLessonRun`, `V`, `W`, `X`, `d0`,
`wrongFeedback`, `solutionFeedback` — a measured negative confirming that
lesson 151403's answer does not go through the native validator branches.

`WebView.addJavascriptInterface` hook installed but emitted no event during
that window (the WebView was created before attach). Recorded as `UNKNOWN`, not
as "no bridge exists".
