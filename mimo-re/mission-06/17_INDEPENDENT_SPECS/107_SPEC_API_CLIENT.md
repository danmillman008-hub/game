# Spec 107 — API Client

## MUST
1. Base `https://api.mimo.org`, all paths under `/v1/`; test host `api-testing.mimo.org`.
2. OkHttp with connect 20 s / read 30 s; interceptors in order: connectivity gate → User-Agent → Bearer.
3. `User-Agent: Mimo/9.35 Android/<release> (<device>)`.
4. `Authorization: Bearer <token>` on the authenticated client only.
5. Result envelope for every call; `NoConnectionException` offline.
6. Verb per endpoint as catalogued: 28 GET, 24 POST, 4 PATCH, 4 DELETE, 2 PUT.
7. WebSocket `wss://api.mimo.org/v1/run/socket` with `Sec-WebSocket-Protocol: authorization.bearer.<token>`.

## MUST NOT
- Assume a retry/backoff policy, a refresh-token flow, or pagination (none recovered).
- Claim any server behaviour beyond the shapes in `50_REQUEST_RESPONSE_SCHEMAS/`.

## GIVEN EVIDENCE
`07_NETWORK/47..55`, `55_ENDPOINT_GRAPH.json`.
