// Stage 1 — reconstruction. A beat-'em-up played on a depth (x, z) plane in the
// manner the original uses: movement along x is horizontal, movement along z
// changes the character's depth on screen, and only characters at similar depth
// can hit each other.
//
// What is reconstructed here is the *mechanics*; what is recovered from the
// original is the *art* and the *stage geometry*. The README separates the two.

import { Assets, loadAssets } from './assets.js';

const W = 320, H = 224;
const canvas = document.getElementById('screen');
const ctx = canvas.getContext('2d', { alpha: false });
ctx.imageSmoothingEnabled = false;

// ---------------------------------------------------------------- stage geometry
// Derived from the capture: the walkable floor occupies roughly the lower third
// of the picture, and the camera follows the player horizontally.
const STAGE = {
  xMin: 8, xMax: 900,          // stage coordinates (world pixels)
  zMin: 0, zMax: 100,          // depth, 0 = furthest, 100 = nearest
  floorTop: 168,               // screen y of zMin at camera centre
  floorBottom: 216,            // screen y of zMax
  cameraLead: 96,              // camera keeps the player this far from the edge
};

const zToY = (z) => STAGE.floorTop + (z / 100) * (STAGE.floorBottom - STAGE.floorTop);
const zToScale = (z) => 0.86 + 0.18 * (z / 100);

