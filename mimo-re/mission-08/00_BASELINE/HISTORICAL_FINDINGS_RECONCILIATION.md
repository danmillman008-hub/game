# Mission 8 — Historical Findings Reconciliation

Every item below follows the same shape mandated by the brief:

1. **original claim** — quoted from the Mission-4…7 artefact (never edited),
2. **evidence that invalidates or refines it** — a file, a DEX offset, or a recomputation,
3. **both records** — the original stays in place; the correction lives here.

Nothing in `mission-04…07` was modified. Sizes and hashes of those trees are pinned in `WORKSPACE_INTEGRITY.json`.

---

## R-01 — Mission-7 open-question counts are not reproducible

**Original claim** (`MISSION_07_FINAL_REPORT.md`, status table): `CLOSED_STATIC 17`, `PARTIALLY_CLOSED 12`,
`BACKEND_ONLY 4`, `NOT_RECOVERED 3`, `GENUINELY_UNKNOWN 3`, `BLOCKED_BY_ENVIRONMENT 2`, total **41**.

**Evidence.** `18_CLOSURE/116_MASTER_OPEN_QUESTION_CLOSURE.csv` contains **39 data rows** and 39 distinct IDs.
Recomputed distribution: `CLOSED_STATIC 14`, `PARTIALLY_CLOSED 11`, `NOT_RECOVERED 7`, `GENUINELY_UNKNOWN 3`,
`BACKEND_ONLY 2`, `BLOCKED_BY_ENVIRONMENT 2` — sum 39.
Reproduce: `python tools/build_canonical_registers.py`.

**Verdict.** `CLOSED_STATIC`, `PARTIALLY_CLOSED`, `BACKEND_ONLY` and `NOT_RECOVERED` were all misreported; the
claimed total 41 cannot be obtained from any artefact in the tree. The closure *data* is internally consistent —
the defect is confined to the summary table.

**Both records.** Mission-7 report untouched. Correct figures: `CANONICAL_OPEN_QUESTION_REGISTER.json`.

---

## R-02 — Mission-7 says 41 domains; the audit contains 40

**Original claim:** "41 domains audited".

**Evidence.** `21_AUDIT/129_FINAL_DOMAIN_AUDIT.md` has **40** parseable domain rows
(24 fully / 9 substantially / 7 partially reconstructed).

**Refinement, not just a correction.** Mission-8 requires 45 domains. Five subsystems that mission-7 folded into
broader rows are separated because mission-8 investigates them explicitly:

| New domain | Was folded into |
|---|---|
| deep-links / URI routing | navigation |
| Compose UI layer | screens, Rive |
| auth token lifecycle | security posture |
| privacy/consent & tracking SDKs | SDKs |
| crash/observability | SDKs, security posture |

They enter the register as `NOT_INVESTIGATED`, never with a borrowed classification. Total: **45**.

---

## R-03 — The audit's `Runtime` column conflates two different things

**Original claim:** the domain table lists `Runtime: complete` for startup/DI, DSL, parser, rendering, lesson
runtime, grading, progression, Room, SSE, resources, background jobs, security…

**Evidence.** Every Mission-7 artefact states **0 runtime-verified findings**; the environment has no device, no
emulator, no ARM translation (`adb`, `emulator` absent). `Runtime: complete` therefore cannot mean execution.

**Diagnosis.** The column actually records *how much of the runtime logic was reconstructed statically*.

**Correction.** `CANONICAL_DOMAIN_REGISTER.json` stores the Mission-7 value verbatim in `static_claim_m7` and adds
`runtime_executed`, which is `NONE` for all 45 domains. Mission-8 does not reintroduce an aggregate "runtime %".

**Why it matters.** This is exactly the "inventoried ≠ understood" trap: a reader of the Mission-7 table could
legitimately conclude that the grading engine had been executed. It never was.

---

## R-04 — Mission-7 evidence references are not resolvable as written

**Original claim:** each closure row carries an `evidence` column such as `03_CONTENT_AND_MODULES/16`.

**Evidence.** `Path("mission-07/03_CONTENT_AND_MODULES/16").exists()` is `False` for **39/39** rows: the values are
extension-less stems of numbered files (`16_DYNAMIC_MODULE_ARCHITECTURE.md`).

