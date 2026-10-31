#!/usr/bin/env bash
# Part 3 — the war, weighted by the frame rather than by the prompt.
#
# Why the earlier takes failed (S27/S28, method/WEIGHTING.md): the model always
# pushes in on the strongest readable FACE in the frame, and a "pull back" does not
# cancel it. The earlier films were portraits because a face was there to land on.
# Here every take either has no legible face or is cut before the push arrives.
#
# The windows below are measured, not guessed (per-second mean luma):
#   hw_backs / hw_wall are canvas->video, so they fade up from black: skip 1.0 / 1.4 s.
#   hw_surge / hw_pull / hs_impact are image->video, no fade: usable from 0.3 s.
#   hw_wall and hw_pull are cut at 3.0 s because their push reaches her face by 3.2 s.
#
# Frame counts are exact: 24 fps, 288 frames = 12.00 s.
#
#   war   backs 2.83 | wall 1.67 | surge 2.67 | pull 1.67 | impact 3.17   = 12.00 s
#   full  approach 8.00 | sword 4.00 | war 12.00                          = 24.00 s
#
# take 51 (`hw_clash`, anchored on impact's last frame) asked for the line to meet the
# enemy. It came back as a slow walk across the field — 15-18 frame delta, below even
# hw_backs' 29-32, and no collision anywhere. Crowd-melee is still silently softened.
# So the film ends on the charge itself (impact, cut at 3.45, before the walk) and
# fades on it. The credit is spent and recorded as a miss.
set -euo pipefail
cd "$(dirname "$0")/../.."

PY=${PY:-/tmp/v3/bin/python}
FF=$( "$PY" -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())" )
SRC=films/short16/clips_gen
OUT=films/anime_ten/deliver
TMP=$(mktemp -d)
TARGET=80

mkdir -p "$OUT"

# frame-exact take: id start frames index
take () {
  "$FF" -y -v error -ss "$2" -i "$SRC/$1_a1.mp4" -frames:v "$3" \
        -vf "fps=24,setsar=1,scale=960:1280" -c:v libx264 -crf 16 -pix_fmt yuv420p -an \
        "$TMP/t$4.mp4"
}
take hw_backs  1.00 68 1
take hw_wall   1.40 40 2
take hw_surge  0.30 64 3
take hw_pull   0.40 40 4
take hs_impact 0.28 76 5

"$PY" studio/lumatch.py match "$TMP"/t{1,2,3,4,5}.mp4 --out "$TMP/nw" --target $TARGET --trim 0
printf "file '%s'\n" "$TMP/nw/t1_norm.mp4" "$TMP/nw/t2_norm.mp4" "$TMP/nw/t3_norm.mp4" \
                      "$TMP/nw/t4_norm.mp4" "$TMP/nw/t5_norm.mp4" > "$TMP/war.txt"
"$FF" -y -v error -f concat -safe 0 -i "$TMP/war.txt" -c copy "$TMP/war_raw.mp4"
"$FF" -y -v error -i "$TMP/war_raw.mp4" -frames:v 288 -vf \
  "fade=t=in:st=0:d=0.35,fade=t=out:st=11.15:d=0.85,tpad=stop_mode=clone:stop_duration=0.2" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p -an -movflags +faststart "$OUT/horse_war_12s.mp4"

# ---- the full piece -------------------------------------------------------
# Part 1 is slowed to carry the approach in 8 s instead of 12 — three framings of
# one face is exactly the weighting this cut is fixing.
# Part 2 contributes 4 s: the blade comes up (3) then one cut back to the army (1).
j=1
for id in hw_wide hm_master; do
  "$FF" -y -v error -ss 0.50 -i "$SRC/${id}_a1.mp4" -frames:v 77 \
        -vf "fps=24,setsar=1,scale=960:1280" -c:v libx264 -crf 16 -pix_fmt yuv420p -an "$TMP/a$j.mp4"
  j=$((j+1))
done
"$FF" -y -v error -ss 0.30 -i "$SRC/hs_sword_a1.mp4" -frames:v 72 \
      -vf "fps=24,setsar=1,scale=960:1280" -c:v libx264 -crf 16 -pix_fmt yuv420p -an "$TMP/b1.mp4"
"$FF" -y -v error -ss 0.30 -i "$SRC/hs_war_a1.mp4" -frames:v 24 \
      -vf "fps=24,setsar=1,scale=960:1280" -c:v libx264 -crf 16 -pix_fmt yuv420p -an "$TMP/b2.mp4"

"$PY" studio/lumatch.py match "$TMP/a1.mp4" "$TMP/a2.mp4" --out "$TMP/na" --target $TARGET --trim 0
"$PY" studio/lumatch.py match "$TMP/b1.mp4" "$TMP/b2.mp4" --out "$TMP/nb" --target $TARGET --trim 0
printf "file '%s'\n" "$TMP/na/a1_norm.mp4" "$TMP/na/a2_norm.mp4" > "$TMP/ap.txt"
"$FF" -y -v error -f concat -safe 0 -i "$TMP/ap.txt" -c copy "$TMP/ap.mp4"
"$FF" -y -v error -i "$TMP/ap.mp4" -vf \
  "minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:vsbmc=1,setpts=1.25*PTS,fps=24" \
  -frames:v 192 -c:v libx264 -crf 16 -pix_fmt yuv420p -an "$TMP/ap8.mp4"

printf "file '%s'\n" "$TMP/ap8.mp4" "$TMP/nb/b1_norm.mp4" "$TMP/nb/b2_norm.mp4" \
                      "$TMP/nw/t1_norm.mp4" "$TMP/nw/t2_norm.mp4" "$TMP/nw/t3_norm.mp4" \
                      "$TMP/nw/t4_norm.mp4" "$TMP/nw/t5_norm.mp4" > "$TMP/all.txt"
"$FF" -y -v error -f concat -safe 0 -i "$TMP/all.txt" -c copy "$TMP/all_raw.mp4"
"$FF" -y -v error -i "$TMP/all_raw.mp4" -frames:v 576 -vf \
  "fade=t=in:st=0:d=0.4,fade=t=out:st=23.2:d=0.8,tpad=stop_mode=clone:stop_duration=0.4" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p -an -movflags +faststart "$OUT/horse_battle_24s_war.mp4"

for f in "$OUT/horse_war_12s.mp4" "$OUT/horse_battle_24s_war.mp4"; do
  echo "== $f"
  "$PY" studio/lumatch.py measure "$f" | head -3
  "$FF" -i "$f" 2>&1 | grep -E "Duration|Stream #0:0" || true
done
ls -lh "$OUT/horse_war_12s.mp4" "$OUT/horse_battle_24s_war.mp4"
echo "tmp: $TMP"
