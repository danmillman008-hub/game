"""MISSION 02 — build COMPLETE_COMPONENT_GRAPH.json and append M02 evidence.

Reads mission-01 artifacts WITHOUT overwriting them, then:
  * builds a method-level graph (real invoke/field edges with DEX offsets)
  * appends (never rewrites) new EV-M02-* entries to EVIDENCE_INDEX.json

Scripts live in ANALYSIS/_TOOLCHAIN/ only.
"""

import os
import json
import re
import collections

A = '/home/user/game/ANALYSIS'
G = json.load(open(A + '/COMPONENT_GRAPH.json'))
B = json.load(open(A + '/DEX_BYTECODE_EVIDENCE.json'))
H = json.load(open(A + '/HTTP_VERBS_RESOLVED.json'))
P = json.load(open(A + '/PATH_GEOMETRY_CONSTANTS.json'))
I = json.load(open(A + '/APK_COMPLETE_INVENTORY.json'))
M = json.load(open(A + '/COVERAGE_METRICS.json'))
S = json.load(open(A + '/SUBSYSTEM_EVIDENCE.json'))['subsystems']

EDGES = B['scenario_exact_edges']


def pick(offset, caller_contains=None):
    for e in EDGES:
        if e['insn_offset'] == offset and (not caller_contains or caller_contains in e['caller']):
            return {
                'dex': e['dex'], 'insn_offset': e['insn_offset'], 'opcode': e['opcode'],
                'caller': e['caller'], 'callee': e['callee'],
                'status': 'OBSERVED (DEX invoke instruction)', 'confidence': 'HIGH',
                'verification_status': 'static bytecode only; NOT RUNTIME VERIFIED',
            }
    return {'insn_offset': offset, 'status': 'UNKNOWN', 'confidence': 'UNKNOWN'}


# ---------------------------------------------------------------------------
# 1. COMPLETE_COMPONENT_GRAPH.json
# ---------------------------------------------------------------------------
nodes = [{
    'class': c['descriptor'], 'layer': c['layer'], 'dex': c['dex'],
    'kotlin_source_file': c.get('kotlin_source_file'),
    'method_names_sample': c.get('method_names', [])[:6],
} for c in G['catalog']]

# subsystem chains: proven where method-call evidence exists, UNKNOWN elsewhere
SUBSYSTEMS = {
    'Application and Initialization': 'A_launch_init',
    'Authentication and Session': 'B_auth_session',
    'Onboarding': 'C_onboarding',
    'Home and Dashboard': 'D_home_dashboard',
    'Learning Path': 'E_learning_path',
    'Lesson and Tutorial': 'F_lesson_execution',
    'Lesson Progress / Sync': 'G_lesson_progress',
    'Practice and Challenges': 'H_practice_challenges',
    'Completion and Scoring': 'I_chapter_scoring',
    'Rewards and Coins': 'J_rewards_currency',
    'Streak and Daily Goal': 'K_goals_streaks',
    'Leaderboards and Leagues': 'L_leaderboard_league',
    'AI Tutor': 'M_ai_tutor',
    'Settings and User Preferences': 'N_settings',
    'Client Config and Flags': 'O_client_config_flags',
    'Subscription / IAP': 'P_subscription',
}

call_pairs = {(e['from'], e['to']): e['invoke_count'] for e in B['call_graph']}

chains = {}
for title, key in SUBSYSTEMS.items():
    v = S[key]
    cls = v['sample_classes']
    by_layer = {}
    for layer in ('ui', 'viewmodel', 'usecase_interactor', 'repository_remote',
                  'repository_local', 'repository'):
        hits = [c['class'] for c in nodes
                if c['layer'] == layer and any(
                    re.search(v['keyword_pattern'], c['class']) for _ in [0])]
        by_layer[layer] = hits[:4]
    linked = sum(1 for (f, t), n in call_pairs.items()
                 if any(re.search(v['keyword_pattern'], f) or re.search(v['keyword_pattern'], t)
                        for _ in [0]))
    api = [{'verb': r['resolved_http_verb'], 'path': r['path'],
            'evidence': 'HTTP_VERBS_RESOLVED.json / classes3.dex @%s' % (r['verb_const_offset'] or '')}
           for r in H['endpoints'] if r['path'] in [x['path'] for x in v['retrofit_endpoints']]]
    chains[title] = {
        'screen': by_layer['ui'], 'viewmodel': by_layer['viewmodel'],
        'usecase': by_layer['usecase_interactor'],
        'repository_remote': by_layer['repository_remote'],
        'repository_local': by_layer['repository_local'],
        'api': api,
        'database': [s[:150] for s in v['sql_statements'][:5]],
        'method_call_edge_pairs_in_graph': linked,
        'chain_status': ('OBSERVED (some method-call edges)' if linked else
                         'UNKNOWN (no method-call edge matched this keyword)'),
        'note': 'The Screen->ViewModel->UseCase->Repository pattern is NOT imposed; '
                'empty arrays mean no class of that layer matched this subsystem keyword.',
    }

