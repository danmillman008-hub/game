# Phase 5.3 — Authentication flows and providers

The renamed repository is `com.getmimo.data.source.remote.authentication.a`, reconstructed as
**`AuthenticationFirebaseRepository`** from the binary names of its own lambdas (see `05_METHOD_NAME_RECOVERY.md`).
Its constructor takes `(Context, com.getmimo.analytics.a, hg.a, ri.d, pe.a, …)` and contains the literal
**`mimo-auth-production`**.

## 1. Method map (evidence-graded)

| Original name (from lambda binary name) | Renamed method | Instructions | Confidence | Evidence |
|---|---|---|---|---|
| `fetchAbTestUserGroups` | `a.c(...)` | 77 | HIGH | lambda `…$fetchAbTestUserGroups$1` invokes only `a.c` |
| `fetchAbTestUserGroupsIfSignup` | `a.d(...)` | 72 | HIGH | lambda `…$fetchAbTestUserGroupsIfSignup$1` → `a.d` |
| `linkCredentialWithAnonymousAccount` | `a.i(AuthCredential, …)` | 181 | HIGH | lambda `…$linkCredentialWithAnonymousAccount$1` → `a.i` |
| `postVisitSafely` | `a.k(...)` | 84 | HIGH | lambda `…$postVisitSafely$1` → `a.k` |
| `signInWithCredential` | `a.l(AuthCredential, …)` | 117 | HIGH | lambda `…$signInWithCredential$1` → `a.l` |
| `anonymousAuthentication` | `a.k` or `a.c` | — | MEDIUM | lambda calls both |
| `createUserWithEmailAndPassword` | `a.i`, `a.k`, `a.c` | — | MEDIUM | several candidate sites |
| `signInWithEmail` | `a.m`, `a.l`, `a.k` | — | MEDIUM | overloads not separated |
| `signInWithFacebook` | `a.i`, `a.l`, `a.k` | — | MEDIUM | delegation to `signInWithCredential` |
| `signInWithGoogle` | `a.i`, `a.l`, `a.k` | — | MEDIUM | delegation to `signInWithCredential` |
| `GoogleSignIn.signIn` (renamed `…authentication.b`) | `b.a` | — | HIGH | lambda `GoogleSignIn$signIn$…` → `b.a` |
| `getProfile`, `getUsername`, `postVisit`, `init` | not mapped to a single method | — | — | see §4 |

The MEDIUM rows are **not** guessed: each candidate is a method the lambda actually invokes. What is missing is the
overload disambiguation, which requires reading each candidate's own body — deferred, and declared as such.

## 2. Flows that are reconstructed

### F-A Anonymous-first onboarding

`anonymousAuthentication` exists as a distinct operation, and `linkCredentialWithAnonymousAccount` upgrades an
anonymous user with a real credential. The latter's body contains

* `"Linking credential was successful but current user is null!"`,
* `"There is no firebase user when merging anonymous account wit…"`,

proving the app deliberately supports **anonymous accounts that later become permanent** — a state transition no
mission-07 artefact recorded.

### F-B Credential sign-in

`signInWithCredential` (181-instruction sibling `linkCredential…`, 117 for sign-in) contains
`"Login was success but current user is null!"`.

### F-C Google sign-in wrapper

`…authentication.b` = `GoogleSignIn`; `signIn` maps to `b.a` (HIGH). Its sibling `…authentication.a` also carries
`"Unexpected type of credential"` and the literal
`"com.google.android.libraries.identity.googleid.TYPE_GOOGLE_ID_TOKEN_CREDENTIAL"` — i.e. **Credential Manager**
(Google ID token) rather than the legacy `GoogleSignInClient`, plus Facebook via
`AuthenticationViewModel$firebaseAuthWithFacebook$1`.

### F-D Post-visit bookkeeping

`postVisitSafely` (`a.k`) logs `"postVisit request failed"` on failure — a fire-and-forget call, consistent with the
"safely" suffix. `PostVisitWorker` (a WorkManager worker in the same package) exists for the deferred case.

### F-E A/B user-group fetch

`fetchAbTestUserGroups` (`a.c`) and `fetchAbTestUserGroupsIfSignup` (`a.d`) are suspend functions called after
authentication; they talk to the backend through `hg.a` (`a(AppName, …)`, `e(String, …)` arms seen in the interface).

## 3. Analytics coupling

`AuthenticationLocation` (10+ variants: `Activity`, `AfterPurchase`, `BeforeOpenChapter`, `ChapterEnd`,
`LeaderBoards`, `Onboarding`, `Practice`, `Profile`, `Settings`, …), `AuthenticationMethod` (`EmailLogin`,
`EmailSignup`, …), `LoginProperty`, `SignupSource` are typed enums in `com.getmimo.analytics.properties`.
They prove **when** the auth screen can be shown and **how** login happened; they do not prove which events were
emitted (no dispatch site was traced in this phase).

## 4. What is genuinely not recovered

| Gap | Reason |
|---|---|
| e-mail/password UI wiring | `AuthenticationFragment` and `AuthenticationViewModel` are not `class_def`s (renamed); only their lambdas exist |
| `getProfile` / `getUsername` mapping | their lambdas invoke several methods across the repository and the cache layer; no single receiver |
| which provider buttons exist in the UI | the fragment is absent; only `configureButtons$2/3/4/5` lambdas survive, and their configuration is applied to a renamed view |
| `mimo-auth-production` semantics | it is a string constant in the constructor; whether it is a tenant id, an emulator project or a preference key is **not** proven by its presence |
| token refresh during an in-flight request | interceptor ordering not established (`02_INTERCEPTOR_CHAIN.md` §4) |

## 5. Evidence

`05_AUTHENTICATION_CLOSURE/evidence/METHOD_NAME_RECOVERY.json`,
`evidence/DEX_auth_interceptors_and_repository.json`,
`evidence/SCAN_TOKEN_LITERALS.json`,
`evidence/SCAN_METHODS_TOKEN.json`.
