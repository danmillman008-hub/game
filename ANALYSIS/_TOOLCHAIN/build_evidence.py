"""Build EVIDENCE_INDEX.json and SUBSYSTEM_EVIDENCE.json from verified artifacts.

All evidence is read from already-produced artifacts / the read-only APK.
Writes two JSON files under ANALYSIS/. Script lives in ANALYSIS/_TOOLCHAIN.
"""

import os
import re
import sys
import json
import glob
import hashlib
import collections

ROOT = '/home/user/game'
A = os.path.join(ROOT, 'ANALYSIS')
sys.path.insert(0, os.path.join(A, '_TOOLCHAIN'))
from dexlib import Dex  # noqa: E402

STATUS = {
    'OBSERVED': 'directly present in the original APK/DEX/resources or in Ghidra-disassembled instructions',
    'STATICALLY INFERRED': 'derived from multiple static references; not runtime verified',
    'RUNTIME VERIFIED': 'observed on an approved emulator/ADB session (none available in this session)',
    'SERVER CONFIRMED': 'response body observed in an authorized test environment (none available in this session)',
    'UNKNOWN': 'evidence insufficient',
}
CONFIDENCE = {
    'HIGH': 'directly supported by executable instructions, DEX structures or resource bytes',
    'MEDIUM': 'supported by multiple independent static references, not runtime verified',
    'LOW': 'based on incomplete metadata or indirect inference',
    'UNKNOWN': 'evidence insufficient',
}

INV = json.load(open(os.path.join(A, 'APK_COMPLETE_INVENTORY.json')))
GRAPH = json.load(open(os.path.join(A, 'COMPONENT_GRAPH.json')))
METRICS = json.load(open(os.path.join(A, 'COVERAGE_METRICS.json')))
ENDPOINTS = json.load(open(os.path.join(A, 'MIMO_RETROFIT_ENDPOINTS.json')))['endpoints']
CF = open(os.path.join(A, 'GHIDRA/CONTROL_FLOW.txt'), errors='replace').read()
CORO = json.load(open(os.path.join(A, 'COROUTINE_STATE_MACHINES.json')))

DEXX = {}
for p in sorted(glob.glob(os.path.join(A, '_INPUT/classes*.dex'))):
    d = Dex(open(p, 'rb').read(), os.path.basename(p))
    DEXX[d.name] = d

ALL_STRINGS = [(d.name, st) for d in DEXX.values() for st in d.strings]


def find_string(substr):
    hits = []
    for name, st in ALL_STRINGS:
        if substr in st['value']:
            hits.append({'dex': name, 'string_index': st['index'],
                         'string_id_off': st['id_off'], 'string_data_off': st['data_off'],
                         'value': st['value'][:220]})
            if len(hits) >= 3:
                break
    return hits


def parse_funcs(text):
    out = []
    prog = None
    for line in text.splitlines():
        m = re.match(r'^=== PROGRAM (\S+) language=\S+ functions=(\d+) symbols=(\d+)', line)
        if m:
            prog = m.group(1)
        m = re.match(r'^FUNC \[(PATH_MAP|SCORING)\] (.+?) @([0-9a-fA-F]+) body_bytes=(\d+)', line)
        if m:
            out.append({'dex': prog, 'kind': m.group(1), 'name': m.group(2),
                        'address': m.group(3), 'body_bytes': int(m.group(4))})
    return out


FUNCS = parse_funcs(CF)

E = []


def add(claim, status, confidence, verification, tool, excerpt, **kw):
    e = {
        'id': 'EV-%04d' % (len(E) + 1),
        'claim': claim,
        'status': status,
        'confidence': confidence,
        'verification_status': verification,
        'tool_and_method': tool,
        'evidence_excerpt': excerpt if isinstance(excerpt, str) else json.dumps(excerpt, ensure_ascii=False)[:600],
    }
    for k in ('dex', 'class_descriptor', 'method_or_signature', 'address_or_offset', 'source_document'):
        if k in kw:
            e[k] = kw[k]
    E.append(e)
    return e['id']


