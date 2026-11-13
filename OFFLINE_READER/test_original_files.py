"""Check raw APK JSON bytes and curriculum order survive the packaging step."""
import base64, hashlib, importlib.util, json, tempfile, zipfile
from pathlib import Path
spec=importlib.util.spec_from_file_location('reader_build','OFFLINE_READER/build.py')
b=importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
with tempfile.TemporaryDirectory() as tmp:
    root='assets/lessons-en/tracks/'
    tracks='{"tracks":[{"id":1,"title":"Python","sections":[{"tutorialIds":[22,11]}]}]}'.encode()
    first=' { "tutorial": {"id":22,"title":"Print", "unusual":"سلام", "chapters":[]} }\n'.encode()
    second=b'{"tutorial":{"id":11,"title":"Variables","chapters":[]}}'
    apk=Path(tmp)/'fixture.apk'; out=Path(tmp)/'reader.html'
    with zipfile.ZipFile(apk,'w') as z:
        z.writestr(root+'tracks.json',tracks)
        z.writestr(root+'tutorial-11.json',second)
        z.writestr(root+'tutorial-22.json',first)
    b.SHA=hashlib.sha256(apk.read_bytes()).hexdigest();b.build(apk,out)
    html=out.read_text(); part=html.split('<script id="curriculum" type="application/json">',1)[1].split('</script>',1)[0]
    payload=json.loads(part)
    assert base64.b64decode(payload['tracksFile']) == tracks
    assert base64.b64decode(payload['tutorialFiles']['22']) == first
    assert base64.b64decode(payload['tutorialFiles']['11']) == second
    assert json.loads(base64.b64decode(payload['tracksFile']))['tracks'][0]['sections'][0]['tutorialIds']==[22,11]
print('PASS byte-exact original files and index order (synthetic fixture)')