# proven 6-step scenario (the user's acceptance criterion)
scenario = [
    {'step': 1, 'label': 'Answer evaluated as correct',
     'evidence': [pick('0xa56474'), pick('0x997612')],
     'ghidra': 'LessonProgress::isSolvedCorrectly @0x509744bc: iget [0x472e] + if_lt v1,1 => intField >= 1',
     'data_change': 'LessonProgress.attempts / tries incremented (STATICALLY INFERRED)',
     'status': 'OBSERVED (static)', 'runtime_verified': False},
    {'step': 2, 'label': 'Lesson progress state created/updated',
     'evidence': [pick('0xa563da'), pick('0x997ddc'), pick('0x997e08'),
                  pick('0x997e22'), pick('0x997e32')],
     'data_change': 'LessonProgressQueue.storeLessonProgress -> '
                    'LessonProgressRepository.addOrUpdateLessonProgressInQueue',
     'status': 'OBSERVED (static)', 'runtime_verified': False},
    {'step': 3, 'label': 'Local persistence + remote sync',
     'evidence': [pick('0x99881a'), pick('0x998976'), pick('0x998992'),
                  pick('0x9989d8'), pick('0x998a08')],
     'api': 'POST /v1/tutorials/{tutorialId}/progress (verb resolved from bytecode)',
     'sql': 'INSERT INTO lesson_progress ... / SELECT * FROM lesson_progress WHERE in_queue = 1 / DELETE ... WHERE in_queue = 1',
     'status': 'OBSERVED (static SQL + invoke)', 'runtime_verified': False,
     'server_confirmed': False},
    {'step': 4, 'label': 'Server response mapped to client state',
     'evidence': [pick('0x998cf4'), pick('0x998cfe')],
     'data_change': 'PostProgressResponse.getReachedGoal() / getDailyGoalCoinReward() -> '
                    'LessonProgressSyncResult via toLessonProgressSyncResult',
     'status': 'OBSERVED (static)', 'runtime_verified': False, 'server_confirmed': False},
    {'step': 5, 'label': 'Reward / chapter-end screens driven by sync result',
     'evidence': [pick('0x9a282a'), pick('0x9a284a'), pick('0x9a2660')],
     'status': 'OBSERVED (static)', 'runtime_verified': False},
    {'step': 6, 'label': 'Learning Path recomputes node state',
     'evidence': [pick('0x9a8f9c'), pick('0x9a9240'), pick('0x9a927e'), pick('0x9a92f4'),
                  pick('0x9a93e6'), pick('0x9a940c'), pick('0x9a9434'), pick('0x9a943c'),
                  pick('0x9a9444')],
     'status': 'OBSERVED (static)', 'runtime_verified': False},
    {'step': 7, 'label': 'Next node becomes available',
     'evidence': [], 'status': 'UNKNOWN',
     'reason': 'The rule mapping completion/isRequired/type -> locked/available/completed '
               'was not reconstructed; no runtime observation exists.',
     'runtime_verified': False},
]

