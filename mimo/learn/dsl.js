/**
 * Lesson DSL parser — the engine's implementation of the recovered Mimo contract.
 * spec: HANDOFF/03_SPEC_LESSON_DSL.md (grammar at HANDOFF/data/dsl_grammar.ebnf)
 *
 * The parser is deliberately small and strict-ish: it builds an AST from the tag stream, reports typed errors,
 * and never throws on malformed input that a learner could trigger. Unknown tags are kept as
 * `unknown` nodes and reported as warnings (policy `ignore-with-warning`, HANDOFF/03 §7).
 */

export const TAGS = Object.freeze([
  'html', 'body', 'head', 'style', 'p', 'code', 'content', 'text', 'strong', 'em', 'br', 'img', 'a',
  'selection', 'item', 'interactions', 'interaction', 'options', 'option', 'webview',
  'database', 'tables', 'table', 'header', 'row', 'data', 'output', 'h1', 'h2', 'h3', 'ul', 'ol', 'li',
  'blockquote', 'hr', 'math', 'diagram', 'grammar', 'audio',
]);

/** Tags the recovered grammar defines. Anything else is `unknown` + warning. */
const KNOWN = new Set(TAGS);
/** Structural tags that never carry visible text. */
const VOID = new Set(['br', 'img', 'hr', 'interaction']);

const ATTR_RE = /([a-zA-Z_][a-zA-Z0-9_:.-]*)(?:\s*=\s*("([^"]*)"|'([^']*)'|([^\s"'>/]+)))?/g;

export function parseAttributes(raw) {
  const attrs = {};
  let m;
  ATTR_RE.lastIndex = 0;
  while ((m = ATTR_RE.exec(raw))) {
    const value = m[3] ?? m[4] ?? m[5] ?? '';
    attrs[m[1]] = decodeEntities(value);
  }
  return attrs;
}

export function decodeEntities(text) {
  return String(text)
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&');
}