TOOL_DEX = 'dexlib.py (read-only DEX header/map/class_data parser)'
TOOL_GHIDRA = 'Ghidra 12.2 analyzeHeadless with Auto Analysis (no -noanalysis)'
TOOL_SMALI = 'apktool 2.9.3 / smali 3.x disassembler output'
TOOL_JADX = 'JADX 1.5.6 / 1.1.0 decompiled Java of the original APK'
TOOL_AXML = 'androguard 4.1.4 AXMLPrinter / ARSCParser (already installed; no new tool)'
TOOL_ZIP = 'Python zipfile, read-only, original APK'

# ---- 1. integrity & APK-level facts ----------------------------------------
add('Original APK SHA-256 matches the previously established original',
    'OBSERVED', 'HIGH', 'verified by recomputation', TOOL_ZIP,
    'sha256=' + INV['apk']['sha256'] + ' expected=' + INV['apk']['sha256_expected'],
    address_or_offset='whole file', source_document='APK_COMPLETE_INVENTORY.json')
add('APK contains 14,398 zip members and exactly 12 DEX files',
    'OBSERVED', 'HIGH', 'verified by enumeration', TOOL_ZIP,
    'zip_members=%d; dex members=%d' % (INV['apk']['zip_members'], len(INV['dex'])),
    source_document='APK_COMPLETE_INVENTORY.json')
add('All 12 DEX adler32 checksums and SHA-1 header signatures are valid',
    'OBSERVED', 'HIGH', 'verified by recomputation', TOOL_DEX,
    'all_dex_adler32_valid=%s all_dex_sha1_signature_valid=%s dex_parse_errors=%d' % (
        INV['integrity']['all_dex_adler32_valid'], INV['integrity']['all_dex_sha1_signature_valid'],
        INV['integrity']['dex_parse_errors']),
    source_document='APK_COMPLETE_INVENTORY.json')
add('ANALYSIS/_INPUT DEX evidence copies are byte-identical to APK members',
    'OBSERVED', 'HIGH', 'verified byte-for-byte', TOOL_ZIP,
    str(INV['integrity']['all_dex_input_copies_match_apk']),
    source_document='APK_COMPLETE_INVENTORY.json')

# ---- 2. per-DEX structural + Ghidra reconciliation -------------------------
for r in INV['ghidra_reconciliation']['per_dex']:
    dex = r['dex']
    add('%s: class_defs=%d code_items=%d defined_methods=%d (without_code=%d)' % (
        dex, r['class_defs'], r['dex_code_items'], r['dex_defined_methods'], r['dex_methods_without_code']),
        'OBSERVED', 'HIGH', 'verified by independent DEX parse', TOOL_DEX,
        'map_list code_item=%d; class_data defined methods=%d' % (
            r['dex_code_items'], r['dex_defined_methods']),
        dex=dex, address_or_offset='header@0x0, map_list@0x%x' % INV['dex'][dex]['header']['map_off'],
        source_document='APK_COMPLETE_INVENTORY.json')
    add('%s: Ghidra Auto Analysis produced %d functions == %d DEX code_items' % (
        dex, r['ghidra_auto_analysis_functions'], r['dex_code_items']),
        'OBSERVED', 'HIGH', 'independent reconciliation, exact match', TOOL_GHIDRA,
        '=== PROGRAM %s ... functions=%d symbols=%d' % (dex, r['ghidra_auto_analysis_functions'],
                                                        r['ghidra_auto_analysis_symbols']),
        dex=dex, source_document='GHIDRA/CONTROL_FLOW.txt')

add('Total Ghidra functions 122,546 reconciles exactly to 122,546 DEX code_items / methods_with_code',
    'OBSERVED', 'HIGH', 'independent reconciliation, exact match', TOOL_GHIDRA,
    'functions_total=%d code_items_total=%d per_dex_all_match=%s' % (
        INV['ghidra_reconciliation']['functions_total'],
        METRICS['denominators']['methods_with_code'],
        INV['ghidra_reconciliation']['functions_exact_match_all_dex']),
    source_document='COVERAGE_METRICS.json')
