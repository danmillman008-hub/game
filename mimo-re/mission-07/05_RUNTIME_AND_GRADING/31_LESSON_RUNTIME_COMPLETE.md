# Mission 7 — Lesson Runtime (complete)

## Sequence (VERIFIED_STATIC)
```
1 construct VM        LessonBundle → base.c
2 initialise          H(0,0) writes an empty progress row; pick CORRECT/WRONG paragraphs; select isDefault interaction
3 render              blocks + slots
4 act                 tap / type
5 submit              Z(verdict) — 300 ms delay only for VALIDATED_INPUT
6 verdict             V() correct | W() normalised-correct (input overwritten) | X() incorrect
7 write               H(tries, attempts) → ProgressRepository → Room (in_queue=1)
8 feedback            visibility switches to correct/wrong paragraph set
9 analytics           f0(interactionType, solved); a0() emits lesson_reset with 7 numeric properties
10 proceed            U(): tries = (lastVerdictCorrect ? 1 : 0), d++, mark solved
11 push               batch POST /v1/tutorials/{tutorialId}/progress; rows deleted on 2xx
```

## New in Mission 7 — exact `lesson_reset` payload (VERIFIED_STATIC)
`a0()` builds `ge.j("lesson_reset", 0)` with `NumberProperty` values: `lesson_id`, `tutorial_id`,
`tutorial_version`, `track_id`, `attempts`, `duration` (7 properties, `duration` from `J()`).
This is the first fully reconstructed analytics event including its property set.

## Invariants
`attempts` increments on every submit; `tries ∈ {0,1}`; a lesson can be completed while incorrect; no score.
