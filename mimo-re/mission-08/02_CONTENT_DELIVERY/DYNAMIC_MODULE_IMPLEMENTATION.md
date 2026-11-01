# Phase 2.6 — Dynamic content modules (measured)

## 1. What the APK actually contains

| Locale | Module dex | dex size | Classes in base APK | Lesson assets in base APK |
|---|---|---|---|---|
| ru | `classes4.dex` | 1,096 B | `…content.ru.BuildConfig`, `…content.ru.R` | yes (`assets/lessons-ru`, 1,030 JSON) |
| pt | `classes5.dex` | 1,096 B | `…pt.BuildConfig`, `…pt.R` | yes (1,030) |
| id | `classes6.dex` | 1,096 B | `…id.BuildConfig`, `…id.R` | yes (1,032) |
| it | `classes7.dex` | 1,096 B | `…it.BuildConfig`, `…it.R` | yes (1,032) |
| pl | `classes8.dex` | 1,096 B | `…pl.BuildConfig`, `…pl.R` | yes (1,032) |
| fr | `classes9.dex` | 1,096 B | `…fr.BuildConfig`, `…fr.R` | yes (1,030) |
| tr | `classes10.dex` | 1,096 B | `…tr.BuildConfig`, `…tr.R` | yes (1,032) |
| es | `classes11.dex` | 1,096 B | `…es.BuildConfig`, `…es.R` | yes (1,030) |
| en | base | — | base classes | yes (1,030) |
| common | base | — | base classes | `lessons-common` (icons, 0 JSON) |

## 2. Interpretation, restricted to what is proven

* Eight locale **code modules** are declared as separate modules (their `R` and `BuildConfig` survive in dedicated
  1,096-byte dex files). A module `R` class is only generated for a Gradle module, so their existence proves the
  module structure.
* Their **lesson assets are nevertheless present** in the supplied APK's `assets/` tree, for all ten locales,
  with 1,030–1,032 JSON documents each and a `tracks.json` carrying `publishSetVersion: 753`.
* Therefore the earlier phrasing "non-English packs absent" is **too strong**: the *code* of the modules is
  stubbed, the *content* is shipped as assets. Q-05 is refined accordingly (correction **C-12**).

## 3. What remains genuinely absent

* the feature-module dex bodies (any classes the modules would add beyond `R`/`BuildConfig`),
* any per-locale *code* differences (e.g. locale-specific normalisation) — those must live in the base APK,
* Play Feature Delivery installation state (no `SplitInstallManager` reference exists in the dex — measured
  negative in Stage A).

## 4. Fallback behaviour

Not observable in Phase 2: `ye.b` derives its base path from `"lessons-"` + locale and does not branch on module
availability, which suggests content is never missing for a shipped locale. Whether a *missing* locale falls back
to `en` is not proven — recorded as question **A12**.
