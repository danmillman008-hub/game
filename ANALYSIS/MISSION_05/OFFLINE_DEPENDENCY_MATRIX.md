# OFFLINE_DEPENDENCY_MATRIX — feature-by-feature offline feasibility

Columns (as required): **logic local?** · **content packaged?** · **server
response needed?** · **auth needed?** · **remote config needed?** ·
**replaceable by local storage/logic?** · **exact missing information**.

`VERIFIED_STATIC` facts come from APK assets, DEX strings/classes, JADX sources
and the 53 resolved Retrofit endpoints. `VERIFIED_RUNTIME` facts come from M04/M05
emulator runs. `INFERRED` / `UNKNOWN` are marked explicitly.
No backend business logic is reconstructed. `SERVER CONFIRMED = 0`.

## 1. Matrix

| # | Client feature | Logic local | Content packaged | Needs server | Needs auth | Needs remote config | Replaceable locally | Exact missing information for offline |
|---:|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| 1 | Read tracks / sections / tutorials / chapters / lessons | ✅ `VERIFIED_STATIC` | ✅ `VERIFIED_STATIC` (10,298 JSON, v753, 10 locales) | ❌ | ❌ | ❌ | ✅ nothing to replace | none |
| 2 | Locate tutorial file by id / locale | ✅ `VERIFIED_STATIC` (`DefaultTrackLoader`, `lessons-<locale>/tracks/tutorial-<id>.json`) | ✅ | ❌ | ❌ | ❌ | ✅ | none |
| 3 | Render prose / code blocks (`<p>`,`<code>`,`<text>`) | ✅ `VERIFIED_STATIC` (parser + WebView + `highlight.min.js`, `prettier`, fonts, CSS shipped) | ✅ | ❌ | ❌ | ❌ | ✅ | exact renderer token-index algorithm for `validatedInput` (`UNKNOWN`) |
| 4 | Multiple-choice answer & feedback | ✅ `VERIFIED_STATIC` (`item correct=`, `visible-if`) | ✅ | ❌ | ❌ | ❌ | ✅ | none |
| 5 | Fill-the-gap / validated-input evaluation | ✅ `VERIFIED_STATIC` class names; `INFERRED` rule | ✅ | ❌ | ❌ | ❌ | ✅ | exact `startIndex/endIndex`→token mapping (`UNKNOWN`) |
| 6 | Embedded interactive WebView exercises | ✅ `VERIFIED_BOTH` (bridge JS static; `lib/arm64` loads runtime) | ✅ | ❌ | ❌ | ❌ | ✅ | 4,257 external URL references (below) |
| 7 | Hard-mode alternate lesson body | ✅ `VERIFIED_STATIC` (6,058 bodies) | ✅ | ❌ | ❌ | ❌ | ✅ | none |
| 8 | Hints / instructions / reference solution for executable lessons | ✅ `VERIFIED_STATIC` (`executableContent.hints`, `files[].solvedContent`) | ✅ | ❌ | ❌ | ❌ | ✅ | whether `solvedContent` is used locally for validation (`INFERRED`, `UNKNOWN`) |
| 9 | Per-lesson progress record | ✅ `VERIFIED_STATIC` (Room `lesson_progress`, `in_queue`) | n/a | ❌ for write; ✅ for sync | ❌ | ❌ | ✅ | none for local-only; sync queue needs a local equivalent of `POST /v1/tutorials/{id}/progress` |
| 10 | Chapter / tutorial completion rows | ✅ `VERIFIED_STATIC` (Room `chapter_completions`, `tutorial_completions`) | n/a | ❌ for write; ✅ for sync | ❌ | ❌ | ✅ | exact completion threshold (`UNKNOWN`) |
| 11 | Locked / unlocked path nodes | `INFERRED` (`GetPathMapState$invoke$3`: `isCompleted`/`isRequired`/`getType`) | ✅ node list shipped | ❌ for shipped nodes; ✅ for remote completion | ❌ | ⚠️ `INFERRED` (feature gates) | ✅ **if** the rule is recovered | exact unlock mapping (`UNKNOWN`, M02 gap #1) |
| 12 | Path-map geometry / scroll / animation | ✅ `VERIFIED_STATIC` (146 constants, Compose composables) | ✅ | ❌ | ❌ | ❌ | ✅ | X/Y assignment, curve function, scroll restore (`UNKNOWN`, M02 gaps #2–5) |
| 13 | Executable lesson code RUN + automated tests | ⚠️ partly: `spieglein/editor.bundle.js` + WebView for HTML/CSS/JS | ✅ starting code | ✅ `POST …/runFiles`, `/v1/code/runfiles` | ⚠️ `INFERRED` | ❌ | ✅ **replaceable** by a local JS engine / interpreter per language | exact test-case semantics, per-language runner behaviour, `ExecuteFilesResponse.tests[]` shape at runtime (`UNKNOWN`) |
| 14 | Saved code / user project files | ❌ (`/v1/code`, `…/savefiles`, `…/savedFiles`) | ❌ (user-generated) | ✅ | ✅ `INFERRED` | ❌ | ✅ local file store | exact file model and sync conflict rule (`UNKNOWN`) |
| 15 | Track ETA / estimated completion date | ❌ (`GET /v1/tracks/{id}/eta`) | ❌ | ✅ | ⚠️ | ✅ `INFERRED` | ✅ omit or compute locally from local progress | `TrackEta` computation formula (`UNKNOWN`) |
| 16 | Track completion / last-interacted sync | ❌ (`GET /v1/tracks/{id}/completion`, `/completion/lastInteracted`) | ✅ local Room rows | ✅ | ✅ `INFERRED` | ❌ | ✅ use Room rows only | merge/conflict rule (`UNKNOWN`) |
| 17 | XP / Sparks / Coins / Keys balances | ❌ (`/v1/user/coins`, `/keys`, `/v2/client-config`) | ❌ | ✅ | ✅ `INFERRED` | ✅ | ✅ define a local economy | all formulas and starting values (`UNKNOWN`) |
| 18 | Streak (current, longest, freeze, repair) | ❌ (`GET /v1/user/activity`) | ❌ | ✅ | ✅ | ✅ | ✅ compute from local timestamps | break/repair/freeze rules (`UNKNOWN`) |
| 19 | Daily goal (level, progress, reward) | ⚠️ local level in DataStore; result server-side (`getReachedGoal`) | ❌ | ✅ | ✅ | ✅ | ✅ compute locally | `dailySparksGoal` per level, coin reward (`UNKNOWN`) |
| 20 | Chapter-end success screen (rewards/leaderboard/ETA/streak) | ⚠️ `handleOnlineState` / `handleOfflineState` branches exist | ⚠️ partial | ✅ | ✅ | ✅ | ✅ local variant from Room | exact offline fallback composition (`UNKNOWN`) |
| 21 | Leaderboard / leagues | ❌ (`/v1/leaderboards/*`) | ❌ | ✅ | ✅ | ✅ | ❌ not reproducible offline (multi-user) | — genuinely requires other users |
| 22 | Favourite tracks | ⚠️ local `FavoriteTracks` + remote sync (`/v1/user/favorites/tracks`) | ✅ | ✅ for cross-device | ✅ | ❌ | ✅ local list | sync conflict rule (`UNKNOWN`) |
| 23 | Onboarding questionnaire + path selection | ✅ `VERIFIED_STATIC` + **`VERIFIED_RUNTIME`** (12 states, run `42002808217`) | ✅ (`LoadOnboardingPaths`, 19 tracks) | ❌ for the first 12 states (**cold start offline works**) | ❌ for the first 12 states | ✅ `INFERRED` (A/B experiments) | ✅ | states after "10M+ people" reassurance, gating, and which later steps call the server (`UNKNOWN`) |
| 24 | Authentication / signup / login | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ out of scope | user account data — deliberately not created |
| 25 | AI tutor | ❌ (`/v1/aiTutor/...`) | ❌ | ✅ | ✅ | ✅ | ❌ (must be replaced by a local model or removed) | model/prompts (`UNKNOWN`) |
| 26 | Subscriptions / paywall / purchases / certificates | ❌ (`/v1/products/user`, `/v1/package/preview`, `/v1/tracks/{id}/certificates`) | ❌ | ✅ | ✅ | ✅ | ✅ remove/omit | — out of scope for offline learning |
| 27 | Push notifications / reminder time | ⚠️ local scheduling | ❌ | ✅ for delivery tokens | ✅ | ✅ | ✅ local alarms | token registration (`UNKNOWN`) |
| 28 | Analytics / attribution / crash reporting | ⚠️ SDKs present | ❌ | ✅ | ❌ | ✅ | ✅ drop | — not needed for learning |
| 29 | Remote config / A-B tests / feature gates | ❌ (`GET /v2/client-config`, `remote_config.json`, Firebase RC) | ❌ | ✅ | ❌ | ✅ | ✅ pin defaults locally | exact default values for each gate (`UNKNOWN`) |
| 30 | External images / demo APIs inside lessons | ✅ rendering local (WebView) | ❌ **not packaged** | ✅ for those URLs | ❌ | ❌ | ✅ mirror into APK assets | **4,257** URL references; see §2 |
| 31 | Fonts / CDN JS inside embedded webviews | ✅ | ❌ partially | ✅ for CDN ones | ❌ | ❌ | ✅ | `fonts.googleapis.com` 180, `cdnjs` 90, `unpkg` 52, `jsdelivr` 45, `fonts.gstatic.com` 42 |
| 32 | Native libraries (6 × 2 ABIs) | ✅ `VERIFIED_BOTH` | ✅ shipped | ❌ | ❌ | ❌ | ✅ | none |

## 2. The concrete offline content gap — `VERIFIED_STATIC`

`SCHEMAS/SHIPPED_CONTENT_STATS.json → external_url_domains` (top 25):

| Host | refs | Kind |
|---|---:|---|
| `mimo.app` | 2,282 | lesson demo images (`/i/*.png`) |
| `mimo.org` | 365 | links |
| `www.w3.org` | 224 | SVG namespaces / links |
| `fonts.googleapis.com` | 180 | web fonts |
| `pokedex.mimo.dev` | 132 | exercise API |
| `example.com` | 124 | placeholder URL in teaching examples |
| `cdnjs.cloudflare.com` | 90 | JS libs |
| `swapi.mimo.dev` | 90 | exercise API |
| `things.mimo.dev` | 57 | exercise API |
| `rickandmortyapi.com` | 53 | exercise API |
| `unpkg.com` | 52 | JS libs |
| `localhost` | 49 | teaching examples |
| `cdn.jsdelivr.net` | 45 | JS libs |
| `fonts.gstatic.com` | 42 | font binaries |
| `airports.mimo.dev` | 39 | exercise API |
| `images.pexels.com` | 36 | photos |
| `api.example.com` | 31 | examples |
| `rickandmorty.mimo.dev` | 25 | exercise API |
| `tile.openstreetmap.org` | 22 | map tiles |
| `youtu.be` | 20 | video links |

Total **4,257** occurrences across ~60 hosts. These are **lesson payload
references**, not curriculum metadata. An offline clone must either mirror
them into `assets/` or substitute local equivalents; the JSON structure itself
needs no change.

## 3. Verdict (engineering, not speculation)

- **Offline-capable today, from the APK alone:** features 1–12, 23 (locally),
  32. That is the entire *learning loop*.
- **Replaceable with local logic/storage:** 13–20, 22, 27, 29–31. Requires
  implementing equivalents for a code runner, a local economy, and a local
  asset mirror — **no backend reconstruction**.
- **Genuinely not reproducible offline:** 21 (leaderboard needs other users),
  24 (auth), 25 (AI tutor model), 26 (payments/certificates). These can be
  omitted without breaking the learning loop.
- **Largest unknowns blocking a faithful offline clone:** unlock rule (#11),
  completion thresholds (#10), scoring formulas (#17–19), `validatedInput`
  index algorithm (#5), and the 4,257 external references (#30).

`VERIFIED_RUNTIME` offline proof (run `42002808217`, archived):
`svc wifi disable` + `svc data disable` → `Active default network: none` →
`am force-stop` + `am start` → `IntroSlidesActivity` (pid 6084) →
`Get started` → `Welcome to Mimo!` → motive → goal. The dumped UI hierarchies
`STEP-01/02/03.xml` and `OFFLINE-01/02/03.xml` are **byte-identical**
(`RUNTIME/OFFLINE_EQUALITY_PROOF.json`). Limitation: `ping` was already 100%
loss before isolation (ICMP blocked on emulator); the isolation proof is
`Active default network: none` + `connect: Network is unreachable`. Restore
commands did not bring the network back within the run — no reconnect claim.

`VERIFIED_RUNTIME` boundary: no lesson answer or completion screen was observed.
Therefore **no claim of runtime-verified offline lesson completion** is made.
`SERVER CONFIRMED = 0`.

**Evidence:** `CONTENT_MODEL.md`, `LOCAL_STORAGE_MODEL.md`, `LEARNING_ENGINE.md`,
`APPLICATION_STATE_MACHINE.md`, `NATIVE_LIBRARIES.md`,
`SCHEMAS/SHIPPED_CONTENT_STATS.json`, `ANALYSIS/MIMO_RETROFIT_ENDPOINTS.json`,
`ANALYSIS/MIMO_API_SURFACE.json`, `ANALYSIS/RUNTIME/MISSION_05/`.
