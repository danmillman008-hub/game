/*
 * Conformance harness for the browser port.
 *
 *   node prototype/web/conformance.js <input.json>
 *
 * <input.json> is {"commands":[{"move_x":..,"move_z":..,"jump":..,"punch":..,"kick":..}, ...]}
 * The harness replays it through the JavaScript engine and prints one full state
 * dump per frame. prototype/tools/web_conformance.py compares that output with the
 * Python reference, exactly, frame by frame.
 */
"use strict";
const fs = require("fs");
const path = require("path");
const NE = require(path.join(__dirname, "neon_alley.js"));

const file = process.argv[2];
if (!file) {
  console.error("usage: node conformance.js <input.json>");
  process.exit(2);
}
const doc = JSON.parse(fs.readFileSync(file, "utf8"));
const commands = doc.commands || doc;

const game = new NE.Game();
game.start();
const dumps = [];
for (const c of commands) {
  if (game.state !== NE.PLAY) break;
  game.update(new NE.Command(c));
  dumps.push(game.dump());
}
process.stdout.write(JSON.stringify(dumps));
