# Mission 7 — AI Tutor Quota

| Aspect | Finding | Label |
|---|---|---|
| counter | `userMessageCount` (int) from `GET …/messages/count` | VERIFIED_STATIC |
| limit value | **not in the payload** | VERIFIED_STATIC (absence) |
| enforcement | server (client has no block branch) | INFERRED_HIGH |
| reset period | not recoverable client-side | UNKNOWN |
| subscription link | upgrade UI references tutor; `isPremium` is the only entitlement | INFERRED |
| local state | none persisted | VERIFIED_STATIC |

## On the "five free questions" observation
Nothing in the client encodes 5. If the free tier is 5 messages, that number is server-side; the client can only
display `userMessageCount` and whatever the server refuses. Mission 7 therefore records it as
**BACKEND_ONLY**, not as a client rule.
