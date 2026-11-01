# Mission 5 — API Catalogue (62 endpoints)

## Scope
Every HTTP call the app is capable of making, with method, path, request body type, response type,
parameter bindings and static headers. Machine-readable source: `evidence/API_CATALOG_V2.csv`.

## Method
1. Corrected the DEX annotation pass (`tools/extract_annotations_v2.py`) — mission-04's parameter
   annotations were garbage (162 bogus rows), the corrected pass yields 105 valid rows.
2. Joined annotations → method descriptors → method `Signature` annotations (generics) → parameter
   bindings (`tools/build_api_catalog_v2.py`).
3. Resolved the response type from the Kotlin continuation generic `Ld70/b<-T;>` — DEX erases it
   from the descriptor, so this was previously UNKNOWN.
4. Constrained HTTP verbs by Retrofit's own rules (GET/DELETE forbid a body) and verified the
   result has **zero** rule violations across all 62 endpoints.

## Sources
| Evidence | File |
|---|---|
| Corrected annotations | `evidence/ANNOTATIONS_V2.csv` (29,686 rows: 23,328 class / 1,666 field / 4,587 method / 105 parameter) |
| Endpoint table | `evidence/API_CATALOG_V2.csv` |
| DTO fields | `evidence/DTO_CATALOG.csv` |

## Findings
- **62 endpoints across 29 interfaces.** Verbs: DELETE 4, GET 28, PATCH 4, POST 24, PUT 2.
- **Parameter bindings recovered: 85** — PATH 45, BODY 20, QUERY 17, HEADER 3.
- **Response types: 34 distinct**; 20 endpoints carry a request body.
- **No hard-coded API host** exists in the decompiled `com.getmimo` classes: only `images.getmimo.com`
  (CDN), `mimo.org`/`support.mimo.org` (web), `api.mixpanel.com`, and a sentinel
  `https://lesson.mimo.invalid/`. The base URL is therefore injected/configured → **UNKNOWN** (U-22).
- Two endpoint families dominate: content/progress (`/v1/tracks/...`, `/v1/tutorials/...`,
  `/v1/package/preview`) and account/identity (`/v1/user/...`, `/v1/account/...`, `/v1/users/...`).
- `/v1/package/preview` returns `application/zip` (`okhttp3.ResponseBody`) — content packs are
  downloaded as archives, confirming the asset-pipeline model.

### Verb evidence (per annotation class)
| Annotation | Verb | n | Body-bearing | Basis |
|---|---|---|---|---|
| `Lie0/f;` | GET | 28 | 0 | no body param anywhere; same paths also carry body-bearing annotations (e.g. `/v1/user/settings`) |
| `Lie0/o;` | POST | 24 | 15 | creates/toggles/logs; pairs with DELETE on the same path |
| `Lie0/n;` | PATCH | 4 | 4 | partial updates (`/v1/user/settings`, `/v1/account/email`); PUT/PATCH pair ambiguous |
| `Lie0/b;` | DELETE | 4 | 0 | removal-shaped, each paired with an add counterpart (`o`, `p`, `n`) |
| `Lie0/p;` | PUT | 2 | 1 | idempotent set-operations (`/v1/user/following/{userId}`) |

