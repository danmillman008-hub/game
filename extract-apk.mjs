#!/usr/bin/env node
// extract-apk.mjs — استخراج اندپوینت/کلید از APK بدون هیچ پیش‌نیاز
// اجرا:  node extract-apk.mjs app.apk
// خروجی: گزارش در ترمینال + فایل REPORT.txt کنار اسکریپت
// فقط از ماژول‌های داخلی Node استفاده می‌کند (zlib برای باز کردن zip).

import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';

/* ---------------- خواندن ZIP (بدون کتابخانه) ---------------- */
function readZip(buf) {
  // پیدا کردن End of Central Directory
  let eocd = -1;
  for (let i = buf.length - 22; i >= Math.max(0, buf.length - 70000); i--) {
    if (buf.readUInt32LE(i) === 0x06054b50) { eocd = i; break; }
  }
  if (eocd < 0) throw new Error('فایل zip/apk معتبر نیست');
  const count = buf.readUInt16LE(eocd + 10);
  let p = buf.readUInt32LE(eocd + 16);
  const entries = [];
  for (let i = 0; i < count; i++) {
    if (buf.readUInt32LE(p) !== 0x02014b50) break;
    const method = buf.readUInt16LE(p + 10);
    const csize = buf.readUInt32LE(p + 20);
    const nlen = buf.readUInt16LE(p + 28);
    const elen = buf.readUInt16LE(p + 30);
    const clen = buf.readUInt16LE(p + 32);
    const off = buf.readUInt32LE(p + 42);
    const name = buf.toString('utf8', p + 46, p + 46 + nlen);
    entries.push({ name, method, csize, off });
    p += 46 + nlen + elen + clen;
  }
  return entries;
}
function readEntry(buf, ent) {
  const o = ent.off;
  const nlen = buf.readUInt16LE(o + 26);
  const elen = buf.readUInt16LE(o + 28);
  const start = o + 30 + nlen + elen;
  const data = buf.subarray(start, start + ent.csize);
  if (ent.method === 0) return data;
  try { return zlib.inflateRawSync(data); } catch { return Buffer.alloc(0); }
}

