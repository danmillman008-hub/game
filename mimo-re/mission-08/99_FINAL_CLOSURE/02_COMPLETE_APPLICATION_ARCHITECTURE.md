# 02 — Complete application architecture

Six layers, each with the classes that actually implement it. Everything below is `VERIFIED_STATIC` unless marked.

## 1. Layer map

```text
┌──────────────────────────────── Activity / Compose UI ─────────────────────────────────┐
│ MainActivity (12 deep-link intent filters, mimo://) → navigation graph → screens         │
│ ViewModels (interactive lesson, chapter, chapter-end, executable, AI tutor, profile, …)  │
├─────────────────────────────── use cases / interactors ────────────────────────────────┤
│ GetChapterEndSuccessState · GetPathMapState · GetPracticeTopics · GetSignupPrompt · …    │
├──────────────────────────────────── repositories ──────────────────────────────────────┤
│ content: ye.b/ye.g  · progress: LessonProgressRepository/Queue · completion: a (Completion)│
│ network: remote.* (29 interfaces) · analytics: analytics.a · settings: kf.*              │
├────────────── local store ──────────────┬───────────── transport ───────────────────────┤
│ Room mimo.db (3 tables, 3 DAOs, v2)     │ OkHttp C1 (3 interceptors) → Retrofit C2      │
│ SharedPreferences mimo_prefs*            │ dedicated clients C3–C6 · SSE C7 · WS C8     │
├───────────────────────────── external services (SDK-owned) ────────────────────────────┤
│ Firebase (Auth, RC, Analytics, FCM) · RevenueCat · Adjust · Sentry · Customer.io · Pusher│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## 2. Startup

Application class → Hilt component (single `oy.t`/`ae.m` switch, **127 provider cases**) → `MainActivity` →
`MainViewModel` which immediately triggers the progress flush
(`fetchLessonProgressAndPostUnsyncedToBackend`) and the favourite-track completion sync. No splash-time network block
exists on the content path.

## 3. Dependency injection

One component, no subcomponents in the recovered set. Provider tokens relevant to the data layer: `v` = OkHttp C1
(case 20), `w` = API host (case 22), `u` = connectivity provider (`ri.d`), `e` = kotlinx converter (`jx.d`), `b()` =
token provider (`ku.a`). Full map: `07_NETWORKING/09_DI_DEPENDENCY_MAP.json`.

## 4. UI ownership

Navigation graph (mission-07 `73_COMPLETE_NAVIGATION_GRAPH.json`) → screen catalogue
(`74_SCREEN_AND_COMPONENT_CATALOG.csv`) → per-screen view-model. The lesson surface is owned by
`InteractiveLessonBaseViewModel` (subclasses per content type), the executable variant by `ExecutableLessonViewModel`.

## 5. Coroutines and threading

Repository suspend functions over `Dispatchers.IO` through `DBUtil.performSuspending` for Room; OkHttp calls are
cancellable through Retrofit's suspend adapter. Two known **blocking** bridges on OkHttp threads: `Tasks.await` inside
`ku.a.d` (token) and inside the deferred-account-deletion worker.

## 6. Error handling

Transport errors are exceptions (`IOException` from `hg.e`, `HttpException` for direct-body calls, status inspection for
the 12 `Response<T>` sites). There is **no** global error type, no `Result` wrapper (correction C-20), no retry policy
and no 401 path.

## 7. Domain ownership of state

| State | Owner | Durable? |
|---|---|---|
| content (tracks/tutorials/chapters/lessons) | assets, read-only | yes (APK) |
| lesson progress | Room `lesson_progress` | only until posted |
| completion | Room `tutorial_completions` / `chapter_completions` | yes, cumulative |
| identity/token | FirebaseAuth | SDK-managed |
| preferences/dev flags | `mimo_prefs*` | yes |
| entitlement | RevenueCat cache + `PublicUser.isPremium` | SDK-managed |
| analytics queue | SDK | outside scope |

## 8. What the architecture does *not* have

No offline-first sync engine (no merge, no conflict resolution, no retry queue beyond the outbox), no local
authorization model (no per-account partition), no content cache in Room, no client-side completion or unlock logic,
no background sync worker for progress, no multi-module feature installation path (dynamic modules are stubs).
