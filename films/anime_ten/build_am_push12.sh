#!/usr/bin/env bash
# 12 seconds, one unbroken take, one cast.
#
# What the three-move batch taught us (18:49): the model will NOT hold a camera that
# was told to hold still. `am_still` ("The camera holds still.") pushed in anyway;
# `am_slow` and `am_still` ended within one step of each other; `am_fast` really was
# faster. Three takes from one anchor are therefore three ramps that all OPEN on the
# same wide frame — so any cut between them jumps the scale backwards, and a 12 s
# monotone cut cannot be built from 4 s takes at all.
#
# A single take can be 12 s though: the push is smooth in a flat cel drawing, so a
# 4.14x time stretch with motion interpolation keeps it clean (measured: median
# frame-to-frame difference 2.72/255, max 6.22 — no judder, no warping at full res).
set -euo pipefail
cd "$(dirname "$0")/../.."

PY=${PY:-/tmp/v3/bin/python}
FF=$( "$PY" -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())" )
SRC=films/short16/clips_gen/am_fast_a1.mp4
OUT=films/anime_ten/deliver/am_push_12s.mp4
TMP=$(mktemp -d)
TARGET=58
STRETCH=4.14          # 2.9 s of push -> 12.0 s

mkdir -p films/anime_ten/deliver
"$PY" studio/lumatch.py measure "$SRC"

# 1. stretch. `mci` + `aobmc` + `vsbmc` is the slow, warping-averse mode; a faster
#    mode visible on line art as wobbling outlines.
"$FF" -y -v error -i "$SRC" -vf \
  "trim=0:2.9,setpts=PTS-STARTPTS,minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:vsbmc=1,setpts=${STRETCH}*PTS,fps=24,setsar=1,scale=960:1280" \
  -t 12 -c:v libx264 -crf 16 -pix_fmt yuv420p -an "$TMP/stretch.mp4"

# 2. one exposure, then the fades
"$PY" studio/lumatch.py match "$TMP/stretch.mp4" --out "$TMP/n" --target $TARGET --trim 12.0
"$FF" -y -v error -i "$TMP/n/stretch_norm.mp4" \
  -vf "fade=t=in:st=0:d=0.4,fade=t=out:st=11.4:d=0.6" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p -an -movflags +faststart "$OUT"

# 3. the numbers
"$PY" studio/lumatch.py measure "$OUT"
"$FF" -i "$OUT" 2>&1 | grep -E "Duration|Stream #0:0" || true
ls -lh "$OUT"
echo "tmp: $TMP"
