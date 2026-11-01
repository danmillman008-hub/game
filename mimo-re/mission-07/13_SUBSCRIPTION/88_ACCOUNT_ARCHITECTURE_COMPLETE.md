# Mission 7 — Account Architecture

## Components (VERIFIED_STATIC where evidenced)
| Piece | Class/evidence |
|---|---|
| user model | `PublicUser{avatarUrl,biography,isPremium,isFollowedByMe,activeStreakLength,leaderboardFirstPlaceCount,leaderboardInfo}` |
| identity | bearer token from `ri.*`, injected by `fh.a` |
| profile fetch | public-user endpoint in the catalogue |
| account actions | delete/account endpoints present in catalogue (exact contract INFERRED) |
| registration/login | UI packages exist; **payload NOT_RECOVERED** (`Q-80`) |
| logout | no implementation recovered (`Q-124`) |
| account switching | no switch flow recovered |