graph = {
    'document': 'MISSION 02 — COMPLETE_COMPONENT_GRAPH (method-level, evidence-backed)',
    'source_of_truth': 'APK sha256 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a',
    'extends_without_overwriting': 'COMPONENT_GRAPH.json (mission 01)',
    'status_tags': ['OBSERVED', 'STATICALLY INFERRED', 'RUNTIME VERIFIED', 'SERVER CONFIRMED', 'UNKNOWN'],
    'method': 'Control-flow-reachable Dalvik decode of all 12 DEX; invoke-*/iget/iput '
              'targets resolved to method_ids/field_ids with exact file offsets. '
              'Junk/obfuscation payloads and invoke-custom call sites excluded.',
    'totals': {
        'mimo_class_nodes': len(nodes),
        'class_defs_all': I['dex_totals']['class_defs'],
        'methods_decoded': B['totals']['methods_decoded'],
        'instructions_decoded_reachable': B['totals']['insns_decoded'],
        'invoke_instructions': B['totals']['invoke_insns'],
        'field_access_instructions': B['totals']['field_insns'],
        'mimo_internal_call_pairs': B['mimo_internal_call_pairs'],
        'mimo_internal_call_edges': B['mimo_internal_call_edges_total'],
        'mimo_field_pairs_full': B['mimo_field_pairs'],
        'scenario_exact_edges': B['scenario_method_edges'],
        'http_verbs_resolved': len(H['endpoints']),
        'http_verbs_corrected': len(H['corrections']),
        'geometry_constants_extracted': P['literal_count'],
        'runtime_verified_edges': 0,
        'server_confirmed_responses': 0,
    },
    'layer_counts': G['layer_counts'],
    'structural_layer_pairs': G['layer_pair_edges_structural'],
    'nodes': nodes,
    'method_call_edges': B['call_graph'][:6016],
    'field_edges_top': B['field_graph'][:2000],
    'scenario_exact_edges': B['scenario_exact_edges'],
    'http_verbs': H['endpoints'],
    'subsystem_chains': chains,
    'proven_scenario_chain': scenario,
    'coverage': {
        'methods_with_reachable_decode': '122546/122546 = 100%',
        'class_defs_with_mimo_catalog': '3133/3133 com/getmimo class_defs = 100%',
        'runtime_tests_executed': '0/9 = 0% (TEST-001..TEST-009)',
        'scenario_steps_static_evidence': '6/7 (step 7 UNKNOWN)',
        'scenario_steps_runtime_verified': '0/7 = 0%',
        'http_verbs_resolved_from_bytecode': '53/53 = 100%',
        'http_verbs_server_confirmed': '0/53 = 0%',
    },
    'limitations': [
        'Method-call edges are static bytecode facts; they do NOT prove execution order or that a call happened.',
        'R8-renamed classes (k, j, d, a ...) cannot be fully de-obfuscated; semantic roles are STATICALLY INFERRED.',
        'No emulator/ADB existed: 0 screenshots, 0 UI hierarchies, 0 logcat, 0 network captures.',
    ],
}
json.dump(graph, open(A + '/COMPLETE_COMPONENT_GRAPH.json', 'w'),
          ensure_ascii=False, separators=(',', ':'))
print('COMPLETE_COMPONENT_GRAPH.json', os.path.getsize(A + '/COMPLETE_COMPONENT_GRAPH.json'), 'bytes')

# ---------------------------------------------------------------------------
# 2. append (never rewrite) EVIDENCE_INDEX.json
# ---------------------------------------------------------------------------
E = json.load(open(A + '/EVIDENCE_INDEX.json'))
prior = len(E['evidence'])
prefix = 'EV-M02-'


def add(claim, status, conf, vstatus, tool, excerpt, **kw):
    row = {
        'id': '%s%04d' % (prefix, len(E['evidence']) - prior + 1),
        'claim': claim, 'status': status, 'confidence': conf,
        'verification_status': vstatus, 'tool_and_method': tool,
        'evidence_excerpt': excerpt,
        'dex': kw.get('dex', 'n/a'),
        'class_descriptor': kw.get('class_descriptor', 'n/a'),
        'method_or_signature': kw.get('method', 'n/a'),
        'address_or_offset': kw.get('offset', 'n/a'),
        'source_document': kw.get('source', 'n/a'),
    }
    E['evidence'].append(row)


