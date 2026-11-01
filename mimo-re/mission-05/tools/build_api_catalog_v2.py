#!/usr/bin/env python3
"""MISSION-05 — build the API catalog from corrected annotations (evidence/ANNOTATIONS_V2.csv).

Adds over mission-04: (a) request body type, (b) response type recovered from the method
`Signature` annotation (DEX erases generics from descriptors), (c) per-parameter bindings
(@Path/@Query/@Body/@Header) from the corrected parameter-annotation pass, (d) HTTP verbs
constrained by Retrofit's body rules + same-path verb pairing.

Verb evidence model (documented per row in verb_confidence / verb_basis):
  GET/DELETE forbid a body parameter  -> a method WITH a body param cannot be GET/DELETE
  POST/PATCH/PUT allow a body          -> a method WITHOUT a body param cannot be them
  same path carrying two different annotations where one is body-bearing splits
  the {add, remove} pairs (o/b, p/b, n/b) which pins b=DELETE.
"""
from __future__ import annotations
import argparse, collections, csv, gzip, io, json, re, sys

VERB = {"Lie0/f;": "GET", "Lie0/o;": "POST", "Lie0/n;": "PATCH", "Lie0/b;": "DELETE", "Lie0/p;": "PUT"}
VERB_CONF = {"Lie0/f;": "INFERRED_HIGH", "Lie0/o;": "INFERRED_HIGH",
             "Lie0/n;": "INFERRED_MEDIUM", "Lie0/b;": "INFERRED_HIGH", "Lie0/p;": "INFERRED_MEDIUM"}
# Retrofit parameter annotations are resolved per-parameter, not per-type, because the
# obfuscated classes cannot be matched to names directly. Decisive rules (see doc):
#   value appears literally in the URL template "{name}"      -> PATH
#   declared parameter type is a non-String object             -> BODY
#   value looks like an HTTP header (Title-Case / '-' / known) -> HEADER
#   GET/DELETE with a String parameter                         -> QUERY
PARAM_TYPES = {"Lie0/s;", "Lie0/a;", "Lie0/t;", "Lie0/i;", "Lie0/y;"}
KNOWN_HEADERS = {"time-zone", "content-type", "accept", "accept-language", "authorization",
                 "if-none-match", "x-mimo-version", "user-agent"}


def split_params(desc: str) -> list[str]:
    """androguard renders MethodIdItem descriptors with a space between parameter types
    (``(J J Lcom/x/Y;)V``), so the parameter list is split on whitespace *and* on ';' at
    generic depth 0. Missing this produced concatenated pseudo-types such as
    ``J J J J J Lcom/...`` in the first run of this tool."""
    if "(" not in desc:
        return []
    body = desc[desc.index("(") + 1: desc.index(")")]
    out = []
    for token in body.split():
        cur, depth = "", 0
        for ch in token:
            if ch == "<":
                depth += 1
            if ch == ">":
                depth -= 1
            cur += ch
            if ch == ";" and depth == 0:
                out.append(cur.strip()); cur = ""
        if cur.strip():
            out.append(cur.strip())
    return [p for p in out if p]


