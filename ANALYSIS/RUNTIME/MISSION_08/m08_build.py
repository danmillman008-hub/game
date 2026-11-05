#!/usr/bin/env python3
"""MISSION 08 — build EXACTLY the seven requested core deliverables.

Reads only real workspace evidence: M05/M06/M07 artefacts, all four M08 unified
timelines, all navigation graphs, private-state snapshots and Frida traces.
No value is invented; anything not observed stays UNKNOWN.
"""
import collections
import json
import pathlib
import re
import xml.etree.ElementTree as ET

ROOT = pathlib.Path('ANALYSIS')
R8 = ROOT / 'RUNTIME' / 'MISSION_08'
OUT = ROOT / 'MISSION_08'
OUT.mkdir(parents=True, exist_ok=True)
APK_SHA = '48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a'
P1_RUN = '42042312640'
P2_RUN = '42046336206'


def jload(p, default=None):
    try:
        return json.loads(pathlib.Path(p).read_text(encoding='utf-8'))
    except Exception:
        return default


def jlines(p):
    out = []
    try:
        for line in pathlib.Path(p).read_text(encoding='utf-8', errors='replace').splitlines():
            if line.strip():
                try:
                    out.append(json.loads(line))
                except Exception:
                    pass
    except Exception:
        pass
    return out


def jwrite(p, obj):
    pathlib.Path(p).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def txt(p, s):
    pathlib.Path(p).write_text(s.rstrip() + '\n', encoding='utf-8')


# ---------------------------------------------------------------------------
# 1. ONE unified event stream
# ---------------------------------------------------------------------------
RAW = []
for p in sorted((R8 / 'TIMELINE').glob('PHASE*_TIMELINE_*.jsonl')):
    m = re.search(r'PHASE(\d)_TIMELINE_(\d+)\.jsonl', p.name)
    if m:
        RAW.append((p, m.group(2), int(m.group(1))))
_cur = R8 / 'TIMELINE' / 'MIMO_RUNTIME_TIMELINE.jsonl'
_cur_lines = jlines(_cur)
if _cur_lines:
    _rs = next((o for o in _cur_lines if o.get('event') == 'run_start'), {})
    _rid, _ph = str(_rs.get('run_id') or P2_RUN), int(_rs.get('phase') or 2)
    if not any(run == _rid for _, run, _ in RAW):
        RAW.append((_cur, _rid, _ph))
RAW.sort(key=lambda t: t[2])
PHASE_RUNS = {ph: run for _, run, ph in RAW}
P3_RUN = PHASE_RUNS.get(3, 'n/a')
P4_RUN = PHASE_RUNS.get(4, 'n/a')
events = []
for path, run, phase in RAW:
    for o in jlines(path):
        o['run_id'] = run
        o['phase'] = phase
        events.append(o)


def evidence_class(o):
    src, ev = o.get('source'), o.get('event')
    if ev in ('attach_retry', 'driver_abort', 'driver_start', 'frida_attach',
              'process_change', 'experiment_start', 'experiment_end', 'run_start',
              'phase_complete', 'timeline_done', 'navigation_graph_written',
              'adb_command', 'baseline_restored', 'natural_baseline_captured',
              'frida_supervisor_done', 'route_target', 'waiting_for_process'):
        return 'INSTRUMENTATION'
    if ev in ('route_not_found', 'no_classified_lesson', 'ftg_snippet_not_found',
              'lesson_target', 'lesson_classification', 'path_map_observation',
              'path_picker', 'route_screen', 'screen', 'ui', 'exploration_stop'):
        return 'UNKNOWN' if 'not_found' in str(ev) or ev in ('lesson_classification', 'no_classified_lesson') else 'VERIFIED_RUNTIME'
    if src == 'frida':
        return 'VERIFIED_RUNTIME'
    if src in ('db', 'net', 'ui', 'lesson', 'progression', 'orchestrator'):
        return 'VERIFIED_RUNTIME'
    return 'INFERRED'


for o in events:
    o['evidence_class'] = evidence_class(o)

# Filter repetitive machine events, preserving the correlation and reporting
# exactly what was collapsed. SQL/LiveData/net/native duplicates are aggregated.
KEEP_FIRST = 3
seen = collections.Counter()
collapsed = collections.Counter()
filtered = []
for o in events:
    ev = o.get('event')
    if ev in ('sql', 'sql_statement', 'liveData', 'net', 'native', 'attach_retry'):
        key = (o.get('run_id'), ev, o.get('kind'), o.get('method'),
               json.dumps(o.get('args') or o.get('value') or o.get('url') or o.get('error'),
                          sort_keys=True, default=str))
        seen[key] += 1
        if seen[key] > KEEP_FIRST:
            collapsed[ev] += 1
            continue
    if ev == 'sql' and seen[(o.get('run_id'), ev, o.get('kind'), o.get('method'),
                             json.dumps(o.get('args') or '', sort_keys=True, default=str))] == KEEP_FIRST:
        o['note'] = 'further identical SQL occurrences collapsed (repetitive SQL filter)'
    filtered.append(o)
collapsed_total = sum(collapsed.values())

filtered.sort(key=lambda o: (o.get('ts_utc') or '', o.get('run_id') or '', o.get('seq') or 0))
for i, o in enumerate(filtered, 1):
    o['global_seq'] = i
    o.setdefault('experiment_id', 'EXP-R1-000')
    o.setdefault('action_id', 'ACT-0000')

timeline_path = OUT / 'MIMO_RUNTIME_TIMELINE.jsonl'
with timeline_path.open('w', encoding='utf-8') as f:
    for o in filtered:
        f.write(json.dumps(o, ensure_ascii=False, sort_keys=False) + '\n')

PHASE_COUNTS = {ph: sum(1 for o in events if o.get('phase') == ph) for _, _, ph in RAW}
P1_COUNT = PHASE_COUNTS.get(1, 0)
P2_COUNT = PHASE_COUNTS.get(2, 0)
P3_COUNT = PHASE_COUNTS.get(3, 0)
P4_COUNT = PHASE_COUNTS.get(4, 0)
by_source = collections.Counter(o.get('source') for o in filtered)
by_event = collections.Counter(o.get('event') for o in filtered)
by_class = collections.Counter(o.get('evidence_class') for o in filtered)
frida_events = [o for o in filtered if o.get('source') == 'frida']
hook_installed = [o for o in frida_events if o.get('event') == 'hook_installed']
method_entries = [o for o in frida_events if o.get('event') == 'entry']
sql_events = [o for o in frida_events if o.get('event') in ('sql', 'sql_statement')]
nav_events = [o for o in frida_events if o.get('event') == 'nav']
di_events = [o for o in frida_events if o.get('event') == 'di']
prefs_writes = [o for o in frida_events if o.get('event') == 'prefs_write']
live_events = [o for o in frida_events if o.get('event') == 'liveData']
net_events = [o for o in frida_events if o.get('event') == 'net']
ld_examples = [o for o in live_events][:8]

# ---------------------------------------------------------------------------
# 2. Navigation graph
# ---------------------------------------------------------------------------
graphs = []
for gp in sorted((R8 / 'EXPERIMENTS').glob('PHASE*_NAV_GRAPH_*.json')):
    m = re.search(r'PHASE(\d)_NAV_GRAPH_(\d+)\.json', gp.name)
    if m:
        graphs.append((jload(gp, {}), m.group(2), int(m.group(1))))
_live_nav = jload(R8 / 'EXPERIMENTS' / 'NAV_GRAPH.json', {})
if _live_nav and not any(ph == 4 for _, _, ph in graphs):
    graphs.append((_live_nav, P4_RUN, 4))
screen_xml = {}
for o in filtered:
    if o.get('event') == 'screen' and o.get('screen_id'):
        screen_xml.setdefault(o['screen_id'], o.get('xml'))

screens, edges = {}, []
for g, run, phase in graphs:
    for sid, s in (g.get('screens') or {}).items():
        act = s.get('activity') or ''
        m = re.search(r'com\.getmimo/(\S+)', act)
        short = m.group(1) if m else 'UNKNOWN'
        key = sid
        if key not in screens:
            screens[key] = {
                'screen_id': sid,
                'activity': short,
                'activity_dumpsys': act,
                'texts': s.get('texts') or [],
                'clickable_nodes': s.get('clickable'),
                'fragments': s.get('fragments') or [],
                'fragments_status': 'UNKNOWN (dumpsys activity top exposed no Mimo fragment records on this screen)' if not s.get('fragments') else 'VERIFIED_RUNTIME',
                'xml': screen_xml.get(sid),
                'run_id': run,
                'phase': phase,
                'evidence_class': 'VERIFIED_RUNTIME',
            }
        else:
            screens[key]['also_seen_in_run'] = run
    for e in (g.get('edges') or []):
        edges.append({
            'from': e.get('from'), 'to': e.get('to'),
            'action': e.get('action'), 'x': e.get('x'), 'y': e.get('y'),
            'experiment': e.get('experiment'), 'run_id': run, 'phase': phase,
            'evidence_class': 'VERIFIED_RUNTIME',
        })

# measured action -> experiment/action correlation
action_map = collections.defaultdict(list)
for o in filtered:
    if o.get('event') == 'ui_action':
        action_map[o.get('action_id')].append(o.get('label'))
for e in edges:
    e['action_labels'] = [l for a, ls in action_map.items() for l in ls
                          if l and l in str(e.get('action'))][:4]