**Correction.** `build_canonical_registers.py` resolves by stem: **39/39** now map to concrete files, recorded in
`evidence_files` per question. Mission-7 files were not edited; the resolution lives in the mission-8 register.

---

## R-05 — Q-121 "token storage mechanism": the hypothesis was wrong, and the answer is now recovered

**Original claim.** Q-121 (`token storage mechanism`) = `NOT_RECOVERED`; `07_STORAGE_AND_SYNC/54_TOKEN_LIFECYCLE.md`
recorded `ri.a` / `ri.c` as the classes that would have answered it, and noted that DAD emitted no source for them.

**Evidence that invalidates the hypothesis.** DEX inspection of the two classes
(`evidence/DEX_ri_network_callback.json`, reproducible with `tools/dex_inspect.py --class ri.a --class ri.c`):

* `ri.a` **extends `android.net.ConnectivityManager$NetworkCallback`**; its fields are a `LinkedHashSet` of
  networks plus a state-flow handle; `onAvailable` adds to the set and emits a `ri.c`, `onLost` removes and emits.
* `ri.c` is a value class `NetworkInfo(previousState, currentState)` over `com.getmimo.network.NetworkState`,
  with three predicates (`a()`, `b()`, `c()`), `equals`, `hashCode` and a `toString` that prints
  `NetworkInfo(previousState=…, currentState=…)`.

So `ri.*` is the **connectivity monitor**, not a credential store.

**Evidence that closes the question.** The request layer does not read a token store; it asks for a token:

`com.getmimo.data.source.remote.account.a.c()` builds `"Bearer ".concat(this.c.d(0))` — a field of type `ku.a`,
method `d(boolean)` (the decompiler printed `0` for the boolean literal). `ku.a` has **no** decompiled Java, so its
body was read from DEX (`evidence/DEX_ku.a_access_token_provider.json`, method `d(Z)Ljava/lang/String;`):

| Instruction (verbatim) | Meaning |
|---|---|
| `iget-object … Lku/a;->a Ljava/lang/Object;` then `check-cast … Lcom/google/firebase/auth/FirebaseAuth;` | token source is `FirebaseAuth`, not app storage |
| `iget-object … FirebaseAuth;->f Lcom/google/firebase/auth/FirebaseUser;`, `if-eqz` → `const-string "There is no Firebase user!"`, `invoke-static Lwc/f;->i`, `return-object v0` (null) | no signed-in user ⇒ returns null, logs |
| reads `…zzad;->b … zzz;->a Ljava/lang/String;` (cache key) and dispatches a `app.rive.c` Runnable through `zu.b.a().a.o.a` | schedules token revocation bookkeeping |
| `FirebaseAuth;->c(Lcom/google/firebase/auth/FirebaseUser; Z)Lcom/google/android/gms/tasks/Task;` with `Z=false` | `getAccessToken(false)` — cached token |
| `get-string "exp"`, `…vu/d;->b Ljava/util/Map;->get`, `DateTime()` seconds vs `exp` | client-side expiry test on the JWT claim |
| on expiry: `FirebaseAuth;->c(…, Z=true)`, then `…vu/d;->a Ljava/lang/String;` | forced refresh, then read the token |
| `const-string "Token doesn't exist!"` → `IllegalStateException`, caught → `new Lcom/getmimo/data/source/remote/authentication/AccessTokenUnavailableException;` | failure type used by every caller |

**Answer.** Tokens are **Firebase Authentication ID tokens**, obtained on demand through
`ku.a.d(boolean forceRefresh)`; there is **no application-owned token store**. Expiry is evaluated in the client
from the `exp` claim (Unix seconds) against `org.joda.time.DateTime`; an expired token triggers one forced
refresh; failure surfaces as `AccessTokenUnavailableException`, and the unsigned-in case returns `null`.

**Status transition.** `NOT_RECOVERED` → **`CLOSED_STATIC`** (mechanism), with a residual explicitly out of scope:
the persistence format *inside* the Firebase SDK is library behaviour, not app behaviour. Formal transition record
in `12_OPEN_QUESTION_CLOSURE/` (Phase 12).

**Both records.** Mission-7's `54_TOKEN_LIFECYCLE.md` is unchanged and still says `NOT_RECOVERED`.

---

## R-06 — Duplicate `Q-27` exists only in prose

