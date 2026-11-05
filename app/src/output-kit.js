/**
 * «خروجی گرفتن آسان» — one click from inside the app.
 *
 * Produces the SAME self-contained HTML that is shipped in app/dist/Mimo.html,
 * a ready-to-host PWA ZIP, the local state, the learning-path CSV and a
 * print-ready report. Everything is built with local Blob/ArrayBuffer APIs;
 * there is no upload, no server and no network request.
 */
import { saveText, saveBytes, makeZip, b64ToBytes, b64ToText, toBytes, stamp, esc } from './util.js';
import { PWA_ASSETS } from './pwa-assets.js';

export const SOURCE_SLOT = '__MIMO' + '_SOURCE_B64_SLOT__';

export function createOutputKit({ doc, store, economy, learningPath, aiStudio, toast }) {
  let deferredInstall = null;
  try {
    window.addEventListener('beforeinstallprompt', (e) => { e.preventDefault(); deferredInstall = e; });
    window.addEventListener('appinstalled', () => { toast('اپلیکیشن روی دستگاه نصب شد'); });
  } catch (_) {}

  const sourceB64 = () => (doc.getElementById('mimoSource')?.textContent || '').trim();
  const hasSource = () => Boolean(sourceB64());

  function standaloneHtml() {
    const b64 = sourceB64();
    if (!b64) return '';
    try {
      const template = b64ToText(b64);
      // template still contains SOURCE_SLOT; re-injecting the same payload makes
      // the exported file able to export itself again.
      return template.replace(SOURCE_SLOT, b64);
    } catch (_) { return ''; }
  }

  function pwaIndex() {
    const html = standaloneHtml();
    if (!html) return '';
    return html
      .replace('<title>', '<link rel="manifest" href="./manifest.webmanifest">\n<link rel="apple-touch-icon" href="./icons/icon-192.png">\n<title>')
      .replace('</body>', '<' + 'script>\n'
        + "if ('serviceWorker' in navigator && location.protocol.indexOf('http') === 0) {\n"
        + "  window.addEventListener('load', function () {\n"
        + "    navigator.serviceWorker.register('./sw.js', {scope:'./'}).catch(function(){});\n"
        + "  });\n}\n"
        + '<' + '/script>\n</body>');
  }

  function startHere() {
    return [
      'میمو · خروجی آفلاین',
      '====================',
      '',
      '۱) Mimo.html را دوبار کلیک کنید (یا در مرورگر گوشی باز کنید).',
      '   نیازی به اینترنت، سرور، نصب وابستگی یا خط فرمان ندارد.',
      '۲) برای نصب روی گوشی: پوشهٔ Mimo-PWA را روی یک آدرس HTTPS قرار دهید',
      '   و از منوی مرورگر «افزودن به صفحهٔ اصلی / Install app» را بزنید.',
      '   در پیشنمایش زنده نیز همان فایل index.html بهصورت PWA قابلنصب است.',
      '۳) همهٔ دادهها فقط روی همین دستگاه ذخیره میشوند؛ هیچ چیز ارسال نمیشود.',
      '۴) محتوای درسها فعلاً از دادهٔ آزمایشی پروتوتایپ تأییدشده است.',
      '   منابع نهایی را از بخش «استودیو یادگیری محلی → وارد کردن بستهٔ محتوا»',
      '   یا با ابزار app/tools/validate_content.py وارد کنید.',
      '',
      `تولید: ${stamp()} · بدون LLM · بدون شبکه · SERVER CONFIRMED=0`,
      '',
    ].join('\n');
  }

  function stateJson() { return JSON.stringify(store.export(), null, 2); }

  function pathCsv() {
    const rows = [['برنامه', 'درس', 'فصل', 'عنوان درس', 'وضعیت', 'منبع']];
    for (const c of learningPath.curriculum.courses) {
      for (const ch of c.chapters) for (const ls of ch.lessons) {
        rows.push([learningPath.state().programKey, c.name, ch.name, ls.title,
          learningPath.statusOf(ls.id), 'prototype:v12.5-fa:KONKUR']);
      }
    }
    return '\uFEFF' + rows.map((r) => r.map((v) => `"${String(v).replace(/"/g, '""')}"`).join(',')).join('\r\n');
  }

  function reportHtml() {
    const p = learningPath.progress(), e = economy.snapshot(), t = aiStudio.tokenStructure();
    return `<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8">
<title>گزارش میمو</title><style>body{font-family:Tahoma,sans-serif;padding:32px;line-height:2}h1{font-size:22px}
table{border-collapse:collapse;width:100%}td,th{border:1px solid #ccc;padding:8px;text-align:right}</style></head><body>
<h1>گزارش وضعیت میمو (محلی، آفلاین)</h1><p>${esc(stamp())}</p>
<h2>مسیر آموزشی</h2><p>تکمیلشده: ${esc(p.doneFa)} از ${esc(p.totalFa)} درس (${esc(p.percentFa)}٪). کل سرفصلها: ${esc(learningPath.curriculum.totalLessons)} درس.</p>
<h2>توکنهای پاداش</h2><table><tr><th>نوع</th><th>مقدار</th></tr>
${economy.structure().map((k) => `<tr><td>${esc(k.fa)}</td><td>${esc(k.valueFa)}</td></tr>`).join('')}</table>
<p>سقف XP روزانه: ${esc(e.dailyXp)} / ${esc(economy.cap)}. دفتر توکنها: ${esc(e.ledger.length)} رویداد.</p>
<h2>توکنهای هوش مصنوعی (صادقانه)</h2><table><tr><th>بخش</th><th>مقدار</th></tr>
${t.map((k) => `<tr><td>${esc(k.fa)}</td><td>${esc(k.value)}</td></tr>`).join('')}</table>
<p>بدون مدل زبانی، بدون اینترنت، بدون تولید متن. استنتاج سرور: تأییدنشده (SERVER CONFIRMED=0).</p>
</body></html>`;
  }

  function downloadHtml() {
    const html = standaloneHtml();
    if (!html) { toast('در این نسخهٔ چندفایله، فایل dist/Mimo.html را دانلود کنید'); return false; }
    const ok = saveText('Mimo.html', html, 'text/html;charset=utf-8');
    toast(ok ? 'فایل تکهای Mimo.html دانلود شد' : 'دانلود در این محیط پشتیبانی نمیشود');
    return ok;
  }

  function downloadZip() {
    const html = standaloneHtml();
    const entries = [
      { name: 'Mimo.html', data: toBytes(html || 'open app/dist/Mimo.html') },
      { name: 'START_HERE.txt', data: toBytes(startHere()) },
      { name: 'mimo-state.json', data: toBytes(stateJson()) },
      { name: 'Mimo-PWA/index.html', data: toBytes(pwaIndex() || html || '') },
      { name: 'Mimo-PWA/manifest.webmanifest', data: toBytes(b64ToText(PWA_ASSETS.manifestB64 || '') || '{}') },
      { name: 'Mimo-PWA/sw.js', data: toBytes(b64ToText(PWA_ASSETS.swB64 || '')) },
      { name: 'Mimo-PWA/گزارش-میمو.html', data: toBytes(reportHtml()) },
    ];
    for (const [name, b64] of Object.entries(PWA_ASSETS.icons || {})) {
      entries.push({ name: `Mimo-PWA/icons/${name}`, data: b64ToBytes(b64) });
    }
    const ok = saveBytes('Mimo.zip', makeZip(entries), 'application/zip');
    toast(ok ? 'بستهٔ کامل Mimo.zip دانلود شد' : 'دانلود در این محیط پشتیبانی نمیشود');
    return ok;
  }

  function printReport() {
    let box = doc.getElementById('plusPrint');
    if (!box) { box = doc.createElement('div'); box.id = 'plusPrint'; doc.body.appendChild(box); }
    box.innerHTML = reportHtml().replace(/^[\s\S]*?<body>/, '').replace(/<\/body>[\s\S]*$/, '');
    const ok = saveText('گزارش-میمو.html', reportHtml(), 'text/html;charset=utf-8');
    try {
      if (typeof window.print === 'function' && !/jsdom/i.test(navigator.userAgent)) window.print();
    } catch (_) {}
    toast(ok ? 'گزارش قابلچاپ ساخته شد (HTML)' : 'گزارش در این محیط پشتیبانی نمیشود');
    return ok;
  }

  function install() {
    if (deferredInstall && typeof deferredInstall.prompt === 'function') {
      try { deferredInstall.prompt(); toast('درخواست نصب ارسال شد'); return true; } catch (_) {}
    }
    toast('منوی مرورگر گوشی ← «افزودن به صفحهٔ اصلی / نصب اپلیکیشن»');
    return false;
  }

  function copyLink() {
    try {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(location.href).then(() => toast('نشانی پیشنمایش کپی شد'),
          () => toast('کپی ممکن نشد'));
        return true;
      }
    } catch (_) {}
    toast('کپی در این محیط پشتیبانی نمیشود'); return false;
  }

  return { hasSource, standaloneHtml, pwaIndex, downloadHtml, downloadZip, printReport,
    install, copyLink, reportHtml, pathCsv, stateJson,
    downloadState: () => { const ok = saveText('mimo-state.json', stateJson(), 'application/json');
      toast(ok ? 'وضعیت محلی دانلود شد' : 'دانلود ممکن نشد'); return ok; },
    downloadCsv: () => { const ok = saveText('مسیر-آموزشی.csv', pathCsv(), 'text/csv;charset=utf-8');
      toast(ok ? 'مسیر آموزشی دانلود شد' : 'دانلود ممکن نشد'); return ok; },
    downloadSession: () => aiStudio.exportSession() };
}
