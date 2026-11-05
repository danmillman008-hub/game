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
        # Identify SQLite by MAGIC, not by filename: Mimo/Room databases can be
        # extensionless (e.g. 'mixpanel') and -wal/-shm are companions.
        try:
            is_sqlite = p.open('rb').read(16) == b'SQLite format 3\x00'
        except Exception:
            is_sqlite = False
        is_companion = p.suffix in ('.wal','.shm','.journal') or p.name.endswith(('-wal','-shm','-journal'))
        if is_sqlite and not is_companion:
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
                        limit = 200 if n <= 200 else 20
                        for r in cur.execute('SELECT * FROM "%s" LIMIT %d' % (m[1].replace('"','""'), limit)).fetchall():
                            rows.append([str(x) if not isinstance(x, (bytes, bytearray)) else '<%d bytes>' % len(x) for x in r])
                        groups = {}
                        for c in cols:
                            if c in ('is_completed','in_queue','is_practice_progress','tries','attempts','track_id'):
                                try:
                                    groups[c] = [list(map(str, r)) for r in cur.execute(
                                        'SELECT "%s", COUNT(*) FROM "%s" GROUP BY "%s" ORDER BY 2 DESC LIMIT 20'
                                        % (c, m[1].replace('"','""'), c)).fetchall()]
                                except Exception: pass
                        db['tables'].append({'name':m[1], 'columns':cols, 'row_count':n,
                                             'rows':rows, 'row_sample_limit':limit, 'group_counts':groups})
                    except Exception as e:
                        db['tables'].append({'name':m[1], 'error':str(e)})
                con.close()
            except Exception as e:
                db['error'] = str(e)
            res['databases'].append(db)
out.write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding='utf-8')
print('[db] label=%s files=%d databases=%d tables=%d' % (label, len(res['files']), len(res['databases']),
      sum(len(d.get('tables',[])) for d in res['databases'])))
