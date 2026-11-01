# Phase 5 — Feature network paths

Format: `UI/ViewModel → repository/use case → interface → client → interceptor → endpoint → response → persistence/UI`.
A path is only drawn where each hop has evidence; otherwise the hop is marked `—` with the reason.

## 5.1 Lesson content delivery — **local only, no HTTP**

```text
Lesson screen → LessonViewModel → ContentRepository → tracks.json (assets) / publishSetVersion 753
```

Content arrives in the APK (`tracks.json`, 10,317 JSON documents, 19 tracks; Stage 2). The network is used for
**versions and ETA**, not for lesson bodies. This is the most important negative result of the stage: a "content
download" path does not exist in the recovered code.

Two related endpoints do exist and are content-adjacent:

* `GET /v1/tracks/{trackId}/eta` (`TrackEtaApi.getTrackEta`) — pacing estimate;
* `GET /v1/package/preview` and the `eh.a` service on client **C3** (10 s / 120 s) — a larger download on a
  long-timeout client, consistent with a package/asset fetch. The response type is `okhttp3.ResponseBody`, so the
  client must stream it; **the consumer was not recovered** (A-03).

## 5.2 Progress synchronisation (closes the Stage-5 question)

```text
lesson graded → base.c.V/W/X/U → createLessonProgress → LessonProgressQueue.storeLessonProgress
   → lesson_progress row (in_queue = 1)
chapter end / app start → storeAndPostAllLessonProgress / MainViewModel
   → moveLessonProgressFromQueue (in_queue = 0)
   → postUnsyncedLessonProgress
        POST /v1/tutorials/{tutorialId}/progress      [LessonProgressApi.postProgress, client C2]
        body PostProgressRequestBody{progressList: [Progress × n]}
        → PostProgressResponse{reachedGoal, dailyGoalCoinReward}
        → cg.e(reachedGoal, dailyGoalCoinReward)
        → DELETE FROM lesson_progress WHERE lesson_id IN (…)
```

Position in the overall architecture, stated precisely:

* the POST is an **outbox flush**, not a live write — it happens at chapter end and app start only;
* it is **per tutorial** (client-side grouping by `tutorialId`), so one session can produce several POSTs;
* the **acknowledgement is the deletion**, not a server id;
* `reachedGoal`/`dailyGoalCoinReward` are the only progression signals the server returns on this path;
* it carries **no idempotency key**, so a duplicated flush is only deduplicated server-side.

The interceptor adds a token only if `postProgress` is annotated; the call would otherwise be anonymous (A-01).

## 5.3 Completion synchronisation

```text
GetChapterEndSuccessState / MainViewModel → CompletionRepository.fetchTrackCompletion(trackId, trackVersion)
   → GET /v1/tracks/{trackId}/completion             [CompletionApi, C2]
   → TutorialCompletion / ChapterCompletion rows     (Stage 5)
   → SharedPreferences last_interacted_tutorial_id_<trackId>
   → attachTutorialAndChapterCompletionToTrack → immutable Track copies → path map / practice topics
GET /v1/tracks/completion/lastInteracted            [CompletionApi.getLastInteractedTrack] → t.M()
```

Ordering (from Stage 5) still holds: **progress POST precedes completion fetch**, so the completion values reflect the
progress just posted.

## 5.4 AI tutor (SSE)

```text
AiTutorViewModel → com.getmimo.data.source.local.aitutor.a (C7)
   → POST /v1/aiTutor/conversations (or /{conversationId})   Accept: text/event-stream
   → manual Authorization: Bearer <ku.a.d(false)>
   → okhttp3.sse RealEventSource → frames appended to the last assistant message
GET /v1/aiTutor/conversations/messages/count        [Ljg/a;, C2] → quota counter
```

Note the asymmetry: the *count* endpoint goes through Retrofit (and therefore through `fh.a` if annotated), while the
*streaming* endpoint bypasses the interceptor entirely.

## 5.5 Code execution

```text
ExecutableLessonViewModel → code execution repository
   ├─ POST /v1/code/runfiles                 [Lhg/c;.c, C2]
   ├─ POST /v1/code/{savedCodeId}/runfiles   [Lhg/c;.d, C2]
   └─ wss://api.mimo.org/v1/run/socket       [pg.a, C8] — streaming run output
```

Both channels exist; which one a given lesson uses was not recovered (A-04).

## 5.6 Account, settings, identity

| Feature | Endpoints | Client |
|---|---|---|
| account deletion / e-mail change / device tokens / visits / event subscription | `DELETE /v1/account`, `PATCH /v1/account/email`, `POST /v1/user/deviceTokens`, `POST /v1/user/visits`, `GET /v1/user/events/subscribe` (`Lhg/a;`, 5 methods) | C2 |
| profile & social | `GET /v1/users/{userId}/profile`, `/code`, `/report`, follow/unfollow (`Lih/a;`) | C2 |
| settings & avatar | `Lkf/a;` (4 methods incl. avatar upload) | C2 |
| identity itself | **no app endpoint** — FirebaseAuth talks to Google directly; `mimoauth.getmimo.com` (`hg.b`, `/api/sendCustomerIoData`) is a Customer.io relay, not a login exchange | C5 |

There is **no login/logout HTTP call in the app's own catalogue**. Authentication is entirely Firebase-SDK-mediated;
the first authenticated app request is whatever the UI does next.

## 5.7 Subscriptions and entitlements

`Lnh/c;` (`GET`/`POST /v1/products/user`) is the only product endpoint; entitlement state otherwise comes from
RevenueCat's SDK (its own network), and `PublicUser.isPremium` (mission-06). So the app's server knows about purchased
products, but the *purchase* itself never touches `api.mimo.org`.

## 5.8 Analytics and telemetry

| Sink | Transport | Evidence |
|---|---|---|
| app analytics batch | `POST /push/events` (`Lhg/d;`, **C4**, `track.customer.io`) | catalogue + case 53 |
| Customer.io identity relay | `POST /api/sendCustomerIoData` (`Lhg/b;`, **C5**) | case 87 |
| e-mail click tracking | `POST /click/{linkId}` (`Lph/b;`, **C6**) | case 117 |
| third-party SDKs | Firebase, Mixpanel, Adjust, Facebook, Sentry, RevenueCat (own clients) | class census |
| customer.io in-app SDK | 6 endpoints under `/api/v1/…` on `io.customer.*` interfaces | catalogue |

Note the split: the **app's own** analytics events do not go to `api.mimo.org`; they go to Customer.io's ingestion
host. Nothing in the client asserts what the backend does with them.

## 5.9 Local-only paths (no network at all)

* lesson rendering, grading, normalisation (Stages 3–4);
* chapter navigation and path map (content + Room completion cache);
* saved-code read from Room/asset cache when offline — only the save/run endpoints are networked;
* dev menu, settings toggles that only write `mimo_prefs`;
* the entire streak sink `gg.e` (Stage 5, B-5): no HTTP call recovered around it.
