/**
 * Content model — track → section → tutorial → chapter → lesson.
 * spec: HANDOFF/02_SPEC_CONTENT_MODEL.md
 *
 * Identity rule: the persisted learner key is (lessonId, tutorialId) — chapterId is navigation-only (correction C-16).
 */

export function lessonKey(lessonId, tutorialId) {
  return `${Number(tutorialId)}:${Number(lessonId)}`;
}

/** Validate a parsed tracks.json + tutorials. Returns {ok, errors[], warnings[]}. */
export function validatePack(pack) {
  const errors = [];
  const warnings = [];
  const tracks = pack?.tracks;
  if (!Array.isArray(tracks) || !tracks.length) errors.push('فایل tracks.json هیچ مسیر یادگیری ندارد.');
  if (!Number.isFinite(Number(pack?.publishSetVersion))) errors.push('publishSetVersion در tracks.json تعریف نشده است.');
  const seenTrackIds = new Set();
  for (const track of tracks || []) {
    if (!Number.isFinite(Number(track.id))) errors.push(`یک مسیر بدون شناسهٔ عددی وجود دارد: ${track.title || '?'}`);
    if (seenTrackIds.has(track.id)) errors.push(`شناسهٔ مسیر تکراری است: ${track.id}`);
    seenTrackIds.add(track.id);
    for (const section of track.sections || []) {
      const seen = new Set();
      for (const t of section.tutorials || []) {
        if (seen.has(t.id)) errors.push(`توتوریال تکراری در بخش «${section.name}»: ${t.id}`);
        seen.add(t.id);
        if (!Number.isFinite(Number(t.id))) errors.push(`توتوریال بدون شناسه در بخش «${section.name}»`);
      }
    }
  }
  return { ok: errors.length === 0, errors, warnings };
}

/** The tutorial file name the loader expects. spec: HANDOFF/02 §1 */
export function tutorialFileName(tutorialId) {
  return `tutorial-${tutorialId}.json`;
}

/** Flatten a pack into an ordered lesson list: usable for progress and for "next lesson". */
export function flattenLessons(track, tutorialsById) {
  const out = [];
  for (const section of track.sections || []) {
    for (const ref of section.tutorials || []) {
      const tutorial = tutorialsById.get(Number(ref.id));
      if (!tutorial) continue;
      for (const chapter of tutorial.chapters || []) {
        for (const lesson of chapter.lessons || []) {
          out.push({
            trackId: track.id,
            trackVersion: track.version,
            sectionName: section.name,
            tutorialId: tutorial.id,
            tutorialVersion: tutorial.version,
            tutorialTitle: tutorial.title,
            chapterId: chapter.id,
            chapterTitle: chapter.title,
            lessonId: lesson.id,
            lesson,
          });
        }
      }
    }
  }
  return out;
}

export function trackDurationLabel(count) {
  return `${count} درس`;
}
