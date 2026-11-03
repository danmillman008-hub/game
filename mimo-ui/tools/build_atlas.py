#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_atlas.py — wrap ATLAS/data.json into a self-contained offline HTML atlas."""
import gzip
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]
p_json, p_gz = OUT / "ATLAS/data.json", OUT / "ATLAS/data.json.gz"
if p_json.is_file():
    data = p_json.read_text(encoding="utf-8")
elif p_gz.is_file():
    data = gzip.open(p_gz, "rt", encoding="utf-8").read()
else:
    raise SystemExit("ATLAS/data.json(.gz) missing — run build_dossiers.py first")
tpl = r'''<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>اطلس کامل رابط کاربری Mimo 9.35 | استخراج صفر تا صد</title>
<style>
:root{--bg:#0f1220;--panel:#191d31;--panel2:#222741;--line:#333a58;--txt:#e8ebf6;--muted:#98a0c0;--acc:#7e4bde;--acc2:#66bc5a;--warn:#f05a6e;--mono:'SFMono-Regular',Consolas,'Liberation Mono',monospace}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--txt);font:14px/1.7 system-ui,-apple-system,"Segoe UI",Tahoma,sans-serif}
header{padding:22px 26px;border-bottom:1px solid var(--line);background:linear-gradient(120deg,#191d31,#252746)}
h1{margin:0 0 6px;font-size:22px}
header p{margin:0;color:var(--muted);font-size:13px}
.badges{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.badge{background:var(--panel2);border:1px solid var(--line);border-radius:8px;padding:5px 10px;font-size:12px}
.badge b{color:#fff;font-size:14px;margin-left:4px}
nav{display:flex;flex-wrap:wrap;gap:4px;padding:10px 20px;border-bottom:1px solid var(--line);background:var(--panel)}
nav button{background:transparent;color:var(--muted);border:1px solid transparent;border-radius:8px;padding:7px 13px;cursor:pointer;font:inherit}
nav button:hover{color:#fff;background:var(--panel2)}
nav button.active{background:var(--acc);color:#fff;border-color:var(--acc)}
main{padding:18px 22px}
section{display:none}
section.active{display:block}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px;margin-bottom:18px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px}
.card .n{font-size:24px;font-weight:700;color:#fff}
.card .l{color:var(--muted);font-size:12px}
.split{display:grid;grid-template-columns:330px 1fr;gap:14px;min-height:70vh}
@media(max-width:900px){.split{grid-template-columns:1fr}}
.listbox,.detail{background:var(--panel);border:1px solid var(--line);border-radius:10px;overflow:hidden}
.listbox{display:flex;flex-direction:column;max-height:76vh}
input[type=search]{width:100%;padding:10px 12px;background:var(--panel2);border:0;border-bottom:1px solid var(--line);color:var(--txt);font:inherit;outline:none}
.items{overflow:auto;flex:1}
.item{display:block;width:100%;text-align:right;background:transparent;border:0;border-bottom:1px solid #242a44;color:var(--txt);padding:8px 12px;cursor:pointer;font:inherit;font-size:12px}
.item:hover{background:var(--panel2)}
.item.sel{background:#2d2650;border-right:3px solid var(--acc)}
.item small{color:var(--muted);display:block;font-family:var(--mono);direction:ltr;text-align:left}
.detail{padding:14px;overflow:auto;max-height:76vh}
.detail h2{margin:0 0 10px;font-size:17px}
.detail h3{margin:16px 0 6px;font-size:14px;color:var(--acc2)}
pre{background:#0c0f1c;border:1px solid var(--line);border-radius:8px;padding:12px;overflow:auto;max-height:52vh;font:12px/1.55 var(--mono);direction:ltr;text-align:left;white-space:pre}
code{font-family:var(--mono);direction:ltr}
table{width:100%;border-collapse:collapse;font-size:12px}
th,td{border-bottom:1px solid var(--line);padding:7px 9px;text-align:right}
th{color:var(--muted);position:sticky;top:0;background:var(--panel)}
.mono{font-family:var(--mono);direction:ltr;display:inline-block;text-align:left}
.sw{display:inline-block;width:18px;height:18px;border-radius:4px;border:1px solid #666;vertical-align:middle;margin-left:6px}
.pill{display:inline-block;padding:2px 7px;border-radius:20px;background:var(--panel2);border:1px solid var(--line);font-size:11px;margin:2px}
.ok{color:var(--acc2)}.bad{color:var(--warn)}
a{color:#a98cff}
.tag{color:#8fd3ff}.att{color:#ffd479}.val{color:#a4e59b}.cm{color:#7f88a8}
.note{background:var(--panel2);border:1px solid var(--line);border-radius:8px;padding:12px;margin-bottom:14px;font-size:13px;color:var(--muted)}
</style>
</head>
<body>
<header>
  <h1>اطلس کامل رابط کاربری Mimo 9.35</h1>
  <p>استخراج ایستای صفرتاصد از <code>com.getmimo</code> — هر فایل XML، هر توکن، هر رشته، هر کلاس UI، و تک‌تک ۱۴٬۳۹۸ عضو APK. بدون نمونه، بدون حذف.</p>
  <div class="badges" id="badges"></div>
</header>
<nav id="nav"></nav>
<main>
  <section id="s-over" class="active"><div class="cards" id="cards"></div>
    <div class="note">این اطلس یک فایل خودبسنده است: همهٔ داده‌ها در همین صفحه جاسازی شده و بدون اینترنت/سرور کار می‌کند. منبع حقیقت همیشه پوشهٔ <code>SOURCE/</code> است (دیکد مستقیم بایت‌های APK)؛ این صفحه فقط نمایشگر است. برچسب شواهد: <span class="ok">VERIFIED_STATIC</span> = مشاهدهٔ مستقیم از بسته، <span>DERIVED</span> = استخراج ماشینی از همان بایت‌ها، <span>INFERRED</span> = تفسیر، <span class="bad">UNKNOWN</span> = نیازمند اجرا/دیکامپایل.</div>
    <h3>جدول پوشش ناحیه‌ای</h3><table id="covtable"></table>
  </section>
  <section id="s-layouts"><div class="note">۱٬۲۹۹ فایل لایهٔ باینری AXML → XML نمادین کامل. شناسه‌های عددی به نام منبع حل شده و مقادیر رایج (<code>-1→match_parent</code>) رمزگشایی شده‌اند؛ نسخهٔ خام در <code>SOURCE/_raw_axml/</code> محفوظ است.</div>
    <div class="split"><div class="listbox"><input type="search" id="q-layout" placeholder="جستجوی لایه، تگ، شناسه…"><div class="items" id="l-layout"></div></div>
    <div class="detail" id="d-layout">یک لایه را انتخاب کنید.</div></div></section>
  <section id="s-screens"><div class="note">فهرست کامل سطوح رابط: ۱۹۲ سطح از مهندسی معکوس قبلی شما + همهٔ کلاس‌های صفحه‌ای کشف‌شده در DEX. هر کدام پروندهٔ جداگانه در <code>SCREENS/</code> دارد.</div>
    <div class="split"><div class="listbox"><input type="search" id="q-screen" placeholder="جستجوی صفحه…"><div class="items" id="l-screen"></div></div>
    <div class="detail" id="d-screen">یک صفحه را انتخاب کنید.</div></div></section>
  <section id="s-tokens"><div class="note">همهٔ ۱٬۱۹۸ نام رنگ و ۱٬۴۰۱ نام دایمنشن از <code>resources.arsc</code>، با تمام ۱۶۱ پیکربندی. جفت روشن/تیره کنار هم.</div>
    <div class="split"><div class="listbox"><input type="search" id="q-token" placeholder="جستجوی توکن…"><div class="items" id="l-token"></div></div>
    <div class="detail" id="d-token">یک توکن را انتخاب کنید.</div></div></section>
  <section id="s-strings"><div class="note">همهٔ ۱٬۷۲۱ نام رشته و ۳۷٬۹۶۹ مقدار در ۱۱۷ زبان (شامل فارسی). مقادیر پیش‌فرض و <code>fa</code> نمایش داده می‌شوند؛ بقیه در <code>SOURCE/values/values-*/string.xml</code>.</div>
    <div class="split"><div class="listbox"><input type="search" id="q-string" placeholder="جستجوی رشته…"><div class="items" id="l-string"></div></div>
    <div class="detail" id="d-string">یک رشته را انتخاب کنید.</div></div></section>
  <section id="s-web"><div class="note">کد واقعی رابط درس/ادیتور که داخل WebView اجرا می‌شود: ۱۱ فایل JS، ۲ CSS، ۱۳ HTML، ۲۱۵ SVG، فونت و باندل ادیتور. متن کامل در اینجا و بایت‌های اصلی در <code>SOURCE/assets/ui/</code>.</div>
    <div class="split"><div class="listbox"><input type="search" id="q-web" placeholder="جستجوی دارایی…"><div class="items" id="l-web"></div></div>
    <div class="detail" id="d-web">یک فایل را انتخاب کنید.</div></div></section>
  <section id="s-entries"><div class="note">سرشماری کامل اعضای ZIP بسته: همهٔ ۱۴٬۳۹۸ عضو، با SHA-256، کلاس و محل تحویل. چیزی به «نمونه» تقلیل نیافته است.</div>
    <div class="split"><div class="listbox"><input type="search" id="q-entry" placeholder="جستجوی مسیر/هش…"><div class="items" id="l-entry"></div></div>
    <div class="detail" id="d-entry">یک عضو را انتخاب کنید.</div></div></section>
</main>
<script id="DATA" type="application/json">__DATA__</script>
<script>
const D=JSON.parse(document.getElementById('DATA').textContent);
const $=s=>document.querySelector(s), esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmt=n=>Number(n).toLocaleString('en-US');
const tabs=[['over','نمای کلی'],['layouts','لایه‌ها'],['screens','صفحات'],['tokens','توکن‌ها'],['strings','رشته‌ها'],['web','کد WebView'],['entries','همهٔ فایل‌ها']];
$('#nav').innerHTML=tabs.map((t,i)=>`<button data-t="${t[0]}" class="${i?'':'active'}">${t[1]}</button>`).join('');
$('#nav').onclick=e=>{const b=e.target.closest('button');if(!b)return;document.querySelectorAll('nav button').forEach(x=>x.classList.remove('active'));b.classList.add('active');document.querySelectorAll('main section').forEach(x=>x.classList.remove('active'));$('#s-'+b.dataset.t).classList.add('active')};
const m=D.meta||{}, arsc=m.arsc||{}, tok=m.tokens||{}, dex=m.dex||{}, ec=m.entry_classes||{};
const stats=[['اعضای APK',m.apk?.entries||14398],['لایه‌های XML',Object.keys(D.layouts).length],['صفحات رابط',D.screens.length],['شناسه‌های منبع',arsc.resource_ids],['ردیف‌های پیکربندی',arsc.config_rows],['نام رنگ',tok.color_names],['نام دایمنشن',tok.dimen_names],['مقدار رشته',tok.string_values],['نام استایل',tok.style_names],['کلاس‌های UI',dex.app_classes],['کلاس‌های Compose',dex.compose_classes],['دارایی WebView',ec.UI_WEBVIEW_ASSET],['فایل‌های محتوا (فهرست‌شده)',ec.CONTENT_DATA]];
$('#badges').innerHTML=stats.map(s=>`<span class="badge">${s[0]} <b>${fmt(s[1])}</b></span>`).join('');
$('#cards').innerHTML=stats.map(s=>`<div class="card"><div class="n">${fmt(s[1])}</div><div class="l">${s[0]}</div></div>`).join('');
$('#covtable').innerHTML='<tr><th>ناحیه</th><th>انتظار</th><th>مشاهده</th><th>وضعیت</th><th>محل تحویل</th></tr>'+D.area_coverage.map(r=>`<tr><td>${esc(r.area)}</td><td>${fmt(r.expected)}</td><td>${fmt(r.observed)}</td><td class="${r.status==='COMPLETE'?'ok':'bad'}">${r.status}</td><td class="mono">${esc(r.deliverable)}</td></tr>`).join('');
function hl(x){return esc(x).replace(/(&lt;\/?)([\w.:-]+)/g,'$1<span class="tag">$2</span>').replace(/([\w:.-]+)=(&quot;.*?&quot;)/g,'<span class="att">$1</span>=<span class="val">$2</span>')}
function makeList(qid,lid,did,keys,render,detail,initial){
  const q=$('#'+qid),L=$('#'+lid),Dd=$('#'+did);let cur=initial;
  function draw(){const t=q.value.trim().toLowerCase();const rows=keys.filter(k=>!t||k.toLowerCase().includes(t)||(k.f&&k.f.toLowerCase().includes(t)));L.innerHTML=rows.slice(0,4000).map((k,i)=>`<button class="item ${k===cur?'sel':''}" data-i="${i}">${render(k)}</button>`).join('')+(rows.length>4000?`<div class="item">… و ${fmt(rows.length-4000)} مورد دیگر (همه در CATALOGS)</div>`:'');L.querySelectorAll('.item[data-i]').forEach(b=>b.onclick=()=>{cur=rows[+b.dataset.i];draw();Dd.innerHTML=detail(cur)})}
  q.oninput=draw;draw();if(initial)Dd.innerHTML=detail(initial);
}
// layouts
const lk=Object.keys(D.layouts).sort();
makeList('q-layout','l-layout','d-layout',lk,k=>`<span class="mono">${esc(k.split('/').slice(-2).join('/'))}</span><small>${esc(k)}</small>`,k=>{
  const o=D.layouts[k],f=o.facts;
  return `<h2 class="mono">${esc(k)}</h2>
  <p><span class="pill">ریشه: ${esc(f.root_tag)}</span><span class="pill">گره: ${f.nodes}</span><span class="pill">id: ${f.ids.length}</span><span class="pill">ارجاع: ${f.references.length}</span><span class="pill">ComposeView: ${f.compose_views.length}</span><span class="pill">WebView: ${f.webviews.length}</span></p>
  <p><a href="../${esc(f.decoded_path)}" target="_blank">فایل XML دیکدشده</a> · <a href="../${esc(f.dossier_path)}" target="_blank">پروندهٔ کامل لایه</a></p>
  <h3>کد XML کامل</h3><pre>${hl(o.xml)}</pre>
  <h3>شناسه‌ها</h3><p class="mono">${esc(f.ids.join('  '))||'—'}</p>
  <h3>ارجاعات</h3><p class="mono">${esc(f.references.join('  '))||'—'}</p>
  <h3>ویوهای سفارشی</h3><p class="mono">${esc(f.custom_views.join('  '))||'—'}</p>`,lk[0]);
// screens
makeList('q-screen','l-screen','d-screen',D.screens.map(s=>s.screen_id),k=>`${esc(k)}<small>${esc((D.screens.find(s=>s.screen_id===k)||{}).class||'')}</small>`,k=>{
  const s=D.screens.find(x=>x.screen_id===k)||{};
  return `<h2>${esc(s.screen_id)}</h2><p class="mono">${esc(s.class)}</p>
  <p><span class="pill">نوع: ${esc(s.kind)}</span><span class="pill">لایه: ${fmt(s.n_layouts)}</span><span class="pill">رشته: ${fmt(s.n_strings)}</span><span class="pill">رنگ: ${fmt(s.n_colors)}</span><span class="pill">دایمن: ${fmt(s.n_dimens)}</span><span class="pill">استایل: ${fmt(s.n_styles)}</span><span class="pill">${s.compose?'ComposeView':''}</span></p>
  <p><a href="../${esc(s.dossier)}" target="_blank">پروندهٔ کامل صفحه</a></p>
  <h3>لایه‌های متصل (همه)</h3><p class="mono">${esc((s.layouts||'').split(';').filter(Boolean).join('\n'))||'—'}</p>`,D.screens[0]?.screen_id);
// tokens
const cn=Object.keys(D.tokens.colors).sort(), dn=Object.keys(D.tokens.dimens).sort();
const tkeys=[...cn.map(n=>'color:'+n),...dn.map(n=>'dimen:'+n)];
makeList('q-token','l-token','d-token',tkeys,k=>`<span class="mono">${esc(k.split(':')[1])}</span><small>${esc(k.split(':')[0])}</small>`,k=>{
  const [t,n]=k.split(':'),v=D.tokens[t==='color'?'colors':'dimens'][n];
  const rows=Object.keys(v).sort().map(q=>`<tr><td>${esc(q)}</td><td class="mono">${esc(v[q])}</td><td>${t==='color'?`<span class="sw" style="background:${esc(v[q])}"></span>`:''}</td></tr>`).join('');
  return `<h2 class="mono">${esc(n)}</h2><p>نوع: ${esc(t)} · تعداد پیکربندی: ${Object.keys(v).length}</p><table><tr><th>qualifier</th><th>مقدار</th><th>نمونه</th></tr>${rows}</table>`,tkeys[0]);
// strings
const sn=Object.keys(D.strings).sort();
makeList('q-string','l-string','d-string',sn,k=>`<span class="mono">${esc(k)}</span><small>${esc(D.strings[k].default||'').slice(0,80)}</small>`,k=>{
  const v=D.strings[k];return `<h2 class="mono">${esc(k)}</h2><table><tr><th>زبان</th><th>متن</th></tr>${Object.keys(v).sort().map(q=>`<tr><td>${esc(q)}</td><td>${esc(v[q])}</td></tr>`).join('')}</table>`,sn[0]);
// web assets
const wk=Object.keys(D.assets).sort();
makeList('q-web','l-web','d-web',wk,k=>`<span class="mono">${esc(k.split('/').slice(-2).join('/'))}</span><small>${esc(k)}</small>`,k=>{
  const a=D.assets[k];return `<h2 class="mono">${esc(k)}</h2><p><span class="pill">${fmt(a.bytes)} بایت</span><span class="pill">${a.kind}</span></p>
  <p><a href="../SOURCE/assets/ui/${esc(k.slice(7))}" target="_blank">فایل اصلی</a></p>
  <pre>${a.kind==='text'?esc(a.text):'(فایل باینری — بایت‌های اصلی در پوشهٔ SOURCE)'}</pre>`,wk[0]);
// all entries
makeList('q-entry','l-entry','d-entry',D.entries.map(e=>e.path),k=>`<span class="mono">${esc(k.split('/').slice(-2).join('/'))}</span><small>${esc(k)}</small>`,k=>{
  const e=D.entries.find(x=>x.path===k)||{};
  return `<h2 class="mono" style="font-size:12px">${esc(k)}</h2><table>
  <tr><th>کلاس</th><td>${esc(e.cls)}</td></tr><tr><th>حجم</th><td>${fmt(e.size)} بایت</td></tr>
  <tr><th>SHA-256</th><td class="mono">${esc(e.sha)}</td></tr><tr><th>محل تحویل</th><td class="mono">${esc(e.dest)}</td></tr></table>`,D.entries[0]?.path);
</script>
</body></html>
'''
html = tpl.replace("__DATA__", data)
(OUT / "ATLAS/index.html").write_text(html, encoding="utf-8")
print("wrote ATLAS/index.html", len(html), "bytes")
