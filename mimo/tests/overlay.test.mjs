/**
 * Localization-layer test (jsdom): the Persian overlay must translate UI text, leave code alone, and flip the page
 * to RTL. Run: node --test mimo/tests
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import { JSDOM } from 'jsdom';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const MIMO = path.resolve(HERE, '..');
const overlay = readFileSync(path.join(MIMO, 'host/overlay/fa.js'), 'utf8');
const dict = JSON.parse(readFileSync(path.join(MIMO, 'host/overlay/dict-epm.json'), 'utf8'));

test('dictionary covers the EPM navigation labels', () => {
  const nav = ['首页', '题库与练习', '模拟考试', '阅读训练', '听力精听', '单词本', '分析与诊断', '错题本',
    '学习诊断', '学习报告', '我的笔记', '成就徽章', '学习排行', 'AI 助手与精批', '作文精批', '口语陪练',
    'AI 学习助手', '规划与配置', '专注计时', '学习日历', '目标中心', '导入题库', '模型与设置',
    '组织管理', '设置组织'];
  const missing = nav.filter((label) => !dict.strings[label]);
  assert.deepEqual(missing, [], `untranslated navigation labels: ${missing.join(', ')}`);
});

test('dictionary has no empty or identical-to-source translations', () => {
  for (const [key, value] of Object.entries(dict.strings)) {
    assert.ok(value && value.trim().length > 0, `empty translation for ${key}`);
    assert.notEqual(value, key, `untranslated entry: ${key}`);
  }
});

test('the overlay translates UI text, keeps code, and sets RTL', async () => {
  const html = `<!doctype html><html lang="zh-CN"><head></head><body>
    <nav><a>首页</a><a>错题本</a></nav>
    <p>加载中…</p>
    <pre><code>取消</code></pre>
    <input placeholder="搜索" />
  </body></html>`;
  const dom = new JSDOM(html, { url: 'http://localhost:4000/practice/', runScripts: 'outside-only' });
  const { window } = dom;
  window.fetch = async (url) => ({
    ok: true,
    json: async () => (String(url).includes('dict-epm') ? dict : {}),
  });
  window.eval(overlay);
  await new Promise((r) => setTimeout(r, 900));

  assert.equal(window.document.documentElement.getAttribute('dir'), 'rtl');
  assert.equal(window.document.documentElement.getAttribute('lang'), 'fa');
  const navText = [...window.document.querySelectorAll('nav a')].map((a) => a.textContent);
  assert.deepEqual(navText, ['صفحهٔ اصلی', 'دفتر اشتباهات']);
  assert.equal(window.document.querySelector('p').textContent, 'در حال بارگذاری…');
  // code must never be translated
  assert.equal(window.document.querySelector('code').textContent, '取消');
  assert.equal(window.document.querySelector('input').getAttribute('placeholder'), 'جست‌وجو');
});