probe = INV['ghidra_reconciliation']['symbol_composition_probe']
add('Total Ghidra symbols 1,284,542 verified arithmetically from 12 program headings; composition UNKNOWN',
    'OBSERVED', 'HIGH', 'arithmetic verified; composition not derivable', TOOL_GHIDRA,
    'sum=%d reported=%d dex_structural_id_baseline=%d residual=%d status=%s' % (
        probe['ghidra_symbol_total_independently_summed'], probe['ghidra_symbol_total_reported'],
        probe['dex_structural_id_baseline'], probe['residual_generated_labels'], probe['status']),
    source_document='APK_COMPLETE_INVENTORY.json')
add('Composition of the 1,284,542 Ghidra symbols cannot be derived from DEX header counts',
    'UNKNOWN', 'UNKNOWN', 'not established', TOOL_GHIDRA,
    'Ghidra creates string_data::, EXTERNAL.dex-N::, class/method/data labels beyond DEX structures',
    source_document='APK_COMPLETE_INVENTORY.json')

# ---- 3. manifest / resources / native / assets ------------------------------
m = INV['manifest']
add('Application class is %s; package=%s versionName=%s versionCode=%s' % (
    m['application']['name'], m['package'], m['versionName'], m['versionCode']),
    'OBSERVED', 'HIGH', 'read from binary AndroidManifest.xml', TOOL_AXML,
    '<manifest package="%s" ...><application android:name="%s">' % (m['package'], m['application']['name']),
    class_descriptor='Lcom/getmimo/App;', source_document='APK_COMPLETE_INVENTORY.json')
for comp in ('activity', 'activity-alias', 'service', 'receiver', 'provider'):
    items = m['components'][comp]
    add('Manifest declares %d %s entries' % (len(items), comp),
        'OBSERVED', 'HIGH', 'read from binary AndroidManifest.xml', TOOL_AXML,
        '; '.join(x['name'] for x in items[:12]) + (' ...' if len(items) > 12 else ''),
        source_document='APK_COMPLETE_INVENTORY.json')
add('Manifest declares %d uses-permission entries' % len(m['uses_permissions']),
    'OBSERVED', 'HIGH', 'read from binary AndroidManifest.xml', TOOL_AXML,
    ', '.join(m['uses_permissions'][:12]), source_document='APK_COMPLETE_INVENTORY.json')
add('Deep-link intent filters exist on SplashActivity and MainActivity (https and mimo schemes)',
    'OBSERVED', 'HIGH', 'read from binary AndroidManifest.xml', TOOL_AXML,
    json.dumps(GRAPH['navigation']['manifest_deep_links'][:3], ensure_ascii=False)[:500],
    source_document='APK_COMPLETE_INVENTORY.json / COMPONENT_GRAPH.json')
add('resources.arsc: %d package(s), %d resource entries across all locales' % (
    len(INV['resources']['packages']), INV['resources']['total_resource_entries']),
    'OBSERVED', 'HIGH', 'parsed from resources.arsc', TOOL_AXML,
    json.dumps(INV['resources']['packages'][0]['default_locale_types'], ensure_ascii=False)[:400],
    source_document='APK_COMPLETE_INVENTORY.json')
add('%d native .so libraries across ABIs %s' % (
    len(INV['native_libraries']), INV['native_library_abis']),
    'OBSERVED', 'HIGH', 'zip enumeration', TOOL_ZIP,
    ', '.join(x['path'] for x in INV['native_libraries'][:6]),
    source_document='APK_COMPLETE_INVENTORY.json')
add('%d assets, %d JSON bundles, locales %s' % (
    INV['assets']['count'], INV['assets']['json_files'], INV['assets']['locale_bundles']),
    'OBSERVED', 'HIGH', 'zip enumeration', TOOL_ZIP,
    'assets/lessons-en/tracks/tracks.json publishSetVersion=753',
    source_document='APK_COMPLETE_INVENTORY.json / MIMO_CONTENT_SCHEMA.json')
add('R8 build marker r8-map-id present on 25,867 class_defs; mapping file not shipped',
    'OBSERVED', 'HIGH', 'read from class_def source_file_idx', TOOL_DEX,
    json.dumps(INV['r8_build_markers'], ensure_ascii=False)[:300],
    source_document='APK_COMPLETE_INVENTORY.json')
