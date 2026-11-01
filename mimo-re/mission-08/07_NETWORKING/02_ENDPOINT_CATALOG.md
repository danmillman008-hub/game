# Phase 2 — Endpoint catalogue

62 endpoints in **29 interfaces**. Machine-readable: `02_ENDPOINT_CATALOG.json` (adds client attribution, origin and
feature classification to every row). Verbs are `VERIFIED_STATIC` for 56 rows and `INFERRED_HIGH` for 6
(`verb_confidence = INFERRED_MEDIUM`).

## 0. Origin grouping

| Origin | Endpoints | How that origin is proven |
|---|---|---|
| `https://api.mimo.org` (shared Retrofit, C2) | 52 | DI case 19 + case 22 |
| `https://api.mimo.org` (long-timeout client, C3) | 1 | DI case 108 |
| `https://track.customer.io` (C4) | 1 | base-URL literal, DI case 53 |
| `https://mimoauth.getmimo.com/` (C5) | 1 | base-URL literal, DI case 87 |
| `https://email.getmimo.com` (C6) | 1 | base-URL literal, DI case 117 |
| third-party SDK clients (Customer.io in-app) | 6 | interfaces in `io.customer.*` packages |

Nothing here asserts a **single backend**. Five distinct hosts are hard-coded or provider-selected; the 52 shared
rows only share a *client*, which is a weaker statement than a shared server.

## 1. Per-endpoint rows

