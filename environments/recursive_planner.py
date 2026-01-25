"""Recursive planner environment stub."""

from __future__ import annotations


class RecursivePlanner:
    """Placeholder for recursive planning tasks."""

    def __init__(self, depth: int = 3) -> None:
        self.depth = depth
        self.level = 0

    def reset(self) -> str:
        self.level = 0
        return "Recursive planner reset."

    def step(self, action: str) -> tuple[str, float, bool, dict[str, int]]:
        self.level += 1
        done = self.level >= self.depth
        reward = 1.0 if done else 0.0
        return "Recursive planner step.", reward, done, {"level": self.level}
