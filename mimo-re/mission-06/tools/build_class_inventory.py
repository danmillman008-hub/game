#!/usr/bin/env python3
"""MISSION-06 Phase 1 — class/method inventory + obfuscation map + graphs.

Outputs under 01_APK_AND_ARCHITECTURE/:
  06_CLASS_METHOD_INVENTORY.csv  every DEX class with package, method count, recovered-source flag
  05_OBFUSCATION_MAP.json        curated obfuscated-name -> responsibility table (evidence per row)
  07_DEPENDENCY_GRAPH.json       construction/wiring edges (from the DI monolith + infrastructure)
  08_CALL_GRAPH.json             curated call edges across the lesson/progress/network spine
Deterministic; reads DEX and the decompiled tree only.
"""
from __future__ import annotations

import csv
import glob
import json
import os
import pathlib
import sys

OUT = pathlib.Path("/home/user/game/mimo-re/mission-06/01_APK_AND_ARCHITECTURE")
DAD = pathlib.Path("/tmp/dad")

# --------------------------------------------------------------------------- obfuscation map
# Every row: obfuscated name, recovered responsibility, key members, evidence, confidence.
OBF = [
 ("te.a", "interactive lesson XML parser: <code> module, interactions, output, collapsibleLines",
  "a(XmlPullParser)->LessonModule$Code, b(...)->content/text", "te.a.java (require/attribute reads); PARSER_GRAMMAR.json", "VERIFIED_STATIC"),
 ("te.b", "<database> module parser: <database><tables><table>", "a()->LessonModule$Database", "te.b.java", "VERIFIED_STATIC"),
 ("te.c", "module dispatcher (html/body/p/code/selection/img/webview/database) + <img> parser",
  "a()->LessonModule$Image, b()->dispatch", "te.c.java", "VERIFIED_STATIC"),
 ("te.d", "paragraph/inline HTML parser: <p>, <a href>, <br>, <span>, inline <code>",
  "a()->LessonModule$Paragraph, b/c/d/e inline handlers", "te.d.java", "VERIFIED_STATIC"),
 ("te.e", "<selection>/<item> parser", "a()->LessonModule$Selection", "te.e.java; attrs iscode/correct", "VERIFIED_STATIC"),
 ("te.f", "<table>/<row>/<header>/<data> parser", "a()->Table", "te.f.java", "VERIFIED_STATIC"),
 ("te.g", "<webview> parser", "a()->LessonModule$Webview", "te.g.java; attrs version/style/interaction/content", "VERIFIED_STATIC"),
 ("qm.d", "ValidatedInput lesson view model", "E(), a0(), L()", "qm.d.java extends base.c", "VERIFIED_STATIC"),
 ("qm.e/qm.f/qm.g", "closed verdict set: Correct / CorrectPartialMatch(user,expected) / Incorrect", "fields h,i", "qm.e/f/g.java", "VERIFIED_STATIC"),
 ("qm.h", "validated-input render state (answer, prefix, suffix)", "ctor(String,CharSequence,CharSequence)", "qm.h.java", "VERIFIED_STATIC"),
 ("qm.i", "answer normaliser", "a(String)", "qm.i.java: lowercase US + keep letter/digit/'<'/'.'", "VERIFIED_STATIC"),
 ("ae.m", "Dagger/Hilt component factory: 127 provider cases (DI graph, OkHttp, API base URL, Gson, Room)",
  "a() per case", "ae.m.java; DI_GRAPH.json", "VERIFIED_STATIC"),
 ("ku.a", "session/token store used by the auth interceptors (token accessor d(int))",
  "d(int)", "fh.a.java calls ku.a.d(0); ae.m wiring", "INFERRED"),
 ("fh.a", "OkHttp interceptor: adds 'Authorization: Bearer <token>' when the endpoint carries @ri/b",
  "intercept()", "fh.a.java", "VERIFIED_STATIC"),
 ("fh.b", "OkHttp interceptor: device/User-Agent header from Build.MANUFACTURER+MODEL", "intercept()", "fh.b.java", "VERIFIED_STATIC"),
 ("hg.e", "OkHttp interceptor: fail-fast offline guard throwing NoConnectionException", "intercept()", "hg.e.java", "VERIFIED_STATIC"),
 ("com.getmimo.network.a", "ConnectivityManager wrapper: online iff transport WIFI(1) or CELLULAR(0)",
  "a(), b()", "com.getmimo.network.a.java", "VERIFIED_STATIC"),
 ("com.getmimo.network.b", "Flow-based online monitor", "ctor", "com.getmimo.network.b.java", "VERIFIED_STATIC"),
 ("pg.a", "code-execution WebSocket listener (wss://api.mimo.org/v1/run/socket, bearer subprotocol)",
  "a(), onMessage/onOpen", "pg.a.java", "VERIFIED_STATIC"),
 ("cg.b", "Room generated INSERT statements for the three tables", "i(statement,entity)", "cg.b.java", "VERIFIED_STATIC"),
 ("cg.c", "Room generated UPDATE statements", "h(statement,entity)", "cg.c.java", "VERIFIED_STATIC"),
 ("np.h", "analytics dispatch handle (not recovered as source; constructed in DI case 2)", "unknown", "ae.m case 2", "NOT_RECOVERED"),
 ("llg.d", "response type of GET /v2/client-config (class not recovered)", "unknown", "API_CATALOG_V2.csv", "NOT_RECOVERED"),
 ("d70.b", "kotlin.coroutines.Continuation (generic carries the suspend return type)", "resumeWith", "method Signature annotations", "VERIFIED_STATIC"),
 ("z60.q", "kotlin.Unit", "-", "API responses typed Lz60/q;", "VERIFIED_STATIC"),
 ("ge0.o0", "HTTP response wrapper (isSuccessful/body/errorBody) used by non-suspending calls", "unknown", "API_CATALOG_V2.csv generic args", "INFERRED"),
 ("ri.b", "marker annotation: endpoint requires bearer auth (read by fh.a)", "-", "fh.a.java", "VERIFIED_STATIC"),
 ("ie0/f", "HTTP verb annotation -> GET (28 endpoints, no body params)", "value", "ANNOTATIONS_V2.csv + body-rule check", "INFERRED"),
 ("ie0/o", "HTTP verb annotation -> POST (24 endpoints, 15 with body)", "value", "idem", "INFERRED"),
 ("ie0/n", "HTTP verb annotation -> PATCH (4 endpoints, all with body)", "value", "idem", "INFERRED"),
 ("ie0/b", "HTTP verb annotation -> DELETE (4 endpoints, no body, paired with add operations)", "value", "idem", "INFERRED"),
 ("ie0/p", "HTTP verb annotation -> PUT (2 endpoints)", "value", "idem", "INFERRED"),
 ("ie0/k", "@Headers literal(s), e.g. Content-Type: application/json", "value[]", "ANNOTATIONS_V2.csv", "VERIFIED_STATIC"),
 ("ie0/w", "unidentified method annotation present on 2 endpoints", "value", "ANNOTATIONS_V2.csv", "UNKNOWN"),
 ("bin.ghost.YRF", "native-driven blocking dialog (10 s auto dismiss) backed by libyrf.so", "execute(), logo(), dpToPx()", "bin.ghost.YRF.java; libyrf.so symbols", "VERIFIED_STATIC (structure)"),
]


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    from loguru import logger as lg
    lg.remove()
    from androguard.core.dex import DEX

    recovered = {p.stem for p in DAD.glob("*.java")}
    rows = []
    for path in sorted(glob.glob("/tmp/x/classes*.dex")):
        dex = path.split("/")[-1]
        d = DEX(open(path, "rb").read())
        for c in d.get_classes():
            name = c.get_name()
            cls = name[1:-1] if name.startswith("L") and name.endswith(";") else name
            pkg = cls.rsplit("/", 1)[0].replace("/", ".") if "/" in cls else "(default)"
            rows.append({
                "class": cls,
                "package": pkg,
                "top_package": pkg.split(".")[0],
                "dex": dex,
                "methods": len(c.get_methods()),
                "fields": len(c.get_fields()),
                "source_recovered": cls.replace("/", ".") in recovered,
            })
    rows.sort(key=lambda r: (r["top_package"], r["class"]))
    with open(OUT / "06_CLASS_METHOD_INVENTORY.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    json.dump({"method": "curated; each row cites the source artifact that establishes it",
               "entries": [dict(zip(["obfuscated", "responsibility", "members", "evidence", "confidence"], r))
                           for r in OBF]},
              open(OUT / "05_OBFUSCATION_MAP.json", "w", encoding="utf-8"), indent=1)

    di = json.load(open(pathlib.Path(__file__).resolve().parents[1] / "evidence" / "DI_GRAPH.json"))
    deps = {"source": "evidence/DI_GRAPH.json (ae.m provider cases) + infrastructure reads",
            "nodes": [], "edges": []}
    seen = set()
    for c in di["providers"]:
        for prov in c["provides"]:
            t = prov
            if t not in seen:
                seen.add(t)
                deps["nodes"].append({"id": t, "provided_by_case": c["case"]})
    edges = [
        ("ae.m", "okhttp3.OkHttpClient", "constructs", "case 20: interceptor chain + 20s/30s timeouts"),
        ("okhttp3.OkHttpClient", "hg.e", "chains", "offline guard"),
        ("okhttp3.OkHttpClient", "fh.b", "chains", "device header"),
        ("okhttp3.OkHttpClient", "fh.a", "chains", "bearer token for @ri/b endpoints"),
        ("ae.m", "apiBaseUrl", "selects", "case 22: api.mimo.org / api-testing.mimo.org via dev-menu flag"),
        ("pg.a", "wss://api.mimo.org/v1/run/socket", "connects", "code execution socket"),
        ("AiTutorRepository", "POST /v1/aiTutor/conversations", "starts", "JSON body"),
        ("AiTutorRepository", "POST /v1/aiTutor/conversations/{id}", "streams", "Accept: text/event-stream"),
        ("te.c", "te.a|te.d|te.e|te.c|te.g|te.b", "dispatches", "module dispatcher by tag name"),
        ("te.b", "te.f", "delegates", "<tables>/<table> parsing"),
        ("InteractiveLessonBaseViewModel", "LessonProgressRepository", "writes", "H(tries,attempts)"),
    ]
    deps["edges"] = [{"from": a, "to": b, "rel": r, "evidence": e} for a, b, r, e in edges]
    json.dump(deps, open(OUT / "07_DEPENDENCY_GRAPH.json", "w", encoding="utf-8"), indent=1)

    calls = {"note": "curated call edges with explicit evidence; not an exhaustive call graph",
             "edges": [
        {"from": "com.getmimo.ui.lesson.interactive.base.c", "to": "com.getmimo.data.source.remote.progress.LessonProgressRepository",
         "method": "createLessonProgress", "evidence": "base.c H(...) -> repo.createLessonProgress(bundle,startedAt,tries,attempts)",
         "label": "VERIFIED_STATIC"},
        {"from": "InteractiveLessonValidatedInputFragment$setupViews$2", "to": "qm.i.a",
         "method": "normalise", "evidence": "normalise(user).equals(normalise(expected))", "label": "VERIFIED_STATIC"},
        {"from": "InteractiveLessonValidatedInputFragment$setupViews$2", "to": "qm.e/qm.f/qm.g",
         "method": "verdict", "evidence": "three-way branch on exact/normalised equality", "label": "VERIFIED_STATIC"},
        {"from": "LessonProgressQueue", "to": "POST /v1/tutorials/{tutorialId}/progress",
         "method": "postProgress", "evidence": "queue batches Progress list", "label": "VERIFIED_STATIC"},
        {"from": "pg.a", "to": "wss://api.mimo.org/v1/run/socket", "method": "newWebSocket",
         "evidence": "Sec-WebSocket-Protocol: authorization.bearer.<token>", "label": "VERIFIED_STATIC"},
    ]}
    json.dump(calls, open(OUT / "08_CALL_GRAPH.json", "w", encoding="utf-8"), indent=1)

    recovered_n = sum(1 for r in rows if r["source_recovered"])
    print(f"classes={len(rows)} recovered_source={recovered_n} "
          f"packages={len({r['top_package'] for r in rows})}")
    print("top packages:", sorted(((sum(1 for r in rows if r['top_package'] == p), p) for p in {r['top_package'] for r in rows}), reverse=True)[:8])
    return 0


if __name__ == "__main__":
    sys.exit(main())
