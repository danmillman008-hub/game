# 17 — Security boundaries and data handling

Scope note: this section reports **observable properties of the artefact**. No attempt was made
to bypass authentication, DRM, paywalls or server controls; no credential values are reproduced.

## 1. Build and signing

| Property | Value | Consequence |
|---|---|---|
| Signing certificate | self-signed, CN `youarefinished`, valid 2021-11-20 → 2046-11-14 | Not Play App Signing ⇒ distribution via own channels/sideload; the signing identity is an in-house joke name shared across builds |
| `android:debuggable` | absent | no adb debugging in release |
| `allowBackup` | `false` | app data excluded from ADB/cloud backup |
| `targetSdk` | 36 | runtime permissions, cleartext blocked by default |
| `networkSecurityConfig` | absent | platform defaults apply: no cleartext, system CAs only |
| Obfuscation | Smob v4.6 + R8 repackaging | class names mostly gone, **string literals fully readable** |

The last row is the security-relevant one: 105,611 literals survive verbatim, including the AI
tutor system prompts, the endpoint catalogue, the analytics schema and the developer-menu
labels. Obfuscation here protects control flow, not intent.

## 2. Transport

* Hosts: `api.mimo.org` (prod), `api-testing.mimo.org` (test), `mimoauth.getmimo.com`,
  `images.getmimo.com` (V).
* The presence of a **testing host inside the release APK** is a real exposure: the base URL is
  switchable (dev menu / build config, I).
* Certificate pinning: `CertificatePinner` classes exist because OkHttp is bundled; **no pin
  configuration strings or annotations are observable** ⇒ pinning is **UNKNOWN**, and the
  default assumption must be "system trust store only".
* No public-key/asset signature verification is observable for downloaded content packs (the
  live-preview download unzips a package and renders it) ⇒ **content integrity rests on TLS
  alone** (I).

## 3. Authentication and identity

* Own auth endpoints (`/auth/login`, `/auth/token`, `/auth/revoke`) plus Firebase Auth social
  providers (`GenericIdpActivity`, `RecaptchaActivity`, Facebook `CustomTabActivity`) (V).
* Tokens: no `EncryptedSharedPreferences` / `security-crypto` strings, no Keystore literals
  observed ⇒ **token storage is plaintext app-private storage** (V negative finding).
* Deferred account creation exists (`signup_prompt_headline_continue_learning`,
  `delayed_account_creation_offline_error`) ⇒ anonymous sessions are a first-class state.
* Account deletion endpoint exists (`/v1/account`) but the UI path was not identified (U).

## 4. Local data at rest

| Data | Storage | Protection |
|---|---|---|
| Progress (3 tables) | Room/SQLite, plaintext | none |
| Profile/settings cache | SharedPreferences, plaintext | none |
| Code autosave | local buffers + `/savefiles` | none |
| Content | read-only assets | APK signature |
| AI tutor conversation | server-side only | n/a |

No SQLCipher, no encrypted prefs, no app-level PIN. For a learning app with no financial data
this is a defensible trade — but `allowBackup=false` plus plaintext means a rooted device can read
everything, including any cached personal data.

## 5. WebView surface (the sharpest edge)

| Element | Evidence | Risk |
|---|---|---|
| JS bridge into lesson webview | `addJavascriptInterface` (1 literal), `removeJavascriptInterface`, `Landroid/webkit/JavascriptInterface;` | Bridge exposure — `bootstrapScript` in `<database>`/`<webview>` modules runs authored JS |
| File access configuration | `setAllowFileAccess`, `setAllowFileAccessFromFileURLs` | If enabled for `file://` lesson assets, a content-level injection could read local files |
| Lesson web assets | `assets/lesson-webview.js`, `highlight.min.js`, `styles/`, `beautify/`, `prettier/`, `snippets/` | trusted, shipped |
| Remote content path | live-preview unzip → rendered in webview | **unpublished content executes with the bridge available** (I) |
| URL interception | `shouldOverrideUrlLoading` present | links inside lessons are intercepted (good) |

Assessment: the WebView bridge plus a content channel that can deliver unpublished markup is the
combination a security reviewer would flag first. There is no evidence of exploitation or of a
missing control beyond TLS; but a compromised network or a malicious insider authoring a lesson
would be executing inside a WebView with a JavaScript interface present.

## 6. Client-side trust decisions

| Decision made on device | Consequence |
|---|---|
| Interactive lesson correctness (answers derived from markup) | trivially "cheatable" by reading the lesson | 
| See-solution usage (`seeSolutionWasUsed`) | self-reported, affects internal analytics only |
| Feature gates from remote config (incl. `isPro` display states) | cosmetic; server re-checks entitlements (I) |
| Dev-menu overrides | local only |
| Puzzle: no Play Integrity / SafetyNet literals | no attestation ⇒ server cannot distinguish a stock client from a modified one (V negative) |

`IntegrityManager` strings appear 11 times but could not be attributed to a Mimo flow without
bytecode-level analysis; they are therefore **UNKNOWN**, not counted as an integrity feature.

## 7. Privacy and telemetry breadth

| Collector | Data implied by literals |
|---|---|
| Mixpanel (own `/v1/events` too) | 305 typed properties including track/tutorial/lesson/experiment ids, paywall source, AI-tutor prompt type |
| Adjust (315 classes) | install attribution, `marketing_campaign`, `ff_*` device-id switches, ad-id permissions |
| Customer.io (351 classes) | identity + email, in-app messaging tokens |
| Firebase | Auth identities, device tokens, Remote Config assignment, A/B ids |
| RevenueCat | subscriber ids, entitlements, receipts (incl. Amazon receipt path) |
| Own backend | device tokens, visits, activity, saved code, avatar |

This is a normal growth stack for a consumer subscription app, and a **compliance problem** for a
Persian product: an Iranian build cannot ship Adjust/Facebook attribution, and should not send
identifiers to US-based processors. All of it is replaceable with a self-hosted collector.

## 8. Production hygiene findings (summary)

1. Developer Menu (55 classes) ships in release.
2. `androidx.compose.ui.tooling.PreviewActivity` exported in release.
3. Testing API host in release binary.
4. Live content download + WebView bridge + no asset signing.
5. Plaintext token storage; no attestation.
6. Self-signed long-lived certificate.
7. Answer keys for interactive lessons are client-side (by design).

None of these is a remote-exploit chain; together they describe a company that optimises for
iteration speed over hardening — which is exactly the trade a young consumer app makes.

## 9. Konkur implications

| Area | Requirement |
|---|---|
| Exam integrity | Question keys must be **server-side** for high-stakes exams, or signed per pack; never derived from client markup |
| Offline simulation | Client-side scoring is unavoidable offline ⇒ sign the exam bundle and submit a hash of results for verification |
| Iranian network | No US analytics/attribution SDKs; self-hosted events; certificate pinning to your own CA/host set |
| Device sharing | Do not cache identity tokens in plaintext; support account switch without data leakage |
| Distribution | Iranian stores (Bazaar/Myket) re-sign APKs — assume the certificate is not under your control |
| Content pipeline | Signed packs + staged review; a wrong key is a trust incident, not a bug |
| Attestation | Consider Play Integrity only if you ship outside Iran; otherwise rely on server-side checks and rate limits |
