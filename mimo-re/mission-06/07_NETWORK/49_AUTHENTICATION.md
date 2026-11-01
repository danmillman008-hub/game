# Mission 6 — Authentication

## Scope
How requests are authenticated and what the client does on 401.

## Method
Interceptor reads, token store usage, endpoint catalogue (authorization annotations), `ri.b` reads.

## Findings (VERIFIED_STATIC)
1. Auth is **bearer-token based**: `Authorization: Bearer <token>` added by `fh.a`, token read from a
   token holder (`ri.b`), value obtained via `d(0)`.
2. 53 of 62 catalogue endpoints are marked as requiring authorization (mission-05 annotation analysis);
   the remainder (auth/bootstrap endpoints) are unauthenticated.
3. No OAuth/OIDC flow classes were recovered in the analysed packages; the login screen was not traced,
   so the credential exchange itself is **NOT_RECOVERED** (`Q-80`).
4. No token-refresh interceptor was identified — a 401 is presumably handled at repository level
   (**UNKNOWN**).
5. WebSocket auth reuses the same token in the `Sec-WebSocket-Protocol` header
   (`authorization.bearer.<token>`) — the only place where the token is put in a non-standard header.

## Evidence labels
Points 1, 2, 5 **VERIFIED_STATIC**; 3, 4 **NOT_RECOVERED/UNKNOWN**.

## Open questions
`Q-80` login exchange; `Q-81` refresh/expiry; `Q-82` anonymous/guest mode.

## Reproduction
`grep -n 'Authorization' /tmp/dad/fh.a.java`