| # | Verb | Path | Interface.method | Client | Feature (classif.) | Req | Resp |
|---|---|---|---|---|---|---|---|
| 1 | POST | `/api/sendCustomerIoData` | `Lhg/b;.a` | mimo_auth | analytics_proxy | CustomerIoData | q |
| 2 | GET | `/api/v1/branding` | `Lio/customer/messaginginapp/inbox/data/InboxService;.fetchBranding` | third_party_sdk | third_party_sdk | — | i |
| 3 | POST | `/api/v1/logs/message/{messageId}` | `Lio/customer/messaginginapp/gist/data/listeners/GistQueueService;.logMessageView` | third_party_sdk | third_party_sdk | — | q |
| 4 | POST | `/api/v1/logs/queue/{queueId}` | `Lio/customer/messaginginapp/gist/data/listeners/GistQueueService;.logUserMessageView` | third_party_sdk | third_party_sdk | — | q |
| 5 | PATCH | `/api/v1/messages/{queueId}` | `Lio/customer/messaginginapp/gist/data/listeners/GistQueueService;.logInboxMessageOpened` | third_party_sdk | third_party_sdk | Map | q |
| 6 | GET | `/api/v1/templates` | `Lio/customer/messaginginapp/inbox/data/InboxService;.fetchTemplates` | third_party_sdk | third_party_sdk | — | i |
| 7 | POST | `/api/v4/users` | `Lio/customer/messaginginapp/gist/data/listeners/GistQueueService;.fetchMessagesForUser` | third_party_sdk | third_party_sdk | Object | QueueMessagesResponse |
| 8 | POST | `/click/{linkId}` | `Lph/b;.a` | email_click | email_tracking | — | q |
| 9 | POST | `/push/events` | `Lhg/d;.a` | customerio | analytics_proxy | PushNotificationDelivered | q |
| 10 | DELETE | `/v1/account` | `Lhg/a;.e` | shared_retrofit | account | — | q |
| 11 | PATCH | `/v1/account/email` | `Lhg/a;.d` | shared_retrofit | account | ChangeEmailRequestBody | q |
| 12 | GET | `/v1/aiTutor/conversations/messages/count` | `Ljg/a;.a` | shared_retrofit | ai_tutor | — | AiTutorialConversationMessag |
| 13 | GET | `/v1/code` | `Lmh/c;.c` | shared_retrofit | saved_code | — | SavedCode |
| 14 | POST | `/v1/code` | `Lmh/c;.d` | shared_retrofit | saved_code | SaveCodeRequestBody | SavedCode |
| 15 | POST | `/v1/code/runfiles` | `Lhg/c;.c` | shared_retrofit | code_execution | CodePlaygroundExecutionBody | CodePlaygroundExecutionRespo |
| 16 | DELETE | `/v1/code/{savedCodeId}` | `Lmh/c;.e` | shared_retrofit | saved_code | — | q |
| 17 | PATCH | `/v1/code/{savedCodeId}` | `Lmh/c;.a` | shared_retrofit | saved_code | SaveCodeRequestBody | SavedCode |
| 18 | POST | `/v1/code/{savedCodeId}/remixes` | `Lmh/c;.b` | shared_retrofit | saved_code | RemixCodeRequestBody | SavedCode |
| 19 | POST | `/v1/code/{savedCodeId}/runfiles` | `Lhg/c;.d` | shared_retrofit | code_execution | CodePlaygroundExecutionBody | CodePlaygroundExecutionRespo |
| 20 | POST | `/v1/invitations/{code}` | `Lug/a;.d` | shared_retrofit | invitations | — | q |
| 21 | GET | `/v1/leaderboards/friends` | `Lug/a;.c` | shared_retrofit | invitations | — | Friends |
| 22 | GET | `/v1/leaderboards/latest` | `Lch/a;.a` | shared_retrofit | leaderboard | — | Leaderboard |
| 23 | GET | `/v1/leaderboards/{leaderboardId}/userrank` | `Lch/a;.b` | shared_retrofit | leaderboard | — | LeaderboardUserResult |
| 24 | GET | `/v1/package/preview` | `Leh/a;.a` | preview_long_timeout | content_preview | — | ResponseBody |
| 25 | GET | `/v1/practice/statistics` | `Lhh/a;.a` | shared_retrofit | practice | — | PracticeStatsResponse |
| 26 | POST | `/v1/preview/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/runFiles` | `Lhg/c;.a` | shared_retrofit | code_execution | ExecuteFilesBody | ExecuteFilesResponse |
| 27 | GET | `/v1/products/user` | `Lnh/c;.b` | shared_retrofit | iap | — | RawProducts |
| 28 | POST | `/v1/products/user` | `Lnh/c;.a` | shared_retrofit | iap | ProductTypeBody | RawPurchasedProduct |
| 29 | GET | `/v1/tracks/completion/lastInteracted` | `Lcom/getmimo/data/source/remote/progress/CompletionApi;.getLastInteractedTrack` | shared_retrofit | completion | — | LastInteractedTrackResponse |
| 30 | GET | `/v1/tracks/{trackId}/certificates` | `Log/a;.b` | shared_retrofit | certificates | — | ResponseBody |
| 31 | GET | `/v1/tracks/{trackId}/completion` | `Lcom/getmimo/data/source/remote/progress/CompletionApi;.getTrackCompletion` | shared_retrofit | completion | — | TrackCompletionResponse |
| 32 | GET | `/v1/tracks/{trackId}/eta` | `Lcom/getmimo/data/source/remote/progress/TrackEtaApi;.getTrackEta` | shared_retrofit | content | — | TrackEtaResponse |
| 33 | POST | `/v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/runFiles` | `Lhg/c;.b` | shared_retrofit | code_execution | ExecuteFilesBody | ExecuteFilesResponse |
| 34 | POST | `/v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/savefiles` | `Ldh/a;.b` | shared_retrofit | lesson_save | SaveLessonFilesBody | q |
| 35 | GET | `/v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/savedFiles` | `Ldh/a;.a` | shared_retrofit | lesson_save | — | SavedLessonFilesBody |
| 36 | GET | `/v1/tutorials/drafts/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/render` | `Lng/a;.a` | shared_retrofit | content | — | LessonDraftResponse |
| 37 | POST | `/v1/tutorials/{tutorialId}/lessons/{lessonIdentityId}/report` | `Lkh/a;.a` | shared_retrofit | lesson_report | ReportLessonBody | q |
| 38 | POST | `/v1/tutorials/{tutorialId}/progress` | `Lcom/getmimo/data/source/remote/progress/LessonProgressApi;.postProgress` | shared_retrofit | progress | PostProgressRequestBody | PostProgressResponse |
| 39 | GET | `/v1/user/activity` | `Lsh/h;.a` | shared_retrofit | profile | — | UserActivityResponse |
| 40 | GET | `/v1/user/coins` | `Lqg/a;.a` | shared_retrofit | gamification | — | Coins |
| 41 | POST | `/v1/user/deviceTokens` | `Lhg/a;.c` | shared_retrofit | account | DeviceToken | q |
| 42 | GET | `/v1/user/events/subscribe` | `Lhg/a;.b` | shared_retrofit | account | — | PusherChannelResponse |
| 43 | GET | `/v1/user/favorites/tracks` | `Lxe/a;.a` | shared_retrofit | favorites | — | FavoriteTracks |
| 44 | DELETE | `/v1/user/favorites/tracks/{trackId}` | `Lxe/a;.c` | shared_retrofit | favorites | — | FavoriteTracks |
| 45 | POST | `/v1/user/favorites/tracks/{trackId}` | `Lxe/a;.b` | shared_retrofit | favorites | — | FavoriteTracks |
| 46 | DELETE | `/v1/user/following/{userId}` | `Lih/a;.a` | shared_retrofit | social | — | q |
| 47 | PUT | `/v1/user/following/{userId}` | `Lih/a;.f` | shared_retrofit | social | — | q |
| 48 | GET | `/v1/user/invitations` | `Lug/a;.a` | shared_retrofit | invitations | — | InvitationsOverview |
| 49 | GET | `/v1/user/keys` | `Lbh/a;.b` | shared_retrofit | keys | — | UserKeys |
| 50 | POST | `/v1/user/keys/consume` | `Lbh/a;.a` | shared_retrofit | keys | — | UserKeys |
| 51 | GET | `/v1/user/rewards/next` | `Llh/a;.b` | shared_retrofit | rewards | — | Rewards |
| 52 | POST | `/v1/user/rewards/{rewardId}/confirm` | `Llh/a;.a` | shared_retrofit | rewards | — | q |
| 53 | GET | `/v1/user/settings` | `Lkf/a;.c` | shared_retrofit | settings | — | Settings |
| 54 | PATCH | `/v1/user/settings` | `Lkf/a;.a` | shared_retrofit | settings | Settings | Settings |
| 55 | POST | `/v1/user/settings/avatar` | `Lkf/a;.e` | shared_retrofit | settings | — | AvatarUpdateResponse |
| 56 | PUT | `/v1/user/settings/avatar/{uploadId}` | `Lkf/a;.d` | shared_retrofit | settings | ConfirmAvatarUploadBody | q |
| 57 | POST | `/v1/user/visits` | `Lhg/a;.a` | shared_retrofit | account | AppName | q |
| 58 | GET | `/v1/users/{userId}/code` | `Lih/a;.b` | shared_retrofit | social | — | PublicUserCode |
| 59 | GET | `/v1/users/{userId}/code/{savedCodeId}` | `Lih/a;.c` | shared_retrofit | social | — | SavedCode |
| 60 | GET | `/v1/users/{userId}/profile` | `Lih/a;.d` | shared_retrofit | social | — | PublicUser |
| 61 | POST | `/v1/users/{userId}/report` | `Lih/a;.e` | shared_retrofit | social | — | q |
| 62 | GET | `/v2/client-config` | `Llg/a;.a` | shared_retrofit | remote_config | — | d |

