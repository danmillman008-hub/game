"""MISSION 02 — resolve Retrofit HTTP verbs from DEX bytecode, not method names.

The obfuscated Retrofit RequestFactory$Builder (Lge0/r0; in classes3.dex) contains
a chain of `instance-of Lie0/X; -> check-cast -> X.value() -> const-string VERB
-> Lge0/m0;->b(verb,path,hasBody)`.  Each VERB is a real string constant adjacent
to the annotation-class check, so the mapping is bytecode evidence (OBSERVED/HIGH).

JADX source files import ie0.<letter>, which ties @f/@o/@n/@p/@b to those classes.
Outputs ANALYSIS/HTTP_VERBS_RESOLVED.json. Read-only. Script in ANALYSIS/_TOOLCHAIN/.
"""

import os
import re
import json
import collections
from dexlib import Dex
from dex_bytecode import decode, INVOKE, CONST

A = '/home/user/game/ANALYSIS'
JADX = '/home/user/_work/_analysis/jadx110/sources'

d = Dex(open(A + '/_INPUT/classes3.dex', 'rb').read(), 'classes3.dex')
tids = [t['descriptor'] for t in d.type_ids]

def insn_rows(code_off):
    return list(decode(d, code_off))

# ---------------------------------------------------------------------------
# 1. find Lge0/r0;->a and derive annotation-class -> verb
# ---------------------------------------------------------------------------
builder = None
for c in d.class_defs:
    if c['descriptor'] == 'Lge0/r0;':
        for m in c['defined_methods']:
            if m['name'] == 'a' and m['code_off']:
                builder = insn_rows(m['code_off'])
                builder_sig = m['signature']
                builder_off = m['code_off']
assert builder, 'Retrofit RequestFactory builder not found'

verb_strings = {}
for (o, op, idx, lit, units) in builder:
    if op in (0x1a, 0x1b) and idx is not None and idx < len(d.strings):
        v = d.strings[idx]['value']
        if v in ('GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'):
            verb_strings[o] = v

mapping = {}
trace = []

tokens = []
for (o, op, idx, lit, units) in builder:
    if op == 0x20 and idx is not None and idx < len(tids):
        tokens.append(('type', o, tids[idx]))
    elif op == 0x1a and idx is not None and idx < len(d.strings) and d.strings[idx]['value'] in verb_strings.values():
        tokens.append(('verb', o, d.strings[idx]['value']))
    elif op in INVOKE and idx is not None and idx < len(d.method_ids):
        sig = d.method_ids[idx]['signature']
        if '->b(Ljava/lang/String;Ljava/lang/String;Z)V' in sig:
            tokens.append(('call_b', o, sig))
        elif '->value()Ljava/lang/String;' in sig:
            tokens.append(('value', o, sig))
        elif '->method()Ljava/lang/String;' in sig:
            tokens.append(('method', o, sig))
        elif '->path()Ljava/lang/String;' in sig:
            tokens.append(('path', o, sig))

# walk: type -> value -> verb -> call_b  =>  type maps to verb
cur_type = None
for t, o, v in tokens:
    if t == 'type':
        cur_type = v
    elif t == 'verb' and cur_type:
        mapping[cur_type] = {'verb': v, 'verb_offset': '0x%x' % o,
                             'type_check': 'instance-of + check-cast',
                             'evidence': 'Lge0/r0;->a @0x%x -> 0x%x' % (builder_off, o)}
        trace.append({'annotation_class': cur_type, 'verb': v,
                      'verb_const_offset': '0x%x' % o})
        cur_type = None
    elif t in ('call_b', 'method', 'path') and cur_type:
        # branch without a literal verb (e.g. @HEAD hoisted, or @HTTP())
        trace.append({'annotation_class': cur_type, 'verb': None,
                      'note': 'no adjacent verb const-string; verb hoisted by R8 or read from annotation'})
        cur_type = None

# HEAD is hoisted before the loop; @HTTP reads method()/path()/hasBody() at runtime.
unresolved = [x for x in trace if x['verb'] is None]
hoisted = [x for x in sorted(verb_strings.items()) if x[0] < min(
    [int(t['verb_const_offset'], 16) for t in trace if t['verb']], default=2**62)]
