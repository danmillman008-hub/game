# Phase 1.4 — Deep class investigation (worked records)

Each record answers the same 23 points. Points that could not be answered are marked
`NOT_RECOVERED` or `UNKNOWN` — never left blank, never filled from the class name.

## The 23 points

| # | Point | # | Point |
|---|---|---|---|
| 1 | identity (name, dex file) | 13 | persistence touched |
| 2 | source basis (`java`, `dex`, both) | 14 | network touched |
| 3 | superclass | 15 | threading / async model |
| 4 | interfaces | 16 | error paths and failure types |
| 5 | fields (type + role) | 17 | string literals that name behaviour |
| 6 | method inventory (count, kinds) | 18 | DI role (who constructs it) |
| 7 | constructor semantics | 19 | lifecycle / entry points |
| 8 | public entry points | 20 | cross-domain effects |
| 9 | responsibility statement (one sentence) | 21 | evidence references |
| 10 | collaborators (callees) | 22 | method-status bucket |
| 11 | callers (static, with invoke kind) | 23 | remaining unknowns |
| 12 | state owned | | |

Evidence files for every record are under `evidence/`; raw instruction dumps are in the mission-08
`evidence/` directory and are reproducible with `tools/dex_inspect.py`.

---

## C-01 `ku.a` — the access-token provider (the answer to Q-121)

1. **Identity** `ku.a`, `classes2.dex`, 22 methods, 0 fields declared besides `a: Object`.
2. **Source basis** `dex_only` — DAD emits no file for this class.
3. **Superclass** `java.lang.Object`; interfaces `ku.b, o.k, z00.b, tt.c, zo.n` (mixed, see §C-01a).
4. **Fields** `a: Ljava/lang/Object;` — cast to `Lcom/google/firebase/auth/FirebaseAuth;` inside `d`.
5. **Constructor semantics** several tagged constructors (`(B)V`, `(Ljava/lang/Object;)V`,
   `(Ljava/lang/String; Landroid/os/Bundle;)V`, `(Lu3/c;)V`, `(Lw90/i; Ljava/lang/Iterable;)V`). The `(B)V`
   constructor switches on the tag byte (cases 13, 17 in the decompiled text) and initialises unrelated state.
6. **Methods** `d(Z)Ljava/lang/String;` (83 insns, the token provider), `i()Z`, `m()Lorg/json/JSONObject;`,
   `n(Lorg/xmlpull/v1/XmlPullParser;)Ljava/util/ArrayList;`, `e(...)`/`k(...)` (Coil image loaders),
   `a(CustomerInfo)V`, `b(PurchasesError)V` (RevenueCat), `c`/`h` (package-manager lookups).
7. **Entry point of interest** `public String d(boolean forceRefresh)`.
8. **Responsibility** *returns the current Firebase ID token, refreshing it at most once when the JWT `exp`
   claim is already in the past; throws `AccessTokenUnavailableException` when no token can be produced.*
9. **Collaborators** `FirebaseAuth` (`getCurrentUser`, `c(FirebaseUser, Z)`), `FirebaseUser`/`zzad`,
   `GetTokenResult` (`vu.d`), `org.joda.time.DateTime`, `Tasks.await`, `zu.b` (Firebase app accessor + executor),
   `com.getmimo.data.source.remote.authentication.AccessTokenUnavailableException`, logging via `wc.f.i`.
10. **Callers (static)** `com.getmimo.data.source.remote.account.a.c()` (`invoke-virtual ku.a->d`,
   0-arg = `false`), plus the other request builders that build `"Bearer "` strings
    (`RemoteCertificateRepository$downloadCertificate$2`, `PusherConnectionManager$initializePusher$1`,
    `AiTutorRepository$sendMessage$2`, `AccountRepository$deleteAccount$2`).
11. **State owned** none of its own beyond the `FirebaseAuth` handle; the credential state lives in Firebase.
12. **Persistence touched** none directly — persistence is Firebase SDK internal (out of app scope).
13. **Network touched** indirectly: token refresh is a Firebase network call.
14. **Async model** blocking: `Tasks.await(...)` inside a coroutine-bound call chain; the caller supplies `d70.b`
    (Continuation) one frame above.
15. **Error paths** no user → `const-string "There is no Firebase user!"`, `return-object v0` (null);
    null token → `IllegalStateException("Token doesn't exist!")`; any exception → `AccessTokenUnavailableException`.
16. **Strings** `"exp"`, `"There is no Firebase user!"`, `"Token doesn't exist!"`.
17. **DI role** injected as a singleton into request-layer classes (field type `ku.a`).
18. **Cross-domain effects** every authenticated request (network, certificate download, Pusher auth, AI tutor,
    account deletion) depends on this method.
19. **Evidence** `evidence/DEX_ku.a_access_token_provider.json`.
20. **Status** `BEHAVIOUR_RECONSTRUCTED` (not `RUNTIME_TESTED`: nothing was executed).
21. **Unknowns** the exact refresh skew (there is no explicit clock-skew constant — the comparison is
    `exp < now_in_seconds`, with no margin); Firebase's own token cache policy.

