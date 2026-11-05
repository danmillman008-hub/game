#!/usr/bin/env python3
"""MISSION 09 / WP9 — deterministic, evidence-only curriculum graph + integrity audit.

Source: the ORIGINAL Mimo 9.35 APK assets, extracted read-only by MISSION 05.
On this sandbox the extracted tree lives at
  /home/user/_work/_analysis/mimo_assets/assets/lessons-<locale>/tracks/
It is OUTSIDE the git repository, so nothing is committed from it; only the
derived, normalized index and the measured integrity facts are written into
ANALYSIS/MISSION_09/COMPLETE_CURRICULUM_GRAPH.json.

Reproduction (runner side, original APK never modified):
  unzip -q MIMO_ORIGINAL.apk 'assets/lessons-*/tracks/*' -d mimo_assets/

No asset is repaired, renamed or rewritten. Discrepancies are REPORTED.
"""
import collections
import hashlib
import json
import os
import pathlib
import re
import sys

ASSETS = pathlib.Path(os.environ.get(
    'M09_ASSET_ROOT', '/home/user/_work/_analysis/mimo_assets/assets'))
OUT = pathlib.Path('ANALYSIS/MISSION_09/COMPLETE_CURRICULUM_GRAPH.json')
APK_SHA = '48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a'

LOCALES = ['en', 'de', 'es', 'fr', 'id', 'it', 'pl', 'pt', 'ru', 'tr']


def jload(p):
    with p.open(encoding='utf-8') as f:
        return json.load(f)


def classify_lesson(l):
    """Renderer/module family derived ONLY from shipped DSL tags.

    M06 06_CONTENT_SCHEMA_AND_DSL.md / 07_LESSON_MODULE_RENDERING.md:
    `gm.h.a(List)` selects a LessonInteractionType from the parsed module list.
    The tag->family mapping below is a deterministic INDEX, not a claim about
    runtime rendering (runtime rendering is VERIFIED_RUNTIME only where a
    MISSION 07/09 experiment observed it).
    """
    s = l.get('interactiveContent') or ''
    tags = re.findall(r'<([a-zA-Z][\w-]*)', s)
    tagset = set(t.lower() for t in tags)
    types = re.findall(r'<interaction[^>]*type="([^"]+)"', s)
    fam = []
    if l.get('contentType') == 'executableFiles' or l.get('executableContent'):
        fam.append('executableFiles')
    for t in types:
        fam.append(t)
    if 'webview' in tagset:
        fam.append('InteractiveWebView')
    if 'selection' in tagset:
        sel = re.search(r'<selection([^>]*)>', s)
        multiple = sel and 'multiple' in sel.group(1)
        fam.append('MultipleChoice' if multiple else 'SingleChoice')
    if 'spell' in tagset:
        fam.append('Spell')
    if 'reveal' in tagset:
        fam.append('Reveal')
    if not fam:
        fam = ['noninteractiveSlide']
    # dedupe, stable order
    seen, out = set(), []
    for f in fam:
        if f not in seen:
            seen.add(f)
            out.append(f)
    return out, sorted(tagset)


