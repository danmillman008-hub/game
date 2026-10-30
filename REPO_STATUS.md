# وضعیت ریپو — ساخته‌شده با اجرا، نه با ادعا

> خودکار از `python3 studio/verify.py` — 2026-10-30 20:54 UTC · پایتون 3.11.2 · sandbox

| ok | FAIL | skip | warn |
|---|---|---|---|
| 47 | 0 | 1 | 1 |

> ⚠️ 4 وابستگی نصب نیست؛ ردیف‌های وابسته `skip` شده‌اند، نه pass — نسخهٔ رانر (verify.yml) این‌ها را نصب می‌کند، پس آنجا باید اجرا شوند: basicsr, pyanime4k, realesrgan, torch

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

- ⚠️ films/anime_ten/deliver/scene_min1.mp4: 23 MB (over 20 MB, tracked in git)
- ✅ 695 files · 0 breaks · 1 size warning(s)

## selftest

- ✅ inventory catches an unlisted file -> FAIL
- ✅ inventory catches a phantom entry -> FAIL
- ✅ deps catches an undeclared import -> FAIL
- ✅ ci mode fails on a declared dependency that is missing -> FAIL
- ✅ a healthy entry passes (control) -> ok

## smoke

- ✅ bridge/mivi_mcp.py --help (0.1s)
- ✅ mivi_web/make_catalog.py --help (0.0s)
- ✅ mivi_web/re/annpaths.py --help (0.0s)
- ✅ mivi_web/re/dexann.py --help (0.0s)
- ✅ mivi_web/re/dumpclass.py --help (0.2s)
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
- ✅ studio/links.py -> 695 tracked files · 0 breaks · 1 size warnings
- ✅ studio/lipsync.py --help (0.0s)
- ✅ studio/mivi_photo.py --help (0.1s)
- ✅ studio/mivi_shot.py --help (0.1s)
- ✅ studio/motionbank.py --help (0.0s)
- ✅ studio/motionlint.py --help (0.1s)
- ✅ studio/motions/ten_shots.py --help (0.0s)
- ✅ studio/render_film.py --help (0.1s)
- ✅ studio/scorer.py --help (0.1s)
- ✅ studio/selftest.py -> SELFTEST OK
- ✅ studio/shotplan.py --help (0.0s)
- ✅ studio/tests/test_mivi_shot.py -> PASS — success recorded, chain waited, refusal isolated
- ⏭️ studio/toolbox/upscale.py needs basicsr, pyanime4k, realesrgan, torch — torch + realesrgan + basicsr ~2.5 GB and model weights; not installed on the runner
- ✅ studio/verify.py --help (0.1s)
- ✅ studio/voice.py --help (0.1s)
- ✅ studio/voicetest.py -> ALL OK
- ✅ studio/wanprompt.py --help (0.0s)

## triggers

- ✅ .mivi-trigger -> films/short16/gen_jobs_empty.json
- ✅ .photo-trigger -> mode 'probe'
- ✅ .render-trigger -> mode 'kick 9'
- ✅ .toolbox-trigger -> mode 'upscale v4'
