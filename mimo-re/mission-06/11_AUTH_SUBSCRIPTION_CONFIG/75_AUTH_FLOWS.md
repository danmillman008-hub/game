# Mission 6 — Auth Flows

## Scope
Registration, login, session and guest mode as visible in the client.

## Method
Manifest activities (auth/onboarding), endpoint catalogue's unauthorised subset, token holder, auth
interceptor; mission-05 `15_AUTH_AND_IDENTITY/`.

## Findings
1. Auth screens exist as activities under `ui.onboarding`/`ui.auth`-like packages (obfuscated names), and 9
   catalogue endpoints are unauthenticated (bootstrap). (VERIFIED_STATIC for counts)
2. The token is stored client-side and injected by `fh.a`; **no refresh interceptor** was found
   (Phase 7.49). (VERIFIED_STATIC)
3. **The credential exchange itself is NOT_RECOVERED**: the login request builder was not in the
   decompiled batch, so the exact payload (email/password vs OAuth code vs magic link) is unknown
   (`Q-80`).
4. Guest/anonymous mode: no distinct anonymous token path was found; onboarding completion likely requires
   an account (`INFERRED`, contradicted-or-supported by nothing recovered).

## Evidence labels
As marked. Nothing about backend auth is asserted.

## Open questions
`Q-80`, `Q-82`, `Q-114` social sign-in providers (manifest shows Google/Facebook/Apple SDK presence only).

## Reproduction
`grep -c 'authorization' ../mission-05/evidence/API_CATALOG_V2.csv`
