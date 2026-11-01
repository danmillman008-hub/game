# Mission 5 — DTO Catalogue

## Scope
Every data-transfer type the API layer references, with its field list as recovered from the
decompiled class, and whether it crosses the wire as a request or a response.

## Method
`tools/build_dto_catalog.py` extracts the response type (from the Kotlin continuation generic) and the
request body type of every endpoint in `evidence/API_CATALOG_V2.csv`, then reads the corresponding
decompiled class and records every `private final <type> <name>;` declaration. Kotlin data classes keep
field names in the DEX string pool, so **field names here are author-chosen, not obfuscated**
(a property that makes this catalogue unusually trustworthy).

## Sources
`evidence/API_CATALOG_V2.csv` (endpoints) → `evidence/DTO_CATALOG.csv` (this table) → decompiled classes
in `/tmp/dad`.

## Findings
- **50 DTO types referenced**; **39 carry a recoverable field list**;
  **10 have no source in the decompiled app tree** (library types:
  OkHttp `ResponseBody`, Gist messaging models, internal wrappers `llg/d`, `ge0/o0`, `jx/i`, `z60/q`).
- The largest author-defined DTOs are `PublicUser` (14 fields), `LeaderboardUserResult` (12) and
  `Settings` (9) — i.e. profile/leaderboard/settings dominate the payload surface.
- `Progress` (9 boxed fields) is the *only* progress DTO and is posted as a list; boxed types are used
  throughout, so absent fields are representable (partial progress rows are legal on the wire).

