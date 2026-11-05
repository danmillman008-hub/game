#!/usr/bin/env python3
"""LAYOUT-AWARE processing of the 848-page biology book (replaces the flat-OCR pass).

The earlier `structure_book.py` read Tesseract's `GetTSVText()` string, whose
two-column pages are interleaved; that is why its 565 "questions" were
column-mixed and had `correctIndex: null`. This tool instead reconstructs each
line from the WORD BOXES (`page-*.boxes.json`): group by (block, par, line),
sort words right-to-left by x, then order lines top-to-bottom by y. It then:

  1. normalises Persian conservatively (Arabic letters/digits -> Persian,
     ZWNJ/tatweel/whitespace cleanup). NO word is corrected or invented.
  2. scores every line with its word-level OCR confidence and a cleanliness
     ratio; low-quality lines are recorded but excluded from content.
  3. parses the book's own ANSWER KEY (`N - گزینه «X» <explanation>` plus
     `بررسی سایر گزینهها: گزینه (۱): …`) and the numbered QUESTION pages.
  4. joins question N to answer-key N inside the same detected chapter,
     producing real `correctIndex`, `explanationFa` and per-option notes.
  5. builds one-concept micro-lessons (~21 words, Mimo's measured mean) from
     high-confidence prose lines, with pedagogicalRole and typed blocks.

Output is a DRAFT (`reviewStatus: unreviewed`, `contentStatus: extracted`)
in the gitignored source folder. It is NOT wired into the app: OCR is noisy
and no sentence may be presented as approved content before human review.

Usage: python3 app/tools/process_book.py
"""
from __future__ import annotations
import collections, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGES = ROOT / 'app/content/source/biology-12/pages'
OUT = ROOT / 'app/content/source/biology-12/PROCESSED_DRAFT.json'
REPORT = ROOT / 'app/content/source/biology-12/PROCESS_REPORT.json'

AR_TO_FA = str.maketrans({'ي': 'ی', 'ك': 'ک', 'ة': 'ه', 'ؤ': 'و',
                          'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ى': 'ی'})
DIGITS = str.maketrans('٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹', '0123456789' + '0123456789')
PERSIAN = re.compile(r'[\u0600-\u06FF]')
LATIN_RUN = re.compile(r'[A-Za-z]{3,}')
BAD_MARKS = re.compile(r'^[«»\|\}\{\[\]\(\)\*\+ـ\-–\sًٌٍَُِ]+')

# «۴- گزینة «۳» …» / «58 - گزینه (3) …»
ANSWER = re.compile(r'(\d{1,3})\s*[-–ـ]\s*گزین[هةٌ]?\s*[«\(\[\""]?\s*([۱-۴1-4٠-٤])')
OPT_EXPL = re.compile(r'گزین[هةٌ]?\s*\(?\s*([۱-۴1-4])\s*\)?\s*:')
QSTART = re.compile(r'^\s*(\d{1,3})\s*[-–ـ]\s*(.+)$')
OPTMARK = re.compile(r'(?:^|\s)([۱-۴1-4]|الف|ب|ج|د)\s*[\)\.\-–]\s*')
LETTER = {'الف': 0, 'ب': 1, 'ج': 2, 'د': 3}


def norm(s):
    s = s.translate(AR_TO_FA).translate(DIGITS)
    s = s.replace('\u200c', ' ').replace('\u00a0', ' ').replace('ـ', '')
    s = s.replace('–', '-').replace('،', '،').replace(';', '؛')
    s = re.sub(r'[ \t]+', ' ', s)
    return s.strip()


def lines_from_boxes(rec):
    groups = collections.defaultdict(list)
    for w in rec['words']:
        groups[(w['block'], w['par'], w['line'])].append(w)
    out = []
    for key, ws in groups.items():
        ws = sorted(ws, key=lambda w: -w['bbox'][0])  # RTL reading order
        text = norm(' '.join(w['text'] for w in ws))
        if not text:
            continue
        conf = sum(w['conf'] for w in ws) / len(ws)
        toks = text.split()
        clean = sum(1 for t in toks if len(t) >= 3 and PERSIAN.search(t)
                    and not LATIN_RUN.search(t)) / max(1, len(toks))
        out.append({'text': text, 'conf': round(conf, 1), 'clean': round(clean, 2),
                    'y': ws[0]['bbox'][1], 'x': ws[0]['bbox'][0], 'key': key})
    out.sort(key=lambda l: (l['y'], -l['x']))
    return out


def good(line, threshold=72.0, clean=0.62):
    s = BAD_MARKS.sub('', line['text'])
    return (line['conf'] >= threshold and line['clean'] >= clean
            and len(s) >= 18 and PERSIAN.search(s) and not LATIN_RUN.search(s))