add('Full R8 de-obfuscation mapping for short-named classes is unavailable',
    'UNKNOWN', 'UNKNOWN', 'not established', TOOL_DEX,
    'Only 491 obfuscated class -> DebugMetadata logical-name mappings recovered',
    source_document='COMPONENT_GRAPH.json')

# ---- 4. Ghidra target function instruction evidence ------------------------
for f in FUNCS:
    add('Ghidra disassembled %s function %s (%d bytes body)' % (
        f['kind'], f['name'], f['body_bytes']),
        'OBSERVED', 'HIGH', 'instruction-level evidence exists; full semantics not reconstructed',
        TOOL_GHIDRA,
        'FUNC [%s] %s @%s' % (f['kind'], f['name'], f['address']),
        dex=f['dex'], class_descriptor=f['name'].split('::')[0] if '::' in f['name'] else None,
        method_or_signature=f['name'], address_or_offset=f['address'],
        source_document='GHIDRA/CONTROL_FLOW.txt')

# ---- 5. DEX string constants with offsets ---------------------------------
CURATED = [
    ('LessonProgress rewardMultiplier field name', ', rewardMultiplier=', 'STATICALLY INFERRED', 'MEDIUM'),
    ('LessonProgress rewardedSparksForCorrectAnswer field name', ', rewardedSparksForCorrectAnswer=', 'STATICALLY INFERRED', 'MEDIUM'),
    ('LessonProgress correctLessonsFirstTry field name', ', correctLessonsFirstTry=', 'STATICALLY INFERRED', 'MEDIUM'),
    ('Room chapter_completions CREATE TABLE', 'CREATE TABLE IF NOT EXISTS `chapter_completions`', 'OBSERVED', 'HIGH'),
    ('Room tutorial_completions CREATE TABLE', 'CREATE TABLE IF NOT EXISTS `tutorial_completions`', 'OBSERVED', 'HIGH'),
    ('Room lesson_progress SELECT', 'SELECT * FROM lesson_progress', 'OBSERVED', 'HIGH'),
    ('Room database name mimo.db', 'mimo.db', 'OBSERVED', 'HIGH'),
    ('Track completion endpoint', '/v1/tracks/{trackId}/completion', 'OBSERVED', 'HIGH'),
    ('Last interacted track endpoint', '/v1/tracks/completion/lastInteracted', 'OBSERVED', 'HIGH'),
    ('Tutorial progress endpoint', '/v1/tutorials/{tutorialId}/progress', 'OBSERVED', 'HIGH'),
    ('Reward confirmation endpoint', '/v1/user/rewards/{rewardId}/confirm', 'OBSERVED', 'HIGH'),
    ('Next reward endpoint', '/v1/user/rewards/next', 'OBSERVED', 'HIGH'),
    ('ChapterFinishedViewModel source file', 'ChapterFinishedViewModel.kt', 'OBSERVED', 'HIGH'),
    ('GetChapterEndSuccessState source file', 'GetChapterEndSuccessState.kt', 'OBSERVED', 'HIGH'),
    ('PathMapViewModel source file', 'PathMapViewModel.kt', 'OBSERVED', 'HIGH'),
    ('PathMapScreen source file', 'PathMapScreen.kt', 'OBSERVED', 'HIGH'),
    ('LessonProgressQueue source file', 'LessonProgressQueue.kt', 'OBSERVED', 'HIGH'),
    ('ChapterFinishedStats data class', 'ChapterFinishedStats(earnedSparks=', 'STATICALLY INFERRED', 'MEDIUM'),
    ('BoxAnimationState earnedCoins', 'BoxAnimationState(earnedCoins=', 'STATICALLY INFERRED', 'MEDIUM'),
    ('Scroll X position field', ' scrollPositionX=', 'STATICALLY INFERRED', 'MEDIUM'),
    ('Scroll Y position field', '} scrollPositionY=', 'STATICALLY INFERRED', 'MEDIUM'),
    ('Chapter index in section field', ', chapterIndexInSection=', 'STATICALLY INFERRED', 'MEDIUM'),
    ('Column count field', ', columnCount=', 'STATICALLY INFERRED', 'MEDIUM'),
    ('Vertical ellipse radius field', ', verticalEllipseRadius=', 'STATICALLY INFERRED', 'MEDIUM'),
    ('Daily goal reached field', ', hasReachedDailyGoal=', 'STATICALLY INFERRED', 'MEDIUM'),
    ('Estimated completion ETA field', ', estimatedCompletionAt=', 'STATICALLY INFERRED', 'MEDIUM'),
]
for label, needle, status, conf in CURATED:
    hits = find_string(needle)
    if hits:
        h = hits[0]
        add(label, status, conf, 'DEX string constant located; field-to-class attribution requires xrefs',
            TOOL_DEX, h['value'], dex=h['dex'],
            address_or_offset='string_id[0x%x]=0x%x, string_data@0x%x' % (
                h['string_id_off'], h['string_id_off'], h['string_data_off']),
            source_document='APK_COMPLETE_INVENTORY.json')
    else:
        add(label + ' — NOT FOUND', 'UNKNOWN', 'UNKNOWN', 'not established',
            TOOL_DEX, 'no DEX string contains: ' + needle)

