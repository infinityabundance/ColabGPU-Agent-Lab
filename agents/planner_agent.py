"""Planner-style agent baseline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Iterable, List

from .base import Agent


@dataclass
class PlannerAgent(Agent):
    """Creates a plan and executes it step-by-step."""

    planner: Callable[[Any], Iterable[Any]]
    fallback: Callable[[Any], Any]
    _plan: List[Any] = field(default_factory=list)
    _has_planned: bool = field(default=False)

    def act(self, observation: Any) -> Any:
        if not self._has_planned:
            self._plan = list(self.planner(observation))
            self._has_planned = True
        if self._plan:
            return self._plan.pop(0)
        return self.fallback(observation)
