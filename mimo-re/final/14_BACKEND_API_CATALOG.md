# 14 — Backend API catalogue (71 endpoint literals)

## 0. Provenance and confidence

All 71 paths below are extracted from DEX **string literals**. None of them has a `const-string`
instruction referencing it in any of the 12 DEX files — a machine-checked fact
(`tools/literal_reverse_index.py`, output `evidence/literal-index.json`: 0 of 71 endpoint
literals appear as code strings). They therefore live in **annotation space**, which is exactly
where Retrofit declares `@GET/@POST("…")`. Conclusion:

* **path: VERIFIED STATIC** (the literal exists and cannot be a runtime-built string);
* **HTTP verb: INFERRED** from name semantics (and, for the ones documented elsewhere in this
  report, from request payload shape);
* **request/response shape: VERIFIED** only where a data class exists (`data-contracts.json`);
  otherwise UNKNOWN.

Base hosts (V): `api.mimo.org`, `api-testing.mimo.org`, `mimoauth.getmimo.com`,
`images.getmimo.com`. A dual prod/testing base-URL pair is present, switchable at runtime (dev
menu / build variant, I).

## 1. Auth and account

| Path | Verb (I) | Purpose |
|---|---|---|
| `/auth/token` | POST | token exchange (`grant_type`-style flow) |
| `/auth/login` | POST | credential login |
| `/auth/revoke` | POST | logout / revoke |
| `/v1/account` | GET/DELETE | account summary / deletion |
| `/v1/account/email` | PUT | change email |
| `/v1/user/settings` | GET/PUT | profile & settings |
| `/v1/user/settings/avatar` | POST | avatar upload (init) |
| `/v1/user/settings/avatar/{uploadId}` | PUT | avatar upload (commit) |
| `/v1/users/{userId}/profile` | GET | public profile |
| `/v1/users/{userId}/report` | POST | report a user |
| `/v1/user/deviceTokens` | POST/DELETE | push registration |

## 2. Content and progress

| Path | Purpose |
|---|---|
| `/v1/tracks/` | track list / metadata |
| `/v1/tracks/{trackId}/completion` | per-track completion summary |
| `/v1/tracks/completion/lastInteracted` | "continue learning" resolution |
| `/v1/tracks/{trackId}/eta` | ETA model (`TrackEtaResponse`) |
| `/v1/tracks/{trackId}/certificates` | certificates for a track |
| `/v1/tutorials/{tutorialId}/progress` | **progress write/read** (outbox target) |
| `/v1/tutorials/{tutorialId}/lessons/{lessonIdentityId}/report` | report a lesson |
| `/v1/tutorials/drafts/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/render` | **server-side draft render** |
| `/v2/client-config` | client config bundle (tabs, flags, streak?) |
| `/v1/config/%s` | legacy config by key (`%s` = `String.format` placeholder) |

## 3. Execution and code

| Path | Purpose |
|---|---|
| `…/lessons/{lessonId}/runFiles` (under `/v1/tracks/…`) | grade an executable lesson |
| `/v1/preview/tracks/…/runFiles` | grade **unpublished** lesson (authoring) |
| `…/lessons/{lessonId}/savefiles` | persist learner files server-side |
| `…/lessons/{lessonId}/savedFiles` | read persisted files |
| `/v1/code` | create/list saved projects |
| `/v1/code/{savedCodeId}` | project CRUD |
| `/v1/code/runfiles` | run an ad-hoc project |
| `/v1/code/{savedCodeId}/runfiles` | run a saved project |
| `/v1/code/{savedCodeId}/remixes` | remix a project |
| `/v1/users/{userId}/code` , `/v1/users/{userId}/code/{savedCodeId}` | public project gallery |

## 4. Practice

| Path | Purpose |
|---|---|
| `/v1/practice/statistics` | `PracticeStatsResponse(duration, chaptersCompleted)` |

There is **no** practice-content endpoint — the client re-serves chapters from the pack (§09).

## 5. Gamification

