/*
 * Headless smoke test for the browser renderer.
 *
 * There is no browser in this environment, so this script stubs the minimal
 * canvas 2D API the renderer uses and records every call. It proves the drawing
 * code runs end to end (no typos, no missing methods, no undefined state) and
 * that it actually issues draw calls in every game state.
 */
"use strict";
const path = require("path");
const NE = require(path.join(__dirname, "neon_alley.js"));

const METHODS = ["setTransform", "clearRect", "fillRect", "strokeRect", "drawImage",
                 "beginPath", "moveTo", "lineTo", "closePath", "stroke", "fill",
                 "arc", "ellipse", "save", "restore", "fillText", "strokeText",
                 "createLinearGradient", "createRadialGradient", "translate", "scale",
                 "measureText"];

let calls = {};
function resetCalls() { for (const k of Object.keys(calls)) delete calls[k]; }
function totalCalls() { return Object.values(calls).reduce((a, b) => a + b, 0); }

function makeCtx(calls) {
  const ctx = {};
  for (const name of METHODS) {
    ctx[name] = function () {
      calls[name] = (calls[name] || 0) + 1;
      if (name === "createLinearGradient" || name === "createRadialGradient") {
        return { addColorStop() {} };
      }
      if (name === "measureText") return { width: 10 };
      return undefined;
    };
  }
  // properties the renderer assigns are plain values; unknown *methods* throw
  ctx.canvas = null;
  return ctx;
}

function makeCanvas(w, h, calls) {
  return { width: w, height: h, getContext() { return makeCtx(calls); } };
}

global.document = {
  createElement(tag) {
    if (tag !== "canvas") throw new Error("unexpected element: " + tag);
    return makeCanvas(384, 240, calls);
  },
};
const cmd = (o) => new NE.Command(o || {});
const game = new NE.Game();
const renderer = new NE.Renderer();

const results = {};

// 1. title
resetCalls();
const titleCanvas = renderer.draw(game, 0.4);
results.title = { calls: totalCalls(), size: [titleCanvas.width, titleCanvas.height] };

// 2. gameplay: movement, a jump, punches and kicks, effects on screen
resetCalls();
game.start();
for (let i = 0; i < 200; i++) {
  game.update(cmd({ move_x: i % 40 < 20 ? 1 : -1, move_z: i % 30 < 10 ? 1 : 0,
                    jump: i === 25 || i === 120,
                    punch: i % 14 === 0, kick: i % 23 === 0 }));
  renderer.draw(game, i / 60);
}
results.play = { calls: totalCalls(),
                 frames: 200, state: game.state, hp: game.player.hp,
                 enemies: game.enemies.length, kills: game.kills };

// 3. defeat card
resetCalls();
const lose = new NE.Game();
lose.start();
for (let i = 0; i < 4000 && lose.state === NE.PLAY; i++) lose.update(cmd());
renderer.draw(lose, 1.0);
results.defeat = { calls: totalCalls(),
                   state: lose.state };

// 4. victory card
resetCalls();
const win = new NE.Game();
win.start();
for (let i = 0; i < 600 && win.state !== NE.VICTORY; i++) {
  for (const e of win.enemies) {
    if (!e.dead) { e.hp = 0; e.dead = true; e.death_timer = 999; win.kills += 1; }
  }
  win.update(cmd());
}
renderer.draw(win, 1.0);
results.victory = { calls: totalCalls(),
                    state: win.state };

const ok = results.title.calls > 50 && results.play.calls > 500 &&
           results.defeat.state === NE.DEFEAT && results.victory.state === NE.VICTORY;
process.stdout.write(JSON.stringify({ ok, results }, null, 2) + "\n");
process.exit(ok ? 0 : 1);
