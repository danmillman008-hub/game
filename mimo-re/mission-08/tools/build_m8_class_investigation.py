#!/usr/bin/env python3
"""Mission 8 — Phase 1 class investigation builder.

Turns the Mission-7 deep-investigation queue (2,178 rows) into an *investigated*
register: per class it records what could actually be read, from which source
(decompiled Java and/or DEX instructions), which subsystems it touches, and a
mission-8 priority P0..P3 derived from a published rule table.

It never infers a behaviour from a class name alone: every flag is produced by an
observed superclass, interface, invoked package, or string literal.

Outputs (under 01_DEEP_CLASS_INVESTIGATION/)
  02_CLASS_CATEGORISATION.csv     one row per queue class
  03_PRIORITISED_QUEUE.json       counts, rule table, top lists
  evidence/PHASE1_CLASS_FACTS.jsonl  per-class fact record (machine evidence)

Usage
  python3 build_m8_class_investigation.py --dex-dir /tmp/x --src-dir /tmp/dad \
      --queue ../mission-07/01_CLASS_UNIVERSE/04_DEEP_INVESTIGATION_QUEUE.csv \
      --out ../mission-08/01_DEEP_CLASS_INVESTIGATION
"""
import argparse
import csv
import glob
import json
import os
import re
from collections import Counter, defaultdict

from androguard.core.dex import DEX

SIGNALS = {
    "firebase": ("Lcom/google/firebase/", "firebase"),
    "room": ("Landroidx/room/", "androidx.room"),
    "retrofit": ("Lretrofit2/",),
    "okhttp": ("Lokhttp3/",),
    "pusher": ("be.tramckrijte.workmanager", "com.pusher", "Lcom/pusher/"),
    "sse": ("Lokhttp3/EventSource", "event-source", "text/event-stream"),
    "rive": ("Lapp/rive/",),
    "webview": ("Landroid/webkit/",),
    "workmanager": ("Landroidx/work/",),
    "revenuecat": ("Lcom/revenuecat/",),
    "datastore": ("Landroidx/datastore/",),
    "glance": ("Landroidx/glance/",),
    "compose": ("Landroidx/compose/",),
    "coroutines": ("Lkotlinx/coroutines/",),
    "room_dao": ("Landroidx/room/Dao",),
    "gson": ("Lcom/google/gson/",),
    "hilt": ("Ldagger/",),
}

PRIORITY_RULES = [
    ("P0", "app-owned class in a mission-8 closure domain (auth, token, learner/progress, "
           "lesson engine/grading, AI tutor, SSE/WS/Pusher/FCM, DI root, navigation root)"),
    ("P1", "app-owned class that implements/persists/transmits state used by a P0 flow"),
    ("P2", "app-owned class with no observed cross-domain effect (UI helper, formatting, adapter)"),
    ("P3", "anonymous/synthetic/lambda class, or library class retained in the queue"),
]

DOMAIN_PATTERNS = [
    # ordered most-specific first; matched against dot/dollar-split tokens of the class name
    ("ai", ("aitutor", "prompt", "chat")),
    ("realtime", ("pusher", "socket", "sse", "eventsource", "streaming")),
    ("push", ("notification", "fcm", "messaging", "push")),
    ("auth", ("authentication", "auth", "login", "signup", "credential", "token", "session")),
    ("subscription", ("subscription", "purchase", "entitle", "paywall", "billing", "revenuecat",
                      "offering", "storekit")),
    ("navigation", ("navigation", "navigator", "deeplink", "route", "destination", "navgraph")),
    ("learner", ("learner", "progress", "streak", "mastery", "proficien", "league", "xp",
                 "gamification", "achievement")),
    ("lesson", ("lesson", "grading", "grade", "answer", "interactive", "exercise", "checker",
                "normalis", "parser", "ast", "dsl", "renderer")),
    ("di", ("di", "dagger", "inject", "component", "provider", "factory")),
    ("analytics", ("analytics", "amplitude", "segment", "appsflyer", "telemetry", "event")),
    ("storage", ("database", "dao", "entity", "room", "datastore", "preference", "cache",
                 "migration")),
    ("network", ("network", "interceptor", "retrofit", "okhttp", "endpoint", "http")),
    ("content", ("content", "chapter", "track", "course", "catalog", "curriculum", "module")),
]

