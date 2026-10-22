"""Neon Alley — entry point.

    python -m prototype.neon_alley            (from the repository root)
    python prototype/neon_alley/main.py       (also works)

Flags:
    --windowed WxH   initial window size (default 1280x720)
    --fullscreen     start fullscreen (Esc leaves)
    --autopilot      let the demo pilot play (useful to watch the encounter)
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# Allow `python prototype/neon_alley/main.py` as well as `-m prototype.neon_alley`.
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    __package__ = "prototype.neon_alley"

from .config import FPS, SIM_DT, VIRTUAL_H, VIRTUAL_W  # noqa: E402

import pygame.locals as _L  # noqa: E402

K_A, K_D, K_J, K_K, K_R, K_S, K_W = _L.K_a, _L.K_d, _L.K_j, _L.K_k, _L.K_r, _L.K_s, _L.K_w
K_SPACE, K_RETURN, K_ESCAPE, K_F11, K_b = _L.K_SPACE, _L.K_RETURN, _L.K_ESCAPE, _L.K_F11, _L.K_b


def _poll_command(game, keys, prev_keys):
    """Map the keyboard to one frame of intent (edge-triggered actions)."""
    from .game import Command
    move_x = (1 if keys[K_D] else 0) - (1 if keys[K_A] else 0)
    move_z = (1 if keys[K_S] else 0) - (1 if keys[K_W] else 0)

    def pressed(key):
        return keys[key] and not prev_keys[key]

    return Command(
        move_x=move_x,
        move_z=move_z,
        jump=pressed(K_SPACE),
        punch=pressed(K_J),
        kick=pressed(K_K),
    )


def run(windowed=(1280, 720), fullscreen=False, autopilot=False,
        max_frames: int = 0, shot: str | None = None) -> int:
    """Run the game loop.

    `max_frames` and `shot` exist for the headless smoke test / screenshots; the
    normal launch passes neither and simply runs until the window is closed.
    """
    import pygame

    pygame.init()
    try:
        pygame.mixer.init()
    except Exception:
        pass

    flags = pygame.FULLSCREEN if fullscreen else pygame.RESIZABLE
    screen = pygame.display.set_mode(windowed, flags)
    pygame.display.set_caption("Neon Alley")
    clock = pygame.time.Clock()

    from .autopilot import AutoPilot
    from .game import Game, Command
    from .render import Renderer

    game = Game()
    renderer = Renderer()
    pilot = AutoPilot() if autopilot else None
    prev = pygame.key.get_pressed()
    accumulator = 0.0
    running = True
    t = 0.0
    frames = 0

    while running:
        dt = clock.tick(FPS) / 1000.0
        dt = min(dt, 0.1)
        t += dt
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_F11:
                    pygame.display.toggle_fullscreen()
                elif event.key == K_r:
                    game.reset()
                    game.start()
                elif event.key in (K_RETURN, K_SPACE) and game.state == game.TITLE:
                    game.start()
                elif event.key == K_b:
                    pass

        accumulator += dt
        steps = 0
        while accumulator >= SIM_DT and steps < 5:
            if game.state == game.TITLE:
                game.update(Command())
            elif pilot is not None:
                game.update(pilot.command(game))
            else:
                game.update(_poll_command(game, keys, prev))
            accumulator -= SIM_DT
            steps += 1
        prev = keys

        surf = renderer.draw(game, t)
        w, h = screen.get_size()
        scale = min(w / VIRTUAL_W, h / VIRTUAL_H)
        target = (max(1, int(VIRTUAL_W * scale)), max(1, int(VIRTUAL_H * scale)))
        scaled = pygame.transform.smoothscale(surf, target) if target != (VIRTUAL_W, VIRTUAL_H) else surf
        screen.fill((0, 0, 0))
        screen.blit(scaled, ((w - target[0]) // 2, (h - target[1]) // 2))
        pygame.display.flip()

        frames += 1
        if shot and frames == 1:
            import pygame as _pg
            _pg.image.save(surf, shot)
        if max_frames and frames >= max_frames:
            running = False

    pygame.quit()
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Neon Alley")
    ap.add_argument("--windowed", default="1280x720")
    ap.add_argument("--fullscreen", action="store_true")
    ap.add_argument("--autopilot", action="store_true")
    ap.add_argument("--frames", type=int, default=0, help="stop after N frames (testing)")
    ap.add_argument("--shot", default=None, help="save frame 1 of the virtual canvas to PNG")
    args = ap.parse_args(argv)
    try:
        w, h = (int(v) for v in args.windowed.lower().split("x"))
    except Exception:
        w, h = 1280, 720
    return run((w, h), args.fullscreen, args.autopilot, args.frames, args.shot)


if __name__ == "__main__":
    raise SystemExit(main())
