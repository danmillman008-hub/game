# MISSION 07 — LIVE RUNTIME RECONSTRUCTION AND OFFLINE STATE FORENSICS

Branch `arena/aebb90b7-game` · baseline M06 `cfc8ea41` · original APK unchanged
(SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`,
142,353,499 B). **`SERVER CONFIRMED = 0`** — no server was contacted or
reconstructed; M01–M06 evidence is preserved verbatim.

## Deliverables (18)
| # | File | Content |
|---|---|---|
| 00 | `00_MISSION_07_PLAN.md` | plan, hypotheses, stage table, classification vocabulary |
| 01 | `01_RUNTIME_ENVIRONMENT.md` | local/runner device, root, SELinux, Frida 17 bridge, offline isolation |
| 02 | `02_LIVE_INSTRUMENTATION_AND_HOOKS.md` | 42 hooks, event totals, direct-invocation inventory |
| 03 | `03_INTERACTIVE_LESSON_VIEWMODEL_RUNTIME.md` | live `LessonBundle`, `LessonProgress`, `c.U/H/e0/f0/N` chain, LiveData |
| 04 | `04_ANSWER_VALIDATION_RUNTIME.md` | E1–E6 truth tables, normaliser, selection validator, `tries>=1`, DSL |
| 05 | `05_ANSWER_STATE_TRANSITIONS.md` | wrong/correct UI, feedback objects, stage-5 full chain |
| 06 | `06_DATABASE_BEFORE_AFTER.md` | Room schema, all snapshots, exact answer row, SQL statements |
| 07 | `07_PERSISTENCE_RESTORATION_AND_QUEUE.md` | offline queue, `NoConnectionException`, queue deletion |
| 08 | `08_PROGRESSION_AND_UNLOCK_LOGIC.md` | `LessonBundle`, key shape, path-map state, adaptive onboarding |
| 09 | `09_OFFLINE_EXECUTION_RESULTS.md` | A/B/C/D/E classification of every tested operation |
| 10 | `10_CODE_EDITOR_AND_WEBVIEW_BOUNDARY.md` | shipped WebView JS, DSL parser results, code editor UI |
| 11 | `11_SCORING_AND_REWARD_LOGIC.md` | local arithmetic vs remote DTOs, `UNKNOWN` formulas |
| 12 | `12_UI_STATE_MACHINE.md` | measured tap chains and lesson state transitions |
| 13 | `13_NATIVE_RUNTIME_FINDINGS.md` | native/ABI facts, unexercised techniques |
| 14 | `14_EXPERIMENT_LOG_AND_LIMITATIONS.md` | all 7 runs, event totals, explicit limitations |
| 15 | `15_ANSWER_TO_SCORING_RECONSTRUCTION.md` | executable local spec + honest `UNKNOWN` list |
| 16 | `16_EVIDENCE_DATABASE.json` | machine-readable claims with statuses, paths and SHA prefixes |
| 17 | `17_ACCEPTANCE_CRITERIA.md` | PASS / PARTIAL / NOT MET self-assessment |
| 18 | `18_OPEN_QUESTIONS.md` | resolved M06 questions + 25 residual unknowns |

## Supporting directories
* `RUNTIME_TRACE/STATIC_DECODE/` — M07 DEX recheck (`W`, `V`, `d0`, path state,
  unlock keys, `sk/a`, `cc/b.y`) with verbatim smali dumps.
* `RUNTIME_TRACE/SHIPPED_CONTENT/SELECTION_ANSWERS.json` — 2,855 shipped
  selection questions with exact correct/wrong item texts (from the ORIGINAL
  APK), used so automation never guesses an answer.
* `DATABASE_EVIDENCE/` — Room schema and row-diff extracts.
* `EXPERIMENTS/`, `SCRIPTS/` — experiment summaries and
  `build_evidence_database.py`.
* `DIAGRAMS/01..05.mmd` — runtime pipeline, answer state machine, Room state,
  offline queue sequence, instrumentation.
* `ANALYSIS/RUNTIME/MISSION_07/` — **all raw evidence**: `ENV/`, `FRIDA/`,
  `TRACES/`, `DB/SNAPSHOT_*`, `UI/`, `EXPERIMENTS/`, `LOGS/`, plus the harness
  scripts (`m07_*.sh`, `m07_*.py`, `m07_frida_stage2.js`,
  `FRIDA/java_bridge_frida17.js`).

## Headline results
* Frida 17 needs an explicit Java bridge; bundled `frida-tools 14.11.0`
  `java.js` made 42 Java hooks work (7,332 events in one run).
* `qm.i.a` Unicode-aware normaliser, `km.f.b` all-match selection predicate,
  `isSolvedCorrectly() = tries >= 1`, `te.c.b` DSL parser — all
  `VERIFIED_RUNTIME` with controlled inputs.
* A real wrong `Q` → `Try again`; correct `D` → `Correct!` / `D O G` →
  `Continue` → a **new `lesson_progress` row** for lesson 151403
  (`tries=1, attempts=1, in_queue=1, publishSetVersion=753`).
* Genuine offline: `Active default network: none` + `Network is unreachable`;
  `postUnsyncedLessonProgress` throws `NoConnectionException`; queued rows are
  deleted at cold start (`2 → 0`), which **does not** confirm M05/M06's
  assumption that unsynced rows restore after force-stop.
* Stage 6 (`42033599909`) attached Frida at the lesson moment and recorded the
  full `U()/H(1,1)/e0()/f0(false,true)` chain, the real `LessonBundle` for
  lesson 151403, `gm.h.a → FillTheGap`, shipped fill-the-gap DSL output and
  `RunButton$State` / `LessonOutput` LiveData — while showing that native
  `V()/W()/X()` is **not** the WebView answer path.
* Scoring/XP/unlock/code-execution internals remain explicitly `UNKNOWN`.