**C-01a — merged-class caveat.** `ku.a` also contains RevenueCat, Facebook and Coil methods that have nothing to
do with tokens. The obfuscation applied to this build merges several original classes into one `class_def`,
discriminated by a tag byte in the constructor. Attribution must therefore always be *per method*, not per class.
See `09_MERGED_CLASS_AND_STRUCTURAL_CAVEATS.md`.

---

## C-02 `ri.a` / `ri.c` — the connectivity monitor (refutes the token-store hypothesis)

| Point | `ri.a` | `ri.c` |
|---|---|---|
| 1 identity | `ri.a`, `classes2.dex`, 3 fields, 4 methods | `ri.c`, 2 fields |
| 2 source basis | dex_only | dex_only |
| 3 superclass | **`android.net.ConnectivityManager$NetworkCallback`** | `java.lang.Object` |
| 4 interfaces | — | — |
| 5 fields | `LinkedHashSet` of networks + flow handle (`ta0.j`) + ref holder | `NetworkState previous`, `NetworkState current` |
| 6 methods | `<init>(Ref$ObjectRef, ta0/k)`, `<init>(ta0/k)`, `onAvailable(Network)`, `onLost(Network)` | `<init>(NetworkState, NetworkState)`, `a()Z`, `b()Z`, `c()Z`, `equals`, `hashCode`, `toString` |
| 9 responsibility | tracks the set of available networks and emits a `ri.c` on every change | immutable before/after pair with three predicates and a `NetworkInfo(previousState=…, currentState=…)` rendering |
| 10 collaborators | `ta0.j.k(...)` (flow emitter), `ri.c` | `com.getmimo.network.NetworkState` |
| 11 callers | Android framework (registered callback) — no static caller by design | constructed inside `ri.a` only |
| 16 error paths | none observed (callback body has no try/catch) | none |
| 20 cross-domain | connectivity state consumed by `com.getmimo.network.*` consumers | same |
| 21 evidence | `evidence/DEX_ri_network_callback.json` | same |
| 22 status | `onAvailable`/`onLost` = `BEHAVIOUR_RECONSTRUCTED` | `toString` = `BEHAVIOUR_RECONSTRUCTED`, `a/b/c` = `DEX_INSPECTED` |
| 23 unknowns | whether `a()`/`b()`/`c()` map to connected/connecting/disconnected — the enum constant mapping is in `NetworkState`, not in `ri.c` | same |

**Correction of record:** Mission-7 stored `ri.a`/`ri.c` as the classes that would answer "token storage"
(Q-121). They answer a different question. `07_STORAGE_AND_SYNC/54_TOKEN_LIFECYCLE.md` remains unchanged.

---

## C-03 `com.getmimo.data.source.remote.account.a` — the account data source

1. **Identity** `…account.a`, `classes.dex`, 5 fields, 4 methods; decompiled Java available.
2. **Fields** `Context`, `hg.a` (service interface), **`ku.a` (token provider)**, `np.d` (account repository
   interface, implemented by `np.b`), `jx.d` (Gson).
3. **Methods** `a(String, Continuation)` → change e-mail; `b(Continuation)` → delete account;
   `c()` → enqueue a deferrable delete.
4. **`c()` behaviour** `"Bearer ".concat(this.c.d(0))` → put `ARGS_ACCESS_TOKEN` into `Data` →
   build a `OneTimeWorkRequest` with `NetworkType.CONNECTED` → `WorkManager.enqueue`.
   i.e. when the network call fails the deletion is deferred as a WorkManager job carrying the *access token*
   as an argument.
5. **Async model** `ra0.z.z(flow, suspendLambda, continuation)` — flow-based, not blocking.
6. **Evidence** `/tmp/dad/com.getmimo.data.source.remote.account.a.java:45` (the `Bearer` line),
   `mission-08/evidence/DEX_*.json` for the interface facts.
7. **Status** `c()` = `BEHAVIOUR_RECONSTRUCTED`; `a`/`b` = `JAVA_INSPECTED`.
8. **Security note (no values recorded)** the token is placed in WorkManager input data, which is persisted by
   WorkManager on disk. This is a *design observation about the client*, not a credential disclosure; no token
   value is read, stored or printed anywhere in mission-08.
9. **Unknowns** whether `AccountDeleteWork` clears the input data after use (its `doWork` body was not read in
   this phase).

---

## C-04 `com.getmimo.ui.lesson.interactive.webview.a` — the executable-lesson WebView bridge

1. **Identity** `…lesson.interactive.webview.a extends android.webkit.WebView`; 252-instruction constructor.
2. **Evidence of a real bridge** (all from `evidence/DEX_rive_webview.json`):
   * `addJavascriptInterface` in the constructor,
   * an asset named `lesson-webview.js`,
   * HTML template placeholders `__MIMO_DOCUMENT_ID__`, `__MIMO_TOUCH_SLOP_CSS_PX__`, `<!DOCTYPE html>`,
   * injected event `window.dispatchEvent(new CustomEvent('mimo-visibility', { detail: … }))`,
   * inbound JSON keys `documentID`, `kind`, `gesture`, `decision`,
   * a `Regex("^\\s*<!doctype[^>]*>")` used to classify/normalise incoming HTML,
   * `UUID.randomUUID().toString()` as a per-document id,
   * a `dispatchToWeb(Landroid/view/MotionEvent;)Z` method exposed to JavaScript.
