#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mimo 9.35 (com.getmimo, versionCode 1792759685) -- minimal offline-unlock patch.

This script modifies ONLY `classes.dex` of the original APK, in four places.
Everything else (14,395 entries, resources, native libs, curriculum JSON,
AndroidManifest.xml) is copied byte-for-byte.  The rebuilt APK is re-signed
with APK Signature Scheme v2 + v3 (minSdkVersion = 28, so v1 is not needed).

Patch sites (all offsets are byte offsets inside classes.dex):

  10048708  keys/a.c()                     -> `return Boolean.TRUE`
            Removes the remote-key / Pro / dev gate used by
            CanOpenChapterWithKeys (`/v1/user/keys` is server-owned).
  10129624 + 0x4aa  GetPathMapState$invoke$3.invokeSuspend
            `if-nez v14, +23h` -> `goto +23h` : never build vn/e0 (Locked).
  10129624 + 0x51a  GetPathMapState$invoke$3.invokeSuspend
            `if-nez v14, +20h` -> `goto +20h` : never build vn/h0
            (UnlockedButNoKeys); always build vn/g0 (Unlocked).
  8684004  + 0xcc   cc/b.y()
            `if-eqz v7, +3h` -> nop; nop : never build vn/y (Locked section);
            every section becomes vn/a0 (Unlocked).

The four sites were located ONLY with reverse-engineering evidence already in
this repository:
  ANALYSIS/MISSION_06/EVIDENCE/DISASM/{DefaultKeysRepository,
    CanOpenChapterWithKeys,NetworkUtils,GetPathMapState_Invoke}.smali.txt
  ANALYSIS/MISSION_06/10_LEARNING_PROGRESSION.md
  ANALYSIS/MISSION_09/COMPLETE_PROGRESSION_ENGINE_SPEC.md
  ANALYSIS/MISSION_09/COMPLETE_CLIENT_ARCHITECTURE.md

Usage:
  python3 APK_PATCH/build_patched_apk.py \
      --original /path/to/Mimo_9.35.apk \
      --out      /path/to/Mimo_9.35_unlocked_offline.apk

