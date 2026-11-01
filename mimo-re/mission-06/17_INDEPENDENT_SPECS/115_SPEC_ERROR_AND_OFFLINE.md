# Spec 115 — Errors and Offline

## MUST
1. Gate every request on connectivity and throw `NoConnectionException` before dialling.
2. Keep lessons fully usable offline (bundled content + local grading).
3. Queue progress offline; executable lessons fail offline.
4. Report crashes to Sentry.

## MUST NOT
- Add retry/backoff, offline banners as "verified", or cached coins/streaks.

## GIVEN EVIDENCE
`06_PERSISTENCE_AND_SYNC/46`, `07_NETWORK/51`.
