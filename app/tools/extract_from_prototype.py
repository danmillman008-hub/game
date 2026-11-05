#!/usr/bin/env python3
"""Build a WORKING COPY of the approved v12.5-fa prototype's design assets.

READ-ONLY with respect to the protected prototype. Writes only into app/assets/.
The product reuses the approved CSS and phone markup BYTE-FOR-BYTE; only the
prototype's demo control script is patched (guards + persistence/export hooks).

Usage:  python3 app/tools/extract_from_prototype.py
"""
from __future__ import annotations
import hashlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PROTO = ROOT / 'mimo-ui' / 'UPGRADE' / 'DESIGN' / 'index.html'
OUT = ROOT / 'app' / 'assets'
EXPECTED_SHA = 'c356068daa5ccafbee46599897ad18bdf1e4f91f1ca23f36b1b8bd153dbfdb78'


def main() -> int:
    if not PROTO.is_file():
        print('PROTOTYPE MISSING', PROTO)
        return 1
    s = PROTO.read_text(encoding='utf-8')
    sha = hashlib.sha256(s.encode('utf-8')).hexdigest()
    if sha != EXPECTED_SHA:
        print('PROTOTYPE HASH MISMATCH: expected', EXPECTED_SHA, 'got', sha)
        return 1

    OUT.mkdir(parents=True, exist_ok=True)

    # 1) CSS — exact bytes, no edits.
    css = s[s.index('<style>') + len('<style>'):s.index('</style>')]
    (OUT / 'proto.css').write_text(css, encoding='utf-8')

    # 2) Phone markup — exact bytes (all 13 approved screens + 5 tabs + sheets).
    a = s.index('<div class="phone"')
    marker = '\n    </div>\n  </div>\n\n  <aside class="spec">'
    b = s.index(marker, a)
    phone = s[a:b] + '\n    </div>\n'
    (OUT / 'phone.html').write_text(phone, encoding='utf-8')

    # 3) Data payloads — exact bytes (GEO / LEARN / NODE / KONKUR).
    blocks = list(re.finditer(r'<script[^>]*>(.*?)</script>', s, re.S))
    if len(blocks) != 5:
        print('unexpected script block count', len(blocks))
        return 1
    data = '\n'.join(block.group(1) for block in blocks[:4]) + '\n'
    (OUT / 'proto-data.js').write_text(data, encoding='utf-8')

    # 4) Working copy of the demo controller, with minimal, documented patches.
    ui = blocks[4].group(1)
    patches = [
        # (a) product shell has no prototype chrome buttons
        ('  q("#themeBtn").addEventListener("click",function()',
         '  var themeBtn=q("#themeBtn");\n  if(themeBtn)themeBtn.addEventListener("click",function()'),
        ('  q("#dirBtn").addEventListener("click",function(){',
         '  var dirBtn=q("#dirBtn");\n  if(dirBtn)dirBtn.addEventListener("click",function(){'),
        # (b) navigation hook so the app can persist the last screen
        ('  function go(name){\n    var prev=',
         '  function go(name){\n    if(window.PROTO_NAV)try{window.PROTO_NAV(name)}catch(e){}\n    var prev='),
        # (c) persist saved exam; called after SAVED is built
        ('    toast("پیشرفت ذخیره شد — بعداً از همان سؤال ادامه میدهید");\n  }',
         '    if(window.PROTO_PERSIST)try{window.PROTO_PERSIST(SAVED)}catch(e){}\n    toast("پیشرفت ذخیره شد — بعداً از همان سؤال ادامه میدهید");\n  }'),
        # (d) clear persisted snapshot when an exam finishes / is resumed
        ('    SAVED=null;q("#resumeBar").hidden=true;',
         '    SAVED=null;q("#resumeBar").hidden=true;if(window.PROTO_PERSIST)try{window.PROTO_PERSIST(null)}catch(e){}'),
        ('    q("#resumeBar").hidden=true;SAVED=null;',
         '    q("#resumeBar").hidden=true;SAVED=null;if(window.PROTO_PERSIST)try{window.PROTO_PERSIST(null)}catch(e){}'),
        # (e) export the UI API for the app controller
        ('  /* v8 · node positions re-applied at runtime from the injected code geometry */',
         '''  /* ---- APP HOOKS (working copy only; protected prototype is untouched) ---- */
  window.PROTO={
    go:go,toast:toast,fa:fa,paintIcons:paintIcons,icon:icon,
    tabMap:tabMap,tabScreen:tabScreen,openExam:openExam,resumeExam:resumeExam,
    renderQuestion:renderQuestion,applyPolicy:applyPolicy,render:render,
    questions:QBANK,bankSize:QTOTAL,
    currentScreen:function(){var e=q(".screen.on");return e?e.dataset.screen:"learn"},
    getSaved:function(){return SAVED},
    setSaved:function(v){SAVED=v;var rb=q("#resumeBar");if(!rb)return;
      rb.hidden=!v;if(v){q("#resumeText").textContent="«"+v.exam+"» · سؤال "+fa(v.qi+1)+" ذخیره شد"}},
    examState:function(){return {exam:q("#examTitle").textContent,kind:EXAM_KIND,qi:QI,
      answers:Object.assign({},ANSWERS),checked:Object.assign({},CHECKED),
      marks:Object.assign({},MARKS),minutes:q("#timerMinutes").value,
      timer:{state:T.state,remaining:T.remaining,total:T.total},qt:QTOTAL}},
    practice:renderPractice
  };
  /* v8 · node positions re-applied at runtime from the injected code geometry */'''),
    ]
    for old, new in patches:
        if old not in ui:
            print('PATCH ANCHOR MISSING:', old[:70])
            return 1
        ui = ui.replace(old, new, 1)
    (OUT / 'proto-ui.js').write_text(ui, encoding='utf-8')

    manifest = {
        'source': 'mimo-ui/UPGRADE/DESIGN/index.html',
        'version': 'v12.5-fa',
        'source_sha256': sha,
        'artifacts': {
            'proto.css': hashlib.sha256(css.encode()).hexdigest(),
            'phone.html': hashlib.sha256(phone.encode()).hexdigest(),
            'proto-data.js': hashlib.sha256(data.encode()).hexdigest(),
            'proto-ui.js': hashlib.sha256(ui.encode()).hexdigest(),
        },
        'note': ('proto.css, phone.html and proto-data.js are exact byte copies of the '
                 'approved design. proto-ui.js is a working copy with 6 documented patches '
                 '(null guards, navigation/persistence hooks, exported API).'),
    }
    import json
    (OUT / 'PROVENANCE.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n',
                                         encoding='utf-8')
    print('prototype sha OK:', sha)
    print('assets:', ', '.join(sorted(p.name for p in OUT.iterdir())))
    return 0


if __name__ == '__main__':
    sys.exit(main())
