# وضعیت ریپو — ساخته‌شده با اجرا، نه با ادعا

> خودکار از `python3 studio/verify.py` — 2026-10-30 20:39 UTC · پایتون 3.11.2 · sandbox

| ok | FAIL | skip | warn |
|---|---|---|---|
| 17 | 0 | 20 | 0 |

> ⚠️ 12 وابستگی در این محیط نصب نبود؛ آن ردیف‌ها `skip` شده‌اند، نه pass. روی رانر (verify.yml) باید همه اجرا شوند: PIL, androguard, basicsr, cv2, ffmpeg, imageio_ffmpeg, kokoro_onnx, numpy, pyanime4k, realesrgan, soundfile, torch

## compile

- ✅ 39/39 compile

## data

- ✅ 61 json files parse
- ✅ 7 workflows parse (structural check — pyyaml not installed here)

## deps

- ✅ every declared dependency matches the file's imports

## inventory

- ✅ 46 entries, every file accounted for

## smoke

- ⏭️ bridge/mivi_mcp.py needs imageio_ffmpeg
- ✅ mivi_web/make_catalog.py --help (0.0s)
- ⏭️ mivi_web/re/dumpclass.py needs androguard
- ⏭️ mivi_web/re/fields.py needs androguard
- ⏭️ mivi_web/re/m2.py needs androguard
- ⏭️ mivi_web/re/staticdump.py needs androguard
- ⏭️ mivi_web/re/xref2.py needs androguard
- ⏭️ studio/artgen.py needs PIL, ffmpeg
- ⏭️ studio/chainkit.py needs PIL, imageio_ffmpeg
- ⏭️ studio/cutlist.py needs cv2, imageio_ffmpeg, numpy
- ⏭️ studio/filmkit.py needs PIL, imageio_ffmpeg
- ✅ studio/knowledge/bank.py --help (0.1s)
- ✅ studio/knowledge/measure.py --help (0.1s)
- ⏭️ studio/lipsync.py needs ffmpeg
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
- ⏭️ studio/toolbox/upscale.py needs PIL, basicsr, numpy, pyanime4k, realesrgan, torch
- ⏭️ studio/voice.py needs kokoro_onnx, soundfile, ffmpeg
- ⏭️ studio/voicetest.py needs ffmpeg
- ✅ studio/wanprompt.py --help (0.0s)

## triggers

- ✅ .mivi-trigger -> films/short16/gen_jobs_empty.json
- ✅ .photo-trigger -> mode 'probe'
- ✅ .render-trigger -> mode 'kick 9'
- ✅ .toolbox-trigger -> mode 'upscale v4'
