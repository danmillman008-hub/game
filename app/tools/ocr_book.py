#!/usr/bin/env python3
"""OCR the scanned Persian biology book into resumable per-page JSON.

Output is RAW OCR and is kept OUT OF GIT (app/content/source/ is gitignored).
It is an intermediate artifact; only form-conformant structured packages are
committed. No content is authored or invented here.

Usage:
  python3 app/tools/ocr_book.py --pdf <book.pdf> --out app/content/source/biology-12 \
      --workers 4 --dpi 200
"""
from __future__ import annotations
import argparse, hashlib, json, multiprocessing as mp, os, sys, time

import pymupdf
from PIL import Image
from tesserocr import PyTessBaseAPI, PSM, OEM, RIL

_W = {}


def init_worker(pdf, out, dpi, tessdata, psm, lang, boxes_only=False):
    _W['doc'] = pymupdf.open(pdf)
    _W['out'] = out
    _W['dpi'] = dpi
    _W['tessdata'] = tessdata
    _W['psm'] = psm
    _W['lang'] = lang
    _W['boxes_only'] = boxes_only
    _W['api'] = PyTessBaseAPI(path=tessdata, lang=lang, psm=psm, oem=OEM.LSTM_ONLY)
    _W['api'].SetVariable('preserve_interword_spaces', '1')


def ocr_page(n):
    """n is 1-based page number."""
    doc, api = _W['doc'], _W['api']
    out = _W['out']
    dest = os.path.join(out, 'pages', f'page-{n:04d}.json')
    if os.path.isfile(dest) and not _W.get('force'):
        return {'page': n, 'status': 'skipped'}
    t0 = time.time()
    page = doc[n - 1]
    pix = page.get_pixmap(dpi=_W['dpi'], colorspace=pymupdf.csGRAY, alpha=False)
    img = Image.frombytes('L', (pix.width, pix.height), pix.samples)
    api.SetImage(img)
    text = api.GetUTF8Text()
    conf = api.MeanTextConf()
    # GetTSVText gives word-level boxes (left/top/width/height/conf) needed to
    # reconstruct the book's TWO-COLUMN layout during structuring.
    words = []
    try:
        for row in api.GetTSVText(0).splitlines()[1:]:
            c = row.split('\t')
            if len(c) < 12 or c[11].strip() == '' or c[0] != '5':
                continue
            words.append({'text': c[11], 'conf': float(c[10]),
                          'bbox': [int(c[6]), int(c[7]), int(c[8]), int(c[9])],
                          'block': int(c[2]), 'par': int(c[3]), 'line': int(c[4])})
    except Exception:
        pass
    rec = {
        'page': n, 'text': text, 'confidence': conf,
        'word_count': len(words), 'words': words[:400],
        'image': {'width': pix.width, 'height': pix.height, 'dpi': _W['dpi']},
        'ocr_seconds': round(time.time() - t0, 2),
        'engine': 'tesserocr/libtesseract LSTM', 'lang': _W['lang'], 'psm': int(_W['psm']),
    }
    tmp = dest + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(rec, f, ensure_ascii=False)
    os.replace(tmp, dest)
    return {'page': n, 'status': 'ok', 'confidence': conf,
            'chars': len(text), 'seconds': round(time.time() - t0, 1)}



def boxes_page(n):
    """Second pass: word boxes only, for column-aware structuring.
    Does NOT touch the already-extracted page text or the manifest."""
    doc, api = _W['doc'], _W['api']
    dest = os.path.join(_W['out'], 'pages', f'page-{n:04d}.boxes.json')
    if os.path.isfile(dest) and not _W.get('force'):
        return {'page': n, 'status': 'skipped'}
    page = doc[n - 1]
    pix = page.get_pixmap(dpi=_W['dpi'], colorspace=pymupdf.csGRAY, alpha=False)
    img = Image.frombytes('L', (pix.width, pix.height), pix.samples)
    api.SetImage(img)
    words = []
    for row in api.GetTSVText(0).splitlines()[1:]:
        c = row.split('\t')
        if len(c) < 12 or not c[11].strip() or c[0] != '5':
            continue
        words.append({'text': c[11], 'conf': float(c[10]),
                      'bbox': [int(c[6]), int(c[7]), int(c[8]), int(c[9])],
                      'block': int(c[2]), 'par': int(c[3]), 'line': int(c[4])})
    tmp = dest + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump({'page': n, 'width': pix.width, 'height': pix.height,
                   'words': words}, f, ensure_ascii=False)
    os.replace(tmp, dest)
    return {'page': n, 'status': 'ok', 'words': len(words), 'chars': 0, 'confidence': None}