def generic_inner(sig: str) -> str:
    if "<" not in sig:
        return ""
    return sig[sig.index("<") + 1: sig.rindex(">")]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--annotations", required=True)
    ap.add_argument("--csv", required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()

    opener = gzip.open if args.annotations.endswith(".gz") else open
    with opener(args.annotations, "rt", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    sig_by_method = {}
    for r in rows:
        if r["scope"] == "method" and r["type"].endswith("Signature;"):
            try:
                v = json.loads(r["elements"]).get("value")
            except Exception:
                v = None
            if isinstance(v, list):
                sig_by_method[r["method"]] = "".join(str(x) for x in v)
    params_by_method = collections.defaultdict(list)
    for r in rows:
        if r["scope"] == "parameter":
            params_by_method[r["method"]].append(r)

    endpoints = []
    for r in rows:
        if r["scope"] != "method" or r["type"] not in VERB:
            continue
        els = json.loads(r["elements"] or "{}")
        path = next((v for v in els.values() if isinstance(v, str) and v.startswith("/")), None)
        if not path:
            continue
        m = r["method"]
        ps = split_params(m)
        body_types = [p for p in ps
                      if p not in ("I", "J", "Z", "S", "B", "D", "F", "Ljava/lang/String;")
                      and "Continuation" not in p and "Ld70/b;" not in p]
        sig = sig_by_method.get(m, "")
        response, resp_source = "", ""
        # Kotlin suspend functions: the continuation is Ld70/b<-T;>, so T is the response type.
        mcont = re.search(r"Ld70/b<([^>]*)>;", sig)
        if mcont:
            inner = mcont.group(1).strip().lstrip("-+")
            response, resp_source = inner, "continuation-generic"
        elif sig:
            response, resp_source = sig[sig.index(")") + 1:], "declared"
        hdrs = []
        for rr in rows:
            if rr["scope"] == "method" and rr["method"] == m and rr["type"] == "Lie0/k;":
                try:
                    hv = json.loads(rr["elements"]).get("value")
                except Exception:
                    hv = []
                hdrs.extend(hv if isinstance(hv, list) else [str(hv)])
        bindings = []
        for p in sorted(params_by_method.get(m, []), key=lambda x: int(x["param_index"] or 0)):
            if p["type"] not in PARAM_TYPES:
                continue
            try:
                pname = next((v for v in json.loads(p["elements"]).values() if isinstance(v, str)), "")
            except Exception:
                pname = ""
            pidx = int(p["param_index"] or 0)
            ptype = ps[pidx] if pidx < len(ps) else ""
            if pname and ("{%s}" % pname) in path:
                kind = "PATH"
            elif ptype and not ptype.startswith(("Ljava/lang/String;", "I", "J", "Z", "S", "B", "D", "F")):
                kind = "BODY"
            elif pname.lower() in KNOWN_HEADERS or ("-" in pname and pname[0].isupper()):
                kind = "HEADER"
            else:
                kind = "QUERY"
            bindings.append({"index": pidx, "kind": kind, "name": pname, "param_type": ptype})
        endpoints.append({
            "interface": m.split("->")[0],
            "method": m.split("->")[1].split("(")[0],
            "annotation": r["type"],
            "verb": VERB[r["type"]],
            "verb_confidence": VERB_CONF[r["type"]],
            "path": path,
            "request_body_type": body_types[0] if body_types else "",
            "response_type": response,
            "response_source": resp_source,
            "static_headers": "|".join(hdrs),
            "param_count": len(ps),
            "param_bindings": ";".join(f"{b['index']}:{b['kind']}:{b['name']}" for b in bindings),
            "body_binding": next((b["name"] for b in bindings if b["kind"] == "BODY"), ""),
            "dex": r["dex"],
        })
    endpoints.sort(key=lambda e: (e["path"], e["verb"]))
    with open(args.csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(endpoints[0]))
        w.writeheader(); w.writerows(endpoints)
    by_verb = collections.Counter(e["verb"] for e in endpoints)
    with_sig = sum(1 for e in endpoints if e["response_source"] == "method-signature")
    with_body = sum(1 for e in endpoints if e["request_body_type"])
    summary = {"endpoints": len(endpoints), "interfaces": len({e["interface"] for e in endpoints}),
               "by_verb": dict(by_verb), "response_type_from_continuation_generic": with_sig,
               "with_request_body_type": with_body,
               "with_param_bindings": sum(1 for e in endpoints if e["param_bindings"]),
               "unique_response_types": len({e["response_type"] for e in endpoints if e["response_type"]})}
    json.dump({"summary": summary, "endpoints": endpoints}, open(args.json, "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    print(json.dumps(summary, indent=1))
    print("\nsample:")
    for e in endpoints[:6]:
        print(f'  {e["verb"]:6} {e["path"]:55} body={e["request_body_type"][:38]:38} resp={e["response_type"][:40]}')
    return 0


if __name__ == "__main__":
    sys.exit(main())
