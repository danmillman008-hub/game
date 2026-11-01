/**
 * Content pack loader — reads a pack directory from the repository and exposes the model.
 * spec: HANDOFF/02_SPEC_CONTENT_MODEL.md
 *
 * A pack lives at `mimo/content/<packId>/`:
 *   tracks.json
 *   tutorial-<id>.json
 *   assets/…
 *
 * Loading is pure fetch over the preview host (same origin) so the engine also works from file:// when the pack is
 * inlined by the build step (see tools/pack_to_bundle.py). No network access beyond the local origin.
 */

import { flattenLessons, validatePack } from './model.js';

export const DEFAULT_PACK = 'demo';

export async function loadPack(packId = DEFAULT_PACK, base = 'content') {
  const root = `${base}/${packId}`;
  const tracksRaw = await fetchJson(`${root}/tracks.json`);
  const packErrors = [];
  const { ok, errors, warnings } = validatePack(tracksRaw);
  if (!ok) packErrors.push(...errors);

  const refs = new Map();
  for (const track of tracksRaw.tracks || []) {
    for (const section of track.sections || []) {
      for (const t of section.tutorials || []) refs.set(Number(t.id), { ...t, trackId: track.id, trackVersion: track.version });
    }
  }

  const tutorialsById = new Map();
  await Promise.all([...refs.values()].map(async (ref) => {
    try {
      const tutorial = await fetchJson(`${root}/tutorial-${ref.id}.json`);
      tutorialsById.set(Number(ref.id), { ...ref, ...tutorial, id: Number(ref.id) });
    } catch (err) {
      packErrors.push(`توتوریال ${ref.id} بارگذاری نشد: ${err.message}`);
    }
  }));

  const index = new Map();
  for (const track of tracksRaw.tracks || []) {
    const lessons = flattenLessons(track, tutorialsById);
    for (const item of lessons) index.set(`${item.tutorialId}:${item.lessonId}`, item);
  }

  return {
    id: packId,
    root,
    publishSetVersion: Number(tracksRaw.publishSetVersion),
    title: tracksRaw.title || 'بستهٔ محتوایی',
    description: tracksRaw.description || '',
    tracks: tracksRaw.tracks || [],
    tutorialsById,
    lessonIndex: index,
    errors: packErrors,
    warnings,
    findByKey(key) { return index.get(key) || null; },
  };
}

async function fetchJson(url) {
  const res = await fetch(url, { cache: 'no-store' });
  if (!res.ok) throw new Error(`${url} (${res.status})`);
  return res.json();
}

/** Next lesson inside the same track, in document order. */
export function nextLesson(pack, current) {
  const all = [];
  for (const track of pack.tracks) {
    for (const section of track.sections || []) {
      for (const ref of section.tutorials || []) {
        const tutorial = pack.tutorialsById.get(Number(ref.id));
        if (!tutorial) continue;
        for (const chapter of tutorial.chapters || []) {
          for (const lesson of chapter.lessons || []) {
            all.push({ tutorialId: tutorial.id, lessonId: lesson.id, trackId: track.id });
          }
        }
      }
    }
  }
  const idx = all.findIndex((x) => x.tutorialId === current.tutorialId && x.lessonId === current.lessonId);
  return idx >= 0 && idx + 1 < all.length ? all[idx + 1] : null;
}
