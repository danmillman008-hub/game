# MISSION 07 — 14 EXPERIMENT LOG AND OBSERVATION LIMITATIONS

All runs use the ORIGINAL APK, SHA-256
`48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`
(142,353,499 B, unchanged). `SERVER CONFIRMED = 0` in every run.
Workflow: `.github/workflows/mimo-runtime-verification.yml`, job `runtime`.

| # | Run | Marker / commit | Result |
|---|---|---|---|
| 1 | `42017453045` | `M07-RUNTIME-RUN-001` / `4716c2ec` | stage 1A: root/private storage measured; Frida `get_process('com.getmimo')` → `ProcessNotFoundError`, `spawn()` → `NotSupportedError`; 0 Frida messages |
| 2 | `42018369099` | `M07-RUNTIME-RUN-002` / `258012e4` | stage 1B: PID attach coded; `nohup frida-server &` inside `adb shell` reaped → `frida.ServerNotRunningError`; 1 message |
| 3 | `42019353340` | `M07-RUNTIME-RUN-003` / `3429d47a` | stage 2: host-side persistent server fixed attach (online pid 3289, offline 7074); both scripts failed `ReferenceError: 'Java' is not defined`; navigation reached adaptive onboarding but `lesson_reached=0`; `mimo.db` 672 seeded rows, `lesson_progress=0`; offline isolation proven |
| 4 | `42025423068` | `M07-RUNTIME-RUN-004` / `9d7e0e9b` | stage 3: bundled `frida-tools 14.11.0` Java bridge → 41 hooks, 914 events; E1/E3/E4/E6 verified; E2 coercion error, E5 no live parser; navigation reached a JavaScript snippet lesson, no classified quiz |
| 5 | `42028049247` | `M07-RUNTIME-RUN-005` / `520e698d` | stage 4: general shipped-answer classifier + live DSL parser + broader SQL hooks; reached WebView lesson 151403, tapped wrong `Q`; 1 real `lesson_progress` row (slide 151410); offline `NoConnectionException` + `DELETE … in_queue=1` measured; E2 (8 cases) and E5 (5 cases) verified |
| 6 | `42030594857` | `M07-RUNTIME-RUN-006` / `c4c79e47` | stage 5: full wrong `Q` → `Try again` → correct `D` → `Correct!`/`D O G` → `Continue` → next code-editor lesson; new row `151403`; offline cold start deletes both queued rows |
| 7 | `42033599909` | `M07-RUNTIME-RUN-007` / `f46c97ba` | stage 6 (recorded in `LOGS/DISPATCH.txt`): Frida attaches at the answer moment and targets a native selection lesson; see its `TRACES/STAGE6_*.jsonl` |

## Frida event totals (measured)
| trace | events | notable kinds |
|---|---|---|
| `STAGE3_ONLINE.jsonl` | 914 | 41 hooks, 818 `sql`, 46 `call` |
| `STAGE4_ONLINE.jsonl` | 7,332 | 42 hooks, 5,222 `sql`, 1,735 `sql_statement`, 117 `entry`/117 `exit`, 38 `liveData` |
| `STAGE4_OFFLINE.jsonl` | 1,701 | 1 `throw` (`NoConnectionException`), E5 parser results, 1,394 `sql` |
| `STAGE5_ONLINE.jsonl` | 1,685 | 1,346 `sql`, 236 `sql_statement`, **0 `entry`/`exit` after 12:58:01** |
| `STAGE5_OFFLINE.jsonl` | 1,219 | 24+24 network-gate entries, 903 `sql` |
| `STAGE6_ONLINE.jsonl` | 317 | 32 `entry`/32 `exit` across the 13:20:08 answer, 14 `liveData`, 42 hooks |
| `STAGE6_OFFLINE.jsonl` | 1,218 | 25+25 network-gate entries, 945 `sql` |

## Explicit limitations (not hidden)
1. **Process restart during onboarding.** Stage-5 hooks were attached to pid
   3175 at 12:55:18; the app restarted around 12:58, so no `entry`/`exit` hook
   records cover the 13:02 answer. The DB/UI chain is independently proven by
   root SQLite backups and `uiautomator` XML. Stage 6 attaches at the lesson
   moment to address this. **Stage 6 succeeded**: hooks cover the entire
   13:20:08 `U()/H()/e0()/f0()` chain and show no `V/W/X` dispatch.
2. **WebView answer path is JS-local.** No native `V()/W()/X()`, `jm/m/n/o`
   LiveData or `onLessonRun$1` dispatch was observed for lesson 151403. Do not
   claim native validator execution for WebView exercises.
3. **No chapter completion.** `chapter_completions` stayed 0; no chapter-end
   screen was reached.
4. **No server response.** No auth, no purchase, no server reconstruction, no
   response body. `SERVER CONFIRMED=0`.
5. **No native/JNI/Xposed/JVMTI/strace/heap dump.** These are `UNKNOWN`, not
   "unavailable" — see `13_NATIVE_RUNTIME_FINDINGS.md`.
6. **`mimo_dev_prefs.xml` absent.** Developer switches in `sk/a` were not
   exercised; no path-state runtime value is claimed.
7. **Adaptive onboarding.** M05's exact 24-tap chain does not replay against
   this build's onboarding; M07 uses measured XML coordinates instead. This is
   why stage 2's `lesson_reached=0` occurred.
8. **Stage labels in auto evidence commits** (`3e3a577a`, `536c0af9`,
   `aa9d3b84`, `15e3efbd`, `c237f461`, `33d3a683`, …) say "MISSION 03" — a
   workflow message artefact, not evidence of mission 3 work.
9. **Second-lesson search** in stage 5 ended `second_lesson_not_found`; no
   selection-answer claim is made from that run.
