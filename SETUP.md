# Setup Guide for ColabGPU Agent Lab

## Prerequisites

- Python 3.10 or later
- (Optional) CUDA-capable GPU for GPU acceleration
- (Optional) Google Colab account for notebook execution

## Installation

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/infinityabundance/ColabGPU-Agent-Lab.git
cd ColabGPU-Agent-Lab
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Google Colab

Click the "Open in Colab" badge in the README.md to open the notebook directly in Google Colab.

## Quick Start

### Running Benchmarks

Run all benchmarks:
```bash
python benchmarks/run_all.py
```

Expected output:
```
Benchmark results: {'tool_maze': {'reward': 1.0, 'done': 1.0, 'success': 1.0}}
```

### Testing Components

Test FAISS GPU fallback:
```python
from memory.gpu_faiss import GpuFaissIndex
from memory.embeddings import normalize_embeddings, seed_everything
import numpy as np

seed_everything(7)
dim = 8
vectors = normalize_embeddings(np.random.rand(5, dim).astype(np.float32))
queries = normalize_embeddings(np.random.rand(2, dim).astype(np.float32))

index = GpuFaissIndex(dim)
index.add(vectors)
scores, indices = index.search(queries, top_k=3)
print(f"Search results: {scores.shape} scores, {indices.shape} indices")
```

Test GPU telemetry:
```python
from telemetry.gpu import query_vram

vram = query_vram()
print(f"GPU Memory: {vram['used_mb']:.0f}MB / {vram['total_mb']:.0f}MB")
# Note: Returns zeros if no GPU is available
```

### Using Agents

#### Reactive Agent
```python
from agents.reactive import ReactiveAgent

# Simple policy-based agent
agent = ReactiveAgent(policy=lambda obs: "action")
action = agent.act("observation")
```

#### Memory Agent
```python
from agents.memory_agent import MemoryAgent

def retrieve_memories(query, top_k):
    # Your memory retrieval logic here
    return ["memory1", "memory2", "memory3"][:top_k]

def policy_with_memory(observation, memories):
    # Your policy that uses memories
    return f"action based on {len(memories)} memories"

agent = MemoryAgent(
    retrieve=retrieve_memories,
    policy=policy_with_memory,
    top_k=3
)
action = agent.act("observation")
```

#### Planner Agent
```python
from agents.planner_agent import PlannerAgent

def create_plan(observation):
    # Your planning logic here
    return ["step1", "step2", "step3"]

def fallback_policy(observation):
    # Used when plan is exhausted
    return "default_action"

agent = PlannerAgent(
    planner=create_plan,
    fallback=fallback_policy
)

# Executes plan step-by-step
action1 = agent.act("obs")  # Returns "step1"
action2 = agent.act("obs")  # Returns "step2"
action3 = agent.act("obs")  # Returns "step3"
action4 = agent.act("obs")  # Returns "default_action" (fallback)
```

### Using Environments

#### Tool Maze
```python
from environments.tool_maze import ToolMaze
from agents.reactive import ReactiveAgent

tools = {
    "alpha": "First tool for simple tasks.",
    "beta": "Second tool with noisy description.",
}

env = ToolMaze(tools=tools, max_steps=2)
agent = ReactiveAgent(policy=lambda obs: "alpha")

observation = env.reset()
action = agent.act(observation)
observation, reward, done, info = env.step(action)

print(f"Reward: {reward}, Done: {done}, Success: {info['success']}")
```

#### Memory Drift (Stub)
```python
from environments.memory_drift import MemoryDrift, MemoryDriftConfig

config = MemoryDriftConfig(drift_rate=0.1, max_steps=10)
env = MemoryDrift(config)

observation = env.reset()
for _ in range(10):
    observation, reward, done, info = env.step("action")
    if done:
        break
```

#### Recursive Planner (Stub)
```python
from environments.recursive_planner import RecursivePlanner

env = RecursivePlanner(depth=3)
observation = env.reset()

for _ in range(3):
    observation, reward, done, info = env.step("action")
    if done:
        break
```

## Project Structure

```
ColabGPU-Agent-Lab/
├── agents/              # Agent implementations
│   ├── base.py         # Agent protocol
│   ├── reactive.py     # Simple reactive agent
│   ├── memory_agent.py # Memory-augmented agent
│   └── planner_agent.py# Planning agent
├── environments/        # Environment implementations
│   ├── tool_maze.py    # Tool selection task (complete)
│   ├── memory_drift.py # Memory task (stub)
│   └── recursive_planner.py # Planning task (stub)
├── memory/             # Memory and embedding utilities
│   ├── embeddings.py   # Embedding normalization and seeding
│   └── gpu_faiss.py    # FAISS GPU/CPU index wrapper
├── telemetry/          # Performance monitoring
│   ├── gpu.py         # GPU memory monitoring
│   └── timing.py      # Timing utilities
├── plots/              # Visualization utilities
│   └── visualize.py   # Plotting functions
├── benchmarks/         # Benchmark runners
│   └── run_all.py     # Main benchmark runner
├── agent_lab.ipynb    # Interactive Colab notebook
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

## Development

### Running Tests

The repository includes comprehensive test infrastructure with 13 tests covering all core components:

```bash
# Run all tests
python tests/run_tests.py

# Run individual test suites
python tests/test_agents.py
python tests/test_environments.py
python tests/test_memory.py
```

Test coverage:
- **Agents**: 4 tests (ReactiveAgent, MemoryAgent, PlannerAgent, fallback bug fix)
- **Environments**: 5 tests (ToolMaze success/failure/exhaustion, stubs)
- **Memory**: 4 tests (embeddings, seeding, FAISS operations)

All tests should pass before submitting changes.

### Contributing

1. Check INSPECTION_REPORT.md for current status and planned work
2. Pick an item from the phased implementation plan
3. Create a feature branch
4. Implement your changes
5. Submit a pull request

## GPU Support

### FAISS GPU

The project uses FAISS with automatic GPU fallback:
- If a CUDA GPU is available, FAISS will use it automatically
- If no GPU is available, FAISS falls back to CPU execution
- No code changes needed - the switch is automatic

### Requirements for GPU

For GPU support, install:
```bash
pip install faiss-gpu  # Instead of faiss-cpu
pip install torch      # With CUDA support
```

Note: The default `requirements.txt` uses `faiss-cpu` for compatibility.

## Troubleshooting

### Import Errors

If you get `ModuleNotFoundError`:
- Ensure you're running scripts from the repository root
- The benchmark runner includes automatic path setup
- For custom scripts, add:
  ```python
  import sys
  import os
  sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
  ```

### GPU Not Detected

If GPU telemetry returns zeros:
- This is expected if no NVIDIA GPU is available
- The code gracefully falls back to CPU
- To verify GPU: Run `nvidia-smi` in terminal

### FAISS Installation Issues

If FAISS installation fails:
- Ensure you have Python 3.10+
- Try installing `faiss-cpu` explicitly: `pip install faiss-cpu`
- For GPU: Follow [official FAISS GPU installation guide](https://github.com/facebookresearch/faiss/wiki)

## Known Issues

See INSPECTION_REPORT.md for:
- Current implementation status
- Known bugs (now fixed in latest version)
- Missing features
- Planned improvements

## Additional Resources

- **README.md**: Project overview and roadmap
- **INSPECTION_REPORT.md**: Detailed status analysis
- **agent_lab.ipynb**: Interactive demonstrations
- **GitHub Issues**: For bug reports and feature requests

## Questions?

Open an issue on GitHub or check the INSPECTION_REPORT.md for detailed documentation about the current state of the project.
