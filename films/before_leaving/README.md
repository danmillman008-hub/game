# قبل از رفتن — production notes

**Delivered:** 2:15 · 960×1280 (720P) · 32 fps · 37 shots · Persian VO (partial) · burned Persian subs
Drive: https://drive.google.com/file/d/19BH3lnmZgOiWkd3ShAiZCDFcPY8tCdKD/view

## Where each asset came from

| Asset | How |
|---|---|
| `assets/master_wide.png` | agent image generation (2 characters, rainy bus stop) |
| `assets/m_raha_close.png`, `m_arad_close.png` | agent generation — Mivi's composer cannot invent new angles (it regenerates the whole frame: master+crop returned a 3-person full-body shot) |
| `assets/m_bench_two.png`, `m_ots.png`, `m_walkaway.png`, `m_bus.png` | agent generation |
| 26 coverage stills | `crop:` local cover-fit to 960×1280 (no server dependency — Mivi superres went async/unreliable) |
| 37 clips | Mivi `beatImage2Video/createNormalTask` (6209), 720P, 4.03 s each |
| edit | ffmpeg xfade 0.4 s, subtitle overlay from shaped PNGs, VO timeline + ducking |
| VO | **21 of 21 lines**, two voices (Raha `voice-00`, Arad `voice-01`), laid on the cut timeline by `filmkit vo`, mixed with `filmkit mix`, normalised to -16 LUFS by `filmkit loud` |

## Honest defects

1. **Costume drift between scenes** — the master (grey coat) and the generated close-ups
   (grey) are consistent, but scene 3's walkaway/bus plates introduce a scarf and a
   slightly different coat. Visible at the 1:50 mark.
2. ~~VO is partial~~ — **fixed**: 17 clips cover all 21 lines (contiguous sentences were
   recorded as one take and span their shots), mixed and loudness-normalised.
3. **Text in frame** — one plate (bench two-shot) came back with a "BUS STOP / اتوبوس" sign;
   it reads as set dressing, not an error, but it is not ours.
4. **Lip sync** — none (Mivi's is account-locked). All dialogue is VO/subtitle over
   non-speaking coverage, per the playbook.
