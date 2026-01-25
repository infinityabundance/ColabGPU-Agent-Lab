"""Memory drift environment stub."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MemoryDriftConfig:
    drift_rate: float = 0.1
    max_steps: int = 10


class MemoryDrift:
    """Placeholder environment for memory drift experiments."""

    def __init__(self, config: MemoryDriftConfig) -> None:
        self.config = config
        self.steps = 0

    def reset(self) -> str:
        self.steps = 0
        return "Memory drift reset."

    def step(self, action: str) -> tuple[str, float, bool, dict[str, float]]:
        self.steps += 1
        reward = 1.0 - self.config.drift_rate * self.steps
        done = self.steps >= self.config.max_steps
        return "Memory drift step.", reward, done, {"drift": self.config.drift_rate}
