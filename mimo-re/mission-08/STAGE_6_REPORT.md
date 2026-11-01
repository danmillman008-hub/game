# Mission 8 — Stage 6 Report (persistence and storage)

**Status:** `substantially_complete` (10 deliverables + 11 semantic tests) · **Base:** Stage 5 `a3e7d1b` · **2026-11-01**

## New evidence obtained in this stage

* the DI provider block that builds the database (`m;.a()`), giving the file name **`mimo.db`** and the exact builder
  call chain (`Room.databaseBuilder` → two boolean flags → `build()`);
* the `RoomOpenHelper.Delegate` (`leg/e`) whose constructor carries **schema version 2** and identity hash
  `2b8ab6d303d9a501bd8c8fb78d8352fc`;
* `Database_Impl`'s three DAO providers (`cg/a` lesson progress, `leg/c` chapter completions, `leg/f` tutorial
  completions), the invalidation tracker over the same three tables, and `j()` returning an **empty** set of
  auto-migration specs;
* the app-owned preference files (`mimo_prefs`, `mimo_prefs_global`, `mimo_dev_prefs`) separated from SDK stores.

## Findings

1. **One database, three tables.** `mimo.db` holds only `lesson_progress`, `tutorial_completions`,
   `chapter_completions`. There is no user, content-cache, analytics or settings table — so "offline content" is not
   stored in Room.
2. **No migration exists.** Zero `Migration` subclasses, empty auto-migration specs, no `addMigrations` call. Version 2
   is the only openable schema; a version bump without migration cannot preserve learner data.
3. **Destructive fallback is likely but not proven.** Two builder booleans are set together, matching
   `fallbackToDestructiveMigration()`'s flag pair. The operand values are outside the readable window → **B-9**.
4. **The outbox is the only self-cleaning table.** Only `lesson_progress` has DELETE statements (pending clear, and
   delete-by-ids after a 2xx). The two completion tables are never deleted by app code, so they are cumulative.
5. **No encryption.** No SQLCipher class and no `SupportOpenHelperFactory` argument in the builder block; the only
   keystore-looking string belongs to a third-party SDK.
6. **Cross-store writes are not transactional.** A completion fetch writes Room rows *and* a SharedPreferences pointer;
   a crash between them leaves a stale pointer with no reconciliation code.

## Limits

Five questions (B-9 … B-13), all about *values passed through generic helpers* (builder flags, preference keys,
DataStore key set). Nothing in this stage is `VERIFIED_RUNTIME`; the schema is `VERIFIED_STATIC` from the DEX
`CREATE TABLE` statements plus the delegate version constant.
