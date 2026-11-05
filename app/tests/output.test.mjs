/** Behavioural tests for the MIMO NATIVE one-click output.
 *  The whole app is one HTML file: boot it from https:// and file:// and drive
 *  the real Mimo 9.35 navigation with state-aware clicks. No server, no mocks.
 */
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
  assert.ok(!/AIza|api\.openai\.com|api\.anthropic\.com/.test(ONE), 'no LLM API key');
  assert.ok(ONE.includes('id="mimoSource"'));
  assert.ok(ONE.includes('data-generated="mimo-bundle.js"'));
  assert.ok(ONE.includes('--primary:#7E4BDE'));
  assert.ok(ONE.includes(fs.readFileSync(path.join(APP, 'assets/phone.html'), 'utf8').trimEnd()));
  assert.ok(ONE.includes('/* ---- src/native.js ---- */'));
  assert.ok(!ONE.includes('/* ---- src/app.js ---- */'), 'legacy admin controller is not shipped');
});

test('one-file HTML boots from BOTH https and file:// with no errors', () => {
  for (const url of ['https://mimo.test/Mimo.html', 'file:///tmp/Mimo.html']) {
    const a = boot(ONE, url);
    assert.ok(a.w.MIMO, 'native controller booted');
    assert.ok(a.w.PROTO, 'approved prototype renderer booted');
    assert.equal(a.w.MIMO.version.startsWith('2.0.0-native'), true);
    assert.deepEqual(a.errors, [], `no console errors for ${url}`);
    assert.deepEqual(a.qa('#tabs .tab').map((t) => t.dataset.tab),
      ['Learn', 'Practice', 'AI', 'Leaderboard', 'Profile']);
    assert.ok(a.qa('.screen').length >= 18, '13 approved + 5 native screens');
    for (const s of ['learn', 'select-path', 'path-overview', 'section-detail', 'lesson',
      'exam-hub', 'exam-run', 'ai', 'native-studio', 'native-tokens', 'native-output',
      'native-gate', 'native-done']) {
      assert.ok(a.q(`[data-screen="${s}"]`), `screen ${s}`);
    }
    assert.equal(a.w.MIMO.curriculum.courses.length, 12);
    assert.equal(a.w.MIMO.curriculum.totalChapters, 60);
    assert.equal(a.w.MIMO.curriculum.totalLessons, 180);
    assert.equal(a.w.MIMO.outputKit.hasSource(), true);
    assert.equal(a.w.MIMO.outputKit.standaloneHtml(), ONE, 'byte-identical self export');
    a.close();
  }
});

test('Learn is Mimo 9.35 PathMap -> ChapterActivity -> Lesson -> Celebration', () => {
  const a = boot(); const M = a.w.MIMO;
  assert.equal(M.state().screen, 'learn');
  const nodes = a.qa('[data-screen="learn"] .pathwrap .node');
  assert.equal(nodes.length, 6, 'six approved path nodes');
  assert.ok(nodes.slice(0, 4).every((n) => n.dataset.lessonId), 'nodes bound to real lessons');
  assert.equal(a.qa('[data-screen="learn"] .pathwrap .node.locked').length, 0,
    'no locked node in learning (F25)');

  a.click(nodes[0]);
  assert.ok(a.q('#chapterModal').classList.contains('on'), 'chapter modal opened');
  assert.ok(a.q('#chapterModal h2').textContent.length > 3);
  a.click('#startLearning');
  assert.equal(M.state().screen, 'lesson');
  assert.ok(a.q('#phone').dataset.fullscreen === '1', 'ChapterActivity hides bottom tabs');
  assert.equal(M.state().lessonSteps, 4, 'slide / multiple choice / gap / reveal');
  assert.ok(a.q('.nl-prog i').style.width, 'Mimo 6dp progress bar');
  assert.ok(a.q('#nlBody .nl-panel'), 'interactive lesson panel');

  a.click('[data-n="lesson:next"]');
  assert.equal(a.qa('#nlBody .nl-choice').length, 4, 'a real 4-option question');
  a.click('#nlBody .nl-choice');
  assert.match(a.q('#nlFeedback').textContent, /درست|پاسخ/);
  a.click('[data-n="lesson:next"]');
  assert.equal(a.qa('#nlBody .nl-snip').length, 4, 'fill-the-gap snippets');
  a.click('#nlBody .nl-snip');
  a.click('[data-n="lesson:next"]');
  assert.ok(a.q('#nlBody .native-banner'), 'real explanation, not generated text');
  const before = M.economy.snapshot().ledger.length;
  a.click('[data-n="lesson:next"]');
  assert.equal(M.state().screen, 'native-done');
  assert.equal(M.state().progress.done, 1, 'lesson completion persisted');
  assert.ok(M.economy.snapshot().ledger.length > before, 'token economy wired to lessons');
  assert.ok(a.q('#doneStats').textContent.includes('امتیاز تجربه'));
  a.click('[data-screen="native-done"] [data-nav="learn"]');
  assert.equal(M.state().screen, 'learn');
  assert.ok(nodes[0].classList.contains('done'), 'completed node turns purple');
  assert.equal(a.q('#phone').dataset.fullscreen, '0');
  assert.deepEqual(a.errors, []);
  a.close();
});

