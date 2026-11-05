"""MISSION 02 — read-only Dalvik instruction decoder.

Decodes code_item instruction streams from the 12 verified DEX files and emits
REAL method-call edges, field-access edges, string constants and numeric literals.

This is NOT a re-run of the mission-01 inventory: it resolves invoke-*/iget/iput
targets from bytecode, which the earlier class-level graph could not do.

No new tools are installed; only ANALYSIS/_TOOLCHAIN/ scripts are added.
"""

import os
import re
import struct
import glob
import json
import collections

A = '/home/user/game/ANALYSIS'
OUT = os.path.join(A, 'DEX_BYTECODE_EVIDENCE.json')

# ---------------------------------------------------------------------------
# Dalvik instruction widths, in 16-bit code units (dex spec, opcode order).
# ---------------------------------------------------------------------------
L = [1] * 256


def _set(lo, hi, n):
    for o in range(lo, hi + 1):
        L[o] = n


_set(0x00, 0x0f, 1)          # nop, move*, move-result*, return*
L[0x02] = L[0x05] = L[0x08] = 2          # move/from16, move-wide/from16, move-object/from16
L[0x03] = L[0x06] = L[0x09] = 3          # move/16 variants
L[0x12] = 1                               # const/4 (11n)
L[0x13] = 2                               # const/16 (21s)
L[0x14] = 3                               # const (31i)
L[0x15] = 2                               # const/high16 (21h)
L[0x16] = 2                               # const-wide/16 (21s)
L[0x17] = 3                               # const-wide/32 (31i)
L[0x18] = 5                               # const-wide (51l)
L[0x19] = 2                               # const-wide/high16 (21h)
L[0x1a] = 2                               # const-string (21c)
L[0x1b] = 3                               # const-string/jumbo (31c)
L[0x1c] = 2                               # const-class (21c)
_set(0x1d, 0x1e, 1)
L[0x1f] = 2                               # check-cast (21c)
L[0x20] = 2                               # instance-of (22c)
L[0x21] = 1                               # array-length
L[0x22] = 2                               # new-instance (21c)
L[0x23] = 2                               # new-array (22c)
L[0x24] = 3                               # filled-new-array (35c)
L[0x25] = 3                               # filled-new-array/range (3rc)
L[0x26] = 3                               # fill-array-data (31t)
L[0x27] = 1                               # throw
L[0x28] = 1                               # goto
L[0x29] = 2                               # goto/16
L[0x2a] = 3                               # goto/32
L[0x2b] = 3                               # packed-switch
L[0x2c] = 3                               # sparse-switch
_set(0x2d, 0x3d, 2)                       # cmp*, if-*
_set(0x3e, 0x43, 1)                       # unused
_set(0x44, 0x51, 2)                       # aget*/aput* (23x)
_set(0x52, 0x5f, 2)                       # iget*/iput* (22c)
_set(0x60, 0x6d, 2)                       # sget*/sput* (21c)
_set(0x6e, 0x72, 3)                       # invoke-* 35c
L[0x73] = 1                               # unused
_set(0x74, 0x78, 3)                       # invoke-*/range 3rc
_set(0x79, 0x8f, 1)                       # unused(2) + unary ops (12x)
_set(0x90, 0xaf, 2)                       # binop 23x
_set(0xb0, 0xcf, 1)                       # binop/2addr 12x
_set(0xd0, 0xd7, 2)                       # binop/lit16 22s
_set(0xd8, 0xe2, 2)                       # binop/lit8 22b
_set(0xe3, 0xf9, 1)                       # unused
L[0xfa] = 4                               # invoke-polymorphic 45cc
L[0xfb] = 4                               # invoke-polymorphic/range 4rcc
L[0xfc] = 3                               # invoke-custom 35c
L[0xfd] = 3                               # invoke-custom/range 3rc

INVOKE = {0x6e: 'invoke-virtual', 0x6f: 'invoke-super', 0x70: 'invoke-direct',
          0x71: 'invoke-static', 0x72: 'invoke-interface',
          0x74: 'invoke-virtual/range', 0x75: 'invoke-super/range',
          0x76: 'invoke-direct/range', 0x77: 'invoke-static/range',
          0x78: 'invoke-interface/range', 0xfa: 'invoke-polymorphic',
          0xfb: 'invoke-polymorphic/range', 0xfc: 'invoke-custom',
          0xfd: 'invoke-custom/range'}
