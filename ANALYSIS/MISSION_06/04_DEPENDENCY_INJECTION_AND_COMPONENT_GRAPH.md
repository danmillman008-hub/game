# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**Target:** original Mimo Android 9.35 APK, SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Branch:** `arena/aebb90b7-game`, baseline `d0714b40`  
**Toolchain:** Androguard 4.1.4 in `/home/user/_work/m06/venv` over all 12 original
`ANALYSIS/_INPUT/classes*.dex`; patched read-only harness `EVIDENCE/M06_DEX_HARNESS.py`.  
`SERVER CONFIRMED = 0`. Backend services, server business logic, server databases and cloud
infrastructure are **not** reconstructed; only client-side boundaries are recorded.

> Every finding is classified `VERIFIED_STATIC`, `VERIFIED_RUNTIME`, `VERIFIED_BOTH`,
> `INFERRED` or `UNKNOWN`. Evidence fields (APK path, class/method, DEX file + code offset,
> bytecode/Smali, caller/callee, SQL, runtime log, reproduction steps) are given inline or in
> the referenced `EVIDENCE/`, `SCHEMAS/`, `CALL_GRAPHS/`, `METHOD_DOSSIERS/` artefacts.

---

## Verified dependency edges
`CALL_GRAPHS/02_class_dependency.mmd` is drawn from real `iget-object`/`invoke` operands;
`CALL_GRAPHS/*.json` list exact signatures and code offsets.

### `Lhm/b;` (13 Object slots) — VERIFIED_STATIC
`base/c;-><init>(Lhm/b;)V` stores the container in field `b`. Verified casts:
| Slot | Cast target | Used by |
|---|---|---|
| `a` | (not decoded) | `O()` |
| `b` | `Lcom/getmimo/analytics/a;` | `f0()`, `a0()`, `g0()` |
| `c` | (not decoded) | |
| `d` | `LessonProgressRepository` | `H()` |
| `e` | (not decoded) | |
| `f` | (not decoded) | |
| `g` | `Lcom/getmimo/data/local/a;` | `d0()` |
| `h` | `Lmf/a;` (filesDir `File`) | `D()` cleanup |
| `i` | `Lcom/getmimo/ui/lesson/sound/a;` | `V()` success sound |
| `j..m` | (not decoded) | |

### Constructor-injected graphs (VERIFIED_STATIC signatures)
- `InteractiveLessonBaseViewModel(Lhm/b;)`
- `InteractiveLessonFillTheGapViewModel(Lbg/a; Lhm/b; Lim/b; base/d;)`
- `InteractiveLessonSelectionViewModel(Lbg/a; Lhm/b; Lnm/f; base/d;)`
- `InteractiveLessonSpellViewModel(Lbg/a; Lhm/b; Lpm/g; base/d;)`
- `InteractiveLessonValidatedInputViewModel(Lqf/d; Lbg/a; Lhm/b; Lqm/i;)`
- `InteractiveWebViewLessonViewModel(Lhm/b;)`
- `InteractiveLessonViewModel(Lye/g; Lgm/h; awesome/b; Lnp/g; codeeditor/highlight/a;)`
- `ExecutableLessonViewModel(32 parameters incl. `Lye/g;`, `LessonProgressRepository`,
  `analytics/a;`, `Lpe/a;`, `LessonProgressQueue`, `Lqf/d;`, `Lze/a;`, `Lbg/a;`,
  `Lri/d;`, `Lmf/a;`, sound, dispatchers, `Lds/z;`, `Lcm/e;`, `interactors/path/a;`,
  `interactors/playgrounds/d;`, `Lmh/b;`, `Lkf/d;`, `Lgi/e;`, IAP, `inputconsole/a;`,
  AiTutor, `interactors/lesson/b;`, `Lep/t0;`, `codeeditor/highlight/a;`)
- `DefaultTracksRepository(Lye/e; Lfe/a;)`, `DefaultTrackLoader(...)`,
  `LessonProgressRepository(LessonProgressApi; Lye/g; Lye/c; Lnp/d; Lri/d; completion/a; Lcg/a;)`
- `ChapterViewModel(Lye/c; Lze/a; analytics/a; LessonProgressQueue; Lmf/a; SavedStateHandle;
  chapter/c; chapter/b; Lri/d; chapter/e; IAP; Lnp/d; Lce/c; data/local/a;)`
- `GetPathMapState`/`GetPathMapDialogs` take 15 collaborators (purchase repository,
  feature flags, analytics, network utils, dev-menu, path interactors…).

### DI framework — `UNKNOWN`
No `@Inject` annotation metadata, Hilt component classes or Koin module DSL were decoded in
M06. Naming/injection shape is `INFERRED` as compile-time constructor injection. Exact
framework, scopes and singleton graph = `UNKNOWN` with pointer: constructor signatures in
`SCHEMAS/METHOD_CATALOG_MIMO.json` (search `<init>`).

### Background workers / services — VERIFIED_STATIC
`PostVisitWorker`, `AccountDeleteWork`, `StreakWidgetRefreshWorker`,
`MimoStreakWidget`, `NotPremiumNotificationService`, `CustomerIOPushNotificationRegistry`,
WorkManager `CoroutineWorker` subclasses. Their triggers/periodicity were not decoded =
`UNKNOWN`.
