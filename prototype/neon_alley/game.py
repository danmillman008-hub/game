"""Neon Alley simulation.

Deterministic, frame-locked, integer-exact. No random numbers are used: the same
command sequence always produces the same result, which is what makes the
scripted encounter test in `prototype/tests/` meaningful.

Division of labour:
  * verified engine behaviour  -> prototype.neon_alley.adapter -> components/sor_engine
  * integration wiring         -> this module (documented inline as [INTEG])
  * new gameplay rules         -> this module / entities.py (marked [PROTO])
"""
from __future__ import annotations

import math
from dataclasses import dataclass

from . import adapter
from .config import (ARENA_X_MAX, ARENA_X_MIN, ARENA_Z_MAX, ARENA_Z_MIN, ATTACKS,
                     CAM_ANCHOR_X, CAM_X_MAX, CAM_X_MIN, DEATH_ANIM_FRAMES,
                     ENEMY_ACCEL, ENEMY_ATTACK, ENEMY_ATTACK_COOLDOWN,
                     ENEMY_DEPTH_VZ, ENEMY_ENGAGE_X, ENEMY_ENGAGE_Z,
                     ENEMY_LANE_OFFSET, ENEMY_WALK_VX, JUMP_VY, PLAYER_ACCEL,
                     PLAYER_DEPTH_VZ, PLAYER_HP, PLAYER_HURT_IFRAMES,
                     PLAYER_WALK_VX, VICTORY_HOLD, WAVE_DELAY_FRAMES, WAVES)
from .entities import Enemy, Player, reset_ids


@dataclass
class Command:
    """One frame of intent, already normalised (keyboard, script or autopilot)."""
    move_x: int = 0          # -1, 0, +1
    move_z: int = 0          # -1, 0, +1
    jump: bool = False       # pressed edge
    punch: bool = False      # pressed edge
    kick: bool = False       # pressed edge


def _approach(value: int, target: int, step: int) -> int:
    if value < target:
        return min(target, value + step)
    if value > target:
        return max(target, value - step)
    return value


def _clamp(v: int, lo: int, hi: int) -> int:
    return lo if v < lo else hi if v > hi else v


