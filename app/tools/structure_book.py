#!/usr/bin/env python3
"""Full-book OCR -> DRAFT form-conformant package (one pass over ALL pages).

HONESTY: this is an EXTRACTED draft, not reviewed content. It never invents a
correct answer, explanation, lesson text or topic name. Unresolved answers are
`null` with reviewStatus='unreviewed'. Output stays in app/content/source/
(gitignored) until a human/verified pass promotes it to a real package.

Usage:
  python3 app/tools/structure_book.py --ocr app/content/source/biology-12 \
      --out app/content/source/biology-12/draft-package.json [--partial]
"""
from __future__ import annotations
import argparse, json, os, re, sys, time

PERSIAN = '۰۱۲۳۴۵۶۷۸۹'
TRANS = str.maketrans(PERSIAN, '0123456789')
ARABIC = str.maketrans('٠١٢٣٤٥٦٧٨٩', '0123456789')


def digits(v):
    return str(v).translate(TRANS).translate(ARABIC)


def to_int(v):
    try:
        return int(digits(v).strip())
    except Exception:
        return None


Q_START = re.compile(r'^\s*(?:سؤال\s*)?(\d{1,3})\s*([-–)\.]\s*)?(.+)$')
Q_MARKERS = ('؟', '?', 'کدام', 'چند مورد', 'کدامیک', 'درست است', 'نادرست', 'عبارت مقابل')
# option markers: ASCII/Persian/Arabic 1-4 OR الف/ب/ج/د, followed by ) . - –
OPT_MARK = re.compile(r'(?:^|\s)([1-4]|الف|ب|ج|د)\s*[\)\.\-–]\s*')
ANSWER_LINE = re.compile(r'(?:پاسخ|گزینه\s*صحیح|جواب)\D{0,12}([1-4])', re.I)
HEADING = re.compile(r'^(فصل|گفتار|مبحث|درسنامه|بخش)\s*(.+)$')
LETTER_INDEX = {'الف': 0, 'ب': 1, 'ج': 2, 'د': 3}


def norm(line):
    line = digits(line).replace('\u200c', ' ').replace('\u00a0', ' ')
    line = line.replace('–', '-').replace('ـ', '-')
    return re.sub(r'[ \t]+', ' ', line).strip()


def split_options(line):
    """Return [(index0-3, text)] found in one OCR line (may hold 2+ options)."""
    hits = list(OPT_MARK.finditer(line))
    out = []
    for i, m in enumerate(hits):
        label = m.group(1)
        idx = LETTER_INDEX.get(label, int(label) - 1 if label.isdigit() else -1)
        if idx < 0 or idx > 3:
            continue
        end = hits[i + 1].start() if i + 1 < len(hits) else len(line)
        text = line[m.end():end].strip(' -.)')
        if len(text) > 2:
            out.append((idx, text))
    return out


