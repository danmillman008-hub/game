#!/usr/bin/env bash
# Part 2 — she draws the blade and rides into the army — and the joined 24 s film.
#
#   1  hs_draw    from hc_close_last.png, the LAST frame of part 1, so the face is a
#                 continuation and the join is exact by construction (S17)
#   2  hs_melee   from hs_draw's last frame: the same face, now furious
#   3  hs_impact  from hw_wide_src.png, the field part 1 opened on: the riders go in
#
# What failed and is NOT in the film: `hs_clash`, a clash asked from a blank canvas —
# it came back as a poster of white smoke and white horses, not a battle. A melee
# between figures is still the shape this model cannot hold (S14, take 25): the
# "enemy line crashes past her" prompt was ignored and the army stood still.
# What exists is the draw, the anger, and the ride into the mass.
#
# These three takes are anchored on stills, not on a canvas, so they have no blank
# opening (S21) and no light loss (drift +0.4 %, -2.0 %, +4.0 %): 4.0 s each, no
# stretch needed.
set -euo pipefail
cd "$(dirname "$0")/../.."

PY=${PY:-/tmp/v3/bin/python}
FF=$( "$PY" -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())" )
SRC=films/short16/clips_gen
OUT=films/anime_ten/deliver
TMP=$(mktemp -d)
TARGET=80            # daylight, same target as part 1 (S23)

mkdir -p "$OUT"

# ---- part 2 takes -----------------------------------------------------------
i=1
for id in hs_draw hs_melee hs_impact; do
  "$FF" -y -v error -i "$SRC/${id}_a1.mp4" -t 4.0 \
        -vf "fps=24,setsar=1,scale=960:1280" -c:v libx264 -crf 16 -pix_fmt yuv420p -an \
        "$TMP/p2_$i.mp4"
  i=$((i+1))
done
"$PY" studio/lumatch.py match "$TMP/p2_1.mp4" "$TMP/p2_2.mp4" "$TMP/p2_3.mp4" \
      --out "$TMP/n" --target $TARGET --trim 4.0
printf "file '%s'\n" "$TMP/n/p2_1_norm.mp4" "$TMP/n/p2_2_norm.mp4" "$TMP/n/p2_3_norm.mp4" > "$TMP/p2.txt"
"$FF" -y -v error -f concat -safe 0 -i "$TMP/p2.txt" -c copy "$TMP/p2_raw.mp4"

# ---- part 1 again, without the closing fade, so the join at 12.0 s is clean ----
j=1
for id in hw_wide hm_master hc_close; do
  "$FF" -y -v error -ss 0.8 -i "$SRC/${id}_a1.mp4" -t 3.2 \
        -vf "fps=24,setsar=1,scale=960:1280" -c:v libx264 -crf 16 -pix_fmt yuv420p -an \
        "$TMP/p1_$j.mp4"
  j=$((j+1))
done
"$PY" studio/lumatch.py match "$TMP/p1_1.mp4" "$TMP/p1_2.mp4" "$TMP/p1_3.mp4" \
      --out "$TMP/n1" --target $TARGET --trim 3.2
printf "file '%s'\n" "$TMP/n1/p1_1_norm.mp4" "$TMP/n1/p1_2_norm.mp4" "$TMP/n1/p1_3_norm.mp4" > "$TMP/p1.txt"
"$FF" -y -v error -f concat -safe 0 -i "$TMP/p1.txt" -c copy "$TMP/p1_cut.mp4"
"$FF" -y -v error -i "$TMP/p1_cut.mp4" -vf \
  "minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:vsbmc=1,setpts=1.25*PTS,fps=24" \
  -t 12 -c:v libx264 -crf 16 -pix_fmt yuv420p -an "$TMP/p1_nofade.mp4"

# ---- 1. part 2 on its own, 12.00 s -----------------------------------------
"$FF" -y -v error -i "$TMP/p2_raw.mp4" \
  -vf "fade=t=in:st=0:d=0.4,fade=t=out:st=11.2:d=0.8" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p -an -movflags +faststart "$OUT/horse_sword_12s.mp4"

# ---- 2. the two parts, joined at exactly 12.00 s ---------------------------
printf "file '%s'\n" "$TMP/p1_nofade.mp4" "$TMP/p2_raw.mp4" > "$TMP/both.txt"
"$FF" -y -v error -f concat -safe 0 -i "$TMP/both.txt" -c copy "$TMP/both_raw.mp4"
"$FF" -y -v error -i "$TMP/both_raw.mp4" \
  -vf "fade=t=in:st=0:d=0.4,fade=t=out:st=23.2:d=0.8" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p -an -movflags +faststart "$OUT/horse_battle_24s.mp4"

# ---- the numbers -----------------------------------------------------------
for f in "$OUT/horse_sword_12s.mp4" "$OUT/horse_battle_24s.mp4"; do
  echo "== $f"
  "$PY" studio/lumatch.py measure "$f" | head -3
  "$FF" -i "$f" 2>&1 | grep -E "Duration|Stream #0:0" || true
done
ls -lh "$OUT/horse_sword_12s.mp4" "$OUT/horse_battle_24s.mp4"
echo "tmp: $TMP"
