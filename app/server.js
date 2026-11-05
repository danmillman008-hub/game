#!/usr/bin/env node
/* Zero-dependency static server for the offline app.
   Binds 0.0.0.0 for the Arena live preview; no backend, no API, no proxy. */
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

// MIMO_ROOT lets the same zero-dependency server host the one-file PWA build
// (app/dist) on a second port for the live preview; default is the app folder.
const ROOT = process.env.MIMO_ROOT
  ? path.resolve(process.env.MIMO_ROOT)
  : path.dirname(fileURLToPath(import.meta.url));
const PORT = Number(process.env.PORT || 3000);
const TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.webmanifest': 'application/manifest+json; charset=utf-8',
  '.md': 'text/markdown; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.ico': 'image/x-icon',
};

const server = http.createServer((req, res) => {
  let pathname;
  try { pathname = decodeURIComponent(new URL(req.url, 'http://localhost').pathname); }
  catch (_) { res.writeHead(400); res.end('Bad request'); return; }
  if (pathname === '/') pathname = '/index.html';
  const target = path.resolve(ROOT, '.' + pathname);
  if (!target.startsWith(ROOT + path.sep) && target !== ROOT) {
    res.writeHead(403); res.end('Forbidden'); return;
  }
  fs.stat(target, (err, stat) => {
    if (err || !stat.isFile()) { res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' }); res.end('Not found'); return; }
    const type = TYPES[path.extname(target).toLowerCase()] || 'application/octet-stream';
    res.writeHead(200, {
      'Content-Type': type,
      'Content-Length': stat.size,
      'Cache-Control': 'no-cache',
      'Service-Worker-Allowed': '/',
      'Access-Control-Allow-Origin': '*',
    });
    if (req.method === 'HEAD') { res.end(); return; }
    fs.createReadStream(target).pipe(res);
  });
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`mimo offline app listening on 0.0.0.0:${PORT}`);
});
