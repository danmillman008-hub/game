# Phase 12.4 — Transition narrative

## T-01 — `Q-121` "token storage mechanism": `NOT_RECOVERED` → **`CLOSED_STATIC`**

**What changed the answer.** Mission-7 assumed the credential store lived in `ri.a`/`ri.c` and could not recover
them. Mission-8 read those classes at DEX level and found a `ConnectivityManager$NetworkCallback` (refutation,
R-05), then followed the `"Bearer "` call sites to `ku.a.d(Z)Ljava/lang/String;` and read that method's 83
instructions.

**What is now known, precisely.**

* the credential is a **Firebase Authentication ID token**; there is no app-owned token store,
* one producer: `ku.a.d(boolean)`,
* client-side expiry check on the JWT `exp` claim (`org.joda.time.DateTime`, seconds), one forced refresh,
* failure type: `com.getmimo.data.source.remote.authentication.AccessTokenUnavailableException`,
* signed-out: returns `null` after logging `"There is no Firebase user!"`,
* header attachment: central `fh.a` interceptor for Retrofit methods annotated `ri.b`; four manual sites
  (SSE tutor stream, certificate download, Pusher auth, WebSocket handshake).

**Residual (stated, not hidden).** The persistence format inside the Firebase SDK. Library behaviour; the mission
does not inspect third-party storage internals.

**Reproduction**

```bash
cd mimo-re/mission-08
/tmp/venv/bin/python tools/dex_inspect.py --dex-dir /tmp/x --class ku.a --instructions \
    --out /tmp/ku.json
grep -n 'Token doesn\\|\\"exp\\"\\|FirebaseAuth' /tmp/ku.json | head
```

## T-02 … T-39 — unchanged, and why

No other question has a transition record. The reasons fall into three groups:

| Group | Questions (examples) | Why unchanged |
|---|---|---|
| awaits an unstarted phase | chapter ordering (`Q-27`), `TrackEtaResponse`, mastery/adaptation, gamification provenance | Phases 3/7/11 are not started |
| structurally not recoverable | authentication UI wiring, Rive per-asset binding | the owning classes are not `class_def`s (renamed); the composable body is absent from the dex |
| blocked by the environment | dynamic feature module contents (`Q-05`), any runtime question | no dynamic modules in the APK; no runtime |

An unchanged status is **not** a finding. It is the absence of one, recorded so that no later document can claim
progress that did not happen.