def classify_domain(name, flags):
    tokens = [t for t in re.split(r"[.$]", name.lower()) if t]
    for dom, pats in DOMAIN_PATTERNS:
        for t in tokens:
            if any(t == p or t.startswith(p) for p in pats):
                return dom
    if "webview" in flags:
        return "lesson"
    if "compose" in flags or "rive" in flags:
        return "ui"
    if "room" in flags or "datastore" in flags:
        return "storage"
    return "other"


def load_pool(dex_dir):
    pool = {}
    for path in sorted(glob.glob(os.path.join(dex_dir, "*.dex"))):
        with open(path, "rb") as fh:
            dx = DEX(fh.read())
        for c in dx.get_classes():
            pool.setdefault(c.get_name()[1:-1].replace("/", "."), (path, c))
    return pool


def facts_for(cd):
    calls = Counter()
    strings = []
    insn = 0
    methods = []
    for m in cd.get_methods():
        code = m.get_code()
        n = 0
        if code:
            for ins in code.get_bc().get_instructions():
                n += 1
                op = ins.get_name()
                if op.startswith("invoke"):
                    out = ins.get_output()
                    if "L" in out:
                        m2 = re.search(r"L([\w/$]+);", out)
                        if m2:
                            calls[m2.group(1).replace("/", ".")] += 1
                elif "const-string" in op:
                    out = ins.get_output()
                    if '"' in out:
                        strings.append(out[out.find('"') + 1:out.rfind('"')][:200])
        insn += n
        methods.append({"name": m.get_name(), "desc": m.get_descriptor(), "insns": n})
    flags = set()
    blob = " ".join(list(calls)[:4000])
    for flagname, needles in SIGNALS.items():
        if any(nd in blob for nd in needles):
            flags.add(flagname)
    for s in strings:
        if "text/event-stream" in s:
            flags.add("sse")
        if "firebase" in s.lower():
            flags.add("firebase")
    return {
        "super": cd.get_superclassname(),
        "interfaces": list(cd.get_interfaces()),
        "fields": len(list(cd.get_fields())),
        "methods": methods,
        "insn_total": insn,
        "invoked_packages": calls.most_common(25),
        "strings_sample": sorted(set(strings))[:40],
        "flags": sorted(flags),
    }


COMPONENT_SUPERS = {
    "Landroid/app/Service;", "Landroidx/work/Worker;", "Landroidx/work/ListenableWorker;",
    "Landroid/app/Application;", "Landroid/content/BroadcastReceiver;", "Landroid/app/Activity;",
    "Landroidx/activity/ComponentActivity;", "Landroidx/fragment/app/Fragment;",
    "Landroidx/lifecycle/ViewModel;", "Landroidx/work/CoroutineWorker;",
}
TRIVIAL = {"<init>", "get", "set", "equals", "hashCode", "toString", "copy", "component1",
           "component2", "component3", "component4", "describeContents", "writeToParcel",
           "values", "valueOf", "getEntries", "a", "b", "c", "d"}
LOGIC_SUFFIX = ("repository", "datasource", "interceptor", "client", "api", "mapper", "usecase",
                "manager", "publisher", "handler", "provider", "coordinator", "engine",
                "controller", "parser", "renderer", "grader", "checker", "store", "cache")


def role_for(name, superclass, methods, insns):
    if "$" in name:
        return "lambda"
    if superclass in COMPONENT_SUPERS:
        return "component"
    if superclass == "Ljava/lang/Enum;":
        return "enum"
    names = [m["name"] for m in methods]
    if names and all(n in TRIVIAL or n.startswith("get") or n.startswith("set") or n.startswith("copy")
                     for n in names):
        return "value"
    low = name.rsplit(".", 1)[-1].lower()
    if low.endswith(LOGIC_SUFFIX):
        return "logic"
    return "logic" if insns > 40 else "value"


CORE_DOMAINS = ("auth", "learner", "lesson", "ai", "realtime", "push", "navigation", "di")


