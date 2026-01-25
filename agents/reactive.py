"""Reactive agent baseline."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from .base import Agent


@dataclass
class ReactiveAgent(Agent):
    """Selects an action from an observation via a policy callable."""

    policy: Callable[[Any], Any]

    def act(self, observation: Any) -> Any:
        return self.policy(observation)
