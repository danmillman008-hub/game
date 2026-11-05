"""MISSION 02 — extract REAL numeric constants from the Learning Path composable.

Targets Lcom/getmimo/ui/path/map/k; (obfuscated Views.kt) and sibling path-map
classes. For every const/high16/const float literal, resolve the NEXT invoke's
full class+method signature so the value is tied to a concrete Compose API.

Read-only. Script in ANALYSIS/_TOOLCHAIN/. Output PATH_GEOMETRY_CONSTANTS.json.
"""

import os
import json
import struct
import collections
from dexlib import Dex
from dex_bytecode import decode_reachable, INVOKE, CONST

A = '/home/user/game/ANALYSIS'
d = Dex(open(A + '/_INPUT/classes.dex', 'rb').read(), 'classes.dex')


def f32(v):
    try:
        return struct.unpack('<f', struct.pack('<I', v & 0xffffffff))[0]
    except Exception:
        return None


results = []
for c in d.class_defs:
    cls = c['descriptor']
    if not ('/ui/path/map/' in cls or '/interactors/path/' in cls):
        continue
    for m in c['defined_methods']:
        if not m['code_off']:
            continue
        rows = decode_reachable(d, m['code_off'])
        for j, (o, op, idx, lit, units) in enumerate(rows):
            if op not in CONST or lit is None:
                continue
            v = f32(lit) if op in (0x14, 0x15) else None
            # only plausible finite float literals (dp / angles / fractions)
            if v is None or not (-1e6 < v < 1e6) or v != v:
                continue
            if abs(v) < 0.0001 and op == 0x15:
                continue
            following = []
            for (o2, op2, idx2, lit2, u2) in rows[j + 1:j + 8]:
                if op2 in INVOKE and idx2 is not None and idx2 < len(d.method_ids):
                    mi = d.method_ids[idx2]
                    following.append({'offset': '0x%x' % o2,
                                      'opcode': INVOKE[op2],
                                      'callee_class': mi['class'],
                                      'callee_signature': mi['signature']})
                if len(following) >= 3:
                    break
            results.append({
                'dex': 'classes.dex',
                'class': cls,
                'method': m['signature'],
                'insn_offset': '0x%x' % o,
                'opcode': CONST[op],
                'raw_bits': '0x%08x' % (lit & 0xffffffff),
                'literal_int': lit,
                'float32_value': round(v, 6),
                'following_invokes': following,
                'status': 'OBSERVED (DEX literal + following call); semantic role STATICALLY INFERRED',
            })

json.dump({
    'document': 'MISSION 02 — numeric literals in Learning Path composable bytecode',
    'source_of_truth': 'APK sha256 48ce1740…; classes.dex',
    'tool_and_method': 'dexlib.py + dex_bytecode.decode_reachable (control-flow aware)',
    'status': 'OBSERVED for the literal and its offset; NOT RUNTIME VERIFIED',
    'warning': 'A float literal near a Compose call is NOT proof of a dp value or a spacing formula. '
               'Without runtime/UI hierarchy and without full semantic decompilation, '
               'the mapping value -> visual distance remains UNKNOWN.',
    'target_classes': sorted(set(r['class'] for r in results)),
    'literal_count': len(results),
    'constants': results,
}, open(A + '/PATH_GEOMETRY_CONSTANTS.json', 'w'), indent=1, ensure_ascii=False)

print('constants', len(results))
print('classes', sorted(set(r['class'] for r in results)))
agg = collections.Counter(r['float32_value'] for r in results)
print('values', agg.most_common(30))
print('wrote', os.path.getsize(A + '/PATH_GEOMETRY_CONSTANTS.json'), 'bytes')
