# Phase 9 — DI dependency map (network arm)

Source: `mission-06/evidence/DI_GRAPH.json` — 127 provider cases of the single Hilt/Dagger component switch, each with
its DAD pseudo-Java body. Machine-readable: `09_DI_DEPENDENCY_MAP.json`.

## 1. The five provider tokens that build the network stack

| Token | Type | Resolves to | Why that case |
|---|---|---|---|
| `v` | `okhttp3.OkHttpClient` | **case 20** (authenticated client) | only cases 20 and 108 construct a client; 108 builds it inline without storing it, so the stored token every other case reads is 20 |
| `w` | `String` | **case 22** (`https://api.mimo.org` / `https://api-testing.mimo.org`) | it is the only provider returning an API host |
| `u` | `ri.d` | connectivity-state provider | case 20 passes it into `hg.e`, whose constructor takes `ri.d` |
| `e` | `jx.d` | kotlinx serialization converter factory | every Retrofit builder calls `he0.a.c(x)` with the `jx.d` read from `e` |
| `b()` | `ku.a` | access-token provider (component method) | passed into `fh.a`, C3, C7, C8 |

## 2. Construction graph

```mermaid
graph TD
  U[ri.d<br/>connectivity] --> HE[hg.e]
  B[ku.a<br/>token provider<br/>component b()] --> FA[fh.a]
  B --> C3[case 108 client]
  B --> C7[aitutor repository<br/>case 81]
  B --> C8[pg.a socket<br/>case 113]
  HE --> C1[case 20 OkHttpClient<br/>20s/30s]
  FB[fh.b UA] --> C1
  FA --> C1
  C1 --> C2[case 19 Retrofit<br/>baseUrl=w]
  E[jx.d converter] --> C2
  W["w → case 22<br/>api.mimo.org | api-testing"] --> C2
  C2 --> IF[25 interfaces<br/>52 endpoints]
  C1 --> C4[case 53<br/>track.customer.io]
  C1 --> C5[case 87<br/>mimoauth.getmimo.com]
  C1 --> C6[case 117<br/>email.getmimo.com]
  C1 --> C3 --> EH[eh.a<br/>1 endpoint]
```

## 3. Host selection (closes mission-06 Q-76)

```text
ze.a (some provider) → cast sk.a (dev-menu storage)
if (sk.a.e.g(this, sk.a.r[2]).booleanValue()) return "https://api-testing.mimo.org";
else                                          return "https://api.mimo.org";
```

* the switch is a **dev-menu preference** (array element index 2 of `sk.a`), i.e. toggled by the developer menu UI, not
  by `BuildConfig.DEBUG` and not by a build flavor;
* `sk.a` is the same dev-menu storage that gates `LessonProgressQueue.storeLessonProgress` (Stage 5, `sk/a.e()`), so the
  same object controls both a logging/storage gate and the API host — a notable coupling;
* the preference key behind `r[2]` is not recovered (A-09).

## 4. Consumers of the shared Retrofit

25 interfaces / 52 endpoints, i.e. repositories in `com.getmimo.data.source.remote.*` and `data.repository.*`. The
generated Hilt factories that call `retrofit.create(Interface)` are outside these 127 cases (Dagger generates them as
`*_Factory` classes), so per-interface creation sites were not in the DI graph; the shared instance is nonetheless
proven by case 19 plus the fact that no other Retrofit provides an `api.mimo.org` base URL.

## 5. What the map cannot answer

* which interceptor set a *specific* endpoint gets when it is on C2 — that is the annotation (A-01), not the DI;
* whether `eh.a` (C3) is a download or a preview (A-03);
* whether any feature constructs a private client at runtime outside DI (a negative claim limited to the recovered
  provider set).
