#!/usr/bin/env python3
"""Build the ONE-CLICK Mimo-native deliverables (dependency-free, pure Python).

    app/dist/Mimo.html      one self-contained file — double-click, no server
    app/dist/index.html     same app + manifest + service worker (installable PWA)
    app/dist/Mimo.zip       everything, ready to host or to send
    app/dist/launcher.html  friendly Persian start page
    app/dist/BUILD_MANIFEST.json

The shell is `app/native/index.html`: the APPROVED v12.5-fa phone markup,
CSS, vectors, data and UI renderer are inlined byte-identically; the new
`app/src/native.js` controller (plus the pure offline engines it imports) is
bundled into ONE classic IIFE via a tiny module registry. No esbuild, no npm,
no network. The generated HTML embeds its own source as base64 so the in-app
«دانلود Mimo.html» button reproduces exactly the same file.

Run:  python3 app/tools/build_output.py
"""
from __future__ import annotations
import base64, hashlib, json, pathlib, re, zipfile, datetime

ROOT = pathlib.Path(__file__).resolve().parents[2]
APP = ROOT / 'app'
SRC = APP / 'src'
NATIVE = APP / 'native'
DIST = APP / 'dist'
SLOT = '__MIMO_SOURCE_B64_SLOT__'
ENTRY = 'native.js'
DIST.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# 1. Tiny ESM -> classic-IIFE bundler (only the graph reachable from ENTRY)
# ---------------------------------------------------------------------------
IMPORT = re.compile(r"^[ \t]*import\s+([\s\S]*?)\s+from\s+['\"]([^'\"]+)['\"];?[ \t]*\r?\n?", re.M)
EXPORT_NAMED = re.compile(r"^[ \t]*export\s*\{([^}]*)\}\s*;?[ \t]*$", re.M)
EXPORT_DECL = re.compile(r"^([ \t]*)export\s+(?:const|let|var|function|class)\s+([A-Za-z_$][\w$]*)", re.M)
EXPORT_DEFAULT = re.compile(r"^[ \t]*export\s+default\b", re.M)


def bindings(spec: str, where: str):
    spec = spec.strip()
    assert spec.startswith('{') and '}' in spec, f'{where}: unsupported import form {spec[:60]!r}'
    inner = spec[1:spec.rindex('}')]
    out = []
    for item in inner.split(','):
        item = item.strip()
        if not item:
            continue
        parts = item.split()
        if len(parts) == 1:
            out.append((parts[0], parts[0]))
        elif len(parts) == 3 and parts[1] == 'as':
            out.append((parts[0], parts[2]))
        else:
            raise AssertionError(f'{where}: unsupported binding {item!r}')
    return out


modules = {}
for path in sorted(SRC.glob('*.js')):
    modules[path.name] = path.read_text(encoding='utf-8')
assert ENTRY in modules, f'{ENTRY} missing from src/'

prepared, deps = {}, {}
for name, text in modules.items():
    assert not EXPORT_DEFAULT.search(text), f'{name}: export default is not supported by the bundler'
    collected = []

    def import_sub(m):
        spec, rel = m.group(1), m.group(2)
        dep = rel.lstrip('./')
        assert dep in modules, f'{name}: unknown import {rel}'
        deps.setdefault(name, set()).add(dep)
        pairs = bindings(spec, name)
        props = ', '.join(a if a == b else f'{a}: {b}' for a, b in pairs)
        return f'const {{ {props} }} = __mods[{dep!r}];\n'

    body = IMPORT.sub(import_sub, text)

    def named_sub(m):
        for item in m.group(1).split(','):
            item = item.strip()
            if not item:
                continue
            parts = item.split()
            collected.append(parts[2] if len(parts) == 3 and parts[1] == 'as' else parts[0])
        return ''

    body = EXPORT_NAMED.sub(named_sub, body)
    for m in EXPORT_DECL.finditer(body):
        collected.append(m.group(2))
    body = re.sub(r"^([ \t]*)export\s+(?=(?:const|let|var|function|class)\b)", r'\1', body, flags=re.M)
    for bad in ('</script', '<!--'):
        assert bad.lower() not in body.lower(), f'{name}: forbidden HTML-breaking sequence in inline script'
    assert not re.search(r"^[ \t]*(?:import|export)\s", body, re.M), f'{name}: residual ESM syntax'
    exports = ', '.join(dict.fromkeys(collected))
    prepared[name] = (deps.setdefault(name, set()), body, exports)

order, done, visiting = [], set(), set()


