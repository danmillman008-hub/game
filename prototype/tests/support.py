"""Shared test setup: headless video, repository import path, small helpers."""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")


def pygame_display(width=384, height=240):
    """Initialise pygame headless and return the module (display is required by convert())."""
    import pygame
    pygame.init()
    if pygame.display.get_surface() is None:
        pygame.display.set_mode((width, height))
    return pygame


def place(fighter, x: int, z: int) -> None:
    fighter.body.x = x << 16
    fighter.body.z = z << 16
    fighter.body.vx = 0
    fighter.body.vz = 0
    fighter.body.y = 0
    fighter.body.vy = 0
    fighter.grounded = True


def dummy_enemy(game, index=0):
    e = game.enemies[index]
    e.spawn_delay = 0
    return e
