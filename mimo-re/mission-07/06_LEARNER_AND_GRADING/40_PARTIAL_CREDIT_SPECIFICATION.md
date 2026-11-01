# Mission 7 — Partial Credit

## Finding
**No partial credit exists.** Evidence:
1. `LessonProgress` has no score/percentage column (11 columns, all counters/ids/versions).
2. `qm.d` has exactly four branches and none produces a fraction.
3. The word "partial" in the state machine refers to the *normalised* verdict (full success after
   normalisation), which Mission 6 already documented; Mission 7 confirms it is not a scoring notion.

## What looks like partial credit but is not
| Thing | Reality |
|---|---|
| `tries` (0/1) | first-attempt-correct *derived* flag, not a score |
| `attempts` | count of submissions |
| `hasPassed` (executable) | boolean from the server |
| `ChapterType.PRACTICE_LEVEL_*` | authored difficulty tier of the chapter |

## Implication
Any reconstruction that adds scoring would be adding a mechanic that does not exist in this build.