TOOL = 'dexlib.py + dex_bytecode.decode_reachable (read-only DEX instruction decode)'
add('MISSION 02 environment: no adb/emulator/sdkmanager/aapt2/apksigner on PATH; '
    'no ANDROID_HOME; no /dev/kvm; no USB device; no emulator process',
    'OBSERVED', 'HIGH', 'measured in sandbox',
    'bash command -v / proc /dev / ps',
    'adb=ABSENT, emulator=ABSENT, /dev/kvm=No such file, dl.google.com HTTP 000',
    source='RUNTIME_VERIFICATION.fa.md')
add('Android SDK system images and SDK tools unreachable (outbound allowlist excludes dl.google.com)',
    'OBSERVED', 'HIGH', 'measured', 'curl -m 5', 'dl.google.com 000; developer.android.com 000',
    source='RUNTIME_VERIFICATION.fa.md')
add('Original APK hash matches established original; ZIP readable; v2+v3 signing block present',
    'OBSERVED', 'HIGH', 'recomputed', 'sha256sum + zipfile + APK Signing Block parser',
    'sha256=48ce1740…f7c7a, 14398 members, signing block @141062144 size 4088, IDs 0x7109871a(v2)/0xf05368c0(v3)',
    source='APK_COMPLETE_INVENTORY.json')
add('APK is non-debuggable with allowBackup=false: adb backup/run-as cannot read the Room DB',
    'OBSERVED', 'HIGH', 'parsed from binary manifest',
    'androguard AXMLPrinter (existing install)',
    'application.allowBackup=false; android:debuggable absent; minSdk=28 targetSdk=36 compileSdk=37',
    source='APK_COMPLETE_INVENTORY.json')
add('Target SDK 36 requires an Android 16 system image; no AVD exists in the repo or workflows',
    'OBSERVED', 'HIGH', 'measured', 'grep over .github/workflows + manifest',
    'uses_sdk targetSdkVersion=36; workflows contain no avd/adb/android-emulator step',
    source='RUNTIME_VERIFICATION.fa.md')
add('122546/122546 methods decoded with control-flow-reachable Dalvik decoder',
    'OBSERVED', 'HIGH', 'independent decode', TOOL,
    '3064593 reachable instructions, 552625 invoke, 391556 field accesses; '
    'Smob junk payloads and 7327 invoke-custom call sites excluded',
    source='DEX_BYTECODE_EVIDENCE.json')
add('6016 real Mimo-internal class-pair call edges with exact DEX offsets',
    'OBSERVED', 'HIGH', 'static bytecode', TOOL,
    '12513 invoke edges between Lcom/getmimo/ classes; each has caller/callee method signature and insn offset',
    source='DEX_BYTECODE_EVIDENCE.json')
add('HTTP verbs resolved from Retrofit bytecode, NOT from method names',
    'OBSERVED', 'HIGH', 'static bytecode; NOT runtime verified; NOT server confirmed', TOOL,
    'classes3.dex Lge0/r0;->a @0xabb18: instance-of Lie0/f; -> const-string GET @0xabb8e; '
    'Lie0/o; -> POST @0xabbf0; Lie0/n; -> PATCH @0xabbce; Lie0/p; -> PUT @0xabc12; Lie0/b; -> DELETE @0xabb6c',
    source='HTTP_VERBS_RESOLVED.json')
add('6 previously inferred HTTP verb labels were wrong and are corrected',
    'OBSERVED', 'HIGH', 'recomputed from annotation classes', TOOL,
    '@n PUT->PATCH (3 endpoints), @p DELETE->PUT (2), @b POST/other->DELETE (1); '
    'corrected counts GET26 POST21 PATCH3 PUT2 DELETE1',
    source='HTTP_VERBS_RESOLVED.json')
add('POST /v1/tutorials/{tutorialId}/progress is called by LessonProgressRepository',
    'OBSERVED', 'HIGH', 'static bytecode', TOOL,
    'classes.dex @0x998976 invoke-interface LessonProgressApi->postProgress(J, PostProgressRequestBody, Continuation)',
    source='DEX_BYTECODE_EVIDENCE.json / HTTP_VERBS_RESOLVED.json')
add('ExecutableLessonViewModel triggers isSolvedCorrectly then storeLessonProgress',
    'OBSERVED', 'HIGH', 'static bytecode', TOOL,
    '@0xa56474 -> LessonProgress.isSolvedCorrectly(); @0xa563da -> LessonProgressQueue.storeLessonProgress()',
    source='DEX_BYTECODE_EVIDENCE.json')
