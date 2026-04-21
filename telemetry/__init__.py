"""Telemetry utilities for ColabGPU Agent Lab."""

from .gpu import query_vram
from .timing import time_block

__all__ = [
    "query_vram",
    "time_block",
]
