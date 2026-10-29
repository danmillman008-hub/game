#!/usr/bin/env python3
"""Builds mivi_web/mivi_catalog.html — the single-file catalogue of Mivi engines,
verified output sizes and the 277-effect resource catalogue."""
import json, pathlib

HERE = pathlib.Path(__file__).parent
cat = json.loads((HERE / "catalog_effects.json").read_text())

# effect -> measured engine/resolution (probe run 40895589443, 2026-10-29)
WANLORA = ["4899", "5291", "5202", "5319", "4991", "4877", "5041", "4990", "5031", "5141",
           "5926", "6686", "7849", "6093"]
ENGINE_OF = {et: "6-col wanlora" for et in WANLORA}
ENGINE_OF["7600"] = "i2v_14b"
ENGINE_OF["6209"] = "GX"

rows = {}
for g in cat["groups"]:
    for r in g["resources"]:
        et = r["effectsType"]
        if et in rows:
            continue
        rows[et] = {
            "n": r["name"], "g": g["groupName"], "r": r.get("videoRatio") or "",
            "e": ENGINE_OF.get(et, ""), "p": r.get("videoPreviewUrl") or "",
        }
rows["6209"] = {"n": "Custom AI Video (متن سفارشی)", "g": "custom", "r": "9:16 / 3:4 / 1:1 / 4:3",
                "e": "GX", "p": ""}

effect_count = len(rows)
groups = sorted({v["g"] for v in rows.values()} | {"custom"})

# P2Type enum -> endpoint -> status/evidence
ENGINES = [
    ("GX_AiVideoP2V", "beatImage2Video/createNormalTask", "ok",
     "۹۶۰×۱۲۸۰ با effectType=6209 · افکت‌های کاتالوگ هم از همین دروازه رد می‌شوند"),
    ("— (60004) img2video_wanlora", "beatImage2Video/createNormalTask", "ok",
     "۱۳ افکت کاتالوگ → ۴۳۲×۵۷۶ · همیشه همین اندازه"),
    ("— (i2v_14b_v131)", "beatImage2Video/createNormalTask", "ok",
     "افکت ۷۶۰۰ (Clone) → ۵۶۲×۷۴۸ · level/quality بی‌اثر"),
    ("AiVideoGoogleVeo", "image2video/image2VideoCreateV5", "blocked",
     "۱۸ درخواست + جاروب ۵۷ مقدار effectType → همیشه effectType illegal"),
    ("AiVideoPixVerse", "image2VideoCreateV3", "blocked",
     "pixVerseId لازم است؛ با هر مقداری → invalid user یا effectType illegal"),
    ("AiVideoUnify", "image2video/unifiedTaskCreate", "blocked",
     "فیلد example اجباری است و هیچ‌کدام از مقادیر ما پذیرفته نشد"),
    ("AiSequenceVideo", "integrated/image2VideoCreateV4", "blocked",
     "effectType کاتالوگ رد می‌شود (همان خطای Veo)"),
    ("— (نسخهٔ قدیم)", "image2video/integratedTaskCreate", "blocked",
     "example is empty → مقدار مجاز نامعلوم"),
    ("AiVideoHDVidu", "createVideoHdTaskVidu", "blocked",
     "taskId تسک beat را رد می‌کند (taskId is invalid) — فضای تسک جدا"),
    ("Enhance (غیر-Vidu)", "createVideoHdTask", "billing",
     "بدنه‌اش ویدیوی ساخته‌شده است (videoUrl+md5+size+fileTime+dims)؛ از اعتبارسنجی گذشت و فقط c=2002 (اعتبار) خورد"),
    ("AiVideoLtx", "image2video/createTask", "unknown",
     "مسیر در dex هست، روی سرور آزموده نشده"),
    ("AiVideoT2V", "createText2VideoTask", "unknown", "فقط متن→ویدیو، خارج از نیاز فعلی"),
    ("AiText2VideoUnify", "—", "unknown", "مسیر در dex پیدا نشد"),
    ("AiHug / AiHugP2V / AiDance", "—", "unknown", "در کد فقط نام enum؛ بدنهٔ درخواست پیدا نشد"),
]

# V5 evidence chain
V5 = [
    ("googleId خالی", "c=400 googleId 不能为空", "اعتبارسنجی اول: googleId"),
    ("googleId=\"1\"، بدون effectType", "c=1013 effectType illegal", "اپ هیچ‌وقت effectType نمی‌فرستد، ولی سرور می‌خواهد"),
    ("effectType=4899/4991/6093/7849/6209 + googleId", "c=1013 effectType illegal", "هیچ افکت کاتالوگی برای Veo مجاز نیست"),
    ("جاروب effectType: ۰..۲۰، ۱۰۰..۵۰۰، ۱۰۰۰..۱۰۰۳، ۲۰۰۰..۲۰۰۲، ۶۰۰۰..۷۱۰۰، ۹۰۰۰..۱۰۰۰۱", "همه: effectType illegal", "مجموعهٔ مجاز Veo جای دیگری است"),
    ("`googleId=1` بدون هیچ effectType (بدنهٔ دقیق اپ)", "c=1013 effectType illegal", "حتی بدنهٔ خودِ اپ هم قبول نمی‌شود"),
    ("googleId=\"veo3\"", "c=500 NumberFormatException", "googleId باید عدد باشد"),
]

