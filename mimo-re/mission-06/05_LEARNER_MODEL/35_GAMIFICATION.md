# Mission 6 — Gamification

## Scope
Every gamified mechanic present in the client contract.

## Method
DTO field extraction + endpoint inventory (leaderboard/coin/streak/key paths), plus analytics event names
as secondary evidence.

## Findings (VERIFIED_STATIC)
| Mechanic | Client representation | Endpoint |
|---|---|---|
| Coins | `Coins { coins: int }` | `/v1/…/coins` (see 39 CSV) |
| Keys (lives) | `UserKeys { currentKeys: int }` | keys endpoint |
| Daily goal | `PostProgressResponse { reachedGoal, dailyGoalCoinReward }` | folded into progress push |
| Streak | `UserActivityResponse { activeStreak, longestStreak }`, `Streak` model | user activity endpoint |
| Leagues | `LeaderboardUserResult { league, newLeague, usedLeagueFreeze, sparks, rank, … }` | leaderboards |
| Leaderboards | `Leaderboard`, `LeaderboardUserResult`, friends + latest boards | `/v1/leaderboards/friends`, `/v1/leaderboards/latest` |
| Sparks | `sparks: long` on leaderboard entries — the league scoring currency | leaderboards |
| League freeze | `usedLeagueFreeze: boolean` (protects a streak/league week) | leaderboards |

## Findings — notable structure
- **Two currencies**: coins (spendable, server-authoritative) and sparks (league score). They are not
  interchangeable in any recovered code.
- **`newLeague` alongside `league`** means league change is reported *by the server in the leaderboard
  payload*, not by a promotion endpoint.
- **`currentKeys`** is an integer with no local decrement path in the lesson code: keys are *not* consumed
  by the graded interaction path in this build (no write found). That contradicts the "hearts" mechanic a
  clone would assume — mark it as an open question, not a fact.
- **No XP field exists** anywhere in the recovered DTOs; "XP" is not part of this client's model.

## Evidence labels
Table: **VERIFIED_STATIC**. "Keys are not consumed by interactive lessons": **VERIFIED_STATIC** for the
recovered code paths, **UNKNOWN** for the server.

## Open questions
`Q-57` key consumption; `Q-58` coin spending surface (shop DTOs?); `Q-59` `Streak` fields.

## Reproduction
`cut -d, -f6 05_LEARNER_MODEL/39_LEARNER_ENDPOINT_INVENTORY.csv`
