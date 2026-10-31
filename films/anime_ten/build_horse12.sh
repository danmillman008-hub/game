#!/usr/bin/env bash
# The horse film: 12.00 s, three angles, one cast.
#
#   1  hw_wide     wide battlefield, low angle, the army in ranks, the rider small
#                  at the right edge — no face is legible, so costume and horse
#                  carry the identity (the shared paragraph in story_horse.md)
#   2  hm_master   three-quarter on her, army behind — the master, face legible
#   3  hc_close    from the master's LAST frame, so it is the same face by
#                  continuation, not by a new generation (S17)
#
# Every clip on this canvas opens on the blank `dusk` gradient: content starts at
# ~0.7 s (standard deviation of the frame jumps 12 -> 28). Cut at 0.8 s, which is
# why each take is 3.2 s and the 9.6 s cut is stretched 1.25x to 12.00 s.
# A 1.25x stretch of a flat cel drawing is invisible; it also buys a slight
# slow-motion weight on the charge without asking the model for anything (S19).
set -euo pipefail
cd "$(dirname "$0")/../.."

PY=${PY:-/tmp/v3/bin/python}
FF=$( "$PY" -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())" )
SRC=films/short16/clips_gen
OUT=films/anime_ten/deliver/horse_charge_12s.mp4
TMP=$(mktemp -d)
TARGET=80        # daylight: the palette here is sky and plain, not a night gate (58 was the winter line)
STRETCH=1.25

mkdir -p films/anime_ten/deliver

# 1. drop the blank-canvas opening of each take
i=1
for id in hw_wide hm_master hc_close; do
  "$FF" -y -v error -ss 0.8 -i "$SRC/${id}_a1.mp4" -t 3.2 \
        -vf "fps=24,setsar=1,scale=960:1280" -c:v libx264 -crf 16 -pix_fmt yuv420p -an \
        "$TMP/t$i.mp4"
  i=$((i+1))
done

# 2. one exposure for the three angles
"$PY" studio/lumatch.py match "$TMP/t1.mp4" "$TMP/t2.mp4" "$TMP/t3.mp4" \
      --out "$TMP/n" --target $TARGET --trim 3.2

# 3. cut, then stretch, then fade
printf "file '%s'\n" "$TMP/n/t1_norm.mp4" "$TMP/n/t2_norm.mp4" "$TMP/n/t3_norm.mp4" > "$TMP/list.txt"
"$FF" -y -v error -f concat -safe 0 -i "$TMP/list.txt" -c copy "$TMP/cut.mp4"
"$FF" -y -v error -i "$TMP/cut.mp4" -vf \
  "minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:vsbmc=1,setpts=${STRETCH}*PTS,fps=24" \
  -t 12 -c:v libx264 -crf 16 -pix_fmt yuv420p -an "$TMP/stretched.mp4"
"$FF" -y -v error -i "$TMP/stretched.mp4" \
  -vf "fade=t=in:st=0:d=0.4,fade=t=out:st=11.2:d=0.8" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p -an -movflags +faststart "$OUT"

# 4. the numbers
"$PY" studio/lumatch.py measure "$OUT"
"$FF" -i "$OUT" 2>&1 | grep -E "Duration|Stream #0:0" || true
ls -lh "$OUT"
echo "tmp: $TMP"
