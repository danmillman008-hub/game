"""Thin oracle wrappers: each function runs one ORIGINAL ROM routine under the
MC68000 core and returns its observable outputs. No component code is used here.

Requires: unicorn (pip). Import is deferred so spec-only tests can run without it.
"""
from __future__ import annotations

import struct
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

from rom_probe import RomProbe, ACTOR  # noqa: E402

ROM = RomProbe  # alias for readability

# Routines probed
ENTRY_NEUTRAL_GRAVITY = 0x00389A
ENTRY_SOFT_GRAVITY = 0x0038A6
ENTRY_DIRECTIONAL_GRAVITY = 0x0038AE
ENTRY_CLAMP = 0x003886
ENTRY_AIR_CONTROL = 0x0038C0
ENTRY_INTEGRATE = 0x00442C
ENTRY_BOXES = 0x004140
ENTRY_AABB = 0x00450C
ENTRY_PROJECT = 0x00AF46
PROJECT_SURVIVED = 0x00AFCA   # after both stores to +$28/+$2C
PROJECT_CULLED = 0x00B17A
AABB_MISS = 0x004550
AABB_HIT = 0x004554


class Oracle:
    def __init__(self):
        self.vm = RomProbe()
        self.vm.clear_actor(ACTOR)
        self.vm.clear_actor(0x00FFB800)

    # -- helpers ------------------------------------------------------
    def _actor_at(self, base: int) -> int:
        self.vm.clear_actor(base)
        return base

    def _u16(self, base, off): return self.vm.read_u16(base + off)
    def _u32(self, base, off): return self.vm.read_u32(base + off)

    # -- kinematics ---------------------------------------------------
    def gravity(self, kind: str, vy: int) -> int:
        base = self._actor_at(ACTOR)
        self.vm.write_u32(base + 0x24, vy)
        self.vm.set_reg("a0", base)
        entry = {"neutral": ENTRY_NEUTRAL_GRAVITY,
                 "soft": ENTRY_SOFT_GRAVITY,
                 "directional": ENTRY_DIRECTIONAL_GRAVITY}[kind]
        self.vm.call(entry)
        return self.vm.read_u32(base + 0x24)

    def clamp(self, vy: int) -> int:
        base = self._actor_at(ACTOR)
        self.vm.write_u32(base + 0x24, vy)
        self.vm.set_reg("a0", base)
        self.vm.call(ENTRY_CLAMP)
        return self.vm.read_u32(base + 0x24)

    def air_control(self, buttons: int, vx: int, state: int, anim_offset: int):
        base = self._actor_at(ACTOR)
        self.vm.write_u8(base + 0x54, buttons)   # byte: held state
        self.vm.write_u32(base + 0x1C, vx)
        self.vm.write_u8(base + 0x30, state)
        self.vm.write_u16(base + 0x08, anim_offset)
        self.vm.set_reg("a0", base)
        self.vm.call(ENTRY_AIR_CONTROL)
        return (self.vm.read_u32(base + 0x1C), self.vm.read_u8(base + 0x30),
                self.vm.read_u16(base + 0x08))

    def integrate(self, x, z, y, vx, vz, vy, anim_offset, flags59):
        base = self._actor_at(ACTOR)
        for off, val in ((0x10, x), (0x14, z), (0x18, y), (0x1C, vx), (0x20, vz), (0x24, vy)):
            self.vm.write_u32(base + off, val)
        self.vm.write_u16(base + 0x08, anim_offset)
        self.vm.write_u8(base + 0x59, flags59)
        self.vm.set_reg("a0", base)
        self.vm.call(ENTRY_INTEGRATE)
        return tuple(self.vm.read_u32(base + off) for off in (0x10, 0x14, 0x18))

    # -- geometry -----------------------------------------------------
    def boxes(self, sprite_w, sprite_h, flags_4b, x, z, y, at_p1_base=False):
        # The ROM test is ``cmpa.w #$b800`` which sign-extends to $FFFFB800,
        # so the P1 record must be addressed through the $FFFF window.
        base = 0x00FFB800 if at_p1_base else ACTOR
        a0 = 0xFFFFB800 if at_p1_base else 0xFFFFB900
        self._actor_at(base)
        self.vm.write_u8(base + 0x02, sprite_w)
        self.vm.write_u8(base + 0x03, sprite_h)
        self.vm.write_u8(base + 0x4B, flags_4b)
        self.vm.write_u16(base + 0x10, x & 0xFFFF)
        self.vm.write_u16(base + 0x14, z & 0xFFFF)
        self.vm.write_u16(base + 0x18, y & 0xFFFF)
        self.vm.set_reg("a0", a0)
        self.vm.call(ENTRY_BOXES)
        return (struct.unpack(">6h", self.vm.read(base + 0x64, 12)),
                struct.unpack(">6h", self.vm.read(base + 0x70, 12)))

    def aabb(self, primary_a, secondary_b) -> bool:
        a = self._actor_at(0x00FFB800)
        b = self._actor_at(0x00FFB880)
        self.vm.write(a + 0x64, struct.pack(">6h", *primary_a))
        self.vm.write(b + 0x70, struct.pack(">6h", *secondary_b))
        self.vm.set_reg("a0", a)
        self.vm.set_reg("a1", b)
        stop = self.vm.call(ENTRY_AABB, stop=[AABB_MISS, AABB_HIT])
        return stop == AABB_HIT

    def project(self, type_id, flags_01, x, z, y, cam_x=0, cam_y=0, police=False):
        base = ACTOR
        self._actor_at(base)
        self.vm.write_u8(base + 0x00, type_id)
        self.vm.write_u8(base + 0x01, flags_01)
        self.vm.write_u32(base + 0x04, 0x00010000)   # valid ROM pointer
        self.vm.write_u16(base + 0x08, 0x0000)
        self.vm.write_u16(base + 0x10, x & 0xFFFF)
        self.vm.write_u16(base + 0x14, z & 0xFFFF)
        self.vm.write_u16(base + 0x18, y & 0xFFFF)
        self.vm.write_u16(0x00FFE002, cam_x)
        self.vm.write_u16(0x00FFE00E, cam_y)
        self.vm.write_u16(0x00FFFA1A, 1 if police else 0)
        self.vm.set_reg("a0", base)
        stop = self.vm.call(ENTRY_PROJECT, stop=[PROJECT_SURVIVED, PROJECT_CULLED])
        if stop == PROJECT_CULLED:
            return (None, None, True)
        return (self.vm.read_u16(base + 0x28), self.vm.read_u16(base + 0x2C), False)

    # -- recovered behaviours (Stage-2 re-verification of earlier claims) ---
    def cheat(self, code: bytes, player1: bool = True):
        """$005920 name-entry routine. Returns (stock_byte, lives_byte)."""
        base = 0x00FFB800 if player1 else 0x00FFB880
        a0 = 0xFFFFB800 if player1 else 0xFFFFB880
        self.vm.write(0x00FFFF0C if player1 else 0x00FFFF14, code)
        self.vm.write_u8(0x00FFFF35, 0xEE)                 # sentinel
        self.vm.write_u8(0x00FFFF20 if player1 else 0x00FFFF23, 0xEE)
        self.vm.set_reg("a0", a0)
        self.vm.call(0x005920)
        return self.vm.read_u8(0x00FFFF35), self.vm.read_u8(0x00FFFF20 if player1 else 0x00FFFF23)

    def jump_profile(self, vy0: int, kind: str, frames: int = 60):
        """Signed y/vy trace of a free-flight jump, via oracle.frame."""
        plan = dict(gravity=kind, air_control=False, buttons=0, cam_x=0, cam_y=0,
                    initial=dict(x=0, z=0, y=0, vx=0, vz=0, vy=vy0,
                                 sprite_w=4, sprite_h=2))
        tr = self.frame(plan, frames)
        ys = [struct.unpack(">i", struct.pack(">I", t["y"]))[0] for t in tr]
        vys = [struct.unpack(">i", struct.pack(">I", t["vy"]))[0] for t in tr]
        return ys, vys

    # -- step-level composition (same order as the player frame) ------
    def frame(self, plan: dict, frames: int):
        """Run `frames` iterations of the documented per-frame order on the ROM
        routines and return a list of snapshots (bytes read back exactly)."""
        base = self._actor_at(ACTOR)
        a = plan["initial"]
        for off, val in (("x", 0x10), ("z", 0x14), ("y", 0x18), ("vx", 0x1C), ("vz", 0x20), ("vy", 0x24)):
            self.vm.write_u32(base + val, a[off])
        self.vm.write_u8(base + 0x00, a.get("type_id", 1))
        self.vm.write_u8(base + 0x01, a.get("flags_01", 0))
        self.vm.write_u8(base + 0x02, a.get("sprite_w", 0))
        self.vm.write_u8(base + 0x03, a.get("sprite_h", 0))
        self.vm.write_u8(base + 0x30, a.get("state", 0))
        self.vm.write_u8(base + 0x4B, a.get("flags_4b", 0))
        self.vm.write_u8(base + 0x59, a.get("flags_59", 0))
        self.vm.write_u16(base + 0x08, a.get("anim_offset", 0))
        self.vm.write_u32(base + 0x04, 0x00010000)   # valid animation-bank pointer for $00AF46
        self.vm.set_reg("a0", base)
        trace = []
        self.vm.write_u16(0x00FFE002, plan.get("cam_x", 0))
        self.vm.write_u16(0x00FFE00E, plan.get("cam_y", 0))
        self.vm.write_u16(0x00FFFA1A, 1 if plan.get("police") else 0)
        for f in range(frames):
            self.vm.write_u8(base + 0x54, plan.get("buttons", 0))
            kind = plan.get("gravity", "neutral")
            self.vm.call({"neutral": ENTRY_NEUTRAL_GRAVITY,
                          "soft": ENTRY_SOFT_GRAVITY,
                          "directional": ENTRY_DIRECTIONAL_GRAVITY}[kind])
            if plan.get("air_control"):
                self.vm.call(ENTRY_AIR_CONTROL)
            self.vm.call(ENTRY_CLAMP)
            self.vm.call(ENTRY_INTEGRATE)
            self.vm.call(ENTRY_BOXES)
            stop = self.vm.call(ENTRY_PROJECT, stop=[PROJECT_SURVIVED, PROJECT_CULLED])
            trace.append({
                "culled": stop == PROJECT_CULLED,
                "frame": f,
                "x": self.vm.read_u32(base + 0x10),
                "z": self.vm.read_u32(base + 0x14),
                "y": self.vm.read_u32(base + 0x18),
                "vx": self.vm.read_u32(base + 0x1C),
                "vz": self.vm.read_u32(base + 0x20),
                "vy": self.vm.read_u32(base + 0x24),
                "sx": self.vm.read_u16(base + 0x28),
                "sy": self.vm.read_u16(base + 0x2C),
                "box_primary": struct.unpack(">6h", self.vm.read(base + 0x64, 12)),
                "box_secondary": struct.unpack(">6h", self.vm.read(base + 0x70, 12)),
                "state": self.vm.read_u8(base + 0x30),
                "anim_offset": self.vm.read_u16(base + 0x08),
            })
        return trace