# ---- 6. SQL, endpoints, dependency graph ----------------------------------
for s in INV['database']['sql_statements'][:40]:
    add('Room/SQLite statement present in DEX strings', 'OBSERVED', 'HIGH',
        'string constant; execution not runtime verified', TOOL_DEX, s[:260],
        source_document='APK_COMPLETE_INVENTORY.json')
for ep in ENDPOINTS:
    add('Retrofit endpoint %s — annotation class %s; HTTP verb UNKNOWN (method-name inference rejected; tentative label %s)' % (
        ep['path'], ep['annotation'], ep['verb_inferred']),
        'STATICALLY INFERRED', 'LOW', 'HTTP verb NOT established; annotation-to-verb mapping is a tentative label only',
        TOOL_JADX, ep['annotations'][0] if ep['annotations'] else ep['path'],
        class_descriptor=ep['source_file'], method_or_signature=ep['signature'],
        source_document='MIMO_RETROFIT_ENDPOINTS.json')

add('Component catalog: %d com.getmimo class_defs classified into layers %s' % (
    GRAPH['totals']['mimo_class_defs_catalogued'], GRAPH['layer_counts']),
    'STATICALLY INFERRED', 'MEDIUM', 'path-based classification, not runtime verified',
    TOOL_DEX + ' + ' + TOOL_SMALI, json.dumps(GRAPH['layer_counts'], ensure_ascii=False),
    source_document='COMPONENT_GRAPH.json')
add('%d structural dependency edges and %d Smali invoke/new-instance/field edges observed' % (
    GRAPH['totals']['structural_edges'], GRAPH['totals']['smali_edges']),
    'OBSERVED', 'HIGH', 'references observed; semantics inferred',
    TOOL_DEX + ' + ' + TOOL_SMALI,
    json.dumps(GRAPH['layer_pair_edges_smali'][:4], ensure_ascii=False)[:400],
    source_document='COMPONENT_GRAPH.json')
for pair in ('ui -> viewmodel', 'viewmodel -> usecase_interactor',
             'usecase_interactor -> repository_remote', 'usecase_interactor -> repository_local',
             'repository -> model'):
    frm, to = pair.split(' -> ')
    n = sum(x['edges'] for x in GRAPH['layer_pair_edges_structural']
            if x['from'] == frm and x['to'] == to)
    add('Observed structural layer edge %s: %d references' % (pair, n),
        'OBSERVED', 'HIGH', 'type-level references; not runtime verified',
        TOOL_DEX, 'sum of method_signature/field_type/superclass edges',
        source_document='COMPONENT_GRAPH.json')

# ---- 7. v753 shipped content ----------------------------------------------
schema = json.load(open(os.path.join(A, 'MIMO_CONTENT_SCHEMA.json')))
add('Shipped tracks.json v753 contains %d tracks / %d sections / %d tutorial refs' % (
    schema['track_count'], schema['section_count'], schema['tutorial_refs_in_tracks']),
    'OBSERVED', 'HIGH', 'parsed from shipped asset', TOOL_ZIP,
    'publishSetVersion=753, assets/lessons-en/tracks/tracks.json',
    source_document='MIMO_CONTENT_SCHEMA.json / ANALYSIS/01_ANALYSIS_CHAIN.fa.md')
