/**
 * «ساختار توکنها» — economy half.
 *
 * Rules are a LOCAL, deterministic interpretation of
 * mimo-ui/UPGRADE/CATALOGS/GAMIFICATION_MAP.csv (12 observed reward events).
 * They are explicitly NOT server-confirmed formulas: nothing here claims to
 * reproduce Mimo's backend. Every mutation is written to a local ledger so the
 * structure is inspectable, exportable and reversible.
 */
import { faNum, stamp } from './util.js';

export const DAILY_XP_CAP = 400;

export const TOKEN_KINDS = Object.freeze([
  { key: 'coins', fa: 'سکه / Sparks', source: 'سربرگ پروتوتایپ', note: 'پاداش تکمیل درس و پاسخ صحیح؛ خرج برای راهنمایی' },
  { key: 'keys', fa: 'کلید / Keys', source: 'سربرگ پروتوتایپ', note: 'باز کردن راهنمایی؛ موجودی محدود' },
  { key: 'streak', fa: 'پیوستگی / Streak', source: 'رویداد هدف روزانه', note: 'با انجام هدف روزانه افزایش مییابد' },
  { key: 'xp', fa: 'امتیاز تجربه / XP', source: 'رویدادهای پاسخ و جلسه', note: 'سقف روزانه دارد؛ منفی نمیشود' },
  { key: 'weeklyXp', fa: 'امتیاز هفته / Weekly XP', source: 'جدول امتیازها', note: 'مجموع هفتگی برای رتبهبندی محلی' },
  { key: 'trophies', fa: 'نشانها / Badges', source: 'تحلیل آزمون و خطاها', note: 'فهرست نشانهای کسبشده' },
]);

export const ECONOMY_RULES = Object.freeze([
  { id: 'answer-correct', fa: 'پاسخ صحیح آزمون', phase: 'exam', formula: 'دشواری × ضریب درس × ۴ (×۱٫۲ در تلاش اول)', verified: false },
  { id: 'answer-wrong', fa: 'پاسخ نادرست آزمون', phase: 'exam', formula: 'کسر یکسوم پاداش همان سؤال', verified: false },
  { id: 'timed-completion', fa: 'اتمام آزمون زماندار', phase: 'exam', formula: 'پاداش تکمیل + پاداش سرعت هوشمند', verified: false },
  { id: 'first-try-no-hint', fa: 'تلاش اول بدون راهنمایی', phase: 'exam', formula: 'ضریب ۱٫۲ روی XP', verified: false },
  { id: 'mistake-resolved', fa: 'رفع خطا', phase: 'exam', formula: 'دو پاسخ صحیح پیاپی → XP + آزادسازی FSRS', verified: false },
  { id: 'lesson-complete', fa: 'تکمیل درس', phase: 'learn', formula: 'XP و سکهٔ ثابت + باز شدن گام بعد', verified: false },
  { id: 'chapter-complete', fa: 'تکمیل فصل', phase: 'learn', formula: 'پاداش بزرگتر + نشان', verified: false },
  { id: 'daily-goal', fa: 'هدف روزانه', phase: 'learn', formula: 'Streak +۱ و XP ثابت', verified: false },
  { id: 'plan-activated', fa: 'فعالسازی قالب برنامه', phase: 'plan', formula: 'XP ثابت + تقویم پیوستگی', verified: false },
  { id: 'plan-day', fa: 'اجرای یک روز برنامه', phase: 'plan', formula: 'XP + گزارش روزانهٔ محلی', verified: false },
  { id: 'lh-reasoning', fa: 'جلسهٔ استدلال (thinking/graph)', phase: 'ai', formula: 'XP فقط برای استدلال ثبتشده، نه گفتگوی عادی', verified: false },
  { id: 'exam-analysis', fa: 'تحلیل آزمون ثبتشده', phase: 'exam', formula: 'نشان «تحلیلگر»', verified: false },
]);

