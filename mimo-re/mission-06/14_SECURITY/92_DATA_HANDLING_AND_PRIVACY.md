# Mission 6 — Data Handling and Privacy

## Scope
What learner data the client holds and where it goes.

## Findings (VERIFIED_STATIC)
| Data | Stored locally | Leaves device |
|---|---|---|
| progress rows (lesson ids, attempts, versions) | Room (`lesson_progress`, 2 completion tables) | yes — `POST /v1/tutorials/{id}/progress` |
| account identity | token in prefs (mechanism unknown) | yes — every authenticated call |
| coins/keys/streaks/leagues | no | fetched, not written |
| AI tutor messages | no local table | yes — tutor endpoints (server-side history) |
| analytics events | no | yes — Firebase/Adjust/Sentry |
| code editor content | saved code endpoints | yes — `POST/PATCH /v1/code…` |

- `allowBackup=false` limits local data exfiltration via backup (**VERIFIED_STATIC**).
- No consent/opt-out surface was recovered (`Q-134`) — significant for a GDPR review.
- No PII field was extracted at any point in this mission (RULE 3).

## Evidence labels
Table **VERIFIED_STATIC**; consent **NOT_RECOVERED**.
