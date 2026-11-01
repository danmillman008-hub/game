# Mission 7 — Authentication (complete to the available extent)

## Verified
1. Every authenticated request carries `Authorization: Bearer <token>` (`fh.a`).
2. 53 of 62 endpoints are marked as requiring authentication.
3. The WebSocket authenticates via subprotocol with the same token.
4. Pusher authorises channels through the API (`f9.j`).
5. Analytics init retrieves the Firebase app-instance id and FCM token (identity plumbing for analytics).

## Not recovered
| Item | Why |
|---|---|
| login/registration request bodies | auth repository not in the decompiled subset |
| provider list actually enabled | manifest shows FB/Apple/Google SDKs; enablement is server-side |
| token format/claims | never decoded (would be a secret-handling violation) |
| refresh/expiry | no interceptor/Authenticator exists |
| guest mode | no anonymous-token path found |

## Note
Because the auth interceptor has no path guard, the client is not the authority on which endpoints are public —
it always sends the header. Any "public endpoint" conclusion must come from the server contract.