## Table
| DTO | Fields | As response | As request | Field list |
|---|---|---|---|---|
| `com/getmimo/data/model/publicprofile/PublicUser` | 14 | 1 | 0 | activeStreakLength:int, avatarUrl:String, biography:String, isFollowedByMe:boolean, isPremium:boolean, leaderboardFirstPlaceCount:int, leaderboardInfo:com.getmimo.data.model.publicprofile.ProfileLeaderboardInfo, leaderboardSecondPlaceCount:int, leaderboardThirdPlaceCount:int, longestStreakLength:int, name:String, progress:java.util.List, sparks:long, subscriptionType:com.getmimo.core.model.inapp.Subscription$Type |
| `com/getmimo/data/model/leaderboard/LeaderboardUserResult` | 12 | 1 | 0 | avatar:String, endDate:String, isInProgress:boolean, leaderboardId:long, league:int, newLeague:int, rank:int, sparks:long, startDate:String, usedLeagueFreeze:boolean, username:String, usersCount:int |
| `com/getmimo/data/settings/model/Settings` | 9 | 2 | 1 | biography:String, dailyReminderTime:String, dailySparksGoal:Integer, hadFreeMaxTrial:Boolean, hadFreeProTrial:Boolean, hasProgrammingExperience:Boolean, name:String, notificationSettings:java.util.List, userId:Long |
| `com/getmimo/data/model/savedcode/SavedCode` | 7 | 4 | 0 | files:java.util.List, hackathonId:Integer, hostedFilesUrl:String, id:long, isPrivate:boolean, modifiedAt:String, name:String |
| `com/getmimo/data/model/friends/InvitationsOverview` | 6 | 1 | 0 | acceptedInvitationsCount:int, invitationSubscriptionRewardDays:int, invitationUrl:String, maximumInvitationRewardCount:int, unconfirmedInvitations:java.util.List, unconfirmedOwnInvitation:com.getmimo.data.model.friends.UnconfirmedInvitation |
| `com/getmimo/core/model/lesson/executablefiles/ExecuteFilesResponse` | 5 | 2 | 0 | consoleOutput:String, error:String, hasPassed:boolean, hostedProjectUrl:String, tests:java.util.List |
| `com/getmimo/data/model/savedcode/SaveCodeRequestBody` | 5 | 0 | 2 | files:java.util.List, isPrivate:Boolean, name:String, sourceTutorialId:Long, sourceTutorialVersion:Integer |
| `com/getmimo/core/model/lesson/report/ReportLessonBody` | 4 | 0 | 1 | interactionType:String, reportOption:String, reportText:String, tutorialVersion:int |
| `com/getmimo/data/model/analytics/PushNotificationDelivered` | 4 | 0 | 1 | delivery_id:String, device_id:String, event:String, timestamp:long |
| `com/getmimo/data/model/customerio/CustomerIoData` | 4 | 0 | 1 | country:String, firstName:String, lastName:String, timezone:String |
| `com/getmimo/data/model/store/RawPurchasedProduct` | 4 | 1 | 0 | boughtAt:org.joda.time.Instant, coinPrice:int, id:int, productType:String |
| `com/getmimo/core/model/streak/UserActivityResponse` | 3 | 1 | 0 | activeStreak:com.getmimo.core.model.streak.Streak, activity:java.util.List, longestStreak:com.getmimo.core.model.streak.Streak |
| `com/getmimo/data/model/codeexecution/CodePlaygroundExecutionResponse` | 3 | 2 | 0 | consoleOutput:String, consoleOutputIsError:boolean, hostedFilesUrl:String |
| `com/getmimo/data/model/progress/TrackEtaResponse` | 3 | 1 | 0 | currentPaceMinutesPerDay:Integer, sections:java.util.List, trackEstimatedCompletionAt:String |
| `com/getmimo/data/model/friends/Friends` | 2 | 1 | 0 | currentUserIndex:int, users:java.util.List |
| `com/getmimo/data/model/practice/PracticeStatsResponse` | 2 | 1 | 0 | chaptersCompleted:int, duration:long |
| `com/getmimo/data/model/progress/PostProgressResponse` | 2 | 1 | 0 | dailyGoalCoinReward:int, reachedGoal:boolean |
| `com/getmimo/data/model/progress/TrackCompletionResponse` | 2 | 1 | 0 | lastInteractedTutorialId:long, tutorials:java.util.List |
| `com/getmimo/data/model/savedcode/RemixCodeRequestBody` | 2 | 0 | 1 | isPrivate:Boolean, name:String |
| `com/getmimo/data/model/store/RawProducts` | 2 | 1 | 0 | productsAvailableForPurchase:java.util.List, purchasedProducts:java.util.List |
| `com/getmimo/data/settings/model/AvatarUpdateResponse` | 2 | 1 | 0 | uploadId:String, uploadUrl:String |
| `com/getmimo/data/source/remote/awesome/LessonDraftResponse` | 2 | 1 | 0 | content:String, executableFilesContent:com.getmimo.data.content.model.track.LessonContent$Executable |
| `com/getmimo/core/model/coins/Coins` | 1 | 1 | 0 | coins:int |
| `com/getmimo/core/model/lesson/executablefiles/ExecuteFilesBody` | 1 | 0 | 2 | files:java.util.List |
| `com/getmimo/data/content/model/track/FavoriteTracks` | 1 | 3 | 0 | favoriteTrackIds:java.util.List |
| `com/getmimo/data/model/AppName` | 1 | 0 | 1 | appName:String |
| `com/getmimo/data/model/account/ChangeEmailRequestBody` | 1 | 0 | 1 | email:String |
| `com/getmimo/data/model/aitutor/AiTutorialConversationMessageCount` | 1 | 1 | 0 | userMessageCount:int |
| `com/getmimo/data/model/codeexecution/CodePlaygroundExecutionBody` | 1 | 0 | 2 | files:java.util.List |
| `com/getmimo/data/model/keys/UserKeys` | 1 | 2 | 0 | currentKeys:int |
| `com/getmimo/data/model/lesson/SaveLessonFilesBody` | 1 | 0 | 1 | files:java.util.List |
| `com/getmimo/data/model/lesson/SavedLessonFilesBody` | 1 | 1 | 0 | savedFiles:java.util.List |
| `com/getmimo/data/model/progress/LastInteractedTrackResponse` | 1 | 1 | 0 | lastInteractedTrackId:Long |
| `com/getmimo/data/model/progress/PostProgressRequestBody` | 1 | 0 | 1 | progressList:java.util.List |
| `com/getmimo/data/model/publicprofile/PublicUserCode` | 1 | 1 | 0 | code:java.util.List |
| `com/getmimo/data/model/pusher/PusherChannelResponse` | 1 | 1 | 0 | channelName:String |
| `com/getmimo/data/model/reward/Rewards` | 1 | 1 | 0 | rewards:java.util.List |
| `com/getmimo/data/model/store/ProductTypeBody` | 1 | 0 | 1 | productType:com.getmimo.data.model.store.ProductType |
| `com/getmimo/data/settings/model/ConfirmAvatarUploadBody` | 1 | 0 | 1 | contentType:String |
| `com/getmimo/data/model/analytics/DeviceToken` | 0 | 0 | 1 | — |
| `ge0/o0<Lcom/getmimo/data/model/leaderboard/Leaderboard` | 0 | 1 | 0 | — |
| `ge0/o0<Lio/customer/messaginginapp/gist/data/model/response/QueueMessagesResponse` | 0 | 1 | 0 | — |
| `ge0/o0<Ljx/i` | 0 | 2 | 0 | — |
| `ge0/o0<Lokhttp3/ResponseBody` | 0 | 2 | 0 | — |
| `ge0/o0<Lz60/q` | 0 | 5 | 0 | — |
| `java/lang/Object` | 0 | 0 | 1 | — |
| `java/util/List<Lcom/getmimo/data/model/savedcode/SavedCode` | 0 | 1 | 0 | — |
| `java/util/Map` | 0 | 0 | 1 | — |
| `lg/d` | 0 | 1 | 0 | — |
| `z60/q` | 0 | 14 | 0 | — |

## Evidence labels
Field names and counts: **VERIFIED_STATIC**. Which endpoint uses which DTO: **VERIFIED_STATIC**
(method signature join). JSON key naming (serialised names) : **INFERRED_HIGH** — the app uses
`@SerializedName`-style annotations in some DTOs; this mission did not extract per-field serialised
names, so a reimplementation must not assume camelCase ↔ snake_case mapping.

## Limitations
Nested/`List<T>` element types are recorded as declared (e.g. `java.util.List<SavedCode;`), not expanded.

## Unresolved
`U-25` serialised field names per DTO (requires field-annotation extraction, which the corrected tool
supports but was not run for fields).

## Reproduction
```bash
/tmp/venv/bin/python tools/build_api_catalog_v2.py --annotations evidence/ANNOTATIONS_V2.csv \
  --csv evidence/API_CATALOG_V2.csv --json evidence/API_CATALOG_V2.json
/tmp/venv/bin/python tools/build_dto_catalog.py     # reads the catalogue, writes evidence/DTO_CATALOG.csv
```
