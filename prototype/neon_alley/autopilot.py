"""[PROTO] Deterministic pilot used by the scripted-encounter test and the demo mode.

It reads only public game state and emits `Command`s, so it exercises exactly the
same code path a keyboard player would use.
"""
from __future__ import annotations

from .game import Command


class AutoPilot:
    def __init__(self) -> None:
        self.attack_cooldown = 0
        self.jump_cooldown = 0
        self.heavy = False

    def command(self, game) -> Command:
        p = game.player
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        if self.jump_cooldown > 0:
            self.jump_cooldown -= 1

        targets = [e for e in game.enemies if not e.dead and e.spawn_delay == 0]
        if not targets or p.dead or p.attack is not None or p.hitstun > 0:
            return Command()

        target = min(targets, key=lambda e: (abs(e.wx - p.wx) + abs(e.wz - p.wz) * 2, e.id))
        dx = target.wx - p.wx
        dz = target.wz - p.wz

        move_x = 0
        if abs(dx) > 34:
            move_x = 1 if dx > 0 else -1
        elif abs(dx) < 20:
            move_x = -1 if dx > 0 else 1      # too close: step back to attack range

        move_z = 0
        if abs(dz) > 5:
            move_z = 1 if dz > 0 else -1

        # Hop over an incoming swing: this is also what puts the airborne
        # gravity / air-control chain on the recorded path.
        jump = False
        threatened = any(
            e.attack is not None and e.attack.phase() == "startup"
            and abs(e.wx - p.wx) <= 46 and abs(e.wz - p.wz) <= 14
            for e in targets)
        if threatened and p.grounded and self.jump_cooldown == 0:
            jump = True
            self.jump_cooldown = 34

        punch = kick = False
        in_range = abs(dx) <= 40 and abs(dz) <= 14
        if in_range and p.grounded and self.attack_cooldown == 0:
            self.heavy = not self.heavy
            kick = self.heavy
            punch = not self.heavy
            self.attack_cooldown = 6

        return Command(move_x=move_x, move_z=move_z, jump=jump, punch=punch, kick=kick)