IFIELD = dict((o, 'iget' if o < 0x59 else 'iput') for o in range(0x52, 0x5f + 1))
SFIELD = dict((o, 'sget' if o < 0x67 else 'sput') for o in range(0x60, 0x6d + 1))
CONST = {0x12: 'const/4', 0x13: 'const/16', 0x14: 'const', 0x15: 'const/high16',
         0x16: 'const-wide/16', 0x17: 'const-wide/32', 0x18: 'const-wide',
         0x19: 'const-wide/high16'}


def sx(v, bits):
    return v - (1 << bits) if v & (1 << (bits - 1)) else v


def u2(b, o):
    return struct.unpack_from('<H', b, o)[0]


def decode(d, code_off):
    """Yield (byte_offset, opcode, index_or_None, literal_or_None, raw_units)."""
    ci = d.code_item(code_off)
    off = ci['insns_off']
    n = ci['insns_size']
    b = d.data
    pc = 0
    while pc < n:
        start = off + pc * 2
        if start + 2 > len(b):
            break
        w0 = u2(b, start)
        op = w0 & 0xff
        width = L[op]
        # Pseudo-instructions: nop with a nonzero high byte is a payload whose
        # length is data-dependent. Walking it linearly creates bogus opcodes.
        payload = False
        if op == 0x00 and (w0 >> 8):
            ident = w0 >> 8
            if ident == 0x0100:            # packed-switch-payload
                width = 4 + 2 * u2(b, start + 2)
            elif ident == 0x0200:          # sparse-switch-payload
                width = 2 + 4 * u2(b, start + 2)
            elif ident == 0x0300:          # fill-array-data-payload
                ew = u2(b, start + 2)
                sz = struct.unpack_from('<I', b, start + 4)[0]
                width = 4 + (sz * ew + 1) // 2
            else:
                width = 1
            payload = True
        if width < 1 or pc + width > n:
            break
        units = [] if payload else [struct.unpack_from('<H', b, start + 2 * i)[0]
                                    for i in range(min(width, 5))]
        idx = None
        lit = None
        if op in INVOKE or op in IFIELD or op in SFIELD:
            idx = units[1] if len(units) > 1 else None
        elif op == 0x1a:
            idx = units[1] if len(units) > 1 else None
        elif op == 0x1b:
            idx = (units[1] | (units[2] << 16)) if len(units) > 2 else None
        elif op == 0x1c or op == 0x1f or op == 0x20 or op == 0x22:
            idx = units[1] if len(units) > 1 else None
        elif op == 0x12:
            lit = sx((w0 >> 12) & 0xf, 4)
        elif op == 0x13:
            lit = sx(units[1], 16)
        elif op == 0x14:
            lit = sx(units[1] | (units[2] << 16), 32)
        elif op == 0x15:
            lit = sx(units[1] << 16, 32)
        elif op == 0x16:
            lit = sx(units[1], 16)
        elif op == 0x17:
            lit = sx(units[1] | (units[2] << 16), 32)
        elif op == 0x18:
            v = units[1] | (units[2] << 16) | (units[3] << 32) | (units[4] << 48)
            lit = v - (1 << 64) if v & (1 << 63) else v
        elif op == 0x19:
            lit = sx(units[1] << 48, 64)
        yield start, op, idx, lit, units
        pc += width


def float32(v):
    try:
        return struct.unpack('<f', struct.pack('<I', v & 0xffffffff))[0]
    except Exception:
        return None