## 2. Distribution

```text
{
 "mimo_auth": 1,
 "third_party_sdk": 6,
 "email_click": 1,
 "customerio": 1,
 "shared_retrofit": 52,
 "preview_long_timeout": 1
}
{
 "account": 5,
 "ai_tutor": 1,
 "analytics_proxy": 2,
 "certificates": 1,
 "code_execution": 4,
 "completion": 2,
 "content": 2,
 "content_preview": 1,
 "email_tracking": 1,
 "favorites": 3,
 "gamification": 1,
 "iap": 2,
 "invitations": 3,
 "keys": 2,
 "leaderboard": 2,
 "lesson_report": 1,
 "lesson_save": 2,
 "practice": 1,
 "profile": 1,
 "progress": 1,
 "remote_config": 1,
 "rewards": 2,
 "saved_code": 5,
 "settings": 4,
 "social": 6,
 "third_party_sdk": 6
}
```

## 3. Authentication per endpoint — what is and is not proven

The mechanism is proven: `fh.a` reads the **Retrofit `Method` object from the OkHttp request tag**, looks up one
annotation on it, and only then appends `Authorization: Bearer <ku.a.d(false)>`. Therefore *some* endpoints carry a
token and *some* do not — a per-method property, not a per-client one.

What is **not** available in committed evidence is the per-row annotation flag. Mission-06's register recorded the
aggregate (`53` authenticated / `9` unauthenticated, `VERIFIED_STATIC` at the time of that scan) but the column is
absent from `API_CATALOG_V2.csv` as committed. Re-deriving it requires a DEX read, which this environment cannot do
(no APK, no mirrors reachable) → **`BLOCKED_BY_ENVIRONMENT`**, question **A-01**.

Practical consequence for anyone consuming this catalogue: treat every row's auth requirement as `unknown` and
consult the server contract; the client-side mechanism is annotation-driven, so the *absence* of a token on a call is
not evidence that the endpoint is public.
