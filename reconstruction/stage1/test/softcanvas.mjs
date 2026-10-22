// A software 2D canvas: enough of the CanvasRenderingContext2D surface for the
// reconstruction (fillRect, drawImage with scaling/flips, transforms, fillText
// as blocks), rasterizing into an RGBA buffer and writing PNG.
//
// This exists so the shipped render path can be executed and inspected without a
// browser. It is a test instrument, not part of the game.
import { deflateSync, inflateSync } from 'node:zlib';
import { readFileSync } from 'node:fs';

export class SoftImage {
  constructor(width, height) {
    this.width = width;
    this.height = height;
    this.data = null;         // RGBA
    this._src = '';
    this.onload = null;
    this.onerror = null;
  }
  set src(p) {
    this._src = p;
    try {
      const path = p.startsWith('file://') ? new URL(p) : p;
      const buf = readFileSync(path);
      const img = decodePng(buf);
      this.width = img.width;
      this.height = img.height;
      this.data = img.data;
      if (this.onload) this.onload();
    } catch (e) {
      if (this.onerror) this.onerror(e);
    }
  }
  get src() { return this._src; }
}

// --- minimal PNG decoder (8-bit RGB / RGBA, non-interlaced) -------------------
function decodePng(buf) {
  if (buf.readUInt32BE(0) !== 0x89504e47) throw new Error('not a PNG');
  let pos = 8;
  let width = 0, height = 0, bitDepth = 0, colorType = 0;
  const idat = [];
  while (pos < buf.length) {
    const len = buf.readUInt32BE(pos);
    const type = buf.toString('ascii', pos + 4, pos + 8);
    const data = buf.subarray(pos + 8, pos + 8 + len);
    if (type === 'IHDR') {
      width = data.readUInt32BE(0);
      height = data.readUInt32BE(4);
      bitDepth = data[8];
      colorType = data[9];
      if (bitDepth !== 8) throw new Error('only 8-bit PNG supported');
    } else if (type === 'IDAT') {
      idat.push(data);
    } else if (type === 'IEND') break;
    pos += 12 + len;
  }
  const raw = inflateSync(Buffer.concat(idat));
  const channels = colorType === 6 ? 4 : colorType === 2 ? 3 : 1;
  const stride = width * channels;
  const out = Buffer.alloc(width * height * 4);
  const prev = Buffer.alloc(stride);
  let rp = 0;
  for (let y = 0; y < height; y++) {
    const filter = raw[rp++];
    const line = Buffer.from(raw.subarray(rp, rp + stride));
    rp += stride;
    for (let i = 0; i < stride; i++) {
      const a = i >= channels ? line[i - channels] : 0;
      const b = prev[i];
      const c = i >= channels ? prev[i - channels] : 0;
      let v = line[i];
      switch (filter) {
        case 1: v = (v + a) & 0xff; break;
        case 2: v = (v + b) & 0xff; break;
        case 3: v = (v + ((a + b) >> 1)) & 0xff; break;
        case 4: {
          const p = a + b - c;
          const pa = Math.abs(p - a), pb = Math.abs(p - b), pc = Math.abs(p - c);
          v = (v + (pa <= pb && pa <= pc ? a : pb <= pc ? b : c)) & 0xff;
          break;
        }
        default: break;
      }
      line[i] = v;
    }
    line.copy(prev);
    for (let x = 0; x < width; x++) {
      const o = (y * width + x) * 4;
      const s = x * channels;
      out[o] = line[s];
      out[o + 1] = channels > 1 ? line[s + 1] : line[s];
      out[o + 2] = channels > 2 ? line[s + 2] : line[s];
      out[o + 3] = channels === 4 ? line[s + 3] : 255;
    }
  }
  return { width, height, data: out };
}

// --- PNG encoder --------------------------------------------------------------
const CRC_TABLE = (() => {
  const t = new Int32Array(256);
  for (let n = 0; n < 256; n++) {
    let c = n;
    for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
    t[n] = c;
  }
  return t;
})();

function crc32(buf) {
  let c = -1;
  for (let i = 0; i < buf.length; i++) c = CRC_TABLE[(c ^ buf[i]) & 0xff] ^ (c >>> 8);
  return (c ^ -1) >>> 0;
}

function chunk(type, data) {
  const len = Buffer.alloc(4);
  len.writeUInt32BE(data.length);
  const t = Buffer.from(type, 'ascii');
  const crc = Buffer.alloc(4);
  crc.writeUInt32BE(crc32(Buffer.concat([t, data])));
  return Buffer.concat([len, t, data, crc]);
}

export function encodePng(width, height, rgba) {
  const stride = width * 4;
  const raw = Buffer.alloc((stride + 1) * height);
  for (let y = 0; y < height; y++) {
    raw[y * (stride + 1)] = 0;
    rgba.copy(raw, y * (stride + 1) + 1, y * stride, y * stride + stride);
  }
  const ihdr = Buffer.alloc(13);
  ihdr.writeUInt32BE(width, 0);
  ihdr.writeUInt32BE(height, 4);
  ihdr[8] = 8;
  ihdr[9] = 6;
  return Buffer.concat([
    Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]),
    chunk('IHDR', ihdr),
    chunk('IDAT', deflateSync(raw)),
    chunk('IEND', Buffer.alloc(0)),
  ]);
}