Requirements: Python 3.8+, `openssl` on PATH.  No Java, no apktool, no
Android SDK, no Python packages are required.
"""
import argparse
import hashlib
import os
import struct
import subprocess
import tempfile
import zipfile
import zlib
from pathlib import Path

SIG_ALGO = 0x0103   # RSASSA-PKCS1-v1_5 / SHA2-256, chunked SHA2-256
V2_BLOCK_ID = 0x7109871a
V3_BLOCK_ID = 0xf05368c0
V3_MIN_SDK, V3_MAX_SDK = 28, 0x7fffffff
MAGIC = b'APK Sig Block 42'
CHUNK = 1 << 20
DEX_NAME = 'classes.dex'
DROP = {'META-INF/MANIFEST.MF', 'META-INF/YOUAREFINISHED.RSA',
        'META-INF/YOUAREFINISHED.SF'}


def u2(b, o): return struct.unpack_from('<H', b, o)[0]
def lp(data): return struct.pack('<I', len(data)) + data
def lp_seq(items): return lp(b''.join(lp(x) for x in items))


# ------------------------------------------------------------------ DEX patch
def patch_dex(raw: bytes):
    b = bytearray(raw)
    edits = []

    off = 10048708                              # keys/a.c(), 74 code units
    assert b[off:off+4] == bytes.fromhex('07621205'), 'unexpected keys/a.c()'
    assert b[off+0x48:off+0x48+6] == bytes.fromhex('711012bc0200'), \
        'unexpected Boolean.valueOf call site'
    method_idx = 48146                          # Boolean.valueOf(Z)
    body = (bytes.fromhex('1210')               # const/4 v0, 1
            + bytes([0x71, 0x10])               # invoke-static {v0}, ...
            + struct.pack('<H', method_idx)
            + bytes.fromhex('0000')             # registers word: v0
            + bytes.fromhex('0c001100'))        # move-result-object v0; return-object v0
    assert len(body) == 12
    b[off:off+148] = body + b'\x00' * (148 - len(body))
    edits.append(('keys/a.c() -> Boolean.TRUE', off, 148))

    ins = 10129624                              # GetPathMapState$invoke$3
    o = ins + 0x4aa
    assert b[o:o+4] == bytes.fromhex('390e2300'), 'unexpected 0x4aa branch'
    b[o:o+4] = bytes.fromhex('28230000')        # goto +23h ; nop
    edits.append(('no vn/e0 Locked tutorial', o, 4))
    o = ins + 0x51a
    assert b[o:o+4] == bytes.fromhex('390e2000'), 'unexpected 0x51a branch'
    b[o:o+4] = bytes.fromhex('28200000')        # goto +20h ; nop
    edits.append(('no vn/h0 UnlockedButNoKeys', o, 4))

    o = 8684004 + 0xcc                          # cc/b.y()
    assert b[o:o+4] == bytes.fromhex('38070300'), 'unexpected cc/b.y branch'
    b[o:o+4] = b'\x00' * 4                      # nop ; nop
    edits.append(('no vn/y Locked section', o, 4))

    # Repair DEX SHA-1 signature and Adler-32 checksum.
    b[12:32] = hashlib.sha1(bytes(b[32:])).digest()
    b[8:12] = struct.pack('<I', zlib.adler32(bytes(b[12:])) & 0xffffffff)
    return bytes(b), edits


def patch_direct_main_experimental(raw: bytes):
    """Route both unauthenticated splash destinations to MainActivity.

    Experimental only: this does not initialize onboarding, a selected track,
    guest state, or replace remote services. Never describe as fully offline.
    """
    b = bytearray(raw)
    insns = 10175824 + 16  # SplashActivity$onCreate$2.invokeSuspend
    edits = [
        # Ignore the update-screen branch so normal startup continues.
        (insns + 0x94, '38053200', '28320000', 'bypass update screen'),
        # Follow the existing unauthenticated path regardless of stored auth.
        (insns + 0x11c, '38051a00', '281a0000', 'use unauthenticated startup path'),
        # Both fallback Intent destinations become MainActivity (type index 0x1f06).
        (insns + 0x19e, '1c023e1f', '1c02061f', 'onboarding destination to MainActivity'),
        (insns + 0x1e4, '1c01511f', '1c01061f', 'intro destination to MainActivity'),
    ]
    for off, old, new, name in edits:
        if b[off:off + 4] != bytes.fromhex(old):
            raise ValueError(f'Unexpected bytecode for {name} at {off:#x}')
        b[off:off + 4] = bytes.fromhex(new)
    b[12:32] = hashlib.sha1(b[32:]).digest()
    b[8:12] = struct.pack('<I', zlib.adler32(b[12:]) & 0xffffffff)
    return bytes(b), [(name, off, 4) for off, _, _, name in edits]


def patch_skip_update_wait_experimental(raw: bytes):
    """Diagnostic only: substitute Boolean.FALSE for the suspending update check.

    At this point v4 is null/zero; Boolean.valueOf(false) is synchronous. The
    coroutine's existing result handling and routing remain intact. This does
    not bootstrap a guest or establish offline functionality.
    """
    b = bytearray(raw)
    off = 10175824 + 16 + 0x70
    if b[off:off + 6].hex() != '6e30d77d3a05':
        raise ValueError('Unexpected update-check invocation; refusing patch')
    b[off:off + 6] = bytes.fromhex('711012bc0400')  # Boolean.valueOf(v4)
    b[12:32] = hashlib.sha1(b[32:]).digest()
    b[8:12] = struct.pack('<I', zlib.adler32(b[12:]) & 0xffffffff)
    return bytes(b), ('EXPERIMENTAL skip suspending update check', off, 6)


def patch_ghost_initialization(raw: bytes, skip_native_init=False, skip_signature_spoof=False):
    """Targeted controls for the injected Application superclass, not a final fix."""
    expected = '4123a7bfea455141df39e4141ee42b0be797d36da488ce876ca99815f7deb5c0'
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError('Unexpected classes12.dex')
    b = bytearray(raw)
    for enabled, pc, old in [(skip_native_init, 0x0c, '71103e000000'),
                              (skip_signature_spoof, 0x1a, '71205a000100')]:
        if enabled:
            pos = 16668 + 16 + pc
            if b[pos:pos+6].hex() != old:
                raise ValueError('Unexpected ghost initializer instruction')
            b[pos:pos+6] = bytes(6)
    b[12:32] = hashlib.sha1(b[32:]).digest()
    b[8:12] = struct.pack('<I', zlib.adler32(b[12:]) & 0xffffffff)
    return bytes(b)


def patch_preserve_queued_progress(raw: bytes):
    """Experimental: suppress one shared DAO DELETE execution, including online.

    It is NOT a complete offline-mode implementation. Sync/logout semantics and
    persistence on a device have not been verified. Only use on the exact DEX.
    """
    b = bytearray(raw)
    code = 8425144 + 16  # Lbb/j;->invoke, code_item instructions
    assert b[code + 0x326:code + 0x332].hex() == '1a0173207220e9b210000c01'
    off = code + 0x332
    assert b[off:off + 6].hex() == '7210edb20100'
    b[off:off + 6] = b'\0' * 6  # do not execute the prepared DELETE; close still runs
    b[12:32] = hashlib.sha1(b[32:]).digest()
    b[8:12] = struct.pack('<I', zlib.adler32(b[12:]) & 0xffffffff)
    return bytes(b), ('EXPERIMENTAL disable queued progress DELETE', off, 6)


# ------------------------------------------------------------- low-level ZIP
def read_entries(apk: bytes):
    import io
    out = []
    for zi in zipfile.ZipFile(io.BytesIO(apk)).infolist():
        ho = zi.header_offset
        assert apk[ho:ho+4] == b'PK\x03\x04', (zi.filename, ho)
        nl, el = u2(apk, ho+26), u2(apk, ho+28)
        data_off = ho + 30 + nl + el
        raw = apk[data_off:data_off+zi.compress_size]
        assert len(raw) == zi.compress_size
        out.append(dict(name=zi.filename, flags=zi.flag_bits & ~0x08,
                        method=zi.compress_type, t=zi.date_time, crc=zi.CRC,
                        csize=zi.compress_size, usize=zi.file_size,
                        extra=apk[ho+30+nl:data_off], raw=raw,
                        external=zi.external_attr, internal=zi.internal_attr,
                        create_version=zi.create_version,
                        extract_version=zi.extract_version,
                        comment=zi.comment))
    return out


def dos_time(t):
    return ((t[3] << 11) | (t[4] << 5) | (t[5] // 2),
            ((t[0] - 1980) << 9) | (t[1] << 5) | t[2])


def build_unsigned(entries, patched_dex, extra_dex=None):
    replacements = {DEX_NAME: patched_dex}
    if extra_dex is not None:
        replacements['classes12.dex'] = extra_dex
    for e in entries:
        if e['name'] in replacements:
            data = replacements[e['name']]
            co = zlib.compressobj(9, zlib.DEFLATED, -15)
            e['raw'] = co.compress(data) + co.flush()
            e['csize'] = len(e['raw'])
            e['usize'] = len(data)
            e['crc'] = zlib.crc32(data) & 0xffffffff
    entries = [e for e in entries if e['name'] not in DROP]

    buf, written = bytearray(), []
    n = len(entries)
    for i, e in enumerate(entries):
        name = e['name'].encode('utf-8')
        tm, dt = dos_time(e['t'])
        extra = bytearray()
        if e['method'] == 0:                    # zipalign: 4-byte data alignment
            r = (-(len(buf) + 30 + len(name))) % 4
            if r:
                extra += struct.pack('<HH', 0, r) + b'\x00' * r
        if i == n - 1:                          # 8-byte APK Signing Block alignment
            cur = len(buf) + 30 + len(name) + len(extra) + e['csize']
            r = (-cur) % 8
            if r:
                delta = r if r >= 4 else r + 8
                extra += struct.pack('<HH', 0, delta - 4) + b'\x00' * (delta - 4)
        hdr = struct.pack('<IHHHHHIIIHH', 0x04034b50, e['extract_version'],
                          e['flags'], e['method'], tm, dt, e['crc'], e['csize'],
                          e['usize'], len(name), len(extra))
        off = len(buf)
        buf += hdr + name + bytes(extra) + e['raw']
        written.append((e, off, name))
    sb_offset = len(buf)
    assert sb_offset % 8 == 0

    cd = bytearray()
    for e, off, name in written:
        tm, dt = dos_time(e['t'])
        cd += struct.pack('<IHHHHHHIIIHHHHHII', 0x02014b50,
                          e['create_version'], e['extract_version'], e['flags'],
                          e['method'], tm, dt, e['crc'], e['csize'], e['usize'],
                          len(name), 0, len(e['comment']), 0, e['internal'],
                          e['external'], off) + name + e['comment']
    return bytes(buf), sb_offset, bytes(cd), len(written)


# --------------------------------------------------------------- v2/v3 signing
def chunked_digest(sections):
    digests = []
    for sec in sections:
        for i in range(0, len(sec), CHUNK):
            c = sec[i:i+CHUNK]
            digests.append(hashlib.sha256(b'\xa5' + struct.pack('<I', len(c)) + c).digest())
    return hashlib.sha256(b'\x5a' + struct.pack('<I', len(digests)) +
                          b''.join(digests)).digest()


def openssl(*args, data=None):
    p = subprocess.run(['openssl', *args], input=data,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return p.stdout


def make_signing_pairs(part1, cd, eocd_for_digest, key_path, cert_der_path):
    content_digest = chunked_digest([part1, cd, eocd_for_digest])
    digest_rec = (struct.pack('<I', SIG_ALGO) +
                  struct.pack('<I', len(content_digest)) + content_digest)
    digests, certs, attrs = lp_seq([digest_rec]), lp_seq([cert_der_path.read_bytes()]), lp_seq([])
    pub = openssl('pkey', '-in', str(key_path), '-pubout', '-outform', 'DER')

    def sign(msg):
        return openssl('dgst', '-sha256', '-sign', str(key_path), data=msg)

    # ---- v2 ----
    inner2 = digests + certs + attrs
    sig2 = sign(inner2)
    rec2 = struct.pack('<I', SIG_ALGO) + struct.pack('<I', len(sig2)) + sig2
    signer2 = lp(inner2) + lp_seq([rec2]) + lp(pub)
    pair2 = (struct.pack('<Q', 4 + len(lp_seq([signer2]))) +
             struct.pack('<I', V2_BLOCK_ID) + lp_seq([signer2]))

    # ---- v3 ----
    sdk = struct.pack('<II', V3_MIN_SDK, V3_MAX_SDK)
    inner3 = digests + certs + sdk + attrs
    sig3 = sign(inner3)
    rec3 = struct.pack('<I', SIG_ALGO) + struct.pack('<I', len(sig3)) + sig3
    signer3 = lp(inner3) + sdk + lp_seq([rec3]) + lp(pub)
    pair3 = (struct.pack('<Q', 4 + len(lp_seq([signer3]))) +
             struct.pack('<I', V3_BLOCK_ID) + lp_seq([signer3]))
    return pair2 + pair3


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--original', required=True, type=Path)
    ap.add_argument('--out', required=True, type=Path)
    ap.add_argument('--workdir', type=Path, default=None)
    ap.add_argument('--experimental-preserve-queue', action='store_true',
                    help='Suppress the shared queued-progress DELETE; affects online sync too; untested on Android')
    ap.add_argument('--experimental-direct-main', action='store_true',
                    help='Skip splash onboarding/auth routes to MainActivity; no guest bootstrap, not Android-tested')
    ap.add_argument('--diagnostic-skip-ghost-native-init', action='store_true')
    ap.add_argument('--diagnostic-skip-ghost-signature-spoof', action='store_true')
    ap.add_argument('--diagnostic-repack-only', action='store_true',
                    help='Control: rebuild and resign with unchanged DEX, not a usable patch')
    ap.add_argument('--experimental-skip-update-wait', action='store_true',
                    help='Diagnostic: bypass suspending startup update check; not Android-tested')
    args = ap.parse_args()

    wd = args.workdir or args.out.parent / '_apk_patch_work'
    wd.mkdir(parents=True, exist_ok=True)
    key, crt, der = wd/'signing_key.pem', wd/'signing_cert.pem', wd/'signing_cert.der'
    if not der.exists():
        openssl('req', '-x509', '-newkey', 'rsa:2048', '-keyout', str(key),
                '-out', str(crt), '-days', '10000', '-nodes', '-sha256',
                '-subj', '/CN=Mimo 9.35 Offline Unlock',
                '-addext', 'basicConstraints=critical,CA:FALSE')
        der.write_bytes(openssl('x509', '-in', str(crt), '-outform', 'DER'))

    apk = args.original.read_bytes()
    print('original', len(apk), hashlib.sha256(apk).hexdigest())
    dex = zipfile.ZipFile(args.original).read(DEX_NAME)
    if hashlib.sha256(dex).hexdigest() != '2f2c0c618f89c6d6cadf7acf93f48eb9572c66f6b68d7dba03a36c0487f6a115':
        raise ValueError('Unexpected classes.dex SHA-256; refusing fixed-offset patch')
    if args.diagnostic_repack_only:
        if args.experimental_direct_main or args.experimental_preserve_queue or args.experimental_skip_update_wait:
            raise ValueError('repack-only must not be combined with patches')
        patched, edits = dex, []
    else:
        patched, edits = patch_dex(dex)
    if args.experimental_direct_main:
        patched, startup_edits = patch_direct_main_experimental(patched)
        edits.extend(startup_edits)
        print('WARNING: direct startup bypass does not initialize a guest or chosen course; untested on Android')
    if args.experimental_skip_update_wait:
        patched, edit = patch_skip_update_wait_experimental(patched)
        edits.append(edit)
        print('WARNING: startup update check skipped experimentally; runtime behavior not established')
    if args.experimental_preserve_queue:
        patched, edit = patch_preserve_queued_progress(patched)
        edits.append(edit)
        print('WARNING: experimental queue preservation is untested on Android and affects online sync')
    print('dex', len(dex), '->', len(patched))
    for name, o, n in edits:
        print('  edit', name, 'offset', hex(o), 'bytes', n)
    assert len(patched) == len(dex)

    extra_dex = None
    if args.diagnostic_skip_ghost_native_init or args.diagnostic_skip_ghost_signature_spoof:
        ghost = zipfile.ZipFile(args.original).read('classes12.dex')
        extra_dex = patch_ghost_initialization(ghost, args.diagnostic_skip_ghost_native_init,
                                               args.diagnostic_skip_ghost_signature_spoof)
        print('WARNING: diagnostic ghost initializer patch; not production tested')
    entries = read_entries(apk)
    part1, sb_offset, cd, count = build_unsigned(entries, patched, extra_dex)
    print('entries', len(entries), '->', count, 'sb_offset', sb_offset)

    def eocd(cd_start):
        return struct.pack('<IHHHHIIH', 0x06054b50, 0, 0, count, count,
                           len(cd), cd_start, 0)

    # Digest section 3 uses sb_offset in place of the real CD offset.
    pairs = make_signing_pairs(part1, cd, eocd(sb_offset), key, der)
    size_after = len(pairs) + 8 + len(MAGIC)
    block = (struct.pack('<Q', size_after) + pairs +
             struct.pack('<Q', size_after) + MAGIC)
    out = part1 + block + cd + eocd(sb_offset + len(block))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(out)
    print('patched APK', len(out), hashlib.sha256(out).hexdigest())
    print('v2+v3 signing block', len(block), 'bytes; cd offset', sb_offset + len(block))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
