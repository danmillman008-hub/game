# 16 — Offline behaviour and synchronisation

Mimo is **partially offline-first by accident of packaging**: the entire curriculum is local, so
learning works offline; everything social, commercial and executable does not. The app is
explicit about this — 14 offline-specific strings and a connectivity probe endpoint.

## 1. Offline capability matrix (V except where noted)

| Capability | Offline | Evidence |
|---|---|---|
| Open a path, chapter, lesson | ✅ | content is in `assets/lessons-<lang>` |
| Interactive lesson (fill gap, validated input, selection) | ✅ **and grades offline** | answers derived from markup (§07) |
| Hard-mode variants | ✅ | bundled in lesson JSON |
| Progress recording | ✅ locally, ⏳ sync later | `in_queue` + outbox (§13) |
| Executable lesson (run code) | ❌ | `executable_lessons_connection_warning`, `ConnectivityError` |
| Autosave of code | ✅ locally, ⏳ server later | `AutoSaveCodeService`, `savefiles` endpoint |
| AI tutor | ❌ | `ai_tutor_offline_description`, `State.offline` |
| Practice hub selection | ❌ (server picks) | `practice_offline_*` |
| Store / paywall / purchase | ❌ | `store_offline_message` |
| Leaderboard / league | ❌, cached view | `leaderboard_offline_message` |
| Streak display | cached; grant needs network (I) | widget has `stateWithoutData` |
| Profile / friends | ❌, cached | `profile_offline_description`, `friends_offline_message` |
| Certificates | ❌ (generated server-side) | `/v1/tracks/{id}/certificates` |
| Lesson report | ❌ | `report_lesson_offline_message` |
| Content update | ❌ (ships in APK) | no content endpoint |
| Map / integrated webview | ❌ | `map_offline_description`, `integrated_webview_offline_view` |

## 2. Sync design (V + I)

```
grade lesson ──► Room upsert (in_queue = 1) ──► UI updates immediately
                      │
                      └─► WorkManager (network-constrained, I)
                             POST /v1/tutorials/{tutorialId}/progress
                                ├─ 2xx → DELETE FROM lesson_progress WHERE lesson_id IN (…)
                                └─ error → keep row, retry; surface chapter_finish_sync_error
chapter end ──► chapter_completions / tutorial_completions upsert (no sync flag)
                 └─► POST /v1/tracks/{trackId}/completion (I)
```
Properties of this design worth noting:
1. **Deletion on success** means Room never accumulates history; the server is the only long-term
   record. Consequence: a device that never syncs shows "completed" only because the completion
   tables are local; a *fresh install without network* shows nothing.
2. **No conflict resolution**: progress is monotonic (`tries`, `attempts`, `completed_at`), so
   last-write-wins is safe by construction. That is a deliberate and clever simplification.
3. **No content sync**: the app never asks "is my curriculum current?" — version skew between a
   user's progress and a newer pack is resolved server-side by `publishSetVersion` (I).
4. **Connectivity probe**: `/v1/health/connectivity` provides an explicit online check for the
   offline views (`offline_view_refresh`), rather than relying on the OS network callback alone.

## 3. Failure surfaces

| Failure | Handling (V strings) |
|---|---|
| Chapter completion could not sync | `chapter_finish_sync_error` analytics key + retry |
| Code execution blocked | `executable_lessons_connection_warning` |
| AI tutor offline | dedicated description + retry on reconnect |
| Account creation deferred | `delayed_account_creation_offline_error` — learning is allowed before signup |
| Cache clearing (dev) | `Cleared the cache successfully.` |

## 4. Weaknesses

* No offline **queue visibility**: the user is not told "3 lessons pending sync".
* No offline **entitlement cache semantics** documented; a Pro user offline sees Pro UI but
  features that need the server (AI tutor) fail.
* Deleting synced rows means an offline device that is factory-reset loses recent unsynced
  progress (there is no export).
* `allowBackup=false` compounds this: no OS-level backup of the outbox.

## 5. Konkur transfer — this is the one area where Konkur must be *better*

Konkur users study in unreliable mobile networks and on shared devices. Recommendations:

| Need | Mimo equivalent | Konkur requirement |
|---|---|---|
| Lesson content available offline | ✅ assets | ✅ **downloaded packs with integrity hash + delta updates** |
| Grading offline | ✅ derived answers | ✅ same mechanism for objective questions |
| Attempt history offline | ❌ only 3 tables | ✅ `question_attempt` table with per-topic aggregates |
| Study plan computed offline | ❌ server | ✅ cache plan + recompute locally on missed days |
| Sync with visible state | ❌ silent | ✅ explicit "۳ درس در انتظار همگام‌سازی" indicator |
| Conflict policy | last-write-wins | same (monotonic counters) — reuse |
| Exam simulation offline | n/a | ✅ must work fully offline; scoring is client-side and signed |
| Account-optional usage | ✅ deferred signup | ✅ essential (students switch devices) |

Two design rules to carry over verbatim: **monotonic counters instead of conflict resolution**,
and **a dedicated lightweight connectivity probe** for choosing which UI variant to render.
