"""GPU telemetry helpers."""

from __future__ import annotations

import subprocess
from typing import Dict


def query_vram() -> Dict[str, float]:
    """Query VRAM usage via nvidia-smi."""
    result = subprocess.run(
        [
            "nvidia-smi",
            "--query-gpu=memory.used,memory.total",
            "--format=csv,noheader,nounits",
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0 or not result.stdout.strip():
        return {"used_mb": 0.0, "total_mb": 0.0}
    used, total = result.stdout.strip().split(",")
    return {"used_mb": float(used), "total_mb": float(total)}
