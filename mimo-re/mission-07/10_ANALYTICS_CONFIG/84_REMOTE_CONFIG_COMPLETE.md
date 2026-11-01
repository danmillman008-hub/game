# Mission 7 — Remote Configuration (complete)

## Mechanism (VERIFIED_STATIC)
Firebase Remote Config with **3 defaults** in `res/xml/remote_config_defaults.xml`, plus **AB-test user groups**:
`com.getmimo.analytics.a` logs "Fetch AB test user groups from Firebase", calls `fetchAndActivate()`, and logs
"FirebaseRemoteConfig fetchAndActivate() failed due to …" on error, plus "Error fetching Firebase's appInstanceId".

## Lifecycle inside analytics init
```
analytics singleton constructor
  → FirebaseAnalytics instance
  → Remote Config: fetch AB-test groups (fetchAndActivate)
      success → groups stored in the singleton (used to tag events/features)
      failure → logged, defaults used (no crash path)
  → Adjust adid / attribution
  → FCM token retrieval
```

## Consumers
The AB-test groups are held by the analytics singleton; **which features read them is not recovered** (`Q-118`).

## Failure fallback
Log-and-continue: the constructor catches the failure (message logged) and proceeds — the only defensive path
recovered in the whole initialisation.
