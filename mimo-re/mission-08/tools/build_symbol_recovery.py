#!/usr/bin/env python3
"""Mission 8 — Stage 1: symbol and lambda recovery.

Renaming removed the app's own class names from the binary but left Kotlin lambda binary names
intact. Those names are the primary evidence this tool uses:

    com.getmimo.data.source.remote.account.AccountRepository$deleteAccount$2
    └── original owner "…account.AccountRepository", original method "deleteAccount", lambda #2

For every *orphan* lambda (one whose owner is no longer a class_def) the tool answers three questions
with measured evidence, never with a guess:

  1. which renamed `class_def` is the owner?  → the short-named class the lambda invokes most often,
     aggregated per original owner (a single lambda is weak evidence; a family of lambdas is strong);
  2. which renamed method corresponds to the original method name? → the method(s) the lambda invokes
     on that owner;
  3. when nothing dominates, the lambda is reported as UNRESOLVED with the competing candidates.

Outputs (01_SYMBOL_RECOVERY/)
  ORPHAN_LAMBDA_REGISTER.csv      one row per orphan lambda
  LAMBDA_ENCLOSURE_MAP.json       original owner/method → candidate renamed owner(s) + counts
  ORIGINAL_METHOD_NAME_MAPPINGS.csv  original method → renamed method, per recovered owner
  RECOVERY_EVIDENCE.json          per-lambda instruction evidence (class + method + call count)
  UNRESOLVED_SYMBOLS.csv          lambdas with no dominant candidate

Usage
  python3 build_symbol_recovery.py --dex-dir /tmp/x --out ../01_SYMBOL_RECOVERY
"""
import argparse
import csv
import glob
import json
import os
import re
from collections import Counter, defaultdict

from androguard.core.dex import DEX

# method names that carry no semantic information in Kotlin lambdas
NOISE = {"invoke", "invokeSuspend", "<init>", "create", "get", "set", "toString", "hashCode", "equals",
         "getClass", "iterator", "hasNext", "next", "append", "getOrCreateKotlinClass", "cast",
         "valueOf", "booleanValue", "intValue", "longValue", "ordinal", "name", "getEntries"}
CLUSTERS = [
    ("authentication", ("auth", "login", "signup", "account", "session", "credential", "token", "logout",
                        "profile", "username", "email", "password", "google", "facebook", "anonymous")),
    ("content", ("content", "track", "course", "chapter", "lesson", "catalog", "curriculum", "module",
                 "publish", "snippet", "file")),
    ("lesson-engine", ("parser", "ast", "renderer", "grading", "grade", "answer", "interaction", "dsl",
                       "exercise", "checker", "normalis", "compile", "editor", "terminal", "execute")),
    ("learner-progress", ("progress", "learner", "streak", "mastery", "xp", "level", "league", "goal",
                          "achievement", "gamification", "leaderboard", "ranking", "reward")),
    ("persistence", ("database", "dao", "room", "entity", "cache", "store", "preferences", "datastore",
                     "outbox", "migration")),
    ("ai-tutor", ("aitutor", "chat", "prompt", "message", "conversation", "assistant")),
    ("realtime", ("pusher", "socket", "sse", "event", "stream", "notification", "push", "fcm")),
    ("subscription", ("subscription", "purchase", "entitle", "paywall", "billing", "offering", "discount",
                      "revenuecat", "product")),
    ("analytics", ("analytics", "event", "track_", "amplitude", "appsflyer", "adjust", "telemetry",
                   "remoteconfig", "abtest", "experiment")),
    ("ui-navigation", ("fragment", "activity", "view", "adapter", "navigation", "navigator", "screen",
                       "dialog", "bottom", "compose", "animation", "rive", "theme", "widget")),
    ("background", ("worker", "work", "scheduler", "alarm", "service", "receiver", "sync", "job")),
]


def parse_lambda(name, existing):
    """Return (root_owner, method_hint) or None.

    The *root* owner is the text before the first `$`: it is the class the Kotlin compiler
    generated the lambda for (nested lambdas keep the whole chain in later segments). A lambda is
    an orphan when that root class is not a class_def any more.
    """
    parts = name.split("$")
    if len(parts) < 2:
        return None
    root = parts[0]
    if root in existing:
        return None
    idx = len(parts)
    while idx > 1 and parts[idx - 1].isdigit():
        idx -= 1
    method = parts[idx - 1] if idx > 1 else None
    if method is None or not re.match(r"^[a-zA-Z_][\w]*$", method):
        return None
    return root, method


