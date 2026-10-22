"""All drawing for Neon Alley — original procedural art, no external assets.

The only engine coupling is `adapter.project()`: every character's screen position
comes from the verified projection/cull routine, not from a second formula.
"""
from __future__ import annotations

import math

import pygame

from . import adapter
from .config import (ARENA_X_MAX, ARENA_X_MIN, ARENA_Z_MAX, ARENA_Z_MIN,
                     COL_BG_BOTTOM, COL_BG_TOP, COL_FLOOR, COL_FLOOR_LINE, COL_INK,
                     COL_NEON_AMBER, COL_NEON_CYAN, COL_NEON_LIME, COL_NEON_PINK,
                     COL_NEON_VIOLET, COL_WHITE, PALETTE, TITLE, VIRTUAL_H, VIRTUAL_W,
                     CHAR_SCALE, WAVES)


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _font(size: int) -> pygame.font.Font:
    return pygame.font.Font(None, size)


class Renderer:
    def __init__(self) -> None:
        pygame.font.init()
        self.f_big = _font(44)
        self.f_mid = _font(20)
        self.f_small = _font(14)
        self.f_tiny = _font(11)
        self.bg = self._build_background()
        self.far = self._build_far()
        self.scanlines = self._build_scanlines()
        self.vignette = self._build_vignette()

    # ---------------------------------------------------------------- static art
    def _build_background(self) -> pygame.Surface:
        """Static street: sky, sidewalk, floor and the depth-lane markings."""
        surf = pygame.Surface((VIRTUAL_W, VIRTUAL_H)).convert()
        for y in range(120):
            surf.fill(_lerp(COL_BG_TOP, COL_BG_BOTTOM, y / 120.0), (0, y, VIRTUAL_W, 1))

        pygame.draw.rect(surf, (22, 19, 36), (0, 120, VIRTUAL_W, 14))
        pygame.draw.rect(surf, COL_FLOOR, (0, 134, VIRTUAL_W, VIRTUAL_H - 134))

        # Depth-lane markings. `sy = (Z >> 1) + $80` is exactly what project()
        # computes for a ground point (Y = 0, cam_y = 0) — same formula, no new one.
        for z in range(ARENA_Z_MIN, ARENA_Z_MAX + 1, 24):
            sy = (z >> 1) + 0x80
            alpha = 30 + int(30 * (1 - z / ARENA_Z_MAX))
            line = pygame.Surface((VIRTUAL_W, 1), pygame.SRCALPHA)
            line.fill((110, 210, 255, alpha))
            surf.blit(line, (0, sy))

        for x in range(-160, VIRTUAL_W + 160, 48):
            pygame.draw.line(surf, (33, 29, 50), (x, 134), (x - 46, VIRTUAL_H), 1)

        for (px, py, pw) in ((30, 196, 62), (236, 214, 84), (146, 166, 46)):
            puddle = pygame.Surface((pw, 8), pygame.SRCALPHA)
            pygame.draw.ellipse(puddle, (70, 120, 160, 36), (0, 0, pw, 8))
            surf.blit(puddle, (px, py))
            pygame.draw.line(surf, (60, 150, 190), (px + 8, py + 4), (px + pw - 10, py + 4), 1)

        pygame.draw.line(surf, (58, 52, 88), (0, 134), (VIRTUAL_W, 134), 2)
        return surf

    def _build_far(self) -> pygame.Surface:
        """Scrollable skyline tile: buildings with lit windows and neon signs."""
        W, H = 512, 134
        surf = pygame.Surface((W, H), pygame.SRCALPHA).convert_alpha()

        # haze towards the horizon
        for y in range(84, 134):
            a = int(150 * (y - 84) / 50)
            pygame.draw.line(surf, (58, 34, 92, a), (0, y), (W, y))

        # far towers
        x, i = 0, 0
        while x < W:
            w = 20 + (i * 37) % 28
            h = 26 + (i * 53) % 52
            top = 122 - h
            pygame.draw.rect(surf, (30, 25, 56), (x, top, w, h + 12))
            pygame.draw.line(surf, (86, 70, 138), (x, top), (x + w, top), 1)
            for wy in range(top + 6, 120, 7):
                for wx in range(x + 4, x + w - 4, 6):
                    if (wx * 7 + wy * 13 + i) % 6 == 0:
                        pygame.draw.rect(surf, (70, 80, 132), (wx, wy, 2, 3))
            x += w + 8
            i += 1

        # near buildings
        for (bx, bw, bh, col) in ((0, 106, 46, (20, 16, 38)), (118, 94, 62, (15, 12, 30)),
                                  (224, 118, 40, (23, 18, 44)), (354, 148, 70, (14, 11, 28))):
            top = 122 - bh
            pygame.draw.rect(surf, col, (bx, top, bw, bh + 12))
            pygame.draw.line(surf, (104, 82, 160), (bx, top), (bx + bw, top), 2)
            for wy in range(top + 7, 116, 8):
                for wx in range(bx + 5, bx + bw - 5, 7):
                    lit = (wx * 5 + wy * 11) % 9
                    if lit < 3:
                        c = (240, 186, 96) if lit == 0 else (104, 156, 220)
                        pygame.draw.rect(surf, c, (wx, wy, 2, 3))

        self._sign(surf, "OPEN", 18, 88, COL_NEON_PINK)
        self._sign(surf, "24H", 186, 74, COL_NEON_CYAN)
        self._sign(surf, "BAR", 374, 92, COL_NEON_AMBER)
        return surf

    def _sign(self, surf, text, x, y, color):
        glow = _font(15).render(text, True, color)
        g2 = pygame.transform.smoothscale(glow, (glow.get_width() + 6, glow.get_height() + 6))
        g2.set_alpha(80)
        surf.blit(g2, (x - 3, y - 3))
        surf.blit(glow, (x, y))

    def _build_scanlines(self) -> pygame.Surface:
        s = pygame.Surface((VIRTUAL_W, VIRTUAL_H), pygame.SRCALPHA)
        for y in range(0, VIRTUAL_H, 3):
            pygame.draw.line(s, (0, 0, 0, 22), (0, y), (VIRTUAL_W, y))
        return s

    def _build_vignette(self) -> pygame.Surface:
        s = pygame.Surface((VIRTUAL_W, VIRTUAL_H), pygame.SRCALPHA)
        for i in range(90):
            a = int(70 * (i / 90) ** 2)
            pygame.draw.rect(s, (0, 0, 0, a), (i, i, VIRTUAL_W - 2 * i, VIRTUAL_H - 2 * i), 1)
        return s

    # ---------------------------------------------------------------- helpers
    def _ground_sy(self, actor, cam_x: int) -> int:
        """Projection of the same spot with Y=0 — the verified routine again."""
        tmp = adapter.Actor(type_id=actor.type_id, x=actor.x, z=actor.z, y=0)
        _, sy, _ = adapter.project(tmp, cam_x, 0)
        return sy

    def _screen(self, actor, cam_x: int):
        sx, sy, culled = adapter.project(actor, cam_x, 0)
        return sx, sy, culled

    # ---------------------------------------------------------------- frame
    def draw(self, game, t: float) -> pygame.Surface:
        surf = pygame.Surface((VIRTUAL_W, VIRTUAL_H)).convert()
        cam = game.cam_x
        surf.blit(self.bg, (0, 0))
        off = -int(cam * 0.45) % self.far.get_width()
        surf.blit(self.far, (off - self.far.get_width(), 0))
        surf.blit(self.far, (off, 0))

        if game.state == game.TITLE:
            self._draw_title(surf, game, t)
            surf.blit(self.scanlines, (0, 0))
            surf.blit(self.vignette, (0, 0))
            return surf

        self._draw_shadows(surf, game, cam)
        self._draw_actors(surf, game, cam, t)
        self._draw_effects(surf, game, cam)
        self._draw_hud(surf, game)

        if game.shake:
            off = (int(math.sin(game.frame * 3.1) * game.shake),
                   int(math.cos(game.frame * 2.3) * game.shake))
            surf = pygame.transform.rotate(surf, 0)
            base = pygame.Surface((VIRTUAL_W, VIRTUAL_H)).convert()
            base.blit(surf, off)
            surf = base

        surf.blit(self.scanlines, (0, 0))
        surf.blit(self.vignette, (0, 0))

        if game.state == game.VICTORY:
            self._draw_end(surf, "AREA CLEARED", COL_NEON_CYAN, game, t)
        elif game.state == game.DEFEAT:
            self._draw_end(surf, "YOU ARE DOWN", COL_NEON_PINK, game, t)
        return surf

    # ---------------------------------------------------------------- title / end
    def _draw_title(self, surf, game, t):
        overlay = pygame.Surface((VIRTUAL_W, VIRTUAL_H), pygame.SRCALPHA)
        overlay.fill((6, 4, 14, 190))
        surf.blit(overlay, (0, 0))
        pulse = 0.5 + 0.5 * math.sin(t * 2.4)
        col = _lerp(COL_NEON_PINK, COL_NEON_CYAN, pulse * 0.6)
        title = self.f_big.render(TITLE, True, col)
        glow = self.f_big.render(TITLE, True, (col[0] // 3, col[1] // 3, col[2] // 3))
        for dx, dy in ((-4, 0), (4, 0), (0, -4), (0, 4)):
            surf.blit(glow, (VIRTUAL_W // 2 - title.get_width() // 2 + dx, 34 + dy))
        surf.blit(title, (VIRTUAL_W // 2 - title.get_width() // 2, 34))
        sub = self.f_small.render("a two-lane brawl under the signs", True, (170, 190, 220))
        surf.blit(sub, (VIRTUAL_W // 2 - sub.get_width() // 2, 68))

        lines = [
            ("A / D   move", COL_WHITE),
            ("W / S   step through depth", COL_WHITE),
            ("SPACE   jump  (air control while holding A/D)", COL_WHITE),
            ("J       punch", COL_NEON_CYAN),
            ("K       kick", COL_NEON_PINK),
            ("R       restart anytime", (150, 160, 190)),
        ]
        y = 88
        for text, c in lines:
            s = self.f_small.render(text, True, c)
            surf.blit(s, (VIRTUAL_W // 2 - s.get_width() // 2, y))
            y += 16
        prompt = "PRESS ENTER" if (t * 2) % 2 < 1.3 else ""
        p = self.f_mid.render(prompt, True, COL_NEON_AMBER)
        surf.blit(p, (VIRTUAL_W // 2 - p.get_width() // 2, 204))

    def _draw_end(self, surf, text, color, game, t):
        overlay = pygame.Surface((VIRTUAL_W, VIRTUAL_H), pygame.SRCALPHA)
        overlay.fill((4, 3, 10, 170))
        surf.blit(overlay, (0, 0))
        big = self.f_big.render(text, True, color)
        surf.blit(big, (VIRTUAL_W // 2 - big.get_width() // 2, 72))
        stats = self.f_small.render(
            f"knockouts {game.kills}/{game.total_enemies}", True, COL_WHITE)
        surf.blit(stats, (VIRTUAL_W // 2 - stats.get_width() // 2, 122))
        prompt = "PRESS R TO RUN IT AGAIN"
        if (t * 2) % 2 < 1.3:
            p = self.f_mid.render(prompt, True, COL_NEON_AMBER)
            surf.blit(p, (VIRTUAL_W // 2 - p.get_width() // 2, 150))

    # ---------------------------------------------------------------- actors
    def _draw_shadows(self, surf, game, cam):
        for f in [game.player, *game.enemies]:
            if f.dead and f.death_timer > 30:
                continue
            sx, _, culled = self._screen(f.body, cam)
            if culled:
                continue
            sy = self._ground_sy(f.body, cam)
            height = max(0, -f.wy)
            fade = max(0.0, 1.0 - height / 190.0)
            w = int(26 - 8 * (1 - fade))
            h = max(3, int(8 * fade))
            sh = pygame.Surface((w, h), pygame.SRCALPHA)
            pygame.draw.ellipse(sh, (0, 0, 0, int(120 * fade)), (0, 0, w, h))
            surf.blit(sh, (sx - w // 2, sy - h // 2))
            if f.kind == "player":
                # ground marker, so the player is findable while airborne
                pygame.draw.polygon(surf, COL_NEON_CYAN, [
                    (sx - 3, sy + 4), (sx + 3, sy + 4), (sx, sy + 1)])

    def _draw_actors(self, surf, game, cam, t):
        drawables = []
        for f in [game.player, *game.enemies]:
            sx, sy, culled = self._screen(f.body, cam)
            if culled:
                continue
            drawables.append((f.wz, f.wy, f.id, f, sx, sy))
        drawables.sort(key=lambda d: (d[0], d[1], d[2]))
        for _, _, _, f, sx, sy in drawables:
            self._draw_fighter(surf, f, sx, sy, t)

    def _pose(self, f, t):
        if f.dead:
            return "down"
        if f.attack is not None:
            ph = f.attack.phase()
            if ph == "startup":
                return "wind"
            if ph == "active":
                return "strike_kick" if f.attack.name == "kick" else "strike_punch"
            return "recover"
        if f.hitstun > 0:
            return "hurt"
        if not f.grounded:
            return "jump"
        if abs(f.body.vx) > 0x3000:
            return "walk"
        return "idle"

    def _draw_fighter(self, surf, f, sx, sy, t):
        """Draw at authoring scale into a small surface, then scale the body art
        down to the ROM body-box height (~42 px) before blitting at the feet."""
        self._draw_fighter_raw(surf, f, int(sx), int(sy), t)

    def _draw_fighter_raw(self, surf, f, sx, sy, t):
        """One fighter, authored at final pixel size (44 px tall, feet at sy)."""
        pal = PALETTE[f.palette]
        pose = self._pose(f, t)
        phase = (f.anim_frames * 0.20) % (2 * math.pi)
        facing = f.facing
        flash = f.flash > 0 and (f.flash % 4 < 2)

        body_col = COL_WHITE if flash else pal["main"]
        accent = pal["accent"]
        glow = pal["glow"]
        skin = pal["skin"]
        dark = pal["dark"]
        outline = (8, 6, 14)

        if pose == "down":
            self._draw_down(surf, sx, sy, pal, facing)
            return

        bob = int(math.sin(phase * 0.6) * 1.0) if pose == "idle" else 0
        lean = {"walk": 1, "hurt": -3, "wind": -2,
                "strike_punch": 3, "strike_kick": 2}.get(pose, 0) * facing

        hip_y = sy - 18 + bob
        head_y = sy - 33 + bob
        shoulder_y = hip_y - 11
        if pose == "jump":
            hip_y, head_y, shoulder_y = sy - 22, sy - 37, sy - 33
        if pose == "hurt":
            head_y += 2

        # ---- legs
        if pose == "jump":
            legs = [(sx - 2, hip_y, sx - 6, hip_y + 8), (sx + 2, hip_y, sx + 5, hip_y + 7)]
        elif pose == "walk":
            sw = math.sin(phase) * 5
            legs = [(sx - 2, hip_y, sx - 2 - sw, sy), (sx + 2, hip_y, sx + 2 + sw, sy)]
        elif pose == "strike_kick":
            legs = [(sx - 2, hip_y, sx - 4, sy), (sx + 1, hip_y, sx + 15 * facing, hip_y + 5)]
        elif pose == "hurt":
            legs = [(sx - 2, hip_y, sx - 4, sy), (sx + 2, hip_y, sx + 4, sy)]
        else:
            legs = [(sx - 2, hip_y, sx - 3, sy), (sx + 2, hip_y, sx + 3, sy)]
        for (x1, y1, x2, y2) in legs:
            self._limb(surf, (x1 + lean, y1), (x2, y2), 3, dark, outline)

        # ---- torso
        tw = 6
        pts = [(sx - tw + lean, hip_y + 1), (sx + tw + lean, hip_y + 1),
               (sx + tw - 1 + lean, shoulder_y - 1), (sx - tw + 1 + lean, shoulder_y - 1)]
        pygame.draw.polygon(surf, outline, [(x + (1 if x > sx else -1), y) for x, y in pts])
        pygame.draw.polygon(surf, body_col, pts)
        pygame.draw.polygon(surf, accent, pts, 1)
        pygame.draw.line(surf, accent, (sx - tw + 1 + lean, hip_y),
                         (sx + tw - 1 + lean, hip_y), 1)

        # ---- head
        pygame.draw.circle(surf, outline, (sx + lean, head_y), 6)
        pygame.draw.circle(surf, skin, (sx + lean, head_y), 5)
        pygame.draw.circle(surf, accent, (sx + lean, head_y), 5, 1)
        pygame.draw.line(surf, glow, (sx + lean + 1 * facing, head_y - 1),
                         (sx + lean + 4 * facing, head_y - 1), 1)
        pygame.draw.arc(surf, dark, (sx + lean - 6, head_y - 7, 12, 10), 0.2, 3.0, 2)

        # ---- arms
        if pose == "strike_punch":
            arms = [(sx - 2, shoulder_y, sx - 6 * facing, shoulder_y + 7),
                    (sx + 2, shoulder_y, sx + 15 * facing, shoulder_y + 1)]
        elif pose == "wind":
            arms = [(sx - 2, shoulder_y, sx - 7, shoulder_y + 6),
                    (sx + 1, shoulder_y, sx - 3 * facing, shoulder_y + 3)]
        elif pose == "strike_kick":
            arms = [(sx - 1, shoulder_y, sx - 9, shoulder_y - 2),
                    (sx + 1, shoulder_y, sx + 5, shoulder_y + 6)]
        elif pose == "hurt":
            arms = [(sx - 1, shoulder_y, sx - 8, shoulder_y - 4),
                    (sx + 1, shoulder_y, sx + 8, shoulder_y - 5)]
        elif pose == "jump":
            arms = [(sx - 1, shoulder_y, sx - 9, shoulder_y - 3),
                    (sx + 1, shoulder_y, sx + 8, shoulder_y - 2)]
        else:
            swing = math.sin(phase) * 3 if pose == "walk" else 0
            arms = [(sx - 1, shoulder_y, sx - 5 - swing, shoulder_y + 9),
                    (sx + 1, shoulder_y, sx + 5 + swing, shoulder_y + 9)]
        for (x1, y1, x2, y2) in arms:
            self._limb(surf, (x1 + lean, y1), (x2, y2), 2, skin, outline)

        # ---- attack tells
        if pose == "wind":
            pygame.draw.circle(surf, COL_NEON_AMBER, (sx + 10 * facing, shoulder_y + 2), 2, 1)
        if f.attack is not None and f.attack.phase() == "active":
            tip = 16 if f.attack.name == "kick" else 14
            ty = hip_y + (4 if f.attack.name == "kick" else 1)
            pygame.draw.circle(surf, COL_WHITE, (sx + tip * facing, ty), 3, 1)



    def _limb(self, surf, p1, p2, width, col, rim):
        pygame.draw.line(surf, rim, p1, p2, width + 2)
        pygame.draw.line(surf, col, p1, p2, width)
        pygame.draw.circle(surf, col, (int(p1[0]), int(p1[1])), width // 2)
        pygame.draw.circle(surf, col, (int(p2[0]), int(p2[1])), width // 2)

    def _draw_down(self, surf, sx, sy, pal, facing):
        pygame.draw.line(surf, (8, 6, 14), (sx - 15, sy - 4), (sx + 15, sy - 4), 8)
        pygame.draw.line(surf, pal["dark"], (sx - 15, sy - 4), (sx + 15, sy - 4), 6)
        pygame.draw.circle(surf, pal["skin"], (sx + 15 * facing, sy - 5), 4)
        pygame.draw.line(surf, pal["accent"], (sx - 14, sy - 7), (sx + 12, sy - 7), 1)

    # ---------------------------------------------------------------- effects
    def _draw_effects(self, surf, game, cam):
        for e in game.effects:
            actor = adapter.Actor(type_id=1, x=e["x"] << 16, z=e["z"] << 16, y=e["y"] << 16)
            sx, sy, culled = adapter.project(actor, cam, 0)
            if culled:
                continue
            k = e["t"] / e["ttl"]
            col = {"cyan": COL_NEON_CYAN, "red": (255, 96, 96),
                   "amber": COL_NEON_AMBER}[e["color"]]
            if e["kind"] == "spark":
                n = 7
                for i in range(n):
                    ang = i * (2 * math.pi / n) + 0.4
                    r0 = 2 + 9 * k
                    r1 = r0 + 6 * (1 - k)
                    pygame.draw.line(surf, COL_WHITE,
                                     (sx + math.cos(ang) * r0, sy + math.sin(ang) * r0),
                                     (sx + math.cos(ang) * r1, sy + math.sin(ang) * r1), 2)
            elif e["kind"] == "ring":
                r = int(3 + 17 * k)
                pygame.draw.circle(surf, col, (sx, sy), r, max(1, 3 - int(2 * k)))
            elif e["kind"] == "popup":
                f = pygame.font.Font(None, 13)
                s = f.render(str(e["value"]), True, COL_WHITE)
                s.set_alpha(max(0, 255 - int(255 * k)))
                surf.blit(s, (sx - 4, sy - 14 - int(14 * k)))
            elif e["kind"] == "dust":
                for dx in (-4, 0, 4):
                    pygame.draw.circle(surf, (120, 120, 150),
                                       (sx + dx, sy - int(3 * k)), int(3 * (1 - k)) + 1)
            elif e["kind"] == "ko":
                r = int(5 + 30 * k)
                pygame.draw.circle(surf, COL_NEON_AMBER, (sx, sy), r, max(1, 4 - int(3 * k)))

    # ---------------------------------------------------------------- HUD
    def _draw_hud(self, surf, game):
        # health
        bar_x, bar_y, bar_w, bar_h = 10, 17, 150, 8
        pygame.draw.rect(surf, (12, 12, 22), (bar_x - 3, bar_y - 3, bar_w + 6, bar_h + 6), border_radius=4)
        frac = game.player.hp / game.player.max_hp
        col = COL_NEON_CYAN if frac > 0.35 else (255, 90, 90)
        pygame.draw.rect(surf, (30, 40, 60), (bar_x, bar_y, bar_w, bar_h), border_radius=3)
        pygame.draw.rect(surf, col, (bar_x, bar_y, int(bar_w * frac), bar_h), border_radius=3)
        for i in range(1, 8):
            x = bar_x + bar_w * i // 8
            pygame.draw.line(surf, (10, 12, 20), (x, bar_y), (x, bar_y + bar_h), 1)
        pygame.draw.rect(surf, (180, 220, 255), (bar_x, bar_y, bar_w, bar_h), 1, border_radius=3)
        name = self.f_tiny.render("KAI", True, COL_WHITE)
        surf.blit(name, (bar_x, bar_y - 10))

        # wave / enemies
        label = f"WAVE {min(game.wave_index + 1, len(WAVES))}/{len(WAVES)}"
        s = self.f_small.render(label, True, COL_NEON_AMBER)
        surf.blit(s, (VIRTUAL_W - s.get_width() - 10, 8))
        alive = len([e for e in game.enemies if not e.dead])
        s2 = self.f_tiny.render(f"enemies {alive}   ko {game.kills}/{game.total_enemies}",
                                True, (170, 190, 220))
        surf.blit(s2, (VIRTUAL_W - s2.get_width() - 10, 24))

        # controls strip
        hint = "A/D move   W/S depth   SPACE jump   J punch   K kick   R restart"
        h = self.f_tiny.render(hint, True, (120, 132, 164))
        surf.blit(h, (VIRTUAL_W // 2 - h.get_width() // 2, VIRTUAL_H - 13))