// ---------------------------------------------------------------- input
const keys = new Set();
addEventListener('keydown', (e) => {
  const k = e.key.length === 1 ? e.key.toLowerCase() : e.key;
  keys.add(k);
  if ([' ', 'ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.key)) e.preventDefault();
  if (k === 'r') reset();
});
addEventListener('keyup', (e) => keys.delete(e.key.length === 1 ? e.key.toLowerCase() : e.key));
canvas.addEventListener('pointerdown', () => canvas.focus());

const held = (...names) => names.some((n) => keys.has(n));
const input = {
  get left() { return held('ArrowLeft', 'a'); },
  get right() { return held('ArrowRight', 'd'); },
  get up() { return held('ArrowUp', 'w'); },
  get down() { return held('ArrowDown', 's'); },
  get attack() { return held('j'); },
  get jump() { return held('k'); },
};

// ---------------------------------------------------------------- determinism
// The original is deterministic for a given input sequence, so this must be too.
// Every "random" decision (enemy attack timing) draws from a seeded generator,
// reset with the game, which makes a run reproducible frame for frame.
let rngState = 0x2f6e2b1;
function rng() {
  // xorshift32
  rngState ^= rngState << 13; rngState >>>= 0;
  rngState ^= rngState >>> 17;
  rngState ^= rngState << 5; rngState >>>= 0;
  return rngState / 0x100000000;
}

// ---------------------------------------------------------------- actors
let player, enemies, camera, effects, timerFrames, score, spawnQueue, state;

function makeActor(kind, x, z, facing) {
  return {
    kind, x, z, facing,
    hp: kind === 'player' ? 48 : 16,
    vx: 0, vz: 0, y: 0, vy: 0, airborne: false,
    state: 'idle', stateFrame: 0, animFrame: 0, animTimer: 0,
    hitstun: 0, downTimer: 0, invuln: 0, hasHit: false,
  };
}

function reset() {
  player = makeActor('player', 90, 62, 1);
  enemies = [];
  effects = [];
  camera = { x: 0 };
  timerFrames = 40 * 60;      // 40 game-units, one per second
  score = 0;
  state = 'play';
  rngState = 0x2f6e2b1;      // same starting point every run
  // Waves: the original sends thugs in from the right in pairs; two waves plus a
  // third guard near the stage mid-point, matching the pacing observed in capture.
  spawnQueue = [
    { at: 40, x: 420, z: 60, name: 'thug' },
    { at: 40, x: 470, z: 40, name: 'thug' },
    { at: 340, x: 660, z: 75, name: 'thug' },
    { at: 340, x: 700, z: 45, name: 'thug' },
    { at: 700, x: 840, z: 60, name: 'thug' },
  ];
  frame = 0;
}

// ---------------------------------------------------------------- combat
const ATTACK = {
  startup: 5, active: 4, recovery: 9, reach: 26, zTolerance: 18, damage: 4,
};

function hurt(a, amount, fromFacing) {
  if (a.invuln > 0 || a.state === 'down') return;
  a.hp -= amount;
  a.hitstun = 12;
  a.vx = fromFacing * 1.6;
  if (a.hp <= 0) {
    a.state = 'down';
    a.downTimer = 46;
    if (a.kind !== 'player') score += 500;
  } else {
    a.state = 'hurt';
  }
}

function startAttack(a) {
  if (a.airborne || a.hitstun || a.state === 'attack' || a.state === 'down') return;
  a.state = 'attack';
  a.stateFrame = 0;
  a.hasHit = false;
}

// Keep an actor inside the stage. Every state that changes x must go through
// this: knockback used to bypass the clamp and push actors off the stage.
function clampActor(a) {
  a.x = Math.max(STAGE.xMin, Math.min(STAGE.xMax, a.x));
  a.z = Math.max(STAGE.zMin, Math.min(STAGE.zMax, a.z));
}

function updateActor(a, dt) {
  const f = dt;   // one update per frame

  if (a.hitstun > 0) a.hitstun -= f;
  if (a.invuln > 0) a.invuln -= f;

  if (a.state === 'down') {
    a.downTimer -= f;
    a.x += a.vx * f;
    a.vx *= 0.9;
    if (a.downTimer <= 0) {
      if (a.kind === 'player') { a.hp = 48; a.state = 'idle'; a.invuln = 40; }
      else { a.dead = true; }
    }
    clampActor(a);
    return;
  }

  if (a.state === 'hurt') {
    a.x += a.vx * f;
    a.vx *= 0.82;
    if (a.hitstun <= 0) a.state = 'idle';
    clampActor(a);
    return;
  }

  if (a.state === 'attack') {
    a.stateFrame += f;
    if (a.stateFrame < ATTACK.startup) return;
    if (a.stateFrame < ATTACK.startup + ATTACK.active) {
      if (!a.hasHit) resolveHit(a);
      return;
    }
    if (a.stateFrame >= ATTACK.startup + ATTACK.active + ATTACK.recovery) {
      a.state = 'idle';
      a.stateFrame = 0;
    }
    return;
  }

  // ---- grounded movement
  let dx = 0, dz = 0;
  if (a.kind === 'player') {
    if (input.left) dx -= 1;
    if (input.right) dx += 1;
    if (input.up) dz -= 1;
    if (input.down) dz += 1;
    if (input.attack) startAttack(a);
    if (input.jump && !a.airborne) { a.vy = -4.2; a.airborne = true; }
  }

  if (dx || dz) {
    const len = Math.hypot(dx, dz) || 1;
    const speed = a.airborne ? 1.1 : 1.9;
    a.x += (dx / len) * speed * f;
    if (!a.airborne) a.z += (dz / len) * speed * 60 * f / 1;  // depth units per px
    if (dx) a.facing = dx > 0 ? 1 : -1;
    a.state = 'walk';
  } else if (!a.airborne && a.state === 'walk') {
    a.state = 'idle';
  }

  // ---- jump arc
  if (a.airborne) {
    a.y += a.vy * f;
    a.vy += 0.42 * f;
    if (a.y >= 0) { a.y = 0; a.vy = 0; a.airborne = false; }
    a.state = 'jump';
  }

  // ---- bounds
  clampActor(a);

  // ---- animation
  a.animTimer += f;
  const rate = a.state === 'walk' ? 7 : 14;
  if (a.animTimer >= rate) { a.animTimer = 0; a.animFrame = (a.animFrame + 1) % 4; }
}

function resolveHit(a) {
  const targets = a.kind === 'player' ? enemies : [player];
  for (const t of targets) {
    if (t.dead || t.hp <= 0) continue;
    const dst = Math.abs(t.x - a.x);
    const dzh = Math.abs(t.z - a.z);
    if (dst > ATTACK.reach || dzh > ATTACK.zTolerance) continue;
    if ((t.x - a.x) * a.facing < 0) continue;         // must be in front
    a.hasHit = true;
    hurt(t, ATTACK.damage, a.facing);
    effects.push({ x: t.x, z: t.z, y: t.y, life: 8, kind: 'impact' });
    break;
  }
}

// ---------------------------------------------------------------- enemy AI
function updateEnemy(e, dt) {
  if (e.dead) return;
  updateActor(e, dt);
  if (e.state === 'down' || e.state === 'hurt' || e.state === 'attack') return;

  const dx = player.x - e.x;
  const dz = player.z - e.z;
  const adx = Math.abs(dx);

  // Close in, then strike. Depth is corrected before distance, which is what the
  // original's enemies visibly do: they line up with you, then attack.
  if (Math.abs(dz) > 4) {
    e.z += Math.sign(dz) * 0.55 * dt;
    e.state = 'walk';
  } else if (adx > ATTACK.reach - 6) {
    e.x += Math.sign(dx) * 0.8 * dt;
    e.facing = Math.sign(dx) || 1;
    e.state = 'walk';
  } else {
    e.facing = Math.sign(dx) || 1;
    if (rng() < 0.02) startAttack(e);
  }
}

// ---------------------------------------------------------------- camera
function updateCamera() {
  const target = Math.max(0, Math.min(STAGE.xMax - W / 2, player.x - STAGE.cameraLead));
  camera.x += (target - camera.x) * 0.18;
}

// ---------------------------------------------------------------- rendering
function drawActor(a) {
  const sx = Math.round(a.x - camera.x);
  const sy = Math.round(zToY(a.z) - a.y);
  const scale = zToScale(a.z);

  if (a.state === 'down') {
    ctx.save();
    ctx.translate(sx, sy);
    ctx.rotate(a.facing * Math.PI / 2);
    drawBody(a, 0, 0, scale);
    ctx.restore();
    return;
  }
  ctx.save();
  ctx.translate(sx, sy);
  if (a.facing < 0) ctx.scale(-1, 1);
  drawBody(a, 0, 0, scale);
  ctx.restore();

  if (a.state === 'attack' && a.stateFrame >= ATTACK.startup &&
      a.stateFrame < ATTACK.startup + ATTACK.active) {
    // attack arc: shows the active hitbox window
    ctx.fillStyle = 'rgba(255, 240, 180, 0.55)';
    ctx.fillRect(sx + (a.facing > 0 ? 8 : -26), sy - 30, 18, 12);
  }
}

const SPRITES = { player: ['axel_stand', 'axel_walk', 'axel_walk2'], enemy: ['thug_stand'] };

function drawBody(a, ox, oy, scale) {
  const list = SPRITES[a.kind === 'player' ? 'player' : 'enemy'];
  const idx = a.state === 'walk' ? (a.animFrame % list.length) : 0;
  const img = Assets.images[list[idx]];
  if (!img) {
    ctx.fillStyle = a.kind === 'player' ? '#4d7dc4' : '#c47a3e';
    ctx.fillRect(ox - 8, oy - 34 * scale, 16 * scale, 34 * scale);
    return;
  }
  const dw = img.width * scale;
  const dh = img.height * scale;
  ctx.drawImage(img, ox - dw / 2, oy - dh, dw, dh);
}

function drawHUD() {
  // Layout taken from the original's own HUD (measured on a captured frame):
  // a 1px yellow frame at the top of the screen, "1UP" + score at the left above
  // a red health bar, lives to its right, then the timer block in the middle.
  ctx.fillStyle = '#202020';           // measured HUD background colour
  ctx.fillRect(0, 0, W, 26);

  ctx.fillStyle = '#eeee20';           // measured HUD frame colour
  ctx.fillRect(0, 0, W, 1);
  ctx.fillRect(0, 25, W, 1);

  ctx.font = '8px monospace';
  ctx.textBaseline = 'top';
  ctx.fillStyle = '#e8e8e0';
  ctx.fillText('1UP-' + String(score).padStart(6, '0'), 6, 4);

  const pct = Math.max(0, player.hp / 48);
  ctx.fillStyle = '#502020';
  ctx.fillRect(6, 14, 96, 8);
  ctx.fillStyle = '#c83028';
  ctx.fillRect(6, 14, 96 * pct, 8);

  ctx.fillStyle = '#e8e8e0';
  ctx.fillText('x3', 104, 14);

  const secs = Math.max(0, Math.ceil(timerFrames / 60));
  ctx.fillText('TIME', 148, 0);
  ctx.fillStyle = secs <= 10 ? '#e06040' : '#e8e8e0';
  ctx.fillText(String(secs).padStart(2, '0'), 156, 11);
}

function render() {
  ctx.fillStyle = '#000';
  ctx.fillRect(0, 0, W, H);

  const plate = Assets.images.plate;
  if (plate) {
    // The plate covers the stage width up to where it was captured; beyond that
    // the same art repeats, which is stated as an approximation in the README.
    const span = plate.width;
    let x = -Math.round(camera.x % span);
    while (x < W) {
      ctx.drawImage(plate, 0, 0, plate.width, plate.height, Math.round(x), 0, plate.width, plate.height);
      x += span;
    }
  } else {
    ctx.fillStyle = '#232a33';
    ctx.fillRect(0, 0, W, H);
  }

  // actors sorted back-to-front
  const all = [player, ...enemies].filter((a) => a && !a.dead);
  all.sort((a, b) => a.z - b.z);
  for (const a of all) drawActor(a);

  for (const fx of effects) {
    ctx.fillStyle = `rgba(255, 230, 150, ${fx.life / 8})`;
    const sx = Math.round(fx.x - camera.x);
    ctx.fillRect(sx - 3, Math.round(zToY(fx.z) - fx.y) - 20, 6, 6);
  }

  drawHUD();
}

// ---------------------------------------------------------------- loop
let frame = 0;
let last = 0;
let acc = 0;
const STEP = 1000 / 60;

function tick(now) {
  if (!last) last = now;
  acc += now - last;
  last = now;
  while (acc >= STEP) {
    update();
    acc -= STEP;
  }
  render();
  requestAnimationFrame(tick);
}

function update() {
  frame++;
  if (state !== 'play') return;

  if (timerFrames > 0) timerFrames--;
  else if (state === 'play') state = 'timeout';

  updateActor(player, 1);

  for (const s of spawnQueue) {
    if (!s.done && frame >= s.at) {
      enemies.push(makeActor('enemy', s.x, s.z, -1));
      s.done = true;
    }
  }
  for (const e of enemies) updateEnemy(e, 1);
  enemies = enemies.filter((e) => !e.dead);

  for (const fx of effects) fx.life--;
  effects = effects.filter((fx) => fx.life > 0);

  updateCamera();

  if (player.hp <= 0 && player.state !== 'down') {
    player.state = 'down';
    player.downTimer = 60;
  }
}

// ---------------------------------------------------------------- boot
reset();
loadAssets().then((r) => {
  const el = document.getElementById('hint');
  if (el) {
    el.textContent = r.missing.length
      ? 'Missing art: ' + r.missing.join(', ')
      : 'Click the canvas, then use the keys.';
  }
  requestAnimationFrame(tick);
});

// expose a small surface for the headless tests
window.STAGE1 = {
  get state() { return state; },
  get player() { return player; },
  get enemies() { return enemies; },
  get camera() { return camera; },
  get score() { return score; },
  get frame() { return frame; },
  step(n = 1) { for (let i = 0; i < n; i++) update(); },
  press(k) { keys.add(k); },
  release(k) { keys.delete(k); },
  reset,
  assetsReady: () => Object.values(Assets.images).every(Boolean),
  // render the current state immediately (used by the headless renderer)
  renderFrame: () => render(),
  get images() { return Assets.images; },
};
