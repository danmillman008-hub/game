"""Static regression checks only; these do not establish runtime functionality."""
import hashlib
import importlib.util
from pathlib import Path
import struct
import unittest
import zlib

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('builder', ROOT / 'APK_PATCH/build_patched_apk.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

class ExistingPatchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = (ROOT / 'ANALYSIS/_INPUT/classes.dex').read_bytes()
        expected = '2f2c0c618f89c6d6cadf7acf93f48eb9572c66f6b68d7dba03a36c0487f6a115'
        actual = hashlib.sha256(cls.original).hexdigest()
        if actual != expected:
            raise AssertionError(f'wrong DEX hash: {actual}, expected {expected}')
        cls.patched, cls.edits = builder.patch_dex(cls.original)

    def test_header_integrity(self):
        b = self.patched
        self.assertEqual(len(b), len(self.original))
        self.assertEqual(hashlib.sha1(b[32:]).digest(), b[12:32])
        self.assertEqual(zlib.adler32(b[12:]) & 0xffffffff, struct.unpack_from('<I', b, 8)[0])

    def test_only_documented_ranges_changed(self):
        ranges = [(8, 32)] + [(offset, offset+length) for _, offset, length in self.edits]
        for i, (old, new) in enumerate(zip(self.original, self.patched)):
            if old != new:
                self.assertTrue(any(a <= i < b for a, b in ranges), f'unexpected change at {i:#x}')

    def test_control_preserves_original_keys_method(self):
        result, edits = builder.patch_dex(self.original, preserve_keys_method=True)
        start, size = 10048708, 148
        self.assertEqual(result[start:start + size], self.original[start:start + size])
        self.assertEqual(len(edits), 3)
        self.assertEqual(hashlib.sha1(result[32:]).digest(), result[12:32])
        self.assertEqual(zlib.adler32(result[12:]) & 0xffffffff, struct.unpack_from('<I', result, 8)[0])
        for i, (old, new) in enumerate(zip(self.patched, result)):
            if old != new:
                self.assertTrue(8 <= i < 32 or start <= i < start + size)

    def test_goto_targets_in_code_units(self):
        base = 10129624
        for pc, delta, target in ((0x4aa, 0x23, 0x4f0), (0x51a, 0x20, 0x55a)):
            self.assertEqual(self.patched[base+pc:base+pc+4], bytes([0x28, delta, 0, 0]))
            self.assertEqual(pc + delta * 2, target)

    def test_practice_topic_filter_is_scoped(self):
        result, edit = builder.patch_include_future_practice_topics(self.patched)
        _, off, size = edit
        self.assertEqual(off, 10159612 + 16 + 0x1de)
        self.assertEqual(self.patched[off:off+size].hex(), '36a60600')
        self.assertEqual(result[off:off+size], bytes(4))
        self.assertEqual(result[32:off], self.patched[32:off])
        self.assertEqual(result[off+size:], self.patched[off+size:])
        self.assertEqual(hashlib.sha1(result[32:]).digest(), result[12:32])
        self.assertEqual(zlib.adler32(result[12:]) & 0xffffffff, struct.unpack_from('<I', result, 8)[0])
        corrupt = bytearray(self.patched); corrupt[off] ^= 1
        with self.assertRaises(ValueError):
            builder.patch_include_future_practice_topics(bytes(corrupt))

    def test_queue_cleanup_sql_not_fixed(self):
        statement = b'DELETE FROM lesson_progress WHERE in_queue = 1'
        self.assertEqual(self.original.count(statement), 1)
        self.assertEqual(self.patched.count(statement), 1)

    def test_experimental_queue_patch_suppresses_only_execution(self):
        result, edit = builder.patch_preserve_queued_progress(self.patched)
        _, off, length = edit
        self.assertEqual(off, 8425144 + 16 + 0x332)
        self.assertEqual(length, 6)
        self.assertEqual(self.patched[off:off + 6].hex(), '7210edb20100')
        self.assertEqual(result[off:off + 6], bytes(6))
        self.assertEqual(result[off + 6:off + 12].hex(), '72100abc0100')  # close()
        for i, (old, new) in enumerate(zip(self.patched, result)):
            if old != new:
                self.assertTrue(8 <= i < 32 or off <= i < off + 6)
        self.assertEqual(hashlib.sha1(result[32:]).digest(), result[12:32])
        self.assertEqual(zlib.adler32(result[12:]) & 0xffffffff, struct.unpack_from('<I', result, 8)[0])

    def test_experimental_patch_rejects_unexpected_instruction(self):
        corrupt = bytearray(self.patched)
        corrupt[8425144 + 16 + 0x332] ^= 1
        with self.assertRaises(AssertionError):
            builder.patch_preserve_queued_progress(bytes(corrupt))

    def test_experimental_direct_main(self):
        result, edits = builder.patch_direct_main_experimental(self.patched)
        base = 10175824 + 16
        expected = {0x94: '28320000', 0x11c: '281a0000',
                    0x19e: '1c02061f', 0x1e4: '1c01061f'}
        self.assertEqual(len(edits), 4)
        for pc, value in expected.items():
            self.assertEqual(result[base + pc:base + pc + 4].hex(), value)
        self.assertEqual(0x94 + 0x32 * 2, 0xf8)
        self.assertEqual(0x11c + 0x1a * 2, 0x150)
        for i, (old, new) in enumerate(zip(self.patched, result)):
            if old != new:
                self.assertTrue(8 <= i < 32 or any(base + p <= i < base + p + 4 for p in expected))
        self.assertEqual(hashlib.sha1(result[32:]).digest(), result[12:32])
        self.assertEqual(zlib.adler32(result[12:]) & 0xffffffff, struct.unpack_from('<I', result, 8)[0])

    def test_direct_main_rejects_unexpected_input(self):
        corrupt = bytearray(self.patched)
        corrupt[10175824 + 16 + 0x19e] ^= 1
        with self.assertRaises(ValueError):
            builder.patch_direct_main_experimental(bytes(corrupt))

    def test_skip_update_wait(self):
        result, edit = builder.patch_skip_update_wait_experimental(self.patched)
        _, off, length = edit
        self.assertEqual(off, 10175824 + 16 + 0x70)
        self.assertEqual(length, 6)
        self.assertEqual(self.patched[off:off + 6].hex(), '6e30d77d3a05')
        self.assertEqual(result[off:off + 6].hex(), '711012bc0400')
        self.assertEqual(hashlib.sha1(result[32:]).digest(), result[12:32])
        self.assertEqual(zlib.adler32(result[12:]) & 0xffffffff, struct.unpack_from('<I', result, 8)[0])
        corrupt = bytearray(self.patched); corrupt[off] ^= 1
        with self.assertRaises(ValueError): builder.patch_skip_update_wait_experimental(bytes(corrupt))

    def test_ghost_initializer_targeted_edits(self):
        raw = (ROOT / 'ANALYSIS/_INPUT/classes12.dex').read_bytes()
        base = 16668 + 16
        for native, spoof in ((True, False), (False, True), (True, True)):
            result = builder.patch_ghost_initialization(raw, native, spoof)
            self.assertEqual(result[base+0x0c:base+0x12], bytes(6) if native else raw[base+0x0c:base+0x12])
            self.assertEqual(result[base+0x1a:base+0x20], bytes(6) if spoof else raw[base+0x1a:base+0x20])
            self.assertEqual(hashlib.sha1(result[32:]).digest(), result[12:32])
            self.assertEqual(zlib.adler32(result[12:]) & 0xffffffff, struct.unpack_from('<I', result, 8)[0])
        with self.assertRaises(ValueError): builder.patch_ghost_initialization(raw[:-1], True, True)

    def test_startup_auth_code_not_changed(self):
        # code_item for SplashActivity$onCreate$2.invokeSuspend starts at 10175824.
        start = 10175824
        size = struct.unpack_from('<I', self.original, start + 12)[0]
        end = start + 16 + 2 * size
        self.assertEqual(self.original[start:end], self.patched[start:end])

if __name__ == '__main__':
    unittest.main()

class PracticeStatsPlaceholderTest(unittest.TestCase):
    def test_exact_dex_and_integrity(self):
        original = (ROOT / 'ANALYSIS/_INPUT/classes3.dex').read_bytes()
        patched = builder.patch_practice_stats_placeholder(original)
        off = 550020 + 16
        self.assertEqual(patched[off:off+20].hex(), '2202a2031a01c9401a00c9407030cb0c12001102')
        self.assertEqual(patched[off+20:off+774], bytes(754))
        self.assertEqual(patched[32:off], original[32:off])
        self.assertEqual(patched[off+774:], original[off+774:])
        self.assertEqual(hashlib.sha1(patched[32:]).digest(), patched[12:32])
        self.assertEqual(zlib.adler32(patched[12:]) & 0xffffffff, struct.unpack_from('<I', patched, 8)[0])

    def test_zip_writer_includes_both_additional_dex_files(self):
        import io
        import zipfile
        source = io.BytesIO()
        with zipfile.ZipFile(source, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            z.writestr('classes.dex', b'old-main')
            z.writestr('classes3.dex', b'old-three')
            z.writestr('classes12.dex', b'old-twelve')
        entries = builder.read_entries(source.getvalue())
        part, _, cd, count = builder.build_unsigned(entries, b'new-main', b'new-twelve', {'classes3.dex': b'new-three'})
        eocd = struct.pack('<IHHHHIIH', 0x06054b50, 0, 0, count, count, len(cd), len(part), 0)
        with zipfile.ZipFile(io.BytesIO(part + cd + eocd)) as z:
            self.assertEqual(z.read('classes.dex'), b'new-main')
            self.assertEqual(z.read('classes3.dex'), b'new-three')
            self.assertEqual(z.read('classes12.dex'), b'new-twelve')

    def test_unknown_dex_is_rejected(self):
        raw = bytearray((ROOT / 'ANALYSIS/_INPUT/classes3.dex').read_bytes())
        raw[-1] ^= 1
        with self.assertRaises(ValueError):
            builder.patch_practice_stats_placeholder(bytes(raw))
