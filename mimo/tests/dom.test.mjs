/**
 * DOM-level engine test (jsdom): render a real lesson from the demo pack, answer it, and assert the graded outcome.
 * This is the browser-free equivalent of clicking through the lesson in the preview.
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import { JSDOM } from 'jsdom';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const MIMO = path.resolve(HERE, '..');

const dom = new JSDOM('<!doctype html><html><body><div id="host"></div></body></html>', { pretendToBeVisual: true });
globalThis.window = dom.window;
globalThis.document = dom.window.document;
globalThis.Node = dom.window.Node;
globalThis.NodeFilter = dom.window.NodeFilter;
globalThis.CustomEvent = dom.window.CustomEvent;
globalThis.MutationObserver = dom.window.MutationObserver;

const { parseLesson } = await import('../learn/dsl.js');
const { renderDocument } = await import('../learn/render.js');
const { createLessonRuntime, wireInteractions } = await import('../learn/lesson.js');
const { isVisible } = await import('../learn/grade.js');

const pack = JSON.parse(readFileSync(path.join(MIMO, 'content/demo/tutorial-101.json'), 'utf8'));
const lesson = pack.chapters[0].lessons[0];

function mount(bodySource) {
  const ast = parseLesson(bodySource);
  assert.equal(ast.errors.length, 0, `parse errors: ${JSON.stringify(ast.errors)}`);
  const host = document.getElementById('host');
  host.innerHTML = '';
  const runtime = createLessonRuntime({ node: host, lesson, handlers: {} });
  const { root, blocks } = renderDocument(ast.ast, runtime.ctx);
  host.appendChild(root);
  wireInteractions(host);
  return { host, runtime, blocks };
}

test('a real lesson renders its blocks and interactions', () => {
  const { host, runtime } = mount(lesson.body);
  assert.ok(host.querySelector('.lesson-paragraph'), 'paragraph rendered');
  assert.ok(host.querySelector('.selection'), 'selection rendered');
  assert.ok(host.querySelector('.answer-input'), 'inline gap rendered');
  assert.equal(runtime.answers.size, 2, 'two interactions registered');
});

test('correct answers produce CORRECT and reveal only the correct/wrong blocks', () => {
  const { host, runtime } = mount(lesson.body);
  // single-choice: the second item is the correct one in lesson 9001
  const items = host.querySelectorAll('.selection-item');
  assert.ok(items.length >= 2);
  const correctIndex = [...items].findIndex((el, i) => lesson.body.includes('correct="true"') && i === 1);
  items[correctIndex].setAttribute('aria-checked', 'true');
  // inline gap expects ∈
  host.querySelector('.answer-input').value = '∈';
  const { verdict } = runtime.submit();
  assert.equal(verdict, 'CORRECT');
  runtime.applyVisibility(host);
  const correctBlock = host.querySelector('[data-visible-if="CORRECT"]');
  const wrongBlock = host.querySelector('[data-visible-if="WRONG"]');
  assert.equal(correctBlock.hidden, false);
  assert.equal(wrongBlock.hidden, true);
});

test('a wrong answer produces INCORRECT and shows the wrong-hint block', () => {
  const { host, runtime } = mount(lesson.body);
  const items = host.querySelectorAll('.selection-item');
  items[0].setAttribute('aria-checked', 'true');
  host.querySelector('.answer-input').value = '∉';
  const { verdict } = runtime.submit();
  assert.equal(verdict, 'INCORRECT');
  runtime.applyVisibility(host);
  assert.equal(host.querySelector('[data-visible-if="WRONG"]').hidden, false);
  assert.equal(host.querySelector('[data-visible-if="CORRECT"]').hidden, true);
});

test('a normalisation-only difference produces PARTIAL (validatedInput only)', () => {
  const src = '<p>مقدار <interaction type="validatedInput" answer="x = 1" label="مقدار"/> را بنویسید.</p>';
  const { host, runtime } = mount(src);
  host.querySelector('.answer-input').value = 'x=1';
  const { verdict } = runtime.submit();
  assert.equal(verdict, 'PARTIAL');
});

test('selection with multiple="multiple" is all-or-nothing', () => {
  const src = `<selection multiple="multiple" question="درست‌ها">
    <item value="1" correct="true">الف</item>
    <item value="2" correct="true">ب</item>
    <item value="3" correct="false">پ</item>
  </selection>`;
  const { host, runtime } = mount(src);
  const items = host.querySelectorAll('.selection-item');
  items[0].setAttribute('aria-checked', 'true');
  items[1].setAttribute('aria-checked', 'true');
  assert.equal(runtime.submit().verdict, 'CORRECT');
  const again = mount(src);
  const its = again.host.querySelectorAll('.selection-item');
  its[0].setAttribute('aria-checked', 'true');
  assert.equal(again.runtime.submit().verdict, 'INCORRECT');
});

test('visibility helper matches the recovered table', () => {
  assert.equal(isVisible('ALWAYS', 'INCORRECT'), true);
  assert.equal(isVisible('CORRECT', 'INCORRECT'), false);
  assert.equal(isVisible('CORRECT', 'CORRECT'), true);
  assert.equal(isVisible('WRONG', 'CORRECT'), false);
  assert.equal(isVisible('WRONG', 'INCORRECT'), true);
});
