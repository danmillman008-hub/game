# وضعیت ریپو — ساخته‌شده با اجرا، نه با ادعا

> خودکار از `python3 studio/verify.py` — 2026-10-30 20:43 UTC · پایتون 3.11.17 · runner

| ok | FAIL | skip | warn |
|---|---|---|---|
| 33 | 0 | 7 | 0 |

> ⚠️ 7 وابستگی در این محیط نصب نبود؛ آن ردیف‌ها `skip` شده‌اند، نه pass. روی رانر (verify.yml) باید همه اجرا شوند: androguard, basicsr, kokoro_onnx, pyanime4k, realesrgan, soundfile, torch

## compile

- ✅ 40/40 compile

## data

- ✅ 62 json files parse
- ✅ 8 workflows parse

## deps

- ✅ every declared dependency matches the file's imports

## inventory

- ✅ 48 entries, every file accounted for

## smoke

- ✅ bridge/mivi_mcp.py --help (0.1s)
- ✅ mivi_web/make_catalog.py --help (0.0s)
- ⏭️ mivi_web/re/dumpclass.py needs androguard
- ⏭️ mivi_web/re/fields.py needs androguard
- ⏭️ mivi_web/re/m2.py needs androguard
- ⏭️ mivi_web/re/staticdump.py needs androguard
- ⏭️ mivi_web/re/xref2.py needs androguard
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
- ✅ studio/scorer.py --help (0.2s)
- ✅ studio/selftest.py -> SELFTEST OK
- ✅ studio/shotplan.py --help (0.0s)
- ✅ studio/tests/test_mivi_shot.py -> PASS — success recorded, chain waited, refusal isolated
- ⏭️ studio/toolbox/upscale.py needs basicsr, pyanime4k, realesrgan, torch
- ✅ studio/verify.py --help (0.0s)
- ⏭️ studio/voice.py needs kokoro_onnx, soundfile
- ✅ studio/voicetest.py -> ALL OK
- ✅ studio/wanprompt.py --help (0.0s)

## triggers

- ✅ .mivi-trigger -> films/short16/gen_jobs_empty.json
- ✅ .photo-trigger -> mode 'probe'
- ✅ .render-trigger -> mode 'kick 9'
- ✅ .toolbox-trigger -> mode 'upscale v4'
