#!/usr/bin/env bash
# The anime-film edit, reproducible: three clips, one cast, one exposure.
#
#   films/short16/clips_gen/am_master_a1.mp4   wide pair at the gate   (4.03 s)
#   films/short16/clips_gen/am_push_a1.mp4     push in to the faces    (4.03 s)
#   films/short16/clips_gen/am_cu_a1.mp4       faces, snow, breath     (4.03 s)
#
# Why the first clip is cut at 0.55 s: it is the only one painted from a blank
# canvas, so the model fades in from white (81.7 -> 46.9 over 0.5 s). lumatch reports
# that as a 42 % "light loss"; it is not drift, it is an opening fade. Cut it, then
# match what is left.
#
# Everything else on this line holds still: the two pushes were generated from the
# master, so neither pumps (drift +0.2 % and +2.5 %).
set -euo pipefail
cd "$(dirname "$0")/../.."

PY=${PY:-/tmp/v3/bin/python}          # pillow + imageio-ffmpeg
FF=$( "$PY" -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())" )
SRC=films/short16/clips_gen
TMP=$(mktemp -d)
OUT=films/anime_ten/deliver/am_guard_11s.mp4
TARGET=58
mkdir -p films/anime_ten/deliver

# 1. drop the blank-canvas fade
"$FF" -y -v error -ss 0.55 -i "$SRC/am_master_a1.mp4" -t 3.5 \
      -vf "fps=24,setsar=1,scale=960:1280" -c:v libx264 -crf 18 -pix_fmt yuv420p -an "$TMP/s1.mp4"

# 2. one mean for all three shots
"$PY" studio/lumatch.py match "$TMP/s1.mp4" --out "$TMP/n" --target $TARGET --trim 3.5
"$PY" studio/lumatch.py match "$SRC/am_push_a1.mp4" "$SRC/am_cu_a1.mp4" --out "$TMP/n" --target $TARGET --trim 4.0

# 3. fades, then the cut
#
# ORDER MATTERS, and got it wrong the first time: shots 1 and 2 both OPEN on the
# wide pair, so cutting master -> push jumps the scale *backwards* mid-film. The push
# is the only clip that moves, so it goes first (wide -> close), the close-up holds,
# and the film cuts wide for its last beat. That is a cut, not a mistake.
"$FF" -y -v error -i "$TMP/n/am_push_a1_norm.mp4" -vf "fade=t=in:st=0:d=0.4" \
      -c:v libx264 -crf 18 -pix_fmt yuv420p -an "$TMP/f1.mp4"
"$FF" -y -v error -i "$TMP/n/am_cu_a1_norm.mp4" -c copy "$TMP/f2.mp4"
"$FF" -y -v error -i "$TMP/n/s1_norm.mp4" -vf "fade=t=out:st=2.9:d=0.6" \
      -c:v libx264 -crf 18 -pix_fmt yuv420p -an "$TMP/f3.mp4"
printf "file '%s'\n" "$TMP/f1.mp4" "$TMP/f2.mp4" "$TMP/f3.mp4" > "$TMP/list.txt"
"$FF" -y -v error -f concat -safe 0 -i "$TMP/list.txt" -c copy -movflags +faststart "$OUT"

# 4. say the numbers, do not assume them
"$PY" studio/lumatch.py measure "$OUT"
"$FF" -i "$OUT" 2>&1 | grep -E "Duration|Stream #0:0" || true
ls -lh "$OUT"
echo "tmp: $TMP"
