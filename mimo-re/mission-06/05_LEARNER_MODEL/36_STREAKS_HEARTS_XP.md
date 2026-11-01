# Mission 6 — Streaks, Hearts, XP (focused)

## Streaks — VERIFIED_STATIC (contract only)
`UserActivityResponse` carries `activeStreak` and `longestStreak` as `Streak` objects plus an `activity`
list (calendar of active days). `PublicUser.activeStreakLength` duplicates the active length on the
profile object. No client-side streak computation was found: the app displays what the server returns.

## Hearts / keys — VERIFIED_STATIC (contract), UNKNOWN (mechanics)
`UserKeys { currentKeys: int }`; an endpoint exists to read keys. **No decrement** appears in the lesson
runtime (`base.c` writes progress only). Either keys are server-side consumption driven by the progress
push, or the mechanic is unused in this build. Not resolved.

## XP — NOT RECOVERED
No `xp`, `experience`, `level` (learner-level) field was found in 50 extracted DTOs. `ChapterType`
`PRACTICE_LEVEL_*` is a content tier, `public user` has no level field. Conclusion for this build: **the
client has no XP model**; if a level exists it is a display name computed from coins/sparks elsewhere
(`Q-60`).

## Daily goal
`PostProgressResponse { reachedGoal: boolean, dailyGoalCoinReward: int }` — the reward is *granted by the
progress response*, i.e. the server decides and the client only displays.

## Evidence labels
As marked per section; the XP absence is **NOT_RECOVERED** (a searched-for absence across 50 DTOs and
3,133 classes, stated as such rather than as proof of non-existence).

## Open questions
`Q-57`, `Q-59`, `Q-60`.

## Reproduction
`grep -ic 'xp' <(python3 -c "import json;print(json.dumps(json.load(open('evidence/DTO_FIELDS.json'))))")`