add('Shipped v753 tracks.json has NO node coordinates/spacing/curve fields; those are code-computed',
    'OBSERVED', 'HIGH', 'full JSON key scan over all shipped asset JSONs', TOOL_ZIP,
    'geometry keys found only inside Lottie animation JSON (res/raw/*.json)',
    source_document='ANALYSIS/01_ANALYSIS_CHAIN.fa.md')
add('v52 testdata fixture differs from shipped v753 (difficulty/color/slug/icon absent in v753)',
    'OBSERVED', 'HIGH', 'direct schema comparison', TOOL_ZIP,
    'v52 keys include difficulty,color,shortDescriptionContent,slug,icon; v753 has onboardingCategory',
    source_document='ANALYSIS/01_ANALYSIS_CHAIN.fa.md')

# ---- 8. coroutines & analysis failures ------------------------------------
add('%d DebugMetadata annotations (%s), %d coroutine state fields, %d suspend classes' % (
    CORO['counts']['annotations'], 'Lf70/c;', CORO['counts']['coroutine_state_fields'],
    CORO['counts']['suspend_classes']),
    'OBSERVED', 'HIGH', 'smali annotation recovery', TOOL_SMALI,
    'fields c/f/l/m/v only; n/i/s spilled-variable tables stripped by R8',
    source_document='COROUTINE_STATE_MACHINES.json')
add('Ghidra string-to-function xrefs = 0 (Reference analyzer disabled in DEX PSPEC)',
    'OBSERVED', 'HIGH', 'measured', TOOL_GHIDRA,
    'CONTROL_FLOW.txt contains STR lines but 0 XREF lines',
    source_document='GHIDRA/CONTROL_FLOW.txt')
add('%d / %d class_defs produced Smali; %d failures confined to classes.dex' % (
    INV['analysis_failures']['smali_files_produced'], METRICS['denominators']['class_defs'],
    INV['analysis_failures']['smali_failed_classes']),
    'OBSERVED', 'HIGH', 'measured', TOOL_SMALI,
    'Invalid element width 3/5/7/9/11/13/15/17/19 identical on baksmali 2.3.4 and smali 3.x',
    source_document='COVERAGE_METRICS.json')
add('JADX 1.5.6 emitted %d com.getmimo Java files, %d with "Method not decompiled" stubs' % (
    INV['analysis_failures']['jadx_1_5_6_java_files'],
    INV['analysis_failures']['jadx_1_5_6_stub_files']),
    'OBSERVED', 'HIGH', 'measured', TOOL_JADX,
    'jadx.log finished with errors, count: %d' % INV['analysis_failures']['jadx_1_5_6_reported_total_errors'],
    source_document='DECOMPILED/REPORT.md')

# ---- 9. runtime / server status -------------------------------------------
for label in [
    'Application launch on emulator/ADB', 'Navigation between screens',
    'Learning Path scrolling and node selection', 'Lesson progression',
    'Chapter completion UI', 'Rewards and progress displays',
    'Network request/response bodies in an authorized test environment']:
    add(label + ' — NOT VERIFIED', 'UNKNOWN', 'UNKNOWN',
        'no approved emulator/ADB or authorized test environment exists in this session',
        'n/a', 'no screenshot, UI hierarchy, logcat, or network capture produced',
        source_document='RUNTIME_VERIFICATION.fa.md')
add('Server-authoritative reward confirmation is inferred, not SERVER CONFIRMED',
    'STATICALLY INFERRED', 'LOW', 'no server response observed',
    TOOL_JADX, '/v1/user/rewards/{rewardId}/confirm + "Confirmed reward with id" DEX string',
    source_document='MIMO_COMPLETION_ENGINE.json')
add('Exact HTTP verb of each Retrofit definition is UNKNOWN; method-name inference is explicitly rejected',
    'UNKNOWN', 'UNKNOWN', 'annotation classes were renamed by R8 (@f/@o/@n/@p/@b); no RequestFactory instruction-level mapping or authorized capture',
    TOOL_JADX, '53 annotation strings such as @o("/v1/code"); verb labels GET/POST/PUT/DELETE are tentative LOW labels only',
    source_document='MIMO_RETROFIT_ENDPOINTS.json / DATA_AND_API_MAP.fa.md')
