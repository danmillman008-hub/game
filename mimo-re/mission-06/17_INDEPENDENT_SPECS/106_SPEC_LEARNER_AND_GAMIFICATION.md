# Spec 106 — Learner and Gamification

## MUST
1. Coins: `{coins:int}`; keys: `{currentKeys:int}`; both server-authoritative, never computed locally.
2. Streaks: display `activeStreak`/`longestStreak` plus an activity calendar from the server.
3. Leagues/leaderboards: render server order; fields `rank, sparks, league, newLeague,
   usedLeagueFreeze, startDate, endDate, isInProgress`.
4. Daily goal: `reachedGoal` + `dailyGoalCoinReward` from the progress push.
5. Hard mode: per-lesson flag selecting an alternate module list.

## MUST NOT
- Implement XP, mastery scores, spaced repetition, or hearts consumption: none recovered.
- Sort leaderboard entries client-side.

## GIVEN EVIDENCE
`05_LEARNER_MODEL/32..39`.
