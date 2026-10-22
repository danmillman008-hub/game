"""Tunable constants for Neon Alley.

Three categories, kept visually separate because they have different epistemic status:

  [ROM]       values taken from the reconstructed engine (components/sor_engine)
  [INTEG]     how this game wires verified components together (integration choices)
  [PROTO]     new rules invented for this prototype (combat, AI, health, flow)

Only [ROM] values are original-game behaviour. [INTEG] and [PROTO] are this game's.
"""
from __future__ import annotations

# ---------------------------------------------------------------- rendering
VIRTUAL_W, VIRTUAL_H = 384, 240   # authentic ROM-scale canvas, integer-upscaled by main.py
FPS = 60
SIM_DT = 1.0 / FPS
TITLE = "NEON ALLEY"

# ---------------------------------------------------------------- arena
# World X is the horizontal axis; Z is screen depth [PROTO layout].
ARENA_X_MIN, ARENA_X_MAX = 48, 1360
ARENA_Z_MIN, ARENA_Z_MAX = 20, 170   # sy = Z/2 + 128 -> ground plane 138..213
WORLD_W = ARENA_X_MAX + 48   # 1408
# Camera keeps the player at this screen offset; project() adds the engine's +$80 bias.
CAM_ANCHOR_X = 128          # sx = X - cam + 128  => player sits at sx 256
CAM_X_MIN, CAM_X_MAX = 0, WORLD_W - VIRTUAL_W + 128
SY_OFFSET = 0               # [INTEG] optional viewport shift, applied after project()
CHAR_SCALE = 0.62           # fighter art is authored at ~96 px and scaled to the 42 px ROM body box

# ---------------------------------------------------------------- [ROM] physics
# Verified constants live in components/sor_engine; these are the *sources* used.
JUMP_VY = -0x78000          # -7.5 px/tick — the measured launch used by D10
JUMP_VY_STRONG = -0x88000   # -8.5 px/tick — second measured launch
PLAYER_SPRITE_W = 7         # body-box table index (+$02) — 14 px wide, y -42..0
PLAYER_SPRITE_H = 7
ENEMY_SPRITE_W = 2          # 10 px wide, y -50..0
ENEMY_SPRITE_H = 6

# ---------------------------------------------------------------- [PROTO] player
PLAYER_HP = 80              # mirrors the ROM's $50 max, chosen for familiarity
PLAYER_WALK_VX = 0x24000        # 2.25 px/tick
PLAYER_DEPTH_VZ = 0x18000       # 1.5 px/tick
PLAYER_ACCEL = 0x0C000          # ground acceleration toward target vx
PLAYER_MAX_HP = PLAYER_HP
PLAYER_HURT_IFRAMES = 26
PLAYER_KNOCKBACK = 0x28000

# ---------------------------------------------------------------- [PROTO] combat
# Attack phases are frame counts at the fixed 60 Hz simulation rate.
ATTACKS = {
    "punch": dict(startup=3, active=3, recovery=7, damage=7, reach=34, depth=22,
                  height=(-58, 6), knockback=0x18000, hitstun=11, hitstop=3,
                  lunge=0x08000, cooldown=5),
    "kick":  dict(startup=8, active=5, recovery=16, damage=13, reach=46, depth=26,
                  height=(-70, 10), knockback=0x30000, hitstun=18, hitstop=5,
                  lunge=0x04000, cooldown=9),
}
# [PROTO] The enemy swings are *armoured* through startup and active frames: a hit
# still deals damage, but does not cancel the swing. Without this, any single fast
# poke stun-locks the whole encounter (measured: autopilot took 0 damage).
ENEMY_ATTACK = dict(startup=16, active=4, recovery=22, damage=8, reach=38, depth=24,
                    height=(-58, 6), knockback=0x20000, hitstun=14, hitstop=3,
                    lunge=0x0C000, cooldown=0, armour=True)
ENEMY_IMMUNITY_AFTER_HIT = 0
ENEMY_HP = 30
ENEMY_HP_WAVE2 = 42

# ---------------------------------------------------------------- [PROTO] AI
ENEMY_WALK_VX = 0x1A000          # 1.625 px/tick
ENEMY_DEPTH_VZ = 0x14000
ENEMY_ACCEL = 0x08000
ENEMY_ENGAGE_X = 30              # stop distance in X
ENEMY_ENGAGE_Z = 6
ENEMY_ATTACK_COOLDOWN = (36, 64)  # deterministic per-enemy value inside this range
ENEMY_LANE_OFFSET = (-10, 0, 10)  # each enemy prefers a slightly different lane
ENEMY_KNOCKBACK_DECAY = 0x5000

# ---------------------------------------------------------------- [PROTO] flow
WAVES = (
    (dict(kind="thug",  hp=ENEMY_HP,       color="amber",  x=980,  z=60),
     dict(kind="thug",  hp=ENEMY_HP,       color="violet", x=1120, z=110)),
    (dict(kind="brute", hp=ENEMY_HP_WAVE2, color="lime",   x=1050, z=85),),
)
WAVE_DELAY_FRAMES = 70           # breather between waves
VICTORY_HOLD = 45
DEATH_ANIM_FRAMES = 46

# ---------------------------------------------------------------- colours
COL_BG_TOP = (10, 8, 22)
COL_BG_BOTTOM = (36, 18, 58)
COL_NEON_PINK = (255, 45, 149)
COL_NEON_CYAN = (34, 230, 255)
COL_NEON_AMBER = (255, 176, 32)
COL_NEON_LIME = (157, 255, 74)
COL_NEON_VIOLET = (186, 108, 255)
COL_WHITE = (240, 246, 255)
COL_INK = (10, 8, 18)
COL_FLOOR = (28, 24, 44)
COL_FLOOR_LINE = (60, 52, 92)

PALETTE = {
    "player": dict(main=(232, 244, 255), accent=COL_NEON_CYAN, glow=COL_NEON_CYAN,
                   skin=(255, 214, 186), dark=(38, 52, 78)),
    "amber":  dict(main=(255, 190, 96), accent=(255, 120, 40), glow=COL_NEON_AMBER,
                   skin=(214, 160, 120), dark=(72, 40, 24)),
    "violet": dict(main=(196, 150, 255), accent=(140, 80, 255), glow=COL_NEON_VIOLET,
                   skin=(206, 170, 200), dark=(48, 30, 72)),
    "lime":   dict(main=(190, 255, 140), accent=(90, 220, 90), glow=COL_NEON_LIME,
                   skin=(200, 220, 170), dark=(30, 60, 36)),
}
