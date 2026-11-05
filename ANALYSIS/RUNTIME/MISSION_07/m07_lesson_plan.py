#!/usr/bin/env python3
"""MISSION 07 — classify a live lesson screen and produce a controlled
wrong/correct answer plan. Correct/wrong option labels are taken VERBATIM from
the ORIGINAL APK's shipped `assets/lessons-en/tracks/` interactiveContent:
  tutorial-904.json  lesson 151403  -> webview Q/R/D, correctLetter='D'
  tutorial-1103.json lesson 123420  -> <selection> correct item value=1
Outputs JSON only; never invents coordinates (all from uiautomator bounds).
"""
import sys, re, json, xml.etree.ElementTree as ET, html, pathlib
xml_path = sys.argv[1]
ANSWERS = {}
_ap = pathlib.Path(__file__).resolve().parents[2] / 'ANALYSIS/MISSION_07/RUNTIME_TRACE/SHIPPED_CONTENT/SELECTION_ANSWERS.json'
if not _ap.exists():
    _ap = pathlib.Path('ANALYSIS/MISSION_07/RUNTIME_TRACE/SHIPPED_CONTENT/SELECTION_ANSWERS.json')
if _ap.exists():
    try: ANSWERS = json.loads(_ap.read_text(encoding='utf-8')).get('by_question', {})
    except Exception: pass
try: root = ET.parse(xml_path).getroot()
except Exception as e:
    print(json.dumps({'type':'PARSE_ERROR','error':str(e)})); sys.exit(0)

raw = open(xml_path, encoding='utf-8', errors='replace').read()
nodes = []
for n in root.iter('node'):
    m = re.match(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]', n.get('bounds') or '')
    if not m: continue
    x1,y1,x2,y2 = map(int, m.groups())
    own = (n.get('text') or '').strip()
    desc = (n.get('content-desc') or '').strip()
    rid = (n.get('resource-id') or '').strip()
    dtexts = [(d.get('text') or '').strip() for d in n.iter('node') if d is not n and (d.get('text') or '').strip()]
    label = own or desc or (dtexts[0] if dtexts else '') or rid
    nodes.append({'x':(x1+x2)//2,'y':(y1+y2)//2,'label':label,
                  'alltext':' '.join([own,desc,rid]+dtexts),
                  'clickable':n.get('clickable')=='true','enabled':n.get('enabled')=='true',
                  'rid':rid,'x1':x1,'x2':x2,'y1':y1,'y2':y2})
def find(label, require_clickable=True):
    t = label.lower().replace('&amp;', '&')
    cands = [n for n in nodes if (not require_clickable) or (n['clickable'] and n['enabled'])]
    for n in cands:                       # exact label wins
        if n['label'].lower().replace('&amp;', '&') == t:
            return {'x':n['x'],'y':n['y'],'label':n['label'],'enabled':n['enabled']}
    for n in cands:                       # then substring
        if t in n['label'].lower() or t in n['alltext'].lower():
            return {'x':n['x'],'y':n['y'],'label':n['label'],'enabled':n['enabled']}
    return None
def cta():
    for lab in ('submit','check','continue','try again','got it','next','start practicing'):
        f = find(lab)
        if f and f['label'].strip(): return dict(f, source='label')
    # Compose exposes the primary CTA as a text-less clickable container at the
    # bottom of the screen (measured in NAV-28.xml: [42,2179][1038,2305]).
    geo = [n for n in nodes if n['clickable'] and n['y1'] > 1900 and (n['x2']-n['x1']) > 500]
    if geo:
        n = max(geo, key=lambda n: n['y1'])
        return {'x':n['x'],'y':n['y'],'label':'<bottom CTA container>',
                'enabled':n['enabled'],'source':'geometry'}
    return None

out = {'source_xml':xml_path,'clickable_count':sum(1 for n in nodes if n['clickable']),
       'texts':[n['label'] for n in nodes if n['label']][:40]}
if 'Guess the letter' in raw or '_ O G' in raw:
    q, d = find('Q'), find('D')
    if q and d:
        out.update(type='WEBVIEW_LETTER_151403', shipped_ref='assets/lessons-en/tracks/tutorial-904.json lesson 151403',
                   correct_letter='D', wrong=q, correct=d, cta=cta(),
                   explanation='webview JS sets correctLetter=D; wrong tap disables that button')
    else:
        out.update(type='WEBVIEW_LETTER_UNRESOLVED')
else:
    # General selection lesson: match a shipped question against the LIVE XML.
    # uiautomator stores visible strings in ATTRIBUTES, not between tags.
    texts = re.findall(r'(?:text|content-desc)="([^"]*)"', raw)
    plain = html.unescape(' '.join(texts))
    plain = re.sub(r'\s+', ' ', plain).lower()
    matched = None
    for q, meta in ANSWERS.items():
        if len(q) < 12: continue
        if q.lower() in plain:
            matched = (q, meta); break
    if matched:
        q, meta = matched
        correct = None; wrong = None
        for t in meta['correct']:
            correct = find(t)
            if correct: break
        for t in meta['wrong']:
            wrong = find(t)
            if wrong: break
        if correct and wrong:
            out.update(type='SELECTION_SHIPPED', shipped_ref=meta['tutorial_file']+' lesson '+str(meta['lesson_id']),
                       question=q, correct_text=meta['correct'], wrong_texts=meta['wrong'],
                       multiple=meta.get('multiple'), wrong=wrong, correct=correct, cta=cta(),
                       explanation='shipped <selection> item correct="true"')
        else:
            out.update(type='SELECTION_SHIPPED_UNRESOLVED', question=q,
                       shipped_ref=meta['tutorial_file']+' lesson '+str(meta['lesson_id']))
    else:
        # Generic short-option lesson (no shipped answer available -> UNKNOWN, no guess)
        opts = [n for n in nodes if n['clickable'] and n['enabled'] and re.fullmatch(r'[A-Za-z0-9]{1,3}', n['label'])]
        out.update(type='UNCLASSIFIED_LESSON', option_labels=[n['label'] for n in opts],
                   note='no shipped correct-answer evidence: do NOT guess')
print(json.dumps(out, indent=1, ensure_ascii=False))
