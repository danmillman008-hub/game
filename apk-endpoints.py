#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
استخراج اندپوینت‌ها و کلیدهای API از اپلیکیشن (APK / AAB / JS / DEX)
=====================================================================

این ابزار روی سیستم خودِ شما اجرا می‌شود (نه روی سرور) و هیچ چیزی به بیرون
نمی‌فرستد. کارش این است که فایل اپ را باز کند و بگوید اپ با چه آدرس‌هایی
حرف می‌زند؛ مخصوصاً اندپوینت «استعلام/اصالت» و کلیدهایی مثل X-SSP-Api-Key.

اجرا:
    python apk-endpoints.py app.apk
    python apk-endpoints.py app.apk --json out.json --txt out.txt
    python apk-endpoints.py assets/index.android.bundle      # فایل تک
    python apk-endpoints.py folder/                          # پوشه (مثلاً خروجی apktool)

خروجی: گزارش خوانا در ترمینال + فایل JSON/TXT اختیاری.
نصب: فقط کتابخانهٔ استاندارد پایتون (3.8+). apktool/jadx لازم نیست،
ولی اگر داشتید، پوشهٔ خروجی آن‌ها را هم می‌توانید مستقیم بدهید.

چرا این‌طور کار می‌کند: در dex/JS/Flutter، رشته‌ها به‌صورت متن ساده باقی
می‌مانند؛ پس بدون decompile هم می‌شود آدرس‌ها و کلیدها را بیرون کشید.
"""

import argparse
import io
import json
import os
import re
import sys
import zipfile

# ---------- الگوها ----------
RE_URL = re.compile(rb"https?://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]{4,300}")
RE_GUID = re.compile(
    rb"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"
)
RE_PATH = re.compile(
    rb"/(?:[A-Za-z0-9_.\-]+/){0,6}"
    rb"(?:api|v1|v2|v3|inquiry|inquiries|esalat|authenticity|uid|barcode|catalog|"
    rb"check|verify|validate|search|nfi|irfda|drug|drugs|product)[A-Za-z0-9_./\-]{0,80}",
    re.I,
)
RE_HOSTISH = re.compile(rb"[a-z0-9][a-z0-9.\-]{2,60}\.(?:ir|com|net|org|io)(?::\d{2,5})?", re.I)
KEY_WORDS = [
    b"x-ssp-api-key", b"ssp-api-key", b"apikey", b"api-key", b"api_key",
    b"x-api-key", b"authorization", b"bearer", b"client_secret", b"token",
]
INTEREST = [b"inquiry", b"esalat", b"authenticity", b"uid", b"barcode", b"catalog", b"nfi"]
FA_INTEREST = ["استعلام", "اصالت", "رهگیری", "فرآورده", "کاتالوگ", "بارکد"]

MAX_ENTRY = 60 * 1024 * 1024      # هر فایل حداکثر ۶۰ مگ خوانده می‌شود
SKIP_EXT = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".ttf", ".otf", ".woff", ".woff2", ".mp3", ".mp4", ".ogg", ".wav")


def dec(b: bytes) -> str:
    try:
        return b.decode("utf-8", "replace")
    except Exception:
        return b.decode("latin-1", "replace")


def ctx(buf: bytes, pos: int, span: int = 90) -> str:
    a = max(0, pos - span)
    b = min(len(buf), pos + span)
    s = dec(buf[a:b])
    s = re.sub(r"[^\x20-\x7E\u0600-\u06FF]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


class Report:
    def __init__(self):
        self.urls = {}
        self.paths = {}
        self.hosts = {}
        self.keys = []          # (kind, value, context)
        self.interesting = []   # (value, context)
        self.files = []
        self.notes = []

    def add(self, bucket: dict, key: str, src: str):
        if not key:
            return
        bucket.setdefault(key, set()).add(src)


def scan_bytes(buf: bytes, src: str, rep: Report):
    # 1) URLها
    for m in RE_URL.finditer(buf):
        u = dec(m.group(0)).rstrip('.,;)"\'>')
        low = u.lower()
        if any(low.endswith(x) for x in (".png", ".jpg", ".css", ".gif", ".svg", ".woff")):
            continue
        rep.add(rep.urls, u, src)
    # 2) مسیرهای شبه‌اندپوینت
    for m in RE_PATH.finditer(buf):
        p = dec(m.group(0)).rstrip('.,;)"\'')
        if len(p) < 6:
            continue
        if any(p.lower().endswith(x) for x in (".png", ".jpg", ".css", ".js", ".svg")):
            continue
        rep.add(rep.paths, p, src)
    # 3) هاست‌ها
    for m in RE_HOSTISH.finditer(buf):
        h = dec(m.group(0)).lower()
        if h.endswith(".ir") or "ttac" in h or "fda" in h or "ssp" in h:
            rep.add(rep.hosts, h, src)
    # 4) کلیدها (GUID نزدیک کلمهٔ کلید)
    lowbuf = buf.lower()
    for kw in KEY_WORDS:
        start = 0
        while True:
            i = lowbuf.find(kw, start)
            if i < 0:
                break
            start = i + 1
            window = buf[max(0, i - 160): i + 260]
            for g in RE_GUID.finditer(window):
                rep.keys.append((dec(kw), dec(g.group(0)), ctx(buf, i)))
    # 5) چیزهای مرتبط با استعلام
    for kw in INTEREST:
        start = 0
        n = 0
        while n < 40:
            i = lowbuf.find(kw, start)
            if i < 0:
                break
            start = i + 1
            n += 1
            rep.interesting.append((dec(kw), ctx(buf, i, 110)))


def scan_file_bytes(name: str, data: bytes, rep: Report):
    low = name.lower()
    if low.endswith(SKIP_EXT):
        return
    if len(data) > MAX_ENTRY:
        data = data[:MAX_ENTRY]
        rep.notes.append("بزرگ بود و فقط بخش اول '%s' خوانده شد" % name)
    scan_bytes(data, name, rep)


def walk_apk(path: str, rep: Report):
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        rep.notes.append("تعداد فایل داخل بسته: %d" % len(names))
        classes = [n for n in names if re.match(r"classes\d*\.dex$", n)]
        if classes:
            rep.notes.append("فایل‌های dex: " + ", ".join(classes))
        flutter = [n for n in names if "flutter_assets" in n or n.endswith("kernel_blob.bin")]
        if flutter:
            rep.notes.append("نشانهٔ Flutter: %d فایل (رشته‌ها در kernel_blob.bin/isolate_snapshot هستند)" % len(flutter))
        if any(n.endswith("index.android.bundle") for n in names):
            rep.notes.append("نشانهٔ React Native: assets/index.android.bundle")
        if any("assets/www/" in n for n in names):
            rep.notes.append("نشانهٔ Cordova/Ionic: assets/www/")
        for n in names:
            if n.endswith("/"):
                continue
            if not (n.endswith((".dex", ".js", ".json", ".xml", ".txt", ".html", ".bundle", ".bin", ".so", ".dat", ".properties", ".yml", ".yaml"))
                    or n.startswith("assets/") or n.startswith("res/raw")):
                continue
            try:
                with z.open(n) as f:
                    data = f.read(MAX_ENTRY)
            except Exception as e:
                rep.notes.append("خطا در خواندن '%s': %s" % (n, e))
                continue
            rep.files.append(n)
            scan_file_bytes(n, data, rep)


def walk_dir(path: str, rep: Report):
    for root, _dirs, files in os.walk(path):
        for fn in files:
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, path)
            if fn.lower().endswith(SKIP_EXT):
                continue
            try:
                with open(full, "rb") as f:
                    data = f.read(MAX_ENTRY)
            except Exception as e:
                rep.notes.append("خطا در خواندن '%s': %s" % (rel, e))
                continue
            rep.files.append(rel)
            scan_file_bytes(rel, data, rep)


def score_path(p: str) -> int:
    pl = p.lower()
    s = 0
    for w, wgt in (("inquiry", 6), ("esalat", 6), ("authenticity", 6), ("uid", 5),
                   ("barcode", 4), ("catalog", 4), ("check", 3), ("verify", 3),
                   ("valid", 2), ("v1", 1), ("api", 2), ("drug", 2), ("search", 2)):
        if w in pl:
            s += wgt
    return s


def build_report(rep: Report) -> str:
    L = []
    L.append("=" * 68)
    L.append("گزارش استخراج اندپوینت از اپلیکیشن")
    L.append("=" * 68)
    for n in rep.notes:
        L.append("• " + n)
    L.append("فایل‌های اسکن‌شده: %d" % len(rep.files))

    L.append("\n--- دامنه‌ها ---")
    for h in sorted(rep.hosts):
        L.append("  " + h + "   (" + ", ".join(sorted(rep.hosts[h])[:3]) + ")")

    L.append("\n--- آدرس‌های کامل (URL) ---")
    for u in sorted(rep.urls):
        L.append("  " + u + "   ⟵ " + ", ".join(sorted(rep.urls[u])[:2]))

    L.append("\n--- مسیرهای شبه‌اندپوینت (به‌ترتیب اهمیت) ---")
    paths = sorted(rep.paths, key=score_path, reverse=True)
    for p in paths[:120]:
        sc = score_path(p)
        flag = " ★" if sc >= 8 else ("  " if sc >= 4 else "")
        L.append("  %s %-60s  (امتیاز %d)" % (flag, p, sc))

    if rep.keys:
        L.append("\n--- کلید/توکن‌های کنار کلمهٔ کلید ---")
        by_val = {}
        for kind, val, c in rep.keys:
            by_val.setdefault(val, {"kinds": set(), "ctx": c})
            by_val[val]["kinds"].add(kind)
        for val, info in by_val.items():
            L.append("  %s" % val)
            L.append("       برچسب‌های دیده‌شده: " + ", ".join(sorted(info["kinds"])))
            L.append("       زمینه: " + info["ctx"][:160])

    L.append("\n--- رشته‌های مرتبط با استعلام (زمینه) ---")
    seen = set()
    for kind, c in rep.interesting:
        if not c or c in seen:
            continue
        seen.add(c)
        if len(seen) > 60:
            break
        L.append("  [" + kind + "] " + c[:200])

    L.append("\n" + "=" * 68)
    L.append("قدم بعدی: آدرس‌های ستاره‌دار را در «آزمایشگاه تیتک» (ttac-lab.html)")
    L.append("بگذارید و با یک UID واقعی تست کنید. هر کدام جواب داد، همان را")
    L.append("در برنامهٔ انبارگردانی قطعی می‌کنیم.")
    L.append("=" * 68)
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="استخراج اندپوینت و کلید API از فایل اپلیکیشن")
    ap.add_argument("target", help="فایل .apk/.aab/.zip/.dex/.js یا پوشه")
    ap.add_argument("--json", dest="json_out", help="ذخیرهٔ گزارش ساختاریافته در JSON")
    ap.add_argument("--txt", dest="txt_out", help="ذخیرهٔ گزارش متنی")
    a = ap.parse_args()

    rep = Report()
    t = a.target
    if not os.path.exists(t):
        print("فایل/پوشه پیدا نشد: " + t)
        return 2
    if os.path.isdir(t):
        walk_dir(t, rep)
    elif zipfile.is_zipfile(t):
        walk_apk(t, rep)
    else:
        with open(t, "rb") as f:
            data = f.read(MAX_ENTRY)
        rep.files.append(os.path.basename(t))
        scan_file_bytes(os.path.basename(t), data, rep)

    text = build_report(rep)
    print(text)

    if a.txt_out:
        with open(a.txt_out, "w", encoding="utf-8") as f:
            f.write(text)
        print("\n✓ متن ذخیره شد: " + a.txt_out)
    if a.json_out:
        data = {
            "hosts": {k: sorted(v) for k, v in rep.hosts.items()},
            "urls": {k: sorted(v) for k, v in rep.urls.items()},
            "paths": {k: sorted(v) for k, v in rep.paths.items()},
            "keys": [{"kind": k, "value": v, "context": c} for k, v, c in rep.keys],
            "notes": rep.notes,
        }
        with open(a.json_out, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("✓ JSON ذخیره شد: " + a.json_out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
