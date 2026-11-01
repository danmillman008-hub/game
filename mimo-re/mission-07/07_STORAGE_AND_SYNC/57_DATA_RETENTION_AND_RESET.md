# Mission 7 — Data Retention and Reset

| Data | Retained | Deleted when | Evidence |
|---|---|---|---|
| progress row | yes | after successful push | repository |
| chapter/tutorial markers | yes | never observed deleted | no delete SQL |
| token | yes | logout (unrecovered) | `ri.*` |
| onboarding flags | yes | reinstall | prefs |
| content assets | yes (bundled/module) | app update | assets |
| AI tutor messages | **not stored** | n/a | no table |
| analytics events | SDK-managed | SDK policy | SDK |
| crash logs | Sentry-managed | Sentry policy | SDK |
| caches | none app-level | n/a | storage map |

## `allowBackup=false`
Local progress does not survive a device backup/restore or an account-less reinstall. Combined with the
assert-only sync, this means losing queued rows on reinstall is expected behaviour, not a bug.
