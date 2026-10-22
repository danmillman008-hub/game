"""Game entities.

A `Fighter` *owns* a `components.sor_engine.Actor` — the verified engine's record —
and keeps every prototype-only field (health, attack, AI) outside it. That keeps the
reconstructed layer untouched and makes the boundary visible in code.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from . import adapter
from .config import (ATTACKS, ENEMY_ATTACK, ENEMY_KNOCKBACK_DECAY, ENEMY_SPRITE_H,
                     ENEMY_SPRITE_W, PLAYER_SPRITE_H, PLAYER_SPRITE_W)

_ID_COUNTER = [0]


def reset_ids() -> None:
    """Per-run id sequence, so two fresh games produce identical snapshots."""
    _ID_COUNTER[0] = 0


def _next_id() -> int:
    _ID_COUNTER[0] += 1
    return _ID_COUNTER[0]


@dataclass
class Attack:
    """[PROTO] A prototype attack instance (frame data, hit tracking)."""
    name: str
    defn: dict
    frame: int = 0
    hit_ids: set[int] = field(default_factory=set)

    @property
    def startup(self) -> int:
        return self.defn["startup"]

    @property
    def active(self) -> int:
        return self.defn["active"]

    @property
    def recovery(self) -> int:
        return self.defn["recovery"]

    @property
    def total(self) -> int:
        return self.startup + self.active + self.recovery

    def phase(self) -> str:
        if self.frame < self.startup:
            return "startup"
        if self.frame < self.startup + self.active:
            return "active"
        if self.frame < self.total:
            return "recovery"
        return "done"

    def advance(self) -> None:
        self.frame += 1


class Fighter:
    """Common state for the player and enemies."""

    def __init__(self, kind: str, *, palette: str, x: int, z: int, hp: int,
                 sprite_w: int, sprite_h: int) -> None:
        self.id = _next_id()
        self.kind = kind
        self.palette = palette
        self.body = adapter.Actor(
            type_id=1,                 # players and enemies share the actor class here
            sprite_w=sprite_w,
            sprite_h=sprite_h,
            x=x << 16, z=z << 16, y=0,
        )
        self.hp = hp
        self.max_hp = hp
        self.facing = 1
        self.grounded = True
        self.attack: Attack | None = None
        self.hitstun = 0
        self.iframes = 0
        self.hitstop = 0
        self.dead = False
        self.death_timer = 0
        self.knockback_vx = 0
        self.anim_frames = 0
        self.flash = 0
        self.attack_cooldown = 0

    # -- geometry ------------------------------------------------------
    @property
    def wx(self) -> int:
        return adapter.hi16(self.body.x)

    @property
    def wz(self) -> int:
        return adapter.hi16(self.body.z)

    @property
    def wy(self) -> int:
        return adapter.hi16(self.body.y)

    def boxes(self):
        return adapter.body_boxes(self.body)

    def body_box(self):
        return self.boxes()[0]

    # -- combat --------------------------------------------------------
    def start_attack(self, name: str, facing: int | None = None) -> Attack:
        self.attack = Attack(name, dict(ATTACKS.get(name, ENEMY_ATTACK)))
        self.body.vx = 0
        self.body.vz = 0
        self.knockback_vx = 0
        if facing:
            self.facing = facing
        return self.attack

    def can_attack(self) -> bool:
        return (self.attack is None and self.attack_cooldown == 0
                and self.hitstun == 0 and not self.dead)

    def attack_box(self):
        """[PROTO] World-space attack rectangle, distinct from body boxes."""
        if self.attack is None:
            return None
        d = self.attack.defn
        reach, depth = d["reach"], d["depth"]
        y1, y2 = d["height"]
        x = self.wx
        x1 = x + 2 if self.facing > 0 else x - reach - 2
        return adapter.Box(
            x1=x1, x2=x1 + reach,
            z1=self.wz - depth // 2, z2=self.wz + depth // 2,
            y1=self.wy + y1, y2=self.wy + y2,
        )

    def take_hit(self, damage: int, source_x: int, defn: dict) -> int:
        """Apply damage. Returns the damage actually dealt (0 if immune)."""
        if self.dead or self.iframes > 0:
            return 0
        dmg = min(damage, self.hp)
        self.hp -= dmg
        self.flash = 6
        direction = 1 if self.wx >= source_x else -1

        # [PROTO] Armour: an attack with `armour` keeps running through its
        # startup/active frames. Damage lands, reaction does not.
        armoured = (self.attack is not None
                    and self.attack.defn.get("armour")
                    and self.attack.phase() in ("startup", "active")
                    and self.hp > 0)
        if armoured:
            self.iframes = defn.get("iframes", 0) // 2
            return dmg

        self.hitstun = defn.get("hitstun", 12)
        self.hitstop = defn.get("hitstop", 0)
        self.iframes = defn.get("iframes", 0)
        self.knockback_vx = defn.get("knockback", 0) * direction
        self.attack = None
        if self.hp <= 0:
            self.dead = True
            self.hp = 0
            self.death_timer = 0
            self.body.vy = -0x20000       # small pop on defeat, then falls
            self.grounded = False
        return dmg

    # -- shared per-frame bits ----------------------------------------
    def tick_timers(self) -> None:
        if self.iframes > 0:
            self.iframes -= 1
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        if self.flash > 0:
            self.flash -= 1
        self.anim_frames += 1

    def apply_knockback(self) -> None:
        if self.hitstun <= 0:
            return
        self.hitstun -= 1
        if self.knockback_vx:
            self.body.vx = self.knockback_vx
            step = ENEMY_KNOCKBACK_DECAY
            if self.knockback_vx > 0:
                self.knockback_vx = max(0, self.knockback_vx - step)
            else:
                self.knockback_vx = min(0, self.knockback_vx + step)


class Player(Fighter):
    def __init__(self, x: int, z: int, hp: int):
        super().__init__("player", palette="player", x=x, z=z, hp=hp,
                         sprite_w=PLAYER_SPRITE_W, sprite_h=PLAYER_SPRITE_H)
        self.air_mode = "neutral"


class Enemy(Fighter):
    def __init__(self, kind: str, palette: str, x: int, z: int, hp: int,
                 lane_offset: int, cooldown: int):
        super().__init__(kind, palette=palette, x=x, z=z, hp=hp,
                         sprite_w=ENEMY_SPRITE_W, sprite_h=ENEMY_SPRITE_H)
        self.lane_offset = lane_offset
        self.cooldown = cooldown
        self.spawn_delay = 18
        self.ai = "approach"
        self.attack_token = False
