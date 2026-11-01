#!/usr/bin/env python3
"""Stage 1 — static inventory of an APK without Java/JADX.

Follows the REA (morluto/rea) evidence order for Android artifacts:
  inspect_android_package  -> manifest identity, components, permissions
  search_android_classes   -> class index over every classesN.dex
  locate string constants  -> string pool per dex (raw evidence)

Usage:
    python3 -m venv .venv && .venv/bin/pip install androguard
    .venv/bin/python tools/analyze_apk.py /path/to/Mimo.apk out/

Outputs (to out/):
    manifest.json           identity, components, permissions, certificate
    all-classes.txt         every L...; type across all dex files
    all-dex-strings.txt     every unique string constant across all dex files
    apk.sha256              artifact digest (chain of custody)
"""
import hashlib
import json
import os
import struct
import sys
import zipfile


def uleb128(buf: bytes, off: int):
    result = shift = 0
    while True:
        byte = buf[off]
        off += 1
        result |= (byte & 0x7F) << shift
        if not byte & 0x80:
            return result, off
        shift += 7


def dex_strings(buf: bytes):
    string_ids_size, string_ids_off = struct.unpack_from("<II", buf, 0x38)
    out = []
    for i in range(string_ids_size):
        off = struct.unpack_from("<I", buf, string_ids_off + 4 * i)[0]
        _, start = uleb128(buf, off)
        end = buf.index(b"\x00", start)
        out.append(buf[start:end].decode("utf-8", "replace"))
    return out


def dex_classes(buf: bytes, strings):
    type_ids_size, type_ids_off = struct.unpack_from("<II", buf, 0x40)
    class_defs_size, class_defs_off = struct.unpack_from("<II", buf, 0x60)
    types = [strings[struct.unpack_from("<I", buf, type_ids_off + 4 * i)[0]]
             for i in range(type_ids_size)]
    names = []
    for i in range(class_defs_size):
        idx = struct.unpack_from("<I", buf, class_defs_off + 32 * i)[0]
        if idx < len(types):
            names.append(types[idx])
    return names


def main(apk_path: str, out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    digest = hashlib.sha256(open(apk_path, "rb").read()).hexdigest()
    open(os.path.join(out_dir, "apk.sha256"), "w").write(f"{digest}  {os.path.basename(apk_path)}\n")

    # ---- DEX pass (pure python, no JVM) ----
    classes, strings = set(), set()
    with zipfile.ZipFile(apk_path) as zf:
        for name in zf.namelist():
            if name.endswith(".dex"):
                buf = zf.read(name)
                if len(buf) < 0x70:      # placeholder dex with no payload
                    continue
                s = dex_strings(buf)
                strings.update(s)
                classes.update(dex_classes(buf, s))
    open(os.path.join(out_dir, "all-classes.txt"), "w").write("\n".join(sorted(classes)))
    open(os.path.join(out_dir, "all-dex-strings.txt"), "w").write("\n".join(sorted(strings)))

    # ---- manifest pass (androguard) ----
    from loguru import logger
    logger.remove()
    from androguard.core.apk import APK
    apk = APK(apk_path, testzip=False)
    certs = apk.get_certificates()
    info = {
        "sha256": digest,
        "size": os.path.getsize(apk_path),
        "package": apk.get_package(),
        "app_name": apk.get_app_name(),
        "version_name": apk.get_androidversion_name(),
        "version_code": apk.get_androidversion_code(),
        "min_sdk": apk.get_min_sdk_version(),
        "target_sdk": apk.get_target_sdk_version(),
        "main_activity": apk.get_main_activity(),
        "activities": apk.get_activities(),
        "services": apk.get_services(),
        "receivers": apk.get_receivers(),
        "providers": apk.get_providers(),
        "permissions": apk.get_permissions(),
        "declared_permissions": sorted(apk.get_declared_permissions()),
        "features": apk.get_features(),
        "cert_issuer": certs[0].issuer.human_friendly if certs else None,
        "cert_sha256": certs[0].sha256_fingerprint if certs else None,
        "cert_valid_from": str(certs[0].not_valid_before) if certs else None,
        "cert_valid_to": str(certs[0].not_valid_after) if certs else None,
        "classes": len(classes),
        "unique_strings": len(strings),
        "app_classes": sum(1 for c in classes if c.startswith("Lcom/getmimo/")),
    }
    json.dump(info, open(os.path.join(out_dir, "manifest.json"), "w"), indent=1, default=str)
    print(json.dumps({k: v for k, v in info.items() if not isinstance(v, list)}, indent=1))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "out")
