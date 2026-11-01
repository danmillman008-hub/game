# Phase 6A — every persistence layer the app owns

| Layer | Identified by | Owned by app? | Content | Evidence |
|---|---|---|---|---|
| Room database `mimo.db` | `const-string "mimo.db"` in the DI provider, `const-class …local/room/Database;` | **yes** | 3 tables | `m;.a()` provider block; `Database_Impl` |
| SharedPreferences `mimo_prefs` | `const-string "mimo_prefs"` | **yes** | app preferences | string census |
| SharedPreferences `mimo_prefs_global` | `const-string "mimo_prefs_global"` | **yes** | global flags | string census |
| SharedPreferences `mimo_dev_prefs` | `const-string "mimo_dev_prefs"` | **yes** | developer menu (`sk/a`) | string census + `DevMenuStorage` usage |
| DataStore | `com.getmimo.data.local.a(Context, np/d)` built in the same provider block | **yes** | preferences-proto store | provider block |
| WorkManager DB `androidx.work.workdb` | `WorkDatabase_Impl`, delegate version **24** | library | job bookkeeping | `leg/e` second constructor |
| SDK stores | `com.google.android.gms.measurement.prefs`, `com.facebook.*`, `com_revenuecat_purchases_preferences`, `adjust_preferences`, `FirebasePerfSharedPrefs`, … | third party | n/a | string census, **excluded** from analysis |

The DI provider block that builds `mimo.db`:

```text
const-class Lcom/getmimo/data/source/local/room/Database;
const-string "mimo.db"
invoke-static {context, Database.class, "mimo.db"} → Lgv/a2;->g(...)   // Room.databaseBuilder
iput-boolean … Landroidx/room/c;->n Z
iput-boolean … Landroidx/room/c;->o Z
invoke-virtual Landroidx/room/c;->b() → RoomDatabase                  // Builder.build()
```

So there is exactly **one** database, opened through the standard builder, with the default journal mode (no
`setJournalMode` call is present in the block) and two builder flags set (see `ROOM_MIGRATION_AND_VERSIONING.md` §3).

## What is *not* in `mimo.db`

No user/account table, no lesson-content cache, no analytics buffer, no settings table, no "downloaded lessons"
table. Everything that looks like content comes from `tracks.json` in assets and from the network; the only durable
learner data is the three tables of Stage 5.