| Path | Purpose |
|---|---|
| `/v1/user/coins` | coin balance |
| `/v1/user/keys` | key balance (`UserKeys(currentKeys)`) |
| `/v1/user/keys/consume` | **spend a key** (explicit, auditable) |
| `/v1/user/rewards/next` | fetch next reward (`Reward(…)` incl. `rewardMultiplier`) |
| `/v1/user/rewards/{rewardId}/confirm` | claim reward |
| `/v1/leaderboards/latest` | current league board (`Leaderboard(…)`) |
| `/v1/leaderboards/friends` | friends board |
| `/v1/leaderboards/{leaderboardId}/userrank` | self rank |
| `/v1/user/activity` | activity feed / streak-relevant events (I) |
| `/v1/user/visits` | visit tracking (streak/retention) |
| `/v1/user/favorites/tracks`, `/v1/user/favorites/tracks/{trackId}` | favourites |
| `/v1/user/following/{userId}` | social follow |
| `/v1/user/invitations`, `/v1/invitations/{code}` | referral/invite links |

## 6. AI tutor

| Path | Purpose |
|---|---|
| `/v1/aiTutor/conversations` | start conversation (SSE stream) |
| `/v1/aiTutor/conversations/` | follow-up (trailing slash variant) |
| `/v1/aiTutor/conversations/messages/count` | freemium quota (`AiTutorialConversationMessageCount(userMessageCount)`) |

## 7. Monetisation and entitlements

| Path | Purpose |
|---|---|
| `/v1/offerings` | paywall offerings |
| `/v1/package/preview` | package preview |
| `/v1/products/user` | user products |
| `/v2/purchase` | purchase validation |
| `/v1/receipts`, `/v1/receipts/amazon/%s/%s` | receipt validation (Amazon Appstore variant!) |
| `/v1/subscribers/%s` … `/v1/subscribers/%s/offerings`, `/attributes`, `/alias`, `/identify`, `/redeem_purchase`, `/virtual_currencies` | RevenueCat subscriber proxy |
| `/v1/product_entitlement_mapping` | product↔entitlement map |

## 8. Ops, support, instrumentation

| Path | Purpose |
|---|---|
| `/v1/events` | analytics ingestion |
| `/v1/user/events/subscribe` | pushes/live updates (Pusher channel auth) |
| `/v1/diagnostics` | client diagnostics |
| `/v1/health/connectivity` | connectivity probe (used by the offline view) |
| `/v1/customercenter/%s`, `/v1/customercenter/support/create-ticket` | support centre |

## 9. Unused-by-count metrics and gaps

* **71 paths**; 8 are execution-related, 4 AI-tutor, 13 gamification, 12 monetisation, 10 content/
  progress, 10 auth/account, 5 ops.
* **No** content-download endpoint (content ships in the APK).
* **No** streak-specific endpoint — streak is delivered inside `/v1/tutorials/{id}/progress`,
  `/v2/client-config` or `/v1/user/activity` (U which).
* **No** notification-preference endpoint under `/v1/` (settings bundle covers it, I).
* **No** search endpoint; practice search is client-side over packed content (I).
* Dual **v1/v2** naming coexists (`/v2/purchase`, `/v2/client-config` vs everything else on v1) —
  evidence of incremental API evolution without a versioning policy.

## 10. Reconstructed OpenAPI sketch

`schemas/api-catalog.openapi.yaml` contains a machine-readable skeleton for these paths with
*schema-unknown* request bodies, verbs marked as inferred, and the data-class fields attached as
response hints where a contract exists. It is deliberately incomplete: inventing bodies would
violate the evidence rules of this report.

## 11. Konkur transfer

| Mimo endpoint group | Reuse | Note |
|---|---|---|
| Progress write + ETA + completion | Reuse | The three-way split (write/aggregate/eta) is right |
| Keys/coins/rewards/leaderboard | Adapt | One economy service, not five |
| Execution (`runFiles`) | Exclude | Not a coding exam |
| AI tutor conversations | Reuse (shape), rewrite prompts | SSE + conversation ids are fine |
| RevenueCat proxy | Exclude | No IAP channel in Iran; use local gateway (Zarinpal/IDPay) contracts |
| `/v1/events` (own collector) | Reuse | Analytics must be self-hosted for Iranian network conditions |
| Dual prod/test hosts | Reuse | Keep it explicit, not a dev-menu toggle |