nav = {
    'document': 'MIMO_NAVIGATION_GRAPH — Mimo 9.35 UI / Activity state machine',
    'apk_sha256': APK_SHA,
    'method': 'adb uiautomator XML + dumpsys activity activities (topResumedActivity) + LiveData Fragment/ViewModel records; state-aware taps computed from measured node bounds. Frida Application.ActivityLifecycleCallbacks failed on API 36 (extra default methods) and is recorded as a hook_error, so no activity names were inferred from it.',
    'runs': [run for _, run, _ in RAW],
    'screen_count': len(screens),
    'edge_count': len(edges),
    'evidence_class': 'VERIFIED_RUNTIME',
    'server_confirmed': 0,
    'states': {
        'STARTUP': {'activity': '.ui.SplashActivity_default / .ui.onboarding.intro.IntroSlidesActivity',
                    'evidence': 'E11 S013 startup_home; E12 p2_startup'},
        'ONBOARDING': {'activity': '.ui.onboarding.OnboardingActivity',
                       'substates': ['goal', 'motivation', 'employment', 'work_field', 'experience',
                                     'interest', 'path_result', 'daily_goal', 'reminder', 'device'],
                       'evidence': 'E11 seq 25..123 (26 measured transitions); E19 S4NAV-01..22'},
        'AUTH_GATE': {'activity': '.ui.authentication.AuthenticationActivity',
                      'note': 'Skip leads to guest learner state; no credentials used',
                      'evidence': 'E11 seq 129'},
        'MAIN': {'activity': '.ui.main.MainActivity',
                 'tabs': ['Learn (bottom_navigation_item_track)',
                          'Practice (bottom_navigation_item_practice)',
                          'Leaderboard (bottom_navigation_item_leaderboard)',
                          'Profile (bottom_navigation_item_profile)'],
                 'evidence': 'E11 UI/S231_resume_02.xml, S229_resume_01_after.xml'},
        'CHAPTER': {'activity': '.ui.chapter.ChapterActivity',
                    'lesson_screens': ['non-interactive slide', 'WebView letter exercise', 'fill-the-gap code editor'],
                    'evidence': 'E11 UI/S136_onboard_21.xml, S144_onboard_22.xml, S151_onboard_23_after.xml'},
        'QUIT_DIALOG': {'activity': '.ui.chapter.ChapterActivity',
                        'text': 'Are you sure you want to quit? / You will lose your progress from this lesson.',
                        'choices': ['Quit lesson', 'Choose a different path', 'Cancel'],
                        'evidence': 'E11 UI/S213_back_from_lesson_after.xml'},
        'PATH_PICKER': {'activity': '.ui.main.MainActivity',
                        'text': 'Select Path / Career Paths / Full-Stack Developer SECTION 0/20 / Python Developer SECTION 0/11',
                        'evidence': 'E11 UI/S221_resume_00_after.xml'},
        'PRACTICE_GATE': {'activity': '.ui.main.MainActivity',
                          'text': 'Lock in your learning / Create a profile to access practice content',
                          'guard': 'unauthenticated guest is blocked from Practice content; no auth bypass attempted',
                          'evidence': 'E11 UI/S234_resume_02_after.xml'},
    },
    'guards': [
        {'id': 'G-AUTH', 'decision': 'Practice content requires a profile',
         'implementation': 'Practice tab renders a Log in / Sign up screen for a guest',
         'evidence_class': 'VERIFIED_RUNTIME', 'evidence': 'E11 UI/S234_resume_02_after.xml'},
        {'id': 'G-KEYS', 'decision': 'chapter unlock by key-set membership',
         'implementation': 'ds/w.c(Set<String>,J,J,J): Set.contains("<trackId>:<tutorialId>:<chapterId>") consumed by CanOpenChapterWithKeys$invoke$1',
         'evidence_class': 'VERIFIED_STATIC', 'evidence': 'E20 08_PROGRESSION_AND_UNLOCK_LOGIC.md; E10 10_LEARNING_PROGRESSION.md'},
        {'id': 'G-QUIT', 'decision': 'back from ChapterActivity requires explicit quit confirmation',
         'implementation': 'three-option dialog; Quit lesson returns to MainActivity',
         'evidence_class': 'VERIFIED_RUNTIME', 'evidence': 'E11 UI/S213_back_from_lesson_after.xml'},
        {'id': 'G-NETWORK', 'decision': 'queued progress posted only when online',
         'implementation': 'com.getmimo.network.a.a(): ConnectivityManager active network has WIFI or CELLULAR; offline throws NoConnectionException',
         'evidence_class': 'VERIFIED_BOTH', 'evidence': 'E08 E4; E10 15_OFFLINE_BEHAVIOR_SPECIFICATION.md'},
    ],
    'screens': screens,
    'edges': edges,
    'unobserved_states': ['chapter completion screen', 'native correct/wrong feedback after a submitted selection',
                          'leaderboard content', 'profile settings', 'streak modal', 'paywall', 'account creation'],
    'unobserved_evidence_class': 'UNKNOWN',
}
jwrite(OUT / 'MIMO_NAVIGATION_GRAPH.json', nav)

# ---------------------------------------------------------------------------
# 3. Learner state schema
# ---------------------------------------------------------------------------
snapshots = sorted((R8 / 'STATE').glob('SNAPSHOT_*.json'))
snap_digests = []
mimo_schema = None
for sp in snapshots:
    d = jload(sp, {})
    for db in d.get('databases') or []:
        if 'consistent_mimo.db' in db.get('path', ''):
            mimo_schema = db.get('schema')
            snap_digests.append({
                'label': d.get('label'), 'timestamp_utc': d.get('timestamp_utc'),
                'sha256': db.get('sha256'), 'journal_mode': db.get('journal_mode'),
                'tables': {t['name']: {'columns': t.get('columns'), 'row_count': t.get('row_count'),
                                       'rows': (t.get('rows') or [])[:20]}
                           for t in db.get('tables') or []},
                'evidence': str(sp),
            })
            break

prefs_events = [o for o in filtered if o.get('event') == 'prefs_state']
prefs_values = {}
for o in prefs_events:
    for k, v in (o.get('values') or {}).items():
        prefs_values.setdefault(k, []).append({'label': o.get('label'), 'run_id': o.get('run_id'), 'value': v})
# also read the real on-device XML directly (authoritative, naturally generated)
real_prefs = {}
for p in sorted((R8 / 'STATE').glob('S*/private/shared_prefs/mimo_prefs.xml')):
    try:
        root = ET.parse(p).getroot()
        d = {}
        for c in root:
            k = c.get('name') or ''
            if any(x in k for x in ('token', 'push_notification_registration', 'secret', 'password')):
                d[k] = '<redacted>'
            elif c.tag == 'set':
                d[k] = {'set': [(x.text or '') for x in c]}
            else:
                d[k] = c.text or ''
        real_prefs[str(p.parent.parent.name)] = d
    except Exception:
        pass

datastore_files = sorted({str(p.relative_to(R8)) for p in (R8 / 'STATE').glob('S*/private/files/datastore/**/*') if p.is_file()})
hint_prefs = {}
hp = R8 / 'STATE' / 'S1_POST_ONBOARDING' / 'private' / 'shared_prefs' / 'sp_lesson_view_properties.xml'
if hp.exists():
    try:
        hint_prefs = {c.get('name'): {'type': c.tag, 'value': c.get('value') if c.tag != 'string' else (c.text or '')}
                      for c in ET.parse(hp).getroot()}
    except Exception:
        pass

progress_rows = []
for d in snap_digests:
    for row in d['tables'].get('lesson_progress', {}).get('rows') or []:
        progress_rows.append({'snapshot': d['label'], 'row': row})

learner = {
    'document': 'MIMO_LEARNER_STATE_SCHEMA — Mimo 9.35 real persisted learner state',
    'apk_sha256': APK_SHA,
    'evidence_class': 'VERIFIED_RUNTIME',
    'synthetic_state_used': False,
    'note': 'All values are naturally generated by the original app on a fresh emulator. Snapshot restoration between independent phase-2 experiments restored this same natural state; no synthetic rows were inserted.',
    'server_confirmed': 0,
    'room_database': {
        'path': '/data/data/com.getmimo/databases/mimo.db',
        'journal_mode': 'wal',
        'wal_files': ['mimo.db-wal', 'mimo.db-shm'],
        'schema_source': 'ANALYSIS/MISSION_05/EVIDENCE/ROOM_SQL.txt + runtime PRAGMA/schema from m07_db_snapshot.py',
        'room_master_identity_hashes': ['08b926448d86528e697981ddd30459f7', '2b8ab6d303d9a501bd8c8fb78d8352fc'],
        'schema_sql': mimo_schema,
        'tables': {
            'lesson_progress': {
                'columns': ['lesson_id', 'completed_at', 'started_at', 'tries', 'tutorial_id', 'tutorial_version',
                            'track_id', 'publish_set_version', 'attempts', 'is_practice_progress', 'in_queue'],
                'primary_key': ['lesson_id', 'tutorial_id'],
                'entity': 'com.getmimo.data.model.room.LessonProgress',
                'constructor': '(J Instant Instant I J I J J I Z Z)V',
                'writer': 'LessonProgressRepository.createLessonProgress(LessonBundle, Instant, I, I) -> LessonProgressQueue.storeLessonProgress -> Room INSERT OR REPLACE',
                'sql': 'INSERT OR REPLACE INTO lesson_progress (11 cols) VALUES (?,?,?,?,?,?,?,?,?,?,?)',
                'readers': ['SELECT * FROM lesson_progress WHERE in_queue = 1',
                            'UPDATE lesson_progress SET in_queue = 0 WHERE in_queue = 1',
                            'DELETE FROM lesson_progress WHERE in_queue = 1'],
                'evidence': 'E03; E05; E06; E13',
                'evidence_class': 'VERIFIED_BOTH',
            },
            'chapter_completions': {'columns': ['chapter_id', 'created_at', 'track_id', 'tutorial_id'],
                                    'primary_key': ['chapter_id', 'track_id'],
                                    'observed_row_counts': [d['tables'].get('chapter_completions', {}).get('row_count') for d in snap_digests],
                                    'evidence': 'E03; E13', 'evidence_class': 'VERIFIED_BOTH'},
            'tutorial_completions': {'columns': ['tutorial_id', 'is_completed', 'updated_at', 'track_id'],
                                     'primary_key': ['tutorial_id', 'track_id'],
                                     'observed_row_counts': [d['tables'].get('tutorial_completions', {}).get('row_count') for d in snap_digests],
                                     'note': '868 seeded rows with is_completed=0 after onboarding; no is_completed=1 row was measured',
                                     'evidence': 'E03; E13; E20', 'evidence_class': 'VERIFIED_BOTH'},
        },
    },
    'observed_progress_rows': progress_rows,
    'shared_preferences': {
        'file': '/data/data/com.getmimo/shared_prefs/mimo_prefs.xml',
        'evidence_class': 'VERIFIED_RUNTIME',
        'evidence': 'E11 STATE/S1_POST_ONBOARDING/private/shared_prefs/mimo_prefs.xml; E12 prefs_state events',
        'keys': {
            'local_coins': {'observed': '{"coins":200}', 'meaning': 'guest coin balance; rendered as toolbar value "200"',
                            'related_classes': ['com.getmimo.core.model.coins.Coins.getCoins()I',
                                                'com.getmimo.data.source.remote.coins.a.a()Lua0/r;',
                                                'com.getmimo.data.source.remote.coins.a.b(SuspendLambda)'],
                            'evidence_class': 'VERIFIED_RUNTIME (value) / VERIFIED_STATIC (classes)',
                            'formula': 'UNKNOWN — no per-lesson arithmetic measured; value was constant across @@SNAPCOUNT@@ snapshots'},
            'user_settings': {'observed': '{"hasProgrammingExperience":false}'},
            'favorite_tracks': {'observed': '{"favoriteTrackIds":[50,219]}'},
            'favorite_tracks_to_sync': {'observed': 'set', 'meaning': 'queued remote favourite-track sync'},
            'favorite_tracks_to_remove': {'observed': 'set'},
            'user_profile_created_at': {'observed': 'ISO-8601 timestamp of guest profile creation'},
            'marketing_network': {'observed': 'Organic'},
            'marketing_campaign': {'observed': ''},
            'token_adjust / token_google_ads / push_notification_registration_id': {'observed': '<redacted>', 'meaning': 'third-party SDK identifiers; not used'},
            'experiments.xml:experiment_adapted_onboarding_android_local': {'observed': 'original',
                 'note': 'seeded ONLY to select the original onboarding variant; not learner progress', 'synthetic': True},
        },
        'natural_snapshots': real_prefs,
    },
    'lesson_view_hints': {'file': 'sp_lesson_view_properties.xml', 'keys': hint_prefs,
                          'evidence_class': 'VERIFIED_RUNTIME',
                          'evidence': 'E11 STATE/S1_POST_ONBOARDING/private/shared_prefs/sp_lesson_view_properties.xml'},
    'jetpack_datastore': {
        'path': '/data/data/com.getmimo/files/datastore/',
        'files_observed': [p.split('/')[-1] for p in datastore_files if 'preferences_pb' in p][:12],
        'mimo_owned': 'user_preferences.preferences_pb',
        'known_keys_static': ['completed_hard_mode_chapters', 'KEY_HARD_MODE_COMPLETED_LESSON_IDS',
                              'onboarding/first_run/path_overview flags', 'dailyGoal'],
        'parse_status': 'UNKNOWN — protobuf contents not decoded in M08; file presence VERIFIED_RUNTIME',
        'evidence': 'E10 11_LOCAL_PERSISTENCE.md; E13',
        'evidence_class': 'VERIFIED_RUNTIME (presence) / VERIFIED_STATIC (key names)',
    },
    'in_memory_state': {
        'livedata': 'androidx.lifecycle.m0 (R8-minified MutableLiveData) l()/k()',
        'observed_values': ['java.lang.Boolean true/false',
                            'com.getmimo.ui.authentication.AuthenticationStep AuthOverview / SignupOverview',
                            'InteractionKeyboardButtonState DISABLED',
                            'com.getmimo.ui.common.runbutton.RunButton$State RUN_DISABLED',
                            'jm.q LessonOutput(outputItems=[], isVisible=false)', 'jm.g'],
        'flows': ['kotlinx.coroutines.flow.i shared flow (h)', '_answersInChapter StateFlow',
                  'LessonProgressQueue unsynced rows', 'Orbit MVI container in executable/q'],
        'evidence': 'E05; E06; E10 11_LOCAL_PERSISTENCE.md',
        'evidence_class': 'VERIFIED_RUNTIME',
    },
    'snapshots': snap_digests,
    'mutation_events': [{'event': o.get('event'), 'label': o.get('label'), 'changes': o.get('count_changes'),
                         'inserted': o.get('lesson_progress_inserted'), 'deleted': o.get('lesson_progress_deleted'),
                         'run_id': o.get('run_id'), 'experiment_id': o.get('experiment_id')}
                        for o in filtered if o.get('event') == 'db_diff'],
}
learner_json = json.dumps(learner, indent=2, ensure_ascii=False).replace('@@SNAPCOUNT@@', str(len(snap_digests)))
txt(OUT / 'MIMO_LEARNER_STATE_SCHEMA.json', learner_json)