export function escapeHtml(text) {
  return String(text)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function node(tag, attrs = {}, children = [], extra = {}) {
  return { kind: tag, tag, attrs, children, text: extra.text ?? null, span: extra.span ?? null };
}

/**
 * @param {string} source
 * @returns {{ast: object, errors: Array<{code:string,message:string,offset:number}>, warnings: string[]}}
 */
export function parseLesson(source) {
  const errors = [];
  const warnings = [];
  const root = { kind: 'document', tag: '#document', attrs: {}, children: [], text: null };
  const stack = [root];
  const src = String(source ?? '');
  let i = 0;

  const top = () => stack[stack.length - 1];

  while (i < src.length) {
    const lt = src.indexOf('<', i);
    if (lt === -1) {
      pushText(src.slice(i), i);
      break;
    }
    if (lt > i) pushText(src.slice(i, lt), i);

    // comment / doctype / cdata
    if (src.startsWith('<!--', lt)) {
      const end = src.indexOf('-->', lt + 4);
      if (end === -1) { errors.push(err('E_UNCLOSED_COMMENT', 'کامنت بسته نشده است', lt)); break; }
      i = end + 3;
      continue;
    }
    if (src.startsWith('<!', lt)) {
      const end = src.indexOf('>', lt);
      if (end === -1) break;
      i = end + 1;
      continue;
    }
    // closing tag
    const closeMatch = /^<\/\s*([a-zA-Z][a-zA-Z0-9-]*)\s*>/.exec(src.slice(lt, lt + 80));
    if (closeMatch) {
      const tag = closeMatch[1].toLowerCase();
      const idx = findOpen(stack, tag);
      if (idx === -1) {
        warnings.push(`بستن تگِ بازنشده <${tag}> نادیده گرفته شد`);
      } else {
        while (stack.length - 1 > idx) {
          const unclosed = stack.pop();
          warnings.push(`تگ <${unclosed.tag}> بسته نشده بود و خودکار بسته شد`);
        }
        stack.pop();
      }
      i = lt + closeMatch[0].length;
      continue;
    }
    // opening tag
    const openMatch = /^<\s*([a-zA-Z][a-zA-Z0-9-]*)((?:"[^"]*"|'[^']*'|[^>"'])*?)(\/?)>/.exec(src.slice(lt));
    if (!openMatch) {
      errors.push(err('E_BAD_TAG', 'تگ نامعتبر یا ناقص است', lt));
      pushText('<', lt);
      i = lt + 1;
      continue;
    }
    const tag = openMatch[1].toLowerCase();
    const attrs = parseAttributes(openMatch[2] || '');
    const selfClosing = openMatch[3] === '/' || VOID.has(tag);
    const element = node(tag, attrs);
    if (!KNOWN.has(tag)) {
      element.unknown = true;
      warnings.push(`تگ ناشناخته <${tag}> به‌صورت محتوای متنی نمایش داده می‌شود`);
    }
    top().children.push(element);
    i = lt + openMatch[0].length;
    if (!selfClosing) stack.push(element);
  }

  while (stack.length > 1) {
    const unclosed = stack.pop();
    warnings.push(`تگ <${unclosed.tag}> در پایان سند بسته نشده بود`);
  }

  if (!errors.length && !root.children.length) {
    errors.push(err('E_EMPTY_DOCUMENT', 'سند درس خالی است', 0));
  }

  return { ast: normalize(root), errors, warnings };

  function pushText(raw, offset) {
    if (!raw) return;
    const text = decodeEntities(raw);
    if (!text.trim() && !/\S/.test(text)) {
      // keep meaningful spaces between inline elements only when inside rich text
      if (text.includes(' ')) top().children.push(node('#text', {}, [], { text, span: [offset, offset + raw.length] }));
      return;
    }
    top().children.push(node('#text', {}, [], { text, span: [offset, offset + raw.length] }));
  }
}

function findOpen(stack, tag) {
  for (let k = stack.length - 1; k >= 1; k -= 1) if (stack[k].tag === tag) return k;
  return -1;
}

function err(code, message, offset) {
  return { code, message, offset };
}

/** Collapse the wrapper elements so callers get a flat, predictable tree. */
function normalize(root) {
  const body = findFirst(root, 'body') || root;
  return {
    kind: 'document',
    attrs: {},
    children: body.children.filter((c) => !(c.kind === '#text' && !(c.text || '').trim())),
    findings: [],
  };
}

export function findFirst(n, tag) {
  for (const c of n.children || []) {
    if (c.tag === tag) return c;
    const hit = findFirst(c, tag);
    if (hit) return hit;
  }
  return null;
}

/* ------------------------------------------------------------------------------------------------------------
 * Interaction extraction
 * ---------------------------------------------------------------------------------------------------------- */

/**
 * Walk the AST and extract every interaction with the code/text it refers to.
 *
 * Canonical Mimo shapes (HANDOFF/03 §3):
 *   <code ...><content>…</content><interactions>
 *      <interaction type="validatedInput" startIndex="N" endIndex="M"/>
 *      <interaction type="fillTheGap"><options><option startIndex endIndex/>…</options></interaction>
 *   </interactions></code>
 *   <selection multiple|single><item value correct>…</item></selection>
 *
 * Engine extension EXT-01 (documented in mimo/docs/DELTAS.md): a bare <interaction type="fillTheGap"> may appear
 * inside a <p>; its prompt text is the paragraph text and the expected answer is the attribute `answer`
 * (or the first <option> child for canonical packs).
 */
export function extractInteractions(ast) {
  const out = [];
  walk(ast, (n) => {
    if (n.tag === 'selection') out.push(selectionInteraction(n));
    else if (n.tag === 'interaction') out.push(gapOrInputInteraction(n));
  });
  return out.filter(Boolean);
}

function walk(n, fn) {
  fn(n);
  for (const c of n.children || []) walk(c, fn);
}

function textOf(n) {
  if (n.text != null) return n.text;
  return (n.children || []).map(textOf).join('');
}

/** Raw text of a node, with no entity decoding surprises for offsets. */
export function rawTextOf(n) {
  return textOf(n);
}

function selectionInteraction(nodeEl) {
  const items = (nodeEl.children || []).filter((c) => c.tag === 'item');
  const multiple = String(nodeEl.attrs.multiple || '') === 'multiple';
  const isCode = String(nodeEl.attrs.iscode || '') === 'true';
  return {
    id: nodeEl.attrs.id || `sel-${items.map((i) => i.attrs.value).join('-')}`,
    type: multiple ? 'selection.multiple' : 'selection.single',
    block: 'selection',
    isCode,
    items: items.map((it, index) => ({
      index,
      value: it.attrs.value ?? String(index),
      label: it.attrs.label || String.fromCharCode(65 + index),
      correct: String(it.attrs.correct) === 'true',
      text: textOf(it).trim(),
      children: it.children,
    })),
    node: nodeEl,
  };
}

function gapOrInputInteraction(nodeEl) {
  const type = nodeEl.attrs.type || 'fillTheGap';
  const start = Number(nodeEl.attrs.startIndex);
  const end = Number(nodeEl.attrs.endIndex);
  const optionsNode = (nodeEl.children || []).find((c) => c.tag === 'options');
  const ranges = optionsNode
    ? optionsNode.children.filter((c) => c.tag === 'option').map((o) => ({
        start: Number(o.attrs.startIndex),
        end: Number(o.attrs.endIndex),
        correct: String(o.attrs.correct) !== 'false',
        text: textOf(o).trim(),
      }))
    : [];
  const parentCode = null; // resolved by caller when the interaction lives in a <code> block
  return {
    id: nodeEl.attrs.id || `int-${type}-${start}-${end}`,
    type: type === 'validatedInput' ? 'validatedInput' : 'fillTheGap',
    block: 'interaction',
    start: Number.isFinite(start) ? start : null,
    end: Number.isFinite(end) ? end : null,
    isDefault: String(nodeEl.attrs.isDefault || '') === 'true',
    ranges,
    answer: nodeEl.attrs.answer ?? (ranges.find((r) => r.correct)?.text ?? null),
    prompt: nodeEl.attrs.prompt ?? null,
    parentCode,
    node: nodeEl,
  };
}

/** The source string an interaction's startIndex/endIndex refer to. */
export function interactionSource(interaction, blocks) {
  const owner = blocks.find((b) => b.tag === 'code' && contains(b.node, interaction.node));
  if (owner) {
    const content = findFirst(owner.node, 'content');
    return content ? textOf(content) : '';
  }
  const p = blocks.find((b) => contains(b.node, interaction.node));
  return p ? textOf(p.node) : '';
}

function contains(root, target) {
  if (root === target) return true;
  for (const c of root.children || []) if (contains(c, target)) return true;
  return false;
}