def parse_page(rec):
    """Return {page, lessonLines[], questions[], headings[], confidence}."""
    page = rec['page']
    conf = rec.get('confidence', 0)
    lines = [norm(x) for x in rec.get('text', '').splitlines()]
    lines = [x for x in lines if x]
    headings, lesson_lines, questions = [], [], []
    cur = None
    for line in lines:
        h = HEADING.match(line)
        if h:
            headings.append(line)
            cur = None
            continue
        q = Q_START.match(line)
        is_q = bool(q) and len(line) > 12 and (
            bool(q.group(2)) or any(m in line for m in Q_MARKERS))
        if is_q:
            cur = {'stem': q.group(3).strip(), 'options': [], 'lines': [line]}
            questions.append(cur)
            continue
        opts = split_options(line)
        if opts and cur and len(cur['options']) < 4:
            for idx, text in opts:
                if idx < len(cur['options']):
                    continue
                cur['options'].append(text)
            cur['lines'].append(line)
            continue
        a = ANSWER_LINE.search(line)
        if a and cur:
            cur['answer_hint'] = int(a.group(1))
            cur['lines'].append(line)
            continue
        if cur and len(cur['options']) < 4 and len(line) > 4 and not line.startswith('پاسخ'):
            cur['stem'] += ' ' + line
            cur['lines'].append(line)
        else:
            lesson_lines.append(line)
    return {'page': page, 'confidence': conf, 'headings': headings,
            'lessonLines': lesson_lines, 'questions': questions}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ocr', default='app/content/source/biology-12')
    ap.add_argument('--out', default='app/content/source/biology-12/draft-package.json')
    ap.add_argument('--partial', action='store_true')
    a = ap.parse_args()
    pages_dir = os.path.join(a.ocr, 'pages')
    files = sorted(f for f in os.listdir(pages_dir) if f.startswith('page-') and f.endswith('.json'))
    if not files:
        print('NO OCR PAGES'); return 1
    manifest_path = os.path.join(a.ocr, 'manifest.json')
    manifest = json.load(open(manifest_path, encoding='utf-8')) if os.path.isfile(manifest_path) else {}

    questions = []
    lesson_pages = []
    headings = []
    low_conf = 0
    for f in files:
        rec = json.load(open(os.path.join(pages_dir, f), encoding='utf-8'))
        parsed = parse_page(rec)
        if parsed['confidence'] < 65: low_conf += 1
        if len(parsed['questions']) >= 3:
            lesson_pages.append({'page': rec['page'], 'type': 'question-page', 'lines': len(parsed['lessonLines'])})
        else:
            lesson_pages.append({'page': rec['page'], 'type': 'lesson/front-matter', 'lines': len(parsed['lessonLines'])})
        headings.extend([{'page': rec['page'], 'text': h} for h in parsed['headings']])
        for i, q in enumerate(parsed['questions']):
            if len(q['options']) < 2:
                continue  # too noisy, do not fabricate options
            qid = f'bio12-p{rec["page"]:04d}-q{i + 1:02d}'
            answer = q.get('answer_hint')
            # Only accept an answer found ON THE SAME PAGE as an explicit پاسخ line.
            questions.append({
                'id': qid,
                'stemFa': q['stem'][:1200],
                'options': q['options'][:6],
                'correctIndex': (answer - 1) if answer is not None and 1 <= answer <= len(q['options']) else None,
                'explanationFa': '',
                'topicId': 'unassigned',
                'difficulty': 'unknown',
                'questionNumberInBook': i + 1,
                'sourcePage': rec['page'],
                'renderer': 'MultipleChoice',
                'contentStatus': 'extracted',
                'trace': {
                    'sourceRef': f'book:biology-12:page-{rec["page"]}:block-{i + 1}',
                    'sourcePage': rec['page'], 'sourceLine': i + 1,
                    'ocrConfidence': rec.get('confidence', 0),
                    'ocrEngine': 'libtesseract 5.5.3 / fas',
                    'reviewStatus': 'unreviewed',
                    'contentStatus': 'extracted',
                    'notes': 'پیشنویس OCR؛ پاسخ صحیح فقط در صورت وجود پاسخنامهٔ صریح همان صفحه ثبت شده است.' if answer is None
                             else 'پاسخ از خط پاسخ همان صفحه استخراج شده؛ نیازمند بازبینی تصویر است.',
                },
            })

    pkg = {
        'formVersion': '1.0.0',
        'packageId': 'biology-12-khayli-sabz-draft',
        'locale': 'fa',
        'publishSetVersion': 753,
        'source': {
            'kind': 'converted-book',
            'title': 'زیستشناسی ۳ · پرسشهای چهارگزینهای · پایه دوازدهم',
            'grade': 'دوازدهم', 'subject': 'زیستشناسی', 'publisher': 'خیلی سبز',
            'pageCount': manifest.get('page_count', 848),
            'sha256': manifest.get('pdf_sha256', ''),
            'contentStatus': 'extracted',
            'note': 'پیشنویس OCR تمام کتاب؛ reviewed نشده، وارد اپ نمیشود. خروجی خام خارج از گیت است.',
        },
        'tracks': [{
            'id': 0, 'version': 1, 'title': 'زیستشناسی دوازدهم',
            'descriptionContent': 'ساختار مسیر؛ پس از بازبینی منابع تکمیل میشود',
            'onboardingCategory': 'learn', 'isNew': False, 'isHidden': False,
            'iconBanner': '', 'sections': [],
            'trace': {'sourceRef': 'book:biology-12:structure', 'contentStatus': 'extracted', 'reviewStatus': 'unreviewed'},
        }],
        'questions': questions,
        'exams': [],
        'provenance': {
            'sourceRef': f'book:biology-12:ocr-{len(files)}-pages',
            'contentStatus': 'extracted', 'reviewStatus': 'unreviewed',
            'notes': 'تمام صفحات OCRشده در یک پاس پردازش شدند؛ هیچ محتوای آموزشی اختراع نشده است.',
        },
    }
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    json.dump(pkg, open(a.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    report = {
        'generated_at': time.strftime('%Y-%m-%dT%H:%M:%S'),
        'pages_processed': len(files), 'pages_expected': manifest.get('page_count', 848),
        'partial': a.partial or len(files) < manifest.get('page_count', 848),
        'questions_extracted': len(questions),
        'questions_with_unknown_answer': sum(1 for q in questions if q['correctIndex'] is None),
        'low_confidence_pages': low_conf,
        'headings_found': len(headings),
        'question_pages': sum(1 for p in lesson_pages if p['type'] == 'question-page'),
        'lesson_pages': sum(1 for p in lesson_pages if p['type'] == 'lesson/front-matter'),
        'honesty': 'EXTRACTED DRAFT ONLY — not reviewed, not wired into the app, no invented content.',
    }
    json.dump(report, open(os.path.join(a.ocr, 'STRUCTURE_REPORT.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=2)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