def decode_reachable(d, code_off):
    """Decode ONLY reachable instructions (worklist from pc=0).

    Smob-style junk bytes after a terminal return (present in this APK) are
    unreachable and must never be interpreted as opcodes. Branch/switch targets
    are followed so real code is still fully covered.
    """
    import collections
    ci = d.code_item(code_off)
    off, n, b = ci['insns_off'], ci['insns_size'], d.data
    q = collections.deque([0])
    seen = set()
    results = []

    def s32(v):
        return v - (1 << 32) if v & (1 << 31) else v

    while q:
        pc = q.popleft()
        if pc in seen or pc < 0 or pc >= n:
            continue
        seen.add(pc)
        start = off + pc * 2
        if start + 2 > len(b):
            continue
        w0 = u2(b, start)
        op = w0 & 0xff
        width = L[op]
        payload = False
        if op == 0x00 and (w0 >> 8):
            ident = w0 >> 8
            if ident == 0x0100:
                width = 4 + 2 * u2(b, start + 2)
            elif ident == 0x0200:
                width = 2 + 4 * u2(b, start + 2)
            elif ident == 0x0300:
                ew = u2(b, start + 2)
                sz = struct.unpack_from('<I', b, start + 4)[0]
                width = 4 + (sz * ew + 1) // 2
            payload = True
        if width < 1 or pc + width > n:
            continue
        units = [] if payload else [struct.unpack_from('<H', b, start + 2 * i)[0]
                                    for i in range(min(width, 5))]
        if payload:
            continue
        idx = None
        lit = None
        if op in INVOKE or op in IFIELD or op in SFIELD:
            idx = units[1] if len(units) > 1 else None
        elif op == 0x1a:
            idx = units[1] if len(units) > 1 else None
        elif op == 0x1b:
            idx = (units[1] | (units[2] << 16)) if len(units) > 2 else None
        elif op in (0x1c, 0x1f, 0x20, 0x22):
            idx = units[1] if len(units) > 1 else None
        elif op == 0x12:
            lit = sx((w0 >> 12) & 0xf, 4)
        elif op == 0x13:
            lit = sx(units[1], 16)
        elif op == 0x14:
            lit = sx(units[1] | (units[2] << 16), 32)
        elif op == 0x15:
            lit = sx(units[1] << 16, 32)
        elif op == 0x16:
            lit = sx(units[1], 16)
        elif op == 0x17:
            lit = sx(units[1] | (units[2] << 16), 32)
        elif op == 0x18:
            v = units[1] | (units[2] << 16) | (units[3] << 32) | (units[4] << 48)
            lit = v - (1 << 64) if v & (1 << 63) else v
        elif op == 0x19:
            lit = sx(units[1] << 48, 64)
        results.append((start, op, idx, lit, units))

        nxt = [pc + width]
        if op == 0x28:                                   # goto (10t)
            nxt = [pc + sx((w0 >> 8) & 0xff, 8)]
        elif op == 0x29:                                 # goto/16
            nxt = [pc + sx(units[1], 16)]
        elif op == 0x2a:                                 # goto/32
            nxt = [pc + s32(units[1] | (units[2] << 16))]
        elif 0x32 <= op <= 0x3d:                         # if-* / if-*z
            nxt = [pc + width, pc + sx(units[1], 16)]
        elif op in (0x2b, 0x2c):                         # packed/sparse switch
            t = s32(units[1] | (units[2] << 16))
            ppc = pc + t
            if 0 <= ppc < n:
                ps = off + ppc * 2
                pw0 = u2(b, ps)
                if (pw0 >> 8) == 0x0100:
                    sz = u2(b, ps + 2)
                    for i in range(sz):
                        nxt.append(pc + struct.unpack_from('<i', b, ps + 8 + 4 * i)[0])
                elif (pw0 >> 8) == 0x0200:
                    sz = u2(b, ps + 2)
                    for i in range(sz):
                        nxt.append(pc + struct.unpack_from('<i', b, ps + 4 + 4 * sz + 4 * i)[0])
            nxt.append(pc + width)
        elif op in (0x0e, 0x0f, 0x10, 0x11, 0x27):      # return*/throw
            nxt = []
        for x in nxt:
            if 0 <= x < n and x not in seen:
                q.append(x)
    return sorted(results)