// --- rasterizer --------------------------------------------------------------
export class SoftCanvas {
  constructor(width, height) {
    this.width = width;
    this.height = height;
    this.data = Buffer.alloc(width * height * 4);
  }
  addEventListener() {}
  focus() {}
  getContext() {
    if (!this._ctx) this._ctx = new SoftCtx(this);
    return this._ctx;
  }
  toPng() { return encodePng(this.width, this.height, this.data); }
}

class SoftCtx {
  constructor(canvas) {
    this.canvas = canvas;
    this.fillStyle = '#000';
    this.font = '';
    this.textBaseline = 'alphabetic';
    this.imageSmoothingEnabled = false;
    this.tx = 0;
    this.ty = 0;
    this.flipX = 1;
    this.rot = 0;
    this.stack = [];
    this.ops = [];
  }
  save() { this.stack.push([this.tx, this.ty, this.flipX, this.rot]); this.ops.push(['save']); }
  restore() { const s = this.stack.pop(); if (s) [this.tx, this.ty, this.flipX, this.rot] = s; this.ops.push(['restore']); }
  translate(x, y) { this.tx += x * this.flipX; this.ty += y; this.ops.push(['translate', x, y]); }
  rotate(a) { this.rot += a; this.ops.push(['rotate', a]); }
  scale(x, y) { this.flipX *= x; this.ops.push(['scale', x, y]); }

  setPixel(x, y, r, g, b, a) {
    x = Math.round(x);
    y = Math.round(y);
    if (x < 0 || y < 0 || x >= this.canvas.width || y >= this.canvas.height) return;
    const o = (y * this.canvas.width + x) * 4;
    const d = this.canvas.data;
    if (a >= 255) { d[o] = r; d[o + 1] = g; d[o + 2] = b; d[o + 3] = 255; return; }
    const alpha = a / 255;
    d[o] = Math.round(r * alpha + d[o] * (1 - alpha));
    d[o + 1] = Math.round(g * alpha + d[o + 1] * (1 - alpha));
    d[o + 2] = Math.round(b * alpha + d[o + 2] * (1 - alpha));
    d[o + 3] = Math.max(d[o + 3], a);
  }

  fillRect(x, y, w, h) {
    const [r, g, b, a] = parseColour(this.fillStyle);
    const x0 = this.tx + x * this.flipX;
    const y0 = this.ty + y;
    const x1 = x0 + w * this.flipX;
    const y1 = y0 + h;
    for (let yy = Math.min(y0, y1); yy < Math.max(y0, y1); yy++) {
      for (let xx = Math.min(x0, x1); xx < Math.max(x0, x1); xx++) {
        this.setPixel(xx, yy, r, g, b, a);
      }
    }
    this.ops.push(['fillRect', x, y, w, h]);
  }

  fillText(text, x, y) {
    // 8px monospace blocks: enough to verify HUD layout, not typography
    const cw = 6, ch = 8;
    const [r, g, b] = parseColour(this.fillStyle);
    let cx = x;
    for (const _ of String(text)) {
      for (let yy = 0; yy < ch - 1; yy++) {
        for (let xx = 0; xx < cw - 1; xx++) {
          this.setPixel(this.tx + cx + xx, this.ty + y + yy, r, g, b, 255);
        }
      }
      cx += cw;
    }
    this.ops.push(['fillText', String(text), x, y]);
  }

  drawImage(img, ...args) {
    if (!img || !img.data) { this.ops.push(['drawImage-skip', img && img._src]); return; }
    let sx = 0, sy = 0, sw = img.width, sh = img.height, dx, dy, dw, dh;
    if (args.length === 2) { [dx, dy] = args; dw = sw; dh = sh; }
    else if (args.length === 4) { [dx, dy, dw, dh] = args; }
    else { [sx, sy, sw, sh, dx, dy, dw, dh] = args; }

    for (let y = 0; y < dh; y++) {
      const srcY = sy + Math.floor((y * sh) / dh);
      if (srcY < 0 || srcY >= img.height) continue;
      for (let x = 0; x < dw; x++) {
        const srcX = sx + Math.floor((x * sw) / dw);
        if (srcX < 0 || srcX >= img.width) continue;
        const o = (srcY * img.width + srcX) * 4;
        const a = img.data[o + 3];
        if (!a) continue;
        const px = this.tx + (dx + x) * this.flipX;
        const py = this.ty + dy + y;
        this.setPixel(px, py, img.data[o], img.data[o + 1], img.data[o + 2], a);
      }
    }
    this.ops.push(['drawImage', img._src, ...args]);
  }
}

function parseColour(css) {
  if (typeof css !== 'string') return [0, 0, 0, 255];
  let m = /^#([0-9a-f]{6})$/i.exec(css);
  if (m) {
    const v = parseInt(m[1], 16);
    return [(v >> 16) & 255, (v >> 8) & 255, v & 255, 255];
  }
  m = /^rgba?\(([^)]+)\)$/i.exec(css);
  if (m) {
    const p = m[1].split(',').map((s) => parseFloat(s.trim()));
    return [p[0] | 0, p[1] | 0, p[2] | 0, p[3] === undefined ? 255 : Math.round(p[3] * 255)];
  }
  return [0, 0, 0, 255];
}
