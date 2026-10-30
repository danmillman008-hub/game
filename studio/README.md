# studio — the instrument I use to make films

One screenplay in, one cut film out, using only Mivi for generation and ffmpeg for
editing. Everything here is mine to run; nothing needs the Mivi app, a browser, or a
human in the loop except the approvals the playbook asks for.

```
studio/
├── PLAYBOOK.md          how I work: MIVI-STD-1, step by step, with the QC gate
├── TECHNIQUES.md        the craft — 15 techniques, each mapped to a real tool
├── filmkit.py           the CLI: one verb per capability, resumable per project
├── selftest.py          offline proof of the editing half (runs in CI)
└── openmontage/
    └── mivi_video.py    drop-in OpenMontage provider so its 12 pipelines can use Mivi

films/<name>/            a project: project.json is the source of truth
├── project.json
├── stills/  clips/  assets/  audio/  subs/  out/  qc/
```

## The verbs

```bash
filmkit new myfilm
filmkit plan myfilm --script script.txt      # SHOT: … / VO: … lines
filmkit status myfilm

filmkit still myfilm --shot 1 --from url:https://…
filmkit still myfilm --shot 2 --from compose:assets/plate.png,assets/actor.png --prompt "…"
filmkit still myfilm --shot 3 --from last:2            # chain shot 2

filmkit shot myfilm --shot 1 --takes 2 --quality 1
filmkit chain myfilm --from 1 --to 2
filmkit assemble myfilm [--crossfade 0.4]
filmkit mix myfilm --vo audio/vo.mp3 --music audio/bed.mp3 --duck
filmkit qc myfilm
filmkit frames out/final.mp4 --at 1,4,7
filmkit deliver myfilm --github --tag v1     # or --drive
```

`--from` accepts: `file:`, `url:`, `last:N`, `compose:a,b`, `upscale:`, `swapface:`, `masks:`.

## Verified

| What | Result |
|---|---|
| `studio/selftest.py` (offline) | 2 synthetic clips → assemble → mix → qc: 960×1280, 7.7 s, audio present, 0 issues |
| `films/watchmaker` (live) | 3 chained shots → 11.31 s film, 960×1280 32 fps, subtitles burned, audio mixed |
| `studio/demo.py` (live, CI run 40932388284) | new → still url: → shot 360P → chain → shot → assemble → qc → deliver, **DEMO OK**, 7.75 s, frame_delta ≤24.9 |
| reference frames | `films/watchmaker/qc/frames/`, `films/studio_demo/qc/frames/` |

Draft note (measured): 360P is **448×576**, not 432×576, and visibly softer than 720P —
useful for checking motion and continuity, useless for judging look.

## Relations to the rest of the repo

- `bridge/mivi_mcp.py` — the MCP server (12 tools). `filmkit` imports its API layer, so
  there is exactly one place that knows how to sign a Mivi request.
- `bridge/mivi_bridge.py` — OpenAI-compatible `/v1/videos`, for third-party studios.
- `bridge/FILM_DIRECTOR_SKILL.md` — the shorter shot-grammar card.
- `bridge/README.md` — repo research: which studio shell to sit this under.

## Honest limits (repeated on purpose)

4.03 s per shot · 960×1280 · no seed · no end frame · no audio · no text-to-video ·
no working lip sync on Mivi · continuity good for ~2 chained hops.

## chainkit.py — گردش کار «پل فریم»

از صفر ویدیو نساز: still → تولید لینک ۴ثانیه‌ای → آخرین فریم → راهنما (edge/gray/annot) →
لینک بعدی. تولید گران است، ffmpeg تقریباً رایگان (۲.۹ ثانیه برای چسباندن ۳۷ کلیپ با
`-c copy` در برابر ۸۵ ثانیه انکود).

```bash
python3 studio/chainkit.py bridge out/film --still still.png --prompt "..." --duration 4
python3 studio/chainkit.py chain  out/film links/L001/out.mp4 --prompt "..."
python3 studio/chainkit.py audit  out/film --anchor still.png
python3 studio/chainkit.py concat out/cut.mp4 links/L00*/out.mp4
python3 studio/chainkit.py grab   clip.mp4 --mode last
python3 studio/chainkit.py guide  frame.png --spec guide.json
```

جزئیات و دام‌ها: [`CHAIN_WORKFLOW.md`](CHAIN_WORKFLOW.md)

## scorer.py — داور عینی بهترین‌از‌چند

تولید رایگان است، داوری گران. این ابزار روی CPU، بدون GPU و بدون ابر، کاندیدها را می‌سنجد:
هویت (SSIM فریم اول و ناحیهٔ چهره)، شارپنس، فریز، فلیکر، انحراف رنگ، و پروکسی لب‌سینک
(همبستگی حرکت دهان با پوش صدا).

```bash
python3 studio/scorer.py score clip.mp4 --ref still.png --audio vo.mp3
python3 studio/scorer.py pick  cands/*.mp4 --ref still.png --audio vo.mp3
```

گردش کار کامل: [`QUALITY_WORKFLOW.md`](QUALITY_WORKFLOW.md)

## حافظهٔ پروژه

[`REPORT.md`](REPORT.md) — چه ساخته شد، چه شکست خورد، چه سنجیده شد، و مشکل دسترسی به Mivi چطور با GitHub Actions حل شد.

## نگارش پرامپت حرکت

[`PROMPTS_MOTION.md`](PROMPTS_MOTION.md) — قواعد حرکت طبیعی (یک حرکت، مقدار دقیق، احساس→بدن) + بازنویسی پرامپت‌های خودمان + فهرست ریپوهای مرجع.

## شکاف‌ها و نقشهٔ راه

[`GAPS.md`](GAPS.md) — ماتریس «داریم/نداریم»، ۱۱ شکاف با عدد و منبع، و اولویت‌بندی P0..P3.