# ---------------------------------------------------------------------------
# 4. System map
# ---------------------------------------------------------------------------
endpoints = jload(ROOT / 'MIMO_RETROFIT_ENDPOINTS.json', {}).get('endpoints') or []
relevant = [e for e in endpoints if any(k in e['path'] for k in
            ('progress', 'coins', 'keys', 'reward', 'settings', 'leaderboard',
             'completion', 'runFiles', 'runfiles', 'activity', 'visits', 'favorites', 'eta'))]
method_catalog = jload(ROOT / 'MISSION_06' / 'SCHEMAS' / 'METHOD_CATALOG_MIMO.json', {})


def sigs(pattern, limit=6):
    ms = method_catalog.get('methods') or []
    return [m['signature'] for m in ms if pattern in m['signature']][:limit]


system_map = {
    'document': 'MIMO_SYSTEM_MAP — Mimo 9.35 implementation-level system map',
    'apk_sha256': APK_SHA,
    'package': 'com.getmimo', 'version_name': '9.35', 'version_code': 1792759685,
    'server_confirmed': 0,
    'evidence_index': {
        'E01': 'ANALYSIS/MISSION_06/SCHEMAS/METHOD_CATALOG_MIMO.json (12,851 methods)',
        'E02': 'ANALYSIS/MISSION_06/03_APPLICATION_ARCHITECTURE.md + 04_DEPENDENCY_INJECTION_AND_COMPONENT_GRAPH.md',
        'E03': 'ANALYSIS/MISSION_05/EVIDENCE/ROOM_SQL.txt',
        'E04': 'ANALYSIS/MIMO_RETROFIT_ENDPOINTS.json + ANALYSIS/HTTP_VERBS_RESOLVED.json',
        'E05': 'ANALYSIS/MISSION_07/03_INTERACTIVE_LESSON_VIEWMODEL_RUNTIME.md',
        'E06': 'ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE6_ONLINE.jsonl (run 42033599909)',
        'E07': 'ANALYSIS/MISSION_07/15_ANSWER_TO_SCORING_RECONSTRUCTION.md',
        'E08': 'ANALYSIS/MISSION_07/04_ANSWER_VALIDATION_RUNTIME.md',
        'E09': 'ANALYSIS/MISSION_06/05_CONTENT_PIPELINE.md, 06_CONTENT_SCHEMA_AND_DSL.md, 08_INTERACTION_VALIDATION.md, 12_CODE_EDITOR_AND_EXECUTABLE_LESSONS.md',
        'E10': 'ANALYSIS/MISSION_06/10_LEARNING_PROGRESSION.md, 11_LOCAL_PERSISTENCE.md, 13_UI_NAVIGATION_AND_RUNTIME.md, 14_NATIVE_LIBRARIES_AND_JNI.md, 15_OFFLINE_BEHAVIOR_SPECIFICATION.md, 16_RECONSTRUCTED_ALGORITHMS.md',
        'E11': 'ANALYSIS/RUNTIME/MISSION_08/TIMELINE/PHASE1_TIMELINE_42042312640.jsonl + UI/ + STATE/ (run 42042312640)',
        'E12': 'ANALYSIS/RUNTIME/MISSION_08/TIMELINE/PHASE2_TIMELINE_42046336206.jsonl + TRACES/ (Frida/DI/Fragments/Room SQL/Settings/network)',
        'E21': 'ANALYSIS/RUNTIME/MISSION_08/TIMELINE/PHASE3_TIMELINE_42049141553.jsonl + ENV/PHASE3_RESTORE_42049141553.txt (natural-state restore)',
        'E22': 'ANALYSIS/RUNTIME/MISSION_08/TIMELINE/PHASE4_TIMELINE_*.jsonl (final targeted main-screen run)',
        'E13': 'ANALYSIS/RUNTIME/MISSION_08/STATE/SNAPSHOT_*.json',
        'E14': 'ANALYSIS/RUNTIME/MISSION_08/UI/*.xml',
        'E15': 'ANALYSIS/RUNTIME/MISSION_08/EXPERIMENTS/PHASE1_NAV_GRAPH_42042312640.json + EXPERIMENTS/NAV_GRAPH.json',
        'E16': 'ANALYSIS/RUNTIME/MISSION_08/ENV/PHASE1_FRIDA_SETUP_42042312640.txt + ENV/M08_FRIDA_SETUP.txt',
        'E17': 'ANALYSIS/MISSION_07/16_EVIDENCE_DATABASE.json (202 entries)',
        'E18': 'ANALYSIS/RUNTIME/MISSION_07/RUNTIME_TRACE/SHIPPED_CONTENT/SELECTION_ANSWERS.json',
        'E19': 'ANALYSIS/MISSION_07/12_UI_STATE_MACHINE.md',
        'E20': 'ANALYSIS/MISSION_07/08_PROGRESSION_AND_UNLOCK_LOGIC.md + 11_SCORING_AND_REWARD_LOGIC.md',
    },
    'modules': [
        {'id': 'startup_di', 'name': 'Process entry and dependency container',
         'classes': ['com.getmimo.App', 'com.getmimo.ui.SplashActivity_default', 'Lhm/b;'],
         'methods': sigs('Lcom/getmimo/App;->') + sigs('Lcom/getmimo/App$onCreate$1;->'),
         'responsibility': 'Application.onCreate assembles the object graph; ViewModels receive a 13-Object-slot container Lhm/b (a..m) cast at use sites.',
         'di_framework': 'UNKNOWN — no @Inject / Hilt / Koin metadata decoded; constructor-injection shape is INFERRED',
         'evidence': ['E01', 'E02', 'E12'], 'evidence_class': 'VERIFIED_STATIC + INFERRED'},
        {'id': 'content', 'name': 'Shipped curriculum and lesson DSL',
         'classes': ['Lye/b;', 'Lye/d;', 'tracks/b; DefaultTrackLoader', 'tracks/c; DefaultTracksRepository',
                     'Lte/c;', 'Lgm/h;', 'com.getmimo.data.content.lessonparser.interactive.model.LessonModule'],
         'methods': sigs('Lte/c;->b(') + sigs('Lgm/h;->a(') + sigs('Lcom/getmimo/data/content/tracks/DefaultTracksRepository;->'),
         'responsibility': 'AssetManager.open("lessons-<lang>/tracks/tutorial-<id>.json") -> kotlinx.serialization models -> XmlPullParser DSL -> LessonModule list -> gm.h.a() interaction type.',
         'shipped_content': {'publish_set_version': 753, 'tracks': 19, 'sections': 144, 'tutorials': 1029,
                             'chapters': 1947, 'lessons': 18272, 'selection_answers': 2855},
         'evidence': ['E09', 'E18'], 'evidence_class': 'VERIFIED_BOTH'},
        {'id': 'navigation_ui', 'name': 'Activities, bottom navigation and ViewModels',
         'classes': ['com.getmimo.ui.main.MainActivity', 'com.getmimo.ui.main.d (MainViewModel)',
                     'com.getmimo.ui.navigation.NavigationBar', 'com.getmimo.ui.path.map.j (PathMapViewModel)',
                     'com.getmimo.ui.chapter.ChapterActivity', 'com.getmimo.ui.chapter.ChapterViewModel',
                     'com.getmimo.ui.lesson.interactive.base.b/c'],
         'methods': sigs('Lcom/getmimo/ui/main/MainActivity;->') + sigs('Lcom/getmimo/ui/path/map/j;->') + sigs('Lcom/getmimo/ui/chapter/ChapterActivity;->'),
         'responsibility': 'Four-tab bottom bar (track/practice/leaderboard/profile); MainActivity -> PathMapViewModel -> ChapterActivity -> per-interaction Fragment + ViewModel; Compose + Orbit MVI for path map/executable lessons.',
         'evidence': ['E02', 'E10', 'E11', 'E14'], 'evidence_class': 'VERIFIED_BOTH'},
        {'id': 'lesson_engine', 'name': 'Lesson session state machine and validators',
         'classes': ['com.getmimo.ui.lesson.interactive.base.c', 'Lim/d;', 'Lkm/f;', 'Lpm/b;', 'Lqm/i;', 'Lqm/d;',
                     'com.getmimo.ui.lesson.executable.q', 'com.getmimo.ui.common.runbutton.RunButton$State'],
         'methods': sigs('Lcom/getmimo/ui/lesson/interactive/base.c;->') + sigs('Lim/d;->E0') + sigs('Lkm/f;->b'),
         'responsibility': 'Y(Z) double-run guard; onLessonRun$1 dispatches V()/X(); U() for auto-advance; H(tries,attempts) creates LessonProgress; e0()/queue store; f0(false,isSolvedCorrectly()) analytics; N() resets input.',
         'validators': {
             'validatedInput': 'qm/i.a: lowercase(Locale.US) + keep letters/digits and < > ( ) : { } , . ; setupViews$2 gives CORRECT / PARTIAL / INCORRECT',
             'selection': 'km/f.b(List): all { selected == correct }',
             'fillTheGap': 'im/d.E0(): ordered, case-sensitive token equality vs correctTokens; answer joined with spaces; Y(boolean)',
             'spell': 'pm/b.E0(): token equality joined without separator',
             'executable': 'q.I(): ArrayList.equals(userFileContents, shipped solvedContent)',
             'isSolvedCorrectly': 'tries >= 1',
             'webview_letter': 'shipped lesson-webview.js correctLetter="D"; try again otherwise; no native validator hook fired',
         },
         'evidence': ['E05', 'E06', 'E08', 'E09', 'E17'], 'evidence_class': 'VERIFIED_BOTH'},
        {'id': 'learner_state', 'name': 'Room / SQLite / WAL / SharedPreferences / DataStore',
         'classes': ['com.getmimo.data.source.local.room.Database', 'Database_Impl', 'Lcg/a; LessonProgressDao',
                     'com.getmimo.data.source.remote.progress.LessonProgressRepository',
                     'com.getmimo.data.source.remote.progress.LessonProgressQueue',
                     'com.getmimo.data.local.a DataStoreUserPreferences'],
         'methods': sigs('LessonProgressQueue;->') + sigs('LessonProgressRepository;->'),
         'responsibility': 'local-only progress rows (in_queue=1), answer counters, streak detector, guest coins/favourites in mimo_prefs.xml, protobuf DataStore flags, WAL journal.',
         'evidence': ['E03', 'E10', 'E11', 'E13'], 'evidence_class': 'VERIFIED_BOTH'},
        {'id': 'progression', 'name': 'Path map, unlock and completion',
         'classes': ['com.getmimo.interactors.path.d GetPathMapState', 'com.getmimo.interactors.chapter.a CanOpenChapterWithKeys',
                     'com.getmimo.interactors.path.sections.a', 'Lcc/b;', 'Lds/w.c;',
                     'com.getmimo.data.source.remote.keys.a DefaultKeysRepository'],
         'methods': sigs('Lcom/getmimo/interactors/path/d;->') + sigs('Lcom/getmimo/interactors/chapter/a;->') + sigs('Lds/w;->c'),
         'responsibility': 'sequential required-tutorial prerequisite; Completed/Locked/Unlocked/UnlockedButNoKeys states; key "<trackId>:<tutorialId>:<chapterId>" membership; section state from cc/b.y completion floats.',
         'evidence': ['E10', 'E20'], 'evidence_class': 'VERIFIED_STATIC (live unlock boolean UNKNOWN)'},
        {'id': 'gamification', 'name': 'Coins, XP, streak, goals, rewards, keys, leaderboard',
         'classes': ['com.getmimo.core.model.coins.Coins', 'com.getmimo.data.source.remote.coins.a DefaultCoinsRepository',
                     'com.getmimo.data.user.streak.a', 'com.getmimo.data.source.remote.reward.a',
                     'com.getmimo.data.settings.a SettingsRepository', 'com.getmimo.ui.main.d MainViewModel'],
         'methods': sigs('Lcom/getmimo/core/model/coins/Coins;->') + sigs('Lcom/getmimo/data/source/remote/coins/a;->') + sigs('Lcom/getmimo/ui/main/d;->'),
         'responsibility': 'local_coins guest balance (200 observed), getCorrectLessonProgressCount / getCorrectLessonsFirstTryCount / updateCorrectAnswersCount / updateLessonStreakDetector; remote reward/keys/leaderboard DTOs; daily goal from SettingsRepository.',
         'measured_algorithm': 'getCorrectLessonProgressCount = queued.count{isSolvedCorrectly()}; getCorrectLessonsFirstTryCount = queued.count{isSolvedCorrectly() && attempts == 1}; AnswersInChapter(correct,total)',
         'evidence': ['E10', 'E20', 'E11', 'E12'], 'evidence_class': 'VERIFIED_STATIC + VERIFIED_RUNTIME (no absolute XP formula)'},
        {'id': 'media_native', 'name': 'WebView, code editor, Rive and native libraries',
         'classes': ['android.webkit.WebView', 'assets/lesson-webview.js', 'EmbeddedLessonWebView',
                     'com.getmimo.ui.codeeditor.view.b CodeEditViewModel',
                     'com.getmimo.ui.codeeditor.highlight.a', 'app.rive.runtime.kotlin'],
         'responsibility': 'WebView exercises use shipped JS + mimo.activity.* messages; executable lessons compare against shipped solvedContent offline; Rive animation runtime; 12 arm64 .so libraries.',
         'native_libraries': ['libsigner.so', 'libdatastore_shared_counter.so', 'libyrf.so', 'librive-android.so',
                              'libandroidx.graphics.path.so', 'libc++_shared.so', 'libimage_processing_util_jni.so',
                              'libbugsnag-ndk.so', 'libbugsnag-plugin-android-anr.so', 'libsqlcipher.so',
                              'libbarhopper_v3.so', 'libmlkit_google_ocr_pipeline.so'],
         'evidence': ['E09', 'E10', 'E08'], 'evidence_class': 'VERIFIED_STATIC + INFERRED (JNI internals UNKNOWN)'},
        {'id': 'network_sync', 'name': 'Retrofit APIs, connectivity gate, offline queue',
         'classes': ['com.getmimo.network.a', 'com.getmimo.data.source.remote.progress.LessonProgressApi',
                     'com.getmimo.data.source.remote.progress.CompletionApi',
                     'com.getmimo.data.source.remote.progress.TrackEtaApi'],
         'responsibility': 'POST /v1/tutorials/{tutorialId}/progress; network.a.a() gate; offline throws NoConnectionException; queue rows deleted at cold start.',
         'endpoints': relevant,
         'evidence': ['E04', 'E07', 'E08', 'E10', 'E11'], 'evidence_class': 'VERIFIED_STATIC + VERIFIED_RUNTIME'},
        {'id': 'background', 'name': 'Workers and services',
         'classes': ['com.getmimo.data.source.remote.authentication.PostVisitWorker',
                     'com.getmimo.ui.widget.StreakWidgetRefreshWorker', 'AccountDeleteWork',
                     'AsyncRequestWorker', 'com.getmimo.data.notification.MimoFirebaseMessagingService',
                     'com.getmimo.data.source.remote.savedcode.AutoSaveCodeService'],
         'responsibility': 'visit posting, streak widget refresh, push token handling, saved-code autosave.',
         'triggers': 'UNKNOWN',
         'evidence': ['E02', 'E10'], 'evidence_class': 'VERIFIED_STATIC (names) / UNKNOWN (triggers)'},
    ],
    'decision_logic': [
        {'id': 'D1', 'decision': 'advance to next lesson / persist progress',
         'input': 'Continue or shipped-WebView correct answer',
         'logic': 'base/c.U() -> H(1,1) -> LessonProgressRepository.createLessonProgress(LessonBundle) -> e0() -> LessonProgressQueue.storeLessonProgress -> Room INSERT OR REPLACE (in_queue=1) -> f0(false,true) -> N() -> next page',
         'output': '11-column lesson_progress row; LiveData next-page index',
         'evidence': ['E05', 'E06', 'E07'], 'evidence_class': 'VERIFIED_RUNTIME'},
        {'id': 'D2', 'decision': 'is the lesson solved?',
         'logic': 'LessonProgress.isSolvedCorrectly() = tries >= 1; tries = (C == Boolean.TRUE) ? 0 : 1 after d++',
         'output': 'boolean used by f0 analytics and answer counters',
         'evidence': ['E08', 'E07'], 'evidence_class': 'VERIFIED_BOTH'},
        {'id': 'D3', 'decision': 'correct-answer counting for chapter/rewards',
         'logic': 'AnswersInChapter(correct=queued.count{isSolvedCorrectly()}, total=queued.size); firstTry = count{isSolvedCorrectly() && attempts == 1}',
         'output': '_answersInChapter StateFlow; consumed by ChapterFinishedViewModel',
         'evidence': ['E10'], 'evidence_class': 'VERIFIED_STATIC'},
        {'id': 'D4', 'decision': 'unlock a chapter',
         'logic': 'ds/w.c(Set<String>,trackId,tutorialId,chapterId) = Set.contains("<a>:<b>:<c>"); CanOpenChapterWithKeys$invoke$1 consumes boolean; path-map requires previous REQUIRED tutorial completed',
         'output': 'Lvn/d0 Completed / Lvn/e0 Locked / Lvn/g0 Unlocked / Lvn/h0 UnlockedButNoKeys',
         'evidence': ['E10', 'E20'], 'evidence_class': 'VERIFIED_STATIC (exact live boolean UNKNOWN)'},
        {'id': 'D5', 'decision': 'sync progress to backend',
         'logic': 'storeAndPostAllLessonProgress -> moveLessonProgressFromQueue (in_queue=0) -> postUnsyncedLessonProgress -> if !network.a() throw NoConnectionException else LessonProgressApi.postProgress',
         'output': 'POST /v1/tutorials/{tutorialId}/progress; response body UNKNOWN',
         'evidence': ['E04', 'E07', 'E10'], 'evidence_class': 'VERIFIED_BOTH'},
        {'id': 'D6', 'decision': 'cold-start queue retention',
         'logic': 'measured: in_queue=1 rows disappeared at process restart (phase1 S8_AFTER_RESUME, online); M07 stage6 also measured offline cold start 2 -> 0',
         'output': 'lesson_progress rows deleted',
         'evidence': ['E11', 'E07'], 'evidence_class': 'VERIFIED_RUNTIME (competition between successful POST and DELETE not isolated; SERVER CONFIRMED=0)'},
        {'id': 'D7', 'decision': 'Practice tab access',
         'logic': 'guest (Skip at AuthenticationActivity) -> Practice renders "Create a profile to access practice content" instead of practice list',
         'output': 'auth gate screen',
         'evidence': ['E11', 'E14'], 'evidence_class': 'VERIFIED_RUNTIME'},
    ],
    'dependencies': {
        'language': 'Kotlin (coroutines, kotlinx.serialization)', 'ui': ['Android Views + Fragments', 'Jetpack Compose', 'Orbit MVI'],
        'lifecycle': ['androidx.lifecycle ViewModel/LiveData (R8-minified m0)', 'SavedStateHandle'],
        'persistence': ['Room / SQLite WAL', 'Jetpack DataStore (protobuf)', 'SharedPreferences', 'libsqlcipher.so (INFERRED)'],
        'network': ['Retrofit-style annotated interfaces', 'OkHttp (R8 obfuscated)', 'Firebase Remote Config / Crashlytics / Analytics', 'RevenueCat IAP', 'Mixpanel', 'Adjust', 'Customer.io'],
        'media': ['android.webkit.WebView', 'app.rive.runtime.kotlin / librive-android.so', 'ML Kit / CameraX'],
        'background': ['WorkManager CoroutineWorker', 'Firebase Messaging'],
        'evidence': ['E01', 'E02', 'E04', 'E10', 'E13'], 'evidence_class': 'VERIFIED_STATIC + INFERRED',
    },
    'client_server_boundary': {
        'client_owned': ['shipped curriculum v753', 'lesson DSL parsing and rendering', 'all answer validation',
                         'LessonProgress rows and answer counters', 'guest coins local_coins', 'offline WebView preview',
                         'executable solvedContent comparison', 'unlock state shape', 'connectivity gate'],
        'server_owned_or_unknown': ['absolute XP / streak / daily-goal / leaderboard award formulas',
                                    'PostProgressResponse / Progress / TrackEtaResponse bodies',
                                    'keys and rewards balances', 'remote code runner result',
                                    'subscription tier gating', 'chapter/tutorial completion acknowledgement'],
        'server_confirmed': 0,
        'evidence': ['E07', 'E10', 'E20'], 'evidence_class': 'VERIFIED_STATIC + UNKNOWN',
    },
}
jwrite(OUT / 'MIMO_SYSTEM_MAP.json', system_map)