add('PostProgressResponse is mapped to client state via getReachedGoal/getDailyGoalCoinReward',
    'OBSERVED', 'HIGH', 'static bytecode', TOOL,
    'toLessonProgressSyncResult @0x998cf4 -> getReachedGoal(); @0x998cfe -> getDailyGoalCoinReward()',
    source='DEX_BYTECODE_EVIDENCE.json')
add('Chapter-end screens are driven by the lesson-progress sync result',
    'OBSERVED', 'HIGH', 'static bytecode', TOOL,
    'GetChapterEndSuccessState$storeAndPostAllLessonProgress$lessonProgressSyncResult$1::invokeSuspend '
    '@0x9a282a -> chapter interactor; @0x9a284a -> storeAndPostAllLessonProgress',
    source='DEX_BYTECODE_EVIDENCE.json')
add('Learning Path node state loop reads isCompleted/isRequired/getType over shipped v753 tutorials',
    'OBSERVED', 'HIGH', 'static bytecode', TOOL,
    'GetPathMapState$invoke$3::invokeSuspend @0x9a9240 getSections; @0x9a927e getTutorials; '
    '@0x9a92f4 getType; @0x9a93e6 isRequired; @0x9a940c isCompleted; @0x9a9444 getChapters',
    source='DEX_BYTECODE_EVIDENCE.json')
add('146 real float/int literals extracted from Learning Path composable bytecode',
    'OBSERVED', 'HIGH', 'static literal extraction', TOOL,
    'classes.dex Lcom/getmimo/ui/path/map/k; e.g. @0xab67c0=4.0, @0xab67cc=6.0, @0xab67f4=12.0, '
    '@0xab6800=3.0 followed by Lu3/c;->i0(F)F; @0xab357a=180.0, @0xab35c0=270.0, @0xab361c=90.0',
    source='PATH_GEOMETRY_CONSTANTS.json')
add('Exact dp values, X/Y node coordinates, curve function, scroll offset and animation remain UNKNOWN',
    'UNKNOWN', 'UNKNOWN', 'not established',
    TOOL + ' + Ghidra CONTROL_FLOW.txt (0 string xrefs)',
    'Literals exist but their semantic attribution to spacing/curve is unresolved; no UI hierarchy / screenshot',
    source='LEARNING_PATH_GEOMETRY.fa.md')
add('Numeric scoring formulas and reward multipliers remain UNKNOWN',
    'UNKNOWN', 'UNKNOWN', 'not established', TOOL,
    'rewardMultiplier / rewardedSparksForCorrectAnswer are field NAMES only; no numeric constants recovered',
    source='LESSON_SCORING_VERIFICATION.fa.md')
add('Rule that unlocks the next Learning Path node remains UNKNOWN',
    'UNKNOWN', 'UNKNOWN', 'not established', TOOL,
    'no reconstructed method body mapping completion/type/section -> locked/available/completed',
    source='COMPLETE_APPLICATION_FLOW.fa.md')
for i in range(1, 10):
    add('TEST-%03d runtime experiment NOT EXECUTED (no approved emulator/ADB)' % i,
        'UNKNOWN', 'UNKNOWN', 'no approved runtime environment',
        'n/a', '0 screenshot, 0 UI hierarchy, 0 logcat, 0 network capture',
        source='RUNTIME_VERIFICATION.fa.md')

E['counts'] = {
    'total': len(E['evidence']),
    'by_status': dict(collections.Counter(x['status'] for x in E['evidence'])),
    'by_confidence': dict(collections.Counter(x['confidence'] for x in E['evidence'])),
}
E['mission_02_append'] = {
    'prior_entries_preserved': prior,
    'new_entries': len(E['evidence']) - prior,
    'note': 'Existing mission-01 entries were preserved byte-for-byte in content; only appended.',
}
json.dump(E, open(A + '/EVIDENCE_INDEX.json', 'w'), indent=1, ensure_ascii=False)
print('EVIDENCE_INDEX.json preserved', prior, 'appended', len(E['evidence']) - prior,
      'total', len(E['evidence']))
print('status', E['counts']['by_status'])
