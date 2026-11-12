"""Transfer a tested artifact through a one-time Drive resumable session.
The session URL remains encrypted in git and is never printed.
"""
import hashlib
import json
import os
from pathlib import Path
import urllib.request

root = Path(os.environ['RUNNER_TEMP'])
url = (root / 'session').read_text().strip()
apk = root / 'source/candidate.apk'
size = apk.stat().st_size
sha = hashlib.sha256()
md5 = hashlib.md5()
with apk.open('rb') as f:
    offset = 0
    while offset < size:
        data = f.read(8 * 1024 * 1024)
        sha.update(data)
        md5.update(data)
        final = offset + len(data) == size
        req = urllib.request.Request(url, data=data, method='PUT', headers={
            'Content-Type': 'application/vnd.android.package-archive',
            'X-Goog-Upload-Offset': str(offset),
            'X-Goog-Upload-Command': 'upload, finalize' if final else 'upload',
            'X-Goog-Upload-Total-Size': str(size),
        })
        try:
            with urllib.request.urlopen(req, timeout=120) as response:
                status = response.headers.get('X-Goog-Upload-Status')
                body = response.read()
        except Exception as e:
            raise RuntimeError(f'Upload failed at byte {offset}: {type(e).__name__}') from None
        if status != ('final' if final else 'active'):
            raise RuntimeError(f'Unexpected upload status {status!r} at byte {offset}')
        offset += len(data)
print('bytes=', size, 'sha256=', sha.hexdigest(), 'md5=', md5.hexdigest())
print('drive_result=', body.decode())
