# Mission 6 — Lesson State Machine

## Scope
Formal state model of an interactive lesson exercise, derived from the base view model.

## Method
Transcribed terminals and their guards from `base.c` (`U`, `V`, `W`, `X`, `Z`, `H`, `a0`, `f0`, `g0`),
then normalised into states and transitions.

## Sources
`com.getmimo.ui.lesson.interactive.base.c`, `qm.d`, `qm.e/f/g`, `InteractiveLessonValidatedInputFragment$setupViews$2`.

## Findings — states
| State | Meaning | Fields |
|---|---|---|
| `IDLE` | lesson opened, no submission yet | `d=0`, `C=null` |
| `AWAITING` | user input present, verdict not yet applied (300 ms window for validated input) | `S=input` |
| `CORRECT` | last verdict correct | `C=false`, `d≥1` |
| `PARTIAL` | last verdict normalised-equal but not exact | input overwritten, `C=false` |
| `INCORRECT` | last verdict wrong | `C=true`, `d≥1` |
| `SOLVED` | learner proceeded (`U()`), progress written with `tries` | `tries = !C`, `d` |
| `RESET` | lesson restart (`a0()`), `lesson_reset` emitted | counters per restart policy (`Q-08`) |

## Findings — transitions
```
IDLE --submit--> AWAITING --(validated, 300ms)--> CORRECT | PARTIAL | INCORRECT
IDLE --tap-->   CORRECT | INCORRECT              (option types, immediate)
CORRECT  --proceed--> SOLVED
PARTIAL  --proceed--> SOLVED            (tries=1, input replaced by expected)
INCORRECT --retry--> AWAITING           (attempts increments each submit)
INCORRECT --proceed--> SOLVED           (tries=0 — the lesson is still "completed")
SOLVED   --restart--> RESET --> IDLE
```
Side effects: every verdict writes a progress row (`H`), emits an analytics interaction event (`f0`),
and pushes the attempt counter into the tracking state.

## Findings — non-states
No `MASTERY`, `HINTED` or `SKIPPED` state exists in the machine. Hints (if any) do not alter `attempts`
in the recovered code (`Q-37`).

## Evidence labels
**VERIFIED_STATIC** for every transition and side effect. `RESET` behaviour beyond the analytics event
is **UNKNOWN** (`Q-08`). A machine-readable transcription is in `38_PROGRESS_STATE_TRANSITIONS.json`.

## Limitations
The machine covers the *exercise* level; chapter/tutorial completion transitions live in Phase 5.

## Open questions
`Q-08`, `Q-37`, `Q-38`.

## Reproduction
`grep -nE 'public final void (U|V|W|X|Z)\(' /tmp/dad/com.getmimo.ui.lesson.interactive.base.c.java`