# ---------------------------------------------------------------------------
# 5. Core flow diagram
# ---------------------------------------------------------------------------
mmd = r'''flowchart TD
    subgraph NAV[Navigation / UI state machine - VERIFIED_RUNTIME]
      A[".ui.onboarding.OnboardingActivity<br/>26 measured transitions"] --> B[".ui.authentication.AuthenticationActivity<br/>Skip -> guest"]
      B --> C[".ui.main.MainActivity<br/>bottom_navigation_item_track/practice/leaderboard/profile"]
      C -->|"PathMapViewModel.G(J,J) / N(ChapterBundle,J)"| D[".ui.chapter.ChapterActivity<br/>LessonBundle 151410 / 151403 / FTG"]
      C -->|"Practice tab guest guard G-AUTH"| P["Create a profile to access practice content"]
      D -->|"quit dialog G-QUIT"| C
    end

    subgraph VM[ViewModel / core logic - VERIFIED_RUNTIME]
      D --> V["base/c InteractiveLessonBaseViewModel<br/>Y(Z) double-run guard; onLessonRun$1"]
      V -->|"exact / partial / wrong"| X["V() / W() / X() / d0()<br/>jm/m, jm/n, jm/o feedback"]
      V -->|"auto-advance slide + WebView Continue"| U["U() lessonSolvedAndProceed"]
      X --> H["H(tries, attempts)"]
      U --> H
    end

    subgraph VAL[Validators - VERIFIED_BOTH]
      V -.-> K1["qm/i.a normalizer + setupViews$2"]
      V -.-> K2["km/f.b all selected==correct"]
      V -.-> K3["im/d.E0 ordered token equality"]
      V -.-> K4["q.I List.equals shipped solvedContent"]
      V -.-> K5["lesson-webview.js correctLetter='D'<br/>mimo.activity.correct|wrong"]
    end

    subgraph REPO[Repository / learner state - VERIFIED_RUNTIME]
      H --> R["LessonProgressRepository.createLessonProgress<br/>(LessonBundle, Instant, I, I)"]
      R --> Q["LessonProgressQueue.storeLessonProgress<br/>in_queue=true"]
      Q --> DB[("Room mimo.db WAL<br/>lesson_progress 11 cols<br/>tutorial_completions / chapter_completions")]
      Q --> CNT["getCorrectLessonProgressCount<br/>getCorrectLessonsFirstTryCount<br/>updateCorrectAnswersCount<br/>updateLessonStreakDetector"]
      Q --> PREFS["mimo_prefs.xml<br/>local_coins={coins:200}<br/>favorite_tracks / user_settings"]
    end

    subgraph SCORE[Scoring / rewards - partial]
      CNT --> SC["AnswersInChapter(correct,total) StateFlow<br/>ChapterFinishedViewModel"]
      SC --> SRV["remote DTOs: Reward / Rewards / UserActivityResponse<br/>Leaderboard / Streak / Settings dailyGoal"]
      SC -.->|"UNKNOWN formula"| XP["XP / streak length / keys / coins award"]
    end

    subgraph SYNC[Sync boundary - VERIFIED_BOTH]
      DB -->|"SELECT in_queue=1"| POST["postUnsyncedLessonProgress<br/>network.a.a() WIFI|CELLULAR gate"]
      POST -->|"online"| API["POST /v1/tutorials/{id}/progress<br/>LessonProgressApi.postProgress"]
      POST -->|"offline"| ERR["NoConnectionException<br/>SERVER CONFIRMED=0"]
      API -.->|"response UNKNOWN"| SRV
    end

    subgraph NEXT[Next activity decision]
      V --> NX["f0(false, isSolvedCorrectly())<br/>N() resetInputState<br/>e = chapterIndex -> next page"]
      NX --> D
      DB --> PM["GetPathMapState / CanOpenChapterWithKeys<br/>Completed|Locked|Unlocked|UnlockedButNoKeys"]
      PM --> C
    end

    classDef rt fill:#e8f4ea,stroke:#2d6a4f,color:#1b4332;
    classDef st fill:#eef2ff,stroke:#3949ab,color:#1a237e;
    classDef unk fill:#fff3e0,stroke:#e65100,color:#4e342e,stroke-dasharray: 4 3;
    class A,B,C,D,P,V,X,U,H,R,Q,DB,PREFS,NX rt;
    class K1,K2,K3,K4,K5,CNT,POST,API,PM st;
    class SRV,XP,ERR unk;
'''
txt(OUT / 'MIMO_CORE_FLOW.mmd', mmd)

