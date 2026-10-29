"""Mivi video tool for OpenMontage — drop-in adapter.

Install (inside an OpenMontage checkout):

    cp -r bridge tools/_mivi                 # our signed Mivi API layer
    cp studio/openmontage/mivi_video.py tools/video/mivi_video.py

Then it appears next to the 20+ paid providers: any pipeline that needs
`video_generation` can pick `provider="mivi"` with no API key and no cost.

Why this shape: OpenMontage's contract is `BaseTool` + `execute(inputs) -> ToolResult`,
with capability/support flags the scorer reads. This file only speaks that contract —
all the Mivi knowledge stays in `tools/_mivi/mivi_mcp.py`.

Caveats, because they matter for the planner:
  * image_to_video only (no text_to_video) — a still is mandatory
  * shot length is fixed at 4.03 s; `seconds` is ignored beyond a warning
  * no seed, no last-frame control, no audio
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from tools.base_tool import (
    BaseTool,
    Determinism,
    ExecutionMode,
    ToolResult,
    ToolRuntime,
    ToolStability,
    ToolStatus,
    ToolTier,
)

# our API layer, vendored at tools/_mivi/
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_mivi"))
try:
    import mivi_mcp as M
except Exception as exc:  # pragma: no cover - surfaces as a health error, not a crash
    M = None
    _IMPORT_ERROR = exc
else:
    _IMPORT_ERROR = None

MODELS = list(getattr(M, "VIDEO_MODELS", {}) or {})
SHOT_SECONDS = 4.03


class MiviVideo(BaseTool):
    name = "mivi_video"
    version = "1.0.0"
    tier = ToolTier.GENERATE
    capability = "video_generation"
    provider = "mivi"
    stability = ToolStability.EXPERIMENTAL
    execution_mode = ExecutionMode.SYNC
    determinism = Determinism.STOCHASTIC
    runtime = ToolRuntime.API

    dependencies: list[str] = []          # no API key: the Mivi account is the credential
    install_instructions = (
        "Vendor this repo's bridge/ as tools/_mivi/ and set MIVI_USER if the default "
        "account is wrong. No key, no billing — renders draw on the Mivi app account."
    )
    agent_skills = ["mivi-film"]

    capabilities = ["image_to_video"]
    supports = {
        "text_to_video": False,           # not offered by Mivi
        "image_to_video": True,
        "first_last_frame_to_video": False,
        "reference_to_video": False,
        "reference_image": True,
        "audio": False,
        "seed": False,
        "duration_control": False,
        "negative_prompt": False,
        "resolution_720p": True,
        "resolution_1080p": False,
        "aspect_9_16": True,
        "aspect_16_9": False,
        "max_seconds": SHOT_SECONDS,
    }

    def health_check(self) -> tuple[ToolStatus, str]:
        if M is None:
            return ToolStatus.UNAVAILABLE, f"mivi api layer not importable: {_IMPORT_ERROR}"
        return ToolStatus.AVAILABLE, f"user {M.USER} via {M.HOST}"

    def estimate_cost(self, inputs: dict[str, Any]) -> float:
        return 0.0                        # paid in-app, not in USD

    def execute(self, inputs: dict[str, Any]) -> ToolResult:
        if M is None:
            return ToolResult(success=False, error=f"mivi api layer not importable: {_IMPORT_ERROR}")

        image = inputs.get("image_path") or inputs.get("image")
        if not image:
            return ToolResult(success=False, error="image_to_video requires image_path")
        seconds = float(inputs.get("seconds") or SHOT_SECONDS)
        if abs(seconds - SHOT_SECONDS) > 0.5:
            # not fatal, but the planner should know the picture will be 4.03 s
            pass

        prompt = (inputs.get("prompt") or "").strip()
        model = inputs.get("model") or "mivi-gx-720p"
        quality = int(inputs.get("quality") or (1 if inputs.get("draft") else 2))
        out_dir = Path(inputs.get("output_dir") or "output")
        out_dir.mkdir(parents=True, exist_ok=True)
        out = inputs.get("output_path") or str(out_dir / "mivi_shot.mp4")

        try:
            created = M.t_video({"image": str(image), "prompt": prompt,
                                 "model": model, "quality": quality})
            res = M.t_video_wait({"task_id": created["task_id"], "out": out,
                                  "timeout_s": float(inputs.get("timeout_s") or 420)})
        except Exception as exc:
            return ToolResult(success=False, error=str(exc), model=model)

        if not res.get("video_url"):
            return ToolResult(success=False, model=model,
                              error=f"render did not finish: {res.get('reason') or res}")

        return ToolResult(
            success=True,
            data={"video_path": res.get("saved"), "video_url": res["video_url"],
                  "task_id": created["task_id"], "duration_seconds": SHOT_SECONDS,
                  "quality": quality, "aspect": "3:4",
                  "note": "chaining via last frame is the continuity tool; no seed"},
            artifacts=[res["saved"]] if res.get("saved") else [],
            cost_usd=0.0, duration_seconds=SHOT_SECONDS, model=model,
        )