ENG_STATUS = {"ok": "کار می‌کند", "blocked": "قفل", "unknown": "نامعلوم", "billing": "فقط اعتبار کم است"}
ok = sum(1 for e in ENGINES if e[2] == "ok")
blocked = sum(1 for e in ENGINES if e[2] in ("blocked", "billing"))

def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

data = {"effects": rows, "groups": groups}

HTML = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>کاتالوگ موتورهای Mivi</title>
<style>
:root{{--bg:#0b0d12;--card:#141821;--card2:#1b2029;--line:#252b37;--txt:#e8ecf4;--dim:#8a93a6;
--ok:#22d3a7;--bad:#ff6b6b;--unk:#f5c451;--acc:#6ea8fe}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--txt);font:15px/1.7 Vazirmatn,"Segoe UI",Tahoma,sans-serif;padding:22px 14px 60px}}
.wrap{{max-width:1080px;margin:0 auto}}
h1{{font-size:24px;margin:0 0 4px}}
.sub{{color:var(--dim);font-size:13px;margin-bottom:18px}}
.chips{{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:24px}}
.chip{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 16px;font-size:13px}}
.chip b{{display:block;font-size:20px}}
h2{{font-size:18px;margin:30px 0 12px;padding-right:10px;border-right:3px solid var(--acc)}}
table{{width:100%;border-collapse:collapse;background:var(--card);border-radius:12px;overflow:hidden;font-size:13.5px}}
th,td{{padding:10px 12px;text-align:right;border-bottom:1px solid var(--line);vertical-align:top}}
th{{background:var(--card2);color:var(--dim);font-weight:600;font-size:12.5px}}
tr:last-child td{{border-bottom:none}}
code{{background:#0f1319;padding:1px 6px;border-radius:5px;font-family:ui-monospace,Menlo,monospace;font-size:12px;direction:ltr;display:inline-block}}
.b{{display:inline-block;padding:2px 9px;border-radius:20px;font-size:11.5px;white-space:nowrap}}
.b.ok{{background:rgba(34,211,167,.14);color:var(--ok);border:1px solid rgba(34,211,167,.3)}}
.b.bad{{background:rgba(255,107,107,.12);color:var(--bad);border:1px solid rgba(255,107,107,.3)}}
.b.billing{{background:rgba(110,168,254,.14);color:var(--acc);border:1px solid rgba(110,168,254,.3)}}
.b.unk{{background:rgba(245,196,81,.12);color:var(--unk);border:1px solid rgba(245,196,81,.3)}}
.controls{{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:10px}}
input,select{{background:var(--card);border:1px solid var(--line);color:var(--txt);border-radius:10px;padding:9px 12px;font:inherit;font-size:13.5px}}
input{{flex:1;min-width:200px}}
.count{{color:var(--dim);font-size:12.5px;margin-bottom:8px}}
.scroll{{max-height:560px;overflow:auto;border-radius:12px;border:1px solid var(--line)}}
.scroll table{{border-radius:0}}
.scroll th{{position:sticky;top:0;z-index:1}}
a{{color:var(--acc);text-decoration:none}}
.foot{{color:var(--dim);font-size:12px;margin-top:30px;line-height:1.9}}
</style>
</head>
<body>
<div class="wrap">
<h1>کاتالوگ موتورها و افکت‌های Mivi</h1>
<div class="sub">استخراج‌شده از APK نسخهٔ ۲.۳۷.۴۰۸ + اندازه‌گیری زندهٔ سرور · ۲۹ اکتبر ۲۰۲۶</div>

<div class="chips">
  <div class="chip"><b>{ok}</b>موتور تأییدشده با خروجی واقعی</div>
  <div class="chip"><b>{blocked}</b>مسیر قفل (با کد خطای دقیق)</div>
  <div class="chip"><b>{effect_count}</b>افکت در کاتالوگ</div>
  <div class="chip"><b>۹۶۰×۱۲۸۰</b>تنها مسیر ۷۲۰p واقعی</div>
</div>

<h2>یک. موتورها</h2>
<table>
<tr><th>موتور (enum)</th><th>اندپوینت</th><th>وضعیت</th><th>مدرک</th></tr>
""" + "\n".join(
    f"<tr><td><code>{esc(n)}</code></td><td><code>{esc(ep)}</code></td>"
    f"<td><span class='b {st}'>{{'ok':'کار می‌کند','blocked':'قفل','unknown':'نامعلوم','billing':'اعتبار'}}[st]</span></td>"
    f"<td>{esc(ev)}</td></tr>"
    for n, ep, st, ev in ENGINES) + """
</table>

<h2>دو. خروجی اندازه‌گیری‌شده</h2>
<table>
<tr><th>موتور در نام فایل خروجی</th><th>رزولوشن</th><th>مدت</th><th>نکته</th></tr>
<tr><td><code>60014/…/&lt;hash&gt;.mp4</code></td><td><b>۹۶۰×۱۲۸۰</b></td><td>۴٬۰۳ ثانیه</td><td>فقط با <code>effectType=6209</code> — همان مسیر فایل نهایی</td></tr>
<tr><td><code>img2video_wanlora-…</code></td><td>۴۳۲×۵۷۶</td><td>۴٬۰۶ ثانیه</td><td>۱۳ افکت کاتالوگ · level و quality تغییری نمی‌دهند</td></tr>
<tr><td><code>i2v_14b_v131-…</code></td><td>۵۶۲×۷۴۸</td><td>۴٬۰۶ ثانیه</td><td>افکت ۷۶۰۰ · با level=2 و بدون quality بایت‌به‌بایت یکسان</td></tr>
<tr><td><code>createVideoHdTask</code> روی ویدیوی ۴۳۲×۵۷۶</td><td>—</td><td>—</td><td>متادیتا پذیرفته شد، جواب <code>c=2002</code> (کسر اعتبار ناموفق) در level 1/2/3</td></tr>
<tr><td><code>INTEGRATED_60019-…</code></td><td>—</td><td>—</td><td>با <code>imageEffectType=7186</code> ساخته می‌شود ولی جدول کوئری‌اش پیدا نشد (c=3035)</td></tr>
</table>

<h2>سه. موتور گوگل (Veo)</h2>
<table>
<tr><th>درخواست</th><th>پاسخ سرور</th><th>معنی</th></tr>
""" + "\n".join(f"<tr><td>{esc(a)}</td><td><code>{esc(b)}</code></td><td>{esc(c)}</td></tr>" for a, b, c in V5) + f"""
</table>
<div class="sub" style="margin-top:10px">نتیجه: موتور گوگل با این حساب باز نمی‌شود. سرور یک <code>effectType</code> مخصوص Veo می‌خواهد که در APK و در کاتالوگ نیست. تنها راهش پیدا کردن فهرست مدل‌های Veo از یک حساب واقعی است.</div>

<h2>چهار. کاتالوگ افکت‌ها</h2>
<div class="controls">
  <input id="q" placeholder="جست‌وجو در نام افکت…">
  <select id="g"><option value="">همهٔ گروه‌ها</option>""" + "".join(
    f"<option value='{esc(g)}'>{esc(g)}</option>" for g in groups) + f"""</select>
</div>
<div class="count" id="cnt"></div>
<div class="scroll">
<table id="tbl">
<thead><tr><th>نام افکت</th><th>effectsType</th><th>گروه</th><th>نسبت</th><th>موتور</th><th>پیش‌نمایش</th></tr></thead>
<tbody></tbody>
</table>
</div>

<div class="foot">
همهٔ اعداد از اجرای زندهٔ خودکار روی GitHub Actions به‌دست آمده‌اند (رون‌های <code>40894312679</code>،
<code>40895589443</code>، <code>40896426948</code>، <code>40900184058</code>، <code>40900388082</code>، <code>40900721028</code>).
فهرست ۲۷۷ افکت از <code>common/vibe/resourceNew</code> سرور <code>cpi.ufotosoft.com</code> گرفته شده است.
</div>
</div>
<script>
const DATA = {json.dumps(data, ensure_ascii=False)};
const rows = Object.entries(DATA.effects).map(([et, v]) => ({{et, ...v}}));
const tbl = document.querySelector('#tbl tbody'), q = document.getElementById('q'),
      g = document.getElementById('g'), cnt = document.getElementById('cnt');
const EN = {{'6-col wanlora': '۴۳۲×۵۷۶', 'i2v_14b': '۵۶۲×۷۴۸', 'GX': '۹۶۰×۱۲۸۰'}};
function render() {{
  const kw = q.value.trim().toLowerCase(), gr = g.value;
  const out = rows.filter(r => (!gr || r.g === gr) && (!kw || r.n.toLowerCase().includes(kw) || r.et.includes(kw)));
  cnt.textContent = out.length + ' افکت از ' + rows.length;
  tbl.innerHTML = out.map(r => '<tr><td>' + r.n + '</td><td><code>' + r.et + '</code></td><td>' +
      r.g + '</td><td>' + r.r + '</td><td>' + (EN[r.e] || '—') + '</td><td>' +
      (r.p ? '<a href="' + r.p + '" target="_blank">mp4</a>' : '—') + '</td></tr>').join('');
}}
q.oninput = render; g.onchange = render; render();
</script>
</body>
</html>
"""
out = HERE / "mivi_catalog.html"
out.write_text(HTML, encoding="utf-8")
print("wrote", out, len(HTML), "bytes;", effect_count, "effects;", ok, "ok /", blocked, "blocked")