3. **Responsibility** hosts a self-contained HTML lesson document, injects identifiers, forwards touch events
   into the page, and receives structured gesture/decision messages back into Kotlin.
4. **Cross-domain** this is the *only* recovered path by which executable lesson content can influence grading
   decisions; it also feeds analytics (`kind`, `decision`).
5. **Status** `b()` = `BEHAVIOUR_RECONSTRUCTED`; `c()`, `d()`, `a()`, `<init>` = `DEX_INSPECTED`.
6. **Unknowns** the exact JSON schema of each message kind (only the four key names are proven), the JS API
   surface in `lesson-webview.js` (asset not decoded in this phase).

---

## C-05 `com.getmimo.ui.components.common.MimoWebView`

`extends android.webkit.WebView`; field set includes three `Function0` callbacks and a lifecycle owner.
`a(String)` loads content through `loadDataWithBaseURL(baseUrl, html, "text/html; charset=UTF-8", …)`.
Two other methods receive `ConsoleMessage` and `WebResourceRequest` — a console hook and a resource
interceptor. No `addJavascriptInterface` here (that lives in C-04). Status: `a(String)` =
`BEHAVIOUR_RECONSTRUCTED`, rest `DEX_INSPECTED`.

---

## C-06 `com.getmimo.data.notification.MimoFirebaseMessagingService`

* Superclass `Ljf/b;` = the renamed **`FirebaseMessagingService`** (proved by the overridden signatures).
* `d(Lcom/google/firebase/messaging/RemoteMessage;)V`, 270 instructions, strings `"Notification received."`,
  `"Handle push notification"`, `"title"`, `"body"`, `"crashKeysHelper"` → the FCM receive path.
* `e(Ljava/lang/String;)V`, 25 instructions, string `"Refreshed token: "` → the FCM token-refresh callback.
* Status: both `BEHAVIOUR_RECONSTRUCTED`.
* Unknowns: which notification channels are created and which deep-link actions are attached (the string set
  read here does not contain channel ids).

---

## C-07 `com.getmimo.ui.authentication.*` — a **negative** result that matters

* `AuthenticationActivity extends bl.b` exists: `onCreate` reads an `AUTHENTICATION_TYPE` extra;
  `onBackPressed` contains `"Trying doing previous step on an other step"`; a method `z()` returns
  `com.getmimo.ui.authentication.t`.
* `AuthenticationFragment` and `AuthenticationViewModel` are **absent from the dex set**; only their lambdas
  (`AuthenticationFragment$configureButtons$2/3/4`, `AuthenticationViewModel$firebaseAuthWithFacebook$1`)
  survive. Their provider implementations were renamed.
* Consequence: the *button-to-provider wiring* (Google / Facebook / Apple / e-mail) cannot be reconstructed
  from the fragment; it must be reconstructed from the renamed classes that the lambdas call into, plus
  the analytics enums `AuthenticationMethod` (`EmailLogin`, `EmailSignup`, …) and `AuthenticationLocation`.
* Status: `AuthenticationActivity.onCreate` = `DEX_INSPECTED`; the fragment/viewmodel = `NOT_RECOVERED`
  (structural, see C-01a and `09_…CAVEATS.md`).

---

## C-08 `f9.j` — an example of the merged-class pattern

* 64 methods, interfaces `fa.d` (with `a()Z`, `shutdown()`) and `com.google.android.gms.tasks.OnCompleteListener`.
* One constructor `(B)V` switches on the tag; branch 13 assigns two shared empty-list singletons, branch 17
  creates two `ConcurrentHashMap`s and registers a list of constants (`m50.g.d … m50.i.b`).
* Meaning: `f9.j` is **several unrelated original classes** fused into one `class_def`. Any statement of the form
  "class `f9.j` does X" is meaningless; only "method `f9.j.<init>(B)` branch 17 does X" is meaningful.
* Status: `<init>` = `DEX_INSPECTED`; the rest `BODY_PRESENT_NOT_READ`.

---

## What these records establish for later phases

| Established | Used by |
|---|---|
| tokens are Firebase ID tokens, no app token store (Q-121) | Phase 5, Phase 12 |
| account deletion is deferred through WorkManager with the token in the input data | Phase 3 (persistence), Phase 8 |
| connectivity is a callback + flow, unrelated to auth | Phase 8 |
| executable lessons talk to Kotlin over a WebView JS bridge with four message keys | Phase 3, Phase 11 |
| FCM receive and token-refresh callbacks are recovered | Phase 6, Phase 7 |
| the auth UI fragment/viewmodel are structurally absent | Phase 5, Phase 10 (excluded-class justification) |
| class-per-responsibility is invalid for merged classes | Phase 1.9, Phase 10 |
