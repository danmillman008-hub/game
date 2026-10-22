// Behavioural tests for the Stage-1 reconstruction.
//
// These drive the shipped module's own update path (STAGE1.step), so they test
// the mechanics that ship rather than a copy of them.
import { installDom } from './harness.mjs';

installDom();
await import('../js/game.js');
const G = globalThis.STAGE1;

let pass = 0;
let fail = 0;
const results = [];
function check(name, cond, detail = '') {
  if (cond) { pass++; results.push(`ok   ${name}`); }
  else { fail++; results.push(`FAIL ${name} ${detail}`); }
}

const ALL = ['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'j', 'k'];
function fresh() {
  G.reset();
  for (const k of ALL) G.release(k);
}

// --- movement
fresh();
const x0 = G.player.x;
const z0 = G.player.z;
G.press('ArrowRight');
G.step(30);
G.release('ArrowRight');
check('right moves +x', G.player.x > x0, `x ${x0} -> ${G.player.x}`);
check('right keeps depth', Math.abs(G.player.z - z0) < 0.001);
check('facing follows movement', G.player.facing === 1);

fresh();
const x1 = G.player.x;
G.press('ArrowLeft');
G.step(30);
G.release('ArrowLeft');
check('left moves -x', G.player.x < x1, `x ${x1} -> ${G.player.x}`);
check('facing left', G.player.facing === -1);

// --- depth
fresh();
const z1 = G.player.z;
G.press('ArrowDown');
G.step(20);
G.release('ArrowDown');
check('down increases depth', G.player.z > z1, `z ${z1} -> ${G.player.z}`);

fresh();
const z2 = G.player.z;
G.press('ArrowUp');
G.step(20);
G.release('ArrowUp');
check('up decreases depth', G.player.z < z2, `z ${z2} -> ${G.player.z}`);

// --- bounds
fresh();
G.press('ArrowRight');
G.step(2000);
G.release('ArrowRight');
check('x is clamped to the stage', G.player.x <= 900, `x=${G.player.x}`);

fresh();
G.press('ArrowDown');
G.step(600);
G.release('ArrowDown');
check('depth is clamped', G.player.z <= 100.001, `z=${G.player.z}`);

// --- jump
fresh();
G.press('k');
G.step(1);
G.release('k');
check('jump leaves the ground', G.player.airborne && G.player.y < 0, `y=${G.player.y}`);
let up = 0;
for (let i = 0; i < 200; i++) {
  G.step(1);
  up = Math.min(up, G.player.y);
  if (!G.player.airborne) break;
}
check('jump apex is bounded', up > -80 && up < 0, `apex=${up}`);
check('jump lands', !G.player.airborne && G.player.y === 0);

// --- attack and damage
fresh();
G.step(45);
check('first wave spawns', G.enemies.length >= 1, `${G.enemies.length} enemies`);
const e1 = G.enemies[0];
e1.x = G.player.x + 18;
e1.z = G.player.z;
const hp1 = e1.hp;
G.press('j');
G.step(1);
G.release('j');
G.step(12);
check('attack damages an adjacent foe', e1.hp < hp1, `hp ${hp1} -> ${e1.hp}`);

// --- attack misses at the wrong depth
fresh();
G.step(45);
const e2 = G.enemies[0];
e2.x = G.player.x + 18;
e2.z = G.player.z + 60;
const hp2 = e2.hp;
G.press('j');
G.step(1);
G.release('j');
G.step(12);
check('attack misses at a different depth', e2.hp === hp2, `hp ${hp2} -> ${e2.hp}`);

// --- attack does not reach behind
fresh();
G.step(45);
const e3 = G.enemies[0];
e3.x = G.player.x - 18;
e3.z = G.player.z;
G.player.facing = 1;
const hp3 = e3.hp;
G.press('j');
G.step(1);
G.release('j');
G.step(12);
check('attack does not reach behind', e3.hp === hp3, `hp ${hp3} -> ${e3.hp}`);

// --- score on defeat
fresh();
G.step(45);
const e4 = G.enemies[0];
e4.hp = 1;
e4.x = G.player.x + 16;
e4.z = G.player.z;
const s0 = G.score;
G.press('j');
G.step(1);
G.release('j');
G.step(80);
check('defeating a foe scores', G.score > s0, `score ${s0} -> ${G.score}`);

// --- camera
fresh();
const c0 = G.camera.x;
G.press('ArrowRight');
G.step(400);
G.release('ArrowRight');
check('camera follows the player', G.camera.x > c0, `cam ${c0} -> ${G.camera.x}`);
check('camera stays inside the stage', G.camera.x <= 900 - 160, `cam=${G.camera.x}`);

// --- timer
fresh();
const before = G.frame;
G.step(120);
check('the loop advances frames', G.frame === before + 120);

// --- determinism
fresh();
G.press('ArrowRight');
G.step(60);
G.release('ArrowRight');
const a = JSON.stringify([G.player.x, G.player.z, G.camera.x]);
fresh();
G.press('ArrowRight');
G.step(60);
G.release('ArrowRight');
const b = JSON.stringify([G.player.x, G.player.z, G.camera.x]);
check('same input gives the same state', a === b, `${a} vs ${b}`);

// --- enemies approach the player
fresh();
G.step(45);
const en = G.enemies[0];
en.x = G.player.x + 120;
en.z = G.player.z + 40;
const d0 = Math.hypot(en.x - G.player.x, en.z - G.player.z);
G.step(90);
const d1 = Math.hypot(en.x - G.player.x, en.z - G.player.z);
check('enemies close the distance', d1 < d0, `dist ${d0.toFixed(1)} -> ${d1.toFixed(1)}`);

// --- enemy damages the player
fresh();
G.step(45);
const atk = G.enemies[0];
atk.x = G.player.x + 12;
atk.z = G.player.z;
atk.facing = -1;
const php = G.player.hp;
let hurtDone = false;
for (let i = 0; i < 600 && !hurtDone; i++) {
  G.step(1);
  if (G.player.hp < php) hurtDone = true;
}
check('an enemy can damage the player', hurtDone, `hp ${php} -> ${G.player.hp}`);

console.log(results.join('\n'));
console.log(`\n${pass} passed, ${fail} failed`);
if (fail) process.exitCode = 1;
