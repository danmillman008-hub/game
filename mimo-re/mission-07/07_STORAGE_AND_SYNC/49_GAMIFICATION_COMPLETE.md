# Mission 7 — Gamification (complete)

| Mechanic | Model | Authority | Client action |
|---|---|---|---|
| Coins | `Coins{coins:int}` | server | display |
| Keys | `UserKeys{currentKeys:int}` + `DefaultKeysRepository.consumeUserKey` | server | **consumption exists** |
| Daily goal | `PostProgressResponse{reachedGoal,dailyGoalCoinReward}` | server | display reward |
| Streak | `UserActivityResponse{activeStreak,longestStreak,activity[]}` | server | display |
| League | `LeaderboardUserResult{league,newLeague,usedLeagueFreeze}` | server | display |
| Sparks | `sparks:long` on leaderboard entry | server | display |
| Leaderboards | friends + latest boards | server ordering | display |
| Rewards | `Rewards{rewards[]}` | server | display |
| XP | — | — | **does not exist** |

## New in Mission 7 — keys are consumed
`com.getmimo.data.source.remote.keys.a` (`DefaultKeysRepository`) exposes `consumeUserKey` and returns a
`UserKeys` flow. This **supersedes** Mission 6's "no decrement path" statement. What remains open is *which UI
action* calls it (no lesson-VM edge found) — so: consumption exists at repository level; the trigger is
`PARTIALLY_CLOSED`.

## Promotion/demotion
Reported by the server in the leaderboard payload (`league` + `newLeague` + `usedLeagueFreeze`), never computed
client-side. No promotion endpoint exists.
