"""Core agent interface for ColabGPU Agent Lab."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


class Agent(Protocol):
    """Minimal agent interface."""

    def act(self, observation: Any) -> Any:
        """Return an action for the given observation."""
        raise NotImplementedError

    def reflect(self, reward: float) -> None:
        """Optional reflection hook."""
        return None


@dataclass
class ActionResult:
    """Standardized result for agent-environment interactions."""

    action: Any
    reward: float
    done: bool
    info: dict[str, Any]
