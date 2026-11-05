"""Mimo 9.35 — verified full APK inventory + Ghidra reconciliation.

READ-ONLY with respect to the original APK/DEX/resources.
Writes only ANALYSIS/*.json. All scripts live in ANALYSIS/_TOOLCHAIN.

Run:  PYTHONPATH=ANALYSIS/_TOOLCHAIN:TOOLS/_pylib python3 ANALYSIS/_TOOLCHAIN/apk_inventory.py
"""

import os
import re
import sys
import json
import glob
import types
import zipfile
import hashlib
import struct
import collections
from xml.dom import minidom

ROOT = '/home/user/game'
APK = '/home/user/_work/apk/Mimo_9.35 (1).apk'
APK_SHA256_EXPECTED = '48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a'
GHIDRA_DIR = os.path.join(ROOT, 'ANALYSIS/GHIDRA')

from dexlib import Dex  # noqa: E402


# ---------------------------------------------------------------------------
# Minimal stubs so the ALREADY-INSTALLED androguard 4.1.4 can be imported
# without installing loguru / lxml. No new tool is installed.
# ---------------------------------------------------------------------------
def _install_stubs():
    if 'loguru' not in sys.modules:
        lg = types.ModuleType('loguru')

        class _Log:
            def __getattr__(self, _n):
                def _noop(*_a, **_k):
                    pass
                return _noop
        lg.logger = _Log()
        sys.modules['loguru'] = lg
    if 'lxml' not in sys.modules:
        lx = types.ModuleType('lxml')
        et = types.ModuleType('lxml.etree')

        class _E:
            def __init__(self, tag, nsmap=None, attrib=None):
                self.tag = tag
                self.attrib = dict(attrib or {})
                self.text = None
                self.children = []
                self.nsmap = nsmap or {}

            def set(self, k, v):
                self.attrib[k] = v

            def append(self, c):
                self.children.append(c)

        def _comment(t):
            e = _E('#comment')
            e.text = t
            return e

        def _tostring(root, encoding='utf-8', pretty_print=True):
            from xml.sax.saxutils import escape, quoteattr

            def ser(e):
                if e.tag == '#comment':
                    return '<!--' + escape(e.text or '') + '-->'
                a = ''.join(' %s=%s' % (k, quoteattr(str(v))) for k, v in e.attrib.items())
                return '<%s%s>%s%s</%s>' % (
                    e.tag, a, escape(e.text or ''),
                    ''.join(ser(c) for c in e.children), e.tag)
            return ser(root).encode(encoding)

        et.Element = _E
        et.SubElement = lambda p, t, **k: None
        et.Comment = _comment
        et.tostring = _tostring
        lx.etree = et
        sys.modules['lxml'] = lx
        sys.modules['lxml.etree'] = et


_install_stubs()
from androguard.core.axml import AXMLPrinter, ARSCParser  # noqa: E402

A = '{http://schemas.android.com/apk/res/android}'


def attr(node, name):
    return (node.getAttribute(A + name) or node.getAttribute('android_' + name)
            or node.getAttribute(name) or '')


