# Phase 2.6 — Callback registrations and framework entry points

Two categories of "call" never appear as ordinary call sites. Both are enumerated here so later phases cannot
mistake their absence for inactivity.

## 1. Callback registrations (327 edges, 321 app-side)

| Registered API | Edges | Reading |
|---|---|---|
| `Flow.collect` | 246 | the dominant asynchronous pattern; each is a coroutine that observes a flow |
| `addOnContextAvailableListener` | 25 | Compose/Activity startup hooks |
| `addOnCompleteListener` | 8 | Google Tasks completion |
| `setOnCheckedChangeListener` | 4 | settings switches (`com.getmimo.ui.settings.SettingsListSwitch…`) |
| `setListener`, `addOnSuccessListener`, `registerForActivityResult`, `setOnClickListener`, `setOnItemClickListener`, `addListener`, `registerListener`, `setEndIconOnClickListener` | 2–3 each | UI wiring |

Notable app-side registrations (examples, all `LOW` confidence by construction):

```
com.getmimo.ui.developermenu.DeveloperMenuFragment            → SettingsListSwitch.setOnCheckedChangeListener
zk.e                                                          → SettingsListSwitch.setOnCheckedChangeListener
com.getmimo.ui.developermenu.discount.DeveloperMenuDiscount…  → SettingsListSwitch.setOnCheckedChangeListener
ci.b, bk.e0, ef.b, dn.f, df.e, fi.a                           → Flow.collect (renamed app classes)
```

`LOW` means: the object is handed to the framework; the framework decides *when* to call it. Mission-8 therefore
never derives an ordering from a registration edge.

## 2. Framework entry points

A framework entry point has no static caller inside the app by definition. The graph records the call sites that
*reach* lifecycle methods from outside (usually none) and the ones that *invoke* lifecycle-like methods internally.
The following app classes carry a platform-invoked entry point that the graph sees only as a method with zero
static callers:

| Class | Entry point | Kind |
|---|---|---|
| `com.getmimo.data.notification.MimoFirebaseMessagingService` | `d(RemoteMessage)` / `e(String)` (overrides of FirebaseMessagingService) | FCM |
| `com.getmimo.apputil.notification.NotPremiumNotificationService` | service entry (`onStartCommand`-family) | service |
| `com.getmimo.ui.authentication.AuthenticationActivity` | `onCreate`, `onBackPressed` | activity |
| `com.getmimo.ui.lesson.interactive.webview.a` | `onAttachedToWindow`, `onScrollChanged`, `onTouchEvent` | view |
| `com.getmimo.ui.components.common.MimoWebView` | `getMimoWebChromeClient`, console/resource hooks | view |
| `ri.a` | `onAvailable(Network)`, `onLost(Network)` | platform callback |
| `com.getmimo.ui.widget.StreakWidgetRefreshWorker` (queue row) | `doWork` | WorkManager |
| `com.getmimo.data.source.remote.authentication.PostVisitWorker` | `doWork` | WorkManager |
| `com.getmimo.data.source.remote.account.AccountDeleteWork` | `doWork` | WorkManager |

Measured consequence for the method register: **269 of 637 methods have no static caller**, and this table
explains the majority of them. A zero-caller method is not dead code.

## 3. Injection and reflection

* DI: mission-06 recovered 127 case arms of `ae.m` (the renamed application component). Constructor call sites
  appear in the graph (e.g. `ae.m → ku.a.<init>` `direct` `HIGH`), so DI construction is visible as ordinary
  `direct` edges even though the *binding decision* is a switch arm.
* Reflection: 20,599 sites, all in libraries (Gson, Kotlin reflection, Firebase). No app-namespace site resolves a
  Mimo class by name. Therefore no `reflection` edge exists — the absence is measured, not assumed.

## 4. What this means for Phase 11 (end-to-end validation)

Sequence diagrams must mark framework-invoked steps with their trigger (`FCM push`, `WorkManager`, `network
callback`, `activity lifecycle`), because the static graph cannot order them relative to app-initiated work.
Any flow that begins at a framework entry point has, at its start, an **unknown latency and an unknown thread**.
