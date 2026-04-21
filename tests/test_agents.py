"""Test suite for agents."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.reactive import ReactiveAgent
from agents.memory_agent import MemoryAgent
from agents.planner_agent import PlannerAgent


def test_reactive_agent():
    """Test ReactiveAgent basic functionality."""
    agent = ReactiveAgent(policy=lambda obs: f"action_{obs}")
    action = agent.act("test")
    assert action == "action_test", f"Expected 'action_test', got {action}"
    print("✓ ReactiveAgent test passed")


def test_memory_agent():
    """Test MemoryAgent with mocked memory retrieval."""
    def mock_retrieve(query, top_k):
        return ["mem1", "mem2", "mem3"][:top_k]
    
    def mock_policy(obs, memories):
        return f"action_with_{len(memories)}_memories"
    
    agent = MemoryAgent(retrieve=mock_retrieve, policy=mock_policy, top_k=2)
    action = agent.act("test")
    assert action == "action_with_2_memories", f"Expected 'action_with_2_memories', got {action}"
    print("✓ MemoryAgent test passed")


def test_planner_agent():
    """Test PlannerAgent plan execution and fallback."""
    def mock_planner(obs):
        return ["action1", "action2"]
    
    def mock_fallback(obs):
        return "fallback"
    
    agent = PlannerAgent(planner=mock_planner, fallback=mock_fallback)
    
    # Test plan execution
    assert agent.act("obs") == "action1", "First action should be action1"
    assert agent.act("obs") == "action2", "Second action should be action2"
    
    # Test fallback when plan is exhausted
    assert agent.act("obs") == "fallback", "Should use fallback when plan is exhausted"
    assert agent.act("obs") == "fallback", "Should continue using fallback"
    
    print("✓ PlannerAgent test passed")


def test_planner_agent_no_replan():
    """Test that PlannerAgent doesn't replan after exhaustion (bug fix verification)."""
    call_count = [0]
    
    def counting_planner(obs):
        call_count[0] += 1
        return ["action1", "action2"]
    
    def mock_fallback(obs):
        return "fallback"
    
    agent = PlannerAgent(planner=counting_planner, fallback=mock_fallback)
    
    # Execute plan
    agent.act("obs")
    agent.act("obs")
    
    # Use fallback multiple times
    agent.act("obs")
    agent.act("obs")
    
    assert call_count[0] == 1, f"Planner should be called once, was called {call_count[0]} times"
    print("✓ PlannerAgent no-replan test passed")


if __name__ == "__main__":
    test_reactive_agent()
    test_memory_agent()
    test_planner_agent()
    test_planner_agent_no_replan()
    print("\n✅ All agent tests passed!")