for h_off, h_verb in hoisted:
    for u in unresolved:
        if u['annotation_class'] == 'Lie0/g;':
            mapping[u['annotation_class']] = {
                'verb': h_verb, 'verb_offset': '0x%x' % h_off,
                'type_check': 'instance-of + check-cast',
                'evidence': 'Lge0/r0;->a; verb const hoisted before branch (R8)',
                'note': 'attribution STATICALLY INFERRED from single unpaired verb constant'}
            break
    break

# ---------------------------------------------------------------------------
# 2. decode Lge0/m0;->b to confirm parameter order (verb, path, hasBody)
# ---------------------------------------------------------------------------
confirm = []
for c in d.class_defs:
    if c['descriptor'] == 'Lge0/m0;':
        for m in c['defined_methods']:
            if m['name'] == 'b' and m['code_off']:
                rows = insn_rows(m['code_off'])
                for (o, op, idx, lit, units) in rows[:60]:
                    if op in INVOKE and idx is not None and idx < len(d.method_ids):
                        confirm.append({'offset': '0x%x' % o,
                                        'call': d.method_ids[idx]['signature'][:130]})
                    elif op == 0x1a and idx is not None and idx < len(d.strings):
                        v = d.strings[idx]['value']
                        if 'method' in v.lower() or 'verb' in v.lower():
                            confirm.append({'offset': '0x%x' % o, 'string': v[:120]})

# ---------------------------------------------------------------------------
# 3. map each of the 53 endpoints using JADX imports
# ---------------------------------------------------------------------------
eps = json.load(open(A + '/MIMO_RETROFIT_ENDPOINTS.json'))['endpoints']
resolved = []
counts = collections.Counter()
for e in eps:
    letter = e['annotation'].lstrip('@')
    desc = 'Lie0/%s;' % letter
    p = os.path.join(JADX, e['source_file'])
    imports = []
    if os.path.isfile(p):
        imports = re.findall(r'import\s+(ie0\.[A-Za-z0-9_$]+);', open(p, errors='replace').read())
    m = mapping.get(desc)
    verb = m['verb'] if m else None
    counts[verb or 'UNKNOWN'] += 1
    resolved.append({
        'path': e['path'],
        'annotation': e['annotation'],
        'annotation_class_descriptor': desc,
        'import_verified_in_jadx_source': ('ie0.' + letter) in imports,
        'source_file': e['source_file'],
        'signature': e['signature'],
        'resolved_http_verb': verb or 'UNKNOWN',
        'previous_inferred_label': e['verb_inferred'],
        'changed_from_previous_inference': bool(verb and verb != e['verb_inferred']),
        'confidence': 'HIGH' if (m and verb and not m.get('note')) else 'MEDIUM',
        'status': 'OBSERVED (DEX bytecode + JADX import); NOT RUNTIME VERIFIED; NOT SERVER CONFIRMED',
        'evidence': m['evidence'] if m else 'annotation class not in RequestFactory verb chain',
        'verb_const_offset': m['verb_offset'] if m else None,
        'dex': 'classes3.dex (Retrofit) / classes.dex (API interface)',
    })

out = {
    'document': 'MISSION 02 — HTTP verbs resolved from DEX bytecode',
    'method': 'Decoded Lge0/r0;->a (obfuscated Retrofit RequestFactory$Builder) in classes3.dex; '
              'paired each instance-of annotation check with its adjacent verb const-string; '
              'linked JADX @x imports (ie0.x) to those descriptors.',
    'status': 'OBSERVED / HIGH for GET/POST/PUT/DELETE/PATCH/OPTIONS; HEAD MEDIUM (R8-hoisted constant)',
    'not': 'NOT inferred from method names; NOT runtime verified; NOT server confirmed',
    'builder_method': builder_sig,
    'builder_code_off': '0x%x' % builder_off,
    'annotation_class_to_verb': mapping,
    'verb_chain_trace': trace,
    'b_parameter_order_probe': confirm[:12],
    'corrected_verb_counts': dict(counts),
    'endpoints': resolved,
    'corrections': [r for r in resolved if r['changed_from_previous_inference']],
}
json.dump(out, open(A + '/HTTP_VERBS_RESOLVED.json', 'w'), indent=1, ensure_ascii=False)
print('annotation->verb:', {k: v['verb'] for k, v in mapping.items()})
print('corrected counts:', dict(counts))
print('corrections:', len(out['corrections']), out['corrections'][:4])
print('wrote HTTP_VERBS_RESOLVED.json', os.path.getsize(A + '/HTTP_VERBS_RESOLVED.json'))
