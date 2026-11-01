# 12 — Analytics, settings, entitlements, other features

## 1. Analytics

| Aspect | Finding |
|---|---|
| Dispatcher | `com.getmimo.analytics.a` implementing `jm.g` |
| Event object | `ge.j(String name, int index)` |
| Property types | `com.getmimo.analytics.properties.base.*` |
| Verified events | **14**, each bound to an emitting class (`EVENTS_WITH_CALLSITES.csv`) |
| Destinations | Firebase Analytics, Adjust (adid/attribution), Customer.io (`POST /push/events` on C4), Mixpanel present |
| Local-only events | none proven — every verified event reaches a sink |

`U-20` (name↔emitter binding) remains partially closed: the 14 are bound, the remaining literals in the string pool are
not. Correction C-14 stands: `solutionFeedbackCorrect/Wrong` are **property names**, not events.

## 2. Settings

`/v1/user/settings` GET/PATCH, `/v1/user/settings/avatar` POST + PUT, plus local preferences (`mimo_prefs*`) and the
developer menu (dev storage `sk.a`, which also flips the API host). Settings that only write preferences work offline.

## 3. Subscription and entitlement

| Layer | Mechanism | Evidence |
|---|---|---|
| purchase | RevenueCat SDK (+ Play Billing) | mission-07 `13_SUBSCRIPTION/90` |
| entitlement flag | `PublicUser.isPremium` mirrored locally | mission-06 `11_AUTH_SUBSCRIPTION_CONFIG/81` |
| product catalogue | `GET`/`POST /v1/products/user` (`Lnh/c;`) | Stage 7 catalogue |
| paywall gates | local UI/use-case checks over the cached flag | mission-07 `91` |
| server validation | not observable | `BACKEND_ONLY` |

No claim is made that a local flag *grants* access: the client checks it, the server decides what content it serves.

## 4. Notifications

FCM receive path documented (mission-07 `09_STREAMING/72`); sending is backend. Device token registration:
`POST /v1/user/deviceTokens`. No client-side scheduling logic beyond WorkManager jobs (mission-07 `86`).

## 5. Background work

WorkManager jobs recovered (mission-07 `10_ANALYTICS_CONFIG/86`), including deferred account deletion
(`AccountDeleteWork`, whose body was never readable — `A6`). No progress-sync worker exists: the outbox flushes only at
chapter end and app start.

## 6. Other application-owned surfaces

Deep links (12 intent filters on `MainActivity` + `mimo://`), developer menu, Rive animation host, accessibility
semantics, design tokens/themes, onboarding and signup-prompt logic. Several are documented in mission-07
`12_UI_RESOURCES` and `13_SUBSCRIPTION`; per-domain status is in `15_FINAL_COVERAGE_MATRIX.csv`.

## 7. Feature ownership rule applied

Presence of an SDK is never treated as presence of a feature: Firebase/Adjust/Sentry/Pusher/RevenueCat are recorded as
integrations, and only the call sites that actually use them are counted as features.
