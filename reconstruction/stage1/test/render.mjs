// Render the shipped game to a PNG using the software canvas.
//
//   node reconstruction/stage1/test/render.mjs <out.png> [frames] [script]
//
// `script` is a compact input program: "right:120,idle:20,j:40" meaning hold
// right for 120 updates, then nothing for 20, then attack for 40.
import { SoftCanvas } from './softcanvas.mjs';
import { writeFileSync } from 'node:fs';

const out = process.argv[2] || '/tmp/stage1.png';
const frames = parseInt(process.argv[3] || '0', 10);
const script = process.argv[4] || '';

const canvas = new SoftCanvas(320, 224);
globalThis.document = { getElementById: (id) => (id === 'screen' ? canvas : { textContent: '' }) };
globalThis.window = globalThis;
globalThis.addEventListener = () => {};
globalThis.requestAnimationFrame = () => 0;
const { SoftImage } = await import('./softcanvas.mjs');
globalThis.Image = SoftImage;
const { fileURLToPath } = await import('node:url');
globalThis.__resolveAsset = (url) => (url.startsWith('file://') ? fileURLToPath(url) : url);

await import('../js/game.js');
const G = globalThis.STAGE1;

const KEY = { right: 'ArrowRight', left: 'ArrowLeft', up: 'ArrowUp', down: 'ArrowDown', j: 'j', k: 'k' };
let elapsed = 0;
const parts = script.split(',').filter(Boolean).map((p) => {
  const [name, n] = p.split(':');
  return { name, n: parseInt(n || '0', 10) };
});
// advance through the script
for (const step of parts) {
  const k = KEY[step.name];
  if (k) G.press(k);
  for (let i = 0; i < step.n; i++) { G.step(1); }
  if (k) G.release(k);
  elapsed += step.n;
}
const extra = Math.max(0, frames - elapsed);
G.step(extra);

const ctx = canvas.getContext();
ctx.renderNow = null;
// run the module's render() by stepping once after drawing is impossible without
// an export, so call the canvas path directly through a render pass
G.renderFrame && G.renderFrame();
writeFileSync(out, canvas.toPng());
console.log(`wrote ${out} (frame ${G.frame}, player x=${G.player.x.toFixed(1)} z=${G.player.z.toFixed(1)}, foes=${G.enemies.length})`);
