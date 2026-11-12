#!/usr/bin/env python3
"""Create one self-contained offline reader from the verified user's APK."""
import argparse, hashlib, json, zipfile
from pathlib import Path
SHA='48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a'
def build(apk,out):
    h=hashlib.sha256(apk.read_bytes()).hexdigest()
    if h!=SHA: raise ValueError('Unexpected original APK SHA-256: '+h)
    root='assets/lessons-en/tracks/'
    with zipfile.ZipFile(apk) as z:
        tracks=json.loads(z.read(root+'tracks.json'))
        if not isinstance(tracks,dict) or not isinstance(tracks.get('tracks'),list):raise ValueError('Unexpected tracks schema')
        tutorials={}
        for name in z.namelist():
            if name.startswith(root+'tutorial-') and name.endswith('.json'):
                raw=json.loads(z.read(name)); t=raw['tutorial']; tutorials[str(t['id'])]=t
        missing=sorted({str(x) for t in tracks['tracks'] for s in t.get('sections',[]) for x in s.get('tutorialIds',[]) if str(x) not in tutorials})
        if missing: raise ValueError('Missing tutorial assets: '+repr(missing[:30]))
    # Keep the normal learning content, not unused hard-mode copies and metadata.
    small_tracks=[{'id':t['id'],'title':t.get('title',''),
                   'descriptionContent':t.get('descriptionContent',''),
                   'sections':[{'name':s.get('name',''), 'description':s.get('description',''),
                                'tutorialIds':s.get('tutorialIds',[])} for s in t.get('sections',[])]}
                  for t in tracks['tracks']]
    small_tutorials={k:{'id':t['id'],'title':t.get('title',''), 'type':t.get('type',''),
                          'chapters':[{'id':c.get('id'),'title':c.get('title',''),
                                       'lessons':[{key:l[key] for key in ('id','title','contentType','interactiveContent','executableContent') if key in l} for l in c.get('lessons',[])]}
                                      for c in t.get('chapters',[])]} for k,t in tutorials.items()}
    payload=json.dumps({'tracks':small_tracks,'tutorials':small_tutorials},ensure_ascii=True,separators=(',',':')).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
    template=Path(__file__).with_name('template.html').read_text(encoding='utf8')
    if template.count('__CURRICULUM__')!=1:raise ValueError('template placeholder error')
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(template.replace('__CURRICULUM__',payload),encoding='utf8')
    chapters=sum(len(x.get('chapters',[])) for x in tutorials.values()); lessons=sum(len(c.get('lessons',[])) for x in tutorials.values() for c in x.get('chapters',[]))
    print(f'tracks={len(tracks["tracks"])} tutorials={len(tutorials)} chapters={chapters} lessons={lessons} bytes={out.stat().st_size} sha256={hashlib.sha256(out.read_bytes()).hexdigest()}')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--apk',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();build(a.apk,a.out)
