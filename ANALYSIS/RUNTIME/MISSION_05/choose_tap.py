#!/usr/bin/env python3
"""Pick a tap target from an ORIGINAL uiautomator XML dump.
Prints: <x> <y> <text>  or  NONE <reason>
Only reads the real dumped hierarchy; never invents nodes."""
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
           'not now', 'maybe later', 'begin', 'got it', 'ok']
AVOID = ['i already have an account', 'log in', 'login', 'sign in', 'signin',
         'sign up', 'signup', 'password', 'email', 'forgot password',
         'subscribe', 'purchase', 'restore purchase', 'rate', 'share']
AUTH = ['log in', 'login', 'sign in', 'sign up', 'email', 'password',
        'i already have an account']

nodes = []
for n in root.iter('node'):
    txt = (n.get('text') or '').strip()
    desc = (n.get('content-desc') or '').strip()
    rid = (n.get('resource-id') or '').strip()
    b = n.get('bounds') or ''
    m = re.match(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]', b)
    if not m: continue
    x1,y1,x2,y2 = map(int, m.groups())
    if x2 <= x1 or y2 <= y1: continue
    clickable = (n.get('clickable') == 'true')
    label = txt or desc or rid
    nodes.append(dict(text=txt, desc=desc, rid=rid, bounds=b,
                      x=(x1+x2)//2, y=(y1+y2)//2, y2=y2,
                      clickable=clickable, label=label,
                      package=n.get('package') or ''))

def key(p): return '%d,%d' % (p['x'], p['y'])
def forbidden(s):
    s = s.lower()
    return any(a in s for a in AVOID)

# 0) Explicit authentication boundary detection
alltext = ' | '.join((n['text'] + ' ' + n['desc']).lower() for n in nodes)
if any(a in alltext for a in AUTH):
    other = [n for n in nodes if n['clickable'] and n['label'] and not forbidden(n['label'])]
    if not other:
        print('NONE auth_boundary'); sys.exit(0)

cands = []
for n in nodes:
    if not n['label']: continue
    if forbidden(n['label']): continue
    if key(n) in avoid: continue
    lower = n['label'].lower()
    score = 0
    for i, p in enumerate(PRIMARY):
        if p in lower:
            score = 1000 - i*10
            break
    if score == 0:
        if n['clickable']: score = 500 - min(n['y2']//40, 200)
        else: score = 100
    # prefer buttons in lower half of screen for onboarding CTAs
    if n['y'] > 1200 and score >= 500: score += 50
    cands.append((score, n))
if not cands:
    print('NONE no_candidate'); sys.exit(0)
cands.sort(key=lambda t: -t[0])
best = cands[0][1]
print('%d %d %s' % (best['x'], best['y'], best['label'][:90].replace(' ', '_')))
