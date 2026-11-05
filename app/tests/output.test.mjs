import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { JSDOM, VirtualConsole } from 'jsdom';
import { makeZip, toBytes, crc32 } from '../src/util.js';

const APP = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const DIST = path.join(APP, 'dist');
const ONE = fs.readFileSync(path.join(DIST, 'Mimo.html'), 'utf8');

function boot(html = ONE, url = 'https://mimo.test/Mimo.html') {
  const errors = [];
  const vc = new VirtualConsole();
  vc.on('jsdomError', (e) => errors.push(String(e.message)));
  vc.on('error', (...a) => errors.push(a.join(' ')));
  const dom = new JSDOM(html, { url, runScripts: 'dangerously', pretendToBeVisual: true,
    virtualConsole: vc });
  const w = dom.window, d = w.document;
  const q = (s) => d.querySelector(s);
  const qa = (s) => [...d.querySelectorAll(s)];
  const click = (s) => {
    const el = typeof s === 'string' ? q(s) : s;
    assert.ok(el, `click target missing: ${s}`);
    el.dispatchEvent(new w.MouseEvent('click', { bubbles: true, cancelable: true }));
    return el;
  };
  return { dom, w, d, q, qa, click, errors, close: () => w.close() };
}

test('one-file HTML is genuinely self-contained (no server, no network, no ESM)', () => {
  const markup = ONE
    .replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi, '<script></script>')
    .replace(/<style\b[^>]*>[\s\S]*?<\/style>/gi, '<style></style>');
  assert.deepEqual([...markup.matchAll(/<[^>]*\s(?:src|href)="(?!data:|#)([^"]+)"/gi)].map((m) => m[1]), []);
  assert.equal(/<script[^>]*type="module"/i.test(ONE), false);
  assert.equal(ONE.toLowerCase().split('<script').length - 1,
    ONE.toLowerCase().split('</script>').length - 1, 'all script tags are closed');
  for (const forbidden of ['fetch(', 'new XMLHttpRequest', 'new WebSocket', 'new EventSource']) {
    assert.equal(ONE.includes(forbidden), false, `no ${forbidden}`);
  }
  assert.ok(ONE.includes('id="mimoSource"'));
  assert.ok(ONE.includes('data-generated="mimo-bundle.js"'));
  assert.ok(ONE.includes('--primary:#7E4BDE'));
  assert.ok(ONE.includes(fs.readFileSync(path.join(APP, 'assets/phone.html'), 'utf8').trimEnd()));
});

test('one-file HTML boots from BOTH https and file:// with no errors', () => {
  for (const url of ['https://mimo.test/Mimo.html', 'file:///device/Download/Mimo.html']) {
    const a = boot(ONE, url);
    assert.ok(a.w.PROTO, 'approved prototype renderer booted');
    assert.ok(a.w.APP, 'application controller booted');
    assert.equal(a.w.APP.plus.mounted, true);
    assert.deepEqual(a.errors, [], `no console errors for ${url}`);
    assert.deepEqual(a.qa('#tabs .tab').map((t) => t.dataset.tab),
      ['Learn', 'Practice', 'AI', 'Leaderboard', 'Profile']);
    for (const s of ['learning-path', 'lesson-studio', 'tokens', 'ai-studio', 'output']) {
      assert.ok(a.q(`[data-screen="${s}"]`), `screen ${s}`);
    }
    assert.equal(a.w.APP.starter.questions, 20);
    assert.equal(a.w.APP.learningPath.curriculum.totalLessons, 180);
    a.close();
  }
});

