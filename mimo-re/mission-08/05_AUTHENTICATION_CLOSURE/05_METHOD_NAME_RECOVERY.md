# Phase 5.5 — Recovering original method names for renamed classes

## 1. The technique

Renaming rewrote class names but left Kotlin lambdas' binary names intact. A lambda generated for
`AuthenticationFirebaseRepository.signInWithGoogle` is still called
`com.getmimo.data.source.remote.authentication.AuthenticationFirebaseRepository$signInWithGoogle$2`, even though
`AuthenticationFirebaseRepository` itself is now `…authentication.a`.

Each such lambda is constructed with the receiver and invokes a bounded set of methods on classes in the same
package. Therefore:

> **original method name (from the lambda's binary name) → obfuscated method(s) the lambda actually invokes**

is a *measured* mapping, not a guess. Where the lambda invokes exactly one method on exactly one receiver class,
confidence is `HIGH`; where it invokes several candidates (overloads, delegation), all candidates are listed and
confidence is `MEDIUM` — none is silently chosen.

Implementation: `tools/recover_method_names.py` (`--package … --out …`), deterministic, no decompiler.

## 2. Result for the authentication package

| Metric | Value |
|---|---|
| lambda families found | 11 |
| `HIGH` mappings | **6** |
| `MEDIUM` mappings | 5 |
| families with no single receiver | 0 in this package |

`HIGH` mappings:

| Original | Renamed |
|---|---|
| `AuthenticationFirebaseRepository.fetchAbTestUserGroups` | `a.c` |
| `AuthenticationFirebaseRepository.fetchAbTestUserGroupsIfSignup` | `a.d` |
| `AuthenticationFirebaseRepository.linkCredentialWithAnonymousAccount` | `a.i` |
| `AuthenticationFirebaseRepository.postVisitSafely` | `a.k` |
| `AuthenticationFirebaseRepository.signInWithCredential` | `a.l` |
| `GoogleSignIn.signIn` | `b.a` |

## 3. Why this matters beyond authentication

1. **It gives the app's own vocabulary back.** The repository's API surface (anonymous auth, link credential,
   sign-in variants, post-visit, A/B groups) is now known from the app's own lambda names rather than from guesses
   about obfuscated letters.
2. **It is applicable to every renamed subsystem.** The same command run over
   `com.getmimo.data.source.remote.pusher`, `…local.aitutor`, `…remote.keys`, `com.getmimo.ui.lesson.interactive`
   etc. recovers their method vocabularies. It is listed as the standard first step of Phases 3, 6, 7.
3. **It is falsifiable.** Each mapping cites the lambda class and the invoke instruction inside it, so a later
   reader can disagree with a specific row.

## 4. Limits

* Lambdas are generated for *suspending* or *inline* call sites; a method never used in a lambda stays unnamed
  (e.g. `getProfile`, `getUsername` in this package did not resolve to a single receiver).
* Overloads are not separated by this technique alone.
* Inlined `suspend` functions can lose their lambda entirely (the `$$inlined$filter$1` classes in this package are
  such artefacts).

## 5. Reproduction

```bash
cd mimo-re/mission-08
/tmp/venv/bin/python tools/recover_method_names.py --dex-dir /tmp/x \
  --package com.getmimo.data.source.remote.authentication \
  --out 05_AUTHENTICATION_CLOSURE/evidence/METHOD_NAME_RECOVERY.json
```