/* ---------------- الگوها ---------------- */
const RE_URL = /https?:\/\/[A-Za-z0-9._~:/?#[\]@!$&'()*+,;=%-]{4,300}/g;
const RE_GUID = /[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/g;
const RE_PATH = /\/(?:[A-Za-z0-9_.-]+\/){0,6}(?:api|v1|v2|v3|inquiry|inquiries|esalat|authenticity|uid|barcode|catalog|check|verify|validate|search|nfi|irfda|drug|drugs|product)[A-Za-z0-9_./-]{0,80}/gi;
const RE_HOST = /[a-z0-9][a-z0-9.\-]{2,60}\.(?:ir|com|net|org|io)(?::\d{2,5})?/gi;
const KEY_WORDS = ['x-ssp-api-key', 'ssp-api-key', 'apikey', 'api-key', 'api_key', 'x-api-key', 'authorization', 'bearer', 'client_secret', 'token'];
const INTEREST = ['inquiry', 'esalat', 'authenticity', 'uid', 'barcode', 'catalog', 'nfi', 'checksingle'];
const SKIP = /\.(png|jpe?g|webp|gif|ttf|otf|woff2?|mp3|mp4|ogg|wav)$/i;
const MAX = 60 * 1024 * 1024;

const map = () => new Map();
const add = (m, k, src) => { if (!k) return; if (!m.has(k)) m.set(k, new Set()); m.get(k).add(src); };
const txt = (b) => b.toString('utf8').replace(/[^\x20-\x7E\u0600-\u06FF]+/g, ' ');
const ctx = (buf, i, span = 90) => txt(buf.subarray(Math.max(0, i - span), Math.min(buf.length, i + span))).replace(/\s+/g, ' ').trim();

const R = { urls: map(), paths: map(), hosts: map(), keys: map(), interesting: [], files: [], notes: [] };

function scan(buf, src) {
  const s = buf.toString('utf8');
  for (const m of s.matchAll(RE_URL)) {
    const u = m[0].replace(/[.,;)"'>]+$/, '');
    if (/\.(png|jpe?g|css|gif|svg|woff2?)$/i.test(u)) continue;
    add(R.urls, u, src);
  }
  for (const m of s.matchAll(RE_PATH)) {
    const p = m[0].replace(/[.,;)"']+$/, '');
    if (p.length < 6 || /\.(png|jpe?g|css|js|svg)$/i.test(p)) continue;
    add(R.paths, p, src);
  }
  for (const m of s.matchAll(RE_HOST)) {
    const h = m[0].toLowerCase();
    if (h.endsWith('.ir') || /ttac|fda|ssp/.test(h)) add(R.hosts, h, src);
  }
  const low = s.toLowerCase();
  for (const kw of KEY_WORDS) {
    let start = 0, n = 0;
    while (n++ < 200) {
      const i = low.indexOf(kw, start);
      if (i < 0) break;
      start = i + 1;
      const win = s.slice(Math.max(0, i - 160), i + 260);
      for (const g of win.matchAll(RE_GUID)) add(R.keys, g[0], kw);
    }
  }
  for (const kw of INTEREST) {
    let start = 0, n = 0;
    while (n++ < 25) {
      const i = low.indexOf(kw, start);
      if (i < 0) break;
      start = i + 1;
      R.interesting.push(`[${kw}] ${ctx(buf, i, 110).slice(0, 190)}`);
    }
  }
}

function walk(target) {
  const st = fs.statSync(target);
  if (st.isDirectory()) {
    const rec = (d) => {
      for (const f of fs.readdirSync(d, { withFileTypes: true })) {
        const full = path.join(d, f.name);
        if (f.isDirectory()) rec(full);
        else if (!SKIP.test(f.name)) {
          R.files.push(path.relative(target, full));
          scan(fs.readFileSync(full).subarray(0, MAX), path.relative(target, full));
        }
      }
    };
    rec(target);
    return;
  }
  const buf = fs.readFileSync(target);
  let entries;
  try { entries = readZip(buf); } catch (e) { R.notes.push('zip نبود، به‌عنوان فایل تک اسکن شد'); R.files.push(path.basename(target)); scan(buf.subarray(0, MAX), path.basename(target)); return; }
  R.notes.push(`فایل داخل بسته: ${entries.length}`);
  const names = entries.map(e => e.name);
  const dex = names.filter(n => /^classes\d*\.dex$/.test(n));
  if (dex.length) R.notes.push('dex: ' + dex.join(', '));
  if (names.some(n => n.includes('flutter_assets') || n.endsWith('kernel_blob.bin'))) R.notes.push('فریم‌ورک: Flutter (رشته‌ها در kernel_blob.bin)');
  if (names.some(n => n.endsWith('index.android.bundle'))) R.notes.push('فریم‌ورک: React Native');
  if (names.some(n => n.includes('assets/www/'))) R.notes.push('فریم‌ورک: Cordova/Ionic');
  if (names.some(n => n.endsWith('.so'))) R.notes.push('کتابخانه‌های نیتیو: ' + names.filter(n => n.endsWith('.so')).length);

  for (const e of entries) {
    if (e.name.endsWith('/')) continue;
    if (SKIP.test(e.name)) continue;
    const interesting = /\.(dex|js|json|xml|txt|html|bundle|bin|so|dat|properties|ya?ml)$/i.test(e.name) || /^(assets|res\/raw)/.test(e.name);
    if (!interesting) continue;
    let data;
    try { data = readEntry(buf, e); } catch { continue; }
    if (!data.length) continue;
    if (data.length > MAX) data = data.subarray(0, MAX);
    R.files.push(e.name);
    scan(data, e.name);
  }
}

function score(p) {
  const l = p.toLowerCase();
  let s = 0;
  const W = [['inquiry', 6], ['esalat', 6], ['authenticity', 6], ['uid', 5], ['barcode', 4], ['catalog', 4], ['check', 3], ['verify', 3], ['valid', 2], ['api', 2], ['drug', 2], ['search', 2], ['v1', 1]];
  for (const [w, n] of W) if (l.includes(w)) s += n;
  return s;
}

function report() {
  const L = [];
  L.push('='.repeat(66));
  L.push('گزارش استخراج اندپوینت از اپلیکیشن');
  L.push('='.repeat(66));
  R.notes.forEach(n => L.push('• ' + n));
  L.push('فایل‌های اسکن‌شده: ' + R.files.length);

  L.push('\n--- دامنه‌ها ---');
  [...R.hosts.keys()].sort().forEach(h => L.push('  ' + h + '   (' + [...R.hosts.get(h)].slice(0, 3).join(', ') + ')'));

  L.push('\n--- آدرس‌های کامل ---');
  [...R.urls.keys()].sort().forEach(u => L.push('  ' + u));

  L.push('\n--- مسیرهای شبه‌اندپوینت (به‌ترتیب اهمیت) ---');
  [...R.paths.keys()].sort((a, b) => score(b) - score(a)).slice(0, 120)
    .forEach(p => L.push(`  ${score(p) >= 8 ? '★' : ' '} ${p}   (امتیاز ${score(p)})`));

  if (R.keys.size) {
    L.push('\n--- کلید/توکن کنار کلمهٔ کلید ---');
    [...R.keys.entries()].forEach(([v, kinds]) => L.push('  ' + v + '\n       برچسب: ' + [...kinds].join(', ')));
  }

  L.push('\n--- رشته‌های مرتبط با استعلام ---');
  [...new Set(R.interesting)].slice(0, 50).forEach(c => L.push('  ' + c));

  L.push('\n' + '='.repeat(66));
  L.push('این فایل را برای تحلیل بفرستید. اندپوینت‌های ستاره‌دار مهم‌ترین‌اند.');
  L.push('='.repeat(66));
  return L.join('\n');
}

const target = process.argv[2];
if (!target) { console.log('استفاده: node extract-apk.mjs <app.apk | پوشه>'); process.exit(1); }
if (!fs.existsSync(target)) { console.log('پیدا نشد: ' + target); process.exit(1); }
walk(target);
const out = report();
console.log(out);
const outPath = path.join(process.cwd(), 'REPORT-APK.txt');
fs.writeFileSync(outPath, out, 'utf8');
console.log('\n✓ گزارش ذخیره شد: ' + outPath);