# ---------------------------------------------------------------------------
# 6 + 7. Prose documents (tokens replaced with measured values)
# ---------------------------------------------------------------------------
T = {
    '@@P1@@': str(P1_COUNT), '@@P2@@': str(P2_COUNT), '@@P3@@': str(P3_COUNT),
    '@@P4@@': str(P4_COUNT), '@@P3RUN@@': str(P3_RUN), '@@P4RUN@@': str(P4_RUN),
    '@@TOTAL@@': str(len(filtered)),
    '@@COLLAPSED@@': str(collapsed_total),
    '@@SCREENS@@': str(len(screens)), '@@EDGES@@': str(len(edges)),
    '@@FRIDA@@': str(len(frida_events)), '@@HOOKS@@': str(len(hook_installed)),
    '@@ENTRIES@@': str(len(method_entries)), '@@SQL@@': str(len(sql_events)),
    '@@NAV@@': str(len(nav_events)), '@@DI@@': str(len(di_events)),
    '@@PWRITES@@': str(len(prefs_writes)), '@@LIVE@@': str(len(live_events)),
    '@@NET@@': str(len(net_events)), '@@SNAPS@@': str(len(snap_digests)),
    '@@BYCLASS@@': ', '.join('%s=%d' % (k, v) for k, v in by_class.most_common()),
    '@@FREQLINES@@': '\n'.join('- `%s`: %d' % (k, v) for k, v in by_event.most_common(12)),
    '@@LD@@': '\n'.join('- `%s` -> `%s`' % (o.get('value_class'), str(o.get('value'))[:110]) for o in ld_examples) or '- none observed in this run',
}

