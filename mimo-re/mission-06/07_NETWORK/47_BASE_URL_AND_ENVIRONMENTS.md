# Mission 6 — Base URL and Environments

## Scope
Which hosts the client can talk to, how the host is chosen at runtime, and what environments exist —
closing mission-05 item U-22.

## Method
`ae.m` (127-case DI switch) case-by-case extraction (`evidence/DI_GRAPH.json`), string-pool scan of all
12 DEX files, and the decompiled network classes.

## Findings (VERIFIED_STATIC)
```
production   https://api.mimo.org
dev/testing  api-testing.mimo.org        (case 22, selected by a build/debug flag)
realtime     wss://api.mimo.org/v1/run/socket
deep link    https://getmimo.com/*  (12 intent filters on MainActivity)  +  mimo://
```
- The host is **not** stored in BuildConfig or `strings.xml`; it is produced by a `when` over an enum of
  ~127 dependencies whose case 22 returns the `HttpUrl`. That is why a plain string search fails and why
  mission-5 could not close U-22 by grep.
- All API paths are versioned under `/v1/`.
- No per-region or per-tenant host was found in the recovered cases.

## Evidence labels
Hosts and versioning: **VERIFIED_STATIC**. The "debug flag" wording: **INFERRED_HIGH** (the flag read
was not traced to its source; the two hosts and the branch are directly visible).

## Open questions
`Q-76` the exact flag controlling case 22; `Q-77` whether a QA/staging host exists outside these branches.

## Reproduction
```bash
/tmp/venv/bin/python tools/extract_di_graph.py --out /tmp/di.json && \
python3 -c "import json;[print(c) for c in json.load(open('/tmp/di.json'))['cases'] if c.get('case')==22]"
```
