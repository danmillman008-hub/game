#!/usr/bin/env python3
"""DSL census: tag/attribute/value domains across a Mimo language pack.
Reads <pack>/tracks/*.json and walks lesson content strings with a tolerant
tag tokenizer. No APK access, read-only.
"""
import json, os, re, sys, csv, collections

TAG_RE = re.compile(r"<\s*/?\s*([A-Za-z][A-Za-z0-9_-]*)")
ATTR_RE = re.compile(r"([A-Za-z_][A-Za-z0-9_:-]*)\s*=\s*\"([^\"]*)\"")
VOID = {"br", "img", "hr", "input", "tab", "file"}

def iter_lessons(packdir):
    for fn in sorted(os.listdir(packdir)):
        if not fn.endswith(".json"):
            continue
        path = os.path.join(packdir, fn)
        doc = json.load(open(path, encoding="utf-8"))
        tuts = doc.get("tutorials")
        if tuts is None and isinstance(doc.get("tutorial"), dict):
            tuts = [doc["tutorial"]]
        for t in tuts or []:
            for ch in t.get("chapters", []):
                for les in ch.get("lessons", []):
                    yield path, t, ch, les

def main(packdir, outdir):
    tag_counts = collections.Counter()
    opens = collections.Counter()
    closes = collections.Counter()
    attr_sets = collections.defaultdict(collections.Counter)   # tag -> attr -> count
    values = collections.defaultdict(collections.Counter)     # "tag@attr" -> value
    roots = collections.Counter()
    depth_max = collections.Counter()
    text_chars = collections.Counter()
    nodes = 0
    for path, t, ch, les in iter_lessons(packdir):
        for field in ("interactiveContent", "hardModeContent"):
            s = les.get(field)
            if not isinstance(s, str) or not s:
                continue
            m = TAG_RE.search(s)
            if m:
                roots[m.group(1)] += 1
            stack = 0
            for mm in TAG_RE.finditer(s):
                name = mm.group(1)
                closing = s[mm.start():mm.end()].find("/") != -1
                tag_counts[name] += 1
                nodes += 1
                if closing:
                    closes[name] += 1
                else:
                    opens[name] += 1
                if not closing and name not in VOID:
                    stack += 1
                    depth_max[name] = max(depth_max[name], stack)
                elif closing:
                    stack = max(0, stack - 1)
                # attributes inside this tag
                end = s.find(">", mm.start())
                chunk = s[mm.start(): end if end != -1 else mm.start() + 400]
                for a, v in ATTR_RE.findall(chunk):
                    attr_sets[name][a] += 1
                    if len(v) <= 40:
                        values[f"{name}@{a}"][v] += 1
        ec = les.get("executableContent")
        if isinstance(ec, dict):
            for f in ec.get("files", []) or []:
                text_chars["executable_files"] += 1
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "DSL_TAG_CENSUS.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(["tag", "occurrences", "open_tags", "close_tags", "distinct_attributes", "attributes", "max_depth", "is_root"])
        for tag, c in tag_counts.most_common():
            w.writerow([tag, c, opens[tag], closes[tag], len(attr_sets[tag]), " ".join(sorted(attr_sets[tag])), depth_max.get(tag, 0), "yes" if roots.get(tag) else ""])
    with open(os.path.join(outdir, "DSL_ATTRIBUTE_MATRIX.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(["tag", "attribute", "occurrences", "distinct_values", "example_values"])
        for tag in tag_counts:
            for a, c in attr_sets[tag].most_common():
                vals = values.get(f"{tag}@{a}", collections.Counter())
                ex = " | ".join(v for v, _ in vals.most_common(4))
                w.writerow([tag, a, c, len(vals), ex[:180]])
    with open(os.path.join(outdir, "DSL_VALUE_DOMAINS.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(["tag", "attribute", "value", "occurrences"])
        for k, vals in sorted(values.items()):
            tag, a = k.split("@", 1)
            for v, c in vals.most_common(40):
                w.writerow([tag, a, v, c])
    summary = {
        "pack": packdir, "tag_occurrences": nodes, "distinct_tags": len(tag_counts),
        "tags": {k: v for k, v in tag_counts.most_common()},
        "elements": {k: v for k, v in opens.most_common()},
        "roots": dict(roots),
    }
    json.dump(summary, open(os.path.join(outdir, "DSL_SUMMARY.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"tags: {len(tag_counts)}  occurrences: {nodes}")
    for tag, c in tag_counts.most_common():
        print(f"  {tag:14s} {c:>9} attrs={','.join(sorted(attr_sets[tag]))[:110]}")
    print("roots:", dict(roots))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