GET/DELETE/POST are **INFERRED_HIGH**; PATCH↔PUT are **INFERRED_MEDIUM** (the pair could be swapped
without violating Retrofit's constraints). No runtime capture was possible to close this.

## Endpoint table
| # | Verb | Path | Request body | Response | Params | Interface |
|---|---|---|---|---|---|---|
| 1 | POST | `/api/sendCustomerIoData` | data/model/customerio/CustomerIoData; | z60/q; | 0:BODY: | Lhg/b; |
| 2 | GET | `/api/v1/branding` | — | ge0/o0<Ljx/i; | — | Lio/customer/messaginginapp/inbox/data/InboxService; |
| 3 | POST | `/api/v1/logs/message/{messageId}` | — | z60/q; | 0:PATH:messageId<br>1:QUERY:sessionId | Lio/customer/messaginginapp/gist/data/listeners/GistQueueService; |
| 4 | POST | `/api/v1/logs/queue/{queueId}` | — | z60/q; | 0:PATH:queueId<br>1:QUERY:sessionId | Lio/customer/messaginginapp/gist/data/listeners/GistQueueService; |
| 5 | PATCH | `/api/v1/messages/{queueId}` | java/util/Map; | z60/q; | 0:PATH:queueId<br>1:QUERY:sessionId<br>2:BODY: | Lio/customer/messaginginapp/gist/data/listeners/GistQueueService; |
| 6 | GET | `/api/v1/templates` | — | ge0/o0<Ljx/i; | — | Lio/customer/messaginginapp/inbox/data/InboxService; |
| 7 | POST | `/api/v4/users` | java/lang/Object; | ge0/o0<Lio/customer/messaginginapp/gist/data/model/response/QueueMessagesResponse; | 0:BODY:<br>1:QUERY:sessionId | Lio/customer/messaginginapp/gist/data/listeners/GistQueueService; |
| 8 | POST | `/click/{linkId}` | — | z60/q; | 0:PATH:linkId | Lph/b; |
| 9 | POST | `/push/events` | data/model/analytics/PushNotificationDelivered; | z60/q; | 0:BODY: | Lhg/d; |
| 10 | DELETE | `/v1/account` | — | ge0/o0<Lz60/q; | 0:HEADER:Authorization | Lhg/a; |
| 11 | PATCH | `/v1/account/email` | data/model/account/ChangeEmailRequestBody; | ge0/o0<Lz60/q; | 0:BODY: | Lhg/a; |
| 12 | GET | `/v1/aiTutor/conversations/messages/count` | — | data/model/aitutor/AiTutorialConversationMessageCount; | — | Ljg/a; |
| 13 | GET | `/v1/code` | — | java/util/List<data/model/savedcode/SavedCode; | — | Lmh/c; |
| 14 | POST | `/v1/code` | data/model/savedcode/SaveCodeRequestBody; | data/model/savedcode/SavedCode; | 0:BODY: | Lmh/c; |
| 15 | POST | `/v1/code/runfiles` | data/model/codeexecution/CodePlaygroundExecutionBody; | data/model/codeexecution/CodePlaygroundExecutionResponse; | 0:BODY: | Lhg/c; |
| 16 | DELETE | `/v1/code/{savedCodeId}` | — | z60/q; | 0:PATH:savedCodeId | Lmh/c; |
| 17 | PATCH | `/v1/code/{savedCodeId}` | data/model/savedcode/SaveCodeRequestBody; | data/model/savedcode/SavedCode; | 0:PATH:savedCodeId<br>1:BODY: | Lmh/c; |
| 18 | POST | `/v1/code/{savedCodeId}/remixes` | data/model/savedcode/RemixCodeRequestBody; | data/model/savedcode/SavedCode; | 0:PATH:savedCodeId<br>1:BODY: | Lmh/c; |
| 19 | POST | `/v1/code/{savedCodeId}/runfiles` | data/model/codeexecution/CodePlaygroundExecutionBody; | data/model/codeexecution/CodePlaygroundExecutionResponse; | 0:PATH:savedCodeId<br>1:BODY: | Lhg/c; |
| 20 | POST | `/v1/invitations/{code}` | — | z60/q; | 0:PATH:code | Lug/a; |
| 21 | GET | `/v1/leaderboards/friends` | — | data/model/friends/Friends; | — | Lug/a; |
| 22 | GET | `/v1/leaderboards/latest` | — | ge0/o0<data/model/leaderboard/Leaderboard; | — | Lch/a; |
| 23 | GET | `/v1/leaderboards/{leaderboardId}/userrank` | — | data/model/leaderboard/eaderboardUserResult; | 0:PATH:leaderboardId | Lch/a; |
| 24 | GET | `/v1/package/preview` | — | ge0/o0<Lokhttp3/ResponseBody; | — | Leh/a; |
| 25 | GET | `/v1/practice/statistics` | — | data/model/practice/PracticeStatsResponse; | — | Lhh/a; |
| 26 | POST | `/v1/preview/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/runFiles` | core/model/lesson/executablefiles/ExecuteFilesBody; | core/model/lesson/executablefiles/ExecuteFilesResponse; | 0:PATH:trackId<br>1:PATH:tutorialId<br>2:PATH:chapterId<br>3:PATH:lessonId<br>4:QUERY:publishSetVersion<br>5:BODY: | Lhg/c; |
| 27 | GET | `/v1/products/user` | — | data/model/store/RawProducts; | — | Lnh/c; |
| 28 | POST | `/v1/products/user` | data/model/store/ProductTypeBody; | data/model/store/RawPurchasedProduct; | 0:HEADER:Time-Zone<br>1:BODY:<br>2:QUERY:useCoins | Lnh/c; |
| 29 | GET | `/v1/tracks/completion/lastInteracted` | — | data/model/progress/astInteractedTrackResponse; | — | Lcom/getmimo/data/source/remote/progress/CompletionApi; |
| 30 | GET | `/v1/tracks/{trackId}/certificates` | — | ge0/o0<Lokhttp3/ResponseBody; | 0:PATH:trackId<br>1:QUERY:fullName<br>2:QUERY:trackVersion | Log/a; |
| 31 | GET | `/v1/tracks/{trackId}/completion` | — | data/model/progress/TrackCompletionResponse; | 0:PATH:trackId<br>1:QUERY:trackVersion | Lcom/getmimo/data/source/remote/progress/CompletionApi; |
| 32 | GET | `/v1/tracks/{trackId}/eta` | — | data/model/progress/TrackEtaResponse; | 0:PATH:trackId<br>1:QUERY:trackVersion | Lcom/getmimo/data/source/remote/progress/TrackEtaApi; |
| 33 | POST | `/v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/runFiles` | core/model/lesson/executablefiles/ExecuteFilesBody; | core/model/lesson/executablefiles/ExecuteFilesResponse; | 0:PATH:trackId<br>1:PATH:tutorialId<br>2:PATH:chapterId<br>3:PATH:lessonId<br>4:QUERY:publishSetVersion<br>5:QUERY:suppressConsoleOutput<br>6:QUERY:language<br>7:BODY: | Lhg/c; |
| 34 | POST | `/v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/savefiles` | data/model/lesson/SaveessonFilesBody; | z60/q; | 0:PATH:trackId<br>1:PATH:tutorialId<br>2:PATH:chapterId<br>3:PATH:lessonId<br>4:QUERY:publishSetVersion<br>5:BODY: | Ldh/a; |
| 35 | GET | `/v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/savedFiles` | — | data/model/lesson/SavedessonFilesBody; | 0:PATH:trackId<br>1:PATH:tutorialId<br>2:PATH:chapterId<br>3:QUERY:trackVersion | Ldh/a; |
| 36 | GET | `/v1/tutorials/drafts/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/render` | — | data/source/remote/awesome/essonDraftResponse; | 0:PATH:tutorialId<br>1:PATH:chapterId<br>2:PATH:lessonId | Lng/a; |
| 37 | POST | `/v1/tutorials/{tutorialId}/lessons/{lessonIdentityId}/report` | core/model/lesson/report/ReportessonBody; | z60/q; | 0:PATH:tutorialId<br>1:PATH:lessonIdentityId<br>2:BODY: | Lkh/a; |
| 38 | POST | `/v1/tutorials/{tutorialId}/progress` | data/model/progress/PostProgressRequestBody; | data/model/progress/PostProgressResponse; | 0:PATH:tutorialId<br>1:BODY: | Lcom/getmimo/data/source/remote/progress/LessonProgressApi; |
| 39 | GET | `/v1/user/activity` | — | core/model/streak/UserActivityResponse; | 0:QUERY:from<br>1:QUERY:to | Lsh/h; |
| 40 | GET | `/v1/user/coins` | — | core/model/coins/Coins; | — | Lqg/a; |
| 41 | POST | `/v1/user/deviceTokens` | data/model/analytics/DeviceToken; | z60/q; | 0:BODY: | Lhg/a; |
| 42 | GET | `/v1/user/events/subscribe` | — | data/model/pusher/PusherChannelResponse; | — | Lhg/a; |
| 43 | GET | `/v1/user/favorites/tracks` | — | data/content/model/track/FavoriteTracks; | — | Lxe/a; |
| 44 | DELETE | `/v1/user/favorites/tracks/{trackId}` | — | data/content/model/track/FavoriteTracks; | 0:PATH:trackId | Lxe/a; |
| 45 | POST | `/v1/user/favorites/tracks/{trackId}` | — | data/content/model/track/FavoriteTracks; | 0:PATH:trackId | Lxe/a; |
| 46 | DELETE | `/v1/user/following/{userId}` | — | ge0/o0<Lz60/q; | 0:PATH:userId | Lih/a; |
| 47 | PUT | `/v1/user/following/{userId}` | — | ge0/o0<Lz60/q; | 0:PATH:userId | Lih/a; |
| 48 | GET | `/v1/user/invitations` | — | data/model/friends/InvitationsOverview; | — | Lug/a; |
| 49 | GET | `/v1/user/keys` | — | data/model/keys/UserKeys; | 0:HEADER:Time-Zone | Lbh/a; |
| 50 | POST | `/v1/user/keys/consume` | — | data/model/keys/UserKeys; | — | Lbh/a; |
| 51 | GET | `/v1/user/rewards/next` | — | data/model/reward/Rewards; | — | Llh/a; |
| 52 | POST | `/v1/user/rewards/{rewardId}/confirm` | — | z60/q; | 0:PATH:rewardId | Llh/a; |
| 53 | GET | `/v1/user/settings` | — | data/settings/model/Settings; | — | Lkf/a; |
| 54 | PATCH | `/v1/user/settings` | data/settings/model/Settings; | data/settings/model/Settings; | 0:BODY: | Lkf/a; |
| 55 | POST | `/v1/user/settings/avatar` | — | data/settings/model/AvatarUpdateResponse; | — | Lkf/a; |
| 56 | PUT | `/v1/user/settings/avatar/{uploadId}` | data/settings/model/ConfirmAvatarUploadBody; | z60/q; | 0:PATH:uploadId<br>1:BODY: | Lkf/a; |
| 57 | POST | `/v1/user/visits` | data/model/AppName; | z60/q; | 0:BODY: | Lhg/a; |
| 58 | GET | `/v1/users/{userId}/code` | — | data/model/publicprofile/PublicUserCode; | 0:PATH:userId | Lih/a; |
| 59 | GET | `/v1/users/{userId}/code/{savedCodeId}` | — | data/model/savedcode/SavedCode; | 0:PATH:userId<br>1:PATH:savedCodeId | Lih/a; |
| 60 | GET | `/v1/users/{userId}/profile` | — | data/model/publicprofile/PublicUser; | 0:PATH:userId | Lih/a; |
| 61 | POST | `/v1/users/{userId}/report` | — | ge0/o0<Lz60/q; | 0:PATH:userId | Lih/a; |
| 62 | GET | `/v2/client-config` | — | lg/d; | — | Llg/a; |

## Evidence labels
Endpoint existence, path, parameter count/bindings, body type, response type: **VERIFIED_STATIC**.
Verb assignment: **INFERRED_HIGH** (GET/DELETE/POST) / **INFERRED_MEDIUM** (PATCH/PUT).
Backend semantics of any endpoint: **UNKNOWN** — no request was ever made (RULE 5).

## Limitations
- A path in the catalogue is *route evidence*, not proof the server serves it in production.
- 10 of the 50 referenced DTO types are library types (OkHttp, gist, internal wrappers) with no
  source in the decompiled app tree.
- Two endpoints return `Lz60/q;` (`Unit`) but still declare `Content-Type: application/json`; the
  header annotation is applied uniformly by the interface, not per-response.

## Unresolved
`U-22` base URL resolution; `U-23` PATCH vs PUT disambiguation; `U-24` server-side error/retry
contract (only `PostProgressResponse` was recoverable as a wrapper shape).

## Reproduction
```bash
/tmp/venv/bin/python tools/extract_annotations_v2.py --dex-dir /tmp/x \
  --csv evidence/ANNOTATIONS_V2.csv.gz.gz --json evidence/ANNOTATIONS_V2.json
/tmp/venv/bin/python tools/build_api_catalog_v2.py --annotations evidence/ANNOTATIONS_V2.csv \
  --csv evidence/API_CATALOG_V2.csv --json evidence/API_CATALOG_V2.json
```
