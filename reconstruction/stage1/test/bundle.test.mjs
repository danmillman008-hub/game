// Proves the single-file bundle is genuinely self-contained and equivalent.
//
//   node reconstruction/stage1/test/bundle.test.mjs
//
// Checks, in order:
//   1. the bundle declares no external references (no src/href to files, no
//      module imports, no path into the assets directory, no network URLs)
//   2. it defines its own canvas and controls, so there is nothing to load
//   3. it executes and boots with every asset decoded from its embedded data
//   4. rendering the same state produces byte-identical pixels to the module
//      build, so the bundle is the same game, not a fork
import { readFileSync } from 'node:fs';
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { runInNewContext } from 'node:vm';
import { SoftCanvas, SoftImage, encodePng } from './softcanvas.mjs';
import { deflateSync } from 'node:zlib';

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = join(HERE, '..');

let pass = 0;
let fail = 0;
const out = [];
function check(name, cond, detail = '') {
  if (cond) { pass++; out.push(`ok   ${name}`); }
  else { fail++; out.push(`FAIL ${name} ${detail}`); }
}

// ---------------------------------------------------------------- 1. static
const html = await readFile(join(ROOT, 'stage1.html'), 'utf8');

const forbidden = [
  [/<script[^>]+src=/i, 'external script src'],
  [/<link[^>]+href=/i, 'external stylesheet'],
  [/<img[^>]+src=/i, 'img tag'],
  [/\bimport\s*\{/, 'module import'],
  [/\bimport\.meta\b/, 'import.meta'],
  [/['"]assets\//, 'path into the assets directory'],
  [/['"]js\//, 'path into the js directory'],
  [/type=["']module["']/i, 'module script tag'],
  [/https?:\/\//i, 'network URL'],
];
for (const [re, why] of forbidden) {
  check(`no ${why}`, !re.test(html), String(html.match(re)));
}
check('exactly one script tag', (html.match(/<script/gi) || []).length === 1);
check('assets embedded as data URIs', (html.match(/data:image\/png;base64,/g) || []).length === 5);
check('inline CSS present', html.includes('<style>') && html.includes('image-rendering: pixelated'));

// ---------------------------------------------------------------- 2. extract
const m = html.match(/<script>\n([\s\S]*?)\n<\/script>/);
check('inline script extracted', !!m);
const source = m ? m[1] : '';

// embedded images must be valid PNGs of the expected size
const uris = html.match(/data:image\/png;base64,[A-Za-z0-9+/=]+/g) || [];
let decoded = 0;
for (const uri of uris) {
  const img = new SoftImage();
  img.src = uri;
  if (img.data && img.width > 0 && img.height > 0) decoded++;
}
check('every embedded image decodes', decoded === uris.length, `${decoded}/${uris.length}`);
check('environment plate is 320x224', uris.some((u) => {
  const i = new SoftImage(); i.src = u; return i.width === 320 && i.height === 224;
}));

// ---------------------------------------------------------------- 3. run it
function makeEnv() {
  const canvas = new SoftCanvas(320, 224);
  const sandbox = {
    document: { getElementById: (id) => (id === 'screen' ? canvas : { textContent: '' }) },
    Image: SoftImage,
    requestAnimationFrame: () => 0,
    addEventListener: () => {},
    console,
    Promise, Math, JSON, Object, Array, String, Number, Boolean, Error,
    setTimeout,
    window: null,
  };
  sandbox.window = sandbox;
  sandbox.globalThis = sandbox;
  return { canvas, sandbox };
}

const { canvas, sandbox } = makeEnv();
let booted = true;
try {
  runInNewContext(source, sandbox, { filename: 'stage1.html' });
} catch (e) {
  booted = false;
  out.push('     boot error: ' + e.message);
}
check('bundle executes without throwing', booted);

// let the (already synchronous) asset promises settle
await new Promise((r) => setTimeout(r, 120));

const G = sandbox.STAGE1;
check('STAGE1 surface exposed', !!G);
if (G) {
  check('every asset loaded inside the bundle', G.assetsReady());
  const missing = Object.entries(G.images).filter(([, v]) => !v).map(([k]) => k);
  check('no asset is missing', missing.length === 0, missing.join(','));

  // drive an identical scenario to the module build
  G.reset();
  G.press('ArrowRight');
  G.step(150);
  G.release('ArrowRight');
  G.renderFrame();
  const bundledPng = canvas.toPng();

  // the same scenario through the module build
  const modCanvas = new SoftCanvas(320, 224);
  const prevDocument = globalThis.document;
  globalThis.document = { getElementById: (id) => (id === 'screen' ? modCanvas : { textContent: '' }) };
  globalThis.window = globalThis;
  globalThis.addEventListener = () => {};
  globalThis.requestAnimationFrame = () => 0;
  globalThis.Image = SoftImage;
  globalThis.__resolveAsset = (u) => (u.startsWith('file://') ? fileURLToPath(u) : u);
  await import('../js/game.js');
  const M = globalThis.STAGE1;
  await new Promise((r) => setTimeout(r, 120));
  M.reset();
  M.press('ArrowRight');
  M.step(150);
  M.release('ArrowRight');
  M.renderFrame();
  const modulePng = modCanvas.toPng();
  globalThis.document = prevDocument;

  check('bundle and module agree on state',
    G.player.x === M.player.x && G.camera.x === M.camera.x,
    `${G.player.x}/${G.camera.x} vs ${M.player.x}/${M.camera.x}`);
  check('bundle renders the same pixels as the module build',
    Buffer.compare(bundledPng, modulePng) === 0);
  check('the rendered frame is not blank', (() => {
    const nonBlank = bundledPng.length > 0 && bundedHasVariety(bundledPng);
    return nonBlank;
  })());
}

function bundedHasVariety(png) {
  // crude: a real frame compresses to far more than a flat-colour image
  return png.length > 3000;
}

console.log(out.join('\n'));
console.log(`\n${pass} passed, ${fail} failed`);
if (fail) process.exitCode = 1;
