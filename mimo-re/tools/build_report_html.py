#!/usr/bin/env python3
"""Stage 3 — render MIMO-REPORT.md into a self-contained RTL HTML report.

    .venv/bin/pip install markdown
    .venv/bin/python tools/build_report_html.py MIMO-REPORT.md report.html
"""
import datetime
import sys

import markdown

TEMPLATE = """<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
  :root {{
    --bg:#0f1115; --panel:#151922; --ink:#e8ecf3; --muted:#9aa4b2;
    --line:#242b38; --accent:#6ea8fe; --accent2:#7ee0c1; --code:#0b0e13;
  }}
  * {{ box-sizing:border-box; }}
  body {{
    margin:0; background:var(--bg); color:var(--ink);
    font-family:"Vazirmatn","Segoe UI",Tahoma,"Noto Naskh Arabic",system-ui,sans-serif;
    line-height:1.9; font-size:16px;
  }}
  .wrap {{ max-width:1080px; margin:0 auto; padding:32px 22px 96px; }}
  header.hero {{
    background:linear-gradient(135deg,#131a26 0%,#0f1115 60%); border:1px solid var(--line);
    border-radius:18px; padding:26px 26px 18px; margin-bottom:28px;
  }}
  header.hero h1 {{ margin:.1em 0 .3em; font-size:1.75rem; line-height:1.5; }}
  header.hero p {{ color:var(--muted); margin:.2em 0; font-size:.95rem; }}
  .badges {{ display:flex; flex-wrap:wrap; gap:8px; margin-top:14px; }}
  .badge {{
    background:var(--panel); border:1px solid var(--line); color:var(--muted);
    border-radius:999px; padding:4px 12px; font-size:.8rem;
  }}
  .badge b {{ color:var(--accent2); font-weight:600; }}
  main h1, main h2, main h3, main h4 {{ line-height:1.6; margin:1.6em 0 .6em; }}
  main h1 {{ font-size:1.45rem; }}
  main h2 {{
    font-size:1.3rem; border-bottom:1px solid var(--line); padding-bottom:.35em;
    color:#fff;
  }}
  main h3 {{ font-size:1.1rem; color:var(--accent); }}
  main h4 {{ font-size:1rem; color:var(--accent2); }}
  p, li {{ color:#dbe2ec; }}
  a {{ color:var(--accent); }}
  strong {{ color:#fff; }}
  blockquote {{
    margin:1.2em 0; padding:12px 16px; background:var(--panel);
    border-right:3px solid var(--accent); border-radius:10px; color:var(--muted);
  }}
  code {{
    background:var(--code); border:1px solid var(--line); border-radius:6px;
    padding:1px 6px; font-family:"JetBrains Mono",Consolas,monospace; font-size:.86em;
    direction:ltr; display:inline-block;
  }}
  pre {{
    background:var(--code); border:1px solid var(--line); border-radius:12px;
    padding:16px; overflow:auto; direction:ltr; text-align:left;
  }}
  pre code {{ border:0; background:none; padding:0; font-size:.84em; line-height:1.65; }}
  table {{
    border-collapse:collapse; width:100%; margin:1.2em 0; font-size:.9rem;
    display:block; overflow-x:auto;
  }}
  th, td {{ border:1px solid var(--line); padding:8px 10px; text-align:right; vertical-align:top; }}
  th {{ background:#1a2130; color:#fff; font-weight:600; white-space:nowrap; }}
  tr:nth-child(even) td {{ background:#12161e; }}
  hr {{ border:0; border-top:1px solid var(--line); margin:2.4em 0; }}
  .toc {{
    background:var(--panel); border:1px solid var(--line); border-radius:14px;
    padding:14px 20px; margin-bottom:26px;
  }}
  .toc-title {{ color:var(--accent2); font-weight:700; margin-bottom:6px; }}
  .toc ul {{ list-style:none; padding:0; margin:0; columns:2; column-gap:26px; }}
  .toc li {{ margin:.15em 0; font-size:.9rem; }}
  .toc a {{ text-decoration:none; color:#cfd8e3; }}
  .toc a:hover {{ color:var(--accent); }}
  footer {{ color:var(--muted); font-size:.82rem; border-top:1px solid var(--line);
            margin-top:48px; padding-top:16px; }}
  @media (max-width:700px) {{ .toc ul {{ columns:1; }} body {{ font-size:15px; }} }}
</style>
</head>
<body>
<div class="wrap">
  <header class="hero">
    <h1>{title}</h1>
    <p>{subtitle}</p>
    <div class="badges">
      <span class="badge">بسته: <b>com.getmimo 9.35</b></span>
      <span class="badge">حجم: <b>142.4 MB</b></span>
      <span class="badge">کلاس: <b>29,454</b></span>
      <span class="badge">مسیر: <b>19</b></span>
      <span class="badge">درس: <b>18,272</b></span>
      <span class="badge">چارچوب: <b>REA</b></span>
    </div>
  </header>
  <div class="toc">
    <div class="toc-title">فهرست</div>
    {toc}
  </div>
  <main>
{body}
  </main>
  <footer>
    تولیدشده در {date} — تحلیل ایستا با androguard + پارسر DEX اختصاصی، در چارچوب متدولوژی
    <a href="https://github.com/morluto/rea">morluto/rea</a>. شواهد خام در پوشهٔ <code>data/</code>.
  </footer>
</div>
</body>
</html>
"""


def main(src: str, dst: str):
    text = open(src, encoding="utf-8").read()
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists", "attr_list"])
    body = md.convert(text)
    toc_html = md.toc
    # first H1 + rest
    title = "مهندسی معکوس Mimo 9.35 — معماری مدیریت آموزشی و پداگوژیک"
    subtitle = ("گزارش تحلیلی: معماری کد، معماری معنایی محتوا، سازوکار آزمون و ارزیابی، "
                "مدیریت پیکربندی/آزمایش و ابزارهای QA")
    html = TEMPLATE.format(title=title, subtitle=subtitle, toc=toc_html, body=body,
                           date=datetime.date.today().isoformat())
    open(dst, "w", encoding="utf-8").write(html)
    print(f"wrote {dst} ({len(html):,} bytes)")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
