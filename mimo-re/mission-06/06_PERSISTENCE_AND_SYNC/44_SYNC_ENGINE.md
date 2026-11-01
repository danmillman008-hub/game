# Mission 6 — Sync Engine

## Scope
The complete synchronisation design: what is pushed, when, in what shape, and what comes back.

## Method
Endpoint catalogue + progress push DTOs + sync repository reads + analytics names.

## Findings (VERIFIED_STATIC)
```
payload   PostProgressRequestBody { progressList: List<…> }      → POST /v1/tutorials/{tutorialId}/progress
response  PostProgressResponse  { reachedGoal, dailyGoalCoinReward }
effect    on 2xx: delete pushed rows; if reachedGoal → coin reward already applied server-side
other     GET /v1/tracks/{trackId}/completion, /v1/tracks/{trackId}/eta, /v1/user/activity,
          /v1/…/keys, /v1/…/coins, /v1/leaderboards/{friends,latest}
```
- Batch is **per tutorial**, not global: the tutorial id is in the path.
- There is no pull-based diff, no `updated_at` watermark on the client, and no conflict token.
- Server data (completion, ETA, activity, coins) is read fresh; nothing is merged into local rows.

## Findings — what sync is not
No background scheduler was recovered for progress push (WorkManager classes exist in the APK but no
progress worker was found); pushes appear tied to app/session lifecycle (`Q-70`).

## Evidence labels
**VERIFIED_STATIC** for payload/response/endpoints. Push triggers: **UNKNOWN**.

## Open questions
`Q-70`, `Q-71` whether `progressList` mixes tutorials despite the path id.

## Reproduction
`grep -n 'tutorials/.*progress\|user/activity\|keys\|coins' ../mission-05/evidence/API_CATALOG_V2.csv`
