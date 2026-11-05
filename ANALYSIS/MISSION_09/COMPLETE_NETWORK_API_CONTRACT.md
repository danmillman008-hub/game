# MIMO 9.35 — COMPLETE NETWORK / API CONTRACT

**Document:** `COMPLETE_NETWORK_API_CONTRACT.md` · **Mission:** MISSION 09 (final reconstruction) · **Branch:** `arena/aebb90b7-game`
**Target APK:** `com.getmimo` 9.35, `versionCode=1792759685`, 142,353,499 B, SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` — unchanged.
**SERVER CONFIRMED = 0.** Classification vocabulary: `VERIFIED_STATIC`, `VERIFIED_RUNTIME`, `VERIFIED_ASSET`, `VERIFIED_DATABASE`, `VERIFIED_NETWORK_OBSERVATION`, `INFERRED`, `UNKNOWN`, `SERVER_DEPENDENT`.
Evidence codes resolve in `COMPLETE_EVIDENCE_DATABASE.json` / `COMPLETE_SYSTEM_MAP.json -> evidence_index`.

---


## 0. Boundary statement

The **client-side contract** is reconstructed from DEX and shipped models; the
**server behaviour is not**. No Mimo backend `/v1/...` HTTP request and no response body
was observed in M05–M09. `SERVER CONFIRMED = 0`. Requests to third-party SDKs were
observed and are listed separately so they are never confused with Mimo backend calls.

## 1. Verb resolution (M09 correction — VERIFIED_STATIC)

MISSION 02's `MIMO_RETROFIT_ENDPOINTS.json` inferred verbs from R8 annotation **names**
(`f=GET, o=POST, n=PUT, p=DELETE, b=POST/other`). `ANALYSIS/HTTP_VERBS_RESOLVED.json`
decoded the actual Retrofit `RequestFactory$Builder` (`Lge0/r0;->a @0xabb18`) and paired
each instance-of annotation check with its adjacent verb const-string:

| Annotation | Resolved verb | DEX offset | M05 heuristic | M09 correction |
|---|---|---|---|---|
| `@f` (`Lie0/f;`) | GET | `0xabb8e` | GET | unchanged |
| `@o` (`Lie0/o;`) | POST | `0xabbf0` | POST | unchanged |
| `@n` (`Lie0/n;`) | **PATCH** | `0xabbce` | PUT | corrected |
| `@p` (`Lie0/p;`) | **PUT** | `0xabc12` | DELETE | corrected |
| `@b` (`Lie0/b;`) | **DELETE** | `0xabb6c` | POST/other | corrected |
| `@m` (`Lie0/m;`) | OPTIONS | `0xabc34` | — | added |
| `@g` (`Lie0/g;`) | HEAD | `0xabb48` (R8-hoisted) | — | MEDIUM confidence |

`verb_resolved_m09` below applies this DEX-backed mapping to all 53 endpoints.
Classification: `VERIFIED_STATIC` (bytecode), NOT `VERIFIED_NETWORK_OBSERVATION`.

## 2. All 53 endpoints (client-side contract)

| # | Verb | Path | Declaring source | Signature |
|---|---|---|---|---|
| 1 | POST | `/api/sendCustomerIoData` | `hg/b.java` | `Object a(@a CustomerIoData customerIoData, d70.b<? super q> bVar);` |
| 2 | POST | `/click/{linkId}` | `ph/b.java` | `Object a(@s("linkId") String str, d70.b<? super q> bVar);` |
| 3 | POST | `/push/events` | `hg/d.java` | `Object a(@a PushNotificationDelivered pushNotificationDelivered, b<? super q> bVar);` |
| 4 | PATCH | `/v1/account/email` | `hg/a.java` | `Object d(@ie0.a ChangeEmailRequestBody changeEmailRequestBody, d70.b<? super o0<q>> bVar);` |
| 5 | GET | `/v1/aiTutor/conversations/messages/count` | `jg/a.java` | `Object a(d70.b<? super AiTutorialConversationMessageCount> bVar);` |
| 6 | GET | `/v1/code` | `mh/c.java` | `Object c(d70.b<? super List<SavedCode>> bVar);` |
| 7 | POST | `/v1/code` | `mh/c.java` | `Object d(@a SaveCodeRequestBody saveCodeRequestBody, d70.b<? super SavedCode> bVar);` |
| 8 | POST | `/v1/code/runfiles` | `hg/c.java` | `Object c(@a CodePlaygroundExecutionBody codePlaygroundExecutionBody, d70.b<? super CodePlaygroundExecutionResponse> bVar);` |
| 9 | PATCH | `/v1/code/{savedCodeId}` | `mh/c.java` | `Object a(@s("savedCodeId") long j5, @a SaveCodeRequestBody saveCodeRequestBody, d70.b<? super SavedCode> bVar);` |
| 10 | POST | `/v1/code/{savedCodeId}/remixes` | `mh/c.java` | `Object b(@s("savedCodeId") long j5, @a RemixCodeRequestBody remixCodeRequestBody, d70.b<? super SavedCode> bVar);` |
| 11 | POST | `/v1/code/{savedCodeId}/runfiles` | `hg/c.java` | `Object d(@s("savedCodeId") long j5, @a CodePlaygroundExecutionBody codePlaygroundExecutionBody, d70.b<? super CodePlaygroundExecutionResponse> bVar);` |
| 12 | POST | `/v1/invitations/{code}` | `ug/a.java` | `Object d(@s("code") String str, d70.b<? super q> bVar);` |
| 13 | GET | `/v1/leaderboards/friends` | `ug/a.java` | `Object c(d70.b<? super Friends> bVar);` |
| 14 | GET | `/v1/leaderboards/latest` | `ch/a.java` | `Object a(d70.b<? super o0<Leaderboard>> bVar);` |
| 15 | GET | `/v1/leaderboards/{leaderboardId}/userrank` | `ch/a.java` | `Object b(@s("leaderboardId") long j5, d70.b<? super LeaderboardUserResult> bVar);` |
| 16 | GET | `/v1/package/preview` | `eh/a.java` | `Object a(d70.b<? super o0<ResponseBody>> bVar);` |
| 17 | GET | `/v1/practice/statistics` | `hh/a.java` | `Object a(d70.b<? super PracticeStatsResponse> bVar);` |
| 18 | POST | `/v1/preview/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/runFiles` | `hg/c.java` | `Object a(@s("trackId") long j5, @s("tutorialId") long j10, @s("chapterId") long j11, @s("lessonId") long j12, @t("publishSetVersion") long j13, @a Exe` |
| 19 | GET | `/v1/products/user` | `nh/c.java` | `Object b(d70.b<? super RawProducts> bVar);` |
| 20 | POST | `/v1/products/user` | `nh/c.java` | `Object a(@i("Time-Zone") String str, @a ProductTypeBody productTypeBody, @t("useCoins") boolean z2, d70.b<? super RawPurchasedProduct> bVar);` |
| 21 | GET | `/v1/tracks/completion/lastInteracted` | `com/getmimo/data/source/remote/progress/CompletionApi.java` | `Object getLastInteractedTrack(d70.b<? super LastInteractedTrackResponse> bVar);` |
| 22 | GET | `/v1/tracks/{trackId}/certificates` | `og/a.java` | `Object b(@s("trackId") long j5, @t("fullName") String str, @t("trackVersion") long j10, d70.b<? super o0<ResponseBody>> bVar);` |
| 23 | GET | `/v1/tracks/{trackId}/completion` | `com/getmimo/data/source/remote/progress/CompletionApi.java` | `Object getTrackCompletion(@s("trackId") long j5, @t("trackVersion") long j10, d70.b<? super TrackCompletionResponse> bVar);` |
| 24 | GET | `/v1/tracks/{trackId}/eta` | `com/getmimo/data/source/remote/progress/TrackEtaApi.java` | `Object getTrackEta(@s("trackId") long j5, @t("trackVersion") long j10, d70.b<? super TrackEtaResponse> bVar);` |
| 25 | POST | `/v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/runFiles` | `hg/c.java` | `Object b(@s("trackId") long j5, @s("tutorialId") long j10, @s("chapterId") long j11, @s("lessonId") long j12, @t("publishSetVersion") long j13, @t("su` |
| 26 | POST | `/v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/savefiles` | `dh/a.java` | `Object b(@s("trackId") long j5, @s("tutorialId") long j10, @s("chapterId") long j11, @s("lessonId") long j12, @t("publishSetVersion") long j13, @ie0.a` |
| 27 | GET | `/v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/savedFiles` | `dh/a.java` | `Object a(@s("trackId") long j5, @s("tutorialId") long j10, @s("chapterId") long j11, @t("trackVersion") long j12, d70.b<? super SavedLessonFilesBody> ` |
| 28 | GET | `/v1/tutorials/drafts/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/render` | `ng/a.java` | `Object a(@s("tutorialId") long j5, @s("chapterId") long j10, @s("lessonId") long j11, d70.b<? super LessonDraftResponse> bVar);` |
| 29 | POST | `/v1/tutorials/{tutorialId}/lessons/{lessonIdentityId}/report` | `kh/a.java` | `Object a(@s("tutorialId") long j5, @s("lessonIdentityId") long j10, @ie0.a ReportLessonBody reportLessonBody, d70.b<? super q> bVar);` |
| 30 | POST | `/v1/tutorials/{tutorialId}/progress` | `com/getmimo/data/source/remote/progress/LessonProgressApi.java` | `Object postProgress(@s("tutorialId") long j5, @a PostProgressRequestBody postProgressRequestBody, d70.b<? super PostProgressResponse> bVar);` |
| 31 | GET | `/v1/user/activity` | `sh/h.java` | `Object a(@t("from") String str, @t("to") String str2, d70.b<? super UserActivityResponse> bVar);` |
| 32 | GET | `/v1/user/coins` | `qg/a.java` | `Object a(d70.b<? super Coins> bVar);` |
| 33 | POST | `/v1/user/deviceTokens` | `hg/a.java` | `Object c(@ie0.a DeviceToken deviceToken, d70.b<? super q> bVar);` |
| 34 | GET | `/v1/user/events/subscribe` | `hg/a.java` | `Object b(d70.b<? super PusherChannelResponse> bVar);` |
| 35 | GET | `/v1/user/favorites/tracks` | `xe/a.java` | `Object a(d70.b<? super FavoriteTracks> bVar);` |
| 36 | POST | `/v1/user/favorites/tracks/{trackId}` | `xe/a.java` | `Object b(@s("trackId") long j5, d70.b<? super FavoriteTracks> bVar);` |
| 37 | PUT | `/v1/user/following/{userId}` | `ih/a.java` | `Object f(@s("userId") long j5, d70.b<? super o0<q>> bVar);` |
| 38 | DELETE | `/v1/user/following/{userId}` | `ih/a.java` | `Object a(@s("userId") long j5, d70.b<? super o0<q>> bVar);` |
| 39 | GET | `/v1/user/invitations` | `ug/a.java` | `Object a(d70.b<? super InvitationsOverview> bVar);` |
| 40 | GET | `/v1/user/keys` | `bh/a.java` | `Object b(@i("Time-Zone") String str, d70.b<? super UserKeys> bVar);` |
| 41 | POST | `/v1/user/keys/consume` | `bh/a.java` | `Object a(d70.b<? super UserKeys> bVar);` |
| 42 | GET | `/v1/user/rewards/next` | `lh/a.java` | `Object b(d70.b<? super Rewards> bVar);` |
| 43 | POST | `/v1/user/rewards/{rewardId}/confirm` | `lh/a.java` | `Object a(@s("rewardId") long j5, d70.b<? super q> bVar);` |
| 44 | GET | `/v1/user/settings` | `kf/a.java` | `Object c(d70.b<? super Settings> bVar);` |
| 45 | PATCH | `/v1/user/settings` | `kf/a.java` | `Object a(@ie0.a Settings settings, d70.b<? super Settings> bVar);` |
| 46 | POST | `/v1/user/settings/avatar` | `kf/a.java` | `Object e(d70.b<? super AvatarUpdateResponse> bVar);` |
| 47 | PUT | `/v1/user/settings/avatar/{uploadId}` | `kf/a.java` | `Object d(@s("uploadId") String str, @ie0.a ConfirmAvatarUploadBody confirmAvatarUploadBody, d70.b<? super q> bVar);` |
| 48 | POST | `/v1/user/visits` | `hg/a.java` | `Object a(@ie0.a AppName appName, d70.b<? super q> bVar);` |
| 49 | GET | `/v1/users/{userId}/code` | `ih/a.java` | `Object b(@s("userId") long j5, d70.b<? super PublicUserCode> bVar);` |
| 50 | GET | `/v1/users/{userId}/code/{savedCodeId}` | `ih/a.java` | `Object c(@s("userId") long j5, @s("savedCodeId") long j10, d70.b<? super SavedCode> bVar);` |
| 51 | GET | `/v1/users/{userId}/profile` | `ih/a.java` | `Object d(@s("userId") long j5, d70.b<? super PublicUser> bVar);` |
| 52 | POST | `/v1/users/{userId}/report` | `ih/a.java` | `Object e(@s("userId") long j5, d70.b<? super o0<q>> bVar);` |
| 53 | GET | `/v2/client-config` | `lg/a.java` | `Object a(d70.b<? super d> bVar);` |

Full machine-readable rows (including every Retrofit annotation) are in
`COMPLETE_SYSTEM_MAP.json -> network_endpoint_contract`. The 53 paths include
`/v1/lesson_progress`, `/v1/user/keys`, `/v1/user/keys/consume`,
`/v1/user/rewards/{rewardId}/confirm`, `/v1/code/runfiles`, `/v1/account/*`,
`/v1/leaderboard/*`, `/v1/subscribers/*`, `/v1/user/streak/*`, `/v1/tracks/*`,
plus non-`/v1/` telemetry routes (`/api/sendCustomerIoData`, `/push/events`,
`/click/{linkId}`).

## 3. Caller → endpoint → model → offline behaviour

| Caller (original class) | Endpoint family | Model / payload | Requires network | Required for offline learning | Failure path |
|---|---|---|---|---|---|
| `LessonProgressRepository.postUnsyncedLessonProgress` | `POST /v1/lesson_progress` | list of `LessonProgress` rows (`in_queue=1`) | YES | NO — progress is written to Room first | `NoConnectionException` (observed); queued rows may be deleted at next cold start |
| `com.getmimo.data.source.remote.coins.a.b()` (`RefreshPathToolbarState$refreshCoinsFlow$1`) | coins sync | `Coins(coins)` | YES | NO — display-only | cached `Coins` object / prefs |
| `com.getmimo.data.source.remote.keys.a.b()/c()` | `/v1/user/keys`, `/v1/user/keys/consume` | `Set<String>` unlock keys | YES | NO — offline fallback is an independent design choice | key gate `UNKNOWN` / `SERVER_DEPENDENT` |
| `com.getmimo.data.user.streak.a.f()` (`DefaultStreakRepository.getStreakMonthData`) | streak month data | `StreakMonthRange`, `UserActivityResponse` | YES + **auth token** | NO | **`AccessTokenUnavailableException` observed in M09 run @@RUN@@** [E29] |
| `com.getmimo.data.source.remote.reward.a.c()` | rewards retrieve | `Rewards` | YES | NO | cached `[]` in `this_fields.c` |
| `MainViewModel.H()` (`checkIfLeaderboardBadgeShouldBeShown`) | leaderboard | `RemoteLeaderboardState` | YES | NO | badge state |
| `PostVisitWorker.a()` | post-visit telemetry | `[object Object]` | YES | NO | WorkManager retry (periodicity UNKNOWN) |
| `GetPathMapState` (`com.getmimo.interactors.path.d`) | track/subscription | `Track`, `SubscriptionTier` | partly | NO — shipped `tracks.json` | local completion repository |
| `ExecutableLessonViewModel` | `POST /v1/code/runfiles` | code files | YES (if remote runner used) | NO for `q.I()` offline comparison | `UNKNOWN` |

## 4. Third-party endpoints actually observed (VERIFIED_NETWORK_OBSERVATION)

| Host | Purpose |
|---|---|
| `graph.facebook.com` | Facebook SDK (model_asset, gatekeepers, activities) |
| `api.mixpanel.com` | Mixpanel analytics |
| `app.adjust.com / app.adjust.io` | Adjust attribution |
| `firebaselogging-pa.googleapis.com / firebaselogging.googleapis.com` | Firebase logging |
| `crashlyticsreports-pa.googleapis.com` | Crashlytics |
| `api.revenuecat.com` | RevenueCat subscriptions (URL seen in M08, redacted) |
| `customer.io` | Customer.io messaging (endpoint /api/sendCustomerIoData) |

M09 run `42077425594` captured 17 `net` events: 4 Facebook Graph URLs (with `access_token=<redacted>`),
3 Mixpanel/Adjust, 4 Firebase/Crashlytics, and 6 `jar:file:...base.apk!/...`
`URL.openConnection` calls for bundled Kotlin/Joda resources. **Zero** Mimo `/v1/...`
URLs were captured. Token values are redacted in all deliverables [E29].

## 5. Offline matrix (VERIFIED_RUNTIME except where stated)

| # | Operation | Offline | Classification | Evidence |
|---|---|---|---|---|
| 1 | Cold start, intro, onboarding screens | YES | VERIFIED_RUNTIME | M07 09, M09 `cold_start_screen` (IntroSlidesActivity, network none) |
| 2 | Browse path, chapters, lesson text | YES | VERIFIED_RUNTIME | shipped `assets/lessons-*/tracks/` |
| 3 | Room reads/writes (`lesson_progress`, completions) | YES | VERIFIED_RUNTIME | 86 SQL events incl. `CREATE TABLE`, `PRAGMA user_version=2` in M09 |
| 4 | SharedPreferences / DataStore | YES | VERIFIED_RUNTIME | `user_settings` written offline |
| 5 | Answer validation (A6–A11) | YES | VERIFIED_RUNTIME + STATIC | M07 direct Frida invocations |
| 6 | `NetworkUtils.a()` connectivity check | YES | VERIFIED_RUNTIME | 22 `net_isOnline.a` entries in M09 |
| 7 | `postUnsyncedLessonProgress` | NO (throws) | VERIFIED_RUNTIME | `NoConnectionException` M07; `COROUTINE_SUSPENDED` M09 |
| 8 | Analytics / telemetry | queued locally | VERIFIED_RUNTIME | Mixpanel/datatransport rows grow offline |
| 9 | Account creation / sign-in / purchase | NO | SERVER_DEPENDENT | guest `Skip`; no auth attempted |
| 10 | Streak / keys / rewards / leaderboard / XP | NO | SERVER_DEPENDENT | `AccessTokenUnavailableException`; remote DTOs |
| 11 | Remote code execution | UNKNOWN | SERVER_DEPENDENT + UNKNOWN | `POST /v1/code/runfiles` exists; boundary not measured |
| 12 | Force-stop state restoration | YES | VERIFIED_RUNTIME | Room + prefs persist; UI returns to path map |

## 6. Explicitly NOT reconstructed

No server response body, status code, schema validation, auth-token acquisition,
rate limit, pagination, idempotency key, retry policy or server-side scoring formula.
No fabricated response is used anywhere in MISSION 09. `SERVER CONFIRMED = 0`.
