#!/usr/bin/env python3
"""Generate the standalone, self-contained app/index.html.

The approved phone markup is inlined verbatim from assets/phone.html so the
product has no build step at runtime and works with no network at all.
Run again after re-running extract_from_prototype.py.
"""
from __future__ import annotations
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
APP = ROOT / 'app'
PHONE = (APP / 'assets' / 'phone.html').read_text(encoding='utf-8')

TEMPLATE = '''<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#F6F7FB">
<meta name="description" content="اپلیکیشن آفلاین یادگیری بر پایهٔ طرح نهایی v12.5-fa">
<title>میمو · اپلیکیشن آفلاین</title>
<link rel="manifest" href="./manifest.webmanifest">
<link rel="stylesheet" href="./assets/proto.css">
<link rel="stylesheet" href="./assets/motion.css">
<link rel="stylesheet" href="./assets/node-match.css">
</head>
<body class="app-body">
<main class="app-stage" aria-label="اپلیکیشن آفلاین میمو">
<!-- APPROVED v12.5-fa PHONE MARKUP: byte-identical to assets/phone.html -->
__PHONE__
</main>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<noscript><div class="banner warn">برای اجرای اپلیکیشن، جاوااسکریپت را فعال کنید.</div></noscript>

<!-- Approved design payloads and UI renderer (working copies, read-only source). -->
<script src="./assets/proto-data.js"></script>
<script src="./assets/proto-ui.js"></script>
<!-- Application controller: state, routes, lifecycle, offline persistence. -->
<script type="module" src="./src/app.js"></script>
<script>
if ('serviceWorker' in navigator && location.protocol.indexOf('http') === 0) {
  window.addEventListener('load', function () {
    navigator.serviceWorker.register('./sw.js', {scope: './'}).catch(function () {});
  });
}
</script>
</body>
</html>
'''

out = TEMPLATE.replace('__PHONE__', PHONE.rstrip('\n'))
(APP / 'index.html').write_text(out, encoding='utf-8')
print('wrote app/index.html', len(out), 'chars; phone bytes', len(PHONE))
