#!/usr/bin/env python3
"""Mission 8 — renamed-app-class register.

Why this exists
---------------
The Mission-7 class universe classifies ownership by *package name*: 3,133 classes
carry a `com.getmimo.` name, 13,113 are "obfuscated candidates". Measurement in
mission-08 shows that split is not ownership:

  * many `com.getmimo.*` classes are Kotlin lambdas whose enclosing class was
    renamed away (e.g. `…account.AccountRepository$deleteAccount$2` exists while
    `…account.AccountRepository` does not),
  * 1,148 classes with short obfuscated names (`ku.a`, `np.b`, `ri.a`, …) reference
    `com/getmimo/` types inside their code, i.e. they *are* app logic.

This tool selects the second group by evidence — an instruction that actually
references an app type — and describes it structurally. It never decides
ownership from a name.

Outputs
  01_DEEP_CLASS_INVESTIGATION/05_RENAMED_APP_LOGIC_REGISTER.csv
  01_DEEP_CLASS_INVESTIGATION/evidence/RENAMED_APP_LOGIC.jsonl

Usage
  python3 build_renamed_app_register.py --dex-dir /tmp/x --src-dir /tmp/dad \
      --out ../mission-08/01_DEEP_CLASS_INVESTIGATION
"""
import argparse
import csv
import glob
import json
import os
import re
from collections import Counter

from androguard.core.dex import DEX


def short_name_reference(dn):
    return len(dn.rsplit(".", 1)[-1]) <= 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dex-dir", required=True)
    ap.add_argument("--src-dir", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(os.path.join(a.out, "evidence"), exist_ok=True)

    rows = []
    jl = open(os.path.join(a.out, "evidence", "RENAMED_APP_LOGIC.jsonl"), "w")
    for path in sorted(glob.glob(os.path.join(a.dex_dir, "*.dex"))):
        with open(path, "rb") as fh:
            dx = DEX(fh.read())
        for cd in dx.get_classes():
            dn = cd.get_name()[1:-1].replace("/", ".")
            if dn.startswith("com.getmimo") or not short_name_reference(dn):
                continue
            app_types = Counter()
            strings = []
            insns = 0
            for m in cd.get_methods():
                code = m.get_code()
                if not code:
                    continue
                for ins in code.get_bc().get_instructions():
                    insns += 1
                    out = ins.get_output()
                    for t in re.findall(r"L(com/getmimo/[\w/$]+);", out):
                        app_types[t.replace("/", ".")] += 1
                    if "const-string" in ins.get_name() and '"' in out:
                        strings.append(out[out.find('"') + 1:out.rfind('"')][:200])
            if not app_types:
                continue
            implements = [i[1:-1].replace("/", ".") for i in cd.get_interfaces()]
            rec = {
                "class": dn,
                "dex": os.path.basename(path),
                "super": cd.get_superclassname()[1:-1].replace("/", "."),
                "implements_app_interface": ",".join(sorted(i for i in implements
                                                            if i.startswith("com.getmimo"))),
                "implements_all": ",".join(sorted(implements)),
                "fields": len(list(cd.get_fields())),
                "methods": len(list(cd.get_methods())),
                "insns": insns,
                "app_types_referenced": len(app_types),
                "top_app_types": ";".join(t for t, _ in app_types.most_common(5)),
                "strings": sorted(set(strings))[:20],
                "java_present": os.path.exists(os.path.join(a.src_dir, dn + ".java")),
            }
            rows.append(rec)
            jl.write(json.dumps(rec, ensure_ascii=False) + "\n")
    jl.close()

    rows.sort(key=lambda r: (-r["app_types_referenced"], r["class"]))
    header = ["class", "super", "implements_app_interface", "implements_all", "methods", "insns",
              "app_types_referenced", "top_app_types", "java_present", "dex"]
    with open(os.path.join(a.out, "05_RENAMED_APP_LOGIC_REGISTER.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=header, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(json.dumps({
        "renamed_app_classes": len(rows),
        "with_implements_app_interface": sum(1 for r in rows if r["implements_app_interface"]),
        "with_java": sum(1 for r in rows if r["java_present"]),
        "top20_by_reference_breadth": [r["class"] for r in rows[:20]],
    }, indent=1))


if __name__ == "__main__":
    main()
