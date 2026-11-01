# Mission 7 — All Network Protocols

| Protocol | Where | Payload | Evidence |
|---|---|---|---|
| HTTPS/JSON REST | Retrofit, 29 interfaces, 62 endpoints | DTOs (kotlinx.serialization) | catalogue |
| Server-Sent Events | `POST /v1/aiTutor/conversations[/{id}]` with `Accept: text/event-stream` | `AiTutorConversationMessage` | repository |
| WebSocket | `wss://api.mimo.org/v1/run/socket` | run streaming (schema NOT_RECOVERED) | `pg.a` |
| Pusher (WSS) | private channels via `f9.j` | channel events (names UNKNOWN) | constructor |
| Firebase (HTTPS) | Remote Config, Analytics, Messaging, Installations | SDK-managed | classes |
| Adjust (HTTPS) | attribution + adid | SDK-managed | `libsigner.so`, calls |
| RevenueCat (HTTPS) | purchases/entitlements | SDK-managed | classes |
| Sentry (HTTPS) | crash events | SDK-managed | classes |
| Play (HTTPS) | dynamic modules, billing | SDK-managed | manifest |

## What is *not* present
No gRPC, no MQTT, no long-polling, no custom binary protocol, no webhook receiver.
