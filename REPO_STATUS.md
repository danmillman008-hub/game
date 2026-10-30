# وضعیت ریپو — ساخته‌شده با اجرا، نه با ادعا

> خودکار از `python3 studio/verify.py` — 2026-10-30 20:50 UTC · پایتون 3.11.17 · runner

| ok | FAIL | skip | warn |
|---|---|---|---|
| 40 | 4 | 1 | 1 |

> ⚠️ 4 وابستگی نصب نیست؛ ردیف‌های وابسته `skip` شده‌اند، نه pass — روی رانر هم اجرا نشدند: basicsr, pyanime4k, realesrgan, torch

> ⏭️ این 1 فایل روی رانر هم اجرا نشد: studio/toolbox/upscale.py

## compile

- ✅ 40/40 compile

## data

- ✅ 62 json files parse
- ✅ 8 workflows parse

## deps

- ✅ every declared dependency matches the file's imports

## inventory

- ✅ 48 entries, every file accounted for

## links

- ❌ 1 broken reference(s) — run studio/links.py
- ⚠️ films/anime_ten/deliver/scene_min1.mp4: 23 MB (over 20 MB, tracked in git)
- ❌ 695 files · 1 breaks · 1 size warning(s)

## smoke

- ✅ bridge/mivi_mcp.py --help (0.1s)
- ✅ mivi_web/make_catalog.py --help (0.0s)
- ✅ mivi_web/re/annpaths.py --help (0.0s)
- ✅ mivi_web/re/dexann.py --help (0.0s)
- ✅ mivi_web/re/dumpclass.py --help (0.5s)
- ✅ mivi_web/re/fields.py --help (0.2s)
- ✅ mivi_web/re/m2.py --help (0.2s)
- ✅ mivi_web/re/staticdump.py --help (0.2s)
- ✅ mivi_web/re/xref2.py --help (0.2s)
- ✅ studio/artgen.py --help (0.1s)
- ✅ studio/chainkit.py --help (0.1s)
- ✅ studio/cutlist.py --help (0.1s)
- ✅ studio/filmkit.py --help (0.1s)
- ✅ studio/knowledge/bank.py --help (0.1s)
- ✅ studio/knowledge/banktest.py -> ALL OK
- ✅ studio/knowledge/measure.py --help (0.1s)
- ❌ studio/links.py rc=1: 695 tracked files · 1 breaks · 1 size warnings
- ✅ studio/lipsync.py --help (0.0s)
- ✅ studio/mivi_photo.py --help (0.1s)
- ✅ studio/mivi_shot.py --help (0.1s)
- ✅ studio/motionbank.py --help (0.0s)
- ✅ studio/motionlint.py --help (0.1s)
- ✅ studio/motions/ten_shots.py --help (0.0s)
- ✅ studio/render_film.py --help (0.1s)
- ✅ studio/scorer.py --help (0.2s)
- ✅ studio/selftest.py -> SELFTEST OK
- ✅ studio/shotplan.py --help (0.0s)
- ✅ studio/tests/test_mivi_shot.py -> PASS — success recorded, chain waited, refusal isolated
- ⏭️ studio/toolbox/upscale.py needs basicsr, pyanime4k, realesrgan, torch — torch + realesrgan + basicsr ~2.5 GB and model weights; not installed on the runner
- ✅ studio/verify.py --help (0.0s)
- ✅ studio/voice.py --help (0.1s)
- ✅ studio/voicetest.py -> ALL OK
- ✅ studio/wanprompt.py --help (0.0s)
- ❌ studio/links.py did not run (ci=true): needs unknown dependency

## triggers

- ✅ .mivi-trigger -> films/short16/gen_jobs_empty.json
- ✅ .photo-trigger -> mode 'probe'
- ✅ .render-trigger -> mode 'kick 9'
- ✅ .toolbox-trigger -> mode 'upscale v4'
