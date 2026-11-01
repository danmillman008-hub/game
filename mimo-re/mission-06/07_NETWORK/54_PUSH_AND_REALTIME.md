# Mission 6 — Push and Realtime

## Scope
Non-HTTP-request channels: sockets, server push and webhooks.

## Method
String-pool scan for `wss://`, listener classes, manifest services/receivers with push-related names,
Pusher references.

## Findings (VERIFIED_STATIC)
1. **WebSocket** `wss://api.mimo.org/v1/run/socket` used for code execution streaming (`pg.a`), auth via
   subprotocol.
2. **Pusher** is instantiated for realtime channels (`f9.j` reads the API host); auth for private channels
   goes through the API. Pusher's role (notifications vs live progress) was not traced (`Q-89`).
3. Firebase/FCM: `firebase-messaging` receiver present in the manifest; Pushwoosh/FCM tokens exist as
   preferences. Notification *content* handling was not traced.
4. No webhook or long-polling endpoint exists in the catalogue.

## Evidence labels
1, 3, 4 **VERIFIED_STATIC**; 2 (role) **INFERRED**.

## Open questions
`Q-89` Pusher channel usage; `Q-90` notification → deep-link mapping.

## Reproduction
`grep -o 'wss://[^"]*' -r /tmp/dad | sort -u`
