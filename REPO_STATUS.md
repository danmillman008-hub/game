# وضعیت ریپو — ساخته‌شده با اجرا، نه با ادعا

> خودکار از `python3 studio/verify.py` — 2026-10-31 20:32 UTC · پایتون 3.11.2 · sandbox

| ok | FAIL | skip | warn |
|---|---|---|---|
| 31 | 0 | 21 | 1 |

> ⚠️ 12 وابستگی نصب نیست؛ ردیف‌های وابسته `skip` شده‌اند، نه pass — نسخهٔ رانر (verify.yml) این‌ها را نصب می‌کند، پس آنجا باید اجرا شوند: PIL, androguard, basicsr, cv2, ffmpeg, imageio_ffmpeg, kokoro_onnx, numpy, pyanime4k, realesrgan, soundfile, torch

## compile

- ✅ 43/43 compile

## data

- ✅ 93 json files parse
- ✅ 8 workflows parse (structural check — pyyaml not installed here)

## deps

- ✅ every declared dependency matches the file's imports

## inventory

- ✅ 51 entries, every file accounted for

## links

- ⚠️ films/anime_ten/deliver/scene_min1.mp4: 23 MB (over 20 MB, tracked in git)
- ✅ 910 files · 0 breaks · 1 size warning(s)

## make

- ✅ 14/14 targets resolve

## selftest

- ✅ inventory catches an unlisted file -> FAIL
- ✅ inventory catches a phantom entry -> FAIL
- ✅ deps catches an undeclared import -> FAIL
- ✅ ci mode fails on a declared dependency that is missing -> FAIL
- ✅ a healthy entry passes (control) -> ok

## smoke

- ⏭️ bridge/mivi_mcp.py needs imageio_ffmpeg
- ✅ mivi_web/make_catalog.py --help (0.0s)
- ✅ mivi_web/re/annpaths.py --help (0.0s)
- ✅ mivi_web/re/dexann.py --help (0.0s)
- ⏭️ mivi_web/re/dumpclass.py needs androguard
- ⏭️ mivi_web/re/fields.py needs androguard
- ⏭️ mivi_web/re/m2.py needs androguard
- ⏭️ mivi_web/re/staticdump.py needs androguard
- ⏭️ mivi_web/re/xref2.py needs androguard
- ⏭️ studio/artgen.py needs PIL, ffmpeg
- ✅ studio/cast.py --help (0.1s)
- ⏭️ studio/chainkit.py needs PIL, imageio_ffmpeg
- ⏭️ studio/cutlist.py needs cv2, imageio_ffmpeg, numpy
- ⏭️ studio/filmkit.py needs PIL, imageio_ffmpeg
- ✅ studio/housecheck.py --help (0.0s)
- ✅ studio/knowledge/bank.py --help (0.1s)
- ✅ studio/knowledge/banktest.py -> ALL OK
- ✅ studio/knowledge/measure.py --help (0.1s)
- ✅ studio/links.py -> 910 tracked files · 0 breaks · 1 size warnings
- ⏭️ studio/lipsync.py needs ffmpeg
- ⏭️ studio/lumatch.py needs PIL, ffmpeg — PIL only; skipped where pillow is absent
- ✅ studio/mivi_photo.py --help (0.1s)
- ⏭️ studio/mivi_shot.py needs imageio_ffmpeg
- ✅ studio/motionbank.py --help (0.0s)
- ⏭️ studio/motionlint.py needs cv2, numpy
- ✅ studio/motions/ten_shots.py --help (0.0s)
- ⏭️ studio/render_film.py needs PIL, ffmpeg
- ⏭️ studio/scorer.py needs cv2, imageio_ffmpeg, numpy
- ⏭️ studio/selftest.py needs ffmpeg
- ✅ studio/shotplan.py --help (0.0s)
- ⏭️ studio/tests/test_mivi_shot.py needs imageio_ffmpeg
- ⏭️ studio/toolbox/upscale.py needs PIL, basicsr, numpy, pyanime4k, realesrgan, torch — torch + realesrgan + basicsr ~2.5 GB and model weights; not installed on the runner
- ✅ studio/verify.py --help (0.0s)
- ⏭️ studio/voice.py needs kokoro_onnx, soundfile, ffmpeg
- ⏭️ studio/voicetest.py needs ffmpeg
- ✅ studio/wanprompt.py --help (0.0s)

## triggers

- ✅ .mivi-trigger -> films/short16/gen_jobs_horse_l.json
- ✅ .photo-trigger -> mode 'probe'
- ✅ .render-trigger -> mode 'kick 9'
- ✅ .toolbox-trigger -> mode 'upscale v4'
