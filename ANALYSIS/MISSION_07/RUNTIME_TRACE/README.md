# MISSION 07 — RUNTIME_TRACE

* `STATIC_DECODE/` — M07 DEX recheck: `00_STATIC_DECODE_M07.md` plus verbatim
  smali dumps for `c.W()` (partial match), `c.V()` (exact), `c.d0()` (wrong),
  `GetPathMapState`, `CanOpenChapterWithKeys`, `ds/w.c` (unlock key), `sk/a`
  (dev prefs) and `cc/b.y` (section classification).
* `SHIPPED_CONTENT/SELECTION_ANSWERS.json` — 2,855 selection questions from the
  ORIGINAL APK's `assets/lessons-en/tracks/*.json`, with exact correct/wrong
  item texts; used by `m07_lesson_plan.py` so automation never guesses an answer.

Raw live traces: `ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE*.jsonl`.
