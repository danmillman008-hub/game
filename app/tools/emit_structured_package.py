#!/usr/bin/env python3
"""Build a STRUCTURED, native-Mimo-shaped content package.

Source of the Persian sentences/questions is the APPROVED v12.5-fa prototype's
QRAW bank (clean, existing, authored text) — NOT the prototype's layout-demo
paragraphs, NOT raw OCR, and NOT generated prose. Nothing is invented here:
every block is either a verbatim question, a verbatim option, a verbatim
explanation, or a split of that explanation.

The resulting hierarchy follows the shipped Mimo 9.35 asset schema measured in
ANALYSIS/MISSION_09/COMPLETE_LESSON_ENGINE_SPEC.md and PEDAGOGY.md:

  track -> sections[] -> tutorialIds[] -> tutorial{chapters[]}
        -> chapter{type: practiceLevel1|2|3|challengeLevel*} -> lessons[]
        -> lesson{pedagogicalRole, blocks[{renderer, contentFa, ...}]}

The package is emitted TWICE:
  app/content/STRUCTURED_PACKAGE.json   (validated by validate_content.py)
  app/src/content-package.js            (ESM const, bundled into the offline app)

Run: python3 app/tools/emit_structured_package.py
"""
from __future__ import annotations
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
APP = ROOT / 'app'
UI = APP / 'assets/proto-ui.js'
OUT_JSON = APP / 'content/STRUCTURED_PACKAGE.json'
OUT_JS = APP / 'src/content-package.js'

PERSIAN_DIGITS = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
DIFFICULTY = {'آسان': 'easy', 'متوسط': 'medium', 'سخت': 'hard'}
CHAPTER_TYPE = {'easy': 'practiceLevel1', 'medium': 'practiceLevel2',
                'hard': 'practiceLevel3'}
ROLE_SEQUENCE = ['hook', 'explain', 'check', 'practice', 'feedback', 'recap']


def fa(n):
    return str(n).translate(PERSIAN_DIGITS)


def parse_qraw():
    s = UI.read_text(encoding='utf-8')
    i = s.index('var QRAW=')
    start = s.index('[', i)
    depth, end = 0, start
    for j in range(start, len(s)):
        if s[j] == '[':
            depth += 1
        elif s[j] == ']':
            depth -= 1
            if depth == 0:
                end = j + 1
                break
    raw = json.loads(s[start:end])
    assert len(raw) == 20, f'expected 20 prototype questions, got {len(raw)}'
    out = []
    for n, r in enumerate(raw, 1):
        sub, stem, opts, ok, expl = r
        parts = [p.strip() for p in sub.split('·')]
        subject, topic, dlabel = parts[0], parts[1], parts[2].replace('دشواری', '').strip()
        out.append({'n': n, 'subject': subject, 'topic': topic,
                    'difficultyLabel': dlabel, 'difficulty': DIFFICULTY[dlabel],
                    'stemFa': stem, 'options': opts, 'correctIndex': ok,
                    'explanationFa': expl})
    return out


def sentences(text):
    """Split a verbatim explanation into sentence atoms (no rewriting)."""
    parts = re.split(r'(?<=[.!؟;:])\s+', text.strip())
    return [p.strip() for p in parts if p.strip()]


def trace(ref, status='placeholder', page=None):
    t = {'sourceRef': ref, 'contentStatus': status, 'reviewStatus': 'unreviewed',
         'notes': 'متن عیناً از بانک تأییدشدهٔ پروتوتایپ v12.5-fa؛ جایگزینی با کتاب پس از بازبینی منابع.'}
    if page is not None:
        t['sourcePage'] = page
    return t


def block(bid, renderer, content, **extra):
    b = {'id': bid, 'renderer': renderer, 'contentFa': content}
    b.update(extra)
    return b


