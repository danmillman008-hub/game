# 09 — Authentication lifecycle (terminal)

## 1. Separation of concerns

| Concern | Owner | Never stored by app |
|---|---|---|
| identity | `FirebaseAuth.currentUser` | yes |
| access token | `ku.a.d(boolean)` per request | yes (no app cache) |
| authorization policy per call | Retrofit **method annotation** → `fh.a` | — |
| user profile | `/v1/users/{userId}/profile`, `/v1/user/settings` | — |
| local session state | none (only a preferences pointer) | — |
| server session | not represented client-side | — |

## 2. Token path

```text
fh.a.intercept → tag(Method).getAnnotation(marker) != null → ku.a.d(false)
ku.a.d: currentUser == null → null
        else Tasks.await(getAccessToken(false)) → claims["exp"] vs now
             expired → Tasks.await(getAccessToken(true))   (exactly one forced refresh)
        failure → AccessTokenUnavailableException (wrapped into IOException by fh.a)
```

No skew margin, no timer, no scheduler, no refresh interceptor, no 401 handling.

## 3. Session states

`SignedOut → Anonymous (anonymousAuthentication) → Linked (linkCredentialWithAnonymousAccount) → Authenticated`;
alternatively `SignedOut → Authenticated` via `signInWithCredential`, e-mail, Google, Facebook. The repository
**observes** auth state through a flow (`AuthenticationFirebaseRepository$init$1` collects it), so features react to the
flow rather than reading `currentUser`.

## 4. Sign-out and session clearing

`com.getmimo.ui.authentication.logout.{a,b}` are the only logout-named app classes; their bodies were never recovered
and no `signOut()` call site was found elsewhere (`A2`/`A-02`, partially closed).

**Therefore: it is not established that logout clears local progress, completion or preferences.** What *is* known:
nothing in the persistence layer keys rows by account (`B-2`), so local progress survives any identity change on the
device until the server merges or discards it.

## 5. Re-authentication and account switching

No client code path was recovered that reacts to an identity change by rewriting or clearing local learner data. Because
`lesson_progress` has no account column, a second account on the same install inherits the first account's pending rows.

## 6. Entitlement interaction

Entitlement is RevenueCat's (`PublicUser.isPremium` mirrored locally). It is **not** read by the auth interceptor and
does not gate the token; gating happens in UI/use-case layer (`Q-115` partially closed).

## 7. Channels

| Transport | Auth channel |
|---|---|
| REST via Retrofit | `fh.a` header, annotation-conditional |
| SSE (AI tutor) | manual `Authorization` header |
| WebSocket (execution) | `Sec-WebSocket-Protocol: authorization.bearer.<token>` |
| Pusher channel auth | manual `Authorization` header |
| Certificate download | manual `Authorization` header |

One provider (`ku.a`) feeds all five, but a change to `fh.a` affects only the first.

**Evidence anchors:** `05_AUTHENTICATION_CLOSURE/01_TOKEN_PROVIDER_AND_LIFECYCLE.md`, `…/02_INTERCEPTOR_CHAIN.md`, `…/04_SESSION_STATE_MACHINE.md`, `07_NETWORKING/03_AUTHENTICATION_LIFECYCLE.md`, records E-A01…E-A03 in `16_CONSOLIDATED_EVIDENCE_REGISTER.json`.