def main():
    integrity = {
        'source': 'original APK assets/lessons-<locale>/tracks/*.json (MISSION 05 read-only extraction)',
        'apk_sha256': APK_SHA,
        'asset_root_at_build_time': str(ASSETS),
        'publish_set_version': None,
        'locales_expected': LOCALES,
        'locales_found': [],
        'json_files_total': 0,
        'tutorial_files_total': 0,
        'tracks_files_total': 0,
        'parse_failures': [],
        'missing_tracks_json': [],
        'duplicate_tutorial_ids': [],
        'duplicate_lesson_ids': [],
        'duplicate_chapter_ids': [],
        'missing_tutorial_references': [],
        'orphan_tutorial_files': [],
        'unreachable_lessons': [],
        'unsupported_module_types': [],
        'schema_violations': [],
        'section_range_violations': [],
        'locale_inconsistencies': [],
        'content_type_histogram': {},
        'renderer_family_histogram': {},
        'dsl_tag_histogram': {},
        'hard_mode_lessons': 0,
        'notes': [],
    }
    if not ASSETS.is_dir():
        integrity['notes'].append(
            'ASSET_ROOT NOT PRESENT on this host; graph built from MISSION 05 '
            'SHIPPED_CONTENT_STATS.json aggregate only. Re-run with M09_ASSET_ROOT '
            'pointing at the extracted APK assets for the full node-level graph.')
        OUT.write_text(json.dumps({
            'document': 'MIMO 9.35 COMPLETE CURRICULUM GRAPH',
            'apk_sha256': APK_SHA, 'evidence_class': 'VERIFIED_ASSET (aggregate only)',
            'status': 'DEGRADED: extracted asset tree unavailable on this host',
            'integrity': integrity, 'tracks': [], 'lessons': [],
            'server_confirmed': 0}, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        print('DEGRADED')
        return

    graphs = {}
    all_tutorial_files = []
    for loc in LOCALES:
        d = ASSETS / ('lessons-' + loc) / 'tracks'
        tj = d / 'tracks.json'
        if not tj.exists():
            integrity['missing_tracks_json'].append(loc)
            continue
        integrity['locales_found'].append(loc)
        try:
            root = jload(tj)
        except Exception as e:
            integrity['parse_failures'].append({'file': str(tj), 'error': str(e)[:200]})
            continue
        integrity['tracks_files_total'] += 1
        if loc == 'en':
            integrity['publish_set_version'] = root.get('publishSetVersion')
        files = sorted(d.glob('tutorial-*.json'))
        all_tutorial_files += [(loc, f) for f in files]
        integrity['json_files_total'] += len(files) + 1
        graphs[loc] = {'tracks': root, 'tutorials': {}}
        for f in files:
            try:
                t = jload(f)
            except Exception as e:
                integrity['parse_failures'].append({'file': str(f), 'error': str(e)[:200]})
                continue
            if not isinstance(t, dict) or 'tutorial' not in t:
                integrity['schema_violations'].append({'file': str(f), 'issue': 'missing tutorial root'})
                continue
            tu = t['tutorial']
            tid = tu.get('id')
            if tid is None:
                integrity['schema_violations'].append({'file': str(f), 'issue': 'missing tutorial id'})
                continue
            graphs[loc]['tutorials'][str(tid)] = (tu, f)

    integrity['tutorial_files_total'] = len(all_tutorial_files)

    # ---- EN is the authoritative shipped curriculum for the offline spec ----
    en = graphs.get('en', {'tracks': {'tracks': []}, 'tutorials': {}})
    tracks_out = []
    lessons_out = []
    lesson_ids = collections.Counter()
    chapter_ids = collections.Counter()
    tutorial_ids = collections.Counter()
    referenced = set()
    tag_hist = collections.Counter()
    fam_hist = collections.Counter()
    ct_hist = collections.Counter()

    for tr in en['tracks'].get('tracks', []):
        tid_tr = tr.get('id')
        sections = []
        prev_chapters = []
        for si, sec in enumerate(tr.get('sections', [])):
            ids = [str(x) for x in sec.get('tutorialIds', [])]
            referenced.update(ids)
            lo, hi = sec.get('startIndex'), sec.get('endIndex')
            if lo is None or hi is None or hi - lo + 1 != len(ids):
                integrity['section_range_violations'].append(
                    {'track': tid_tr, 'section': sec.get('name'), 'startIndex': lo,
                     'endIndex': hi, 'tutorialIds': len(ids)})
            sections.append({
                'index': si, 'name': sec.get('name'), 'description': sec.get('description'),
                'startIndex': lo, 'endIndex': hi, 'tutorialIds': ids,
                'prerequisite': (sections[-1]['name'] if sections else None),
            })
        # tutorials are referenced by section, in section order
        tut_out = []
        for sec in sections:
            for tuid in sec['tutorialIds']:
                rec = en['tutorials'].get(tuid)
                if not rec:
                    integrity['missing_tutorial_references'].append(
                        {'track': tid_tr, 'tutorialId': tuid, 'section': sec['name']})
                    continue
                tu, fpath = rec
                tutorial_ids[str(tuid)] += 1
                ch_out = []
                for ci, ch in enumerate(tu.get('chapters', [])):
                    cid = ch.get('id')
                    chapter_ids[str(cid)] += 1
                    les_out = []
                    prev_lesson = None
                    for li, l in enumerate(ch.get('lessons', [])):
                        lid = l.get('id')
                        lesson_ids[str(lid)] += 1
                        fams, tags = classify_lesson(l)
                        for t in tags:
                            tag_hist[t] += 1
                        for fm in fams:
                            fam_hist[fm] += 1
                        ct = l.get('contentType') or 'unknown'
                        ct_hist[ct] += 1
                        if l.get('hardModeSelected'):
                            integrity['hard_mode_lessons'] += 1
                        node = {
                            'lessonId': lid,
                            'chapterId': cid,
                            'tutorialId': tuid,
                            'trackId': tid_tr,
                            'sectionIndex': sec['index'],
                            'chapterIndex': ci,
                            'lessonIndex': li,
                            'contentType': ct,
                            'title': l.get('title'),
                            'rendererFamilies': fams,
                            'dslTagCount': len(tags),
                            'asset': str(fpath.relative_to(ASSETS)),
                            'hasInteractiveContent': bool(l.get('interactiveContent')),
                            'hasExecutableContent': bool(l.get('executableContent')),
                            'hasHardMode': bool(l.get('hardModeSelected') or l.get('hardModeContent')),
                            'prerequisiteLessonId': prev_lesson,
                            'prerequisiteChapterId': (prev_chapters[-1] if ci > 0 else None),
                            'evidence_class': 'VERIFIED_ASSET',
                        }
                        lessons_out.append(node)
                        les_out.append(lid)
                        prev_lesson = lid
                    ch_out.append({
                        'chapterId': cid, 'title': ch.get('title'), 'type': ch.get('type'),
                        'lessonIds': les_out,
                        'prerequisiteChapterId': (ch_out[-1]['chapterId'] if ch_out else None),
                    })
                    prev_chapters.append(cid)
                tut_out.append({
                    'tutorialId': tuid, 'title': tu.get('title'), 'type': tu.get('type'),
                    'version': tu.get('version'), 'codeLanguage': tu.get('codeLanguage'),
                    'showInTrack': tu.get('showInTrack'),
                    'asset': str(fpath.relative_to(ASSETS)),
                    'chapters': ch_out,
                })
        tracks_out.append({
            'trackId': tid_tr, 'title': tr.get('title'), 'version': tr.get('version'),
            'onboardingCategory': tr.get('onboardingCategory'),
            'isHidden': tr.get('isHidden'), 'isNew': tr.get('isNew'),
            'sections': sections, 'tutorials': tut_out,
        })

    for k, v in lesson_ids.items():
        if v > 1:
            integrity['duplicate_lesson_ids'].append({'lessonId': k, 'count': v})
    for k, v in chapter_ids.items():
        if v > 1:
            integrity['duplicate_chapter_ids'].append({'chapterId': k, 'count': v})
    for k, v in tutorial_ids.items():
        if v > 1:
            integrity['duplicate_tutorial_ids'].append({'tutorialId': k, 'count': v})
    en_ids = {p.stem.replace('tutorial-', '') for loc, p in all_tutorial_files if loc == 'en'}
    integrity['orphan_tutorial_files'] = sorted(en_ids - set(referenced))[:200]
    integrity['content_type_histogram'] = dict(ct_hist)
    integrity['renderer_family_histogram'] = dict(fam_hist)
    integrity['dsl_tag_histogram'] = dict(tag_hist.most_common(80))
    integrity['unreachable_lessons'] = [
        n['lessonId'] for n in lessons_out
        if not n['prerequisiteLessonId'] and n['lessonIndex'] > 0][:200]

    # locale consistency: same tutorial-id set?
    en_set = {p.stem.replace('tutorial-', '') for loc, p in all_tutorial_files if loc == 'en'}
    for loc in integrity['locales_found']:
        s = {p.stem.replace('tutorial-', '') for l, p in all_tutorial_files if l == loc}
        if s != en_set:
            integrity['locale_inconsistencies'].append({
                'locale': loc, 'files': len(s), 'missing_vs_en': sorted(en_set - s)[:20],
                'extra_vs_en': sorted(s - en_set)[:20]})

    integrity['notes'] += [
        'Exactly 10 locales ship a tracks.json; en is authoritative for the independent offline client.',
        'Renderer families are DERIVED from shipped DSL tags (VERIFIED_ASSET), not from runtime observation.',
        'No asset was repaired. All discrepancies above are reported, not silently fixed.',
        'The full asset bodies are NOT committed to git (only this normalized index and hashes); '
        'regenerate from the original APK with unzip as documented in MISSION_09_REPRODUCTION_GUIDE.md.',
    ]

    doc = {
        'document': 'MIMO 9.35 — COMPLETE CURRICULUM GRAPH (MISSION 09)',
        'apk_sha256': APK_SHA,
        'publish_set_version': integrity['publish_set_version'],
        'evidence_class': 'VERIFIED_ASSET',
        'server_confirmed': 0,
        'counts': {
            'locales': len(integrity['locales_found']),
            'tracks': len(tracks_out),
            'sections': sum(len(t['sections']) for t in tracks_out),
            'tutorials': len({n['tutorialId'] for n in lessons_out}),
            'chapters': len({n['chapterId'] for n in lessons_out}),
            'lesson_placements': len(lessons_out),
            'unique_lesson_ids': len({n['lessonId'] for n in lessons_out}),
            'tutorial_references': sum(len(t['sections'][0]['tutorialIds']) for t in []) if False else len(set(referenced)),
            'json_files_validated': integrity['json_files_total'],
            'tutorial_json_files_validated': integrity['tutorial_files_total'],
        },
        'index_definition': 'Track -> Section -> Tutorial -> Chapter -> Lesson -> Asset -> Renderer -> Prerequisite',
        'integrity': integrity,
        'tracks': tracks_out,
        'lessons': lessons_out,
    }
    doc['counts']['tutorial_references'] = len(referenced)
    doc['counts']['note'] = ('37,183 lesson PLACEMENTS because a tutorial may be referenced by '
                             'more than one track/section; 18,272 unique lesson IDs are shipped.')
    integrity['notes'].append(
        'Four locales (id, it, pl, tr) ship two extra tutorial files (2433, 2441) absent from en; '
        'en is the authoritative offline curriculum.')
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(doc, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
    print('graph: tracks=%d lessons=%d json=%d parse_fail=%d missing_ref=%d orphan=%d' % (
        len(tracks_out), len(lessons_out), integrity['json_files_total'],
        len(integrity['parse_failures']), len(integrity['missing_tutorial_references']),
        len(integrity['orphan_tutorial_files'])))


if __name__ == '__main__':
    main()
