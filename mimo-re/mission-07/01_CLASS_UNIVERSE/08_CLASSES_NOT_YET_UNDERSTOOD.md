# Mission 7 — Classes Not Yet Understood

## Quantitative position
- 29,454 classes inventoried; 3,284 decompiled (11.1%); 15,087 methods indexed from those.
- 2,178 classes are in the deep-investigation queue (application-owned, hotspot or ≥25 methods).
- Classes that are **inventoried only** (no body inspected): ~26,170.

## Named classes whose behaviour is still unknown
| Class | Why it matters | What is known | What is missing |
|---|---|---|---|
| `oi.a`, `ra0.*`, `ua0.*` (coroutine helpers) | async plumbing for every repository | names only | no semantic need recovered |
| `np.h`, `be.d`, `oy.t` | injected analytics wrappers (constructor deps of `com.getmimo.analytics.a`) | constructor parameters | method bodies/semantics |
| `ri.b`, `ri.c` | token/session holder | `ri.b.d(0)` returns the bearer token | storage backend, refresh, expiry |
| `vi.n`, `z60.*` | kotlinx.serialization plumbing | descriptors | not app logic |
| `sonar.*` (59 classes) | unknown UI effect system | package presence | purpose |
| `jm.q`, `jm.g`, `jm.o` | analytics property/event interfaces | used as types | full interface surface |
| `ea0.*` / `ia0.*` | inferred network+DB modules | usage sites | responsibility split |

## Why these remain
The decompiled subset was chosen by feature hotspots; the remaining application classes were never required to
explain a recovered execution path. Closing them would need a full-tree decompile (≈26k classes), which is
outside this environment's time/memory budget (DAD peak RSS ≈2.6 GB, ~40 s per 100 classes).

## Consequence
Every behaviour claimed in Mission 7 is supported by an inspected class; no claim depends on an uninspected one.
