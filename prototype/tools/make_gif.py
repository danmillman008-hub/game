"""Render the recorded encounter to an animated GIF (visual evidence + preview).

    python -m prototype.tools.make_gif

Two files are written into prototype/media/:
  neon_alley_full.gif       the whole 875-frame recorded run, sampled
  neon_alley_highlight.gif  a short loop: approach, punch, kick, knockout
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pygame  # noqa: E402
from PIL import Image  # noqa: E402

from prototype.neon_alley.config import VIRTUAL_H, VIRTUAL_W  # noqa: E402
from prototype.neon_alley.game import Command, Game  # noqa: E402
from prototype.neon_alley.render import Renderer  # noqa: E402

MEDIA = ROOT / "prototype" / "media"
FIELDS = ("move_x", "move_z", "jump", "punch", "kick")


def load_commands():
    data = json.loads((ROOT / "prototype" / "data" / "scripted_run.json").read_text())
    return [Command(**{f: e[f] for f in FIELDS}) for e in data["commands"]]


def render_frames(commands, scale=1.5, every=2, start=0, stop=None):
    """Replay the recording and yield upscaled RGB frames."""
    size = (int(VIRTUAL_W * scale), int(VIRTUAL_H * scale))
    game = Game()
    game.start()
    renderer = Renderer()
    frames = []
    for i, cmd in enumerate(commands):
        if stop is not None and i >= stop:
            break
        if game.state != Game.PLAY:
            break
        game.update(cmd)
        if i < start or (i - start) % every:
            continue
        surf = renderer.draw(game, i / 60.0)
        if size != (VIRTUAL_W, VIRTUAL_H):
            surf = pygame.transform.smoothscale(surf, size)
        raw = pygame.image.tobytes(surf, "RGB")
        frames.append(Image.frombytes("RGB", size, raw))
    return frames


def write_gif(frames, path: Path, fps=20, colours=96) -> Path:
    if not frames:
        raise SystemExit("no frames rendered")
    quantized = [f.quantize(colors=colours, method=Image.Quantize.MEDIANCUT,
                            dither=Image.Dither.NONE) for f in frames]
    quantized[0].save(
        path, save_all=True, append_images=quantized[1:],
        duration=int(1000 / fps), loop=0, optimize=True, disposal=2,
    )
    print(f"wrote {path.relative_to(ROOT)}  ({len(frames)} frames, "
          f"{path.stat().st_size / 1024:.0f} KiB)")
    return path


def main() -> int:
    pygame.init()
    pygame.display.set_mode((VIRTUAL_W, VIRTUAL_H))
    MEDIA.mkdir(parents=True, exist_ok=True)
    commands = load_commands()

    full = render_frames(commands, scale=1.0, every=3)
    write_gif(full, MEDIA / "neon_alley_full.gif", fps=20, colours=32)

    # a compact loop around the first two knockouts
    hi = render_frames(commands, scale=1.5, every=2, start=170, stop=400)
    write_gif(hi, MEDIA / "neon_alley_highlight.gif", fps=20, colours=48)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
