# Mission 7 — External SDKs (complete)

| SDK | Version evidence | Purpose | Client integration |
|---|---|---|---|
| Firebase Analytics | classes | product analytics | via `com.getmimo.analytics.a` |
| Firebase Remote Config | classes + defaults xml | AB-test groups, 3 flags | analytics init |
| Firebase Messaging | classes + manifest | push token + notifications | analytics init |
| Firebase Installations / app-instance-id | log string | identity for analytics | analytics init |
| Adjust | `libsigner.so` + classes | attribution | `getAdid`, `getAttribution` |
| Sentry | classes | crash reporting | SDK init |
| RevenueCat | classes + `ui.iap` | subscriptions | purchase flow |
| Play Billing / Core | manifest + meta-data | purchases, dynamic modules | SDK |
| Pusher | 16 classes | realtime | `f9.j` |
| Rive | `librive-android.so` | animation | 59 `.riv` |
| Google reCAPTCHA | classes (used incidentally for UA builder helper) | — | incidental |
| Facebook / Apple / Google Sign-In | manifest providers | social auth | INFERRED |
| Glance | widget string resources | home-screen widget | INFERRED |

## Incidental dependency note
`fh.b` builds the User-Agent through `com.google.android.recaptcha.internal.b.k(...)` — a *helper* used only for
string joining. This is an artefact of R8 inlining, not a reCAPTCHA feature in that path.
