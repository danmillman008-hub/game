# وضعیت ریپو — ساخته‌شده با اجرا، نه با ادعا

> خودکار از `python3 studio/verify.py` — 2026-10-31 17:53 UTC · پایتون 3.11.2 · sandbox

| ok | FAIL | skip | warn |
|---|---|---|---|
| 43 | 9 | 7 | 1 |

> ⚠️ 7 وابستگی نصب نیست؛ ردیف‌های وابسته `skip` شده‌اند، نه pass — نسخهٔ رانر (verify.yml) این‌ها را نصب می‌کند، پس آنجا باید اجرا شوند: androguard, basicsr, kokoro_onnx, pyanime4k, realesrgan, soundfile, torch

## compile

- ✅ 43/43 compile

## data

- ✅ 74 json files parse
- ✅ 8 workflows parse (structural check — pyyaml not installed here)

## deps

- ✅ every declared dependency matches the file's imports

## inventory

- ✅ 51 entries, every file accounted for

## links

- ❌ studio/knowledge/method/CONSISTENCY_PLAYBOOK.md: mentions missing file films/before_leaving/.probe/probe.py
- ⚠️ films/anime_ten/deliver/scene_min1.mp4: 23 MB (over 20 MB, tracked in git)
- ❌ 784 files · 1 breaks · 1 size warning(s)

## make

- ✅ 14/14 targets resolve

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
- ⏭️ mivi_web/re/dumpclass.py needs androguard
- ⏭️ mivi_web/re/fields.py needs androguard
- ⏭️ mivi_web/re/m2.py needs androguard
- ⏭️ mivi_web/re/staticdump.py needs androguard
- ⏭️ mivi_web/re/xref2.py needs androguard
- ✅ studio/artgen.py --help (0.0s)
- ✅ studio/cast.py --help (0.1s)
- ✅ studio/chainkit.py --help (0.1s)
- ✅ studio/cutlist.py --help (0.1s)
- ✅ studio/filmkit.py --help (0.1s)
- ✅ studio/housecheck.py --help (0.0s)
- ✅ studio/knowledge/bank.py --help (0.1s)
- ✅ studio/knowledge/banktest.py -> ALL OK
- ✅ studio/knowledge/measure.py --help (0.1s)
- ❌ studio/links.py rc=1: 784 tracked files · 1 breaks · 1 size warnings
- ✅ studio/lipsync.py --help (0.0s)
- ✅ studio/lumatch.py --help (0.0s)
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
- ⏭️ studio/voice.py needs kokoro_onnx, soundfile
- ✅ studio/voicetest.py -> ALL OK
- ✅ studio/wanprompt.py --help (0.0s)
- ❌ mivi_web/re/dumpclass.py did not run (ci=true): needs androguard
- ❌ mivi_web/re/fields.py did not run (ci=true): needs androguard
- ❌ mivi_web/re/m2.py did not run (ci=true): needs androguard
- ❌ mivi_web/re/staticdump.py did not run (ci=true): needs androguard
- ❌ mivi_web/re/xref2.py did not run (ci=true): needs androguard
- ❌ studio/voice.py did not run (ci=true): needs kokoro_onnx, soundfile

## triggers

- ✅ .mivi-trigger -> films/short16/gen_jobs_winter_b.json
- ✅ .photo-trigger -> mode 'probe'
- ✅ .render-trigger -> mode 'kick 9'
- ✅ .toolbox-trigger -> mode 'upscale v4'
