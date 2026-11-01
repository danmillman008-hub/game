/**
 * Persian localization layer for the embedded engines (EPM and LearnHarness).
 *
 * Why a runtime layer instead of rewriting the applications: both engines are large third-party products with their
 * own string tables baked into templates and bundles. Rewriting their business logic to localize them would violate
 * the "reuse, do not rebuild" rule and would diverge from the pinned upstream sources. This layer
 *   · sets `lang="fa"` and `dir="rtl"`,
 *   · translates text nodes and user-visible attributes against a curated dictionary,
 *   · never touches code, formulas, user content or imported question text,
 *   · keeps an audit of the strings it could not translate.
 *
 * The dictionary is served from the same host (`/__overlay/dict-epm.json`, `/__overlay/dict-max.json`).
 * Documented in mimo/docs/LOCALIZATION.md.
 */
(() => {
  'use strict';

  const path = location.pathname;
  const ENGINE = path.startsWith('/practice') ? 'epm' : path.startsWith('/max') ? 'max' : null;
  if (!ENGINE) return;

  const AUDIT = new URLSearchParams(location.search).has('fa-audit')
    || localStorage.getItem('mimo.fa.audit') === '1';

  const SKIP_TAGS = new Set(['SCRIPT', 'STYLE', 'CODE', 'PRE', 'KBD', 'SAMP', 'TEXTAREA', 'SVG', 'MATH', 'CANVAS', 'IFRAME']);
  const SKIP_SELECTOR = [
    '.katex', '.mermaid', '.monaco-editor', '.cm-editor', '.cm-content', '.hljs', '[data-no-translate]',
    '[translate="no"]', '.lh-graph', '.react-flow', '.source-view', '.document-view', '.pdf-viewer',
    'input[type="password"]', '[contenteditable="true"]',
  ].join(',');

  const CJK = /[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]/;
  const LATIN = /[A-Za-z]/;

  let dict = {};
  let patterns = [];
  const missed = new Map();
  let translating = false;

  function norm(text) {
    return text.replace(/\s+/g, ' ').trim();
  }

  function translateString(raw) {
    const key = norm(raw);
    if (!key) return null;
    if (dict[key]) return dict[key];
    for (const [re, replacement] of patterns) {
      if (re.test(key)) {
        const out = key.replace(re, replacement);
        if (out !== key) return out;
      }
    }
    return null;
  }

  function shouldSkip(node) {
    const parent = node.parentElement;
    if (!parent) return true;
    if (SKIP_TAGS.has(parent.tagName)) return true;
    if (parent.closest(SKIP_SELECTOR)) return true;
    return false;
  }

  function recordMiss(text) {
    if (!AUDIT) return;
    const key = norm(text);
    if (!key || (!CJK.test(key) && !(ENGINE === 'max' && LATIN.test(key)))) return;
    missed.set(key, (missed.get(key) || 0) + 1);
  }

  function translateTextNode(node) {
    const raw = node.nodeValue;
    if (!raw || !raw.trim()) return;
    const out = translateString(raw);
    if (out === null) {
      recordMiss(raw);
      return;
    }
    if (node.nodeValue !== out) node.nodeValue = out;
  }

  const ATTRS = ['placeholder', 'title', 'aria-label', 'alt', 'data-placeholder'];

  function translateAttributes(el) {
    for (const attr of ATTRS) {
      if (!el.hasAttribute || !el.hasAttribute(attr)) continue;
      const value = el.getAttribute(attr);
      const out = translateString(value);
      if (out !== null && out !== value) el.setAttribute(attr, out);
    }
  }

  function walk(root) {
    if (!root) return;
    if (root.nodeType === Node.TEXT_NODE) {
      if (!shouldSkip(root)) translateTextNode(root);
      return;
    }
    if (root.nodeType !== Node.ELEMENT_NODE && root.nodeType !== Node.DOCUMENT_NODE) return;
    if (root.nodeType === Node.ELEMENT_NODE) {
      if (SKIP_TAGS.has(root.tagName) || (root.matches && root.matches(SKIP_SELECTOR))) return;
      translateAttributes(root);
    }
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT | NodeFilter.SHOW_ELEMENT, null);
    const batch = [];
    let current = walker.nextNode();
    while (current) {
      batch.push(current);
      current = walker.nextNode();
    }
    for (const node of batch) {
      if (node.nodeType === Node.TEXT_NODE) {
        if (!shouldSkip(node)) translateTextNode(node);
      } else {
        if (SKIP_TAGS.has(node.tagName) || (node.matches && node.matches(SKIP_SELECTOR))) continue;
        translateAttributes(node);
      }
    }
  }

  function applyDirection() {
    const html = document.documentElement;
    html.setAttribute('lang', 'fa');
    html.setAttribute('dir', 'rtl');
    const style = document.createElement('style');
    style.id = 'mimo-fa-style';
    style.textContent = `
      html[dir="rtl"] body { text-align: right; }
      html[dir="rtl"] pre, html[dir="rtl"] code, html[dir="rtl"] .katex, html[dir="rtl"] .cm-editor,
      html[dir="rtl"] textarea, html[dir="rtl"] input[type="url"], html[dir="rtl"] input[type="email"] {
        direction: ltr; text-align: left; unicode-bidi: isolate;
      }
      html[dir="rtl"] .mimo-fa-badge {
        position: fixed; inset-block-end: 8px; inset-inline-start: 8px; z-index: 2147483000;
        background: rgba(15,61,46,.86); color: #eaf6ee; font: 11px/1.6 system-ui, sans-serif;
        padding: 3px 8px; border-radius: 999px; pointer-events: none; letter-spacing: .2px;
      }
    `;
    (document.head || html).appendChild(style);
  }

  function startObserver() {
    const observer = new MutationObserver((mutations) => {
      if (translating) return;
      translating = true;
      try {
        for (const mutation of mutations) {
          for (const node of mutation.addedNodes) walk(node);
          if (mutation.type === 'characterData') {
            const node = mutation.target;
            if (!shouldSkip(node)) translateTextNode(node);
          }
        }
      } finally {
        translating = false;
      }
    });
    observer.observe(document.body, { childList: true, subtree: true, characterData: true });
  }

  async function loadDictionary() {
    try {
      const res = await fetch(`/__overlay/dict-${ENGINE}.json`, { cache: 'no-store' });
      if (!res.ok) return;
      const payload = await res.json();
      dict = payload.strings || payload;
      patterns = (payload.patterns || []).map(([re, repl]) => [new RegExp(re), repl]);
    } catch (err) {
      console.warn('[mimo-fa] dictionary unavailable', err);
    }
  }

  async function flushAudit() {
    if (!AUDIT || !missed.size) return;
    const payload = {
      engine: ENGINE,
      route: location.pathname + location.hash,
      missing: [...missed.entries()].sort((a, b) => b[1] - a[1]).map(([text, count]) => ({ text, count })),
    };
    try {
      await fetch('/api/preview/i18n-missing', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
        keepalive: true,
      });
    } catch { /* console table below is the fallback */ }
    console.info(`[mimo-fa] ${payload.missing.length} untranslated strings on this screen`, payload.missing.slice(0, 40));
  }

  async function boot() {
    await loadDictionary();
    applyDirection();
    // the SPA mounts after this script; translate repeatedly during hydration, then settle
    let rounds = 0;
    const tick = () => {
      translating = true;
      try { walk(document.body); } finally { translating = false; }
      rounds += 1;
      if (rounds < 12) setTimeout(tick, rounds < 4 ? 120 : 500);
      else { flushAudit(); window.__MIMO_FA__ = { translated: Object.keys(dict).length, missed: missed.size }; }
    };
    tick();
    startObserver();
    // EPM registers a service worker; under a path prefix its scope is wrong and it would cache stale bundles
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.getRegistrations().then((regs) => regs.forEach((r) => r.unregister())).catch(() => {});
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot, { once: true });
  else boot();
})();
