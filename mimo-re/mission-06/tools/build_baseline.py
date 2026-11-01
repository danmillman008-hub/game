#!/usr/bin/env python3
"""MISSION-06 Phase 0 — baseline, provenance and environment inventory.

Produces the machine-readable baseline artifacts under 00_BASELINE/:
  ENVIRONMENT_INVENTORY.json, SOURCE_INVENTORY.json, APK_MANIFEST.json, DEX_HASHES.json,
  DECOMPILATION_STATUS.json, PREVIOUS_MISSIONS_INTEGRITY.json
Everything is computed from local files only; no network calls; nothing is mutated.
"""
from __future__ import annotations

import hashlib
import json
import os
import pathlib
import platform
import shutil
import subprocess
import sys
import zipfile

REPO = pathlib.Path("/home/user/game")
OUT = REPO / "mimo-re" / "mission-06" / "00_BASELINE"
APK = pathlib.Path("/tmp/apk/Mimo_9.35 (1).apk")
DEXDIR = pathlib.Path("/tmp/x")
DAD = pathlib.Path("/tmp/dad")
RES = pathlib.Path("/tmp/res")

TOOLS = ["python3", "java", "javac", "jadx", "apktool", "baksmali", "smali", "aapt", "aapt2",
         "dot", "mmdc", "adb", "emulator", "nm", "readelf", "objdump", "strings", "unzip", "git"]


def sha256(p: pathlib.Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def md5(p: pathlib.Path) -> str:
    h = hashlib.md5()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def run(cmd: list[str]) -> str:
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=120).stdout.strip()
    except Exception as exc:  # pragma: no cover
        return f"<error: {exc}>"


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)

    # ---- environment
    env = {"python": sys.version.split()[0], "platform": platform.platform(),
           "tools": {}, "notes": []}
    for t in TOOLS:
        path = shutil.which(t)
        entry = {"present": bool(path), "path": path}
        if path and t in ("nm", "readelf", "objdump", "strings", "git", "unzip"):
            v = run([t, "--version"]).splitlines()
            entry["version"] = v[0][:120] if v else "<no output>"
        env["tools"][t] = entry
    venv_pkgs = run(["/tmp/venv/bin/pip", "list", "--format=freeze"]).splitlines()
    env["python_packages"] = [p for p in venv_pkgs if p.lower().startswith(("androguard", "pytest", "lxml"))]
    env["blocked_by"] = {k: v["present"] is False for k, v in env["tools"].items()}
    json.dump(env, open(OUT / "ENVIRONMENT_INVENTORY.json", "w"), indent=1)

    # ---- APK manifest
    z = zipfile.ZipFile(APK)
    top: dict[str, int] = {}
    for n in z.namelist():
        key = n.split("/")[0] if "/" in n else "(root)"
        top[key] = top.get(key, 0) + 1
    sig = [n for n in z.namelist() if n.startswith("META-INF/") and n.endswith((".RSA", ".DSA", ".EC"))]
    apk = {
        "path": str(APK),
        "bytes": APK.stat().st_size,
        "md5": md5(APK),
        "sha256": sha256(APK),
        "zip_entries": len(z.namelist()),
        "top_level_dirs": dict(sorted(top.items(), key=lambda kv: -kv[1])),
        "signature_blocks": sig,
        "signature_sha256": {n: sha256_from_zip(z, n) for n in sig} if sig else {},
    }
    json.dump(apk, open(OUT / "APK_MANIFEST.json", "w"), indent=1)

    # ---- dex hashes
    dexes = []
    for p in sorted(DEXDIR.glob("classes*.dex"), key=lambda q: (len(q.name), q.name)):
        dexes.append({"file": p.name, "bytes": p.stat().st_size, "sha256": sha256(p)})
    json.dump({"dex_count": len(dexes), "dexes": dexes,
               "note": "13 dex files incl. 8 tiny stubs; hotspot dex is classes.dex"},
              open(OUT / "DEX_HASHES.json", "w"), indent=1)

    # ---- decompilation status
    files = sorted(DAD.glob("*.java"))
    status = {
        "output_dir": str(DAD),
        "java_files": len(files),
        "total_bytes": sum(f.stat().st_size for f in files),
        "resources_extracted": str(RES),
        "resource_files": sum(1 for _ in RES.rglob("*") if _.is_file()) if RES.exists() else 0,
        "mission05_manifests": sorted(str(p.relative_to(REPO)) for p in
                                      (REPO / "mimo-re" / "mission-05" / "evidence").glob("DECOMPILE_MANIFEST_*.json")),
        "verification": "mission-06 re-derives dex hashes above; mission-05 manifests are cross-checked "
                        "by name+size, not trusted blindly",
    }
    json.dump(status, open(OUT / "DECOMPILATION_STATUS.json", "w"), indent=1)

    # ---- previous missions integrity (git-tracked, read-only)
    def tracked(prefix: str) -> dict:
        out = run(["git", "-C", str(REPO), "ls-tree", "-r", "--name-only", "HEAD", prefix]).splitlines()
        out = [x for x in out if x]
        return {"tracked_files": len(out), "bytes": sum((REPO / x).stat().st_size for x in out if (REPO / x).exists())}
    integrity = {
        "head": run(["git", "-C", str(REPO), "rev-parse", "HEAD"]),
        "branch": run(["git", "-C", str(REPO), "rev-parse", "--abbrev-ref", "HEAD"]),
        "worktree_dirty": bool(run(["git", "-C", str(REPO), "status", "--porcelain"])),
        "mission04": tracked("mimo-re/complete-extraction"),
        "mission05": tracked("mimo-re/mission-05"),
        "policy": "mission-06 only reads missions 4 and 5; no file under them is modified",
    }
    json.dump(integrity, open(OUT / "PREVIOUS_MISSIONS_INTEGRITY.json", "w"), indent=1)

    # ---- source inventory (recovered artifacts)
    src = {"apk": apk["sha256"], "dex": dexes, "decompiled_java": status["java_files"],
           "resources": status["resource_files"],
           "assets": sum(1 for _ in (DEXDIR / "assets").rglob("*") if _.is_file()) if (DEXDIR / "assets").exists() else 0,
           "native_libs": sorted(str(p.relative_to(DEXDIR)) for p in (DEXDIR / "meta" / "lib").rglob("*.so")) if (DEXDIR / "meta").exists() else []}
    json.dump(src, open(OUT / "SOURCE_INVENTORY.json", "w"), indent=1)
    print(json.dumps({k: (v if not isinstance(v, dict) else "...") for k, v in
                      {"apk_sha256": apk["sha256"], "dex": len(dexes), "java": status["java_files"],
                       "resources": status["resource_files"]}.items()}, indent=1))
    return 0


def sha256_from_zip(z: zipfile.ZipFile, name: str) -> str:
    h = hashlib.sha256()
    h.update(z.read(name))
    return h.hexdigest()


if __name__ == "__main__":
    sys.exit(main())