test('learning path is complete: 12 courses / 60 chapters / 180 lessons, sequential unlock, real answers', () => {
  const a = boot();
  const A = a.w.APP;
  assert.equal(A.learningPath.curriculum.courses.length, 12);
  assert.equal(A.learningPath.curriculum.totalChapters, 60);
  assert.equal(A.learningPath.curriculum.totalLessons, 180);
  A.go('learning-path');
  assert.equal(a.qa('#lpChapters .plus-card').length, 5);
  assert.equal(a.qa('[data-plus="lp:lesson"]').length, 15);
  assert.equal(a.q('[data-plus="lp:lesson"]').disabled, false, 'first lesson is open');
  assert.equal(a.qa('[data-plus="lp:lesson"][disabled]').length, 14, 'the rest are locked');
  a.click('[data-plus="lp:lesson"]');
  assert.equal(A.proto.currentScreen(), 'lesson-studio');
  assert.ok(a.q('#lsTitle').textContent.length > 3);
  assert.equal(a.qa('[data-plus="ls:opt"]').length, 4, 'a real 4-option question');
  a.click('[data-plus="ls:opt"][data-oi="0"]');
  a.click('[data-plus="ls:check"]');
  assert.ok(a.q('#lsBody .banner'), 'immediate feedback from the existing explanation');
  const before = A.plus.economy.snapshot().ledger.length;
  a.click('[data-plus="ls:complete"]');
  assert.equal(A.learningPath.progress().done, 1);
  assert.ok(A.plus.economy.snapshot().ledger.length > before, 'token economy is wired to lessons');
  assert.equal(a.qa('[data-plus="lp:lesson"][disabled]').length, 13, 'next lesson unlocked');
  a.click('[data-plus="lp:course"][data-key="chem12"]');
  assert.equal(A.learningPath.course().key, 'chem12');
  a.click('[data-plus="lp:program"][data-key="grade10"]');
  assert.equal(A.learningPath.state().programKey, 'grade10');
  assert.deepEqual(a.errors, []);
  a.close();
});

test('token structure works in all three meanings: design, economy, AI context', () => {
  const a = boot(); const A = a.w.APP;
  A.go('tokens');
  assert.equal(a.qa('#tkBody .plus-swatch').length, 23, '23 approved design tokens');
  assert.equal(A.plus.designTokens.catalogCounts.colors, 1198);
  a.click('[data-plus="tk:economy"]');
  assert.equal(a.qa('#tkBody .plus-grid span').length, 6, 'six economy token kinds');
  const s0 = A.plus.economy.snapshot();
  a.click('[data-plus="tk:earn-goal"]');
  assert.equal(A.plus.economy.snapshot().streak, s0.streak + 1);
  const keys = A.plus.economy.snapshot().keys;
  a.click('[data-plus="tk:spend-key"]');
  assert.equal(A.plus.economy.snapshot().keys, Math.max(0, keys - 1));
  assert.ok(A.plus.economy.snapshot().ledger.length >= 2);
  a.click('[data-plus="tk:ai"]');
  assert.equal(a.qa('#tkBody .plus-row').length, 5, 'Model/Context/Cost/Steps/Settings');
  assert.match(A.aiStudio.tokenStructure()[0].value, /بدون LLM/);
  assert.match(A.aiStudio.tokenStructure()[2].value, /۰/);
  assert.deepEqual(a.errors, []);
  a.close();
});

test('AI section is complete: four phases, real explanations, graph, honest token accounting', () => {
  const a = boot(); const A = a.w.APP;
  A.go('ai-studio');
  assert.equal(a.qa('#aiStudioTokenChips .chip').length, 5);
  assert.match(a.q('#aiStudioHonest').textContent, /بدون LLM/);
  a.q('#aiGoal').value = 'ژنتیک مولکولی';
  a.q('#aiReasoning').value = 'ابتدا همانندسازی را مرور میکنم سپس رونویسی و ترجمه را مقایسه مینمایم';
  a.click('[data-ai="start"]');
  assert.equal(A.harnessStatus().steps, 6, 'plan has 6 dependency steps');
  assert.equal(a.qa('[data-ai="mopt"]').length, 20, 'five diagnostic questions, four options each');
  for (let i = 0; i < 5; i += 1) a.click(`[data-ai="mopt"][data-qi="${i}"][data-oi="0"]`);
  a.click('[data-ai="measure-submit"]');
  assert.ok(A.aiStudio.state().measureScore >= 0);
  a.click('[data-ai="phase:plan"]');
  assert.equal(a.qa('#aiStudioBody .plus-steps li').length, 6);
  a.click('[data-ai="phase:teach"]');
  a.click('[data-ai="teach-record"]');
  const status = A.harnessStatus();
  assert.equal(status.propositions, 1);
  assert.equal(status.generatesText, false);
  assert.equal(status.externalProvider, 'not-configured');
  assert.equal(A.harness.state.graph.propositions[0].generated, false);
  a.click('[data-ai="phase:practice"]');
  assert.equal(a.qa('[data-ai="popt"]').length, 4);
  a.click('[data-ai="popt"][data-oi="0"]');
  a.click('[data-ai="practice-check"]');
  assert.ok(a.q('#aiStudioBody .banner'), 'real explanation shown, not generated');
  assert.equal(A.aiStudio.state().sessions.length, 1);
  assert.ok(A.aiStudio.state().contextUnits > 0, 'AI context tokens are counted');
  assert.equal(a.qa('#aiStudioGraph .plus-grid span').length, 5);
  assert.deepEqual(a.errors, []);
  a.close();
});

