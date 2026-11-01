# Mission 6 — Third-Party SDKs

## Scope
Which external SDKs the client embeds (privacy/architecture relevant).

## Findings (VERIFIED_STATIC — presence in DEX/manifest/libs)
| SDK | Purpose | Evidence |
|---|---|---|
| OkHttp/Retrofit/kotlinx.serialization | networking/parsing | Phases 7 |
| Firebase (Analytics, Messaging, Remote Config, Crashlytics?) | analytics/push/config | classes + manifest receiver |
| RevenueCat | subscriptions | purchase classes |
| Adjust | attribution | `libsigner.so` |
| Sentry | error reporting | `io.sentry` classes |
| Pusher | realtime channels | `f9.j` |
| Rive | animation | `librive-android.so` |
| Google Play (Billing/Feature Delivery/Core) | purchases + dynamic modules | manifest meta-data |
| reCAPTCHA (Google) | abuse protection | `com.google.android.recaptcha` referenced in `fh.b` |
| Facebook/Apple/Google sign-in | social auth | manifest providers/activities (`Q-114`) |
| Glance (app widgets) | home-screen widget | string resources referencing `GlanceAppWidget` |

Notable: `fh.b` builds the User-Agent through a **reCAPTCHA internal utility**
(`com.google.android.recaptcha.internal.b.k(...)`) — an incidental dependency, not a functional use of
reCAPTCHA in that path.

## Open questions
`Q-137` Crashlytics vs Sentry duplication; `Q-138` widget functionality.