def visit(n):
    if n in done:
        return
    assert n not in visiting, f'cycle involving {n}'
    visiting.add(n)
    for d in sorted(prepared[n][0]):
        visit(d)
    visiting.discard(n)
    done.add(n)
    order.append(n)


visit(ENTRY)  # ONLY the native controller graph; legacy app.js is not shipped.
assert 'app.js' not in order and 'plus.js' not in order, 'legacy controller leaked into the one-file build'

chunks = ["(function () {\n'use strict';\nvar __mods = {};\n"]
for n in order:
    _, body, exports = prepared[n]
    chunks.append(f"/* ---- src/{n} ---- */\n__mods[{n!r}] = (function () {{\n'use strict';\n")
    chunks.append(body)
    chunks.append(f"\nreturn {{ {exports} }};\n}})();\n")
chunks.append('})();\n')
bundle = ''.join(chunks)
print(f'bundled {len(order)} reachable ESM modules -> {len(bundle):,} chars')

# ---------------------------------------------------------------------------
# 2. Inline CSS / classic scripts / approved phone markup into one HTML
# ---------------------------------------------------------------------------
html = (NATIVE / 'index.html').read_text(encoding='utf-8')


def resolve(rel):
    p = (NATIVE / rel).resolve()
    assert p.is_file(), f'missing asset {rel}'
    return p


def inline_css(m):
    rel = m.group(1)
    css = resolve(rel).read_text(encoding='utf-8')
    assert '</style' not in css.lower()
    return f'<style data-src="{rel}">\n{css}\n</style>'


html, ncss = re.subn(r'<link rel="stylesheet" href="([^"]+\.css)">', inline_css, html)
assert ncss == 4, f'expected 4 stylesheets, inlined {ncss}'


def inline_js(m):
    rel = m.group(1)
    js = resolve(rel).read_text(encoding='utf-8')
    assert '</script' not in js.lower() and '<!--' not in js, f'{rel}: unsafe inline script'
    return f'<script data-src="{rel}">\n{js}\n</script>'


html, njs = re.subn(r'<script src="([^"]+\.js)"></script>', inline_js, html)
assert njs == 2, f'expected 2 classic scripts, inlined {njs}'

phone = (APP / 'assets' / 'phone.html').read_text(encoding='utf-8').rstrip('\n')
assert '<!-- MIMO_NATIVE_PHONE_MARKUP -->' in html
html = html.replace('<!-- MIMO_NATIVE_PHONE_MARKUP -->',
                    '<!-- APPROVED v12.5-fa PHONE MARKUP: byte-identical -->\n' + phone)

icon_b64 = base64.b64encode((APP / 'assets/icons/icon-192.png').read_bytes()).decode('ascii')
html = html.replace(
    '<link rel="manifest" href="./manifest.webmanifest">',
    f'<link rel="icon" href="data:image/png;base64,{icon_b64}">\n'
    f'<link rel="apple-touch-icon" href="data:image/png;base64,{icon_b64}">')

module_tag = '<script type="module" src="./src/native.js"></script>'
assert module_tag in html
html = html.replace(module_tag, f'<script data-generated="mimo-bundle.js">\n{bundle}\n</script>')

meta = ('<meta name="apple-mobile-web-app-capable" content="yes">\n'
        '<meta name="mobile-web-app-capable" content="yes">\n'
        '<meta name="apple-mobile-web-app-status-bar-style" content="default">\n'
        '<meta name="apple-mobile-web-app-title" content="میمو">\n')
html = html.replace('<title>', meta + '<title>', 1)
# Put the source payload in <head> so it exists before the bundle executes.
html = html.replace('</head>', f'  <script id="mimoSource" type="text/plain">{SLOT}</script>\n</head>', 1)

# No external resource references may remain (script/style bodies may contain URLs).
markup = re.sub(r'<script\b[^>]*>[\s\S]*?</script>', '<script></script>', html, flags=re.I)
markup = re.sub(r'<style\b[^>]*>[\s\S]*?</style>', '<style></style>', markup, flags=re.I)
leftovers = re.findall(r'<[^>]*\s(?:src|href)="(?!data:|#)([^"]+)"', markup, re.I)
assert not leftovers, f'external references remain: {leftovers[:8]}'
assert html.count(SLOT) == 1, 'source slot must appear exactly once'
assert '<script type="module"' not in html

template = html
payload = base64.b64encode(template.encode('utf-8')).decode('ascii')
onefile = template.replace(SLOT, payload)
(DIST / 'Mimo.html').write_text(onefile, encoding='utf-8')
print('wrote dist/Mimo.html', f'{len(onefile.encode()):,} bytes')

