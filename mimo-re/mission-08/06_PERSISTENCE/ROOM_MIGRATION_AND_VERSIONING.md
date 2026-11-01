# Phase 6B — schema version, migrations, destruction policy

## 1. Version

`leg/e` is the `RoomOpenHelper.Delegate` for `mimo.db`:

```text
Leg/e.<init>(Database_Impl)
    const/4 v4, 0            → iput-byte  Leg/e->d = 0
    const/4 v4, 2            → v1
    const-string "2b8ab6d303d9a501bd8c8fb78d8352fc"   (identity hash)
    const-string "9dc1d821a06045a1613b5d80f714188c"   (legacy hash, unused path)
    invoke-direct {v1=2, hash, legacyHash} Lx7/b0;-><init>(I …)      // version = 2
```

**Schema version 2**, identity hash `2b8ab6d303d9a501bd8c8fb78d8352fc`.

The same obfuscated class also carries the WorkManager delegate (`version 24`,
hash `08b926448d86528e697981ddd30459f7`) — a class-pooling artefact, not app data.

## 2. Migrations

| Check | Result |
|---|---|
| subclasses of `androidx.room.m` (`Migration`) in the APK | **0** |
| `Builder.migrations` (`d` field, `ArrayList`) populated | never — no `addMigrations` call site exists outside the library |
| auto-migration specs (`Database_Impl.j()`) | returns an **empty** `LinkedHashSet` |
| `onUpgrade` / `onDowngrade` logic in `leg/e` | none beyond the Room defaults (`s()` validates the schema) |

Consequence: the app has **no upgrade path**. Version 2 is the only schema this build can open without either an
identical schema or a destructive reset.

## 3. Destructive reset

The provider sets two `Builder` booleans right after the builder is created (`n` and `o`). In the Room 2.5 builder the
boolean fields after `allowMainThreadQueries` (`i`) are the migration-policy pair (`requireMigration`,
`allowDestructiveMigrationOnDowngrade`). The **pair being set together** matches `fallbackToDestructiveMigration()`,
which flips exactly those two flags.

Status: **INFERRED**, not verified — the two `iput-boolean` operands are registers whose values are assigned before the
provider block's linear window, so the literal `0`/`1` could not be read (question **B-9**). If the inference holds,
a version or schema mismatch silently wipes lesson progress and the completion cache, and no user-visible migration
notice exists anywhere in the code.

## 4. Validation path

`leg/e.s(...)` contains `check-cast … Database_Impl;` plus the three `CREATE TABLE` statements and the `clearAllTables`
call in `Database_Impl.d()`. This is the standard `RoomOpenHelper.Delegate` shape: identity-hash comparison on open,
`onCreate` executes the `CREATE TABLE`s, `onDestroy`/clear drops them.

## 5. What versioning means for learner data

* the schema version is **independent of** `publishSetVersion` (753, content) and `tutorialVersion` (per tutorial);
* bumping content does not touch the schema version;
* bumping the schema version without a migration is the only way local learner data can disappear, and there is no
  code that would survive it.
