"""Test runner - runs all test suites."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import test modules
import test_agents
import test_environments
import test_memory


def run_all_tests():
    """Run all test suites."""
    print("=" * 60)
    print("Running ColabGPU Agent Lab Test Suite")
    print("=" * 60)
    
    print("\n📦 Testing Agents...")
    print("-" * 60)
    test_agents.test_reactive_agent()
    test_agents.test_memory_agent()
    test_agents.test_planner_agent()
    test_agents.test_planner_agent_no_replan()
    
    print("\n🌍 Testing Environments...")
    print("-" * 60)
    test_environments.test_tool_maze_success()
    test_environments.test_tool_maze_failure()
    test_environments.test_tool_maze_max_steps()
    test_environments.test_memory_drift_basic()
    test_environments.test_recursive_planner_basic()
    
    print("\n🧠 Testing Memory System...")
    print("-" * 60)
    test_memory.test_normalize_embeddings()
    test_memory.test_seed_everything()
    test_memory.test_gpu_faiss_index()
    test_memory.test_gpu_faiss_self_search()
    
    print("\n" + "=" * 60)
    print("✅ ALL TESTS PASSED!")
    print("=" * 60)


if __name__ == "__main__":
    try:
        run_all_tests()
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
