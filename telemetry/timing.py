"""Timing helpers."""

from __future__ import annotations

import time
from contextlib import contextmanager
from typing import Generator


@contextmanager
def time_block(label: str) -> Generator[float, None, None]:
    start = time.perf_counter()
    yield start
    end = time.perf_counter()
    duration = end - start
    print(f"{label}: {duration:.4f}s")
