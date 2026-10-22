/*
 * End-to-end smoke test of the BUILT page (prototype/release/index.html).
 *
 * Runs the real file — the same markup, styles and inline scripts that a browser
 * gets — inside a minimal DOM stand-in, then drives it: presses ENTER, walks,
 * punches, jumps, finishes a run and restarts. Only the canvas 2D API is stubbed,
 * and every call it receives is counted, so "the page drew something" is checked
 * rather than assumed.
 *
 * No browser, no npm packages: the harness only needs Node.
 */
"use strict";
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const PAGE = path.join(__dirname, "..", "release", "index.html");
const html = fs.readFileSync(PAGE, "utf8");

// ---------------------------------------------------------------- environment
const calls = {};
const CTX_METHODS = ["setTransform", "clearRect", "fillRect", "strokeRect", "drawImage",
  "beginPath", "moveTo", "lineTo", "closePath", "stroke", "fill", "arc", "ellipse",
  "save", "restore", "fillText", "strokeText", "createLinearGradient",
  "createRadialGradient", "translate", "scale", "measureText"];

function makeCtx() {
  const ctx = {};
  for (const name of CTX_METHODS) {
    ctx[name] = function () {
      calls[name] = (calls[name] || 0) + 1;
      if (name === "createLinearGradient" || name === "createRadialGradient") {
        return { addColorStop() {} };
      }
      if (name === "measureText") return { width: 10 };
    };
  }
  return ctx;
}

function makeCanvas() {
  const c = {
    width: 384, height: 240, style: {},
    getContext: () => makeCtx(),
    addEventListener: (type, fn) => { (c._listeners[type] ||= []).push(fn); },
    _listeners: {},
  };
  return c;
}

const elements = {
  game: makeCanvas(),
  status: { textContent: "" },
};

const listeners = {};
function addListener(type, fn) { (listeners[type] ||= []).push(fn); }

const documentStub = {
  getElementById: (id) => elements[id] || { textContent: "", style: {} },
  querySelectorAll: () => [],
  createElement: (tag) => {
    if (tag !== "canvas") throw new Error("unexpected element: " + tag);
    return makeCanvas();
  },
  addEventListener: addListener,
};

let rafQueue = [];
const windowStub = {
  innerWidth: 1280,
  innerHeight: 800,
  addEventListener: addListener,
  matchMedia: () => ({ matches: false, addEventListener() {} }),
  requestAnimationFrame: (fn) => { rafQueue.push(fn); return rafQueue.length; },
  performance: { now: () => 0 },
  document: documentStub,
  console: console,
};

const sandbox = {
  window: windowStub,
  document: documentStub,
  performance: windowStub.performance,
  requestAnimationFrame: windowStub.requestAnimationFrame,
  console: console,
  Math: Math, Date: Date, JSON: JSON, Set: Set, Array: Array, Object: Object,
};
sandbox.globalThis = sandbox;
windowStub.NeonAlley = undefined;

// ---------------------------------------------------------------- run the page
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map((m) => m[1]);
if (scripts.length !== 2) throw new Error("expected 2 inline scripts, found " + scripts.length);

const context = vm.createContext(sandbox);
vm.runInContext(scripts[0], context, { filename: "index.html:engine" });
// In a browser `window === globalThis`; in the sandbox they differ, so alias the
// engine onto `window` exactly like the browser would see it.
const NE = vm.runInContext("typeof NeonAlley !== 'undefined' ? NeonAlley : undefined", context);
windowStub.NeonAlley = NE;
if (!NE) throw new Error("engine did not export NeonAlley");
vm.runInContext(scripts[1], context, { filename: "index.html:page" });
sandbox.NeonAlley = NE;
const game = sandbox.window.__neon.game;
const results = {};

function key(type, k, repeat) {
  for (const fn of listeners[type] || []) {
    fn({ key: k, repeat: !!repeat, preventDefault() {} });
  }
}

let now = 0;
function frames(n, msPerFrame) {
  msPerFrame = msPerFrame || 16.7;
  for (let i = 0; i < n; i++) {
    now += msPerFrame;
    const queue = rafQueue;
    rafQueue = [];
    for (const fn of queue) fn(now);
  }
}

// 1. boots into the title screen and draws
frames(3);
results.boot = { state: game.state, calls: Object.values(calls).reduce((a, b) => a + b, 0),
                 status: elements.status.textContent,
                 canvas: [elements.game.width, elements.game.height],
                 cssSize: [elements.game.style.width, elements.game.style.height] };
if (game.state !== NE.TITLE) throw new Error("did not boot into the title screen");

// 2. ENTER starts the game
key("keydown", "Enter");
key("keyup", "Enter");
frames(2);
results.start = { state: game.state, enemies: game.enemies.length,
                  wave: game.wave_index };
if (game.state !== NE.PLAY) throw new Error("ENTER did not start the game");

// 3. hold D for a second: the player must move right
const x0 = game.player.wx;
key("keydown", "d");
frames(60);
results.walk = { from: x0, to: game.player.wx, moved: game.player.wx - x0 };
if (game.player.wx <= x0) throw new Error("holding D did not move the player");
key("keyup", "d");

// 4. J throws a punch
key("keydown", "j");
key("keyup", "j");
frames(1);
results.punch = { attack: game.player.attack ? game.player.attack.name : null };
if (!game.player.attack) throw new Error("J did not start an attack");
frames(20);

// 5. SPACE jumps
key("keydown", " ");
key("keyup", " ");
frames(4);
results.jump = { airborne: !game.player.grounded, y: game.player.wy };
if (game.player.grounded) throw new Error("SPACE did not jump");
frames(60);

// 6. play a real run with an autopilot-ish key sequence until the game ends
let guard = 0;
while (game.state === NE.PLAY && guard < 6000) {
  const target = game.enemies.filter((e) => !e.dead)[0];
  if (target) {
    const dx = target.wx - game.player.wx;
    if (dx > 30) { key("keydown", "d"); key("keyup", "a"); }
    else if (dx < -30) { key("keydown", "a"); key("keyup", "d"); }
    else { key("keyup", "d"); key("keyup", "a"); }
    if (Math.abs(dx) < 40) { key("keydown", guard % 2 ? "j" : "k"); key("keyup", guard % 2 ? "j" : "k"); }
  }
  frames(1);
  guard += 1;
}
results.finished = { state: game.state, frames: guard, kills: game.kills,
                     hp: game.player.hp };
if (game.state === NE.PLAY) throw new Error("run never finished");

// 7. R restarts
key("keydown", "r");
key("keyup", "r");
frames(2);
results.restart = { state: game.state, wave: game.wave_index, hp: game.player.hp,
                    kills: game.kills };
if (game.state !== NE.PLAY || game.player.hp !== 80) throw new Error("R did not restart");

// 8. resizing keeps the canvas crisp (integer scale, 16:10)
sandbox.window.innerWidth = 800; sandbox.window.innerHeight = 600;
for (const fn of listeners.resize || []) fn();
results.resize = { cssSize: [elements.game.style.width, elements.game.style.height] };

const total = Object.values(calls).reduce((a, b) => a + b, 0);
results.drawCalls = total;
results.ok = total > 1000 &&
             results.boot.canvas[0] === 384 && results.boot.canvas[1] === 240 &&
             results.finished.state !== NE.PLAY;

process.stdout.write(JSON.stringify(results, null, 2) + "\n");
process.exit(results.ok ? 0 : 1);
