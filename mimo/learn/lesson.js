/**
 * Lesson runtime — the session loop: open → answer → submit → verdict → feedback → next.
 * spec: HANDOFF/04 §5–§6, HANDOFF/05 §2–§6
 *
 * Engine rule EXT-02 (documented in mimo/docs/DELTAS.md): a lesson may contain several interactions. The lesson
 * verdict aggregates them: any INCORRECT → INCORRECT; else any PARTIAL → PARTIAL; else CORRECT. Mimo's own lessons
 * carried one default interaction per document, so this aggregation is an engine decision, not a recovered fact.
 */

import { CORRECT, PARTIAL, INCORRECT, gradeSelection, gradeValidatedInput, gradeFillTheGap } from './grade.js';
import { parseLesson, extractInteractions } from './dsl.js';
import { isVisible } from './grade.js';

export function createLessonRuntime({ node, lesson, handlers }) {
  const answers = new Map();
  const state = {
    verdict: null,
    submitted: false,
    interactions: [],
    warnings: [],
    errors: [],
  };

  const ctx = {
    verdict: null,
    registerAnswer(el, spec) { answers.set(el, spec); },
    onAnswerChange: handlers?.onAnswerChange,
  };

  function collect() {
    const results = [];
    for (const [wrapper, spec] of answers) {
      if (spec.kind === 'selection') {
        const chosen = [...wrapper.querySelectorAll('.selection-item[aria-checked="true"]')]
          .map((btn) => Number(btn.dataset.index));
        results.push({ wrapper, spec, chosen, verdict: gradeSelection(spec.items, chosen) });
      } else {
        const value = spec.input.value ?? '';
        results.push({
          wrapper,
          spec,
          value,
          verdict: gradeValidatedInput(value, spec.expected),
        });
      }
    }
    return results;
  }

  function resetMarks() {
    for (const wrapper of answers.keys()) {
      wrapper.classList.remove('is-correct', 'is-partial', 'is-wrong');
      const fb = wrapper.querySelector?.('.inline-feedback');
      if (fb) fb.textContent = '';
    }
  }

  function aggregate(results) {
    if (!results.length) return CORRECT; // informational lesson: "continue" is the only action
    if (results.some((r) => r.verdict === INCORRECT)) return INCORRECT;
    if (results.some((r) => r.verdict === PARTIAL)) return PARTIAL;
    return CORRECT;
  }

  function submit() {
    const results = collect();
    const verdict = aggregate(results);
    resetMarks();
    for (const r of results) {
      r.wrapper.classList.add(r.verdict === CORRECT ? 'is-correct' : r.verdict === PARTIAL ? 'is-partial' : 'is-wrong');
      const fb = r.wrapper.querySelector?.('.inline-feedback');
      if (fb) {
        fb.textContent = r.verdict === CORRECT ? 'درست' : r.verdict === PARTIAL ? 'نزدیک بود' : 'نادرست';
      }
    }
    state.verdict = verdict;
    state.submitted = true;
    ctx.verdict = verdict;
    return { verdict, results };
  }

  function applyVisibility(root) {
    for (const el of root.querySelectorAll('[data-visible-if]')) {
      el.hidden = !isVisible(el.dataset.visibleIf, state.verdict);
    }
  }

  return { state, ctx, answers, submit, applyVisibility, collect };
}

/**
 * Wire a rendered lesson: selection toggles and Enter-to-submit.
 * `documentRoot` is the element containing the rendered blocks.
 */
export function wireInteractions(documentRoot) {
  for (const widget of documentRoot.querySelectorAll('.selection')) {
    const multiple = widget.classList.contains('is-multiple');
    for (const item of widget.querySelectorAll('.selection-item')) {
      item.addEventListener('click', () => {
        const on = item.getAttribute('aria-checked') === 'true';
        if (!multiple) {
          for (const other of widget.querySelectorAll('.selection-item')) other.setAttribute('aria-checked', 'false');
          item.setAttribute('aria-checked', on ? 'false' : 'true');
        } else {
          item.setAttribute('aria-checked', on ? 'false' : 'true');
        }
        widget.dispatchEvent(new CustomEvent('answer-change', { bubbles: true }));
      });
    }
  }
  for (const input of documentRoot.querySelectorAll('.answer-input')) {
    input.addEventListener('keydown', (ev) => {
      if (ev.key === 'Enter') {
        ev.preventDefault();
        documentRoot.dispatchEvent(new CustomEvent('answer-submit', { bubbles: true }));
      }
    });
    input.addEventListener('input', () => documentRoot.dispatchEvent(new CustomEvent('answer-change', { bubbles: true })));
  }
}