test('quit dialog has the three measured M09 choices', () => {
  const a = boot(); const M = a.w.MIMO;
  a.click('[data-screen="learn"] .pathwrap .node.l10n1');
  a.click('#startLearning');
  a.click('[data-n="lesson:quit"]');
  assert.ok(a.q('#nativeQuit').classList.contains('on'));
  assert.equal(a.qa('[data-quit]').length, 3);
  a.click('[data-quit="path"]');
  assert.equal(M.state().screen, 'select-path');
  assert.equal(a.q('#nativeQuit').classList.contains('on'), false);
  a.close();
});

test('path picker / overview / section detail follow Mimo navigation', () => {
  const a = boot(); const M = a.w.MIMO;
  a.click('#pathSwitchBtn');
  assert.equal(M.state().screen, 'select-path');
  assert.equal(a.qa('#careerCards .career-card').length, 3, 'three program cards (F38)');
  a.click('[data-nav="path-overview"]');
  assert.equal(M.state().screen, 'path-overview');
  assert.ok(a.qa('#sectionRows .po-sec').length > 0, 'sections from KONKUR');
  a.click('#sectionRows .po-sec');
  assert.equal(M.state().screen, 'section-detail');
  assert.ok(a.qa('#lessonRows .sd-row').length >= 3, 'real lesson rows');
  a.click('#lessonRows .sd-row');
  assert.ok(a.q('#chapterModal').classList.contains('on'));
  a.click('#startLearning');
  assert.equal(M.state().screen, 'lesson');
  assert.deepEqual(a.errors, []);
  a.close();
});

test('Practice respects the measured guest gate, then opens the exam hub', () => {
  const a = boot(); const M = a.w.MIMO;
  assert.equal(M.state().guest, true);
  a.click('#tabs .tab[data-tab="Practice"]');
  assert.equal(M.state().screen, 'native-gate');
  assert.match(a.q('[data-screen="native-gate"] h2').textContent, /تثبیت/);
  a.click('[data-n="profile:create"]');
  assert.equal(M.state().screen, 'exam-hub');
  assert.equal(M.state().guest, false);
  assert.equal(a.qa('[data-screen="exam-hub"] .sec').length, 7, 'seven exam sections');
  a.close();
});

test('AI section is complete: four phases, local content, honest token accounting', () => {
  const a = boot(); const M = a.w.MIMO;
  a.click('#tabs .tab[data-tab="AI"]');
  assert.equal(M.state().screen, 'ai');
  a.click('[data-nav="native-studio"]');
  assert.equal(M.state().screen, 'native-studio');
  assert.equal(a.qa('[data-ai="mopt"]').length, 20, 'five diagnostic questions x four options');
  assert.equal(a.qa('#nsTokenChips .chip').length, 5);
  assert.equal(a.qa('#nsGraph span').length, 4, 'knowledge graph phases');
  a.click('[data-ai="plan"]');
  assert.equal(M.harnessStatus().steps, 6, 'six dependency steps');
  assert.equal(a.qa('#nsBody .native-steps li').length, 6);
  a.click('[data-ai="teach"]');
  assert.ok(a.q('#nsBody').textContent.length > 20, 'content from the local package');
  assert.equal(M.harnessStatus().generatesText, false);
  a.click('[data-ai="practice"]');
  assert.equal(a.qa('[data-ai="popt"]').length, 4);
  a.click('[data-ai="popt"]');
  assert.ok(a.q('#nsPracticeFeedback .native-banner'), 'real explanation shown');
  assert.equal(M.harnessStatus().externalProvider, 'not-configured');
  assert.match(M.aiStudio.tokenStructure()[0].value, /بدون LLM/);
  assert.match(M.aiStudio.tokenStructure()[2].value, /۰/);
  assert.equal(M.aiStudio.state().sessions.length, 1);
  assert.deepEqual(a.errors, []);
  a.close();
});

