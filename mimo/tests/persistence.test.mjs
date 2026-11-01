/** Progress persistence test: save after grading, reload from the same storage, verify the row and stats survive. */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import { JSDOM } from 'jsdom';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const MIMO = path.resolve(HERE, '..');
const dom = new JSDOM('<!doctype html><html><body></body></html>', { url: 'http://localhost:4000/' });
globalThis.window = dom.window;
globalThis.document = dom.window.document;
globalThis.localStorage = dom.window.localStorage;

const store = await import('../learn/store.js');
const pack = JSON.parse(readFileSync(path.join(MIMO, 'content/demo/tutorial-101.json'), 'utf8'));
const chapter = pack.chapters[0];
const lesson = chapter.lessons[0];

test('a graded lesson writes a row that survives a reload', () => {
  store.clearState();
  const state = store.loadState();
  const row = store.ensureRow(state, {
    lessonId: lesson.id,
    tutorialId: pack.id,
    tutorialVersion: pack.version ?? 1,
    trackId: 101,
    publishSetVersion: 1,
  });
  // the real submission counter mirrors Mimo's 0/1 `tries` flag and an attempt counter
  store.applyResult(state, row, 'CORRECT', (verdict, previousWasWrong, attempts) => ({
    attempts: attempts + 1,
    tries: 1,
    previousWasWrong: verdict !== 'CORRECT',
  }));
  store.saveState(state);

  const reloaded = store.loadState();
  const again = store.getRow(reloaded, lesson.id, pack.id);
  assert.ok(again, 'row persisted');
  assert.equal(again.lastVerdict, 'CORRECT');
  assert.ok(again.tries >= 1, 'tries flagged');
  assert.equal(reloaded.user, 'local');
  assert.equal(reloaded.schemaVersion, store.SCHEMA_VERSION);
});

test('chapter progress reflects the graded lesson after reload', () => {
  const state = store.loadState();
  const progress = store.chapterProgress(state, chapter, pack.id);
  assert.ok(progress.total >= 1);
  assert.equal(progress.solved, 1, `progress=${JSON.stringify(progress)}`);
});

test('storage key is the documented one and the payload is JSON', () => {
  const raw = dom.window.localStorage.getItem(store.STORAGE_KEY);
  assert.equal(store.STORAGE_KEY, 'mimo.learn.progress.v1');
  assert.doesNotThrow(() => JSON.parse(raw));
});