def priority_for(name, kind, flags, domain, role="logic"):
    if kind == "anonymous" or "$" in name or name.endswith(("Kt$1", "$1")):
        return "P3"
    if not name.startswith("com.getmimo"):
        return "P3"
    if role in ("enum", "value"):
        return "P2"
    if domain in CORE_DOMAINS:
        return "P0"
    if domain in ("network", "storage", "content", "subscription", "analytics"):
        return "P1"
    return "P1" if role in ("logic", "component") else "P2"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dex-dir", required=True)
    ap.add_argument("--src-dir", required=True)
    ap.add_argument("--queue", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()

    os.makedirs(os.path.join(a.out, "evidence"), exist_ok=True)
    with open(a.queue, newline="") as fh:
        queue = list(csv.DictReader(fh))
    if a.limit:
        queue = queue[:a.limit]
    with open(a.queue.replace("04_DEEP_INVESTIGATION_QUEUE.csv", "02_COMPLETE_CLASS_INVENTORY.csv"),
              newline="") as fh:
        inv = {r.get("class"): r for r in csv.DictReader(fh)}

    pool = load_pool(a.dex_dir)
    rows = []
    dist = Counter()
    catdist = Counter()
    facts_fh = open(os.path.join(a.out, "evidence", "PHASE1_CLASS_FACTS.jsonl"), "w")
    for q in queue:
        name = q["class"].strip()
        entry = pool.get(name)
        java = os.path.exists(os.path.join(a.src_dir, name + ".java"))
        if not entry:
            rows.append({"class": name, "priority": "P3", "category": "not_in_dex",
                         "source_basis": "none", "methods": 0, "insns": 0,
                         "flags": "", "domain": "other", "java": "0"})
            dist["P3"] += 1
            catdist["not_in_dex"] += 1
            continue
        path, cd = entry
        f = facts_for(cd)
        domain = classify_domain(name, set(f["flags"]))
        role = role_for(name, f["super"], f["methods"], f["insn_total"])
        prio = priority_for(name, q.get("kind", ""), set(f["flags"]), domain, role)
        cat = "app-owned" if name.startswith("com.getmimo") else (
            "androidx/library" if name.startswith(("androidx", "com.google", "kotlin", "okhttp",
                                                   "retrofit2", "com.facebook", "com.pusher",
                                                   "app.rive", "com.revenuecat")) else "obfuscated")
        rec = {
            "class": name,
            "dex": os.path.basename(path),
            "priority": prio,
            "category": cat,
            "domain": domain,
            "role": role,
            "source_basis": "decompiled_java+dex" if java else "dex_only",
            "java": "1" if java else "0",
            "methods": len(f["methods"]),
            "insns": f["insn_total"],
            "fields": f["fields"],
            "super": f["super"],
            "flags": ",".join(f["flags"]),
            "queue_reason": q.get("reason", ""),
            "inventory_kind": q.get("kind", ""),
        }
        rows.append(rec)
        dist[prio] += 1
        catdist[cat] += 1
        facts_fh.write(json.dumps({
            "class": name, "dex": os.path.basename(path), **f,
            "priority": prio, "domain": domain,
            "source_basis": rec["source_basis"],
            "inventory_row": inv.get(name),
        }, ensure_ascii=False) + "\n")

    facts_fh.close()
    header = ["class", "priority", "category", "domain", "role", "source_basis", "java", "methods",
              "insns", "fields", "super", "flags", "queue_reason", "inventory_kind", "dex"]
    with open(os.path.join(a.out, "02_CLASS_CATEGORISATION.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=header)
        w.writeheader()
        for r in sorted(rows, key=lambda r: (r["priority"], r["class"])):
            w.writerow({k: r.get(k, "") for k in header})

    summary = {
        "generated": "2026-11-01",
        "queue_rows": len(queue),
        "priority_distribution": dict(sorted(dist.items())),
        "category_distribution": dict(sorted(catdist.items())),
        "source_basis": dict(Counter(r["source_basis"] for r in rows)),
        "priority_rules": PRIORITY_RULES,
        "domain_distribution": dict(sorted(Counter(
            r["domain"] for r in rows
            if r["class"].startswith("com.getmimo") and "$" not in r["class"]).items())),
        "domain_distribution_scope": "app-owned, non-anonymous classes only",
        "role_distribution": dict(sorted(Counter(r.get("role", "") for r in rows).items())),
        "p0_classes": [r["class"] for r in rows if r["priority"] == "P0"][:400],
        "p0_count": sum(1 for r in rows if r["priority"] == "P0"),
        "p1_count": sum(1 for r in rows if r["priority"] == "P1"),
        "dex_only_p0": [r["class"] for r in rows if r["priority"] == "P0" and r["source_basis"] == "dex_only"],
    }
    with open(os.path.join(a.out, "03_PRIORITISED_QUEUE.json"), "w") as fh:
        json.dump(summary, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print(json.dumps({k: summary[k] for k in
                      ("queue_rows", "priority_distribution", "category_distribution",
                       "source_basis", "p0_count", "p1_count")}, indent=1))


if __name__ == "__main__":
    main()