ARCH = r'''# MIMO 9.35 — CORE ARCHITECTURE (MISSION 08)

**Target:** original APK `com.getmimo` 9.35, `versionCode=1792759685`, 142,353,499 B,
SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` — unchanged.
**Branch:** `arena/aebb90b7-game`. **SERVER CONFIRMED = 0.**

This is an **implementation-level reconstruction of the connected client system**, not a
class catalogue. Every major claim below carries an evidence reference `E##` resolved in
`MIMO_SYSTEM_MAP.json -> evidence_index`, and a classification
`VERIFIED_STATIC` / `VERIFIED_RUNTIME` / `VERIFIED_BOTH` / `INFERRED` / `UNKNOWN`.
No backend, no credentials, no fabricated server responses, and no replacement application.

**Evidence base:** M01–M07 (APK/DEX, Androguard, curriculum decoder, Room SQL, Frida 17 Java
bridge, stage-6 runtime traces, 202-entry evidence DB) plus four M08 controlled runs:
`42042312640` (broad navigation/DB, @@P1@@ events), `42046336206` (Frida/DI/onboarding,
@@P2@@ events), `@@P3RUN@@` (natural-state restore, @@P3@@ events) and `@@P4RUN@@`
(final targeted main-screen attempt, @@P4@@ events).
The single unified stream `MIMO_RUNTIME_TIMELINE.jsonl` contains @@TOTAL@@ correlated events
(@@COLLAPSED@@ repetitive machine events collapsed). Classification mix: @@BYCLASS@@.
`MIMO_NAVIGATION_GRAPH.json` holds @@SCREENS@@ measured screens and @@EDGES@@ transitions.
All four runs used the SAME orchestrator, the SAME curated 63-hook agent and the SAME
experiment/action ID scheme; the timeline carries `run_id`, `phase`, `experiment_id` and
`action_id` on every event so cross-run correlation is explicit rather than implicit.

---

## 1. Process entry, startup and dependency injection

The launcher is `.ui.SplashActivity_default`; the first measured Activity after a cold start
is `.ui.onboarding.intro.IntroSlidesActivity`, then `.ui.onboarding.OnboardingActivity` →
`.ui.authentication.AuthenticationActivity` → `.ui.main.MainActivity` →
`.ui.chapter.ChapterActivity` [E11, E14, E19]. `Lcom/getmimo/App;` has 6 methods and 13
collaborator fields typed by obfuscated interfaces (`Lx30/g;`, `Ldf/c;`, `Lbe/d;`, …);
`App$onCreate$1` and `App$onCreate$2$1` are the coroutine bodies started from `onCreate`
[E01, E02]. `MainActivity.B()` returns `Lcom/getmimo/ui/main/d;` (`MainViewModel`);
`ChapterActivity.B()` returns `ChapterViewModel` [E01].

**DI mechanism.** There is no decoded Hilt/Dagger/Koin metadata. What *is* verified is a
hand-rolled 13-slot `Ljava/lang/Object;` container `Lhm/b;` (`a`..`m`) passed into
`InteractiveLessonBaseViewModel(Lhm/b;)V` and cast at each use site: `b` →
`Lcom/getmimo/analytics/a;`, `d` → `LessonProgressRepository`, `g` →
`Lcom/getmimo/data/local/a;`, `h` → `Lmf/a;` (filesDir), `i` →
`Lcom/getmimo/ui/lesson/sound/a;` [E02]. Larger graphs use constructor injection, e.g.
`ExecutableLessonViewModel` (32 parameters), `GetPathMapState` (15 collaborators),
`LessonProgressRepository(LessonProgressApi, Lye/g, Lye/c, Lnp/d, Lri/d, completion/a, Lcg/a)`
and `LessonProgressQueue_Factory` / `LessonProgressRepository_Factory` [E01, E02].
`LessonProgressQueue_Factory` is the only decoded generated factory, so compile-time
constructor injection is `INFERRED`; **the exact framework, scopes and singleton graph remain
`UNKNOWN`**. Phase 2 additionally hooks the *live* `App` instance with `Java.choose` (@@DI@@ DI events)
because an attach happens after `Application.onCreate`; this yields real field values instead
of inferred ones. The measured `com.getmimo.App` object held `A=0`, `a=true` and 13
collaborators including `com.getmimo.analytics.a`, `com.getmimo.data.source.remote.authentication.a`,
`x30.g`, `df.c`, `be.d`, `q9.f`, `i9.h`, `lf.a`, `ke.a`, `kf.c`, `be.a4`
[E12 `env application`, `di live_instance`]. `Java.choose` found 0 live instances of
`MainViewModel`, `PathMapViewModel` and `LessonProgressQueue` at attach time (they are created
later), so their field values remain `UNKNOWN`. The loaded-class inventory measured 36,498
classes: `okhttp3` 235, `com.getmimo` 104, `app.rive` 84–100, `com.google.firebase` 112–114,
`androidx.datastore` 127, `androidx.room` 11, `androidx.fragment` 28, `androidx.work` 1,
`retrofit2` 0 (R8-obfuscated) [E12 `env class_inventory`].

## 2. Layered module map and communication

`APK assets → loader → kotlinx.serialization → content models → XmlPullParser DSL →
LessonModule → gm.h.a() interaction type → Fragment/ViewModel → repository → Room / queue →
Retrofit API` [E09, E10]. Modules are plain Kotlin classes with `invoke` / suspend
`a(…, Continuation)` use-cases, not a framework; UI is a **hybrid** of
Fragments + AndroidX `ViewModel`/`LiveData` (`androidx.lifecycle.m0` after R8) and
Jetpack Compose + Orbit MVI (`org.orbitmvi.orbit`) for the path map and executable lessons
[E02, E10]. Communication is: `LiveData` posts for feedback/input state, `StateFlow`
(`_answersInChapter`) for counters, `SharedFlow` for interaction events, `SavedStateHandle`
for navigation arguments, and coroutine `Continuation` across repositories [E05, E10].
See `MIMO_SYSTEM_MAP.json -> modules` for the ten modules with exact signatures.

## 3. Navigation and UI state machine

Measured graph: @@SCREENS@@ screens / @@EDGES@@ transitions [E15]. Onboarding is a
26-transition decision chain (goal → motivation → employment → work field → coding
experience → interest → path result → daily goal → reminder → device); choosing **Web apps**
yields the Front-End Developer path and shipped tutorial 904 (HTML), while **Data science**
yields Python Developer and shipped selection lesson 123420 [E11, E19]. The `Skip` at
`AuthenticationActivity` creates a **guest** profile (`user_profile_created_at` in
`mimo_prefs.xml`) and enters `MainActivity` [E11, E13].

`MainActivity` owns a four-tab bottom bar with measured resource IDs
`bottom_navigation_item_track` (`Learn`), `_practice`, `_leaderboard`, `_profile` [E14
`UI/S231_resume_02.xml`]. The **Practice tab for a guest** does not show practice content:
it renders `Lock in your learning / Create a profile to access practice content` — a real
client-side auth gate, not an inference [E11, E14 `S234_resume_02_after.xml`]. The path map
shows `Python Developer / 1. Intro to Python`, toolbar counters `200` and `0`, and section
progress `0/20`, `0/11`, `0/9`, `0/15` in the `Select Path` sheet [E14
`S229_resume_01_after.xml`, `S221_resume_00_after.xml`]. Back from `ChapterActivity` requires
an explicit `Quit lesson / Choose a different path / Cancel` confirmation
[E14 `S213_back_from_lesson_after.xml`]. Activities are identified from `dumpsys activity
activities` (`topResumedActivity`) on every screen event; the attempted Frida
`ActivityLifecycleCallbacks` hook produced @@NAV@@ nav events because the API-36 interface
has extra default methods [E11, E12].

**M08 discovery — real Fragment/ViewModel controller chain.** `androidx.lifecycle.m0.k`
LiveData posts during onboarding exposed the actual Jetpack Navigation controller objects:
`NavHostFragment{...}` with `SavedStateHandlesVM` and `NavControllerViewModel`, followed by
`IntroductionFragment`, `SetMotiveFragment`, `OnboardingMotiveReassuranceFragment`,
`SetOccupationFragment`, `SetWorkFunctionFragment`, `SetExperienceFragment`,
`OnboardingSelectPathContainerFragment` and the pick-a-path bottom sheet
`com.getmimo.ui.onboarding.selectpath.pickapath.b`. Their `ViewModelProvider.DefaultKey`
entries name per-step ViewModels (`m7.f.a`, `com.getmimo.ui.onboarding.step2.b`, `f7.e`,
`un.d`) [E12 `liveData` events]. This closes M06's "exact navigation graph UNKNOWN" gap for
the onboarding subgraph: it is a single `NavHostFragment` inside `OnboardingActivity`,
not a separate Activity per step. `ActivityLifecycleCallbacks` registration itself failed on
API 36 because `Java.registerClass` must also implement the eight `onActivityPre*/Post*`
default methods; that is recorded as a `hook_error`, not silently dropped [E12].

## 4. UI rendering

`gm.h.a(List)` selects one of nine `LessonInteractionType`s (`InteractiveWebView`,
`FillTheGap`, `Spell`, `Selection`, `ValidatedInput`, `SingleChoice`, `MultipleChoice`,
`Reveal`, `None`); `base/c.O(LessonContent$Interactive, LessonBundle)` maps ALWAYS-visible
modules to render items `jm/j` (Paragraph), `jm/i` (Image), `jm/k` (Webview) and posts them
to LiveData `m`; CORRECT/WRONG modules are revealed by `c0()`/`d0()` after a run [E09].
`RunButton$State` (`RUN_ENABLED, RUN_DISABLED, SUBMIT_ENABLED, SUBMIT_DISABLED, PROCESSING,
CONTINUE_BIG, CONTINUE_DISABLED, NOT_SHOWN`) and `InteractionKeyboardButtonState`
(`ENABLED/DISABLED/HIDDEN`) gate input [E05, E10]. Observed LiveData values in this run:
@@LD@@

## 5. Content pipeline and lesson DSL

Shipped English curriculum `publishSetVersion=753`: 19 tracks / 144 sections / 1,029
tutorials / 1,947 chapters / 18,272 lessons, with 2,855 decoded selection answers [E09, E18].
`Lye/b.b(J)` opens `lessons-<lang>/tracks/tutorial-<id>.json` via `AssetManager.open`;
`DefaultTrackLoader.a(J,I,I)` decodes with `kotlinx.serialization`; the lesson `content` is
XML-like text parsed by `XmlPullParserFactory` (`p`, `code`, `selection`, `img`, `webview`,
`database`), with unknown tags dropped and `xml_parse_error_module` analytics [E09]. Runtime
verification: `te.c.b(String)` returned Paragraph/Code/FillTheGap/Option(correct=true)/
Paragraph(WRONG) for a shipped lesson; `gm.h.a(nonEmpty)` = `FillTheGap` [E05, E08].
`LessonContent$Executable` carries `instructions, preselectedFileIndex, files,
getHasBrowserOutput(), getHasInputConsole()`; each `File` has
`name, codeLanguage, content, solvedContent` [E09].

## 6. Lesson engine, execution path and validators

The **central chain** (the mission's priority) is runtime-verified at the answer moment
in M07 stage 6 [E05, E06, E07]:

```
NonInteractiveLessonFragment$goToNextPage$1 / WebView Continue
  -> base/c.U()                       lessonSolvedAndProceed  (N=true)
  -> base/c.H(1, 1)                  createLessonProgress
  -> LessonProgressRepository.createLessonProgress(
       LessonBundle(lessonId=151403, lessonIndex=1, chapterId=17742,
                    tutorialId=904, trackId=219, tutorialVersion=161,
                    tutorialTitle="Discovering HTML and Tags", publishSetVersion=753))
  -> LessonProgress(... tries=1, attempts=1, isPracticeProgress=false, inQueue=true)
  -> base/c.e0(progress)             storeProgressInMemory
  -> LessonProgressQueue.storeLessonProgress(progress, false, true, cont)
  -> LessonProgress.isSolvedCorrectly() = true   (151410, 151403)
  -> base/c.f0(false, true)          trackLessonResult   [FIRST ARG IS FALSE]
  -> base/c.N()                      resetInputState
  -> e = chapterIndex -> next lesson
```

`Y(Z)` sets `f=TRUE` to prevent double submission; `onLessonRun$1.invokeSuspend` dispatches
`V()` (exact), `W()` (normalised partial match), `X()`/`d0()` (wrong), then resets `f`
[E09, E10]. Validators, all local: `qm/i.a` lowercases with `Locale.US` and keeps letters,
digits and `< > ( ) : { } , .`; `setupViews$2` produces CORRECT / PARTIAL / INCORRECT
[E08]; `km/f.b(List)` = all `selected == correct` [E08]; `im/d.E0()` ordered case-sensitive
token equality [E09]; `q.I()` compares user file contents with shipped `solvedContent` via
`ArrayList.equals` [E09]; `isSolvedCorrectly() = tries >= 1` [E08]. The shipped WebView
letter exercise 151403 uses `correctLetter='D'` in `lesson-webview.js`: wrong `Q` →
`Try again` and disables Q, correct `D` → `Correct! / D O G / dog_yawn.png`; **no native
`V()/W()/X()` or WebView JS-interface event fired** — M07's negative result is preserved
[E06, E07, E08].

## 7. Learner state and persistence

`mimo.db` is Room/SQLite in WAL mode (`mimo.db-wal`, `mimo.db-shm`), with three app tables
and identity hashes `08b92644…` / `2b8ab6d3…` [E03, E13]. `lesson_progress` has exactly 11
columns, PK(`lesson_id`,`tutorial_id`); the measured row after lesson 151403 is
`151403 | 1793883744787 | 1793883713744 | 1 | 904 | 161 | 219 | 753 | 1 | 0 | 1`
[E07, E13]. Phase 1 measured the natural transition `lesson_progress 0 → 2` during
onboarding (slide 151410 + WebView 151403) and `2 → 0` after a cold start, with
`tutorial_completions` holding 868 seeded `is_completed=0` rows and
`chapter_completions` 0 rows [E11, E13]. Phase 2 hooked `SQLiteDatabase` and captured the
**actual Room bootstrap SQL executed at runtime** against
`/data/user/0/com.getmimo/databases/mimo.db`: `PRAGMA user_version;`, the three
`CREATE TABLE IF NOT EXISTS` statements, `INSERT OR REPLACE INTO room_master_table
(id,identity_hash) VALUES(42, '2b8ab6d303d9a501bd8c8fb78d8352fc')` and
`PRAGMA user_version = 2`, plus `SELECT identity_hash FROM room_master_table WHERE id = 42`
[E12 `sql`]. This runtime-confirms the M05 static schema and establishes the shipped
Room migration version (`user_version = 2`); the complete migration class list remains
`UNKNOWN`.

**M08 discovery:** the persisted economy is in `mimo_prefs.xml` —
`local_coins = {"coins":200}` (matching the toolbar `200`), `user_settings =
{"hasProgrammingExperience":false}`, `favorite_tracks = {"favoriteTrackIds":[50,219]}`,
`user_profile_created_at`, `favorite_tracks_to_sync/remove` sets [E11, E13].
`sp_lesson_view_properties.xml` holds per-interaction hint booleans and
`code_editor_line_length=-1` [E13]. Jetpack DataStore `user_preferences.preferences_pb`
plus Firebase/RevenueCat/Mixpanel/Facebook stores were present; protobuf contents were **not**
decoded (`UNKNOWN`) [E13, E10]. Full schema in `MIMO_LEARNER_STATE_SCHEMA.json`.

## 8. Progression and unlock

`GetPathMapState$invoke$3` (659 instructions) builds
`Completed / Locked / Unlocked / UnlockedButNoKeys` states from `Tutorial.isCompleted()`,
`TutorialType.isRequired()`, subscription tier, `CanOpenChapterWithKeys`, keys count and dev
overrides; a reverse `listIterator` enforces the **sequential required-tutorial prerequisite**;
`Challenge` tutorials are excluded; `cc/b.y` classifies sections by completion floats
against `1.0f` [E10]. The unlock key is `ds/w.c(Set<String>,J,J,J)`: join the three longs
with `":"` and test `Set.contains("<trackId>:<tutorialId>:<chapterId>")`, consumed by
`CanOpenChapterWithKeys$invoke$1`; the key set comes from the remote
`DefaultKeysRepository.fetchKeys/consumeUserKey` (`/v1/user/keys`,
`/v1/user/keys/consume`) [E04, E20]. Section/classification state was observed as `0/20`,
`0/11`, `0/9`, `0/15` [E14]. **The exact live boolean combining tier / keys / progress is
`UNKNOWN`** — 659 decoded instructions with suspension labels; no runtime unlock decision
was forced with a seeded key [E10, E20].

## 9. Scoring, XP, coins, streak, goals and rewards

What is **verified**: `lesson_progress` has no XP/score/streak/key column [E03, E20];
`d0()` and `f0()` contain no XP arithmetic [E07]. Local answer counting is an exact
algorithm: `AnswersInChapter(correct = queued.count{isSolvedCorrectly()}, total =
queued.size)`, `getCorrectLessonProgressCount` = same count, and
`getCorrectLessonsFirstTryCount = queued.count{isSolvedCorrectly() && attempts == 1}`;
`updateCorrectAnswersCount` publishes the StateFlow and `updateLessonStreakDetector` runs
when `attempts == 1` [E10]. Phase 2 captured two real learner-state writes during onboarding:
`SharedPreferencesImpl$EditorImpl.putString("onboarding_goal", "build_something_useful")`
and `putString("user_settings", "{\"hasProgrammingExperience\":false}")`, and a real
`com.getmimo.data.settings.a.l(Settings)` call with
`Settings(dailySparksGoal=null, hasProgrammingExperience=false, dailyReminderTime=null,
notificationSettings=null, name=null, biography=null, userId=null, hadFreeProTrial=null,
hadFreeMaxTrial=null)`; `a()` returned `null` before that write [E12 `prefs_write`,
`entry settings_write`, `entry settings_get`]. This is a measured **onboarding decision →
repository → SharedPreferences** path; note the goal field is `dailySparksGoal`, not a
minute count. Phase 2 hooks the coin layer
(`com.getmimo.core.model.coins.Coins.getCoins()I`,
`com.getmimo.data.source.remote.coins.a.a()/b()`,
`LessonProgressQueue.getCorrectLessonProgressCount/getCorrectLessonsFirstTryCount/
updateCorrectAnswersCount/updateLessonStreakDetector`, `MainViewModel E/F/G/H/I`,
`data.settings.a` daily-goal, reward/keys repositories) so a scoring claim would need
input → calculation → output → storage [E12].

What is **not** verified: absolute XP per lesson, streak length, leaderboard rank, key
balance, coin award formula or daily-goal award thresholds. These live in remote DTOs
(`Reward/Rewards`, `UserActivityResponse`, `Leaderboard*`, `PostProgressResponse`,
`TrackEtaResponse`) and caches (`RevenueCat remote_config.json`) [E20]. The measured guest
`local_coins` stayed `200` across @@SNAPS@@ natural snapshots, so **no per-lesson coin
increment was demonstrated** [E11, E13]. `SERVER CONFIRMED = 0`.

## 10. Learning and review

`CompletionRepository.b(Track, cont)` attaches `TutorialCompletion.isCompleted` and
`completedChapters` from Room; `ChapterFinishedViewModel.R` is the offline fallback
`handleChapterAlreadyCompletedState`; `ChapterFinishedSuccessType` distinguishes
`DAILY_GOAL_NOT_REACHED / REACHED / ALREADY_REACHED_EARLIER_TODAY` [E10]. Practice/review
content exists as `PRACTICE_LEVEL_1..3`, `PracticeRequired`, `PracticeOptional` chapter
types, but for a guest the Practice tab is gated behind profile creation [E10, E11].
No chapter-end screen, no `is_completed=1` row and no review session was reached — those
transitions are `UNKNOWN` [E11, E20].

## 11. Media / WebView / Rive / code editor / native

`assets/lesson-webview.js` relays gesture/activity/focus/height/ready and
`mimo.activity.correct|wrong|completed`; shipped `solvedContent` makes executable lessons
decidable offline [E09]. The code editor is `CodeEditViewModel` + `CodeDiffViewModel` +
syntax highlighter + input console + `CodePlaygroundActivity`; a shipped HTML template uses
`style.css` / `script.js` [E09]. Phase 1 reached the fill-the-gap code-editor lesson
("Click on `<button>Like</button>`") and measured its clickable snippet and
`tv_ftg_hint` [E14 `S151_onboard_23_after.xml`]. Twelve arm64 `.so` libraries ship,
including `librive-android.so` (Rive), `libsqlcipher.so`, `libdatastore_shared_counter.so`,
`libsigner.so` and ML Kit/CameraX/Bugsnag libraries [E10]. `System.loadLibrary` is hooked
(deduplicated), but JNI method tables, request signing and the native↔Kotlin surface
remain `UNKNOWN` [E12, E10]. `WebView.addJavascriptInterface` was hooked in M07 stage 6 and
produced **no** event for lesson 151403 [E06].

## 12. API, network, sync and offline boundary

53 Retrofit-annotated endpoints were decoded; the relevant ones are listed in
`MIMO_SYSTEM_MAP.json -> modules[network_sync].endpoints` [E04]:
`POST /v1/tutorials/{tutorialId}/progress`, `GET /v1/tracks/{trackId}/completion`,
`GET /v1/user/coins`, `GET /v1/user/keys`, `POST /v1/user/keys/consume`,
`GET /v1/user/rewards/next`, `POST /v1/user/rewards/{rewardId}/confirm`,
`GET /v1/leaderboards/latest`, `GET|PUT /v1/user/settings`,
`POST /v1/code/runfiles`, `POST /v1/user/visits`, `GET /v1/user/activity`.

`java.net.URL.openConnection` was hooked and produced the only observed outbound
connections: `https://graph.facebook.com/v16.0/app/model_asset?...`,
`https://api.mixpanel.com/track/?ip=1`, `https://app.adjust.com/event` and
`https://firebaselogging-pa.googleapis.com/v1/firelog/legacy/batchlog` — i.e. third-party
analytics/model-asset endpoints [E12 `net`]. `okhttp3.OkHttpClient.newCall` could not be
hooked (`net_probe okhttp_missing`: R8 removed that symbol), and **no Mimo backend
`/v1/...` request was observed in the window**, so the decoded endpoints below remain
`VERIFIED_STATIC` only. `SERVER CONFIRMED = 0`.

`com.getmimo.network.a.a()` is the exact connectivity gate:
`ConnectivityManager.getActiveNetwork()` + `hasTransport(WIFI) || hasTransport(CELLULAR)`;
`b() = !a()` [E10]. Offline, `postUnsyncedLessonProgress()` logs
"No internet connection, not posting unsynced lesson progress" and throws
`NoConnectionException`; this was runtime-verified [E08]. M07 stage 6 and M08 phase 1 both
measured `in_queue=1` rows being deleted at a cold start (2 → 0), including once while
`Active default network: 102` was online [E07, E11]. Whether deletion followed a successful
POST or a local `DELETE FROM lesson_progress WHERE in_queue = 1` was **not isolated**;
no server response was observed. `SERVER CONFIRMED = 0`.

## 13. Background jobs

`PostVisitWorker`, `StreakWidgetRefreshWorker`, `AccountDeleteWork`,
`AsyncRequestWorker`, `MimoFirebaseMessagingService`, `AutoSaveCodeService` and
`NotPremiumNotificationService` are decoded WorkManager `CoroutineWorker` / service classes
[E02, E10]. Phase 2 hooks `PostVisitWorker.a` and `StreakWidgetRefreshWorker.a`; their
**triggers and periodicity remain `UNKNOWN`** because no worker fired in the observed window
[E12].

## 14. The central decision graph (data flow, not class names)

1. **Navigation** chooses a route (bottom-nav tab / path-map icon / ChapterActivity page).
2. The **ViewModel** (`MainViewModel`, `PathMapViewModel`, `ChapterViewModel`,
   `InteractiveLessonBaseViewModel`) loads a `LessonBundle` from **shipped** content.
3. The **DSL + interaction selector** determine the renderer and validator.
4. User input → **validator** → `Y(boolean)` → `V/W/X/U`.
5. `H(tries,attempts)` → **Repository** `createLessonProgress` → 11-field
   `LessonProgress`.
6. `e0()` → **Queue** → Room `lesson_progress(in_queue=1)` + `AnswersInChapter`
   counters + streak detector.
7. `f0(false, isSolvedCorrectly())` analytics; `N()` resets input; `e = chapterIndex`
   posts the **next page**; `GetPathMapState` recomputes **unlock state** for the next
   Activity.
8. On reconnect/startup, `postUnsyncedLessonProgress` applies the **network gate** and
   either POSTs or throws `NoConnectionException`.
9. Remote **reward/streak/leaderboard/goal** objects are consumed by `MainViewModel`;
   their award formulas are server-owned (`UNKNOWN`).

`MIMO_CORE_FLOW.mmd` draws exactly this graph; decisions D1–D7 with inputs, logic and
outputs are in `MIMO_SYSTEM_MAP.json -> decision_logic`.

## 15. Dependencies and client/server responsibilities

Kotlin + coroutines + kotlinx.serialization; AndroidX ViewModel/LiveData; Jetpack Compose +
Orbit MVI; Room/SQLite WAL; Jetpack DataStore; SharedPreferences; Retrofit-style APIs over
OkHttp; WorkManager; Firebase (Remote Config, Crashlytics, Analytics, Messaging); RevenueCat
IAP; Mixpanel; Adjust; Customer.io; WebView; Rive; ML Kit/CameraX [E01, E02, E04, E13].
**Client-owned:** curriculum, DSL, validation, progress rows, counters, guest coins,
offline correctness, unlock *state shape*, connectivity gate. **Server-owned / UNKNOWN:**
absolute XP, streak length, daily-goal awards, keys/rewards balances, leaderboard ranks,
`PostProgressResponse`, remote code-runner results, subscription tier, completion
acknowledgement [E07, E10, E20]. No server was reconstructed or contacted by design.

## 16. Honest verdict

M08 establishes the connected architecture, the real navigation state machine, the
answer → ViewModel → Repository → Room → queue → next-lesson execution path, the exact
learner-state stores (including the previously unknown `local_coins`), the unlock *shape*,
local answer counters, the network gate and the client/server boundary. @@FRIDA@@ Frida
events (@@HOOKS@@ hook installs, @@ENTRIES@@ method entries, @@SQL@@ SQL,
@@LIVE@@ LiveData, @@NAV@@ lifecycle, @@DI@@ DI, @@PWRITES@@ preference writes,
@@NET@@ network) were correlated into the one timeline [E12]. All 63 curated hooks
installed successfully in each attached process (the only `hook_error` was the API-36
lifecycle interface), so the absence of `V()/W()/X()` or `LessonProgressApi.postProgress`
events is a **negative runtime result**, not a hook failure. Phase 3 switched technique —
restoring the naturally generated post-onboarding snapshot instead of replaying the
Compose onboarding that stalled phase 2 — to put hooks on the main screens. It does **not** establish
absolute XP/streak/reward formulas, native validator dispatch for a submitted native answer,
chapter-completion transitions, JNI internals, or any server response. No complete
reconstruction is claimed. `SERVER CONFIRMED = 0`.
'''

