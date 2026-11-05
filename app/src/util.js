/**
 * Shared helpers for the "one-click output" layer. No network, no deps, no
 * server calls: Blob + <a download> and a tiny stored-ZIP writer are local.
 */
export const esc = (v) => String(v ?? '')
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
  .replace(/"/g, '&quot;').replace(/'/g, '&#39;');

export const faNum = (n) => String(n).replace(/\d/g, (d) => '۰۱۲۳۴۵۶۷۸۹'[+d]);

export function stamp() {
  try { return new Intl.DateTimeFormat('fa-IR', { dateStyle: 'medium', timeStyle: 'short' }).format(new Date()); }
  catch (_) { return new Date().toISOString(); }
}

export function toBytes(s) {
  if (typeof TextEncoder !== 'undefined') return new TextEncoder().encode(s);
  // jsdom / older WebViews: build UTF-8 bytes through btoa without any deps.
  const utf8 = encodeURIComponent(s).replace(/%([0-9A-F]{2})/g,
    (_, h) => String.fromCharCode(parseInt(h, 16)));
  const bin = btoa(utf8), out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i += 1) out[i] = bin.charCodeAt(i);
  return out;
}

export function b64ToText(b64) {
  const bytes = b64ToBytes(b64);
  if (typeof TextDecoder !== 'undefined') return new TextDecoder().decode(bytes);
  let pct = '';
  for (let i = 0; i < bytes.length; i += 1) pct += '%' + bytes[i].toString(16).padStart(2, '0');
  return decodeURIComponent(pct);
}

export function saveBytes(name, bytes, mime = 'application/octet-stream') {
  try {
    const blob = new Blob([bytes], { type: mime });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = name; a.rel = 'noopener';
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(() => { try { URL.revokeObjectURL(url); } catch (_) {} }, 4000);
    return true;
  } catch (_) { return false; }
}

export const saveText = (name, text, mime) =>
  saveBytes(name, toBytes(text), mime || 'text/plain;charset=utf-8');

/* ---- minimal STORE-ONLY ZIP writer (RFC 1951 method 0, no compression) ---- */
let CRC_TABLE = null;
function crcTable() {
  if (CRC_TABLE) return CRC_TABLE;
  CRC_TABLE = new Uint32Array(256);
  for (let n = 0; n < 256; n += 1) {
    let c = n;
    for (let k = 0; k < 8; k += 1) c = (c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1);
    CRC_TABLE[n] = c >>> 0;
  }
  return CRC_TABLE;
}
export function crc32(u8) {
  const t = crcTable(); let c = 0xFFFFFFFF;
  for (let i = 0; i < u8.length; i += 1) c = t[(c ^ u8[i]) & 0xFF] ^ (c >>> 8);
  return (c ^ 0xFFFFFFFF) >>> 0;
}
const p16 = (a, o, v) => { a[o] = v & 255; a[o + 1] = (v >>> 8) & 255; };
const p32 = (a, o, v) => { a[o] = v & 255; a[o + 1] = (v >>> 8) & 255; a[o + 2] = (v >>> 16) & 255; a[o + 3] = (v >>> 24) & 255; };

export function makeZip(entries) {
  const parts = [], central = [];
  let offset = 0, cdSize = 0;
  for (const e of entries) {
    const name = toBytes(e.name), data = e.data instanceof Uint8Array ? e.data : toBytes(String(e.data));
    const crc = crc32(data);
    const local = new Uint8Array(30 + name.length);
    p32(local, 0, 0x04034b50); p16(local, 4, 20); p16(local, 6, 0x0800); p16(local, 8, 0);
    p16(local, 10, 0); p16(local, 12, 0); p32(local, 14, crc);
    p32(local, 18, data.length); p32(local, 22, data.length);
    p16(local, 26, name.length); p16(local, 28, 0); local.set(name, 30);
    parts.push(local, data);
    const cen = new Uint8Array(46 + name.length);
    p32(cen, 0, 0x02014b50); p16(cen, 4, 20); p16(cen, 6, 20); p16(cen, 8, 0x0800);
    p16(cen, 10, 0); p16(cen, 12, 0); p16(cen, 14, 0); p32(cen, 16, crc);
    p32(cen, 20, data.length); p32(cen, 24, data.length);
    p16(cen, 28, name.length); p16(cen, 30, 0); p16(cen, 32, 0);
    p16(cen, 34, 0); p16(cen, 36, 0); p32(cen, 38, 0); p32(cen, 42, offset);
    cen.set(name, 46); central.push(cen);
    offset += local.length + data.length; cdSize += cen.length;
  }
  const eocd = new Uint8Array(22);
  p32(eocd, 0, 0x06054b50); p16(eocd, 4, 0); p16(eocd, 6, 0);
  p16(eocd, 8, entries.length); p16(eocd, 10, entries.length);
  p32(eocd, 12, cdSize); p32(eocd, 16, offset); p16(eocd, 20, 0);
  const all = [...parts, ...central, eocd];
  const out = new Uint8Array(all.reduce((n, p) => n + p.length, 0));
  let at = 0;
  for (const p of all) { out.set(p, at); at += p.length; }
  return out;
}

export function b64ToBytes(b64) {
  try {
    const bin = atob(b64);
    const out = new Uint8Array(bin.length);
    for (let i = 0; i < bin.length; i += 1) out[i] = bin.charCodeAt(i);
    return out;
  } catch (_) { return new Uint8Array(); }
}
