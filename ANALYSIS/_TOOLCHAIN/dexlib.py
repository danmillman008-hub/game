"""Read-only DEX structure parser for the Mimo 9.35 analysis.

ANALYSIS/_TOOLCHAIN only. No tool installation, no writes to the APK/DEX.
Implements the parts of the DEX spec needed for an independent inventory:
header, map_list, string/type/proto/field/method id tables, class_defs,
class_data (defined methods + code offsets) and code_item headers.
"""

import struct
import hashlib
import zlib

MAP_TYPES = {
    0x0000: 'header_item', 0x0001: 'string_id_item', 0x0002: 'type_id_item',
    0x0003: 'proto_id_item', 0x0004: 'field_id_item', 0x0005: 'method_id_item',
    0x0006: 'class_def_item', 0x0007: 'call_site_id_item',
    0x0008: 'method_handle_item', 0x1000: 'map_list', 0x1001: 'type_list',
    0x1002: 'annotation_set_ref_list', 0x1003: 'annotation_set_item',
    0x2000: 'class_data_item', 0x2001: 'code_item', 0x2002: 'string_data_item',
    0x2003: 'debug_info_item', 0x2004: 'annotation_item',
    0x2005: 'encoded_array_item', 0x2006: 'annotations_directory_item',
}


def u2(b, o):
    return struct.unpack_from('<H', b, o)[0]


def u4(b, o):
    return struct.unpack_from('<I', b, o)[0]


def uleb(b, o):
    result = 0
    shift = 0
    while True:
        byte = b[o]
        o += 1
        result |= (byte & 0x7f) << shift
        if not (byte & 0x80):
            break
        shift += 7
        if shift > 35:
            raise ValueError('malformed uleb128 at %d' % o)
    return result, o


def mutf8(b, o):
    # string_data_item = uleb128 utf16_size + MUTF-8 bytes + 0x00.
    # The uleb128 length MUST be skipped; otherwise the length byte leaks
    # into the decoded value as a control character.
    _size, start = uleb(b, o)
    end = b.find(b'\x00', start)
    if end < 0:
        end = len(b)
    raw = b[start:end]
    s = raw.decode('utf-8', errors='replace')
    return s, end + 1


