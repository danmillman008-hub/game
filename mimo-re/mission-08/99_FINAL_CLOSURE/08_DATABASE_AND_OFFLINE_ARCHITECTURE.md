# 08 — Database and offline architecture

## 1. Database

| Property | Value |
|---|---|
| File | `mimo.db` |
| Class | `com.getmimo.data.source.local.room.Database` / `…Database_Impl` |
| Version | **2** |
| Identity hash | `2b8ab6d303d9a501bd8c8fb78d8352fc` |
| Tables | `lesson_progress`, `tutorial_completions`, `chapter_completions` |
| DAOs | `cg/a` (progress), `leg/c` (chapter completion), `leg/f` (tutorial completion) |
| Indices / FKs | none declared |
| Migrations | **0** subclasses, no `addMigrations`, empty auto-migration set |
| Encryption | none (no SQLCipher, no open-helper factory argument) |
| Destructive fallback | **inferred** (two builder flags set as a pair) — `B-9` blocked |

Statements: 4 for progress (select pending / move / clear / select-all) plus delete-by-ids; completion tables have
insert + select-by-track only (`Q-54`, `B-13`).

## 2. Secondary stores

`mimo_prefs`, `mimo_prefs_global`, `mimo_dev_prefs` (SharedPreferences); a Preferences DataStore
(`com.getmimo.data.local.a`); WorkManager's `androidx.work.workdb` (library). SDK stores excluded.

Only one app preference key is evidenced end-to-end: `last_interacted_tutorial_id_<trackId>` (written by the completion
fetch). It has **no reader** in recovered code; the "continue" pointer is the network call
`GET /v1/tracks/completion/lastInteracted` (`B-10` closed).

## 3. Offline capability matrix (summary)

`08_OFFLINE_CAPABILITY_MATRIX.csv` holds all 18 rows. The shape:

| Capability | Offline |
|---|---|
| start, browse tracks, open lessons, render, grade, feedback, next lesson | **yes** |
| persist progress, restart, resume | **yes** (Room) |
| see completion / unlock next chapter | **no** (server-derived; cached values only until refetch) |
| upload progress | deferred (outbox) |
| coins, streak, daily goal, leaderboards, profile | **no** |
| AI tutor, code execution | **no** |
| subscription/paywall | cached entitlement only |

Verdict: **content-offline, progression-online**. Calling the app "offline-capable" without that qualifier would be
wrong.

## 4. Consistency risks (evidenced)

1. completion row + preference pointer are written in two stores without a transaction;
2. a chapter exit can delete pending rows before a flush (`B-6`);
3. a successful POST deletes rows before the completion fetch, so a crash in between leaves the server ahead of the
   local cache until the next fetch;
4. a schema bump without migration destroys learner data (no upgrade path exists).
