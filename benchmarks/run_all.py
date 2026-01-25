"""Benchmark runner."""

from __future__ import annotations

from agents.reactive import ReactiveAgent
from environments.tool_maze import ToolMaze


def run_tool_maze() -> dict[str, float]:
    tools = {
        "alpha": "First tool for simple tasks.",
        "beta": "Second tool with noisy description.",
    }
    env = ToolMaze(tools=tools, max_steps=2)
    agent = ReactiveAgent(policy=lambda obs: "alpha")
    observation = env.reset()
    _, reward, done, info = env.step(agent.act(observation))
    return {"reward": reward, "done": float(done), "success": float(info["success"])}


def main() -> None:
    results = {
        "tool_maze": run_tool_maze(),
    }
    print("Benchmark results:", results)


if __name__ == "__main__":
    main()