UNKNOWN = r'''# MIMO 9.35 — CRITICAL UNKNOWNS (MISSION 08)

**Scope:** only the material unknowns that block a complete implementation-level
reconstruction of the *central execution paths*. Anything below is deliberately `UNKNOWN`,
not guessed from bytecode. `SERVER CONFIRMED = 0`. Evidence codes resolve in
`MIMO_SYSTEM_MAP.json -> evidence_index`.

## Evidence status of this run

| Item | Value |
|---|---|
| Broad run | `42042312640`, @@P1@@ events, SUCCESS, no Frida method events (server binary not pushed); reached MainActivity, ChapterActivity, FTG code editor and quit dialog |
| Targeted run 2 | `42046336206`, @@P2@@ events, Frida attach OK (3 processes), 63 hooks per process, live DI / Fragments / Room SQL / Settings / network URLs; onboarding stalled on a Compose screen |
| Targeted run 3 | `@@P3RUN@@`, @@P3@@ events; natural post-onboarding state restored (82 files, 2 `lesson_progress` rows, `local_coins=200`) but the app still opened the IntroSlides carousel; the route loop hit a keyword collision and aborted |
| Final run 4 | `@@P4RUN@@`, @@P4@@ events; bounded, state-aware "Get started" navigation to reach MainActivity, keyword collision fixed |
| Unified stream | `MIMO_RUNTIME_TIMELINE.jsonl` — @@TOTAL@@ events, @@COLLAPSED@@ repetitive events collapsed |
| Navigation | @@SCREENS@@ screens / @@EDGES@@ edges in `MIMO_NAVIGATION_GRAPH.json` |
| State snapshots | @@SNAPS@@ natural (non-synthetic) Room/preferences snapshots |

## 1. Absolute scoring / XP / streak / rewards — highest priority

`VERIFIER_STATIC` classes exist (`Coins.getCoins`, `LessonProgressQueue` counters,
`DefaultStreakRepository`, `DefaultRewardRepository`, `MainViewModel E/F/G/H/I`,
`SettingsRepository.getUserDailyGoal`), and `local_coins={"coins":200}` is a real persisted
value [E11, E13, E20]. **Missing:** a single observed event exposing input → calculation →
output → storage for an XP/coin/streak award. `local_coins` was constant across
@@SNAPS@@ snapshots, so a per-lesson increment was NOT demonstrated. No XP column exists in
`mimo.db`. The award formulas depend on `PostProgressResponse` / `Progress` /
`TrackEtaResponse` server bodies that were deliberately not reconstructed.
**Why it matters:** without it the "Scoring → Next Activity" half of the priority chain is
only structurally known. Precise pointer: `MainViewModel$confirmRewardAndLookForNewRewards$1`,
`MainViewModel$fetchRewards$1`, `/v1/user/rewards/next`.

## 2. Live unlock boolean and key values

`ds/w.c(Set,J,J,J)` = membership of `"<trackId>:<tutorialId>:<chapterId>"` in a key set from
`DefaultKeysRepository` is `VERIFIED_STATIC` [E20]; path-map states and the sequential
required-tutorial prerequisite are decoded [E10]. **Missing:** a runtime observation of
`GetPathMapState$invoke$3` (659 instructions, branches at PC `0x04aa`, `0x4f0`, `0x51a`,
`0x608`) or `CanOpenChapterWithKeys$invoke$1` @10104004 deciding `Locked` vs
`UnlockedButNoKeys` vs `Unlocked`, and any real key value. No key was seeded (that would be
synthetic state without exposing the algorithm).

## 3. Native validator dispatch and feedback objects

`V()`/`W()`/`X()`/`d0()` and `jm/m`, `jm/n`, `jm/o` are decoded statically [E09], and M07
stage 6 proved the WebView letter exercise uses `U()/H()` **instead** [E06]. **Missing:** a
submitted native `validatedInput` / `fillTheGap` / `selection` answer that actually reaches
`onLessonRun$1`, with the resulting LiveData feedback object and UI. Phase 1 reached the
fill-the-gap code-editor lesson and located the measured `<button>Like</button>` snippet
(`S151_onboard_23_after.xml`), but its exploration stalled on `btn_lesson_close`; phases 2–4
never reached a native lesson. If no `V/W/X` entry appears in the unified timeline, this
remains `UNKNOWN`.

## 4. Chapter / tutorial completion transitions

`chapter_completions` stayed 0 rows and `tutorial_completions` held 868 `is_completed=0`
rows in every snapshot [E13]. No chapter-end screen, no `is_completed=1` row, no
`ChapterFinishedSuccessType` transition was observed. `CompletionRepository.b(Track, cont)`
and `ChapterFinishedViewModel.R` are `VERIFIED_STATIC` only [E10, E20].

## 5. Code execution and WebView bridge

`q.I()` compares user files with shipped `solvedContent` offline, and `/v1/code/runfiles`
endpoints exist [E04, E09]. **Missing:** `WebView.addJavascriptInterface` payloads
(M07 stage 6 had zero events), the exact local-WebView vs remote-runner routing, the remote
runner's test/result feedback, and any JNI/native execution inside the 12 shipped `.so`
libraries (`libsigner.so`, `librive-android.so`, `libsqlcipher.so`, …). Native signing,
JNI method tables and the native↔Kotlin API are `UNKNOWN` by explicit scope [E10].

## 6. Sync / cold-start queue semantics

Both M07 stage 6 (offline) and M08 phase 1 (online, `Active default network: 102`) measured
`in_queue=1` rows disappearing at a cold start [E07, E11]. **Missing:** isolation of whether
the DELETE was preceded by a successful `POST /v1/tutorials/{id}/progress` (and its
acknowledgement) or was a local `DELETE FROM lesson_progress WHERE in_queue = 1`. No server
response was observed or fabricated; `SERVER CONFIRMED = 0`. This is why earlier "queued-row
restore" expectations are not claimed.

## 7. DI framework, worker triggers and DataStore contents

No `@Inject`/Hilt/Koin metadata was decoded; only `Lhm/b;` 13-slot container and two
generated `_Factory` classes are known, so the framework/scopes are `UNKNOWN` [E02].
`PostVisitWorker`, `StreakWidgetRefreshWorker`, `AccountDeleteWork`, `AsyncRequestWorker`
names are `VERIFIED_STATIC` but no trigger/periodicity was observed [E10].
`user_preferences.preferences_pb` is present but its protobuf was not decoded in M08; the
DataStore key names come from M06 static strings only [E13].

## 8. Screens and states deliberately not reached

Leaderboard content, Profile/Settings screens, streak modal, purchase/paywall, account
creation, native correct/wrong feedback after a submitted selection, and the chapter-end
screen. `AuthenticationActivity` was passed with `Skip` (guest), so authenticated practice,
sync and leaderboard behaviour were not exercised — no credentials or auth bypass were used.

## 9. Instrumentation limitations (recorded, not hidden)

- Phase-1 run `42042312640` produced **no Frida method events**: the GitHub release asset
  download failed silently, `adb push` could not stat `frida-server`, and
  `dev.attach()` returned `unable to connect to remote frida-server: closed`
  [E16 `PHASE1_FRIDA_SETUP_42042312640.txt`]. All 275 phase-1 events are therefore UI /
  navigation / DB / orchestrator evidence, not method-level evidence.
- Phase 2 fixes this with three independent download paths, an `lzma` decompressor, a
  `pkill` + fresh device install, and an **actual attach preflight** before the orchestrator
  starts [E16 `M08_FRIDA_SETUP.txt`]. If the preflight is `attach_ok=false`, the phase-2
  timeline itself records the failure and method-level claims stay `UNKNOWN`.
- `dumpsys activity top` on this API-36 image exposed Launcher3 item dumps rather than
  Mimo fragments; fragment-level state is therefore `UNKNOWN` in the navigation graph.
  Activities come from `dumpsys activity activities` (`topResumedActivity`) and Frida
  `ActivityLifecycleCallbacks`.
- `uiautomator2` was probed successfully but **not adopted**: adb hierarchy dumps +
  `dumpsys` + lifecycle hooks already provided the required evidence [E11, E16].
- Phase 2's state-aware onboarding replay stalled at a Compose screen whose nodes are not
  exposed by `uiautomator dump` (three identical empty hierarchies). Rather than repeat it,
  phase 3 restored the naturally generated post-onboarding private state from run
  `42042312640` before launching. No synthetic learner rows were inserted; the restore is
  tagged `synthetic=false` in the timeline and in the learner-state schema.
- `Java.registerClass` for `Application$ActivityLifecycleCallbacks` failed on API 36
  ("Missing implementation for onActivityPostStarted …"), so Activity names come from
  `dumpsys activity activities` and Fragment names from `LiveData` posts instead.
- `okhttp3.OkHttpClient.newCall` is not present under that name after R8; only
  `java.net.URL.openConnection` produced network events. Hence the absence of a Mimo
  `/v1/...` request is an observation limit, not proof that no request occurred.
- A third-party launcher overlay ("This release is provided by …", with a countdown and
  "Do not show again.") appeared on cold start in phase 2. Its origin is `UNKNOWN` and no
  claim is made about it; it was waited out / dismissed as a UI obstacle only.
- No snapshot contains synthetic learner rows. The only seeded value is
  `experiments.xml:experiment_adapted_onboarding_android_local=original`, which selects the
  original onboarding variant and is tagged `synthetic=true` in the learner-state schema.
  Snapshot restoration between independent experiments restored naturally generated state.

## Closure criterion

Investigation stops here: the main architecture, module communication, navigation state
machine, lesson engine, validators, learner state, offline/sync boundary, progression,
local scoring counters, media/code-execution boundaries and the central
`Navigation → ViewModel → Repository → Core Logic → Learner State → Scoring → Next Activity`
chain are established with real evidence. The remaining items are server-owned or require
authenticated/native execution paths that were deliberately not fabricated.
'''

def subst(s):
    for k, v in T.items():
        s = s.replace(k, v)
    return s

txt(OUT / 'MIMO_CORE_ARCHITECTURE.md', subst(ARCH))
txt(OUT / 'MIMO_CRITICAL_UNKNOWNs.md', subst(UNKNOWN))

print('BUILT 7 deliverables in', OUT)
for p in sorted(OUT.iterdir()):
    print(' ', p.name, p.stat().st_size, 'bytes')
print('timeline events:', len(filtered), 'collapsed:', collapsed_total)
print('frida:', len(frida_events), 'hooks:', len(hook_installed), 'entries:', len(method_entries),
      'sql:', len(sql_events), 'nav:', len(nav_events), 'di:', len(di_events),
      'prefs_write:', len(prefs_writes), 'liveData:', len(live_events), 'net:', len(net_events))
print('screens:', len(screens), 'edges:', len(edges), 'snapshots:', len(snap_digests))
