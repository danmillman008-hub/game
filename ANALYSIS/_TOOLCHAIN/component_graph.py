"""Mimo 9.35 — component catalog + dependency graph from REAL references.

Evidence sources (all read-only):
  * 12 DEX files via dexlib.py (class_defs, superclass, field_ids, method_ids)
  * 17,626 Smali files produced by apktool 2.9.3 (invoke-*, new-instance, .field, .super)
  * JADX 1.1.0 / 1.5.6 emitted Java class lists
  * AndroidManifest.xml parsed in APK_COMPLETE_INVENTORY.json
  * Kotlin DebugMetadata / source-file strings

No architecture is assumed: edges only exist where a reference was observed.
Writes ANALYSIS/COMPONENT_GRAPH.json.
"""

import os
import re
import sys
import json
import glob
import collections

ROOT = '/home/user/game'
SMALI = '/home/user/_work/_analysis/apktool2_out'
JADX110 = '/home/user/_work/_analysis/jadx110/sources/com/getmimo'
JADX156 = '/home/user/_work/_analysis/jadx156/classes/com/getmimo'
sys.path.insert(0, os.path.join(ROOT, 'ANALYSIS/_TOOLCHAIN'))
from dexlib import Dex  # noqa: E402

SUBSYSTEMS = {
    'A_launch_init': r'(?i)(^com/getmimo/App|MainActivity|Splash|/di/|Hilt|Initializer|WorkManager|Startup)',
    'B_auth_session': r'(?i)(authentication|/auth|login|session|Token|Account|signin|signup)',
    'C_onboarding': r'(?i)(onboarding|initialconfig)',
    'D_home_dashboard': r'(?i)(^com/getmimo/ui/home|dashboard|/feed|HomeScreen)',
    'E_learning_path': r'(?i)(/path/|pathmap|track|section|certificate)',
    'F_lesson_execution': r'(?i)(/lesson/|tutorial|interactive|exercise|codeeditor|quiz)',
    'G_lesson_progress': r'(?i)(progress|LessonProgress|completion)',
    'H_practice_challenges': r'(?i)(practice|challenge)',
    'I_chapter_scoring': r'(?i)(chapterend|ChapterFinished|scoring|stats|eta)',
    'J_rewards_currency': r'(?i)(reward|coins|sparks|store|product)',
    'K_goals_streaks': r'(?i)(streak|dailygoal|habit)',
    'L_leaderboard_league': r'(?i)(leaderboard|league)',
    'M_ai_tutor': r'(?i)(aitutor|ai_tutor|conversation|sse|chatmessage)',
    'N_settings': r'(?i)(settings|preference|/config)',
    'O_client_config_flags': r'(?i)(clientconfig|remoteconfig|featureflag|experiment|abtest|/config/)',
    'P_subscription': r'(?i)(/iap|subscription|paywall|purchase|billing|entitlement|revenuecat)',
}

LAYER_RULES = [
    ('application', lambda q: q == 'App' or q.startswith('App$') or 'Application' in q),
    ('entry_point', lambda q: bool(re.search(r'(Activity|Fragment)$', q)) or q.startswith('ui/Main')),
    ('viewmodel', lambda q: 'ViewModel' in q),
    ('usecase_interactor', lambda q: q.startswith('interactors/') or '/usecase' in q or '/interactor' in q or 'UseCase' in q),
    ('repository_remote', lambda q: q.startswith('data/source/remote/') or q.startswith('data/remote/')),
    ('repository_local', lambda q: q.startswith('data/source/local/') or q.startswith('data/local/') or '/room/' in q),
    ('repository', lambda q: 'Repository' in q),
    ('network_client', lambda q: q.startswith('data/network/') or '/retrofit' in q or 'ApiService' in q or q.endswith('Api')),
    ('model', lambda q: q.startswith('data/model/') or q.startswith('core/model/') or q.startswith('data/content/') or '/model/' in q),
    ('dependency_injection', lambda q: q.startswith('di/') or '/di/' in q or 'Module' in q or '_Factory' in q or 'Hilt' in q),
    ('background_worker', lambda q: 'Worker' in q or q.startswith('worker/') or 'JobService' in q or '/work/' in q),
    ('navigation', lambda q: 'Navigation' in q or 'NavHost' in q or 'Route' in q or 'Navigator' in q or 'Destination' in q),
    ('analytics', lambda q: q.startswith('analytics/') or 'Analytics' in q or 'Tracking' in q),
    ('ui', lambda q: q.startswith('ui/') or q.startswith('widget/') or 'Screen' in q or q.endswith('Kt') or 'Compose' in q),
    ('data_other', lambda q: q.startswith('data/') or q.startswith('core/')),
    ('other_mimo', lambda q: True),
]