add('Exact numeric scoring formula, dp spacing and curve function remain unresolved',
    'UNKNOWN', 'UNKNOWN', 'method bodies not reconstructed', TOOL_GHIDRA,
    'rewardMultiplier / rewardedSparksForCorrectAnswer field names exist but no numeric constants recovered',
    source_document='LESSON_AND_SCORING_ENGINE.fa.md / LEARNING_PATH_ENGINE.fa.md')

# ---- write EVIDENCE_INDEX --------------------------------------------------
by_status = collections.Counter(e['status'] for e in E)
by_conf = collections.Counter(e['confidence'] for e in E)
index = {
    'document': 'Mimo 9.35 — machine-readable evidence index',
    'source_of_truth': 'original APK sha256=' + INV['apk']['sha256'],
    'status_vocabulary': STATUS,
    'confidence_vocabulary': CONFIDENCE,
    'counts': {'total': len(E), 'by_status': dict(by_status), 'by_confidence': dict(by_conf)},
    'evidence': E,
}
json.dump(index, open(os.path.join(A, 'EVIDENCE_INDEX.json'), 'w'), indent=1, ensure_ascii=False)
print('EVIDENCE_INDEX.json entries', len(E), dict(by_status))

# ---- SUBSYSTEM_EVIDENCE ----------------------------------------------------
KEYWORDS = {
    'A_launch_init': r'(?i)(Lcom/getmimo/App;|Lcom/getmimo/App\$|MainActivity|SplashActivity|/di/|Hilt|Initializer|WorkManager|Startup|InitializationProvider)',
    'B_auth_session': r'(?i)(authentication|/auth/|login|session|Token|AccountRepository|signin|signup|deviceTokens)',
    'C_onboarding': r'(?i)(onboarding|OnboardingActivity|initialconfig|PickAPath|Interests)',
    'D_home_dashboard': r'(?i)(/ui/home|dashboard|/feed|HomeScreen|Overview|OverviewEntryPoint)',
    'E_learning_path': r'(?i)(pathmap|/path/|GetPathMap|tracks?/|\btrack\b|section|certificate|estimatedcompletion|PathToolbar)',
    'F_lesson_execution': r'(?i)(/lesson/|tutorial|interactive|exercise|answer|quiz|CodePlayground|LessonBundle)',
    'G_lesson_progress': r'(?i)(LessonProgress|/progress|completion|completedAt|in_queue)',
    'H_practice_challenges': r'(?i)(practice|challenge)',
    'I_chapter_scoring': r'(?i)(chapterend|ChapterFinished|scoring|earned|GetChapterEnd|CreateChapterEnd)',
    'J_rewards_currency': r'(?i)(reward|coins|sparks|store|product)',
    'K_goals_streaks': r'(?i)(streak|dailygoal|DailyGoal|habit)',
    'L_leaderboard_league': r'(?i)(leaderboard|league|userrank)',
    'M_ai_tutor': r'(?i)(aitutor|conversation|SseConnection|chatmessage|/aiTutor/)',
    'N_settings': r'(?i)(settings|preference|SettingsRepository)',
    'O_client_config_flags': r'(?i)(clientconfig|remoteconfig|featureflag|experiment|contentexperiment|/config/)',
    'P_subscription': r'(?i)(/iap|subscription|paywall|purchase|billing|entitlement|revenuecat|AllPlans)',
}
# Endpoint matching must NOT reuse the class pattern: short tokens such as 'di'
# or 'eta' otherwise match unrelated paths ({rewardId}, metadata ...).
EP_PATTERNS = {
    'A_launch_init': r'(?i)(/v2/client-config|/v1/user/visits|/v1/account$)',
    'B_auth_session': r'(?i)(/v1/account|/v1/authentication|/v1/user/deviceTokens|/v1/user/login|/v1/auth)',
    'C_onboarding': r'(?i)(onboarding|/v1/user/settings|/v1/user/interests|/v1/onboarding)',
    'D_home_dashboard': r'(?i)(/v1/leaderboards/latest|/v1/user/rewards/next|/v1/tracks/completion/lastInteracted)',
    'E_learning_path': r'(?i)(/v1/tracks|/v1/tutorials/[^/]*/progress|certificate|/v1/path|/v1/sections)',
    'F_lesson_execution': r'(?i)(/v1/code|/v1/lessons|/v1/tutorials|/v1/savedCode|/v1/lesson)',
    'G_lesson_progress': r'(?i)(progress|completion)',
    'H_practice_challenges': r'(?i)(practice|challenge)',
    'I_chapter_scoring': r'(?i)(/v1/chapter|/v1/user/rewards|/v1/user/coins|/v1/leaderboards)',
    'J_rewards_currency': r'(?i)(reward|coins|sparks|store|product|/v1/user/activity)',
    'K_goals_streaks': r'(?i)(streak|dailygoal|/v1/user/settings|/v1/user/activity)',
    'L_leaderboard_league': r'(?i)(leaderboard|league|userrank)',
    'M_ai_tutor': r'(?i)(aiTutor|conversation|message)',
    'N_settings': r'(?i)(/v1/user/settings|/v1/user/account|/v1/user/notifications)',
    'O_client_config_flags': r'(?i)(client-config|remote-config|config|experiment)',
    'P_subscription': r'(?i)(iap|subscription|purchase|billing|entitlement|/v1/store|/v1/products)',
}
catalog = GRAPH['catalog']
subs = {}
for key, pat in KEYWORDS.items():
    classes = [c for c in catalog if re.search(pat, c['descriptor'])]
    methods = sorted(set(mm for c in classes[:250] for mm in c['method_names']))[:60]
    ep_pat = EP_PATTERNS.get(key, pat)
    eps = [e for e in ENDPOINTS if re.search(ep_pat, e['path'])]
    sql_pat = {
        'G_lesson_progress': r'(?i)(lesson_progress|chapter_completions|tutorial_completions)',
        'I_chapter_scoring': r'(?i)(chapter_completions|lesson_progress)',
        'E_learning_path': r'(?i)(chapter_completions|tutorial_completions|lesson_progress)',
    }.get(key, pat)
    sql = [s for s in INV['database']['sql_statements'] if re.search(sql_pat, s)]
    kt = sorted(set(c['kotlin_source_file'] for c in classes if 'kotlin_source_file' in c))[:30]
    strings = sorted(set(st['value'] for _, st in ALL_STRINGS
                         if re.search(pat, st['value']) and 3 < len(st['value']) < 90
                         and re.search(r'(?i)(ViewModel|Repository|Api|State|Screen|Fragment|UseCase|/v\d/|Sparks|Coins|Progress)', st['value'])))[:50]
    gf = [f for f in FUNCS if re.search(pat, f['name'])]
    layers = dict(collections.Counter(c['layer'] for c in classes).most_common())
    subs[key] = {
        'keyword_pattern': pat,
        'class_count': len(classes),
        'layer_distribution': layers,
        'sample_classes': [c['descriptor'] for c in classes[:35]],
        'distinct_method_names': methods,
        'retrofit_endpoints': [{'path': e['path'], 'verb_inferred': e['verb_inferred'],
                                'source_file': e['source_file']} for e in eps],
        'sql_statements': sql[:15],
        'kotlin_source_files': kt,
        'dex_string_evidence': strings,
        'ghidra_target_functions': [{'dex': f['dex'], 'name': f['name'], 'address': f['address']} for f in gf[:30]],
        'evidence_index_ids': [e['id'] for e in E if re.search(pat, e['claim'])][:20],
    }
json.dump({'document': 'Per-subsystem evidence extracted from the original APK',
           'subsystems': subs},
          open(os.path.join(A, 'SUBSYSTEM_EVIDENCE.json'), 'w'), indent=1, ensure_ascii=False)
print('SUBSYSTEM_EVIDENCE.json subsystems', len(subs))
for k, v in subs.items():
    print(' ', k, 'classes', v['class_count'], 'eps', len(v['retrofit_endpoints']),
          'sql', len(v['sql_statements']), 'ghidra', len(v['ghidra_target_functions']))
