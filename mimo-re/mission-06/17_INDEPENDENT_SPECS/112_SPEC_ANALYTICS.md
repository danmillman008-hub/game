# Spec 112 — Analytics

## MUST
1. Emit at least the verified `lesson_reset` event and per-interaction verdict events carrying
   `interactionType` and `solved`.
2. Treat property values as typed enums (e.g. `AiTutorInteractionSource`).
3. Route to Firebase Analytics, Adjust (attribution) and Sentry (crash).

## MUST NOT
- Reproduce the 252-candidate name list as an event inventory — it is a hypothesis list (`83`).

## GIVEN EVIDENCE
`12_ANALYTICS/82..85`, `evidence/EVENT_CANDIDATES.csv`.