class Game:
    """The whole game state. One `update()` call == one 1/60 s frame."""

    TITLE, PLAY, VICTORY, DEFEAT = "title", "play", "victory", "defeat"

    def __init__(self) -> None:
        self.reset()

    # ------------------------------------------------------------------
    def reset(self) -> None:
        reset_ids()
        self.state = Game.TITLE
        self.frame = 0
        self.player = Player(300, 84, PLAYER_HP)
        self.enemies: list[Enemy] = []
        self.wave_index = -1
        self.wave_timer = 0
        self.kills = 0
        self.total_enemies = sum(len(w) for w in WAVES)
        self.attack_token_owner: int | None = None
        self.cam_x = self._camera_target()
        self.shake = 0
        self.hitstop = 0
        self.effects: list[dict] = []
        self.outcome_timer = 0
        adapter.reset_stats()

    def start(self) -> None:
        """Leave the title screen and spawn the first wave."""
        self.state = Game.PLAY
        self._spawn_wave(0)

    # ------------------------------------------------------------------
    @property
    def alive_enemies(self) -> list[Enemy]:
        return [e for e in self.enemies if not e.dead]

    def _spawn_wave(self, index: int) -> None:
        self.wave_index = index
        for i, spec in enumerate(WAVES[index]):
            self.enemies.append(Enemy(
                spec["kind"], spec["color"], spec["x"], spec["z"], spec["hp"],
                lane_offset=ENEMY_LANE_OFFSET[i % len(ENEMY_LANE_OFFSET)],
                cooldown=ENEMY_ATTACK_COOLDOWN[0] + i * 11,
            ))

    def _camera_target(self) -> int:
        return _clamp(self.player.wx - CAM_ANCHOR_X, CAM_X_MIN, CAM_X_MAX)

    # ------------------------------------------------------------------
    def update(self, cmd: Command | None = None) -> None:
        cmd = cmd or Command()
        if self.state != Game.PLAY:
            self.frame += 1
            return

        self.frame += 1

        # [PROTO] hit-stop freezes gameplay frames, not effects/UI.
        if self.hitstop > 0:
            self.hitstop -= 1
            self._update_effects()
            return

        self._update_player(cmd)
        for enemy in self.enemies:
            self._update_enemy(enemy)
        self._resolve_body_collisions()
        self._cleanup_dead()
        self._update_waves()
        self._update_effects()
        self._update_camera()

        if self.shake > 0:
            self.shake -= 1
        for e in (self.player, *self.enemies):
            e.tick_timers()

        if self.player.dead:
            self.outcome_timer += 1
            if self.outcome_timer > DEATH_ANIM_FRAMES:
                self.state = Game.DEFEAT
        elif self.wave_index == len(WAVES) - 1 and not self.enemies:
            self.outcome_timer += 1
            if self.outcome_timer > VICTORY_HOLD:
                self.state = Game.VICTORY

    # ------------------------------------------------------------ player
    def _update_player(self, cmd: Command) -> None:
        p = self.player
        if p.dead:
            self._death_physics(p)
            return
        if p.hitstun > 0:
            p.apply_knockback()
            adapter.integrate(p.body)
            self._clamp_actor(p)
            return

        if p.attack is not None:
            self._advance_attack(p, is_player=True)
            adapter.integrate(p.body)
            self._clamp_actor(p)
            return

        if p.grounded:
            # [PROTO] ground locomotion: the ROM's per-frame walk speeds live in
            # animation data that Stage 2 did not recover, so this is new tuning.
            target_vx = cmd.move_x * PLAYER_WALK_VX
            p.body.vx = _approach(p.body.vx, target_vx, PLAYER_ACCEL)
            p.body.vz = cmd.move_z * PLAYER_DEPTH_VZ
            if cmd.move_x:
                p.facing = cmd.move_x
            if cmd.jump:
                p.body.vy = JUMP_VY
                p.grounded = False
                p.air_mode = "directional" if cmd.move_x else "neutral"
            if p.body.vx or cmd.move_x:
                pass
        else:
            # [ROM] the airborne chain, in the verified order:
            # gravity -> air control -> terminal clamp -> integration
            p.body.buttons = (adapter.BTN_RIGHT if cmd.move_x > 0
                              else adapter.BTN_LEFT if cmd.move_x < 0 else 0)
            adapter.gravity(p.body, p.air_mode)
            adapter.air_control(p.body)
            adapter.clamp_terminal(p.body)
            p.facing = adapter.facing_from_state(p.body)

        if p.grounded and (cmd.punch or cmd.kick) and p.can_attack():
            p.start_attack("kick" if cmd.kick else "punch")

        # [ROM] integrate() returns False when the engine's freeze predicate
        # ($00442C: (state & $FC) == $14 with bit7 of +$59) suppressed the step.
        # A suppressed step must not be interpreted as landing.
        if adapter.integrate(p.body) and not p.grounded and p.body.vy > 0 and p.body.y >= 0:
            p.body.y = 0
            p.body.vy = 0
            p.grounded = True
            self._spawn_effect("dust", p.wx, p.wz, 0)
        self._clamp_actor(p)

    def _death_physics(self, f: "Player | Enemy") -> None:
        if not f.grounded:
            adapter.gravity(f.body, "directional")
            adapter.clamp_terminal(f.body)
        if adapter.integrate(f.body) and not f.grounded and f.body.y >= 0:
            f.body.y = 0
            f.body.vy = 0
            f.grounded = True
        f.death_timer += 1
        self._clamp_actor(f)

    # ------------------------------------------------------------ enemies
    def _update_enemy(self, e: Enemy) -> None:
        if e.dead:
            self._death_physics(e)
            return
        if e.spawn_delay > 0:
            e.spawn_delay -= 1
            return
        if e.hitstun > 0:
            e.apply_knockback()
            adapter.integrate(e.body)
            self._clamp_actor(e)
            return

        if e.attack is not None:
            self._advance_attack(e, is_player=False)
            adapter.integrate(e.body)
            self._clamp_actor(e)
            return

        p = self.player
        dx = p.wx - e.wx
        dz = (p.wz + e.lane_offset) - e.wz

        target_x = p.wx - math.copysign(ENEMY_ENGAGE_X, dx if dx else 1)
        target_x = int(target_x)
        target_z = _clamp(p.wz + e.lane_offset, ARENA_Z_MIN, ARENA_Z_MAX)

        desired_vx = 0
        if abs(dx) > ENEMY_ENGAGE_X - 4:
            desired_vx = ENEMY_WALK_VX if target_x > e.wx else -ENEMY_WALK_VX
        e.body.vx = _approach(e.body.vx, desired_vx, ENEMY_ACCEL)

        desired_vz = 0
        if abs(dz) > 3:
            desired_vz = ENEMY_DEPTH_VZ if target_z > e.wz else -ENEMY_DEPTH_VZ
        e.body.vz = _approach(e.body.vz, desired_vz, ENEMY_ACCEL)

        if dx:
            e.facing = 1 if dx > 0 else -1

        if e.cooldown > 0:
            e.cooldown -= 1

        in_range = abs(dx) <= ENEMY_ENGAGE_X + 6 and abs(dz) <= ENEMY_ENGAGE_Z + 4
        if in_range and e.cooldown == 0 and self.attack_token_owner is None and not p.dead:
            e.start_attack("enemy", facing=1 if dx >= 0 else -1)
            e.ai = "attack"
            self.attack_token_owner = e.id

        adapter.integrate(e.body)
        self._clamp_actor(e)

    # ------------------------------------------------------------ combat
    def _advance_attack(self, f: "Player | Enemy", is_player: bool) -> None:
        atk = f.attack
        assert atk is not None
        phase = atk.phase()

        # [PROTO] lunge: a small forward drift during startup/active, so a
        # whiffed swing still closes the last few pixels.
        if phase in ("startup", "active"):
            f.body.vx = atk.defn.get("lunge", 0) * f.facing
        elif phase == "recovery":
            f.body.vx = 0
        if phase == "active":
            box = f.attack_box()
            if is_player:
                for enemy in self.enemies:
                    if enemy.dead or enemy.id in atk.hit_ids:
                        continue
                    if adapter.overlap(box, enemy.body_box()):
                        atk.hit_ids.add(enemy.id)
                        dealt = enemy.take_hit(atk.defn["damage"], f.wx, atk.defn)
                        if dealt:
                            self._on_hit(f, enemy, dealt, atk.name)
            else:
                p = self.player
                if p.id not in atk.hit_ids:
                    defn = dict(atk.defn, iframes=PLAYER_HURT_IFRAMES)
                    if adapter.overlap(box, p.body_box()):
                        atk.hit_ids.add(p.id)
                        dealt = p.take_hit(defn["damage"], f.wx, defn)
                        if dealt:
                            self._on_hit(f, p, dealt, "enemy")
        atk.advance()
        if atk.phase() == "done":
            f.attack = None
            f.attack_cooldown = atk.defn.get("cooldown", 0)
            if not is_player:
                f.ai = "approach"
                f.cooldown = ENEMY_ATTACK_COOLDOWN[1]
                if self.attack_token_owner == f.id:
                    self.attack_token_owner = None

    def _on_hit(self, attacker, victim, damage: int, kind: str) -> None:
        self.hitstop = max(self.hitstop, attacker.attack.defn.get("hitstop", 0) if attacker.attack else 0)
        self.shake = max(self.shake, 6 if kind == "kick" else 4)
        x, z, y = victim.wx, victim.wz, victim.wy - 28
        self._spawn_effect("spark", x, z, y, color="cyan" if kind != "enemy" else "red")
        self._spawn_effect("ring", x, z, y, color="cyan" if kind != "enemy" else "red")
        self._spawn_effect("popup", x, z, y, value=damage)
        if victim.dead and victim is not self.player:
            self.kills += 1
            self._spawn_effect("ko", x, z, y, color="amber")
            if self.attack_token_owner == victim.id:
                self.attack_token_owner = None

    # ------------------------------------------------------------ physics glue
    def _clamp_actor(self, f) -> None:
        """[PROTO] Arena bounds. The ROM uses per-round bands; this arena has one."""
        f.body.x = adapter.s32(_clamp(f.wx, ARENA_X_MIN, ARENA_X_MAX) << 16 |
                               (f.body.x & 0xFFFF))
        f.body.z = adapter.s32(_clamp(f.wz, ARENA_Z_MIN, ARENA_Z_MAX) << 16 |
                               (f.body.z & 0xFFFF))
        if f.grounded:
            f.body.y = 0
            f.body.vy = 0

    def _resolve_body_collisions(self) -> None:
        """[INTEG] Push actors apart using the verified AABB predicate and the
        ROM-derived body boxes. Pairing and resolution weights are prototype rules."""
        actors = [self.player, *self.enemies]
        for i in range(len(actors)):
            for j in range(i + 1, len(actors)):
                a, b = actors[i], actors[j]
                if a.dead or b.dead:
                    continue
                ba, bb = a.body_box(), b.body_box()
                if not adapter.overlap(ba, bb):
                    continue
                ox = min(ba.x2, bb.x2) - max(ba.x1, bb.x1)
                oz = min(ba.z2, bb.z2) - max(ba.z1, bb.z1)
                if ox <= 0 or oz <= 0:
                    continue
                if a is self.player:
                    wa, wb = 0.25, 0.75
                elif b is self.player:
                    wa, wb = 0.75, 0.25
                else:
                    wa = wb = 0.5
                if ox <= oz:
                    ax = int(ox * wa) << 16
                    bx = int(ox * wb) << 16
                    if a.wx < b.wx:
                        a.body.x = adapter.s32(a.body.x - ax)
                        b.body.x = adapter.s32(b.body.x + bx)
                    else:
                        a.body.x = adapter.s32(a.body.x + ax)
                        b.body.x = adapter.s32(b.body.x - bx)
                else:
                    az = int(oz * wa) << 16
                    bz = int(oz * wb) << 16
                    if a.wz < b.wz:
                        a.body.z = adapter.s32(a.body.z - az)
                        b.body.z = adapter.s32(b.body.z + bz)
                    else:
                        a.body.z = adapter.s32(a.body.z + az)
                        b.body.z = adapter.s32(b.body.z - bz)
                self._clamp_actor(a)
                self._clamp_actor(b)

    # ------------------------------------------------------------ flow
    def _cleanup_dead(self) -> None:
        keep = []
        for e in self.enemies:
            if e.dead and e.death_timer > DEATH_ANIM_FRAMES:
                continue
            keep.append(e)
        self.enemies = keep

    def _update_waves(self) -> None:
        if self.player.dead:
            return
        if self.enemies:
            return
        if self.wave_index < 0:
            return
        if self.wave_index + 1 < len(WAVES):
            self.wave_timer += 1
            if self.wave_timer >= WAVE_DELAY_FRAMES:
                self.wave_timer = 0
                self._spawn_wave(self.wave_index + 1)
        else:
            self.wave_timer += 1

    def _update_camera(self) -> None:
        target = self._camera_target()
        self.cam_x += _clamp(target - self.cam_x, -12, 12)

    # ------------------------------------------------------------ effects
    def _spawn_effect(self, kind: str, x: int, z: int, y: int,
                      color: str = "cyan", value: int = 0) -> None:
        ttl = {"spark": 12, "ring": 14, "popup": 38, "dust": 16, "ko": 26}[kind]
        self.effects.append(dict(kind=kind, x=x, z=z, y=y, t=0, ttl=ttl,
                                 color=color, value=value))

    def _update_effects(self) -> None:
        live = []
        for e in self.effects:
            e["t"] += 1
            if e["t"] < e["ttl"]:
                live.append(e)
        self.effects = live

    # ------------------------------------------------------------ queries
    def snapshot(self) -> dict:
        return {
            "state": self.state,
            "frame": self.frame,
            "wave": self.wave_index,
            "kills": self.kills,
            "player": {
                "hp": self.player.hp, "x": self.player.wx, "z": self.player.wz,
                "y": self.player.wy, "grounded": self.player.grounded,
                "facing": self.player.facing, "dead": self.player.dead,
            },
            "enemies": [
                {"id": e.id, "hp": e.hp, "x": e.wx, "z": e.wz, "dead": e.dead}
                for e in self.enemies
            ],
        }
