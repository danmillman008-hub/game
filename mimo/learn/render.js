/**
 * Renderer — AST → DOM.
 * spec: HANDOFF/03_SPEC_LESSON_DSL.md §4 (blocks, tokens, visibility gating)
 *
 * The renderer never grades. It exposes answer widgets through `registerAnswer` so the lesson runtime owns state.
 */

import { escapeHtml, findFirst, rawTextOf } from './dsl.js';
import { isVisible } from './grade.js';

export function renderDocument(ast, ctx) {
  const root = el('div', { class: 'lesson-body' });
  const blocks = [];
  for (const child of ast.children || []) {
    const node = renderBlock(child, ctx, blocks);
    if (node) root.appendChild(node);
  }
  return { root, blocks };
}

function renderBlock(node, ctx, blocks) {
  const tag = node.tag;
  if (tag === '#text') {
    if (!(node.text || '').trim()) return null;
    return el('p', { class: 'plain-text' }, node.text);
  }
  const visibleIf = node.attrs?.['visible-if'];
  const wrapper = tag === 'p' || tag === 'code' || tag === 'selection' || tag === 'webview' || tag === 'database'
    ? null
    : null;

  let rendered = null;
  switch (tag) {
    case 'h1': case 'h2': case 'h3':
      rendered = el(tag, { class: 'lesson-heading' }, ...renderInline(node.children, ctx, blocks));
      break;
    case 'p':
      rendered = el('p', { class: 'lesson-paragraph' }, ...renderInline(node.children, ctx, blocks));
      break;
    case 'strong': rendered = el('strong', {}, ...renderInline(node.children, ctx, blocks)); break;
    case 'em': rendered = el('em', {}, ...renderInline(node.children, ctx, blocks)); break;
    case 'br': rendered = el('br'); break;
    case 'hr': rendered = el('hr'); break;
    case 'ul': rendered = el('ul', { class: 'lesson-list' }, ...(node.children || []).map((c) => renderBlock(c, ctx, blocks)).filter(Boolean)); break;
    case 'ol': rendered = el('ol', { class: 'lesson-list' }, ...(node.children || []).map((c) => renderBlock(c, ctx, blocks)).filter(Boolean)); break;
    case 'li': rendered = el('li', {}, ...renderInline(node.children, ctx, blocks)); break;
    case 'blockquote': rendered = el('blockquote', { class: 'lesson-quote' }, ...renderInline(node.children, ctx, blocks)); break;
    case 'img': {
      const src = node.attrs.src || '';
      rendered = el('img', { class: 'lesson-image', src, alt: node.attrs.alt || '' });
      break;
    }
    case 'a': {
      const href = node.attrs.href || '#';
      const safe = /^(https?:|#|\/)/i.test(href) ? href : '#';
      rendered = el('a', { class: 'lesson-link', href: safe, target: '_blank', rel: 'noopener noreferrer' }, ...renderInline(node.children, ctx, blocks));
      break;
    }
    case 'code': rendered = renderCode(node, ctx, blocks); break;
    case 'selection': rendered = renderSelection(node, ctx, blocks); break;
    case 'interaction': rendered = renderInlineInteraction(node, ctx); break;
    case 'webview': rendered = renderWebview(node); break;
    case 'database': rendered = renderDatabase(node); break;
    case 'table': rendered = renderTable(node); break;
    case 'output': rendered = el('pre', { class: 'lesson-output' }, rawTextOf(node)); break;
    case 'math': rendered = el('div', { class: 'lesson-math', dir: 'ltr' }, rawTextOf(node)); break;
    case 'diagram': rendered = el('pre', { class: 'lesson-diagram' }, rawTextOf(node)); break;
    case 'audio': rendered = el('audio', { controls: 'controls', src: node.attrs.src || '' }); break;
    default: {
      // unknown tag → render its text, keep the warning (policy: ignore-with-warning, HANDOFF/03 §7)
      const text = rawTextOf(node).trim();
      rendered = text ? el('p', { class: 'lesson-unknown', title: `تگ ناشناخته: <${tag}>` }, text) : null;
    }
  }
  if (!rendered) return null;
  if (visibleIf) {
    rendered.dataset.visibleIf = String(visibleIf).toUpperCase();
    rendered.classList.add('gated');
    rendered.hidden = !isVisible(visibleIf, ctx.verdict || null);
  }
  return rendered;
}

function renderInline(children, ctx, blocks) {
  const out = [];
  for (const child of children || []) {
    if (child.tag === '#text') { out.push(document.createTextNode(child.text || '')); continue; }
    const node = renderBlock(child, ctx, blocks);
    if (node) out.push(node);
  }
  return out;
}

function renderCode(node, ctx, blocks) {
  const content = findFirst(node, 'content');
  const lang = node.attrs.codelang || node.attrs.lang || '';
  const pre = el('pre', { class: 'code-block', dir: 'ltr' });
  const codeEl = el('code', { class: `language-${lang}` });
  const interactions = [];
  const interactionsNode = findFirst(node, 'interactions');
  if (interactionsNode) {
    for (const child of interactionsNode.children || []) if (child.tag === 'interaction') interactions.push(child);
  }

  const tokens = content ? (content.children || []) : [];
  // Flatten tokens to text so startIndex/endIndex (offsets into the code text) can be placed as slot markers.
  const flat = tokens.map((t) => (t.tag === 'text' ? (t.text || '') : rawTextOf(t))).join('');
  const slots = interactions
    .map((i) => ({
      start: Number(i.attrs.startIndex),
      end: Number(i.attrs.endIndex),
      type: i.attrs.type || 'fillTheGap',
      id: i.attrs.id,
      raw: i,
    }))
    .filter((s) => Number.isFinite(s.start) && Number.isFinite(s.end) && s.end >= s.start)
    .sort((a, b) => a.start - b.start);

  let cursor = 0;
  const pushText = (text) => { if (text) codeEl.appendChild(document.createTextNode(text)); };

  const emit = (from, to) => {
    // re-emit the styled tokens covering [from,to)
    let offset = 0;
    for (const token of tokens) {
      const text = token.tag === 'text' ? (token.text || '') : rawTextOf(token);
      const start = offset;
      const end = offset + text.length;
      offset = end;
      if (end <= from || start >= to) continue;
      const sliceStart = Math.max(0, from - start);
      const sliceEnd = Math.min(text.length, to - start);
      const piece = text.slice(sliceStart, sliceEnd);
      if (!piece) continue;
      if (token.tag === 'text' && String(token.attrs?.type || '') === 'break') { codeEl.appendChild(el('br')); continue; }
      const cls = token.attrs?.class;
      if (cls) codeEl.appendChild(el('span', { class: `tok tok-${cls}` }, piece));
      else pushText(piece);
    }
  };

  for (const slot of slots) {
    if (slot.start > cursor) emit(cursor, slot.start);
    const widget = buildInlineWidget({
      id: slot.id || `slot-${slot.start}`,
      type: slot.type === 'validatedInput' ? 'validatedInput' : 'fillTheGap',
      expected: flat.slice(slot.start, slot.end),
      raw: slot.raw,
      ctx,
      inline: true,
    });
    codeEl.appendChild(widget);
    cursor = Math.max(cursor, slot.end);
  }
  if (cursor < flat.length) emit(cursor, flat.length);
  if (!tokens.length && !slots.length) pushText(node.attrs.content || '');

  pre.appendChild(codeEl);
  const wrapper = el('div', { class: 'code-shell' });
  if (node.attrs.name) wrapper.appendChild(el('div', { class: 'code-title' }, node.attrs.name));
  wrapper.appendChild(pre);
  blocks.push({ tag: 'code', node });
  return wrapper;
}

function renderSelection(node, ctx, blocks) {
  const items = (node.children || []).filter((c) => c.tag === 'item');
  const multiple = String(node.attrs.multiple || '') === 'multiple';
  const widget = el('div', { class: `selection ${multiple ? 'is-multiple' : 'is-single'}` });
  widget.dataset.interactionId = node.attrs.id || `selection-${Math.random().toString(36).slice(2, 8)}`;
  const question = node.attrs.question ? el('p', { class: 'selection-question' }, node.attrs.question) : null;
  if (question) widget.appendChild(question);
  const list = el('div', { class: 'selection-items', role: multiple ? 'group' : 'radiogroup' });
  items.forEach((item, index) => {
    const label = item.attrs.label || String.fromCharCode(65 + index);
    const btn = el('button', {
      type: 'button',
      class: 'selection-item',
      role: multiple ? 'checkbox' : 'radio',
      'aria-checked': 'false',
      'data-index': String(index),
    });
    btn.appendChild(el('span', { class: 'option-label' }, toPersianLabel(label)));
    const body = el('span', { class: 'option-body' });
    if (String(node.attrs.iscode || '') === 'true') body.setAttribute('dir', 'ltr');
    body.appendChild(el('span', {}, ...renderInline(item.children, ctx, blocks)));
    btn.appendChild(body);
    list.appendChild(btn);
  });
  widget.appendChild(list);
  ctx.registerAnswer(widget, {
    kind: 'selection',
    multiple,
    items: items.map((it, index) => ({ index, correct: String(it.attrs.correct) === 'true', value: it.attrs.value })),
  });
  blocks.push({ tag: 'selection', node });
  return widget;
}

function renderInlineInteraction(node, ctx) {
  const type = node.attrs.type || 'fillTheGap';
  if (type === 'validatedInput') {
    return buildInlineWidget({
      id: node.attrs.id || `vi-${Math.random().toString(36).slice(2, 8)}`,
      type: 'validatedInput',
      expected: node.attrs.answer ?? '',
      raw: node,
      ctx,
      inline: true,
    });
  }
  return buildInlineWidget({
    id: node.attrs.id || `fg-${Math.random().toString(36).slice(2, 8)}`,
    type: 'fillTheGap',
    expected: node.attrs.answer ?? '',
    raw: node,
    ctx,
    inline: true,
  });
}

/** A text input bound to the lesson answer registry (canonical gap/exact-input behaviour). */
export function buildInlineWidget({ id, type, expected, raw, ctx, inline }) {
  const wrap = el('span', { class: `answer-slot answer-slot--${type}` });
  const input = el('input', {
    type: 'text',
    class: 'answer-input',
    dir: 'auto',
    autocomplete: 'off',
    spellcheck: 'false',
    'aria-label': raw?.attrs?.label || 'پاسخ خود را وارد کنید',
    placeholder: raw?.attrs?.placeholder || '…',
  });
  if (raw?.attrs?.width) input.style.width = `${Number(raw.attrs.width) || 8}ch`;
  else input.style.width = `${Math.max(6, Math.min(28, String(expected || '').length + 4))}ch`;
  wrap.appendChild(input);
  const feedback = el('span', { class: 'inline-feedback', 'aria-live': 'polite' });
  wrap.appendChild(feedback);
  ctx.registerAnswer(wrap, { kind: type, input, expected, id, feedback });
  if (!inline) wrap.classList.add('standalone');
  return wrap;
}

function renderWebview(node) {
  const wrap = el('div', { class: 'webview-block' });
  wrap.appendChild(el('div', { class: 'webview-badge' }, 'محتوای تعبیه‌شده (webview)'));
  const iframe = el('iframe', {
    class: 'webview-frame',
    sandbox: 'allow-scripts',
    srcdoc: node.attrs.content || '',
    title: 'محتوای تعاملی',
  });
  wrap.appendChild(iframe);
  return wrap;
}

function renderDatabase(node) {
  const wrap = el('div', { class: 'database-block' });
  if (node.attrs.bootstrapScript) {
    wrap.appendChild(el('div', { class: 'db-caption' }, 'اسکریپت اولیه (bootstrap)' ));
    wrap.appendChild(el('pre', { class: 'lesson-output' }, node.attrs.bootstrapScript));
  }
  const tables = findFirst(node, 'tables');
  for (const table of tables ? tables.children.filter((c) => c.tag === 'table') : []) {
    wrap.appendChild(renderTable(table));
  }
  const output = findFirst(node, 'output');
  if (output) wrap.appendChild(el('pre', { class: 'lesson-output' }, rawTextOf(output)));
  return wrap;
}

function renderTable(node) {
  const table = el('table', { class: 'lesson-table' });
  const headers = (node.children || []).filter((c) => c.tag === 'header');
  if (headers.length) {
    const thead = el('thead');
    const tr = el('tr');
    for (const h of headers) tr.appendChild(el('th', {}, h.attrs.content || rawTextOf(h)));
    thead.appendChild(tr);
    table.appendChild(thead);
  }
  const tbody = el('tbody');
  for (const row of (node.children || []).filter((c) => c.tag === 'row')) {
    const tr = el('tr');
    for (const cell of (row.children || []).filter((c) => c.tag === 'data')) {
      tr.appendChild(el('td', {}, cell.attrs.content || rawTextOf(cell)));
    }
    tbody.appendChild(tr);
  }
  if (tbody.children.length) table.appendChild(tbody);
  return table;
}

/* --- helpers --------------------------------------------------------------------------------------------- */

export function el(tag, attrs = {}, ...children) {
  const node = document.createElement(tag);
  for (const [key, value] of Object.entries(attrs || {})) {
    if (value == null) continue;
    if (key === 'class') node.className = value;
    else if (key === 'srcdoc') node.srcdoc = value;
    else node.setAttribute(key, String(value));
  }
  for (const child of children) {
    if (child == null) continue;
    node.appendChild(typeof child === 'string' ? document.createTextNode(child) : child);
  }
  return node;
}

const PERSIAN_LABELS = ['الف', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح'];
function toPersianLabel(label) {
  const idx = 'ABCDEFGH'.indexOf(String(label).toUpperCase());
  return idx >= 0 ? PERSIAN_LABELS[idx] : label;
}

export { escapeHtml };
