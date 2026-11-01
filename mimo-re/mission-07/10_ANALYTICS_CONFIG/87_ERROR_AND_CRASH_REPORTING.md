# Mission 7 — Error and Crash Reporting

| Layer | Mechanism | Evidence |
|---|---|---|
| crash | Sentry SDK | `io.sentry` classes + native libs |
| network errors | `NoConnectionException` + `d70.b` envelope | interceptors |
| remote-config errors | logged via `le0.b.a.e(...)` | analytics constructor |
| Adjust failures | `AdjustTokenNotAvailableException` | `com.getmimo.analytics` class |
| analytics failures | log-and-continue | constructor |
| uncaught handler | none app-owned found | absence |

## Logging
`le0.b.a` is the app's logging facade (used with tags/warnings inside analytics init). No structured logger or
log-file sink was recovered.

## Gap
No mapping from exception types to user messages was recovered; errors surface as envelope failures.