def make():
    qs = parse_qraw()
    subjects = []
    for q in qs:
        if q['subject'] not in subjects:
            subjects.append(q['subject'])
    tutorials, questions, sections = [], [], []
    tut_id = 1000
    chapter_id = 2000
    lesson_id = 30000

    for s_idx, subject in enumerate(subjects):
        group = [q for q in qs if q['subject'] == subject]
        topics = []
        for q in group:
            if q['topic'] not in topics:
                topics.append(q['topic'])
        section_tut_ids = []
        for t_idx, topic in enumerate(topics):
            tut_id += 1
            section_tut_ids.append(tut_id)
            tq = [q for q in group if q['topic'] == topic]
            chapters = []
            for c_idx, q in enumerate(tq):
                chapter_id += 1
                sents = sentences(q['explanationFa'])
                lead = sents[0] if sents else q['explanationFa']
                rest = ' '.join(sents[1:]) if len(sents) > 1 else ''
                qid = f'proto-q-{q["n"]:02d}'
                ref = f'prototype:v12.5-fa:qbank-{q["n"]:02d}'
                ctype = CHAPTER_TYPE[q['difficulty']]

                # ---- micro-lessons: one concept, short text, one interaction ----
                lessons = []

                def add_lesson(title, role, blocks, refs=None):
                    nonlocal lesson_id
                    lesson_id += 1
                    lessons.append({
                        'id': lesson_id, 'title': title, 'contentType': 'interactive',
                        'pedagogicalRole': role,
                        'blocks': blocks,
                        'questionRefs': refs or [],
                        'trace': trace(ref + ':' + role),
                    })

                # 1. HOOK — present the concept with the verbatim question stem
                #    (NOT the explanation: that would spoil the answer).
                add_lesson(f'مفهوم: {topic}', 'hook', [
                    block(f'b{lesson_id}-1', 'text', q['stemFa'],
                          hintFa=f'یک مفهوم؛ {topic}'),
                    block(f'b{lesson_id}-2', 'strong', topic),
                ])
                # 2. CHECK — the real 4-option MultipleChoice, with the real key
                add_lesson(f'بررسی: {topic}', 'check', [
                    block(f'b{lesson_id}-1', 'MultipleChoice', q['stemFa'],
                          options=list(q['options']), correctIndex=q['correctIndex'],
                          explanationFa=q['explanationFa'], questionId=qid,
                          hintFa=f'دشواری: {q["difficultyLabel"]}'),
                ], [qid])
                # 3. FEEDBACK — answer key (تشریحی) + per-option status
                option_notes = []
                for i, opt in enumerate(q['options']):
                    state = 'گزینهٔ درست' if i == q['correctIndex'] else 'گزینهٔ نادرست'
                    option_notes.append(f'گزینهٔ {fa(i + 1)} ({state}): {opt}')
                add_lesson(f'پاسخنامه: {topic}', 'feedback', [
                    block(f'b{lesson_id}-1', 'feedback', q['explanationFa'],
                          options=option_notes, questionId=qid),
                ])
                # 4. EXPLAIN — درسنامه: the verbatim explanation, now that the
                #    learner has answered. Mimo teaches AFTER the first attempt.
                explain_body = rest or q['explanationFa']
                add_lesson(f'درسنامه: {topic}', 'explain', [
                    block(f'b{lesson_id}-1', 'text', explain_body or lead,
                          explanationFa=q['explanationFa']),
                    block(f'b{lesson_id}-2', 'text', lead),
                ])
                # 5. PRACTICE — fillTheGap from the SAME option set (no new text)
                add_lesson(f'جای خالی: {topic}', 'practice', [
                    block(f'b{lesson_id}-1', 'fillTheGap',
                          q['stemFa'] + ' … جای خالی را با پاسخ درست پر کنید.',
                          options=list(q['options']), correctIndex=q['correctIndex'],
                          explanationFa=q['explanationFa'], questionId=qid),
                ], [qid])
                # 6. RECAP — Reveal: correct option as the final recall
                add_lesson(f'جمع بندی: {topic}', 'recap', [
                    block(f'b{lesson_id}-1', 'text',
                          f'پاسخ درست: {q["options"][q["correctIndex"]]}',
                          explanationFa=q['explanationFa']),
                ])

                chapters.append({
                    'id': chapter_id, 'title': f'{topic} · {q["difficultyLabel"]}',
                    'type': ctype, 'lessons': lessons,
                    'practiceQuestionIds': [qid],
                    'trace': trace(ref + ':chapter'),
                })

            tutorials.append({
                'id': tut_id, 'version': 1, 'type': 'course',
                'title': topic,
                'descriptionContent': f'درسنامه و تمرین «{topic}» از {subject}',
                'shortDescriptionContent': f'{len(tq)} مبحث · {len(tq) * 6} ریزدرس',
                'showInTrack': True, 'isNew': False, 'codeLanguage': '',
                'iconBanner': '',
                'learningObjectives': [f'درک {topic}', 'پاسخ به سؤال چهارگزینهای مربوط',
                                       'بازیابی فعال با جای خالی'],
                'chapters': chapters,
                'trace': trace(f'prototype:v12.5-fa:topic-{t_idx + 1}'),
            })

            for q in tq:
                qid = f'proto-q-{q["n"]:02d}'
                questions.append({
                    'id': qid, 'stemFa': q['stemFa'], 'options': list(q['options']),
                    'correctIndex': q['correctIndex'],
                    'explanationFa': q['explanationFa'],
                    'topicId': f'{subject}:{topic}',
                    'chapterId': chapter_id,
                    'difficulty': q['difficulty'],
                    'renderer': 'MultipleChoice',
                    'contentStatus': 'placeholder',
                    'trace': trace(f'prototype:v12.5-fa:qbank-{q["n"]:02d}'),
                })

        sections.append({
            'name': subject,
            'description': f'{len(topics)} درسنامه · {len(group)} پرسش چهارگزینهای',
            'startIndex': s_idx, 'endIndex': s_idx,
            'tutorialIds': section_tut_ids,
            'trace': trace(f'prototype:v12.5-fa:subject-{s_idx + 1}'),
        })

    pkg = {
        'formVersion': '1.0.0',
        'packageId': 'mimo-structured-content-v1',
        'locale': 'fa',
        'publishSetVersion': 753,
        'source': {
            'kind': 'placeholder',
            'title': 'ساختار درسنامهٔ ساختهشده از بانک تأییدشدهٔ v12.5-fa',
            'grade': 'دوازدهم', 'subject': 'کنکور تجربی',
            'contentStatus': 'structured',
            'note': ('سلسلهمراتب و رندررها عیناً از داراییهای میمو ۹٫۳۵. جملهها و '
                     'پرسشها عیناً از QRAW پروتوتایپ تأییدشده؛ هیچ متن آموزشی، پاسخ '
                     'یا توضیحی تولید نشده است. کتاب/OCR پیشنویس است و وارد اپ نشده.'),
        },
        'tracks': [{
            'id': 1, 'version': 1, 'title': 'مسیر کنکور · درسنامهٔ ساختاریافته',
            'descriptionContent': 'چهار درس · بیست پرسش · صدوبیست ریزدرس',
            'onboardingCategory': 'learn', 'isNew': False, 'isHidden': False,
            'iconBanner': '', 'sections': sections,
            'trace': trace('prototype:v12.5-fa:track'),
        }],
        'tutorials': tutorials,
        'questions': questions,
        'exams': [],
        'provenance': trace('prototype:v12.5-fa:structured', 'structured'),
    }
    return pkg


def main():
    pkg = make()
    OUT_JSON.write_text(json.dumps(pkg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    OUT_JS.write_text(
        '/* GENERATED by app/tools/emit_structured_package.py — do not hand-edit.\n'
        '   Native-Mimo-shaped structured content package. */\n'
        'export const STRUCTURED_PACKAGE = ' +
        json.dumps(pkg, ensure_ascii=False, separators=(',', ':')) + ';\n',
        encoding='utf-8')
    n_lessons = sum(len(c['lessons']) for t in pkg['tutorials'] for c in t['chapters'])
    n_blocks = sum(len(l['blocks']) for t in pkg['tutorials'] for c in t['chapters']
                   for l in c['lessons'])
    print(json.dumps({
        'tracks': len(pkg['tracks']), 'sections': len(pkg['tracks'][0]['sections']),
        'tutorials': len(pkg['tutorials']),
        'chapters': sum(len(t['chapters']) for t in pkg['tutorials']),
        'microLessons': n_lessons, 'blocks': n_blocks,
        'questions': len(pkg['questions']),
        'questionsWithKnownAnswer': sum(1 for q in pkg['questions'] if q['correctIndex'] is not None),
        'bytes': OUT_JSON.stat().st_size,
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
