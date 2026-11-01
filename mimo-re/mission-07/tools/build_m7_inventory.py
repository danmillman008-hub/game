#!/usr/bin/env python3
"""MISSION-07 — class/method universe + investigation queue builder.

Inputs : dex dir (/tmp/x), decompiled tree (/tmp/dad)
Outputs: 01_CLASS_UNIVERSE/02_COMPLETE_CLASS_INVENTORY.csv
         01_CLASS_UNIVERSE/03_METHOD_INVENTORY.csv
         01_CLASS_UNIVERSE/04_DEEP_INVESTIGATION_QUEUE.csv
         01_CLASS_UNIVERSE/05_OBFUSCATED_SYMBOL_MAP.json
Deterministic; no network; read-only.
"""
import argparse, csv, glob, json, os, re, sys

APP_PREFIXES = ("com.getmimo.",)
LIB_PREFIXES = ("androidx.", "android.", "kotlin.", "kotlinx.", "com.google.", "okhttp3.", "retrofit2.",
                "io.reactivex", "io.sentry", "com.adjust.", "com.pusher.", "app.rive.", "com.facebook.",
                "com.android.", "org.jetbrains.", "com.squareup.", "dagger.", "javax.", "io.coil-kt")

def classify(name: str) -> str:
    if name.startswith("bin.ghost"):
        return "target-modified-base"
    if any(name.startswith(p) for p in APP_PREFIXES):
        if "$" in name and re.search(r"\$\d+$", name):
            return "app-anonymous"
        return "app"
    if any(name.startswith(p) for p in LIB_PREFIXES):
        return "library"
    if re.match(r"^[a-z]{1,3}\d?\.[a-z]", name) or re.match(r"^[a-z]{1,3}\.[a-z0-9]{1,3}$", name):
        return "obfuscated-app-candidate"
    return "other"

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dex-dir", default="/tmp/x")
    ap.add_argument("--src", default="/tmp/dad")
    ap.add_argument("--out-dir", default="01_CLASS_UNIVERSE")
    a = ap.parse_args()
    from androguard.core.dex import DEX
    classes = {}
    for f in sorted(glob.glob(os.path.join(a.dex_dir, "*.dex"))):
        dex = DEX(open(f, "rb").read())
        for c in dex.get_classes():
            n = c.get_name()[1:-1].replace("/", ".")
            classes[n] = {"dex": os.path.basename(f), "methods": len(c.get_methods()),
                          "fields": len(c.get_fields()), "super": c.get_superclassname()[1:-1].replace("/", ".") if c.get_superclassname() else ""}
    decompiled = {os.path.basename(p)[:-5]: p for p in glob.glob(os.path.join(a.src, "*.java"))}
    os.makedirs(a.out_dir, exist_ok=True)
    kinds = {}
    with open(os.path.join(a.out_dir, "02_COMPLETE_CLASS_INVENTORY.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["class", "kind", "dex", "methods", "fields", "superclass", "decompiled"])
        for n in sorted(classes):
            k = classify(n)
            kinds[k] = kinds.get(k, 0) + 1
            w.writerow([n, k, classes[n]["dex"], classes[n]["methods"], classes[n]["fields"], classes[n]["super"], int(n in decompiled)])
    METHOD = re.compile(r"^\s{4}(?:public|private|protected|static|final|synthetic|abstract|\s)*[\w.$<>\[\], ?]+\s+([\w$<>]+)\s*\(")
    with open(os.path.join(a.out_dir, "03_METHOD_INVENTORY.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["class", "method", "file", "line", "signature_line"])
        total = 0
        for n in sorted(decompiled):
            if n not in classes:
                continue
            for i, line in enumerate(open(decompiled[n], encoding="utf-8", errors="replace"), 1):
                m = METHOD.match(line)
                if m and m.group(1) not in ("if", "for", "while", "switch", "catch", "return"):
                    w.writerow([n, m.group(1), os.path.basename(decompiled[n]), i, line.strip()[:160]])
                    total += 1
    hotspots = ["analytics", "lesson.interactive", "aitutor", "room", "sync", "network", "auth", "subscription",
                "keys", "leaderboard", "onboarding", "paywall", "config", "worker", "notification", "rive"]
    with open(os.path.join(a.out_dir, "04_DEEP_INVESTIGATION_QUEUE.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["priority", "class", "kind", "methods", "decompiled", "reason"])
        rows = []
        for n, meta in classes.items():
            if classify(n) not in ("app", "obfuscated-app-candidate", "app-anonymous", "target-modified-base"):
                continue
            low = n.lower()
            pri = 0
            reason = ""
            for i, h in enumerate(hotspots):
                if h in low:
                    pri = i + 1
                    reason = "hotspot:" + h
                    break
            if pri == 0 and meta["methods"] >= 25:
                pri = 90
                reason = "large-class"
            if pri:
                rows.append((pri, n, classify(n), meta["methods"], int(n in decompiled), reason))
        for r in sorted(rows):
            w.writerow(r)
    SYMBOLS = {
      "ae.m": {"responsibility":"dependency-injection switch (127 cases), builds OkHttp/Retrofit/DB/analytics graph","methods":["<init>"],"evidence":"mission-06/evidence/DI_GRAPH.json"},
      "te.a": {"responsibility":"parser for <code> module incl. interactions/output/collapsibleLines","methods":["a","b"]},
      "te.b": {"responsibility":"parser for <database>/<tables>","methods":["a"]},
      "te.c": {"responsibility":"module dispatcher + <img> parser","methods":["a","b"]},
      "te.d": {"responsibility":"<p> paragraph + inline HTML (a,br,span,em,strong,code)","methods":["a","b","c","e"]},
      "te.e": {"responsibility":"<selection>/<item> parser","methods":["a"]},
      "te.f": {"responsibility":"<table>/<row>/<header>/<data> parser","methods":["a"]},
      "te.g": {"responsibility":"<webview> parser","methods":["a"]},
      "qm.i": {"responsibility":"grader: exact then normalised comparison","methods":["<init>","a"]},
      "qm.d": {"responsibility":"verdict visitor over interaction kinds","methods":["a"]},
      "base.c": {"responsibility":"interactive lesson base ViewModel: state, verdicts, progress writes","methods":["H","U","V","W","X","Z","a0","f0","g0"]},
      "hg.e": {"responsibility":"connectivity interceptor -> NoConnectionException","methods":["intercept"]},
      "fh.a": {"responsibility":"Authorization: Bearer interceptor","methods":["intercept"]},
      "fh.b": {"responsibility":"User-Agent interceptor (Mimo/9.35 Android/<release>)","methods":["intercept"]},
      "pg.a": {"responsibility":"WebSocket listener for wss://api.mimo.org/v1/run/socket","methods":["onOpen","onMessage","onFailure","onClosed"]},
      "f9.j": {"responsibility":"Pusher client/auth using API host","methods":["<init>"]},
      "com.getmimo.analytics.a": {"responsibility":"analytics singleton: Firebase logEvent + Adjust + FCM token + AB-test groups","methods":["a","b","e","f"]},
      "ge.j": {"responsibility":"analytics event value object (name, index)","methods":["<init>"]},
      "com.getmimo.data.source.remote.keys.a": {"responsibility":"DefaultKeysRepository: fetch keys + consumeUserKey","methods":["consumeUserKey"]},
      "com.getmimo.data.source.local.aitutor.AiTutorRepository": {"responsibility":"AI tutor SSE transport","methods":["sendMessage"]},
      "ri.c": {"responsibility":"token/session holder (used by fh.a via d(0))","methods":[]},
    }
    json.dump(SYMBOLS, open(os.path.join(a.out_dir, "05_OBFUSCATED_SYMBOL_MAP.json"), "w"), indent=1)
    print("classes", len(classes), "kinds", kinds)
    print("decompiled", len(decompiled), "methods indexed", total)
    return 0

if __name__ == "__main__":
    sys.exit(main())
