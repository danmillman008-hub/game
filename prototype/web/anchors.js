"use strict";
const NE = require(require("path").join(__dirname, "neon_alley.js"));
const ONE = NE.ONE;
function box(typeId, spriteW, spriteH, x, z) {
  const a = new NE.Actor(typeId, spriteW, spriteH, x * ONE, z * ONE, 0);
  return NE.buildPlayerBoxes(a, false)[0].asTuple();
}
process.stdout.write(JSON.stringify({
  player_100_60: box(1, 7, 7, 100, 60),
  enemy_200_60: box(1, 2, 6, 200, 60),
}) + "\n");
