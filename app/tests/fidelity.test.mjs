import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { APP, readFile, readBytes } from './harness.mjs';

const ROOT = path.resolve(APP, '..');
const PROTO = path.join(ROOT, 'mimo-ui/UPGRADE/DESIGN/index.html');
const EXPECTED_SHA = 'c356068daa5ccafbee46599897ad18bdf1e4f91f1ca23f36b1b8bd153dbfdb78';
const sha = (b) => crypto.createHash('sha256').update(b).digest('hex');

test('protected prototype is untouched (v12.5-fa)', () => {
  const raw = fs.readFileSync(PROTO);
  assert.equal(sha(raw), EXPECTED_SHA);
  const text = raw.toString('utf8');
  assert.match(text, /<html lang="fa" dir="rtl">/);
  assert.match(text, /طرح رابط کاربری v12\.5/);
});

test('CSS is a byte-for-byte copy of the approved stylesheet', () => {
  const raw = fs.readFileSync(PROTO);
  const css = raw.subarray(raw.indexOf('<style>') + 7, raw.indexOf('</style>'));
  assert.equal(sha(readBytes('assets/proto.css')), sha(css));
  assert.equal(readBytes('assets/proto.css').length, css.length);
  // design tokens survive unchanged
  for (const token of ['--primary:#7E4BDE', '--bg:#F6F7FB', '--text:#252746',
    '--radius-card:12.0px', '--toolbar:56.0px', '--progressbar:6.0px']) {
    assert.ok(readFile('assets/proto.css').includes(token), token);
  }
});

test('phone markup is a byte-for-byte copy of the approved phone', () => {
  const raw = fs.readFileSync(PROTO);
  const a = raw.indexOf('<div class="phone"');
  const marker = '\n    </div>\n  </div>\n\n  <aside class="spec">';
  const b = raw.indexOf(Buffer.from(marker), a);
  const phone = Buffer.concat([raw.subarray(a, b), Buffer.from('\n    </div>\n')]);
  assert.equal(sha(readBytes('assets/phone.html')), sha(phone));
  assert.equal(readBytes('assets/phone.html').length, phone.length);
  assert.ok(readFile('index.html').includes(readFile('assets/phone.html').trimEnd()),
    'the generated product inlines the approved phone markup verbatim');
});

test('data payloads (GEO/LEARN/NODE/KONKUR) are exact copies', () => {
  const s = fs.readFileSync(PROTO, 'utf8');
  const blocks = [...s.matchAll(/<script[^>]*>(.*?)<\/script>/gs)];
  assert.equal(blocks.length, 5);
  const data = blocks.slice(0, 4).map((m) => m[1]).join('\n') + '\n';
  assert.equal(sha(readFile('assets/proto-data.js')), sha(data));
});

test('bottom bar is exactly the 5 approved tabs, with no Max tab', () => {
  const html = readFile('index.html');
  const start = html.indexOf('id="tabs"');
  const nav = html.slice(start, start + 2600);
  const tabs = [...nav.matchAll(/data-tab="([A-Za-z]+)"/g)].map((m) => m[1]);
  assert.deepEqual(tabs, ['Learn', 'Practice', 'AI', 'Leaderboard', 'Profile']);
  assert.ok(!/data-tab="max"/i.test(html));
  assert.ok(!/مکس/.test(html));
  for (const label of ['یادگیری', 'تمرین', 'هوش مصنوعی', 'امتیازها', 'پروفایل']) {
    assert.ok(nav.includes(label), label);
  }
});

test('all 13 approved prototype screens are present in the product', () => {
  const html = readFile('index.html');
  const screens = ['learn', 'select-path', 'path-overview', 'section-detail', 'lesson',
    'leaderboard', 'user-profile', 'profile', 'exam-hub', 'exam-run', 'exam-result',
    'ai', 'section-practice'];
  for (const s of screens) {
    assert.ok(html.includes(`data-screen="${s}"`), `missing approved screen ${s}`);
  }
});

test('motion.css only adds transitions/animations, no new colours or fonts', () => {
  const css = readFile('assets/motion.css');
  assert.equal(/#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})\b/.test(css), false,
    'motion.css must not introduce hard-coded colours outside the approved tokens');
  assert.ok(css.includes('@keyframes screenIn'));
  assert.ok(css.includes('prefers-reduced-motion'));
});

test('provenance manifest records source hash and artifact hashes', () => {
  const p = JSON.parse(readFile('assets/PROVENANCE.json'));
  assert.equal(p.source_sha256, EXPECTED_SHA);
  for (const [name, expected] of Object.entries(p.artifacts)) {
    assert.equal(sha(readBytes(`assets/${name}`)), expected, name);
  }
});
