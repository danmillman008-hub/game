# Mission 6 — Leaderboard

## Scope
Board scopes, entry model, league mechanics and ranking source.

## Method
Endpoint rows + `Leaderboard`/`LeaderboardUserResult` fields + analytics names (`leaderboard_*`).

## Findings (VERIFIED_STATIC)
1. Two scopes in the catalogue: `GET /v1/leaderboards/friends` (returns `Friends`) and
   `GET /v1/leaderboards/latest` (returns `Leaderboard`); a third leaderboard endpoint exists (see CSV).
2. Entry model `LeaderboardUserResult { leaderboardId, rank, league, newLeague, sparks, startDate,
   endDate, isInProgress, usedLeagueFreeze, avatar }` — entries carry **both** a rank and a date window,
   so a board is *time-boxed* (`startDate`/`endDate`, `isInProgress`).
3. Ranking metric is `sparks` (long) — not coins, not lessons completed in the recovered payload.
4. League membership is per-entry (`league`), and `newLeague` reports the change that took effect for
   that result. `usedLeagueFreeze` is per-entry too, which means the freeze is consumed at board level.
5. The client does no sorting or rank computation: it renders server-ordered entries.

## Evidence labels
All **VERIFIED_STATIC**. Ordering guarantee and tie-breaking: **UNKNOWN**.

## Open questions
`Q-61` tie-breaking; `Q-62` whether friends' board is cached; `Q-63` freeze acquisition.

## Reproduction
`grep leaderboard 05_LEARNER_MODEL/39_LEARNER_ENDPOINT_INVENTORY.csv`
