#!/usr/bin/env python3
"""Extract Mimo's real pedagogical grammar from the decoded lesson assets.

READ-ONLY. Source: /home/user/_work/_analysis/mimo_assets/assets/lessons-*/tracks/
(10 locales x ~1029 tutorial JSON). Produces app/content/PEDAGOGY_STATS.json.
No curriculum is generated here; this is measurement, not authoring.
"""
from __future__ import annotations
import collections, glob, json, os, re, sys

BASE = '/home/user/_work/_analysis/mimo_assets/assets'
OUT = os.path.join(os.path.dirname(__file__), '..', 'content', 'PEDAGOGY_STATS.json')

TAG = re.compile(r'<\s*([a-zA-Z][\w-]*)')
RENDERERS = ['fillthegap', 'multiplechoice', 'executablefiles', 'validatedinput',
             'interactivewebview', 'noninteractiveslide', 'webview', 'code', 'quiz']
DEVICES = {
    'explain/define': r'\b(is (?:a|the)|means|refers to|called|stands for|defined as)\b',
    'example': r'\b(for example|for instance|such as|e\.g\.|like this)\b',
    'instruction/try': r"\b(let's|try it|now you|your turn|type|change|run|create|add|write)\b",
    'recall/check': r'\b(remember|did you know|quiz|question|which of|what is|true or false|correct)\b',
    'feedback/recap': r'\b(well done|great|correct|nice|congrat|you learned|in this lesson|summary|recap)\b',
    'scaffold/hint': r'\b(hint|tip|note|careful|watch out|don\'t worry|step by step)\b',
}

def main():
    locales = sorted(d for d in os.listdir(BASE) if d.startswith('lessons-') and
                     os.path.isdir(os.path.join(BASE, d, 'tracks')))
    tutorials = collections.Counter()
    chapter_types = collections.Counter()
    content_types = collections.Counter()
    code_langs = collections.Counter()
    tut_types = collections.Counter()
    tags = collections.Counter()
    renderer_hits = collections.Counter()
    devices = collections.Counter()
    lesson_titles = collections.Counter()
    chapter_lesson_counts = []
    lesson_wordcounts = []
    sequences = collections.Counter()
    chapter_type_sequences = collections.Counter()
    per_locale = {}
    errors = []

    for loc in locales:
        files = sorted(glob.glob(os.path.join(BASE, loc, 'tracks', 'tutorial-*.json')))
        per_locale[loc] = {'tutorial_files': len(files), 'parse_failures': 0}
        for fp in files:
            try:
                t = json.load(open(fp, encoding='utf-8'))['tutorial']
            except Exception as e:
                per_locale[loc]['parse_failures'] += 1
                errors.append(f'{loc}/{os.path.basename(fp)}: {e}')
                continue
            if loc != 'lessons-en':
                continue  # deep pedagogy measured on the canonical English set
            tutorials['count'] += 1
            tut_types[str(t.get('type'))] += 1
            code_langs[str(t.get('codeLanguage'))] += 1
            chapters = t.get('chapters', [])
            tutorials['chapters'] += len(chapters)
            ct_seq = []
            for ch in chapters:
                ct = str(ch.get('type'))
                chapter_types[ct] += 1
                ct_seq.append(ct)
                lessons = ch.get('lessons', [])
                chapter_lesson_counts.append(len(lessons))
                tutorials['lessons'] += len(lessons)
                seq = []
                for l in lessons:
                    title = str(l.get('title', ''))
                    lesson_titles[title] += 1
                    seq.append(title.split(':')[0].strip()[:28])
                    content_types[str(l.get('contentType'))] += 1
                    html = str(l.get('interactiveContent', ''))
                    words = re.findall(r"[A-Za-z0-9']+", re.sub(r'<[^>]+>', ' ', html))
                    lesson_wordcounts.append(len(words))
                    for tag in TAG.findall(html):
                        tags[tag.lower()] += 1
                    low = html.lower()
                    for r in RENDERERS:
                        if r in low:
                            renderer_hits[r] += 1
                    plain = re.sub(r'<[^>]+>', ' ', html)
                    for name, pat in DEVICES.items():
                        if re.search(pat, plain, re.I):
                            devices[name] += 1
                for a, b in zip(seq, seq[1:]):
                    sequences[f'{a} → {b}'] += 1
            for a, b in zip(ct_seq, ct_seq[1:]):
                chapter_type_sequences[f'{a} → {b}'] += 1

    def top(c, n=25):
        return [[k, v] for k, v in c.most_common(n)]

    stats = {
        'method': 'measurement of decoded Mimo lesson assets (no authoring, no server claims)',
        'source': BASE,
        'locales': locales,
        'per_locale': per_locale,
        'parse_failures_total': sum(v['parse_failures'] for v in per_locale.values()),
        'parse_errors_sample': errors[:10],
        'counts': {
            'tutorials': tutorials['count'], 'chapters': tutorials['chapters'],
            'lessons': tutorials['lessons'], 'locales': len(locales),
        },
        'tutorial_types': top(tut_types),
        'code_languages': top(code_langs),
        'chapter_types': top(chapter_types),
        'content_types': top(content_types),
        'html_tags': top(tags, 40),
        'renderer_signals': top(renderer_hits),
        'teaching_devices': top(devices),
        'lesson_titles_top': top(lesson_titles, 40),
        'chapter_lesson_count': {
            'min': min(chapter_lesson_counts), 'max': max(chapter_lesson_counts),
            'mean': round(sum(chapter_lesson_counts) / len(chapter_lesson_counts), 2),
        },
        'lesson_wordcount': {
            'min': min(lesson_wordcounts), 'max': max(lesson_wordcounts),
            'mean': round(sum(lesson_wordcounts) / len(lesson_wordcounts), 1),
        },
        'lesson_title_transitions_top': top(sequences, 30),
        'chapter_type_transitions_top': top(chapter_type_sequences, 20),
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(stats, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('locales', len(locales), 'tutorial files total', sum(v['tutorial_files'] for v in per_locale.values()))
    print('canonical(EN) counts', stats['counts'])
    print('chapter types', stats['chapter_types'][:8])
    print('content types', stats['content_types'][:8])
    print('renderer signals', stats['renderer_signals'][:10])
    print('devices', stats['teaching_devices'])
    print('chapter lesson count', stats['chapter_lesson_count'])
    print('lesson wordcount', stats['lesson_wordcount'])
    print('wrote', OUT)
    return 0

if __name__ == '__main__':
    sys.exit(main())
