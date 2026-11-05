#!/usr/bin/env python3
"""Static verifier for the MIMO NATIVE one-click output (no dependencies)."""
from __future__ import annotations
import base64, hashlib, json, pathlib, re, sys, zipfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
APP = ROOT / 'app'
DIST = APP / 'dist'
SLOT = '__MIMO_SOURCE_B64_SLOT__'
checks = []


def check(label, ok, detail=''):
    checks.append((label, bool(ok), detail))
    print(('PASS  ' if ok else 'FAIL  ') + label + ((' — ' + str(detail)) if detail else ''))


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    one = (DIST / 'Mimo.html').read_bytes()
    text = one.decode('utf-8')
    check('dist/Mimo.html exists', one.startswith(b'<!doctype html>'), f'{len(one):,} bytes')
    check('approved v12.5-fa phone markup inlined verbatim',
          (APP / 'assets/phone.html').read_text(encoding='utf-8').strip() in text)

    approved = ['learn', 'select-path', 'path-overview', 'section-detail', 'lesson',
                'leaderboard', 'user-profile', 'profile', 'exam-hub', 'exam-run',
                'exam-result', 'ai', 'section-practice']
    native = ['native-studio', 'native-tokens', 'native-output', 'native-gate', 'native-done']
    for s in approved:
        check(f'screen «{s}» present', f'data-screen="{s}"' in text)
    # Native screens are created at runtime by the controller (dataset.screen),
    # so their names live in the inlined JS rather than in the static markup.
    for s in native:
        check(f'native screen «{s}» present', f"insertScreen('{s}'" in text)

    nav = text[text.index('id="tabs"'):text.index('id="tabs"') + 2600]
    check('5 approved tabs in exact order',
          re.findall(r'data-tab="([A-Za-z]+)"', nav) ==
          ['Learn', 'Practice', 'AI', 'Leaderboard', 'Profile'])

    markup = re.sub(r'<script\b[^>]*>[\s\S]*?</script>', '<script></script>', text, flags=re.I)
    markup = re.sub(r'<style\b[^>]*>[\s\S]*?</style>', '<style></style>', markup, flags=re.I)
    check('no external resource reference',
          not re.findall(r'<[^>]*\s(?:src|href)="(?!data:|#)([^"]+)"', markup, re.I))
    check('no ESM module tag', '<script type="module"' not in text)
    check('script tags balanced', text.lower().count('<script') == text.lower().count('</script>'))
    check('no network API in inline scripts',
          all(x not in text for x in ['fetch(', 'new XMLHttpRequest', 'new WebSocket', 'new EventSource']))
    check('no API key / LLM vendor literal in inline scripts',
          all(x not in text for x in ['AIza', 'api.openai.com', 'api.anthropic.com'])
          and not re.search(r'\bsk-[A-Za-z0-9_-]{16,}', text))
    check('approved payloads + native CSS + controller inlined',
          all(x in text for x in ['data-generated="mimo-bundle.js"',
                                  'data-src="../assets/proto-data.js"',
                                  'data-src="../assets/proto-ui.js"',
                                  'data-src="../assets/proto.css"',
                                  'data-src="../assets/native.css"']))
    check('legacy admin controller NOT bundled',
          '/* ---- src/app.js ---- */' not in text and '/* ---- src/plus.js ---- */' not in text)
    check('Mimo 9.35 navigation state machine present',
          all(x in text for x in ['nativeQuit', 'lesson:quit', 'profile:create',
                                  'ChapterActivity', 'PracticeGate']))
    check('full-screen ChapterActivity (no fake status bar / bottom tabs)',
          'data-fullscreen' in text and 'phone.dataset.fullscreen' in text)

    # Self-export round trip: the embedded payload IS the template of this file.
    m = re.search(r'<script id="mimoSource" type="text/plain">([A-Za-z0-9+/=]+)</script>', text)
    check('embedded source payload found', bool(m))
    if m:
        template = base64.b64decode(m.group(1)).decode('utf-8')
        check('payload is the canonical template', template.count(SLOT) == 1)
        check('payload regenerates this exact file',
              sha(template.replace(SLOT, m.group(1)).encode('utf-8')) == sha(one))

    idx = (DIST / 'index.html').read_text(encoding='utf-8')
    check('PWA host = one-file app + manifest + SW',
          'rel="manifest" href="./manifest.webmanifest"' in idx
          and 'serviceWorker.register' in idx and len(idx) > len(text))
    check('SW registration is a real trailing script, not injected inside the bundle',
          idx.rstrip().endswith('</script>\n</body>\n</html>')
          and idx.rfind('<script>\nif (\'serviceWorker\' in navigator') > idx.rfind('data-generated="mimo-bundle.js"'))
    man = json.loads((DIST / 'manifest.webmanifest').read_text(encoding='utf-8'))
    check('manifest is a standalone PWA', man.get('display') == 'standalone' and len(man.get('icons', [])) == 3)
    for ic in man['icons']:
        p = DIST / ic['src'].lstrip('./')
        b = p.read_bytes()
        w = int.from_bytes(b[16:20], 'big'); h = int.from_bytes(b[20:24], 'big')
        check(f'icon {p.name} is a PNG', b[:8] == b'\x89PNG\r\n\x1a\n' and w == h == int(ic['sizes'].split('x')[0]))
    sw = (DIST / 'sw.js').read_text(encoding='utf-8')
    check('service worker is GET-only, same-origin, cache-first',
          "req.method !== 'GET'" in sw and 'caches.match(req)' in sw
          and 'new URL(req.url).origin !== self.location.origin' in sw)

    zpath = DIST / 'Mimo.zip'
    with zipfile.ZipFile(zpath) as z:
        names = z.namelist()
        check('zip is valid and complete',
              all(n in names for n in ['Mimo.html', 'index.html', 'launcher.html', 'START_HERE.txt',
                                       'manifest.webmanifest', 'sw.js', 'icons/icon-192.png',
                                       'icons/icon-512.png', 'icons/maskable-512.png']), f'{len(names)} members')
        check('zip Mimo.html matches dist', z.read('Mimo.html') == one)
        check('zip has no corrupt member', z.testzip() is None)

    bm = json.loads((DIST / 'BUILD_MANIFEST.json').read_text(encoding='utf-8'))
    bad = [n for n, meta in bm['files'].items()
           if not (DIST / n).is_file() or sha((DIST / n).read_bytes()) != meta['sha256']]
    check('build manifest hashes match', not bad, ','.join(bad[:5]))
    check('build manifest declares honesty flags',
          bm['honest'] == {'llm': False, 'network': False, 'generatedText': False,
                           'externalProvider': 'not-configured', 'serverConfirmed': False})
    check('build manifest declares native controller', bm.get('controller') == 'src/native.js')
    check('build manifest declares the structured content layer',
          bm.get('content', {}).get('layoutDemoTextUsedAsLesson') is False
          and 'content-engine.js' in bm.get('bundledModules', [])
          and 'content-package.js' in bm.get('bundledModules', []))
    check('native content engine + 120 micro-lessons are bundled',
          all(x in text for x in ['/* ---- src/content-engine.js ---- */',
                                  'STRUCTURED_PACKAGE', 'nl-answerkey',
                                  'native-chapter-row', 'publishSetVersion']))
    check('prototype layout-demo text is NOT read into lesson content',
          'const lessonParas' not in text and 'browserBits' not in text)

    start = (DIST / 'START_HERE.txt').read_text(encoding='utf-8')
    check('Persian quick-start covers all three subsystems',
          all(x in start for x in ['مسیر آموزشی', 'ساختار توکنها', 'هوش مصنوعی', 'Mimo.html']))
    check('content form validator accepts the starter package',
          (APP / 'content/STARTER_PACKAGE.json').is_file()
          and json.loads((APP / 'content/STARTER_PACKAGE.json').read_text(encoding='utf-8'))['source']['contentStatus'] == 'placeholder')

    failed = [c[0] for c in checks if not c[1]]
    print(f'\nchecks: {len(checks)}  passed: {len(checks) - len(failed)}  failed: {failed}')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
