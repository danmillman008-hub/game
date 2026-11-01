# Stage 1 — Symbol confidence audit

**Tool:** `tools/build_symbol_recovery.py` · **Inputs:** the 12-dex set (hashes in `00_BASELINE/INPUT_HASHES.json`)
**Outputs:** `ORPHAN_LAMBDA_REGISTER.csv`, `LAMBDA_ENCLOSURE_MAP.json`, `ORIGINAL_METHOD_NAME_MAPPINGS.csv`,
`RENAMED_CLASS_REGISTER.csv`, `COMPONENT_CLUSTERS.json`, `UNRESOLVED_SYMBOLS.csv`, `RECOVERY_EVIDENCE.json`

## 1. Method, in one paragraph

Renaming replaced class names but preserved Kotlin lambda binary names, which still read
`<original.Class>$<originalMethod>$<n>`. For every app-named class containing `$` whose **root owner** is no longer
a `class_def`, the tool records the original owner and method, then inspects the lambda's instructions to find
which obfuscated class it actually calls into. Because renaming **kept the package**, only callees in the owner's
own package are accepted as candidates — this single rule removes the two false families that a naive version
produced (Orbit DSL builders `org.orbitmvi.orbit.syntax.b` and the logger `wc.f`), both of which are heavily called
by view-model lambdas but are not owners.

## 2. Numbers

| Metric | Value |
|---|---|
| orphan lambdas analysed (root owner absent) | **1,275** |
| distinct original owners | **265** |
| owners resolved with `HIGH` confidence | **76** |
| owners resolved with `MEDIUM` confidence | 45 |
| owners unresolved / low | 144 |
| original→renamed method mappings emitted | **436** (`HIGH 385`, `MEDIUM 51`) |
| renamed app classes in the register | **1,148** |
| … of which matched to at least one original owner | 21 |
| lambdas left completely unresolved | 44 |

## 3. Confidence rules (fixed, published)

| Confidence | Rule |
|---|---|
| `HIGH` | the owner family has ≥ 3 lambdas, the dominant same-package class receives ≥ 60 % of the family's qualifying invokes, and the mapping has exactly one method candidate |
| `MEDIUM` | family ≥ 2 with ≥ 45 % share, or a single lambda with ≥ 2 invokes to the candidate |
| `LOW` | a candidate exists but the family is thin or the share is small |
| `UNRESOLVED` | no same-package short-named candidate at all |

A guess is never promoted: `MEDIUM` stays `MEDIUM` unless a second independent source (interface declaration, DI
arm, DTO field) confirms it.

## 4. High-confidence owners that matter for the next phases

| Original owner | Renamed class | Share | Lambdas | Cluster |
|---|---|---|---|---|
| `data.local.DataStoreUserPreferences` | `com.getmimo.data.local.a` | 1.00 | 70 | persistence |
| `ui.lesson.executable.ExecutableLessonViewModel` | `com.getmimo.ui.lesson.executable.q` | 1.00 | 70 | executable lesson |
| `ui.projects.ProjectViewModel` | `com.getmimo.ui.projects.f` | 1.00 | 42 | projects |
| `ui.main.MainViewModel` | `com.getmimo.ui.main.d` | 1.00 | 39 | navigation |
| `ui.path.map.PathMapScreenKt` | `com.getmimo.ui.path.map.j` | 1.00 | 34 | path |
| `data.settings.SettingsRepository` | `com.getmimo.data.settings.a` | 1.00 | 26 | settings |
| `ui.reactivation.ReactivationViewModel` | `com.getmimo.ui.reactivation.k` | 1.00 | 26 | reactivation |
| `data.source.remote.authentication.AuthenticationFirebaseRepository` | `…authentication.a` | 1.00 | 18 | authentication |
| `ui.lesson.interactive.base.InteractiveLessonBaseViewModel` | `…interactive.base.c` | 1.00 | 18 | lesson engine |
| `ui.lesson.interactive.base.InteractiveLessonBaseFragment` | `…interactive.base.b` | 0.73 | 18 | lesson engine |
| `data.content.tracks.DefaultTracksRepository` | `…content.tracks.c` | 0.88 | 7 | content |
| `data.source.local.completion.CompletionRepository` | `…local.completion.a` | 1.00 | 7 | progress |
| `data.content.tracks.DefaultFavoriteTracksRepository` | `…content.tracks.a` | 1.00 | 6 | content |
| `data.source.remote.iap.PurchasesWrapper` | `…iap.c` | 1.00 | 6 | subscription |
| `data.source.remote.iap.BillingClientWrapper` | `…iap.b` | 0.60 | 6 | subscription |
| `data.source.remote.publicprofile.DefaultPublicProfileRepository` | `…publicprofile.a` | 1.00 | 4 | profile |
| `ui.developermenu.discount.DeveloperMenuDiscountViewModel` | `…discount.c` | 1.00 | 4 | discount |

These names are **evidence**, not inference: each is the class that the corresponding family of lambda classes
invokes, inside the package that the original class lived in.

## 5. Known limits (why the remaining 144 owners stay unresolved)

1. **Cross-package delegation** — some owners delegate their bodies almost entirely to a shared module (e.g. a
   training-session manager). The package rule then finds no candidate; reported unresolved rather than guessed.
2. **Property/delegate lambdas** — lambdas generated for `val x by lazy {}` or property delegates invoke nothing
   distinctive.
3. **Inlined suspend functions** — the compiler inlines them and the lambda disappears (`$$inlined$…` classes).
4. **Nested owners** — for `A$B$method$1` the root `A` may still exist while `A$B` does not; those are counted in
   the immediate-outer figure (1,379) but not in this register's 1,275.
5. **Merged classes** — 47 classes carry several original responsibilities; a mapping into one of them describes
   the branch, not the class.

## 6. What this unlocks

| Next phase | Uses |
|---|---|
| Phase 2 content delivery | `…content.tracks.c` = tracks repository; `…local.completion.a`; `…local.a` (preferences) |
| Phase 3 lesson engine | `…interactive.base.c` (base view-model), `…interactive.base.b` (base fragment), `…interactive.d` (interactive view-model) |
| Phase 5 learner/progress | `…local.completion.a`, `…local.a`, `…learner.*` families |
| Phase 9 AI tutor | `…local.aitutor.*` families (recovered below `MEDIUM`) |
| Phase 10 executable lessons | `…lesson.executable.q` |

## 7. Reproduction

```bash
cd mimo-re/mission-08
/tmp/venv/bin/python tools/build_symbol_recovery.py --dex-dir /tmp/x --out 01_SYMBOL_RECOVERY
# per-package method-name recovery (complements this stage)
/tmp/venv/bin/python tools/recover_method_names.py --dex-dir /tmp/x \
  --package com.getmimo.data.content.tracks --out /tmp/tracks_names.json
```
