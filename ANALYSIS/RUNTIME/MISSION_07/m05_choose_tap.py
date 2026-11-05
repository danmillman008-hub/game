#!/usr/bin/env python3
"""Pick a tap target from an ORIGINAL uiautomator XML dump.
Compose exposes clickable android.view.View nodes with NO text of their own;
the visible label lives in a descendant TextView. This script therefore
derives a composite label from descendants, and never invents a node.
Prints: <x> <y> <label>  or  NONE <reason>"""
import sys, re, xml.etree.ElementTree as ET
xml_path = sys.argv[1]
avoid = set()
if len(sys.argv) > 2:
    for a in sys.argv[2].split(';'):
        if a.strip(): avoid.add(a.strip())
try:
    root = ET.parse(xml_path).getroot()
except Exception as e:
    print('NONE parse_error=%s' % e); sys.exit(0)

PRIMARY = ['get started', 'continue', 'next', "let's go", 'start learning',
           "i'm ready", 'start', 'choose', 'select', 'yes', 'skip',
           'not now', 'maybe later', 'begin', 'got it', 'ok', 'let’s go']
# Never tap these: account/login/purchase actions are outside this mission.
AVOID = ['i already have an account', 'log in', 'login', 'sign in', 'signin',
         'sign up', 'signup', 'password', 'email', 'forgot password',
         'subscribe', 'purchase', 'restore purchase', 'rate', 'share',
         'privacy policy', 'terms of service']
# A screen is treated as an authentication boundary only when it has a real
# password field, or email/sign-in text AND no usable primary action.
BOUNDARY_STRONG = ['password="true"']

def texts_under(n):
    out = []
    for d in n.iter('node'):
        if d is n: continue
        t = (d.get('text') or '').strip()
        if t: out.append(t)
    return out

def bounds(n):
    b = n.get('bounds') or ''
    m = re.match(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]', b)
    if not m: return None
    x1,y1,x2,y2 = map(int, m.groups())
    if x2 <= x1 or y2 <= y1: return None
    return (x1,y1,x2,y2,(x1+x2)//2,(y1+y2)//2)

raw = open(xml_path, encoding='utf-8', errors='replace').read()
strong_boundary = any(s in raw for s in BOUNDARY_STRONG)

nodes = []
for n in root.iter('node'):
    bb = bounds(n)
    if not bb: continue
    own = (n.get('text') or '').strip()
    desc = (n.get('content-desc') or '').strip()
    rid = (n.get('resource-id') or '').strip()
    clickable = (n.get('clickable') == 'true')
    descendants = texts_under(n)
    label = own or desc or (descendants[0] if descendants else '') or rid
    nodes.append(dict(text=own, label=label, rid=rid,
                      all_text=' '.join([own] + descendants + [desc]).lower(),
                      clickable=clickable, bounds=bb[0:4],
                      x=bb[4], y=bb[5], y2=bb[3],
                      package=n.get('package') or ''))

def forbidden(s):
    s = s.lower()
    return any(a in s for a in AVOID)

def key(n): return '%d,%d' % (n['x'], n['y'])

cands = []
for n in nodes:
    if not n['label'] or forbidden(n['label']): continue
    if key(n) in avoid: continue
    if strong_boundary and not any(p in n['label'].lower() for p in PRIMARY[:6]):
        continue
    lower = n['label'].lower()
    score = 0
    for i, p in enumerate(PRIMARY):
        if p in lower:
            score = 1000 - i*10
            break
    if score == 0:
        # prefer real clickable containers, especially lower on the screen
        score = (600 if n['clickable'] else 200) - min(n['y2']//60, 150)
    if n['clickable']: score += 120
    if n['y'] > 1200: score += 40
    cands.append((score, n))
if not cands:
    print('NONE auth_boundary' if strong_boundary else 'NONE no_candidate')
    sys.exit(0)
cands.sort(key=lambda t: -t[0])
best = cands[0][1]
print('%d %d %s' % (best['x'], best['y'], best['label'][:90].replace(' ', '_')))