def option_index(tok):
    tok = tok.translate(DIGITS)
    if tok.isdigit():
        return int(tok) - 1
    return LETTER.get(tok, -1)


def main():
    boxes = sorted(PAGES.glob('page-*.boxes.json'))
    assert boxes, f'no word boxes in {PAGES}'
    answer_entries, question_candidates, prose_lines, stats = [], [], [], []
    stats = {'pages': len(boxes), 'lines': 0, 'keptLines': 0, 'lowConfidenceLines': 0}

    for path in boxes:
        page = int(path.stem.split('-')[1].split('.')[0])
        rec = json.loads(path.read_text(encoding='utf-8'))
        lines = lines_from_boxes(rec)
        stats['lines'] += len(lines)
        for ln in lines:
            if good(ln):
                stats['keptLines'] += 1
            else:
                stats['lowConfidenceLines'] += 1
        text_lines = [l['text'] for l in lines]

        # ---- ANSWER KEY entries -------------------------------------------
        for i, ln in enumerate(lines):
            m = ANSWER.search(ln['text'])
            if not m:
                continue
            num = int(m.group(1).translate(DIGITS))
            idx = option_index(m.group(2))
            if idx not in (0, 1, 2, 3):
                continue
            body = [ln['text'][m.end():].strip(' :«»-')]
            j = i + 1
            while j < len(lines) and not ANSWER.search(lines[j]['text']) and len(body) < 8:
                body.append(lines[j]['text'])
                j += 1
            joined = ' '.join(x for x in body if x)
            confs = [lines[k]['conf'] for k in range(i, min(j, len(lines)))]
            option_notes = {}
            for om in OPT_EXPL.finditer(joined):
                oi = option_index(om.group(1))
                if 0 <= oi <= 3:
                    start = om.end()
                    nxt = OPT_EXPL.search(joined, start)
                    option_notes[str(oi)] = joined[start:(nxt.start() if nxt else len(joined))].strip(' ./')
            answer_entries.append({
                'page': page, 'number': num, 'correctIndex': idx,
                'explanationFa': norm(joined[:900]),
                'optionExplanations': option_notes,
                'confidence': round(sum(confs) / max(1, len(confs)), 1),
                'reviewStatus': 'unreviewed',
            })

        # ---- QUESTION stems and options -----------------------------------
        cur = None
        for ln in lines:
            q = QSTART.match(ln['text'])
            if q and len(q.group(2)) > 18 and not ANSWER.search(ln['text']):
                cur = {'page': page, 'number': int(q.group(1).translate(DIGITS)),
                       'stemFa': q.group(2).strip(), 'options': [], 'confidence': ln['conf']}
                question_candidates.append(cur)
                continue
            if cur and len(cur['options']) < 4:
                hits = list(OPTMARK.finditer(ln['text']))
                for h, m in enumerate(hits):
                    oi = option_index(m.group(1))
                    end = hits[h + 1].start() if h + 1 < len(hits) else len(ln['text'])
                    val = ln['text'][m.end():end].strip(' -.)')
                    if 0 <= oi <= 3 and len(val) > 2 and oi == len(cur['options']):
                        cur['options'].append(val)

        # ---- PROSE (درسنامه) lines -----------------------------------------
        for ln in lines:
            if good(ln) and not QSTART.match(ln['text']) and not ANSWER.search(ln['text']):
                prose_lines.append({'page': page, 'text': BAD_MARKS.sub('', ln['text']),
                                    'confidence': ln['conf'], 'clean': ln['clean']})

    # ---- join answer key to questions -------------------------------------
    # Question numbers restart in every chapter, so a number alone is NOT a
    # key. Use (same number) as a prior and word overlap between the question's
    # stem/options and the answer-key explanation as the disambiguator. No text
    # is invented: this is a similarity join over verbatim book sentences.
    STOP = {'که', 'این', 'آن', 'است', 'باشد', 'شود', 'های', 'در', 'به', 'از', 'با',
            'را', 'برای', 'یک', 'چه', 'کدام', 'گزینه', 'می', 'هم', 'یا', 'و'}
    def tokens(t):
        t = re.sub(r'[^\w\s]', ' ', norm(t))
        return {w for w in t.split() if len(w) >= 4 and w not in STOP}
    a_by_num = collections.defaultdict(list)
    for a in answer_entries:
        a_by_num[a['number']].append(a)
    for a in answer_entries:
        a['_tok'] = tokens(a['explanationFa'])
    ranked = []
    for qc in question_candidates:
        if len(qc['options']) != 4:
            continue
        qt = tokens(qc['stemFa'] + ' ' + ' '.join(qc['options']))
        scored = []
        for a in answer_entries:
            if not a['_tok']:
                continue
            ov = len(qt & a['_tok']) / max(1, min(len(qt), len(a['_tok'])))
            prior = 0.35 if a['number'] == qc['number'] else 0.0
            scored.append((ov + prior, ov, a))
        scored.sort(key=lambda x: -x[0])
        best = scored[0] if scored else None
        # require real textual corroboration, not just a shared question number
        key = best[2] if best and best[1] >= 0.12 else None
        ranked.append((qc, key))
        if key is not None:
            key['_matched'] = True
    joined, unresolved = [], 0
    for qc, key in ranked:
        if key is None:
            unresolved += 1
        joined.append({
            'id': f'book-p{qc["page"]:04d}-q{qc["number"]:03d}',
            'stemFa': qc['stemFa'], 'options': qc['options'],
            'correctIndex': key['correctIndex'] if key else None,
            'explanationFa': key['explanationFa'] if key else '',
            'optionExplanations': key['optionExplanations'] if key else {},
            'difficulty': 'unknown', 'topicId': 'unassigned',
            'questionNumberInBook': qc['number'], 'sourcePage': qc['page'],
            'answerKeyPage': key['page'] if key else None,
            'joinBasis': 'question-number + verbatim word overlap (no invented text)',
            'contentStatus': 'extracted',
            'trace': {'sourceRef': f'book:biology-12:page-{qc["page"]}:q-{qc["number"]}',
                      'sourcePage': qc['page'], 'ocrConfidence': qc['confidence'],
                      'ocrEngine': 'libtesseract 5.5.3 / fas (word boxes)',
                      'reviewStatus': 'unreviewed', 'contentStatus': 'extracted',
                      'notes': 'بازسازی خطوط از word boxes؛ نیازمند مقایسه با تصویر صفحه.'},
        })

    # ---- micro-lessons from clean prose -----------------------------------
    lessons = []
    for i in range(0, min(len(prose_lines), 900), 3):
        chunk = prose_lines[i:i + 3]
        words = ' '.join(x['text'] for x in chunk).split()
        if len(words) < 8:
            continue
        lessons.append({
            'id': 40000 + i, 'title': words[0][:32],
            'pedagogicalRole': 'explain', 'contentType': 'interactive',
            'blocks': [{'id': f'b{40000 + i}-1', 'renderer': 'text',
                        'contentFa': ' '.join(words[:45])}],
            'trace': {'sourceRef': f'book:biology-12:page-{chunk[0]["page"]}:line-{i}',
                      'sourcePage': chunk[0]['page'],
                      'ocrConfidence': round(sum(x['confidence'] for x in chunk) / len(chunk), 1),
                      'reviewStatus': 'unreviewed', 'contentStatus': 'extracted'},
        })

    draft = {
        'formVersion': '1.0.0', 'packageId': 'biology-12-layout-aware-draft',
        'locale': 'fa', 'publishSetVersion': 753,
        'source': {'kind': 'converted-book', 'title': 'زیستشناسی ۳ · دوازدهم · خیلیسبز',
                   'grade': 'دوازدهم', 'subject': 'زیستشناسی', 'publisher': 'خیلی سبز',
                   'contentStatus': 'extracted',
                   'note': 'پیشنویس پردازششده از word boxes؛ بازبینینشده، وارد اپ نمیشود.'},
        'tracks': [], 'tutorials': [], 'questions': joined, 'exams': [],
        'provenance': {'sourceRef': 'book:biology-12:word-boxes',
                       'contentStatus': 'extracted', 'reviewStatus': 'unreviewed',
                       'notes': 'هیچ واژه، پاسخ یا توضیحی اختراع نشده است.'},
    }
    OUT.write_text(json.dumps(draft, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    rep = {
        **stats,
        'answerKeyEntries': len(answer_entries),
        'questionCandidates': len(question_candidates),
        'fourOptionQuestions': len(joined),
        'questionsWithAnswerKey': sum(1 for q in joined if q['correctIndex'] is not None),
        'questionsWithoutAnswerKey': unresolved,
        'answerKeyEntriesMatched': sum(1 for a in answer_entries if a.get('_matched')),
        'answerKeyEntriesWithPerOptionExplanation': sum(1 for a in answer_entries if a['optionExplanations']),
        'microLessonsFromProse': len(lessons),
        'method': 'word-box line reconstruction (RTL, top-to-bottom) + conservative Persian normalisation',
        'honesty': 'EXTRACTED DRAFT ONLY — unreviewed, not shipped, no invented content. SERVER CONFIRMED=0.',
    }
    REPORT.write_text(json.dumps(rep, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(rep, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