export function createEconomy(store) {
  const dayKey = () => {
    const d = new Date();
    return `${d.getFullYear()}-${d.getMonth() + 1}-${d.getDate()}`;
  };
  function ensure() {
    const e = store.get('economy') || {};
    if (e.dayKey !== dayKey()) {
      store.set('economy.dayKey', dayKey());
      store.set('economy.dailyXp', 0);
    }
    if (!Array.isArray(store.get('economy.ledger'))) store.set('economy.ledger', []);
    if (!Array.isArray(store.get('economy.badges'))) store.set('economy.badges', []);
  }
  function read() {
    ensure();
    const e = store.get('economy') || {};
    return {
      coins: Number(e.coins) || 0, keys: Number(e.keys) || 0,
      streak: Number(e.streak) || 0, xp: Number(e.xp) || 0,
      weeklyXp: Number(e.weeklyXp) || 0, dailyXp: Number(e.dailyXp) || 0,
      trophies: Array.isArray(e.trophies) ? e.trophies : [],
      badges: Array.isArray(e.badges) ? e.badges : [],
      ledger: Array.isArray(e.ledger) ? e.ledger : [],
      dayKey: e.dayKey || dayKey(),
    };
  }
  function write(delta, ruleId, reason) {
    const s = read();
    let xp = Math.round(delta.xp || 0);
    if (xp > 0) xp = Math.max(0, Math.min(xp, DAILY_XP_CAP - s.dailyXp));
    const next = {
      coins: Math.max(0, s.coins + (delta.coins || 0)),
      keys: Math.max(0, s.keys + (delta.keys || 0)),
      streak: Math.max(0, s.streak + (delta.streak || 0)),
      xp: Math.max(0, s.xp + xp),
      weeklyXp: Math.max(0, s.weeklyXp + xp),
      dailyXp: s.dailyXp + Math.max(0, xp),
    };
    for (const [k, v] of Object.entries(next)) store.set(`economy.${k}`, v);
    if (delta.badge) store.set('economy.badges', [...new Set([...s.badges, delta.badge])]);
    const entry = {
      id: `t-${Date.now()}-${Math.random().toString(36).slice(2, 7)}`,
      at: stamp(), ruleId, reason: reason || ruleId,
      xp, coins: delta.coins || 0, keys: delta.keys || 0, streak: delta.streak || 0,
      badge: delta.badge || null, balance: { coins: next.coins, keys: next.keys, xp: next.xp },
      capped: (delta.xp > 0 && xp < delta.xp),
    };
    store.set('economy.ledger', [...s.ledger, entry].slice(-250));
    return entry;
  }
  function apply(ruleId, ctx = {}) {
    const difficulty = Math.max(1, Math.min(5, Number(ctx.difficulty) || 2));
    const factor = Number(ctx.subjectFactor) || 1;
    const base = Math.round(difficulty * factor * 4 * (ctx.firstTry ? 1.2 : 1));
    switch (ruleId) {
      case 'answer-correct': return write({ xp: base, coins: 1 }, ruleId, ctx.reason);
      case 'answer-wrong': return write({ xp: -Math.round(base / 3) }, ruleId, ctx.reason);
      case 'timed-completion': return write({ xp: 20 + Math.min(20, Number(ctx.speedBonus) || 0), coins: 2 }, ruleId);
      case 'first-try-no-hint': return write({ xp: Math.round(base * 0.2) }, ruleId);
      case 'mistake-resolved': return write({ xp: 12 }, ruleId);
      case 'lesson-complete': return write({ xp: 15, coins: 3 }, ruleId, ctx.reason);
      case 'chapter-complete': return write({ xp: 40, coins: 8 }, ruleId, ctx.reason);
      case 'daily-goal': return write({ xp: 25, streak: 1 }, ruleId);
      case 'plan-activated': return write({ xp: 10 }, ruleId);
      case 'plan-day': return write({ xp: 18 }, ruleId);
      case 'lh-reasoning': return write({ xp: 8 }, ruleId);
      case 'exam-analysis': return write({ xp: 0, badge: 'تحلیلگر' }, ruleId);
      default: return null;
    }
  }
  function spend(kind, amount = 1, reason = 'راهنمایی') {
    if (!['coins', 'keys'].includes(kind)) return false;
    const s = read();
    if (s[kind] < amount) return false;
    store.set(`economy.${kind}`, s[kind] - amount);
    const entry = { id: `s-${Date.now()}`, at: stamp(), ruleId: `spend-${kind}`, reason,
      xp: 0, coins: kind === 'coins' ? -amount : 0, keys: kind === 'keys' ? -amount : 0, streak: 0,
      badge: null, balance: { coins: kind === 'coins' ? s.coins - amount : s.coins,
        keys: kind === 'keys' ? s.keys - amount : s.keys, xp: s.xp }, capped: false };
    store.set('economy.ledger', [...s.ledger, entry].slice(-250));
    return true;
  }
  function structure() {
    const s = read();
    return TOKEN_KINDS.map((k) => ({ ...k, value: k.key === 'trophies' ? s.badges.length : s[k.key],
      valueFa: k.key === 'trophies' ? faNum(s.badges.length) : faNum(s[k.key]) }));
  }
  return { apply, spend, read, structure, snapshot: read, rules: ECONOMY_RULES, cap: DAILY_XP_CAP };
}