def sha256(path, chunk=8 * 1024 * 1024):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(chunk), b''):
            h.update(b)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pdf', required=True)
    ap.add_argument('--out', default='app/content/source/biology-12')
    ap.add_argument('--start', type=int, default=1)
    ap.add_argument('--end', type=int, default=0)
    ap.add_argument('--workers', type=int, default=4)
    ap.add_argument('--dpi', type=int, default=200)
    ap.add_argument('--psm', type=int, default=int(PSM.AUTO))
    ap.add_argument('--lang', default='fas')
    ap.add_argument('--tessdata', default='/home/user/_work/ocr_data/tessdata')
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--boxes-only', action='store_true',
                    help='only generate word boxes (second pass); leave text/manifest intact')
    a = ap.parse_args()

    doc = pymupdf.open(a.pdf)
    total = doc.page_count
    end = a.end or total
    doc.close()
    os.makedirs(os.path.join(a.out, 'pages'), exist_ok=True)
    pages = list(range(a.start, min(end, total) + 1))

    if a.boxes_only:
        t0 = time.time(); done = 0
        ctx = mp.get_context('fork')
        worker = boxes_page
        with ctx.Pool(a.workers, initializer=init_worker,
                      initargs=(a.pdf, a.out, a.dpi, a.tessdata, a.psm, a.lang, True)) as pool:
            for r in pool.imap_unordered(worker, pages, chunksize=1):
                done += 1
                if done % 20 == 0:
                    print(f'[boxes {done}/{len(pages)}] page {r["page"]} {r["status"]} '
                          f'words={r.get("words")} elapsed={round(time.time()-t0)}s', flush=True)
        print('BOXES DONE', done, 'pages in', round(time.time()-t0, 1), 's', flush=True)
        return 0

    manifest = {
        'pdf': os.path.abspath(a.pdf), 'pdf_sha256': sha256(a.pdf),
        'page_count': total, 'range': [a.start, min(end, total)],
        'dpi': a.dpi, 'psm': a.psm, 'lang': a.lang,
        'tessdata': a.tessdata,
        'tessdata_fas_sha256': sha256(os.path.join(a.tessdata, 'fas.traineddata')),
        'engine': __import__('tesserocr').tesseract_version(),
        'started_at': time.strftime('%Y-%m-%dT%H:%M:%S'),
        'status': 'running', 'kind': 'raw-ocr-intermediate', 'gitignored': True,
        'note': 'Raw OCR of a user-provided copyrighted book. Not committed. No authored content.',
    }
    mp_path = os.path.join(a.out, 'manifest.json')
    json.dump(manifest, open(mp_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('PDF pages', total, 'OCR range', pages[0], '-', pages[-1], 'workers', a.workers, flush=True)

    t0 = time.time()
    done = 0
    confs = []
    ctx = mp.get_context('fork')
    with ctx.Pool(a.workers, initializer=init_worker,
                  initargs=(a.pdf, a.out, a.dpi, a.tessdata, a.psm, a.lang)) as pool:
        for r in pool.imap_unordered(ocr_page, pages, chunksize=1):
            done += 1
            if r.get('confidence') is not None:
                confs.append(r['confidence'])
            if done % 10 == 0 or r.get('status') == 'ok' and done <= 3:
                print(f"[{done}/{len(pages)}] page {r['page']} {r['status']} "
                      f"conf={r.get('confidence')} chars={r.get('chars')} "
                      f"elapsed={round(time.time()-t0)}s", flush=True)
    manifest.update({
        'status': 'complete', 'finished_at': time.strftime('%Y-%m-%dT%H:%M:%S'),
        'pages_done': done, 'elapsed_seconds': round(time.time() - t0, 1),
        'mean_confidence': round(sum(confs) / len(confs), 1) if confs else None,
        'min_confidence': round(min(confs), 1) if confs else None,
    })
    json.dump(manifest, open(mp_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('DONE', done, 'pages in', round(time.time() - t0, 1), 's; mean conf',
          manifest['mean_confidence'], flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