class Dex:
    def __init__(self, data, name):
        self.data = data
        self.name = name
        self.sha256 = hashlib.sha256(data).hexdigest()
        self.errors = []
        h = self.header = {}
        h['magic'] = data[0:8].decode('latin-1')
        h['checksum_stored'] = u4(data, 8)
        h['signature_stored'] = data[12:32].hex()
        h['checksum_computed'] = zlib.adler32(data[12:]) & 0xffffffff
        h['signature_computed'] = hashlib.sha1(data[32:]).hexdigest()
        h['checksum_valid'] = h['checksum_stored'] == h['checksum_computed']
        h['signature_valid'] = h['signature_stored'] == h['signature_computed']
        h['file_size'] = u4(data, 32)
        h['header_size'] = u4(data, 36)
        h['endian_tag'] = hex(u4(data, 40))
        h['link_size'] = u4(data, 44)
        h['link_off'] = u4(data, 48)
        h['map_off'] = u4(data, 52)
        h['string_ids_size'] = u4(data, 56)
        h['string_ids_off'] = u4(data, 60)
        h['type_ids_size'] = u4(data, 64)
        h['type_ids_off'] = u4(data, 68)
        h['proto_ids_size'] = u4(data, 72)
        h['proto_ids_off'] = u4(data, 76)
        h['field_ids_size'] = u4(data, 80)
        h['field_ids_off'] = u4(data, 84)
        h['method_ids_size'] = u4(data, 88)
        h['method_ids_off'] = u4(data, 92)
        h['class_defs_size'] = u4(data, 96)
        h['class_defs_off'] = u4(data, 100)
        h['data_size'] = u4(data, 104)
        h['data_off'] = u4(data, 108)
        self.map_list = self._parse_map()
        self.strings = self._parse_strings()
        self.type_ids = self._parse_type_ids()
        self.proto_ids = self._parse_proto_ids()
        self.field_ids = self._parse_field_ids()
        self.method_ids = self._parse_method_ids()
        self.class_defs = self._parse_class_defs()

    def _parse_map(self):
        b = self.data
        off = self.header['map_off']
        n = u4(b, off)
        out = []
        for i in range(n):
            o = off + 4 + 12 * i
            t = u2(b, o)
            out.append({'type': hex(t), 'type_name': MAP_TYPES.get(t, 'UNKNOWN'),
                        'size': u4(b, o + 4), 'offset': u4(b, o + 8)})
        return out

    def _parse_strings(self):
        b = self.data
        n = self.header['string_ids_size']
        off = self.header['string_ids_off']
        out = []
        for i in range(n):
            id_off = off + 4 * i
            data_off = u4(b, id_off)
            try:
                s, _ = mutf8(b, data_off)
            except Exception as e:
                self.errors.append('string %d: %s' % (i, e))
                s = ''
            out.append({'index': i, 'id_off': id_off, 'data_off': data_off, 'value': s})
        return out

    def _parse_type_ids(self):
        b = self.data
        n = self.header['type_ids_size']
        off = self.header['type_ids_off']
        out = []
        for i in range(n):
            si = u4(b, off + 4 * i)
            s = self.strings[si]['value'] if si < len(self.strings) else ''
            out.append({'index': i, 'descriptor': s})
        return out

    def _parse_proto_ids(self):
        b = self.data
        n = self.header['proto_ids_size']
        off = self.header['proto_ids_off']
        out = []
        for i in range(n):
            o = off + 12 * i
            shorty = u4(b, o)
            ret = u4(b, o + 4)
            params_off = u4(b, o + 8)
            params = []
            if params_off:
                cnt = u4(b, params_off)
                for j in range(cnt):
                    ti = u2(b, params_off + 4 + 2 * j)
                    params.append(self.type_ids[ti]['descriptor'] if ti < len(self.type_ids) else '')
            out.append({'index': i,
                        'shorty': self.strings[shorty]['value'] if shorty < len(self.strings) else '',
                        'return_type': self.type_ids[ret]['descriptor'] if ret < len(self.type_ids) else '',
                        'parameters': params})
        return out

    def _parse_field_ids(self):
        b = self.data
        n = self.header['field_ids_size']
        off = self.header['field_ids_off']
        out = []
        for i in range(n):
            o = off + 8 * i
            ci = u2(b, o)
            ti = u2(b, o + 2)
            ni = u4(b, o + 4)
            out.append({'index': i,
                        'class': self.type_ids[ci]['descriptor'] if ci < len(self.type_ids) else '',
                        'type': self.type_ids[ti]['descriptor'] if ti < len(self.type_ids) else '',
                        'name': self.strings[ni]['value'] if ni < len(self.strings) else ''})
        return out

    def _parse_method_ids(self):
        b = self.data
        n = self.header['method_ids_size']
        off = self.header['method_ids_off']
        out = []
        for i in range(n):
            o = off + 8 * i
            ci = u2(b, o)
            pi = u2(b, o + 2)
            ni = u4(b, o + 4)
            proto = self.proto_ids[pi] if pi < len(self.proto_ids) else {'return_type': '', 'parameters': []}
            out.append({'index': i,
                        'class': self.type_ids[ci]['descriptor'] if ci < len(self.type_ids) else '',
                        'name': self.strings[ni]['value'] if ni < len(self.strings) else '',
                        'return_type': proto['return_type'],
                        'parameters': proto['parameters'],
                        'signature': '%s->%s(%s)%s' % (
                            self.type_ids[ci]['descriptor'] if ci < len(self.type_ids) else '',
                            self.strings[ni]['value'] if ni < len(self.strings) else '',
                            ''.join(proto['parameters']), proto['return_type'])})
        return out

    def _parse_class_defs(self):
        b = self.data
        n = self.header['class_defs_size']
        off = self.header['class_defs_off']
        out = []
        for i in range(n):
            o = off + 32 * i
            ci = u4(b, o)
            super_i = u4(b, o + 8)
            src_i = u4(b, o + 16)
            ann_off = u4(b, o + 20)
            class_data_off = u4(b, o + 24)
            rec = {
                'index': i,
                'descriptor': self.type_ids[ci]['descriptor'] if ci < len(self.type_ids) else '',
                'access_flags': u4(b, o + 4),
                'superclass': self.type_ids[super_i]['descriptor'] if 0xffffffff != super_i and super_i < len(self.type_ids) else '',
                'interfaces_off': u4(b, o + 12),
                'source_file': self.strings[src_i]['value'] if src_i != 0xffffffff and src_i < len(self.strings) else '',
                'annotations_off': ann_off,
                'class_data_off': class_data_off,
                'static_values_off': u4(b, o + 28),
                'defined_methods': [],
                'n_static_fields': 0, 'n_instance_fields': 0,
                'n_direct_methods': 0, 'n_virtual_methods': 0,
            }
            if class_data_off:
                try:
                    cd, counts = self._parse_class_data(class_data_off)
                    rec['defined_methods'] = cd
                    rec['n_static_fields'] = counts[0]
                    rec['n_instance_fields'] = counts[1]
                    rec['n_direct_methods'] = counts[2]
                    rec['n_virtual_methods'] = counts[3]
                except Exception as e:
                    self.errors.append('class_def %d class_data: %s' % (i, e))
            out.append(rec)
        return out

    def _parse_class_data(self, off):
        b = self.data
        o = off
        n_static, o = uleb(b, o)
        n_inst, o = uleb(b, o)
        n_direct, o = uleb(b, o)
        n_virtual, o = uleb(b, o)
        for _ in range(n_static):
            _, o = uleb(b, o)
            _, o = uleb(b, o)
        for _ in range(n_inst):
            _, o = uleb(b, o)
            _, o = uleb(b, o)
        methods = []
        for group, count in (('direct', n_direct), ('virtual', n_virtual)):
            idx = 0
            for _ in range(count):
                diff, o = uleb(b, o)
                access, o = uleb(b, o)
                code_off, o = uleb(b, o)
                idx += diff
                mi = self.method_ids[idx] if idx < len(self.method_ids) else {}
                methods.append({
                    'method_idx': idx, 'group': group, 'access_flags': access,
                    'code_off': code_off,
                    'name': mi.get('name', ''), 'signature': mi.get('signature', ''),
                })
        return methods, (n_static, n_inst, n_direct, n_virtual)

    def code_item(self, off):
        """Return the code_item header only (no instruction decoding)."""
        if not off:
            return None
        b = self.data
        return {
            'offset': off,
            'registers_size': u2(b, off), 'ins_size': u2(b, off + 2),
            'outs_size': u2(b, off + 4), 'tries_size': u2(b, off + 6),
            'debug_info_off': u4(b, off + 8), 'insns_size': u4(b, off + 12),
            'insns_off': off + 16,
        }

    def summary(self):
        defined = sum(len(c['defined_methods']) for c in self.class_defs)
        with_code = sum(1 for c in self.class_defs for m in c['defined_methods'] if m['code_off'])
        no_code = defined - with_code
        ci_count = next((e['size'] for e in self.map_list if e['type_name'] == 'code_item'), None)
        return {
            'name': self.name,
            'bytes': len(self.data),
            'sha256': self.sha256,
            'header': {k: v for k, v in self.header.items() if k != 'signature_stored' and k != 'signature_computed'},
            'signature_stored': self.header['signature_stored'],
            'signature_computed': self.header['signature_computed'],
            'map_list': self.map_list,
            'counts': {
                'string_ids': self.header['string_ids_size'],
                'type_ids': self.header['type_ids_size'],
                'proto_ids': self.header['proto_ids_size'],
                'field_ids': self.header['field_ids_size'],
                'method_ids': self.header['method_ids_size'],
                'class_defs': self.header['class_defs_size'],
                'code_items_from_map': ci_count,
                'defined_methods_from_class_data': defined,
                'defined_methods_with_code': with_code,
                'defined_methods_without_code': no_code,
                'defined_fields': sum(c['n_static_fields'] + c['n_instance_fields'] for c in self.class_defs),
                'n_direct_methods': sum(c['n_direct_methods'] for c in self.class_defs),
                'n_virtual_methods': sum(c['n_virtual_methods'] for c in self.class_defs),
            },
            'parse_errors': self.errors,
        }
