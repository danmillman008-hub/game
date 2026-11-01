# Mission 7 — Application Initialization

```
Zygote → process
 └─ bin.ghost.YRF (base Application, 19 classes)
     └─ com.getmimo.App
         └─ ae.m graph (127 arms, eager, field-ordered)
             ├─ case 1  analytics singleton (FirebaseAnalytics, Adjust, FCM token, AB-test groups)
             ├─ case 20 OkHttpClient (20s/30s, interceptors hg.e, fh.b, fh.a)
             ├─ case 22 HttpUrl (prod vs testing)
             ├─ Room database + 3 DAOs
             └─ repositories / interactors
         └─ MainActivity (12 deep-link filters) | onboarding nav graph (17 fragments)
             └─ home / learning path
```

## Evidence
- Cases and order: `09_COMPLETE_DI_GRAPH.json` (`lines` give source order).
- Analytics init side effects: `com.getmimo.analytics.a.<init>` — `Adjust.getAdid`, `Adjust.getAttribution`,
  `FirebaseMessaging…`, log strings "Fetch AB test user groups from Firebase",
  "FirebaseRemoteConfig fetchAndActivate() failed due to …".
- Splash aliases + `MainActivity` filters: decoded manifest.

## Unresolved
What `bin.ghost` does before `com.getmimo.App` (static structure only; see `97_BIN_GHOST_*`).