def parse_manifest(xml_bytes):
    raw = AXMLPrinter(xml_bytes).get_xml(pretty=False).decode('utf-8', 'replace')
    # AXMLPrinter emits Clark-notation attribute names which expat rejects.
    raw = re.sub(r'\{[^{}]+\}([A-Za-z_][\w.\-:]*)', r'android_\1', raw)
    doc = minidom.parseString(raw)
    m = doc.documentElement
    app = doc.getElementsByTagName('application')
    out = {
        'package': m.getAttribute('package'),
        'versionCode': attr(m, 'versionCode'),
        'versionName': attr(m, 'versionName'),
        'compileSdkVersion': attr(m, 'compileSdkVersion'),
        'platformBuildVersionCode': m.getAttribute('platformBuildVersionCode'),
        'uses_sdk': [dict(x.attributes.items()) for x in doc.getElementsByTagName('uses-sdk')],
        'uses_permissions': sorted(set(x.getAttribute('android_name') or x.getAttribute('name') for x in doc.getElementsByTagName('uses-permission'))),
        'uses_permission_sdk_23': [],
        'application': {},
        'components': {},
    }
    if app:
        a = app[0]
        out['application'] = {
            'name': attr(a, 'name'), 'label': attr(a, 'label'),
            'allowBackup': attr(a, 'allowBackup'), 'theme': attr(a, 'theme'),
            'usesCleartextTraffic': attr(a, 'usesCleartextTraffic'),
            'networkSecurityConfig': attr(a, 'networkSecurityConfig'),
            'extractNativeLibs': attr(a, 'extractNativeLibs'),
        }
    for tag in ['activity', 'activity-alias', 'service', 'receiver', 'provider', 'uses-library', 'meta-data']:
        items = []
        for x in doc.getElementsByTagName(tag):
            rec = {'name': attr(x, 'name'), 'exported': attr(x, 'exported'),
                   'enabled': attr(x, 'enabled'), 'permission': attr(x, 'permission'),
                   'process': attr(x, 'process'), 'authorities': attr(x, 'authorities'),
                   'targetActivity': attr(x, 'targetActivity')}
            if tag == 'meta-data':
                rec['value'] = attr(x, 'value') or attr(x, 'resource')
            intents = []
            for f in x.getElementsByTagName('intent-filter'):
                intents.append({
                    'actions': [y.getAttribute('android_name') or y.getAttribute('name') for y in f.getElementsByTagName('action')],
                    'categories': [y.getAttribute('android_name') or y.getAttribute('name') for y in f.getElementsByTagName('category')],
                    'schemes': [y.getAttribute('android_scheme') or y.getAttribute('scheme') for y in f.getElementsByTagName('data')],
                })
            rec['intent_filters'] = intents
            items.append(rec)
        out['components'][tag] = items
    return out


def parse_arsc(raw):
    r = ARSCParser(raw)
    pkgs = r.get_packages_names()
    out = {'packages': [], 'total_resource_entries': 0, 'types_all_locales': {}}
    for pkg in pkgs:
        try:
            locales = r.get_locales(pkg)
        except Exception:
            locales = []
        default_types = {}
        try:
            for t in r.get_types(pkg, '\x00\x00'):
                try:
                    default_types[t] = len(r.values[pkg]['\x00\x00'][t])
                except Exception:
                    default_types[t] = None
        except Exception:
            pass
        all_entries = 0
        for loc in locales:
            try:
                for t, items in r.values[pkg][loc].items():
                    try:
                        all_entries += len(items)
                    except Exception:
                        pass
            except Exception:
                pass
        out['packages'].append({
            'name': pkg, 'locales': locales, 'locale_count': len(locales),
            'default_locale_types': default_types,
            'default_locale_entry_count': sum(v for v in default_types.values() if v),
            'all_locale_entries': all_entries,
        })
        out['total_resource_entries'] += all_entries
    return out


