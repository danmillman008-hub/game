# Mission 7 — Background Tasks

## Recovered
| Mechanism | Present? | Evidence |
|---|---|---|
| FCM service | yes | manifest + `FirebaseMessagingService` subclass |
| Pusher connection | yes | `f9.j` |
| WorkManager progress sync | **no** | no `Worker`/`ListenableWorker` subclass found in the decompiled set or manifest |
| AlarmManager jobs | no | not in manifest |
| foreground services | 19 services in manifest, none progress-related by name | manifest |
| cleanup/download jobs | no | none recovered |

## Consequence
Progress push is **foreground-only**. If the app is killed with queued rows, they wait for the next live push
cycle. This is consistent with `in_queue` rows surviving restarts and with the absence of a scheduler.

## Manifest services (19)
Names are obfuscated; the identifiable ones are SDK services (Firebase Messaging, Play Core/Billing,
Adjust/RevenueCat support, WebView/`androidx` workers for libraries). No app-owned scheduling service was found.
