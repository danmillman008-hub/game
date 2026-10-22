// Asset loading. Art is PNG recovered from the original game by tools/build_plate2.py
// and tools/extract_sprites.py; see the README for provenance.

const ASSET_MANIFEST = {
  plate: 'assets/plate.png',   // environment at the Stage-1 camera position
  axel_stand: 'assets/axel_stand.png',
  axel_walk: 'assets/axel_walk.png',
  axel_walk2: 'assets/axel_walk2.png',
  thug_stand: 'assets/thug_stand.png',
};

export const Assets = { images: {} };

// Asset URLs resolve against this module, so the game works no matter which
// document (or test harness) imports it.
const BASE = new URL('../', import.meta.url);

function resolveAsset(src) {
  return new URL(src, BASE).href;
}

function loadImage(src) {
  return new Promise((resolve) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = () => resolve(null);
    // a test harness may install a resolver for environments without a browser
    img.src = globalThis.__resolveAsset ? globalThis.__resolveAsset(src) : src;
  });
}

export async function loadAssets() {
  const entries = await Promise.all(
    Object.entries(ASSET_MANIFEST).map(async ([k, src]) => [k, await loadImage(resolveAsset(src))]),
  );
  for (const [k, img] of entries) Assets.images[k] = img;
  const missing = entries.filter(([, img]) => !img).map(([k]) => k);
  return { loaded: entries.length - missing.length, missing };
}
