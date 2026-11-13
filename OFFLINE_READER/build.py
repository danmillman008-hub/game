#!/usr/bin/env python3
"""Create one self-contained offline reader from the verified user's APK."""
import argparse, base64, hashlib, json, zipfile
from pathlib import Path
SHA='48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a'
def build(apk,out):
    h=hashlib.sha256(apk.read_bytes()).hexdigest()
    if h!=SHA: raise ValueError('Unexpected original APK SHA-256: '+h)
    root='assets/lessons-en/tracks/'
    with zipfile.ZipFile(apk) as z:
        tracks_bytes=z.read(root+'tracks.json')
        tracks=json.loads(tracks_bytes)
        if not isinstance(tracks,dict) or not isinstance(tracks.get('tracks'),list):raise ValueError('Unexpected tracks schema')
        tutorials={}
        source_files={}
        for name in z.namelist():
            if name.startswith(root+'tutorial-') and name.endswith('.json'):
                source=z.read(name); raw=json.loads(source); t=raw['tutorial']; key=str(t['id'])
                if key in tutorials: raise ValueError('Duplicate tutorial id: '+key)
                tutorials[key]=t
                source_files[key]=base64.b64encode(source).decode('ascii')
        missing=sorted({str(x) for t in tracks['tracks'] for s in t.get('sections',[]) for x in s.get('tutorialIds',[]) if str(x) not in tutorials})
        if missing: raise ValueError('Missing tutorial assets: '+repr(missing[:30]))
    # Embed the original files byte-for-byte, rather than discarding fields or
    # reordering objects. Decode tutorial JSON only when its ID is opened.
    payload=json.dumps({'format':'original-base64-v1',
                        'tracksFile':base64.b64encode(tracks_bytes).decode('ascii'),
                        'tutorialFiles':source_files},separators=(',',':'))
    template=Path(__file__).with_name('template.html').read_text(encoding='utf8')
    if template.count('__CURRICULUM__')!=1:raise ValueError('template placeholder error')
    reference_css=Path('app/assets/proto.css').read_text(encoding='utf8')
    if template.count('__REFERENCE_CSS__') != 1: raise ValueError('reference CSS placeholder error')
    output=template.replace('__REFERENCE_CSS__',reference_css).replace('__CURRICULUM__',payload)
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(output,encoding='utf8')
    chapters=sum(len(x.get('chapters',[])) for x in tutorials.values()); lessons=sum(len(c.get('lessons',[])) for x in tutorials.values() for c in x.get('chapters',[]))
    print(f'tracks={len(tracks["tracks"])} tutorials={len(tutorials)} chapters={chapters} lessons={lessons} bytes={out.stat().st_size} sha256={hashlib.sha256(out.read_bytes()).hexdigest()}')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--apk',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();build(a.apk,a.out)