def main():
    from dexlib import Dex
    call_agg = collections.defaultdict(lambda: {'n': 0, 'samples': []})
    field_agg = collections.defaultdict(lambda: {'n': 0, 'samples': []})
    external_agg = collections.Counter()
    scenario_edges = []
    string_hits = collections.defaultdict(list)
    geom = []
    http_methods = []
    totals = collections.Counter()

    SCEN = re.compile(r'(?i)(LessonProgress|LessonProgressQueue|CompletionRepository|'
                      r'PostProgressResponse|PathMap|GetPathMap|ChapterFinish|ChapterEnd|'
                      r'Reward|CoinsRepository|StreakRepository|DailyGoal|Progress|Scoring)', re.I)
    GEOM_CLASS = re.compile(r'(?i)(ui/path/map|interactors/path|PathMap|PathToolbar|ViewsKt)', re.I)
    HTTP_VERBS = {'GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'}
    HTTP_MSGS = re.compile(r'(?i)(HTTP method annotation is required|FormUrlEncoded can only|'
                           r'Multiple Retrofit annotations|@Body method annotations)', re.I)

    for p in sorted(glob.glob(A + '/_INPUT/*.dex')):
        d = Dex(open(p, 'rb').read(), os.path.basename(p))
        mids = d.method_ids
        fids = d.field_ids
        strs = d.strings
        tids = [t['descriptor'] for t in d.type_ids]
        nmid, nfid, ns = len(mids), len(fids), len(strs)
        for c in d.class_defs:
            caller_cls = c['descriptor']
            mimo_caller = caller_cls.startswith('Lcom/getmimo/')
            geom_class = bool(GEOM_CLASS.search(caller_cls))
            for m in c['defined_methods']:
                if not m['code_off']:
                    continue
                caller_sig = m['signature']
                try:
                    insns = list(decode_reachable(d, m['code_off']))
                except Exception:
                    totals['decode_errors'] += 1
                    continue
                totals['methods_decoded'] += 1
                totals['insns_decoded'] += len(insns)
                geom_ins = []
                http_verbs_in = []
                http_types_in = []
                for (start, op, idx, lit, units) in insns:
                    # ---- method calls -------------------------------------
                    if op in INVOKE:
                        # invoke-custom/polymorphic carry a call_site_idx (or a
                        # MethodHandle ref), NOT the callee method_idx.
                        if op in (0xfa, 0xfb, 0xfc, 0xfd):
                            totals['dynamic_invokes_skipped'] += 1
                            continue
                        if idx is None or idx >= nmid:
                            continue
                        t = mids[idx]
                        callee_cls, callee_sig = t['class'], t['signature']
                        totals['invoke_insns'] += 1
                        if mimo_caller and callee_cls.startswith('Lcom/getmimo/'):
                            k = (caller_cls, callee_cls)
                            a = call_agg[k]
                            a['n'] += 1
                            if len(a['samples']) < 3:
                                a['samples'].append({
                                    'caller_method': caller_sig, 'callee_method': callee_sig,
                                    'opcode': INVOKE[op], 'dex': d.name,
                                    'insn_offset': '0x%x' % start, 'method_ref_idx': idx})
                            if SCEN.search(caller_sig) or SCEN.search(callee_sig):
                                if len(scenario_edges) < 40000:
                                    scenario_edges.append({
                                        'dex': d.name, 'insn_offset': '0x%x' % start,
                                        'opcode': INVOKE[op], 'caller': caller_sig,
                                        'callee': callee_sig, 'method_ref_idx': idx})
                        elif mimo_caller:
                            external_agg[callee_cls.split('/')[1].rstrip(';')] += 1
                    # ---- field access -------------------------------------
                    elif op in IFIELD or op in SFIELD:
                        if idx is None or idx >= nfid:
                            continue
                        f = fids[idx]
                        totals['field_insns'] += 1
                        if mimo_caller or f['class'].startswith('Lcom/getmimo/'):
                            k = (caller_cls, f['class'])
                            a = field_agg[k]
                            a['n'] += 1
                            if len(a['samples']) < 2:
                                a['samples'].append({
                                    'access': IFIELD.get(op, SFIELD.get(op)),
                                    'field': '%s->%s:%s' % (f['class'], f['name'], f['type']),
                                    'caller_method': caller_sig, 'dex': d.name,
                                    'insn_offset': '0x%x' % start, 'field_ref_idx': idx})
                    # ---- string constants ---------------------------------
                    elif op in (0x1a, 0x1b):
                        if idx is None or idx >= ns:
                            continue
                        v = strs[idx]['value']
                        if v in HTTP_VERBS:
                            http_verbs_in.append((start, v))
                        if HTTP_MSGS.search(v) or v.startswith('Lretrofit2/'):
                            string_hits[v[:150]].append({
                                'dex': d.name, 'method': caller_sig,
                                'insn_offset': '0x%x' % start, 'string_idx': idx})
                        if len(v) < 90 and SCEN.search(v):
                            string_hits[v[:150]].append({
                                'dex': d.name, 'method': caller_sig,
                                'insn_offset': '0x%x' % start, 'string_idx': idx})
                    # ---- type references for HTTP resolution ---------------
                    elif op in (0x1c, 0x1f, 0x20, 0x22):
                        if idx is not None and idx < len(tids):
                            http_types_in.append((start, tids[idx]))
                    # ---- numeric literals (geometry) ----------------------
                    elif op in CONST and geom_class:
                        fv = float32(lit) if op in (0x14, 0x15) and lit is not None else None
                        geom.append({
                            'dex': d.name, 'class': caller_cls, 'method': caller_sig,
                            'insn_offset': '0x%x' % start, 'opcode': CONST[op],
                            'literal_int': lit,
                            'as_float32': round(fv, 6) if fv is not None else None})
                if http_verbs_in and http_types_in:
                    http_methods.append({
                        'dex': d.name, 'class': caller_cls, 'method': caller_sig,
                        'verbs': [{'offset': '0x%x' % o, 'verb': v} for o, v in http_verbs_in],
                        'type_refs': [{'offset': '0x%x' % o, 'type': t} for o, t in http_types_in if t][:40]})
        print('%s: decoded=%d inv=%d' % (d.name, totals['methods_decoded'], totals['invoke_insns']))

    # ---- HTTP verb resolution ----------------------------------------------
    # Retrofit's RequestFactory maps annotation CLASS -> verb string. R8 renamed
    # the annotation classes, but the strings survive. Collect candidate methods.
    http_candidates = [h for h in http_methods if len(h['verbs']) >= 3]
    resolved = []
    for h in http_candidates:
        seq = sorted(h['verbs'] + [{'offset': t['offset'], 'verb': 'TYPE:' + t['type']}
                                   for t in h['type_refs']],
                     key=lambda x: int(x['offset'], 16))
        resolved.append(dict(h, sequence=seq[:120]))

    out = {
        'document': 'MISSION 02 — method-level DEX bytecode evidence (read-only decode)',
        'source_of_truth': 'APK sha256 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a',
        'tool_and_method': 'dexlib.py + dex_bytecode.py; control-flow-reachable Dalvik invoke-*/iget/iput/const decoding over all 12 DEX (Smob junk excluded)',
        'status': 'OBSERVED (bytecode) — NOT RUNTIME VERIFIED',
        'totals': dict(totals),
        'mimo_internal_call_pairs': len(call_agg),
        'mimo_internal_call_edges_total': sum(v['n'] for v in call_agg.values()),
        'mimo_field_pairs': len(field_agg),
        'scenario_method_edges': len(scenario_edges),
        'call_graph': [
            {'from': k[0], 'to': k[1], 'invoke_count': v['n'], 'samples': v['samples']}
            for k, v in sorted(call_agg.items(), key=lambda x: -x[1]['n'])],
        'field_graph': [
            {'from': k[0], 'to': k[1], 'access_count': v['n'], 'samples': v['samples']}
            for k, v in sorted(field_agg.items(), key=lambda x: -x[1]['n'])[:6000]],
        'scenario_exact_edges': scenario_edges,
        'external_call_target_prefixes': dict(external_agg.most_common(40)),
        'retrofit_verb_resolution_candidates': resolved[:40],
        'retrofit_string_hits': {k: v[:6] for k, v in list(string_hits.items())[:200]},
        'geometry_numeric_literals_sample': geom[:1500],
        'geometry_numeric_literals_full_file': 'PATH_GEOMETRY_CONSTANTS.json',
        'geometry_literal_count': len(geom),
    }
    json.dump(out, open(OUT, 'w'), ensure_ascii=False, separators=(',', ':'))
    print('WROTE', OUT, os.path.getsize(OUT), 'bytes')
    print('totals', dict(totals))
    print('call pairs', len(call_agg), 'scenario edges', len(scenario_edges),
          'http candidates', len(resolved), 'geom literals', len(geom))


if __name__ == '__main__':
    main()