Mission-7's final response listed `Q-27` twice. The CSV holds `Q-27` exactly once
(`PARTIALLY_CLOSED`, chapter ordering). Reporting defect only; the register is sound. No fix applied to Mission-7.

---

## R-07 — "2,178 classes deeply investigated" overstates reachability

**Original framing:** the 2,178-row queue is called the deep-investigation set.

**Evidence.** 1,059 of those rows (**48.6 %**) have no `.java` in the decompiled tree; the queue's own
`decompiled` column agrees exactly (1,119 / 1,059), so Mission-7 counted correctly but never stated the
consequence: for half the queue, no body is readable by the decompiler path.

**Mitigation.** `tools/dex_inspect.py` reads the instruction stream directly, and mission-8 marks, per class,
whether a claim rests on `decompiled_java` or on `dex_instructions`.

---

## R-08 — Mission-7 test path

The suite is `mission-07/20_TESTS/test_mission07_semantics.py`; earlier notes (including this session's log) said
`19_TESTS`, which is the tooling directory. All four inherited suites re-run green — see
`REGRESSION_TEST_RESULTS.md`.

---

## R-09 — "59 `.riv` assets, zero bindings recovered" needs splitting

**Original claim:** 59 `.riv` assets, no bindings recovered.

**Refinement.** There *is* a generic consumer path, and it is not asset-specific:

* `com.getmimo.ui.content.ImageContent$Rive` is a `Parcelable` content node whose fields are
  `(int resourceId, String ?, Float ?, String ?, Map ?)` — an asset id plus a name plus an input map, i.e. the
  state-machine inputs are modelled as data (`evidence/DEX_rive_webview.json`).
* `com.getmimo.ui.compose.animation.rive.RiveAnimationProperties` is a `Parcelable` carrying
  `autoplay`, `Fit`, `Alignment`, `Loop`.
* The composable itself (`RiveAnimationKt`) is **absent from the dex set** — only its lambdas
  (`RiveAnimationKt$RiveAnimation$6$1`, `…$bytes$1`) are present — so the rendering call sequence is
  `NOT_RECOVERED` for a structural reason, not a decompiler reason.

So: no *per-asset* binding is recovered, but a *generic* Rive content model and property object are. The statement
"zero bindings" is replaced by two precise statements (generic consumer: recovered; per-asset binding and
composable body: not recovered).

---

## R-10 — Region previously marked thin but actually recoverable: the lesson WebView bridge

Not a correction of a wrong claim, but a scope correction. Mission-7 graded interactive/executable lessons
"substantial". The bridge is concretely recoverable and was not yet documented:

* `com.getmimo.ui.lesson.interactive.webview.a extends android.webkit.WebView`; its constructor installs
  `addJavascriptInterface` and registers a JS asset named `lesson-webview.js`; the HTML template carries the
  placeholders `__MIMO_DOCUMENT_ID__` and `__MIMO_TOUCH_SLOP_CSS_PX__`; the bridge injects
  `window.dispatchEvent(new CustomEvent('mimo-visibility', { detail: … }))`; inbound messages are JSON with keys
  `documentID`, `kind`, `gesture`, `decision` (parsed with `org.json.JSONObject`).
* `com.getmimo.ui.components.common.MimoWebView` loads local HTML through
  `loadDataWithBaseURL(baseUrl, html, "text/html; charset=UTF-8", …)`.

Reference: `evidence/DEX_rive_webview.json`. Full treatment belongs to Phase 3 (executable lessons) and Phase 4
(UI/resource consumers).

---

## C-12 — Q-05 refined: eight locale content modules exist as feature modules with stub-only presence

**Original claim (Mission 7, Q-05).** "dynamic feature module contents (non-English packs) absent from the APK" —
status `BLOCKED_BY_ENVIRONMENT`.

**New evidence (mission-08 checkpoint pass).** Eight of the twelve dex files are 1,096-byte stubs that contain
exactly two classes each: `com.getmimo.data.content.<locale>.BuildConfig` and `…R`, for **ru, pt, id, it, pl, fr,
tr, es**. The substantive code is confined to `classes.dex` (12,944 classes), `classes2.dex` (13,155),
`classes3.dex` (3,318) and `classes12.dex` (21 `bin.ghost` classes).

**What changes.** The *existence and names* of the modules is now proven (`VERIFIED_STATIC`), and so is the fact
that their payloads are not in the base APK. The **contents** remain absent, so Q-05 stays
`BLOCKED_BY_ENVIRONMENT` — the blocker is now precise: the module payloads are delivered by Play Feature Delivery
and are not present in the supplied artifact.

**Both records.** Mission-7's `03_CONTENT_AND_MODULES/16_DYNAMIC_MODULE_ARCHITECTURE.md` is unchanged.

## R-11 — A mission-08 statement that was wrong and is corrected here

**Original claim (mission-08, Phase 2 data flow):** "header construction is inside the request builders" — i.e. the
app attaches `Authorization` per request and has no central mechanism.

**Evidence that invalidates it.** `fh.a` implements `okhttp3.Interceptor` and, when a request carries no
`Authorization` header *and* its Retrofit method is annotated with `ri.b`, adds
`"Authorization: Bearer " + ku.a.d(false)` (`05_AUTHENTICATION_CLOSURE/02_INTERCEPTOR_CHAIN.md`,
`05_AUTHENTICATION_CLOSURE/evidence/DEX_auth_interceptors_and_repository.json`). The manual `"Bearer "` sites are
the *exception* (streaming, certificate download, Pusher auth, WebSocket handshake), not the rule.

**Both records.** `02_METHOD_RELATIONSHIPS/05_DATA_FLOW.md` (DF-01) now states the correct three-consumer model and
keeps an explicit correction note. This entry exists because a mission that corrects history must also be able to
correct itself.

**By-product.** The same evidence refines R-05: the `ri.*` family is `ri.b` = authorization annotation,
`ri.d` = network-state interface, `ri.a` = platform callback, `ri.c` = state value.

## C-13 — "non-English content packs absent" is wrong as stated

**Original finding (mission-07, Q-05):** the APK's non-English content lives in dynamic feature modules that are
absent from the supplied APK, so non-English behaviour is `BLOCKED_BY_ENVIRONMENT`.

**What the APK actually contains (measured, Stage 2):**

| Locale | module dex | classes in base APK | lesson assets in base APK |
|---|---|---|---|
| ru, pt, id, it, pl, fr, tr, es | `classes4`–`classes11` (1,096 B each) | `…content.<locale>.BuildConfig`, `…R` only | present: `assets/lessons-<locale>` with 1,030–1,032 JSON |
| en | base | base | present (1,030) |

`assets/` holds **10,317** JSON documents across ten locale directories, each with
`tutorial-<id>.json` files and a `tracks.json` carrying `publishSetVersion: 753` and 19 tracks. The bundle is read by
`ye.b` (base path `lessons-<locale>/tracks`) through `ye.f`.

**Why the earlier statement was wrong.** It conflated *module code* with *module content*. Only the code is stubbed;
the content is shipped as assets in the base APK. The 1,096-byte dex files prove the module structure, not the
absence of the content.

**Effect on Q-05.** Q-05 is restated: *what the eight locale modules would have contributed in code is absent; their
content is present and readable.* The question's status changes from a content-absence blocker to a code-absence
limitation: non-English **content** is now `VERIFIED_STATIC`, while locale-specific **code** paths remain unread
(nothing in those stubs but `R`/`BuildConfig`).

**Preserved:** the original Q-05 text and the mission-07 evidence remain in the mission-07 directories, untouched.

## Summary of corrections carried into mission-8

| ID | Kind | Effect on mission-8 |
|---|---|---|
| R-01 | count defect | canonical register is the only source of question counts |
| R-02 | count defect + scope | 45-domain register; 5 rows start at NOT_INVESTIGATED |
| R-03 | semantic defect | no domain may ever claim runtime execution again |
| R-04 | evidence defect | all references resolve to files |
| R-05 | substantive | Q-121 closed statically; `ri.*` reclassified; token path documented |
| R-06 | prose defect | none |
| R-07 | coverage defect | per-class source basis (java vs DEX) is now recorded |
| R-08 | documentation | correct suite path |
| R-09 | refinement | Rive: generic consumer vs per-asset binding vs missing composable |
| R-10 | scope | WebView bridge enters Phase 3/4 with evidence |
| R-11 | self-correction | central auth interceptor `fh.a` exists; `ri.*` family fully mapped |
| C-13 | substantive | locale content **is** present as assets; only the module code is stubbed; Q-05 restated |
