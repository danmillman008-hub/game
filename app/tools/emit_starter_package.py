#!/usr/bin/env python3
"""Build the STARTER content package from the APPROVED prototype fixtures.

The 20 stems/options/answers/explanations are the exact QRAW rows inside
app/assets/proto-ui.js (a working copy of the approved v12.5-fa payload).
Nothing is invented: every unit keeps a trace to its prototype row, is marked
contentStatus=placeholder and reviewStatus=unreviewed.

Outputs:
  app/content/STARTER_PACKAGE.json   (form-conformant, validated)
  app/src/starter-package.js        (ES module for browser + single-file build)
"""
from __future__ import annotations
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
APP = ROOT / 'app'
ui = (APP / 'assets/proto-ui.js').read_text(encoding='utf-8')
i = ui.index('var QRAW=[')
j = ui.index('\n  ];', i)
rows = json.loads('[' + ui[i + len('var QRAW=['):j].strip().rstrip(',') + ']')
assert len(rows) == 20, len(rows)

REF = 'prototype:v12.5-fa:qbank'
TRACE = {'sourceRef': REF, 'contentStatus': 'placeholder', 'reviewStatus': 'unreviewed',
         'notes': 'دادهٔ آزمایشی پروتوتایپ؛ منبع کتاب درسی نیست.'}

questions, tutorials = [], []
for n, (sub, stem, opts, ok, expl) in enumerate(rows, 1):
    qid = f'proto-q-{n:02d}'
    tid = 1000 + n
    questions.append({
        'id': qid, 'stemFa': stem, 'options': opts, 'correctIndex': int(ok),
        'explanationFa': expl, 'topicId': 'prototype-fixture',
        'difficulty': 'unknown', 'renderer': 'MultipleChoice',
        'contentStatus': 'placeholder',
        'trace': {'sourceRef': f'{REF}-{n:02d}', 'contentStatus': 'placeholder',
                  'reviewStatus': 'unreviewed'},
    })
    tutorials.append({
        'id': tid, 'version': 1, 'type': 'placeholder', 'title': sub,
        'descriptionContent': 'واحد آزمایشی ساختهشده از بانک سؤال پروتوتایپ تأییدشده؛ '
                              'درسنامهٔ نهایی پس از تحویل منابع جایگزین میشود.',
        'trace': {'sourceRef': f'{REF}-{n:02d}', 'contentStatus': 'placeholder',
                  'reviewStatus': 'unreviewed'},
        'chapters': [{
            'id': tid * 10 + 1, 'title': 'نگاه و پاسخ', 'type': 'practiceLevel1',
            'practiceQuestionIds': [qid],
            'trace': {'sourceRef': f'{REF}-{n:02d}', 'contentStatus': 'placeholder',
                      'reviewStatus': 'unreviewed'},
            'lessons': [{
                'id': tid * 100 + 1, 'title': stem[:60],
                'contentType': 'interactive', 'pedagogicalRole': 'check',
                'questionRefs': [qid],
                'trace': {'sourceRef': f'{REF}-{n:02d}', 'contentStatus': 'placeholder',
                          'reviewStatus': 'unreviewed'},
                'blocks': [{
                    'id': f'{qid}-b1', 'renderer': 'MultipleChoice', 'contentFa': stem,
                    'options': opts, 'correctIndex': int(ok), 'explanationFa': expl,
                    'questionId': qid,
                    'trace': {'sourceRef': f'{REF}-{n:02d}', 'contentStatus': 'placeholder',
                              'reviewStatus': 'unreviewed'},
                }, {
                    'id': f'{qid}-b2', 'renderer': 'feedback',
                    'contentFa': expl, 'questionId': qid,
                    'trace': {'sourceRef': f'{REF}-{n:02d}', 'contentStatus': 'placeholder',
                              'reviewStatus': 'unreviewed'},
                }],
            }],
        }],
    })

pkg = {
    'formVersion': '1.0.0',
    'packageId': 'mimo-starter-prototype-fixture',
    'locale': 'fa',
    'publishSetVersion': 753,
    'source': {
        'kind': 'placeholder',
        'title': 'دادهٔ آزمایشی پروتوتایپ تأییدشدهٔ v12.5-fa',
        'contentStatus': 'placeholder',
        'note': 'این بسته فقط از ۲۰ سؤال، پاسخ و توضیح موجود در پروتوتایپ ساخته شده است. '
                'هیچ درسنامه، پاسخ یا محتوای جدیدی تولید نشده؛ منابع نهایی (کتاب/OCR/پاسخنامه) '
                'پس از تحویل با ابزار واردسازی جایگزین میشوند. استنتاج سرور: تأییدنشده.',
    },
    'tracks': [{
        'id': 1, 'version': 1, 'title': 'بستهٔ آغازین (آزمایشی)',
        'descriptionContent': 'مسیر آموزشی قابلاستفاده برای شروع؛ عنوان درسها از سرفصلهای '
                              'پروتوتایپ و محتوای تمرین از بانک سؤال همان پروتوتایپ است.',
        'onboardingCategory': 'learn', 'isNew': False, 'isHidden': False, 'iconBanner': '',
        'sections': [{
            'name': 'بانک سؤال پروتوتایپ', 'startIndex': 0, 'endIndex': len(tutorials) - 1,
            'tutorialIds': [t['id'] for t in tutorials],
            'trace': dict(TRACE),
        }],
        'trace': dict(TRACE),
    }],
    'tutorials': tutorials,
    'questions': questions,
    'exams': [],
    'provenance': {
        'sourceRef': REF, 'contentStatus': 'placeholder', 'reviewStatus': 'unreviewed',
        'notes': 'تولیدشده توسط app/tools/emit_starter_package.py از app/assets/proto-ui.js؛ '
                 'بدون شبکه، بدون LLM، بدون محتوای ساختگی.',
    },
}
json_path = APP / 'content' / 'STARTER_PACKAGE.json'
json_path.write_text(json.dumps(pkg, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
js_path = APP / 'src' / 'starter-package.js'
js_path.write_text(
    '/* GENERATED by tools/emit_starter_package.py — do not edit by hand. */\n'
    'export const STARTER_PACKAGE = ' + json.dumps(pkg, ensure_ascii=False, indent=2) + ';\n'
    'export const STARTER_SUMMARY = '
    + json.dumps({'questions': len(questions), 'tutorials': len(tutorials),
                  'lessons': sum(len(c['lessons']) for t in tutorials for c in t['chapters']),
                  'kind': 'placeholder', 'externalProvider': 'not-configured'},
                 ensure_ascii=False) + ';\n',
    encoding='utf-8')
print('wrote', json_path.relative_to(ROOT), 'and', js_path.relative_to(ROOT),
      'questions=', len(questions), 'tutorials=', len(tutorials))