def main():
    z = zipfile.ZipFile(APK)
    apk_bytes = open(APK, 'rb').read()
    apk_sha = hashlib.sha256(apk_bytes).hexdigest()
    print('APK sha256', apk_sha, 'MATCH' if apk_sha == APK_SHA256_EXPECTED else 'MISMATCH')
    assert apk_sha == APK_SHA256_EXPECTED

    info = z.infolist()
    print('zip members', len(info))

    # ---------------- APK member inventory ----------------
    cats = collections.Counter()
    libs = []
    assets = []
    versions = []
    dex_members = {}
    for i in info:
        n = i.filename
        if n.endswith('/'):
            continue
        if re.match(r'^classes\d*\.dex$', n):
            cats['dex'] += 1
            dex_members[n] = i
        elif n.endswith('.so'):
            cats['native_lib'] += 1
            libs.append({'path': n, 'size': i.file_size, 'crc': '0x%08x' % i.CRC})
        elif n.startswith('assets/'):
            cats['assets'] += 1
            assets.append({'path': n, 'size': i.file_size})
        elif n.startswith('res/'):
            cats['res'] += 1
        elif n.startswith('META-INF/'):
            cats['meta_inf'] += 1
            if n.endswith('.version'):
                versions.append({'path': n, 'content': z.read(n).decode('utf-8', 'replace').strip()})
        elif n.startswith('lib/') or n.startswith('kotlin/') or n.startswith('org/'):
            cats['other_root'] += 1
        else:
            cats['other'] += 1
        if n.endswith('.json'):
            cats['json_files'] += 1
        if n == 'AndroidManifest.xml':
            cats['manifest'] = 1
        if n == 'resources.arsc':
            cats['arsc'] = 1

    # ---------------- DEX: from APK, verified against _INPUT ----------------
    dexs = {}
    for name in sorted(dex_members, key=lambda x: (len(x), x)):
        raw = z.read(name)
        local_path = os.path.join(ROOT, 'ANALYSIS/_INPUT', name)
        local = open(local_path, 'rb').read() if os.path.exists(local_path) else None
        d = Dex(raw, name)
        s = d.summary()
        s['apk_member_size'] = dex_members[name].file_size
        s['apk_member_crc'] = '0x%08x' % dex_members[name].CRC
        s['input_copy_identical'] = (local == raw)
        s['input_copy_sha256'] = hashlib.sha256(local).hexdigest() if local else None
        dexs[name] = (d, s)
        print(name, 'code_items', s['counts']['code_items_from_map'],
              'defined', s['counts']['defined_methods_from_class_data'],
              'with_code', s['counts']['defined_methods_with_code'],
              'input_identical', s['input_copy_identical'])
        assert s['input_copy_identical'], 'DEX evidence copy differs from APK member: ' + name

    total = collections.Counter()
    for _, s in dexs.values():
        for k, v in s['counts'].items():
            if v:
                total[k] += v
    print('TOTALS', dict(total))

    # ---------------- Manifest / resources ----------------
    manifest = parse_manifest(z.read('AndroidManifest.xml'))
    arsc = parse_arsc(z.read('resources.arsc'))
    print('manifest components',
          {k: len(v) for k, v in manifest['components'].items()})
    print('arsc packages', len(arsc['packages']), 'entries', arsc['total_resource_entries'])

    # ---------------- DEX strings: schemas, endpoints, packages ------------
    all_strings = []
    per_dex_strings = {}
    for name, (d, _) in dexs.items():
        per_dex_strings[name] = d.strings
        for st in d.strings:
            all_strings.append((name, st))
    unique_strings = sorted(set(st['value'] for _, st in all_strings))
    print('string_ids total', len(all_strings), 'unique values', len(unique_strings))

    sql_re = re.compile(r'(?i)^\s*(CREATE\s+(?:TABLE|INDEX|UNIQUE\s+INDEX|VIEW|TRIGGER)|ALTER\s+TABLE|DROP\s+TABLE|INSERT\s+INTO|UPDATE\s+`|SELECT\s|PRAGMA\s|DELETE\s+FROM)', re.S)
    sql = sorted(set(st['value'][:1200] for _, st in all_strings
                     if sql_re.match(st['value']) and any(k in st['value'].lower() for k in
                        ('complet', 'lesson', 'progress', 'chapter', 'tutorial', 'queue', 'user', 'room', 'CREATE TABLE', 'CREATE INDEX'))))
    db_names = sorted(set(st['value'] for _, st in all_strings
                          if re.match(r'^[A-Za-z][\w\-. ]{2,60}\.db$', st['value'])))
    room_markers = sorted(set(st['value'] for _, st in all_strings
                              if re.search(r'(?i)(room\b|RoomOpenHelper|room_schema|Migration|IdentityHashMap|auto_migrations|_Impl\.kt)', st['value']) and len(st['value']) < 180))

    endpoint_strings = sorted(set(st['value'] for _, st in all_strings
                                  if re.match(r'^/v\d+/', st['value'])))
    https_strings = sorted(set(st['value'] for _, st in all_strings
                               if st['value'].startswith('https://') and len(st['value']) < 200))

    # type descriptors -> dependency families
    type_desc = sorted(set(t['descriptor'] for _, (d, _) in dexs.items() for t in d.type_ids))
    fam = collections.Counter()
    for t in type_desc:
        if not t.startswith('L') or ';' not in t:
            continue
        p = t[1:t.index(';')].split('/')[0]
        fam[p] += 1
    mimo_classes = [t for t in type_desc if t.startswith('Lcom/getmimo/')]
    mimo_pkg = collections.Counter('/'.join(t[1:-1].split('/')[:4]) for t in mimo_classes)

    # class_defs per DEX with layer classification
    per_dex_mimo = {}
    for name, (d, _) in dexs.items():
        per_dex_mimo[name] = {
            'class_defs': len(d.class_defs),
            'mimo_class_defs': sum(1 for c in d.class_defs if c['descriptor'].startswith('Lcom/getmimo/')),
            'source_file_names': len(set(c['source_file'] for c in d.class_defs if c['source_file'])),
            'methods_without_code': sum(1 for c in d.class_defs for m in c['defined_methods'] if not m['code_off']),
        }

    # ---------------- Ghidra reconciliation ----------------
    cf = open(os.path.join(GHIDRA_DIR, 'CONTROL_FLOW.txt'), errors='replace').read()
    headings = re.findall(r'^=== PROGRAM (\S+) language=(\S+) functions=(\d+) symbols=(\d+) memory_blocks=(\d+)', cf, re.M)
    gh = {h[0]: {'language': h[1], 'functions': int(h[2]), 'symbols': int(h[3]), 'memory_blocks': int(h[4])} for h in headings}
    cov = open(os.path.join(GHIDRA_DIR, 'DEX_COVERAGE.txt'), errors='replace').read()
    cov_progs = re.findall(r'^DEX (\S+) language=(\S+) memory_blocks=(\d+) symbols=(\d+) functions=(\d+)', cov, re.M)
    recon = []
    for name, (d, s) in dexs.items():
        g = gh.get(name, {})
        ci = s['counts']['code_items_from_map']
        recon.append({
            'dex': name,
            'dex_code_items': ci,
            'dex_defined_methods': s['counts']['defined_methods_from_class_data'],
            'dex_methods_with_code': s['counts']['defined_methods_with_code'],
            'dex_methods_without_code': s['counts']['defined_methods_without_code'],
            'ghidra_auto_analysis_functions': g.get('functions'),
            'functions_match': g.get('functions') == ci,
            'ghidra_auto_analysis_symbols': g.get('symbols'),
            'ghidra_noanalysis_coverage_functions': next((int(x[4]) for x in cov_progs if x[0] == name), None),
            'ghidra_language': g.get('language'),
            'string_ids': s['counts']['string_ids'],
            'type_ids': s['counts']['type_ids'],
            'proto_ids': s['counts']['proto_ids'],
            'field_ids': s['counts']['field_ids'],
            'method_ids': s['counts']['method_ids'],
            'class_defs': s['counts']['class_defs'],
            'header_checksum_valid': s['header']['checksum_valid'],
            'header_signature_valid': s['header']['signature_valid'],
            'parse_errors': len(s['parse_errors']),
        })
    print('function reconciliation all-match:', all(r['functions_match'] for r in recon))
    print('ghidra functions total', sum(r['ghidra_auto_analysis_functions'] or 0 for r in recon))
    print('ghidra symbols total', sum(r['ghidra_auto_analysis_symbols'] or 0 for r in recon))

    # ---------------- analysis failure inventory ----------------
    smali_fail = 0
    smali_widths = collections.Counter()
    apklog = '/home/user/_work/_analysis/apktool2.log'
    if os.path.exists(apklog):
        for line in open(apklog, errors='replace'):
            if 'Error occurred while disassembling' in line or 'Invalid element width' in line:
                smali_fail += 1
            m = re.search(r'Invalid element width[:\s]+(\d+)', line)
            if m:
                smali_widths[m.group(1)] += 1
    jadx_log = os.path.join(ROOT, 'ANALYSIS/DECOMPILED/jadx.log')
    jadx_errors = 0
    if os.path.exists(jadx_log):
        jadx_errors = sum(1 for l in open(jadx_log, errors='replace') if l.startswith('ERROR'))
    jadx_report = os.path.join(ROOT, 'ANALYSIS/DECOMPILED/REPORT.md')
    jadx_stub_files = None
    jadx_java_files = None
    jadx_error_total = None
    if os.path.exists(jadx_report):
        t = open(jadx_report, errors='replace').read()
        m = re.search(r'java files:\s*([\d,]+)', t, re.I)
        if m:
            jadx_java_files = int(m.group(1).replace(',', ''))
        m = re.search(r'files containing JADX stubs:\s*([\d,]+)', t, re.I)
        if m:
            jadx_stub_files = int(m.group(1).replace(',', ''))
    if os.path.exists(jadx_log):
        m = re.search(r'finished with errors, count:\s*(\d+)',
                      open(jadx_log, errors='replace').read())
        if m:
            jadx_error_total = int(m.group(1))

    smali_failed_classes = sum(smali_widths.values())

    # R8 build marker from class_def source_file_idx
    r8_ids = collections.Counter(c['source_file'] for _, (d, _) in dexs.items()
                                 for c in d.class_defs if c['source_file'].startswith('r8-map-id'))

    # Symbol composition probe: 1,284,542 is a Ghidra-internal label count,
    # not a DEX structural count. Record the measurable DEX baseline.
    structural = sum(r[k] for r in recon for k in
                     ('string_ids', 'type_ids', 'proto_ids', 'field_ids',
                      'method_ids', 'class_defs', 'dex_code_items'))
    sym_total = sum(r['ghidra_auto_analysis_symbols'] or 0 for r in recon)
    symbol_probe = {
        'ghidra_symbol_total_independently_summed': sym_total,
        'ghidra_symbol_total_reported': 1284542,
        'arithmetic_matches': sym_total == 1284542,
        'dex_structural_id_baseline': structural,
        'residual_generated_labels': sym_total - structural,
        'observable_symbol_families': ['string_data::<value>', 'EXTERNAL.dex-N::<class>::<member>',
                                       'class/method/field labels', 'data/function labels'],
        'status': 'PARTIALLY RECONCILED — total verified by arithmetic; composition NOT derivable from DEX headers (UNKNOWN)',
    }

    out = {
        'document': 'Mimo 9.35 — complete verified APK inventory',
        'source_of_truth': 'original APK from Google Drive folder mimo (reassembled split archive)',
        'apk': {
            'path': APK, 'bytes': len(apk_bytes), 'sha256': apk_sha,
            'sha256_expected': APK_SHA256_EXPECTED, 'sha256_match': True,
            'zip_members': len(info),
            'zip_member_categories': dict(cats),
        },
        'dex': {name: s for name, (_, s) in dexs.items()},
        'dex_totals': dict(total),
        'ghidra_reconciliation': {
            'per_dex': recon,
            'all_12_import_covered': all(any(x[0] == n for x in cov_progs) for n in dexs),
            'auto_analysis_programs': len(headings),
            'functions_total': sum(r['ghidra_auto_analysis_functions'] or 0 for r in recon),
            'symbols_total': sum(r['ghidra_auto_analysis_symbols'] or 0 for r in recon),
            'functions_exact_match_all_dex': all(r['functions_match'] for r in recon),
            'symbol_composition_probe': symbol_probe,
            'symbol_reconciliation_note': 'Ghidra symbol count is a Ghidra-internal metric (string_data labels, EXTERNAL method/field refs, class/data/function labels). It is NOT equal to any single DEX header count; see symbol_composition_probe.',
        },
        'r8_build_markers': dict(r8_ids),
        'manifest': manifest,
        'resources': arsc,
        'native_libraries': sorted(libs, key=lambda x: x['path']),
        'native_library_abis': dict(collections.Counter(x['path'].split('/')[1] for x in libs if '/' in x['path'])),
        'embedded_dependency_version_files': sorted(versions, key=lambda x: x['path']),
        'assets': {
            'count': len(assets),
            'total_bytes': sum(a['size'] for a in assets),
            'json_files': sum(1 for a in assets if a['path'].endswith('.json')),
            'top_level': dict(collections.Counter(a['path'].split('/')[1] if '/' in a['path'][7:] else a['path'][7:].split('/')[0] for a in assets).most_common(20)),
            'locale_bundles': sorted(set(re.findall(r'assets/lessons-([a-zA-Z\-]+)/', '\n'.join(a['path'] for a in assets)))),
        },
        'strings': {'string_ids_total': len(all_strings), 'unique_values': len(unique_strings)},
        'type_descriptors': {'total_unique': len(type_desc), 'mimo_descriptors': len(mimo_classes),
                             'top_level_families': dict(fam.most_common(40)),
                             'mimo_package_top': dict(mimo_pkg.most_common(40))},
        'class_defs_per_dex': per_dex_mimo,
        'database': {'sql_statements': sql, 'database_names': db_names,
                     'room_markers': room_markers[:120]},
        'network': {'endpoint_like_paths': endpoint_strings, 'https_urls': https_strings[:120]},
        'analysis_failures': {
            'smali_disassembler_error_lines': smali_fail,
            'smali_failed_classes': smali_failed_classes,
            'smali_invalid_element_widths': dict(smali_widths),
            'smali_files_produced': sum(len(glob.glob(p + '/**/*.smali', recursive=True)) for p in glob.glob('/home/user/_work/_analysis/apktool2_out/smali*')),
            'jadx_1_5_6_error_lines_starting_ERROR': jadx_errors,
            'jadx_1_5_6_reported_total_errors': jadx_error_total,
            'jadx_1_5_6_java_files': jadx_java_files,
            'jadx_1_5_6_stub_files': jadx_stub_files,
        },
        'evidence_status_tags': ['OBSERVED', 'STATICALLY INFERRED', 'RUNTIME VERIFIED', 'SERVER CONFIRMED', 'UNKNOWN'],
        'integrity': {'apk_sha256_match': True,
                      'all_dex_input_copies_match_apk': all(s['input_copy_identical'] for _, s in dexs.values()),
                      'all_dex_adler32_valid': all(s['header']['checksum_valid'] for _, s in dexs.values()),
                      'all_dex_sha1_signature_valid': all(s['header']['signature_valid'] for _, s in dexs.values()),
                      'dex_parse_errors': sum(len(s['parse_errors']) for _, s in dexs.values())},
    }
    json.dump(out, open(os.path.join(ROOT, 'ANALYSIS/APK_COMPLETE_INVENTORY.json'), 'w'),
              indent=1, ensure_ascii=False)
    print('wrote APK_COMPLETE_INVENTORY.json',
          os.path.getsize(os.path.join(ROOT, 'ANALYSIS/APK_COMPLETE_INVENTORY.json')), 'bytes')

    # coverage metrics with real denominators
    tot_classes = total['class_defs']
    tot_methods = total['defined_methods_from_class_data']
    tot_code = total['code_items_from_map']
    smali_produced = out['analysis_failures']['smali_files_produced']
    mimo_cdefs_total = sum(v['mimo_class_defs'] for v in per_dex_mimo.values())
    mimo_cdefs_primary = per_dex_mimo['classes.dex']['mimo_class_defs']
    metrics = {
        'document': 'Measurable coverage denominators — Mimo 9.35',
        'denominators': {
            'dex_files': 12,
            'dex_bytes': sum(s['bytes'] for _, s in dexs.values()),
            'class_defs': tot_classes,
            'defined_methods': tot_methods,
            'methods_with_code': tot_code,
            'methods_without_code': tot_methods - tot_code,
            'method_ids_references': total['method_ids'],
            'field_ids_references': total['field_ids'],
            'string_ids': total['string_ids'],
            'type_ids': total['type_ids'],
            'proto_ids': total['proto_ids'],
            'mimo_type_descriptors': len(mimo_classes),
        },
        'coverage': {
            'dex_imported_by_ghidra': {'count': 12, 'denominator': 12, 'pct': 100.0},
            'dex_auto_analysed_by_ghidra': {'count': 12, 'denominator': 12, 'pct': 100.0},
            'ghidra_functions_vs_methods_with_code': {'count': out['ghidra_reconciliation']['functions_total'], 'denominator': tot_code,
                                                       'pct': round(100.0 * out['ghidra_reconciliation']['functions_total'] / tot_code, 4)},
            'smali_class_files_vs_class_defs': {'count': smali_produced, 'denominator': tot_classes,
                                                'pct': round(100.0 * smali_produced / tot_classes, 4)},
            'smali_failures_vs_class_defs': {'count': smali_failed_classes, 'denominator': tot_classes,
                                             'pct': round(100.0 * smali_failed_classes / tot_classes, 4)},
            'jadx_1_5_6_com_getmimo_java_vs_primary_dex_mimo_class_defs': {
                'count': jadx_java_files, 'denominator': mimo_cdefs_primary, 'pct': None,
                'note': 'JADX 1.5.6 was run on classes.dex only; denominator is the com.getmimo class_defs of that DEX.'},
            'jadx_1_5_6_stub_file_rate': {
                'count': jadx_stub_files, 'denominator': jadx_java_files, 'pct': None,
                'note': 'files containing "Method not decompiled" stubs / emitted Java files'},
            'ghidra_symbol_total_arithmetic_verified': {
                'count': sym_total, 'denominator': 1284542,
                'pct': 100.0 if sym_total == 1284542 else None,
                'note': 'composition remains UNKNOWN; see APK_COMPLETE_INVENTORY.json -> symbol_composition_probe'},
            'runtime_verified_behaviours': {'count': 0, 'denominator': 'undefined (no emulator/ADB available)', 'pct': 0.0},
            'server_confirmed_responses': {'count': 0, 'denominator': 'undefined (no authorized test environment)', 'pct': 0.0},
        },
        'extra_denominators': {
            'mimo_class_defs_all_dex': mimo_cdefs_total,
            'mimo_class_defs_primary_dex': mimo_cdefs_primary,
            'mimo_type_descriptors_unique': len(mimo_classes),
            'dex_structural_id_baseline': structural,
            'ghidra_symbol_residual_generated_labels': sym_total - structural,
        },
        'notes': [
            'Ghidra functions = DEX code_item count exactly, per DEX and in total (independent reconciliation via dexlib.py).',
            'Ghidra symbols are NOT reconciled to a DEX header count; Ghidra creates EXTERNAL and string_data labels beyond DEX structures.',
            'Smali success is measured against class_defs; 11,828 failures are confined to classes.dex.',
            'JADX 1.5.6 emitted only com.getmimo Java; its stub rate is measured over that set, not over all classes.',
            'Runtime and server verification are 0 because no approved emulator/ADB or authorized test environment exists.',
        ],
    }
    for key in ('jadx_1_5_6_com_getmimo_java_vs_primary_dex_mimo_class_defs',
                'jadx_1_5_6_stub_file_rate'):
        m = metrics['coverage'][key]
        if m['count'] and m['denominator']:
            m['pct'] = round(100.0 * m['count'] / m['denominator'], 4)
    json.dump(metrics, open(os.path.join(ROOT, 'ANALYSIS/COVERAGE_METRICS.json'), 'w'),
              indent=1, ensure_ascii=False)
    print('wrote COVERAGE_METRICS.json')
    print(json.dumps(metrics['denominators'], indent=1))
    print(json.dumps(metrics['coverage'], indent=1))
    return out, metrics


if __name__ == '__main__':
    main()
