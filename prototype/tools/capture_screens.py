"""Render the screenshot set used as visual evidence.

    python -m prototype.tools.capture_screens

Writes PNGs into prototype/screenshots/ (virtual canvas upscaled 3x, nearest
neighbour, so the pixel grid stays visible).
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pygame  # noqa: E402

from prototype.neon_alley.config import VIRTUAL_H, VIRTUAL_W  # noqa: E402
from prototype.neon_alley.game import Command, Game  # noqa: E402
from prototype.neon_alley.render import Renderer  # noqa: E402

OUT = ROOT / "prototype" / "screenshots"
SCALE = 3


def save(renderer, game, name: str, t: float) -> None:
    surf = renderer.draw(game, t)
    up = pygame.transform.scale(surf, (VIRTUAL_W * SCALE, VIRTUAL_H * SCALE))
    path = OUT / name
    pygame.image.save(up, path)
    print(f"wrote {path.relative_to(ROOT)} ({path.stat().st_size} bytes)")


def started() -> Game:
    game = Game()
    game.start()
    return game


def main() -> int:
    pygame.init()
    pygame.display.set_mode((VIRTUAL_W, VIRTUAL_H))
    renderer = Renderer()
    OUT.mkdir(parents=True, exist_ok=True)

    # 1. title / controls
    save(renderer, Game(), "01_title.png", 0.35)

    # 2. street, both lanes, wave 1
    game = started()
    for _ in range(20):
        game.update(Command(move_x=1))
    save(renderer, game, "02_street.png", 0.6)

    # 3. jump: body off the ground, shadow stays on the plane
    game = started()
    game.update(Command(jump=True, move_x=1))
    for _ in range(7):
        game.update(Command(move_x=1))
    save(renderer, game, "03_jump.png", 0.8)

    # 4. punch connecting (spark + damage number + hit-stop)
    game = started()
    p = game.player
    e = game.enemies[0]
    p.body.x, p.body.z = 300 << 16, 90 << 16
    e.body.x, e.body.z = 330 << 16, 90 << 16
    e.spawn_delay = 0
    game.enemies[1].spawn_delay = 999
    for i in range(8):
        game.update(Command(punch=True) if i == 0 else Command())
    save(renderer, game, "04_punch_hit.png", 1.0)

    # 5. kick
    game = started()
    p = game.player
    e = game.enemies[0]
    p.body.x, p.body.z = 300 << 16, 90 << 16
    e.body.x, e.body.z = 340 << 16, 90 << 16
    e.spawn_delay = 0
    game.enemies[1].spawn_delay = 999
    for i in range(12):
        game.update(Command(kick=True) if i == 0 else Command())
    save(renderer, game, "05_kick.png", 1.1)

    # 6. wave 2: the brute walking in on the player
    game = started()
    for e in game.enemies:
        e.hp, e.dead, e.death_timer = 0, True, 999
    game.kills = 2
    for _ in range(90):
        game.update(Command())
    game.player.body.x = 860 << 16
    game.player.body.z = 80 << 16
    for _ in range(60):
        game.update(Command())
    save(renderer, game, "06_wave2.png", 1.3)

    # 7. victory card: clear both waves, then let the victory hold expire
    game = started()
    for _ in range(600):
        for e in game.enemies:
            if not e.dead:
                e.hp, e.dead, e.death_timer = 0, True, 999
                game.kills += 1
        if game.state == Game.VICTORY:
            break
        game.update(Command())
    assert game.state == Game.VICTORY, game.state
    save(renderer, game, "07_victory.png", 1.5)

    # 8. defeat card: stand still and take the beating
    game = started()
    for _ in range(4000):
        if game.state != Game.PLAY:
            break
        game.update(Command())
    save(renderer, game, "08_defeat.png", 1.7)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
