# MISSION 07 — DATABASE_EVIDENCE

Room/SQLite evidence is **not duplicated here**; the authoritative raw data
lives in `ANALYSIS/RUNTIME/MISSION_07/DB/`:

* `SNAPSHOT_*.json` — file inventory, `sqlite_master` SQL, table schemas,
  row counts, row samples and group counts for every consistent on-device
  `.backup` database (stages 2/4/5/6, states A–I).
* `SNAPSHOT_*/private/` and `SNAPSHOT_*/consistent_*` — raw DB, WAL, SHM,
  `shared_prefs`, `files/datastore`, `no_backup`.
* `SNAPSHOT_S5_1_C…F.json` — the requested before/after diff: 1 row → 2 rows
  with new `lesson_progress` row `151403`.
* `DEVICE_SQLITE_INVENTORY.txt`, `PREFS_AND_DATASTORE.txt`.

Extracts and the full analysis: `../06_DATABASE_BEFORE_AFTER.md`,
`../07_PERSISTENCE_RESTORATION_AND_QUEUE.md`. Schema cross-reference:
`ANALYSIS/MISSION_05/EVIDENCE/ROOM_SQL.txt`.
