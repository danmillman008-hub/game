# Mission 6 — Learner Model

## Scope
What the client actually knows about a learner: stored entities, derived fields, and what is fetched.

## Method
DTO field extraction (`evidence/DTO_FIELDS.json`), Room schema, endpoint inventory
(`39_LEARNER_ENDPOINT_INVENTORY.csv`).

## Findings (VERIFIED_STATIC)
| Aspect | Representation | Source |
|---|---|---|
| identity | server account + token (`Authorization: Bearer` via `fh.a` + `ri.b`) | Phase 7 |
| name/avatar/bio | `PublicUser { avatarUrl, biography, isPremium, isFollowedByMe, activeStreakLength, leaderboardFirstPlaceCount, leaderboardInfo, … }` | DTO |
| premium | `PublicUser.isPremium` (boolean) — the only entitlement flag on the user object | DTO |
| activity | `UserActivityResponse { activeStreak: Streak, longestStreak: Streak, activity: List }` | DTO |
| keys (hearts) | `UserKeys { currentKeys: int }` | DTO |
| coins | `Coins { coins: int }` | DTO |
| last position | `LastInteractedTrackResponse { lastInteractedTrackId: Long }` | DTO |
| progress | local Room rows (3 tables) + server aggregate | Phase 6 |

The client stores **no learner profile locally** in Room: identity, coins, keys and streaks are
server-authoritative and held in memory/flows; only lesson/chapter/tutorial progress rows are persisted.

## Findings — derived (not stored)
- first-try correctness = `solved && attempts == 1`
- chapter/tutorial completion: flags on models, computed from rows
- daily goal reached: `PostProgressResponse { reachedGoal, dailyGoalCoinReward }` — decided **server-side**
  as part of the progress push response

## Evidence labels
All above **VERIFIED_STATIC**. Anything about how the server derives `activeStreak` is **UNKNOWN**.

## Open questions
`Q-52` local caching of coins/keys; `Q-53` whether `isPremium` is trusted client-side (RevenueCat
`CustomerInfo` exists — see Phase 14).

## Reproduction
`python3 -c "import json;d=json.load(open('evidence/DTO_FIELDS.json'));print(d['com.getmimo.data.model.user.UserKeys'])"`