def layer_of(desc):
    if not desc.startswith('Lcom/getmimo/') or not desc.endswith(';'):
        return 'external_or_obfuscated'
    q = desc[1:-1][len('com/getmimo/'):]
    for name, fn in LAYER_RULES:
        try:
            if fn(q):
                return name
        except Exception:
            pass
    return 'other_mimo'


def subsystem_of(desc):
    q = desc[1:-1] if desc.startswith('L') and desc.endswith(';') else desc
    out = [k for k, pat in SUBSYSTEMS.items() if re.search(pat, q)]
    return out or ['U_unclassified']


def main():
    # ---------- DEX structures ----------
    dexs = {}
    for p in sorted(glob.glob(os.path.join(ROOT, 'ANALYSIS/_INPUT/classes*.dex'))):
        d = Dex(open(p, 'rb').read(), os.path.basename(p))
        dexs[d.name] = d

    catalog = {}
    structural_edges = collections.Counter()
    evidence_by_class = collections.defaultdict(list)

    for name, d in dexs.items():
        for c in d.class_defs:
            desc = c['descriptor']
            if not desc.startswith('Lcom/getmimo/') or not desc.endswith(';'):
                continue
            rec = catalog.setdefault(desc, {
                'descriptor': desc, 'dex': name, 'layer': layer_of(desc),
                'subsystems': subsystem_of(desc),
                'superclass': c['superclass'], 'interfaces_off': c['interfaces_off'],
                'source_file': c['source_file'], 'access_flags': c['access_flags'],
                'defined_methods': len(c['defined_methods']),
                'defined_methods_with_code': sum(1 for m in c['defined_methods'] if m['code_off']),
                'defined_fields': c['n_static_fields'] + c['n_instance_fields'],
                'method_names': [], 'field_types': [], 'signature_types': [],
                'smali_file': None,
            })
            if c['superclass'].startswith('Lcom/getmimo/'):
                structural_edges[(desc, c['superclass'], 'superclass')] += 1
            for m in c['defined_methods']:
                if m['name']:
                    rec['method_names'].append(m['name'])
                sig = m['signature']
                for t in re.findall(r'L[^;]+;', sig):
                    if t.startswith('Lcom/getmimo/') and t != desc:
                        rec['signature_types'].append(t)
                        structural_edges[(desc, t, 'method_signature')] += 1
        for f in d.field_ids:
            cl, ty = f['class'], f['type']
            if cl.startswith('Lcom/getmimo/') and ty.startswith('Lcom/getmimo/') and cl != ty and cl in catalog:
                catalog[cl]['field_types'].append(ty)
                structural_edges[(cl, ty, 'field_type')] += 1

    for desc, rec in catalog.items():
        rec['method_names'] = sorted(set(rec['method_names']))[:40]
        rec['field_types'] = sorted(set(rec['field_types']))[:40]
        rec['signature_types'] = sorted(set(rec['signature_types']))[:40]
        rec['method_name_count'] = len(rec['method_names'])

    # ---------- JADX class lists (logical names, even where bodies are stubs) ----------
    jadx_lists = {}
    for label, root in (('jadx_1_1_0', JADX110), ('jadx_1_5_6', JADX156)):
        fs = glob.glob(root + '/**/*.java', recursive=True)
        jadx_lists[label] = len(fs)
        for p in fs:
            rel = os.path.relpath(p, root).replace(os.sep, '/')
            desc = 'Lcom/getmimo/' + rel[:-5].replace('/', '/') + ';'
            if desc in catalog:
                catalog[desc][label + '_java'] = True
    print('JADX class lists', jadx_lists)

    # ---------- Smali: real invoke / new-instance / field / super edges ----------
    smali_edges = collections.Counter()
    smali_class_files = 0
    obf_to_logical = {}
    srcfile_obf = collections.Counter()
    for p in glob.glob(SMALI + '/smali*/**/*.smali', recursive=True):
        smali_class_files += 1
        try:
            s = open(p, errors='replace').read()
        except Exception:
            continue
        cm = re.search(r'^\.class .*?(L[^;\s]+);', s, re.M)
        if not cm:
            continue
        # smali regexes capture the descriptor WITHOUT the trailing ';'.
        # Normalize to the exact DEX form so layer_of()/catalog lookups work.
        caller = cm.group(1) + ';'
        sm = re.search(r'^\.source "([^"]*)"', s, re.M)
        src = sm.group(1) if sm else ''
        dm = re.search(r'\.annotation runtime Lf70/c;(.*?)\.end annotation', s, re.S)
        logical = src_kotlin = None
        if dm:
            block = dm.group(1)
            ccm = re.search(r'\bc\s*=\s*"([^"]+)"', block)
            ffm = re.search(r'\bf\s*=\s*"([^"]+)"', block)
            logical = ccm.group(1) if ccm else None
            src_kotlin = ffm.group(1) if ffm else None
        if logical and not caller.startswith('Lcom/getmimo/'):
            obf_to_logical[caller] = logical
        if src_kotlin and src_kotlin.endswith('.kt'):
            srcfile_obf[src_kotlin] += 1
        if src and not src.startswith('r8-map-id') and src.endswith('.kt'):
            srcfile_obf[src] += 1
        if caller in catalog:
            catalog[caller]['smali_file'] = os.path.relpath(p, SMALI)
            if src_kotlin:
                catalog[caller]['kotlin_source_file'] = src_kotlin
        for m in re.finditer(r'\binvoke-\w+(?:/\w+)?\s+(?:\{[^}]*\}|\{[^}]*\})\s*,\s*(L[^;\s]+);->([^\s(]+)\(', s):
            callee = m.group(1) + ';'
            if callee != caller:
                smali_edges[(caller, callee, 'invoke')] += 1
        for m in re.finditer(r'\bnew-instance\s+\S+,\s*(L[^;\s]+);', s):
            callee = m.group(1) + ';'
            if callee != caller:
                smali_edges[(caller, callee, 'new_instance')] += 1
        for m in re.finditer(r'^\.field[^\n]*:\s*(L[^;\s]+);', s, re.M):
            callee = m.group(1) + ';'
            if callee != caller:
                smali_edges[(caller, callee, 'field_type')] += 1
        sup = re.search(r'^\.super\s+(L[^;\s]+);', s, re.M)
        if sup:
            target = sup.group(1) + ';'
            if target != caller:
                smali_edges[(caller, target, 'superclass')] += 1
    print('smali files', smali_class_files, 'smali edges', len(smali_edges),
          'obfuscated->logical mappings', len(obf_to_logical), 'kotlin source names', len(srcfile_obf))

    # ---------- layer-pair aggregation ----------
    def agg(edges):
        pairs = collections.Counter()
        for (a, b, kind), n in edges.items():
            pairs[(layer_of(a), layer_of(b), kind)] += n
        return [{'from': k[0], 'to': k[1], 'kind': k[2], 'edges': v}
                for k, v in pairs.most_common()]

    mimo_smali = collections.Counter({k: v for k, v in smali_edges.items()
                                      if k[0].startswith('Lcom/getmimo/')})
    print('mimo smali edges', sum(mimo_smali.values()))

    # ---------- navigation / route evidence ----------
    all_strings = set()
    for d in dexs.values():
        all_strings.update(st['value'] for st in d.strings)
    routes = sorted(s for s in all_strings
                    if re.match(r'^[a-z][a-z0-9_/{}.\-]{2,70}$', s)
                    and re.search(r'(?i)(route|screen|destination|home|learn|practice|leaderboard|profile|onboarding|lesson|path|chapter|settings|paywall|login|ai|track)', s)
                    and ' ' not in s and len(s) < 70)
    nav_classes = sorted(desc for desc in catalog
                         if re.search(r'(?i)(NavHost|Navigation|Navigator|Route|Destination|NavGraph|NavController)', desc))
    deep_links = []
    inv = json.load(open(os.path.join(ROOT, 'ANALYSIS/APK_COMPLETE_INVENTORY.json')))
    for comp, items in inv['manifest']['components'].items():
        for it in items:
            for f in it.get('intent_filters', []):
                if f.get('schemes') and any(x for x in f['schemes'] if x):
                    deep_links.append({'component': comp, 'name': it['name'], 'schemes': f['schemes'],
                                       'actions': f['actions']})

    # ---------- Compose / ViewModel / Repository evidence lists ----------
    groups = collections.defaultdict(list)
    for desc, rec in catalog.items():
        groups[rec['layer']].append(desc)
    print('layers', {k: len(v) for k, v in groups.items()})
    print('subsystems', dict(collections.Counter(s for r in catalog.values() for s in r['subsystems']).most_common()))

    out = {
        'document': 'Mimo 9.35 — component catalog and observed dependency graph',
        'method': 'edges derived from DEX class_defs/field_ids/method_ids and Smali invoke/new-instance/.field/.super instructions only',
        'status_tags': ['OBSERVED', 'STATICALLY INFERRED', 'RUNTIME VERIFIED', 'SERVER CONFIRMED', 'UNKNOWN'],
        'totals': {
            'mimo_class_defs_catalogued': len(catalog),
            'all_class_defs': sum(len(d.class_defs) for d in dexs.values()),
            'smali_files_scanned': smali_class_files,
            'structural_edges': len(structural_edges),
            'smali_edges': len(smali_edges),
            'mimo_smali_edges': sum(mimo_smali.values()),
            'jadx_class_lists': jadx_lists,
            'obfuscated_to_logical_mappings': len(obf_to_logical),
            'kotlin_source_file_names_recovered': len(srcfile_obf),
        },
        'layer_counts': {k: len(v) for k, v in groups.items()},
        'subsystem_counts': dict(collections.Counter(s for r in catalog.values() for s in r['subsystems']).most_common()),
        'layer_pair_edges_structural': agg(structural_edges),
        'layer_pair_edges_smali': agg(mimo_smali),
        'navigation': {
            'nav_related_classes': nav_classes[:150],
            'route_like_strings': routes[:300],
            'manifest_deep_links': deep_links,
            'note': 'route strings are OBSERVED DEX constants; whether a string is actually a navigation route is STATICALLY INFERRED only where NavHost/Navigator class references exist. Full route graph UNKNOWN.',
        },
        'r8': {
            'map_id': inv['r8_build_markers'],
            'mapping_file_shipped': False,
            'mapped_obfuscated_classes_sample': dict(list(sorted(obf_to_logical.items()))[:60]),
            'kotlin_source_file_names': dict(srcfile_obf.most_common(80)),
            'note': 'R8 mapping file is NOT shipped; de-obfuscation of short-named classes is partial and evidence-limited.',
        },
        'catalog': sorted(catalog.values(), key=lambda r: r['descriptor']),
        'edges_sample_structural': [
            {'from': a, 'to': b, 'kind': k, 'count': n}
            for (a, b, k), n in list(structural_edges.most_common(200))],
        'edges_sample_smali': [
            {'from': a, 'to': b, 'kind': k, 'count': n}
            for (a, b, k), n in list(mimo_smali.most_common(200))],
    }
    path = os.path.join(ROOT, 'ANALYSIS/COMPONENT_GRAPH.json')
    json.dump(out, open(path, 'w'), indent=1, ensure_ascii=False)
    print('wrote COMPONENT_GRAPH.json', os.path.getsize(path), 'bytes')
    print('\nTop structural layer pairs:')
    for x in out['layer_pair_edges_structural'][:12]:
        print(' ', x)
    print('\nTop smali layer pairs:')
    for x in out['layer_pair_edges_smali'][:12]:
        print(' ', x)
    return out


if __name__ == '__main__':
    main()
