#!/usr/bin/env python3
"""MISSION 07 — deterministic UI target resolution from an ORIGINAL
uiautomator dump. Unlike M05's generic choose_tap.py, this matches an EXPECTED
label from the archived run-003 chain; only if that label is absent does it fall
back to the generic chooser. Prints: <x> <y> <label> <match_mode>.
Never invents a node; coordinates come from the measured XML bounds.
"""
import sys, re, xml.etree.ElementTree as ET, subprocess, pathlib
xml_path = sys.argv[1]
expected = sys.argv[2] if len(sys.argv) > 2 else ''
avoid = set(x.strip() for x in (sys.argv[3].split(';') if len(sys.argv) > 3 else []) if x.strip())
# Optional 4th arg: comma-separated PREFERRED label keywords. A matching node
# wins over the generic chooser, making onboarding deterministic.
prefer = [x.strip() for x in (sys.argv[4].split('|') if len(sys.argv) > 4 else []) if x.strip()]

def bounds(n):
    m = re.match(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]', n.get('bounds') or '')
    if not m: return None
    x1,y1,x2,y2 = map(int, m.groups())
    if x2<=x1 or y2<=y1: return None
    return (x1+x2)//2, (y1+y2)//2, y2

def descendants_text(n):
    return [(d.get('text') or '').strip() for d in n.iter('node') if d is not n and (d.get('text') or '').strip()]

def norm(s):
    s = (s or '').lower().replace('&amp;', '&').replace('&amp', '&')
    s = s.replace('’', "'").replace('‘', "'").replace('\u2019', "'")
    return re.sub(r'[^a-z0-9]+', '', s)

try: root = ET.parse(xml_path).getroot()
except Exception as e:
    print('NONE parse_error=%s' % e); sys.exit(0)

nodes=[]
for n in root.iter('node'):
    b = bounds(n)
    if not b: continue
    own=(n.get('text') or '').strip(); desc=(n.get('content-desc') or '').strip()
    rid=(n.get('resource-id') or '').strip(); dtexts=descendants_text(n)
    label = own or desc or (dtexts[0] if dtexts else '') or rid
    alltext = ' '.join([own, desc, rid] + dtexts)
    nodes.append(dict(x=b[0], y=b[1], y2=b[2], label=label, alltext=alltext,
                      clickable=n.get('clickable')=='true', enabled=n.get('enabled')=='true',
                      rid=rid, key='%d,%d'%(b[0],b[1])))

# Preferred labels first (e.g. "Web apps" to select the HTML path).
if prefer:
    for kw in prefer:
        k = norm(kw)
        for mode, fn in [('preferred_exact', lambda n: norm(n['label']) == k),
                         ('preferred_contains', lambda n: k in norm(n['alltext']))]:
            for n in nodes:
                if n['enabled'] and n['clickable'] and n['key'] not in avoid and fn(n):
                    print('%d %d %s %s' % (n['x'], n['y'], n['label'][:90].replace(' ', '_'), mode))
                    sys.exit(0)

e = norm(expected)
if e:
    # 1) exact normalised label, 2) label contains expected, 3) any node text contains expected
    for mode, fn in [('exact', lambda n: norm(n['label'])==e),
                     ('label_contains', lambda n: e in norm(n['label'])),
                     ('alltext_contains', lambda n: e in norm(n['alltext']))]:
        for n in nodes:
            if n['enabled'] and n['key'] not in avoid and fn(n):
                print('%d %d %s %s' % (n['x'], n['y'], n['label'][:90].replace(' ','_'), mode))
                sys.exit(0)

# fallback: M05 generic chooser (bounded, never crosses auth/purchase boundary)
helper = pathlib.Path(__file__).with_name('m05_choose_tap.py')
if not helper.exists():
    helper = pathlib.Path('ANALYSIS/RUNTIME/MISSION_05/choose_tap.py')
try:
    out = subprocess.check_output([sys.executable, str(helper), xml_path,
                                  ';'.join(avoid)], stderr=subprocess.DEVNULL, timeout=20).decode().strip()
    if out and not out.startswith('NONE'):
        p = out.split(None, 2); print('%s %s %s fallback' % (p[0], p[1], p[2] if len(p)>2 else ''))
        sys.exit(0)
    print('NONE no_target')
except Exception as e:
    print('NONE fallback_error=%s' % e)
