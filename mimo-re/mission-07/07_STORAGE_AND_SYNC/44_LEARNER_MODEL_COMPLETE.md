# Mission 7 — Learner Model (complete)

## Fields the client actually holds (VERIFIED_STATIC)
| Group | Field | Source | Client-computed? |
|---|---|---|---|
| identity | token (opaque) | `ri.*` holder | no |
| profile | `PublicUser{avatarUrl,biography,isPremium,isFollowedByMe,activeStreakLength,leaderboardFirstPlaceCount,…}` | server | no |
| economy | `Coins{coins}`, `UserKeys{currentKeys}`, `Rewards{rewards}` | server | no |
| activity | `UserActivityResponse{activeStreak,longestStreak,activity[]}` | server | no |
| position | `LastInteractedTrackResponse{lastInteractedTrackId}` | server | no |
| progress | `LessonProgress` (per lesson/tutorial) | **local + pushed** | yes (counters) |
| preferences | onboarding flags, remote config cache, FCM token | local | partly |

## What does not exist
No XP, no level, no mastery score, no skill profile, no review queue, no per-exercise score. A learner in this
build is: *a position in the content graph + a set of per-lesson attempt counters + server-side economy values*.

## Consequence for progression
Progression is **content-order + completion flags**, not performance-based. `hasProgress` on a section and
`isCompleted` on a chapter are the only gates recovered.
