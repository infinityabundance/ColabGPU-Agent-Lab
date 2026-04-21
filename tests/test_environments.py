"""Test suite for environments."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from environments.tool_maze import ToolMaze
from environments.memory_drift import MemoryDrift, MemoryDriftConfig
from environments.recursive_planner import RecursivePlanner


def test_tool_maze_success():
    """Test ToolMaze with correct tool selection."""
    tools = {
        "alpha": "First tool",
        "beta": "Second tool",
    }
    env = ToolMaze(tools=tools, max_steps=2)
    obs = env.reset()
    
    # The goal tool is always the first one (alpha)
    obs, reward, done, info = env.step("alpha")
    
    assert reward == 1.0, f"Expected reward 1.0 for correct tool, got {reward}"
    assert done is True, "Episode should be done after correct selection"
    assert info["success"] is True, "Success flag should be True"
    print("✓ ToolMaze success test passed")


def test_tool_maze_failure():
    """Test ToolMaze with incorrect tool selection."""
    tools = {
        "alpha": "First tool",
        "beta": "Second tool",
    }
    env = ToolMaze(tools=tools, max_steps=2)
    obs = env.reset()
    
    # Select wrong tool
    obs, reward, done, info = env.step("beta")
    
    assert reward == -0.1, f"Expected reward -0.1 for wrong tool, got {reward}"
    assert done is False, "Episode should continue after wrong selection"
    assert info["success"] is False, "Success flag should be False"
    assert info["steps_left"] == 1, f"Should have 1 step left, got {info['steps_left']}"
    print("✓ ToolMaze failure test passed")


def test_tool_maze_max_steps():
    """Test ToolMaze exhausts max steps."""
    tools = {"alpha": "First", "beta": "Second"}
    env = ToolMaze(tools=tools, max_steps=1)
    obs = env.reset()
    
    # Use wrong tool, exhausting steps
    obs, reward, done, info = env.step("beta")
    
    assert done is True, "Episode should end when steps exhausted"
    assert info["steps_left"] == 0, "Should have 0 steps left"
    print("✓ ToolMaze max_steps test passed")


def test_memory_drift_basic():
    """Test MemoryDrift stub environment."""
    config = MemoryDriftConfig(drift_rate=0.1, max_steps=5)
    env = MemoryDrift(config)
    
    obs = env.reset()
    assert obs == "Memory drift reset.", f"Expected reset message, got {obs}"
    
    # Step through environment
    obs, reward, done, info = env.step("action")
    assert reward == 0.9, f"Expected reward 0.9, got {reward}"
    assert done is False, "Should not be done after 1 step"
    
    # Check final step
    for _ in range(4):
        obs, reward, done, info = env.step("action")
    
    assert done is True, "Should be done after max_steps"
    print("✓ MemoryDrift basic test passed")


def test_recursive_planner_basic():
    """Test RecursivePlanner stub environment."""
    env = RecursivePlanner(depth=3)
    
    obs = env.reset()
    assert obs == "Recursive planner reset.", f"Expected reset message, got {obs}"
    
    # Step through levels
    for level in range(1, 4):
        obs, reward, done, info = env.step("action")
        assert info["level"] == level, f"Expected level {level}, got {info['level']}"
        
        if level < 3:
            assert done is False, f"Should not be done at level {level}"
            assert reward == 0.0, f"Expected reward 0.0 at level {level}, got {reward}"
        else:
            assert done is True, "Should be done at final level"
            assert reward == 1.0, f"Expected reward 1.0 at final level, got {reward}"
    
    print("✓ RecursivePlanner basic test passed")


if __name__ == "__main__":
    test_tool_maze_success()
    test_tool_maze_failure()
    test_tool_maze_max_steps()
    test_memory_drift_basic()
    test_recursive_planner_basic()
    print("\n✅ All environment tests passed!")