# ---------------------------------------------------------------------------
# 3. Installable PWA host, launcher, static PWA files
# ---------------------------------------------------------------------------
SW_REGISTER = """<script>
if ('serviceWorker' in navigator && location.protocol.indexOf('http') === 0) {
  window.addEventListener('load', function () {
    navigator.serviceWorker.register('./sw.js', {scope: './'}).catch(function () {});
  });
}
</script>
"""
pwa_index = onefile.replace('<title>', '<link rel="manifest" href="./manifest.webmanifest">\n<title>', 1)
# The bundle contains HTML template strings with literal "</body>" inside them;
# only the LAST closing body tag is the document's real one.
end_body = pwa_index.rfind('</body>')
assert end_body > 0, 'could not locate the document closing body tag'
pwa_index = pwa_index[:end_body] + SW_REGISTER + pwa_index[end_body:]
(DIST / 'index.html').write_text(pwa_index, encoding='utf-8')

(DIST / 'manifest.webmanifest').write_bytes((APP / 'assets/pwa/manifest.webmanifest').read_bytes())
(DIST / 'sw.js').write_bytes((APP / 'assets/pwa/sw.js').read_bytes())
icons_dir = DIST / 'icons'; icons_dir.mkdir(exist_ok=True)
for p in (APP / 'assets/icons').glob('*.png'):
    (icons_dir / p.name).write_bytes(p.read_bytes())

START_HERE = """میمو · خروجی آفلاین (ناوبری بومی ۹٫۳۵)
=========================================

۱) Mimo.html را دوبار کلیک کنید (یا در مرورگر گوشی باز کنید). تمام شد.
   نیازی به اینترنت، سرور، npm، خط فرمان یا نصب چیزی ندارد.
۲) نصب روی گوشی: همین پوشه را روی یک آدرس HTTPS قرار دهید (پیشنمایش زنده
   نیز همین کار را میکند)، سپس منوی مرورگر ← «افزودن به صفحهٔ اصلی / نصب اپ».
   فایل index.html همان اپ بهعلاوهٔ manifest و Service Worker است.
۳) ناوبری دقیقاً از میمو: یادگیری (نقشهٔ مسیر ← فصل ← درس ← خروج/پایان)،
   انتخاب مسیر، نمای کلی مسیر، جزئیات فصل، درگاه تمرین، آزمونها، امتیازها،
   پروفایل و دستیار هوشمند. پنج تب و تمام نشانههای طرح تأییدشده حفظ شدهاند.
۴) مسیر آموزشی: ۱۲ کتاب · ۶۰ فصل · ۱۸۰ درس، همگی از سرفصلهای پروتوتایپ
   تأییدشدهٔ v12.5-fa. تمرین هر درس از ۲۰ سؤال واقعی همان پروتوتایپ است.
   درسنامهٔ نهایی پس از تحویل منابع از «وارد کردن بستهٔ محتوا» جایگزین میشود.
۵) ساختار توکنها: سه معنا (طراحی CSS / پاداش و دفتر توکنها / زمینه و هزینهٔ
   هوش مصنوعی) همگی زنده، قابل خروجی و ذخیرهشده روی همین دستگاهاند.
۶) بخش هوش مصنوعی: چهار فاز LearnHarness (سنجش/برنامه/آموزش/تمرین)، گراف
   دانش، وارد کردن بسته، و شمارش توکن زمینه — کاملاً محلی.
   !!! بدون مدل زبانی، بدون اینترنت، بدون کلید API و بدون تولید متن !!!
   متنها عیناً از بستهٔ محتوا خوانده میشوند. ارائهدهندهٔ خارجی: not-configured.

هیچ دادههای به سرور فرستاده نمیشود. استنتاج از سرور میمو تأیید نشده
(SERVER CONFIRMED=0). قواعد پاداش، فرمولهای سروری و محتوای نهایی ادعایی نیستند.

تولید: {date}
""".format(date=datetime.datetime.now().isoformat(timespec='seconds'))
(DIST / 'START_HERE.txt').write_text(START_HERE, encoding='utf-8')

