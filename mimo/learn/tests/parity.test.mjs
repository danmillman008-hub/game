/**
 * Parity tests: the engine must reproduce the recovered vectors from HANDOFF/data/*.json exactly.
 * Run: node --test mimo/learn/tests
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

import { normalise, gradeValidatedInput, gradeSelection, gradeFillTheGap, gradeSpell,
  isVisible, applySubmission, isSolved, chapterIsComplete, firstTryCount, answersInChapter } from '../grade.js';
import { parseLesson, extractInteractions } from '../dsl.js';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const DATA = path.resolve(HERE, '../../../HANDOFF/data');
const G = JSON.parse(readFileSync(path.join(DATA, 'grading_vectors.json'), 'utf8'));
const P = JSON.parse(readFileSync(path.join(DATA, 'progress_vectors.json'), 'utf8'));

test('normaliser matches every source-derived vector', () => {
  for (const v of G.normaliser.vectors) assert.equal(normalise(v.input), v.expected, v.input);
});

test('validatedInput verdicts match (incl. the PARTIAL raw-equality trap)', () => {
  for (const v of G.validated_input_verdict.vectors) {
    assert.equal(gradeValidatedInput(v.user, v.expected), v.verdict, `${v.user} vs ${v.expected}`);
  }
});

test('selection verdicts match (all-or-nothing, empty guard)', () => {
  for (const v of G.selection_verdict.vectors) {
    const chosen = v.items.map((it, i) => (it.selected ? i : null)).filter((x) => x !== null);
    // the vector annotates the empty-selection guard as "INCORRECT (empty guard)"; the verdict itself is INCORRECT
    const expected = v.verdict.startsWith('INCORRECT') ? 'INCORRECT' : v.verdict;
    assert.equal(gradeSelection(v.items.map((it, i) => ({ index: i, correct: it.correct })), chosen), expected);
  }
});

test('fill-the-gap and spell verdicts match', () => {
  for (const v of G.fill_the_gap_verdict.vectors) assert.equal(gradeFillTheGap(v.selected, v.expected), v.verdict);
  for (const v of G.spell_verdict.vectors) assert.equal(gradeSpell(v.selected, v.expected), v.verdict);
});

test('visibility gating matches', () => {
  for (const v of G.module_visibility.vectors) assert.equal(isVisible(v.visibility, v.verdict), v.rendered);
});

test('progress completion flag matches', () => {
  for (const v of G.progress_completion.vectors) assert.equal(isSolved(v.tries), v.solved);
});

test('counter update sites (V/W/X/U) match every vector', () => {
  for (const v of P.counter_update.vectors) {
    const c = v.C_before === 'null' ? null : v.C_before;
    const out = applySubmission(v.verdict, c, v.d_before);
    // vector naming: C_after == the engine's `previousWasWrong` flag after the submission
    const got = { ...out, C_after: out.previousWasWrong };
    for (const [field, expected] of Object.entries(v.expected)) {
      assert.equal(got[field], expected, `${v.verdict} ${field}`);
    }
  }
});

test('tries stays a 0/1 flag across repeated correct submissions', () => {
  let attempts = 0; let tries = 1; let c = false;
  for (let i = 0; i < 5; i += 1) {
    const out = applySubmission('CORRECT', c, attempts);
    attempts = out.attempts; tries = out.tries; c = out.previousWasWrong;
    assert.ok(tries === 0 || tries === 1);
  }
  assert.equal(tries, 1);
});

test('derived metrics: first try and chapter answers', () => {
  const rows = P.first_try_count.vectors[0].rows;
  assert.equal(firstTryCount(rows), P.first_try_count.vectors[0].expected);
  const chapter = P.answers_in_chapter.vectors[0];
  assert.deepEqual(answersInChapter(chapter.rows), chapter.expected);
});

test('ADD-04 local completion rule', () => {
  assert.equal(chapterIsComplete([{ tries: 0 }, { tries: 0 }]), false);
  assert.equal(chapterIsComplete([{ tries: 1 }, { tries: 0 }]), false);
  assert.equal(chapterIsComplete([{ tries: 1 }, { tries: 1 }]), true);
  assert.equal(chapterIsComplete([]), false);
});

/* ---- DSL ----------------------------------------------------------------------------------------------- */

test('parses a paragraph and inline formatting', () => {
  const { ast, errors } = parseLesson('<p>سلام <strong>دنیا</strong></p>');
  assert.equal(errors.length, 0);
  assert.equal(ast.children[0].tag, 'p');
  assert.ok(ast.children[0].children.some((c) => c.tag === 'strong'));
});

test('parses a canonical code block with an interaction range', () => {
  const src = '<code codelang="js" version="2"><content><text class="keyword">let</text> x = 1;</content>'
    + '<interactions><interaction type="validatedInput" startIndex="4" endIndex="9"/></interactions></code>';
  const { ast, errors } = parseLesson(src);
  assert.equal(errors.length, 0);
  const [interaction] = extractInteractions(ast);
  assert.equal(interaction.type, 'validatedInput');
  assert.equal(interaction.start, 4);
  assert.equal(interaction.end, 9);
});

test('parses a selection with correct flags', () => {
  const src = '<selection><item value="1" correct="true">الف</item><item value="2">ب</item></selection>';
  const { ast } = parseLesson(src);
  const [sel] = extractInteractions(ast);
  assert.equal(sel.type, 'selection.single');
  assert.equal(sel.items.length, 2);
  assert.equal(sel.items[0].correct, true);
});

test('unknown tags are warnings, not crashes', () => {
  const { warnings } = parseLesson('<video src="x"></video>');
  assert.ok(warnings.length >= 1);
});

test('malformed input returns typed errors', () => {
  const { errors } = parseLesson('<p class="x>unclosed</p>');
  assert.ok(errors.length >= 1);
  assert.ok(errors[0].code.startsWith('E_'));
});

test('empty document is an error, never thrown', () => {
  const { errors } = parseLesson('');
  assert.equal(errors[0].code, 'E_EMPTY_DOCUMENT');
});
