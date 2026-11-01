#!/usr/bin/env python3
"""Build the Mimo API catalogue from *verified* annotation evidence.

Discovery that makes this possible
----------------------------------
Mimo ships an obfuscated build in which Retrofit itself is repackaged, so the HTTP
annotations are renamed to single letters (`Lie0/f;`, `Lie0/o;`, `Lie0/n;`, `Lie0/b;`,
`Lie0/p;` …). Because every endpoint path is an *annotation value* (never a `const-string`),
the path list can only be recovered by dereferencing `EncodedValue` objects — see
`tools/extract_annotations.py`.

Verb assignment is then done by cross-tabulation instead of guesswork:
  * the annotated method's own name convention (get*/fetch*/post*/put*/delete*/…) and
  * the semantics of the annotated path (read vs create vs mutate vs remove),
are compared against each annotation class. When an annotation class agrees with the
method-name convention on (almost) all members, the verb for that annotation class is
recorded with HIGH confidence; otherwise MEDIUM/LOW is reported.

Usage:
    python tools/build_api_catalog.py ANNOTATIONS_JSON LITERALS_TXT OUT_PREFIX

Writes OUT_PREFIX.json + OUT_PREFIX.csv. Deterministic, offline.
"""
from __future__ import annotations

import argparse
import collections
import csv
import json
import re

VERB_HINTS = [
    ("DELETE", re.compile(r"^(delete|remove|unfollow|unfavorite)", re.I)),
    ("PUT", re.compile(r"^(put|update|edit|set|upload|change)", re.I)),
    ("PATCH", re.compile(r"^(patch)", re.I)),
    ("POST", re.compile(r"^(post|create|send|add|submit|report|consume|confirm|run|execute|redeem|refresh|track|register|login|logout|join|start|finish|save|mark|publish|alias|identify)", re.I)),
    ("GET", re.compile(r"^(get|fetch|load|observe|list|read|is|has|download|query|render)", re.I)),
]
PATH_HINTS = [
    ("DELETE", re.compile(r"\{[a-zA-Z]+Id\}$")),
    ("POST", re.compile(r"/(consume|confirm|runfiles|runFiles|report|remixes|visits|deviceTokens|progress|settings/avatar|subscribe|login|token)$")),
    ("PUT", re.compile(r"/(settings|account/email|email)$")),
    ("GET", re.compile(r"/(next|latest|statistics|count|eta|completion|certificates|preview|branding|templates|userrank|friends|savedFiles)$")),
]


def walk(node):
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for v in node.values():
            yield from walk(v)
    elif isinstance(node, (list, tuple)):
        for v in node:
            yield from walk(v)


def method_name(owner: str) -> str:
    m = re.search(r"->([^(\s]+)\(", owner)
    if m:
        return m.group(1)
    m = re.search(r"->\s*([A-Za-z0-9_$]+)", owner)
    return m.group(1) if m else ""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("annotations_json")
    ap.add_argument("endpoint_literals_txt")
    ap.add_argument("out_prefix")
    args = ap.parse_args()

    rows = json.load(open(args.annotations_json))
    annotated = []
    for r in rows:
        strings = [s for s in walk(r["elements"]) if s.startswith("/")]
        if not strings:
            continue
        path = strings[0]
        name = method_name(r.get("owner", ""))
        hint = next((v for v, rx in VERB_HINTS if name and rx.match(name)), None)
        phint = next((v for v, rx in PATH_HINTS if rx.search(path)), None)
        annotated.append({
            "path": path,
            "annotation_class": r["type"],
            "owner": r.get("owner", ""),
            "method_name": name,
            "verb_from_method_name": hint,
            "verb_from_path_shape": phint,
            "scope": r.get("scope"),
        })

    # cross-tabulate annotation class -> declared verb evidence
    votes = collections.defaultdict(collections.Counter)
    for a in annotated:
        for key in (a["verb_from_method_name"], a["verb_from_path_shape"]):
            if key:
                votes[a["annotation_class"]][key] += 1
    mapping, mapping_confidence = {}, {}
    for ann, counter in votes.items():
        verb, n = counter.most_common(1)[0]
        total = sum(counter.values())
        share = n / total if total else 0
        mapping[ann] = verb
        mapping_confidence[ann] = "HIGH" if share >= 0.8 else ("MEDIUM" if share >= 0.55 else "LOW")

    for a in annotated:
        a["http_method"] = mapping.get(a["annotation_class"], "UNKNOWN")
        a["verb_confidence"] = mapping_confidence.get(a["annotation_class"], "LOW")
        a["evidence_class"] = "VERIFIED_STATIC"
        a["verb_status"] = "VERIFIED_STATIC_BY_ANNOTATION_MAPPING" if a["http_method"] != "UNKNOWN" else "UNKNOWN"
        a["path_params"] = re.findall(r"\{([a-zA-Z0-9_]+)\}", a["path"])

    literals = [l.strip() for l in open(args.endpoint_literals_txt) if l.strip().startswith("/")]
    annotated_paths = {a["path"] for a in annotated}
    unannotated = sorted(p for p in literals if p not in annotated_paths and not any(
        a["path"].rstrip("/") == p.rstrip("/") for a in annotated))
    third_party = sorted({a["owner"].split("->")[0] for a in annotated
                          if a["owner"].startswith("Lio/customer") or "gist" in a["owner"].lower()})
    mimo_api = [a for a in annotated
                if a["path"].startswith("/v") and not a["owner"].startswith("Lio/customer")]

    out = {
        "generated_by": "tools/build_api_catalog.py",
        "annotation_verb_mapping": {k: {"verb": v, "confidence": mapping_confidence[k],
                                        "votes": dict(votes[k])} for k, v in mapping.items()},
        "counts": {
            "endpoint_annotations": len(annotated),
            "mimo_api_endpoints": len(mimo_api),
            "literal_paths": len(literals),
            "literal_paths_without_annotation": len(unannotated),
            "third_party_interfaces": len(third_party),
        },
        "endpoints": sorted(annotated, key=lambda x: (x["path"], x["http_method"])),
        "unannotated_literals": unannotated,
        "notes": [
            "PATH = VERIFIED_STATIC (annotation value dereferenced from DEX).",
            "HTTP METHOD = VERIFIED_STATIC *relative to the annotation-class mapping*: the mapping itself is derived by cross-tabulation of method-name and path-shape evidence and must be read together with its confidence.",
            "Request/response bodies remain UNKNOWN unless a data contract exists (evidence/data-contracts.json).",
        ],
    }
    with open(args.out_prefix + ".json", "w") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)
    with open(args.out_prefix + ".csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["path", "http_method", "verb_confidence", "annotation_class",
                                           "method_name", "owner", "path_params", "evidence_class",
                                           "verb_status"])
        w.writeheader()
        for a in sorted(annotated, key=lambda x: (x["http_method"], x["path"])):
            row = {k: (json.dumps(v) if isinstance(v, list) else v) for k, v in a.items()}
            w.writerow({k: row.get(k, "") for k in w.fieldnames})

    print("annotation -> verb mapping:")
    for k, v in sorted(mapping.items()):
        print(f"  {k:12s} -> {v:7s} ({mapping_confidence[k]:6s}) votes={dict(votes[k])}")
    print(json.dumps(out["counts"], indent=1))
    print("unannotated literals:", unannotated)


if __name__ == "__main__":
    main()
