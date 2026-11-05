/* Offline shell cache. Network-first so development edits are always fresh;
   cached copies keep the app usable when the device is completely offline. */
const CACHE = 'mimo-offline-v2';
const SHELL = [
  './', './index.html', './assets/proto.css', './assets/motion.css', './assets/node-match.css',
  './assets/proto-data.js', './assets/proto-ui.js',
  './src/app.js', './src/store.js', './src/engine.js', './src/fixtures.js',
  './src/routes.js', './src/views.js', './src/nodes.js', './src/harness.js', './src/exam-template.js', './src/templates.js', './manifest.webmanifest',
];

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(CACHE).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim()),
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;
  event.respondWith(
    fetch(req).then((res) => {
      const copy = res.clone();
      caches.open(CACHE).then((c) => c.put(req, copy)).catch(() => {});
      return res;
    }).catch(() => caches.match(req).then((hit) => hit || caches.match('./index.html'))),
  );
});
