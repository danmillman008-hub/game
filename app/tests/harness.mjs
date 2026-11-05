/** jsdom harness: loads the REAL index.html + real assets, then boots app.js.
 *  A "restart" is a brand-new JSDOM whose localStorage is seeded with the
 *  previous instance's snapshot — this is the acceptance test for recovery. */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { JSDOM } from 'jsdom';

const HERE = path.dirname(fileURLToPath(import.meta.url));
export const APP = path.resolve(HERE, '..');
export const STORAGE_KEY = 'mimo.offline.app.v1';
let counter = 0;

export async function createApp({ seed = null } = {}) {
  counter += 1;
  const html = fs.readFileSync(path.join(APP, 'index.html'), 'utf8');
  const dom = new JSDOM(html, {
    url: 'http://localhost:3000/index.html',
    runScripts: 'outside-only',
    pretendToBeVisual: true,
  });
  const w = dom.window;
  if (seed) w.localStorage.setItem(STORAGE_KEY, seed);

  // Classic scripts define GEO/LEARN/NODE/KONKUR + window.PROTO.
  w.eval(fs.readFileSync(path.join(APP, 'assets/proto-data.js'), 'utf8'));
  w.eval(fs.readFileSync(path.join(APP, 'assets/proto-ui.js'), 'utf8'));

  // app.js is an ESM module; give the Node realm the browser globals it needs.
  globalThis.window = w;
  globalThis.document = w.document;
  globalThis.localStorage = w.localStorage;
  Object.defineProperty(globalThis, 'navigator', { value: w.navigator, configurable: true });
  globalThis.location = w.location;
  globalThis.NODE = w.NODE;
  globalThis.GEO = w.GEO;
  globalThis.LEARN = w.LEARN;
  globalThis.KONKUR = w.KONKUR;

  await import(`file://${path.join(APP, 'src/app.js')}?v=${counter}`);

  const q = (sel) => w.document.querySelector(sel);
  const qa = (sel) => [...w.document.querySelectorAll(sel)];
  const click = (el) => {
    if (!el) throw new Error('click target missing');
    el.dispatchEvent(new w.MouseEvent('click', { bubbles: true, cancelable: true }));
    return el;
  };
  const go = (name) => w.APP.go(name);
  const snapshot = () => w.localStorage.getItem(STORAGE_KEY);
  const close = () => dom.window.close();
  return { dom, w, q, qa, click, go, snapshot, close, app: w.APP, proto: w.PROTO };
}

export function readFile(rel) { return fs.readFileSync(path.join(APP, rel), 'utf8'); }
export function readBytes(rel) { return fs.readFileSync(path.join(APP, rel)); }
