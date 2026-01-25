"""Tool Maze environment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class ToolState:
    observation: str
    steps_left: int
    goal_tool: str
    done: bool = False


class ToolMaze:
    """Environment where the agent must select the correct tool."""

    def __init__(self, tools: Dict[str, str], max_steps: int = 3) -> None:
        self.tools = tools
        self.max_steps = max_steps
        self.state = self._reset_state()

    def _reset_state(self) -> ToolState:
        tool_names = list(self.tools.keys())
        goal_tool = tool_names[0]
        observation = self._render_observation(goal_tool)
        return ToolState(observation=observation, steps_left=self.max_steps, goal_tool=goal_tool)

    def _render_observation(self, goal_tool: str) -> str:
        descriptions = [f"{name}: {desc}" for name, desc in self.tools.items()]
        return "Choose the correct tool.\n" + "\n".join(descriptions) + f"\nTarget: {goal_tool}"

    def reset(self) -> str:
        self.state = self._reset_state()
        return self.state.observation

    def step(self, action: str) -> tuple[str, float, bool, Dict[str, Any]]:
        if self.state.done:
            return self.state.observation, 0.0, True, {"reason": "already_done"}

        self.state.steps_left -= 1
        success = action == self.state.goal_tool
        reward = 1.0 if success else -0.1
        done = success or self.state.steps_left <= 0
        self.state.done = done
        info = {"success": success, "steps_left": self.state.steps_left}
        return self.state.observation, reward, done, info

    def available_tools(self) -> List[str]:
        return list(self.tools.keys())