launcher = """<!doctype html>
<html lang="fa" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#7E4BDE">
<title>میمو · شروع کنید</title>
<link rel="manifest" href="./manifest.webmanifest">
<style>
:root{--primary:#7E4BDE;--bg:#F6F7FB;--card:#FFFFFF;--text:#252746;--line:#EDEEF6}
*{box-sizing:border-box}body{margin:0;min-height:100vh;background:var(--bg);color:var(--text);
font-family:Tahoma,"Segoe UI",sans-serif;display:flex;align-items:center;justify-content:center;padding:24px}
.card{max-width:520px;width:100%;background:var(--card);border:1px solid var(--line);
border-radius:18px;padding:28px;box-shadow:0 16px 40px rgba(37,39,70,.10)}
h1{margin:0 0 6px;font-size:26px}p{line-height:1.9;color:#4A4D85;font-size:14px}
a.btn{display:block;margin:12px 0;padding:15px;border-radius:12px;text-align:center;
text-decoration:none;font-weight:700;background:var(--bg);color:var(--text);border:1px solid var(--line)}
a.btn.main{background:var(--primary);color:#fff;border-color:var(--primary)}
small{display:block;margin-top:16px;line-height:1.9;color:#4A4D85}
</style></head><body><main class="card">
<h1>میمو · شروع کنید</h1>
<p>همهچیز آماده است. فقط یکی را بزنید؛ نیازی به اینترنت، سرور یا نصب وابستگی نیست.</p>
<a class="btn main" href="./index.html">► باز کردن اپلیکیشن (کلیک)</a>
<a class="btn" href="./Mimo.html" download="Mimo.html">↓ دانلود تکفایل Mimo.html</a>
<a class="btn" href="./Mimo.zip" download="Mimo.zip">↓ دانلود بستهٔ کامل Mimo.zip (شامل PWA)</a>
<a class="btn" href="./START_HERE.txt">راهنمای فارسی</a>
<small>نصب روی گوشی: همین صفحه را در مرورگر گوشی باز کنید و «افزودن به صفحهٔ اصلی / نصب اپلیکیشن» را بزنید.
ناوبری یادگیری دقیقاً از میمو ۹٫۳۵: نقشهٔ مسیر ← فصل ← درس ← خروج/پایان.
بدون LLM، بدون شبکه، بدون تولید متن · SERVER CONFIRMED=0</small>
</main></body></html>
"""
(DIST / 'launcher.html').write_text(launcher, encoding='utf-8')
readme = ROOT / 'app/docs/OUTPUT_GUIDE.md'
if readme.is_file():
    (DIST / 'README-fa.md').write_text(readme.read_text(encoding='utf-8'), encoding='utf-8')
else:
    (DIST / 'README-fa.md').write_text(START_HERE, encoding='utf-8')

# ---------------------------------------------------------------------------
# 4. ZIP + build manifest (hashes for every shipped file)
# ---------------------------------------------------------------------------
zip_path = DIST / 'Mimo.zip'
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in sorted(DIST.iterdir()):
        if p.is_file() and p.name not in ('Mimo.zip', 'BUILD_MANIFEST.json'):
            z.write(p, p.name)
    for p in sorted((DIST / 'icons').glob('*')):
        z.write(p, f'icons/{p.name}')

files = {}
for p in sorted(DIST.rglob('*')):
    if p.is_file() and p.name != 'BUILD_MANIFEST.json':
        b = p.read_bytes()
        files[str(p.relative_to(DIST))] = {'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b)}
manifest = {
    'generatedAt': datetime.datetime.now().isoformat(timespec='seconds'),
    'generator': 'app/tools/build_output.py (MIMO NATIVE)',
    'entry': {'oneFile': 'Mimo.html', 'pwa': 'index.html', 'launcher': 'launcher.html',
              'zip': 'Mimo.zip', 'guide': 'START_HERE.txt'},
    'shell': 'app/native/index.html',
    'controller': 'src/native.js',
    'bundledModules': order,
    'navigation': ['MainActivity/tabs', 'PathMap', 'ChapterActivity', 'LessonRenderer',
                   'QuitDialog', 'Celebration', 'SelectPath', 'PathOverview',
                   'SectionDetail', 'PracticeGate', 'ExamHub', 'AI', 'Tokens', 'Output'],
    'sourceSlot': SLOT,
    'honest': {'llm': False, 'network': False, 'generatedText': False,
               'externalProvider': 'not-configured', 'serverConfirmed': False},
    'files': files,
}
(DIST / 'BUILD_MANIFEST.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n',
                                          encoding='utf-8')
print('wrote dist/Mimo.zip', zip_path.stat().st_size, 'bytes;', len(files), 'files hashed')
print('DONE — open app/dist/Mimo.html by double-clicking it, or serve app/dist/ as a PWA.')
