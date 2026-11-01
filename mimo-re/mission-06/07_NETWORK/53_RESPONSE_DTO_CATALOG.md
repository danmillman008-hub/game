# Mission 6 — Response DTO Catalogue

## Scope
What the server is expected to return, per endpoint, at field level.

## Method
`response_type` column + `DTO_FIELDS.json` field extraction + serializer presence.

## Findings (VERIFIED_STATIC)
All responses are wrapped in `Ld70/b<T>` (coroutine result envelope); the inner types include:
`Coins{coins}`, `UserKeys{currentKeys}`, `UserActivityResponse{activeStreak,longestStreak,activity}`,
`LeaderboardUserResult{leaderboardId,rank,league,newLeague,sparks,startDate,endDate,isInProgress,usedLeagueFreeze,avatar,…}`,
`TrackCompletionResponse{lastInteractedTutorialId,tutorials}`, `TrackEtaResponse{currentPaceMinutesPerDay,
trackEstimatedCompletionAt,sections}`, `ExecuteFilesResponse{consoleOutput,error,hasPassed,hostedProjectUrl,tests}`,
`PostProgressResponse{reachedGoal,dailyGoalCoinReward}`, `LastInteractedTrackResponse{lastInteractedTrackId}`,
`PublicUser{…}`, `Rewards{rewards}`, `AiTutorConversationMessage{content,conversationId,finishReason}`,
`AiTutorialConversationMessageCount{userMessageCount}`.

Field lists for 39 of 50 types are in `evidence/DTO_FIELDS.json`; the catalogue in
`../mission-05/evidence/DTO_CATALOG.csv` remains the per-endpoint index.

## Evidence labels
**VERIFIED_STATIC** (field names). Nullability/optionality **INFERRED**.

## Open questions
`Q-88` pagination shape (none of the recovered responses shows a cursor/page object).

## Reproduction
`grep -c ',' ../mission-05/evidence/DTO_CATALOG.csv`
