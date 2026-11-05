#!/usr/bin/env python3
"""Static integrity verifier for the offline app (no dependencies).

Checks that the approved v12.5-fa design is preserved, that the product shell
is complete, and that no server behaviour / forbidden tab slipped in.
Behavioural checks live in `npm test`; the protected prototype verifier is run
separately (mimo-ui/UPGRADE/tools/verify_upgrade.py).
"""
from __future__ import annotations
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
APP = ROOT / 'app'
PROTO = ROOT / 'mimo-ui' / 'UPGRADE' / 'DESIGN' / 'index.html'
EXPECTED = 'c356068daa5ccafbee46599897ad18bdf1e4f91f1ca23f36b1b8bd153dbfdb78'

checks = []


def check(label, ok, detail=''):
    checks.append((label, bool(ok), detail))
    print(('PASS  ' if ok else 'FAIL  ') + label + ((' — ' + detail) if detail else ''))


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    raw = PROTO.read_bytes()
    check('protected prototype sha256 == v12.5-fa', sha(raw) == EXPECTED)
    css = raw[raw.index(b'<style>') + 7:raw.index(b'</style>')]
    check('proto.css byte-identical', sha((APP / 'assets/proto.css').read_bytes()) == sha(css))
    a = raw.index(b'<div class="phone"')
    marker = b'\n    </div>\n  </div>\n\n  <aside class="spec">'
    phone = raw[a:raw.index(marker, a)] + b'\n    </div>\n'
    check('phone.html byte-identical', sha((APP / 'assets/phone.html').read_bytes()) == sha(phone))

    prov = json.loads((APP / 'assets/PROVENANCE.json').read_text(encoding='utf-8'))
    for name, expected in prov['artifacts'].items():
        check(f'provenance hash {name}', sha((APP / 'assets' / name).read_bytes()) == expected)

    text = raw.decode('utf-8')
    import re
    blocks = list(re.finditer(r'<script[^>]*>(.*?)</script>', text, re.S))
    data = '\n'.join(m.group(1) for m in blocks[:4]) + '\n'
    check('proto-data.js exact', sha((APP / 'assets/proto-data.js').read_bytes()) == sha(data.encode()))

    index = (APP / 'index.html').read_text(encoding='utf-8')
    check('index.html inlines approved phone verbatim',
          (APP / 'assets/phone.html').read_text(encoding='utf-8').strip() in index)
    nav = index[index.index('id="tabs"'):index.index('id="tabs"') + 2600]
    tabs = re.findall(r'data-tab="([A-Za-z]+)"', nav)
    check('5 approved tabs in exact order',
          tabs == ['Learn', 'Practice', 'AI', 'Leaderboard', 'Profile'], ','.join(tabs))
    check('no Max tab / مکس anywhere', 'data-tab="max"' not in index and 'مکس' not in index)
    for label in ['یادگیری', 'تمرین', 'هوش مصنوعی', 'امتیازها', 'پروفایل']:
        check(f'bottom label «{label}»', label in nav)
    screens = ['learn', 'select-path', 'path-overview', 'section-detail', 'lesson',
               'leaderboard', 'user-profile', 'profile', 'exam-hub', 'exam-run',
               'exam-result', 'ai', 'section-practice', 'study-plan', 'practice-bank']
    check('all 15 screens present', all(f'data-screen="{s}"' in index or
                                        f'data-screen="{s}"' in (APP / 'src/views.js').read_text(encoding='utf-8')
                                        for s in screens))
    for rel in ['src/app.js', 'src/store.js', 'src/engine.js', 'src/fixtures.js',
                'src/routes.js', 'src/views.js', 'src/nodes.js', 'src/harness.js', 'src/exam-template.js',
                'src/templates.js', 'src/util.js', 'src/token-economy.js',
                'src/learning-path.js', 'src/ai-studio.js', 'src/output-kit.js',
                'src/plus.js', 'src/design-tokens.js', 'src/starter-package.js',
                'src/pwa-assets.js', 'assets/node-match.css', 'assets/extra.css',
                'content/STARTER_PACKAGE.json', 'tools/build_output.py',
                'dist/Mimo.html', 'dist/index.html', 'dist/Mimo.zip',
                'server.js', 'sw.js', 'index.html']:
        check(f'required file {rel}', (APP / rel).is_file())
    app_src = '\n'.join((APP / rel).read_text(encoding='utf-8') for rel in
                        ['src/app.js', 'src/store.js', 'src/engine.js', 'src/routes.js'])
    check('no fetch/XHR/WebSocket in app logic',
          'fetch(' not in app_src and 'new XMLHttpRequest' not in app_src)
    check('offline flag present', 'serverConfirmed: false' in (APP / 'src/store.js').read_text(encoding='utf-8'))
    check('placeholder data isolated', (APP / 'src/fixtures.js').is_file()
          and 'PLACEHOLDER' in (APP / 'src/fixtures.js').read_text(encoding='utf-8'))
    for rel in ['README.md', 'docs/ARCHITECTURE.md', 'docs/DEVELOPMENT.md',
                'docs/TESTING.md', 'APP_FINAL_REPORT.md']:
        check(f'document {rel}', (APP / rel).is_file())

    failed = [c for c in checks if not c[1]]
    print(f'\nchecks: {len(checks)}  passed: {len(checks) - len(failed)}  failed: {[c[0] for c in failed]}')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