def cluster_for(owner, method):
    low = (owner + "." + method).lower()
    for name, keys in CLUSTERS:
        if any(k.strip("_") in low for k in keys):
            return name
    return "unknown"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dex-dir", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)

    pool = {}
    for path in sorted(glob.glob(os.path.join(a.dex_dir, "*.dex"))):
        with open(path, "rb") as fh:
            dx = DEX(fh.read())
        for c in dx.get_classes():
            pool[c.get_name()[1:-1].replace("/", ".")] = (os.path.basename(path), c)
    names = set(pool)

    lambdas = {}
    for n in names:
        if not n.startswith("com.getmimo") or "$" not in n:
            continue
        parsed = parse_lambda(n, names)
        if not parsed:
            continue
        owner, method = parsed
        if owner in names:            # owner still exists: not an orphan
            continue
        lambdas[n] = {"owner": owner, "method": method}

    # per original owner: which renamed classes does the lambda family invoke?
    family_targets = defaultdict(Counter)
    lambda_detail = {}
    for lam, meta in lambdas.items():
        owner_pkg = meta["owner"].rsplit(".", 1)[0]
        cd = pool[lam][1]
        targets = Counter()
        methods_by_target = defaultdict(Counter)
        insns = 0
        for m in cd.get_methods():
            code = m.get_code()
            if not code:
                continue
            for ins in code.get_bc().get_instructions():
                insns += 1
                if not ins.get_name().startswith("invoke"):
                    continue
                out = ins.get_output()
                t = re.search(r"L([\w/$]+);->([\w<>$]+)", out)
                if not t:
                    continue
                cls = t.group(1).replace("/", ".")
                meth = t.group(2)
                if cls.startswith("java.") or cls.startswith("kotlin.") or cls.startswith("android"):
                    continue
                if meth in NOISE:
                    continue
                if len(cls.rsplit(".", 1)[-1]) > 2:
                    continue          # the renamed owner always has a short simple name
                if not (cls == owner_pkg or cls.startswith(owner_pkg + ".")):
                    continue          # renaming preserved the package; a cross-package callee
                                      # (Orbit DSL, logger, DI helper) is not the owner
                targets[cls] += 1
                methods_by_target[cls][meth] += 1
        lambda_detail[lam] = {"targets": targets, "methods": methods_by_target, "insns": insns}
        for cls, n in targets.items():
            family_targets[meta["owner"]][cls] += n

    # dominant renamed owner per original owner
    enclosure = {}
    for owner, counter in family_targets.items():
        ranked = counter.most_common(6)
        total = sum(counter.values()) or 1
        fam_lambdas = [l for l, meta in lambdas.items() if meta["owner"] == owner]
        best_cls, best_n = ranked[0] if ranked else (None, 0)
        share = best_n / total
        if best_cls is None:
            conf = "UNRESOLVED"
        elif len(fam_lambdas) >= 3 and share >= 0.6:
            conf = "HIGH"
        elif len(fam_lambdas) >= 2 and share >= 0.45:
            conf = "MEDIUM"
        elif len(fam_lambdas) == 1 and best_n >= 2:
            conf = "MEDIUM"
        else:
            conf = "LOW"
        enclosure[owner] = {
            "original_owner": owner,
            "lambda_count": len(fam_lambdas),
            "candidates": [{"class": c, "invokes": n} for c, n in ranked],
            "dominant": best_cls,
            "dominant_share": round(share, 3),
            "confidence": conf,
            "cluster": cluster_for(owner, ""),
        }

    # method-name mappings: original method → renamed method on the dominant class
    mappings = []
    for lam, meta in sorted(lambdas.items()):
        enc = enclosure.get(meta["owner"], {})
        dom = enc.get("dominant")
        detail = lambda_detail[lam]
        if not dom:
            continue
        cand = detail["methods"].get(dom, Counter())
        real = [(m, n) for m, n in cand.most_common(4) if m not in NOISE]
        if not real:
            continue
        mappings.append({
            "lambda": lam,
            "original_owner": meta["owner"],
            "original_method": meta["method"],
            "renamed_owner": dom,
            "renamed_method_candidates": ";".join(f"{m}({n})" for m, n in real),
            "confidence": "HIGH" if len(real) == 1 else ("MEDIUM" if real else "UNRESOLVED"),
            "cluster": cluster_for(meta["owner"], meta["method"]),
        })

    # write registers
    with open(os.path.join(a.out, "ORPHAN_LAMBDA_REGISTER.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["lambda", "original_owner", "method_hint", "renamed_owner", "enclosure_confidence",
                    "insns", "invoked_targets", "cluster"])
        for lam, meta in sorted(lambdas.items()):
            enc = enclosure.get(meta["owner"], {})
            w.writerow([lam, meta["owner"], meta["method"], enc.get("dominant", ""),
                        enc.get("confidence", ""), lambda_detail[lam]["insns"],
                        len(lambda_detail[lam]["targets"]), enc.get("cluster", "")])

    with open(os.path.join(a.out, "ORIGINAL_METHOD_NAME_MAPPINGS.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["original_owner", "original_method", "renamed_owner",
                                           "renamed_method_candidates", "confidence", "cluster",
                                           "lambda"])
        w.writeheader()
        for m in sorted(mappings, key=lambda x: (x["original_owner"], x["original_method"], x["lambda"])):
            w.writerow(m)

    with open(os.path.join(a.out, "LAMBDA_ENCLOSURE_MAP.json"), "w") as fh:
        json.dump({"generated": "2026-11-01", "owners": enclosure}, fh, indent=1, sort_keys=True)

    unresolved = [l for l, meta in lambdas.items()
                  if enclosure.get(meta["owner"], {}).get("confidence") in ("UNRESOLVED", "LOW")]
    with open(os.path.join(a.out, "UNRESOLVED_SYMBOLS.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["lambda", "original_owner", "method_hint", "reason", "competing_candidates"])
        for lam in sorted(unresolved):
            meta = lambdas[lam]
            enc = enclosure.get(meta["owner"], {})
            w.writerow([lam, meta["owner"], meta["method"], enc.get("confidence", "UNRESOLVED"),
                        ";".join(c["class"] for c in enc.get("candidates", [])[:4])])

    evidence = {lam: {"insns": d["insns"],
                      "top_targets": d["targets"].most_common(5),
                      "methods_by_target": {k: v.most_common(4) for k, v in
                                            list(d["methods"].items())[:5]}}
                for lam, d in list(lambda_detail.items())[:400]}
    with open(os.path.join(a.out, "RECOVERY_EVIDENCE.json"), "w") as fh:
        json.dump({"note": "first 400 lambdas; regenerate for the full set",
                   "evidence": evidence}, fh, indent=1)

    # renamed class register: short-named app classes, annotated with the owners they were matched to
    owner_of = defaultdict(list)
    for owner, enc in enclosure.items():
        if enc.get("dominant"):
            owner_of[enc["dominant"]].append({"original_owner": owner,
                                              "confidence": enc["confidence"],
                                              "share": enc["dominant_share"],
                                              "lambdas": enc["lambda_count"]})
    renamed = []
    for n, (dexfile, cd) in pool.items():
        if n.startswith("com.getmimo") or len(n.rsplit(".", 1)[-1]) > 2:
            continue
        touched = False
        for m in cd.get_methods():
            code = m.get_code()
            if not code:
                continue
            for ins in code.get_bc().get_instructions():
                if "Lcom/getmimo/" in ins.get_output():
                    touched = True
                    break
            if touched:
                break
        if not touched:
            continue
        owners = owner_of.get(n, [])
        renamed.append({
            "class": n,
            "dex": dexfile,
            "super": cd.get_superclassname()[1:-1].replace("/", "."),
            "interfaces": ";".join(i[1:-1].replace("/", ".") for i in cd.get_interfaces())[:200],
            "methods": len(list(cd.get_methods())),
            "fields": len(list(cd.get_fields())),
            "recovered_owners": ";".join(o["original_owner"] for o in owners)[:300],
            "owner_confidence": ";".join(f'{o["original_owner"].rsplit(".",1)[-1]}:{o["confidence"]}'
                                         for o in owners)[:200],
            "cluster": next((x["cluster"] for o in owners
                             for x in [enclosure[o["original_owner"]]] if x), "unknown"),
        })
    with open(os.path.join(a.out, "RENAMED_CLASS_REGISTER.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(renamed[0].keys()))
        w.writeheader()
        w.writerows(sorted(renamed, key=lambda r: r["class"]))

    clusters = defaultdict(lambda: {"owners": [], "classes": []})
    for owner, enc in enclosure.items():
        cl = enc.get("cluster") or "unknown"
        clusters[cl]["owners"].append({"original_owner": owner, "dominant": enc.get("dominant"),
                                       "confidence": enc.get("confidence"),
                                       "share": enc.get("dominant_share"),
                                       "lambdas": enc.get("lambda_count")})
        if enc.get("dominant"):
            clusters[cl]["classes"].append(enc["dominant"])
    for cl in clusters:
        clusters[cl]["classes"] = sorted(set(clusters[cl]["classes"]))
        clusters[cl]["owners"].sort(key=lambda o: -o["lambdas"])
    with open(os.path.join(a.out, "COMPONENT_CLUSTERS.json"), "w") as fh:
        json.dump({"generated": "2026-11-01",
                   "note": "clusters are derived from the recovered original owner names; a class appears "
                           "under a cluster only when an owner lambda family votes for it",
                   "clusters": clusters}, fh, indent=1, sort_keys=True)

    conf = Counter(e["confidence"] for e in enclosure.values())
    clusters = Counter(e["cluster"] for e in enclosure.values())
    print(json.dumps({"orphan_lambdas": len(lambdas), "original_owners": len(enclosure),
                      "enclosure_confidence": dict(conf),
                      "clusters": dict(clusters),
                      "unresolved_lambdas": len(unresolved),
                      "method_mappings": len(mappings)}, indent=1))


if __name__ == "__main__":
    main()
