// A tiny DOM/canvas stand-in so the game module can be exercised under Node.
// It records draw calls, so tests can assert on what was rendered as well as on
// game state.

class FakeImage {
  constructor() {
    this.width = 320;
    this.height = 224;
    this._src = '';
    this.onload = null;
    this.onerror = null;
  }
  set src(v) {
    this._src = v;
    if (this.onload) this.onload();
  }
  get src() { return this._src; }
}

class FakeCtx {
  constructor(canvas) {
    this.canvas = canvas;
    this.fillStyle = '#000';
    this.font = '';
    this.textBaseline = '';
    this.imageSmoothingEnabled = true;
    this.ops = [];
  }
  fillRect(x, y, w, h) { this.ops.push(['fillRect', x, y, w, h, this.fillStyle]); }
  fillText(s, x, y) { this.ops.push(['fillText', s, x, y]); }
  drawImage(img, ...rest) { this.ops.push(['drawImage', (img && img._src) || 'img', ...rest]); }
  save() { this.ops.push(['save']); }
  restore() { this.ops.push(['restore']); }
  translate(x, y) { this.ops.push(['translate', x, y]); }
  rotate(a) { this.ops.push(['rotate', a]); }
  scale(x, y) { this.ops.push(['scale', x, y]); }
}

export function installDom() {
  const ctx = new FakeCtx(null);
  const canvas = {
    width: 320,
    height: 224,
    focus() {},
    addEventListener() {},
    getContext: () => ctx,
  };
  ctx.canvas = canvas;
  const listeners = {};
  globalThis.document = {
    getElementById: (id) => (id === 'screen' ? canvas : { textContent: '' }),
  };
  globalThis.window = globalThis;
  globalThis.addEventListener = (t, fn) => { (listeners[t] ||= []).push(fn); };
  globalThis.requestAnimationFrame = () => 0;
  globalThis.Image = FakeImage;
  globalThis.__listeners = listeners;
  return { canvas, ctx };
}