test('one-click self-export reproduces the exact file, and that file boots again', () => {
  const a = boot(); const A = a.w.APP;
  A.go('output');
  assert.equal(A.outputKit.hasSource(), true);
  const exported = A.outputKit.standaloneHtml();
  assert.equal(exported, ONE, 'byte-for-byte identical HTML string');
  assert.match(A.outputKit.pwaIndex(), /rel="manifest"/);
  assert.match(A.outputKit.reportHtml(), /گزارش وضعیت میمو/);
  assert.equal(A.outputKit.pathCsv().split('\r\n').length, 181, '180 lessons + header');
  const b = boot(exported, 'file:///phone/Download/Mimo-exported.html');
  assert.ok(b.w.APP.plus.mounted);
  assert.equal(b.w.APP.outputKit.hasSource(), true, 'the export can export itself again');
  assert.deepEqual(b.errors, []);
  a.close(); b.close();

  // The in-app ZIP button uses a dependency-free stored-ZIP writer: check it.
  const u32 = (a, o) => (a[o] | (a[o + 1] << 8) | (a[o + 2] << 16) | (a[o + 3] << 24)) >>> 0;
  const u16 = (a, o) => (a[o] | (a[o + 1] << 8)) >>> 0;
  const zip = makeZip([{ name: 'a.txt', data: toBytes('hello') },
                       { name: 'Mimo.html', data: toBytes('<b>میمو</b>') }]);
  assert.equal(u32(zip, 0), 0x04034b50, 'local file header');
  assert.equal(crc32(toBytes('hello')), 0x3610a686, 'CRC32');
  let eocd = -1;
  for (let i = zip.length - 22; i >= 0; i -= 1) if (u32(zip, i) === 0x06054b50) { eocd = i; break; }
  assert.ok(eocd > 0, 'end-of-central-directory record');
  assert.equal(u16(zip, eocd + 8), 2, 'two entries');
  assert.equal(u16(zip, eocd + 10), 2, 'two entries total');
  assert.equal(u32(zip, eocd + 16) + u32(zip, eocd + 12), eocd, 'central directory offsets');
});

test('PWA host and distribution files are present and coherent', () => {
  const manifest = JSON.parse(fs.readFileSync(path.join(DIST, 'manifest.webmanifest'), 'utf8'));
  assert.equal(manifest.display, 'standalone');
  assert.equal(manifest.icons.length, 3);
  for (const ic of manifest.icons) {
    const p = path.join(DIST, ic.src.replace('./', ''));
    const b = fs.readFileSync(p);
    assert.equal(b.subarray(1, 4).toString('ascii'), 'PNG');
  }
  const idx = fs.readFileSync(path.join(DIST, 'index.html'), 'utf8');
  assert.match(idx, /rel="manifest" href="\.\/manifest\.webmanifest"/);
  assert.match(idx, /serviceWorker\.register/);
  assert.ok(idx.length > ONE.length, 'PWA host = one-file app + manifest + SW registration');
  const sw = fs.readFileSync(path.join(DIST, 'sw.js'), 'utf8');
  assert.match(sw, /req\.method !== 'GET'/);
  assert.match(sw, /caches\.match/);
  const launcher = fs.readFileSync(path.join(DIST, 'launcher.html'), 'utf8');
  for (const href of ['./index.html', './Mimo.html', './Mimo.zip']) assert.ok(launcher.includes(href));
  const build = JSON.parse(fs.readFileSync(path.join(DIST, 'BUILD_MANIFEST.json'), 'utf8'));
  assert.ok(build.bundledModules.length >= 18);
  assert.equal(build.honest.llm, false);
  assert.equal(build.honest.serverConfirmed, false);
});