test('token structure works in all three meanings: design, economy, AI context', () => {
  const a = boot(); const M = a.w.MIMO;
  a.click('#tabs .tab[data-tab="Profile"]');
  a.click('[data-nav="native-tokens"]');
  assert.equal(M.state().screen, 'native-tokens');
  assert.equal(a.qa('#tkBody .native-swatch').length, 23, '23 approved design tokens');
  assert.equal(M.economy.cap, 400, 'daily XP cap');
  a.click('[data-tk="economy"]');
  assert.ok(a.qa('#tkBody .native-kv').length >= 6, 'six economy token kinds');
  const before = M.economy.snapshot().streak;
  a.click('[data-tk="goal"]');
  assert.equal(M.economy.snapshot().streak, before + 1);
  a.click('[data-tk="ai"]');
  assert.equal(a.qa('#tkBody .native-kv').length, 5, 'Model/Context/Cost/Steps/Settings');
  assert.deepEqual(a.errors, []);
  a.close();
});

test('one-click exports reproduce the exact file and the exported file boots again', () => {
  const a = boot(); const M = a.w.MIMO;
  assert.equal(M.outputKit.hasSource(), true);
  assert.equal(M.outputKit.standaloneHtml(), ONE);
  assert.match(M.outputKit.pwaIndex(), /rel="manifest"/);
  assert.match(M.outputKit.reportHtml(), /گزارش وضعیت میمو/);
  assert.equal(M.outputKit.pathCsv().split('\r\n').length, 181, '180 lessons + header');
  const b = boot(M.outputKit.standaloneHtml());
  assert.ok(b.w.MIMO);
  assert.equal(b.w.MIMO.outputKit.hasSource(), true, 'the export can export itself again');
  assert.deepEqual(b.errors, []);
  a.close(); b.close();
});

test('ZIP writer is a valid stored ZIP (local header, CRC32, EOCD)', () => {
  const zip = makeZip([{ name: 'a.txt', data: toBytes('hello') }, { name: 'b.txt', data: toBytes('mimo') }]);
  const u32 = (b, i) => (b[i] | (b[i + 1] << 8) | (b[i + 2] << 16) | (b[i + 3] << 24)) >>> 0;
  const u16 = (b, i) => b[i] | (b[i + 1] << 8);
  assert.equal(u32(zip, 0), 0x04034b50, 'local file header');
  assert.equal(crc32(toBytes('hello')), 0x3610a686, 'CRC32');
  let eocd = -1;
  for (let i = zip.length - 22; i >= 0; i -= 1) if (u32(zip, i) === 0x06054b50) { eocd = i; break; }
  assert.ok(eocd > 0, 'end-of-central-directory record');
  assert.equal(u16(zip, eocd + 8), 2, 'two entries');
});

test('PWA files, launcher and build manifest are complete', () => {
  const manifest = JSON.parse(fs.readFileSync(path.join(DIST, 'manifest.webmanifest'), 'utf8'));
  assert.equal(manifest.display, 'standalone');
  assert.equal(manifest.icons.length, 3);
  for (const ic of manifest.icons) {
    const b = fs.readFileSync(path.join(DIST, ic.src.replace('./', '')));
    assert.equal(b.slice(0, 8).toString('binary'), '\x89PNG\r\n\x1a\n');
  }
  const idx = fs.readFileSync(path.join(DIST, 'index.html'), 'utf8');
  assert.ok(idx.includes('serviceWorker.register'));
  const sw = fs.readFileSync(path.join(DIST, 'sw.js'), 'utf8');
  assert.ok(sw.includes("req.method !== 'GET'"));
  const launcher = fs.readFileSync(path.join(DIST, 'launcher.html'), 'utf8');
  for (const href of ['./index.html', './Mimo.html', './Mimo.zip']) assert.ok(launcher.includes(href));
  const build = JSON.parse(fs.readFileSync(path.join(DIST, 'BUILD_MANIFEST.json'), 'utf8'));
  assert.equal(build.controller, 'src/native.js');
  assert.deepEqual(build.honest, { llm: false, network: false, generatedText: false,
    externalProvider: 'not-configured', serverConfirmed: false });
});
