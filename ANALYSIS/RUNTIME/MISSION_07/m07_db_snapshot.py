#!/usr/bin/env python3
"""MISSION 07 — snapshot private application storage pulled from the ORIGINAL
app sandbox on a rooted, controlled emulator. Emits schema, row counts and
row-level content as JSON. No inference: only what SQLite actually contains."""
import sys, json, sqlite3, pathlib, hashlib, os, datetime

root = pathlib.Path(sys.argv[1]); label = sys.argv[2]; out = pathlib.Path(sys.argv[3])
out.parent.mkdir(parents=True, exist_ok=True)

def sha(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()

res = {'label': label, 'timestamp_utc': datetime.datetime.utcnow().isoformat() + 'Z',
       'root': str(root), 'files': [], 'databases': [], 'errors': []}
if not root.exists():
    res['errors'].append('snapshot root does not exist: %s' % root)
else:
    for p in sorted(root.rglob('*')):
        if p.is_file():
            res['files'].append({'path': str(p.relative_to(root)), 'bytes': p.stat().st_size,
                                 'sha256': sha(p)})
    for p in sorted(root.rglob('*')):
        if not p.is_file(): continue
        # Room/SQLite main db files and WAL/SHM companions
        if p.suffix in ('.db', '.sqlite', '.sqlite3', '.wal', '.shm') or p.name.endswith('-wal') or p.name.endswith('-shm'):
            if p.suffix in ('.wal','.shm') or p.name.endswith('-wal') or p.name.endswith('-shm'):
                continue
            db = {'path': str(p.relative_to(root)), 'bytes': p.stat().st_size,
                  'sha256': sha(p), 'journal_mode': None, 'tables': [], 'error': None}
            try:
                con = sqlite3.connect('file:%s?mode=ro' % p.as_posix(), uri=True)
                cur = con.cursor()
                db['journal_mode'] = cur.execute('PRAGMA journal_mode').fetchone()[0]
                masters = cur.execute("SELECT type,name,tbl_name,sql FROM sqlite_master ORDER BY type,name").fetchall()
                db['schema'] = [{'type':m[0],'name':m[1],'tbl_name':m[2],'sql':m[3]} for m in masters]
                for m in masters:
                    if m[0] != 'table' or m[1].startswith('sqlite_'): continue
                    try:
                        n = cur.execute('SELECT COUNT(*) FROM "%s"' % m[1].replace('"','""')).fetchone()[0]
                        cols = [c[1] for c in cur.execute('PRAGMA table_info("%s")' % m[1].replace('"','""')).fetchall()]
                        rows = []
                        if n <= 200:
                            for r in cur.execute('SELECT * FROM "%s" LIMIT 200' % m[1].replace('"','""')).fetchall():
                                rows.append([str(x) if not isinstance(x, (bytes, bytearray)) else '<%d bytes>' % len(x) for x in r])
                        db['tables'].append({'name':m[1], 'columns':cols, 'row_count':n, 'rows':rows})
                    except Exception as e:
                        db['tables'].append({'name':m[1], 'error':str(e)})
                con.close()
            except Exception as e:
                db['error'] = str(e)
            res['databases'].append(db)
out.write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding='utf-8')
print('[db] label=%s files=%d databases=%d tables=%d' % (label, len(res['files']), len(res['databases']),
      sum(len(d.get('tables',[])) for d in res['databases'])))
