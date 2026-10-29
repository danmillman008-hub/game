#!/usr/bin/env python3
"""Raw-DEX annotation reader: maps every method in the Retrofit service
interface to its HTTP path (@POST/@GET/@Multipart values live in the
annotation section, which androguard does not expose as values).

usage: python3 annpaths.py <dex> [<dex> ...]
"""
import sys, struct

def uleb(b, o):
    r = s = 0
    while True:
        x = b[o]; o += 1
        r |= (x & 0x7f) << s
        if not x & 0x80:
            return r, o
        s += 7

def mutf8(b, o):
    n, o = uleb(b, o)
    end = o + n
    out = bytearray()
    while o < end:
        c = b[o]
        if c < 0x80:
            out.append(c); o += 1
        elif c & 0xe0 == 0xc0:
            out.append(((c & 0x1f) << 6) | (b[o+1] & 0x3f)); o += 2
        else:
            cp = ((c & 0x0f) << 12) | ((b[o+1] & 0x3f) << 6) | (b[o+2] & 0x3f)
            out += chr(cp).encode('utf-8'); o += 3
    return out.decode('utf-8', 'replace')

class Dex:
    def __init__(self, path):
        self.b = open(path, 'rb').read()
        h = self.b
        self.class_defs_size = struct.unpack_from('<I', h, 0x60)[0]
        self.string_ids = self.u4(0x3C)
        self.type_ids = self.u4(0x44)
        self.proto_ids = self.u4(0x4C)
        self.field_ids = self.u4(0x54)
        self.method_ids = self.u4(0x5C)
        self.class_defs = self.u4(0x64)
        self.map_off = struct.unpack_from('<I', h, 0x34)[0]

    def u4(self, off): return struct.unpack_from('<I', self.b, off)[0]

    def string(self, idx):
        off = self.u4(self.string_ids + 4 * idx)
        return mutf8(self.b, off)

    def type(self, idx):
        return self.string(self.u4(self.type_ids + 4 * idx))

    def method(self, idx):
        cls, proto, name = struct.unpack_from('<HHI', self.b, self.method_ids + 8 * idx)
        return self.type(cls), self.string(name)

    def proto_desc(self, idx):
        shorty, ret, params = struct.unpack_from('<III', self.b, self.proto_ids + 12 * idx)
        out = []
        if params:
            n = self.u4(params)
            for i in range(n):
                out.append(self.string(self.u4(self.type_ids + 4 * self.u4(params + 4 + 4 * i))))
        return self.type(ret), out

    def method_annotations(self, idx):
        """return list of (annotation_type, [(name, value)])"""
        cls, proto, name = struct.unpack_from('<HHI', self.b, self.method_ids + 8 * idx)
        return None

    def encoded_value(self, off, depth=0):
        hdr = self.b[off]; off += 1
        vt = hdr & 0x1f
        arg = hdr >> 5
        if vt in (0x15, 0x16, 0x18, 0x19, 0x1a, 0x1b, 0x17):
            # fixed-width index: value_arg+1 bytes, little-endian
            n = arg + 1
            i = int.from_bytes(self.b[off:off+n], 'little')
            if vt == 0x17: return self.string(i), off + n
            if vt == 0x18: return self.type(i), off + n
            return i, off + n
        if vt in (0x00, 0x02, 0x03, 0x04, 0x06):   # byte/short/char/int/long
            n = arg + 1
            v = int.from_bytes(self.b[off:off+n], 'little'); return v, off + n
        if vt == 0x10:                      # float
            return struct.unpack_from('<f', self.b, off)[0], off + 4
        if vt == 0x11:                      # double
            return struct.unpack_from('<d', self.b, off)[0], off + 8
        if vt == 0x1c:                      # array
            n, off = uleb(self.b, off); out = []
            for _ in range(n):
                v, off = self.encoded_value(off, depth+1); out.append(v)
            return out, off
        if vt == 0x1d:                      # annotation
            return self.encoded_annotation(off)
        if vt == 0x1e:                      # null
            return None, off
        if vt == 0x1f:                      # boolean
            return bool(arg), off
        raise ValueError('enc value type 0x%x' % vt)

    def encoded_annotation(self, off):
        t, off = uleb(self.b, off)
        size, off = uleb(self.b, off)
        els = []
        for _ in range(size):
            ni, off = uleb(self.b, off)
            v, off = self.encoded_value(off)
            els.append((self.string(ni), v))
        return (self.type(t), els), off

    def annotation_set(self, off):
        if off == 0: return []
        n = self.u4(off); out = []
        for i in range(n):
            aoff = self.u4(off + 4 + 4 * i)
            vis = self.b[aoff]
            ann, _ = self.encoded_annotation(aoff + 1)
            out.append((vis, ann))
        return out

    def class_method_annotations(self):
        """yield (class, access, method_name, proto, [(ann_type, els)])"""
        cls_count = self.class_defs_size
        for ci in range(cls_count):
            base = self.class_defs + 32 * ci
            class_idx, access, super_idx, ifaces_off, src_idx, ann_off, data_off, sv_off = \
                struct.unpack_from('<IIIIIIII', self.b, base)
            if not ann_off: continue
            cname = self.type(class_idx)
            dir_off = ann_off
            class_ann = self.u4(dir_off)
            fsize = self.u4(dir_off + 4)
            msize = self.u4(dir_off + 8)
            psize = self.u4(dir_off + 12)
            o = dir_off + 16 + 8 * fsize
            for _ in range(msize):
                midx = self.u4(o); aoff = self.u4(o + 4); o += 8
                mc, mname = self.method(midx)
                try:
                    protoname = self.proto_desc(struct.unpack_from('<HHI', self.b, self.method_ids + 8 * midx)[1])
                except Exception:
                    protoname = None
                try:
                    anns = self.annotation_set(aoff)
                except Exception:
                    continue
                yield cname, access, mname, protoname, anns

    def map_size(self, name):
        off = self.map_off
        n = self.u4(off)
        for i in range(n):
            b = off + 4 + 12 * i
            t = struct.unpack_from('<H', self.b, b)[0]
            size = self.u4(b + 4)
            # type codes
            if t == 0x0006: return size   # CLASS_DEF_ITEM
        return 0

if __name__ == '__main__':
    for p in sys.argv[1:]:
        d = Dex(p)
        for cname, acc, mname, proto, anns in d.class_method_annotations():
            if not anns: continue
            paths = []
            for vis, (atype, els) in anns:
                if 'retrofit2/http' in atype or 'retrofit2' in atype:
                    paths.append((atype.split('/')[-1], dict(els)))
            if paths:
                for nm, kv in paths:
                    print(f'{p}\t{cname}\t{mname}\t{nm}\t{kv}')
