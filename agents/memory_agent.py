"""Agent that consults an embedding memory before acting."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Sequence

from .base import Agent


@dataclass
class MemoryAgent(Agent):
    """Retrieves relevant memories and passes them to the policy."""

    retrieve: Callable[[str, int], Sequence[str]]
    policy: Callable[[Any, Sequence[str]], Any]
    top_k: int = 3

    def act(self, observation: Any) -> Any:
        memories = self.retrieve(str(observation), self.top_k)
        return self.policy(observation, memories)
