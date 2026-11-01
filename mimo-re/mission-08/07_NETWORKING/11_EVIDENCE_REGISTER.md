# Phase 11 — Evidence register (network domain)

12 records, machine-readable in `11_EVIDENCE_REGISTER.json`. Labels follow the mission-6 evidence model
(`VERIFIED_STATIC`, `VERIFIED_RUNTIME`, `VERIFIED_EXPERIMENTAL`, `INFERRED`, `UNKNOWN`, `NOT_RECOVERED`, `BLOCKED`).

## Reproduce

```bash
# 1. DI provider bodies (client/timeout/interceptor/host evidence)
python3 -c "import json;d=json.load(open('mimo-re/mission-06/evidence/DI_GRAPH.json'));\
[print(c['case'],c['body']) for c in d['providers'] if c['case'] in (19,20,22,53,81,87,108,113,117)]"

# 2. Interceptor bodies
python3 -c "import json;d=json.load(open('mimo-re/mission-08/05_AUTHENTICATION_CLOSURE/evidence/DEX_auth_interceptors_and_repository.json'))['classes'];\
[print(k,[x.get('target') for m in v['methods'] if m.get('name')=='intercept' for x in m.get('calls',[])]) for k,v in d.items() if k in ('fh.a','hg.e')]"

# 3. Endpoint rows
python3 -c "import csv;r=list(csv.DictReader(open('mimo-re/mission-05/evidence/API_CATALOG_V2.csv')));print(len(r))"

# 4. d70.b == Continuation
python3 -c "import json;print(json.load(open('mimo-re/mission-06/01_APK_AND_ARCHITECTURE/05_OBFUSCATION_MAP.json')))" | grep -o '"obfuscated": "d70.b"[^}]*'
```

Recorded APK identity: `sha256 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`,
`classes.dex 2f2c0c61…`, `classes2.dex 1e0e36c0…`.

**Environment note:** the APK and DEX files are absent from this sandbox; the commands above read *committed* evidence,
not the APK. That is why every record carries `artifact_scope: committed evidence` and why no new instruction offsets
were produced in this stage.

## Records

| ID | Claim | Class/method | Instruction evidence | Status | Conf. |
|---|---|---|---|---|---|
| N-01 | 3 interceptors, order `hg.e`→`fh.b`→`fh.a` | DI case 20 | `interceptors.add(new hg.e(ri.d))`, `.add(new fh.b())`, `.add(new fh.a(ku.a))` | VERIFIED_STATIC | HIGH |
| N-02 | connect 20 s, read/write 30 s, `retryOnConnectionFailure=1` | `OkHttpClient$Builder` | `y=toMillis(20)`, `z=toMillis(30)`, `f=1` | VERIFIED_STATIC | HIGH |
| N-03 | host switch is a dev-menu preference | case 22 | `sk.a.e.g(this, sk.a.r[2]).booleanValue()` | VERIFIED_STATIC | HIGH |
| N-04 | shared Retrofit = C1 + case-22 host + kotlinx converter | case 19 | `client v`, `baseUrl w`, `he0.a.c(jx.d)` | VERIFIED_STATIC | HIGH |
| N-05 | second client 10 s/120 s without connectivity gate | case 108 | `y=10`, `z=120`, interceptors `fh.b`+`fh.a` | VERIFIED_STATIC | HIGH |
| N-06 | Bearer added only for annotated methods | `fh.a.intercept` | `Tags.a(KClass)` → `Method.getAnnotation(Class)` → `ku.a.d(Z)` | VERIFIED_STATIC | HIGH |
| N-07 | interceptor never forces refresh | `fh.a.intercept` | `ku.a.d(Z)` with constant 0 | VERIFIED_STATIC | HIGH |
| N-08 | offline gate throws `java.io.IOException` | `hg.e.intercept` | `com.getmimo.network.a.b()` → `new java.io.IOException(String)` | VERIFIED_STATIC | HIGH |
| N-09 | token provider: currentUser → exp check → one forced refresh | `ku.a.d(Z)` | phase-5 dump (83 instructions) | VERIFIED_STATIC | HIGH |
| N-10 | `d70.b` = `kotlin.coroutines.Continuation`, no Result envelope | `d70.b` | obfuscation map entry | VERIFIED_STATIC | HIGH |
| N-11 | three dedicated Retrofit instances with host literals | cases 53/87/117 | `baseUrl("…")` + `client v` + `create(iface)` | VERIFIED_STATIC | HIGH |
| N-12 | AI tutor repository receives client, host and token provider | case 81 | constructor argument list | VERIFIED_STATIC | HIGH |

## What is deliberately absent

* no runtime capture, no traffic, no token value, no header value, no user identifier;
* no server-side claim (all "what the server does" statements are in `mission-07/08_NETWORK/64_BACKEND_CONTRACT_BOUNDARIES.md`);
* no per-endpoint auth rows (A-01) and no WebSocket frame schema (A-04) — those are open, not filled with plausibility.
