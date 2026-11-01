# 13 — Local persistence and state ownership

## 1. The Room database contains exactly three tables (V)

Recovered from `CREATE TABLE` literals in
`com.getmimo.data.source.local.room.Database` (`data/room-schema.sql`):

```sql
CREATE TABLE IF NOT EXISTS `lesson_progress` (
  `lesson_id` INTEGER NOT NULL, `completed_at` INTEGER NOT NULL, `started_at` INTEGER NOT NULL,
  `tries` INTEGER NOT NULL, `tutorial_id` INTEGER NOT NULL, `tutorial_version` INTEGER NOT NULL,
  `track_id` INTEGER NOT NULL, `publish_set_version` INTEGER NOT NULL,
  `attempts` INTEGER NOT NULL, `is_practice_progress` INTEGER NOT NULL, `in_queue` INTEGER NOT NULL,
  PRIMARY KEY(`lesson_id`, `tutorial_id`));

CREATE TABLE IF NOT EXISTS `chapter_completions` (
  `chapter_id` INTEGER NOT NULL, `created_at` INTEGER NOT NULL,
  `track_id` INTEGER NOT NULL, `tutorial_id` INTEGER NOT NULL,
  PRIMARY KEY(`chapter_id`, `track_id`));

CREATE TABLE IF NOT EXISTS `tutorial_completions` (
  `tutorial_id` INTEGER NOT NULL, `is_completed` INTEGER NOT NULL, `updated_at` INTEGER NOT NULL,
  `track_id` INTEGER NOT NULL, PRIMARY KEY(`tutorial_id`, `track_id`));
```

DAOs seen (V literals): `SELECT * FROM chapter_completions WHERE track_id = ? AND tutorial_id in (…)`,
`SELECT * FROM tutorial_completions WHERE track_id = ? AND tutorial_id in (…)`,
`DELETE FROM lesson_progress WHERE lesson_id IN (…)` (after a successful sync).

## 2. What is *not* in the database — and why that is the design

| State | Where it lives | Evidence |
|---|---|---|
| Content (tracks, tutorials, lessons) | `assets/lessons-<lang>` (read-only files, parsed on demand) | pack inventory |
| Streak, coins, keys, league, rewards | **server only**, mirrored in memory/UI state | `/v1/user/*` endpoints, no tables |
| User profile, settings | server (`/v1/user/settings`), cached in prefs | endpoint + `SettingsActivity` |
| AI tutor messages | server (`conversationId`), no local table | `AiTutorConversationMessage(conversationId, content, finishReason)` |
| Saved code / projects | server (`/v1/code`, `…/savedFiles`), local autosave buffers | `SavedCode(id, name, hostedFilesUrl, files, modifiedAt, isPrivate, hackathonId)` |
| Certificates | server (`/v1/tracks/{trackId}/certificates`) | endpoint + `CertificateActivity` |
| Experiment/flag values | Firebase Remote Config + prefs (`abt_experiments_key`) | remote-config keys |
| Hard/fast mode, daily goal | prefs (no columns) | absence of columns + `hardModeSelected`/`fast_mode` literals (I) |

**The rule:** the device stores only what it must *not* lose when offline — graded progress —
and treats everything else as a projection of server state. There is no offline-first content
database; the content is immutable files.

## 3. State ownership map (who is authoritative for what)

| Fact | Authority | Client behaviour on conflict |
|---|---|---|
| lesson completed? | server (but client writes optimistically) | `in_queue=1` rows retried; server wins on success (I) |
| attempts / tries | client increments, server accepts | monotonic counters |
| long-term progress | server | Room is a cache + outbox |
| streak / coins / keys | server | displayed from server, never computed locally |
| entitlements (Pro) | RevenueCat → `/v1/subscribers/*` | server-side check per feature |
| content text | **APK assets** | no conflict possible |
| experiment assignment | Firebase A/B + server (`ContentExperiment`) | server wins |
| AI tutor quota | server (`usedMessages`) | optimistic decrement (I) |

## 4. The outbox pattern (V + I)

`lesson_progress.in_queue` + `LessonProgressQueue` + `LessonProgressRepository$postUnsyncedLessonProgress$2`
→ `DELETE FROM lesson_progress WHERE lesson_id IN (…)` on success. So:
1. grading writes a row (or updates it) with `in_queue=1`;
2. a WorkManager job (`WorkManager` present, 19 services) posts unsynced rows to
   `/v1/tutorials/{tutorialId}/progress`;
3. on 2xx, the rows are **deleted from Room**, not marked synced — meaning Room holds *only*
   un-synced progress plus completion tables. That is why the app can be reinstalled without
   losing progress (it is on the server) but shows nothing offline until it syncs.

`chapter_completions` and `tutorial_completions` follow the same pattern with `created_at` /
`updated_at` timestamps and no sync flag — their rows are the app's *local read model* of
"what's done", refreshed from the server.

## 5. Failure semantics

* `chapter_finish_sync_error` (V analytics/config key) ⇒ a chapter completion can fail to sync
  and is surfaced.
* `Error when executing the MFEL` and `Error sending/receiving ai message` show per-feature
  error handling rather than a global one.
* No local encryption: `allowBackup=false`, no `SQLCipher`, no encrypted prefs (V negative
  finding) ⇒ progress and cached profile data are readable on a rooted device.

## 6. Konkur transfer

| Mimo decision | Verdict | Reason |
|---|---|---|
| 3-table Room schema + outbox flag | **Reuse** | Minimal, provably correct; easy to extend |
| Content as read-only assets | **Exclude** | Konkur needs downloadable question banks + figures |
| Server-authoritative economy | **Reuse** | Non-negotiable for exams (anti-cheat) |
| Progress triple with versions | **Reuse** | Survives content corrections |
| No local encryption | **Exclude** | Iranian app-store reviews + user trust; encrypt prefs, at least |
| Deleting synced rows | **Adapt** | Keep a compact "answered question ids" table locally; Konkur users study offline a lot |

For Konkur, add three local tables Mimo does not need:
`question_attempt(questionId, chosen, correct, ms, at, synced)` — the weakness model's raw
material; `bookmark(questionId, at)`; `simulation_result(examId, score, per-topic JSON, at)`.
Without `question_attempt` on device, Mode C cannot compute a plan while offline.
