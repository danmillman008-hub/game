#!/usr/bin/env python3
"""List clickable short-label nodes (quiz options) and a primary CTA from an
ORIGINAL uiautomator dump. Prints lines: <x> <y> <kind> <text>"""
import sys, re, xml.etree.ElementTree as ET
try: root=ET.parse(sys.argv[1]).getroot()
except Exception as e: print('ERROR',e); sys.exit(0)
for n in root.iter('node'):
    if n.get('clickable')!='true': continue
    b=n.get('bounds') or ''
    m=re.match(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]',b)
    if not m: continue
    x1,y1,x2,y2=map(int,m.groups())
    x,y=(x1+x2)//2,(y1+y2)//2
    texts=[(d.get('text') or '').strip() for d in n.iter('node')]
    texts=[t for t in texts if t]
    label=texts[0] if texts else (n.get('content-desc') or n.get('resource-id') or '')
    if not label: continue
    if re.fullmatch(r'[A-Za-z0-9#@.,_+\-/*()<>/]{1,3}',label):
        kind='OPTION'
    elif label.lower() in ('continue','check','submit','next','got it','start practicing'):
        kind='CTA'
    else: continue
    print(x,y,kind,label.replace(' ','_')[:60])
