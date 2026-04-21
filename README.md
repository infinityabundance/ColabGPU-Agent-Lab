# ColabGPU Agent Lab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ColabGPU-Agent-Lab/ColabGPU-Agent-Lab/blob/main/agent_lab.ipynb)

A GPU-accelerated, fully reproducible agent research lab that runs entirely inside a single Google Colab notebook. The goal is to make **agent research measurable, deterministic, and GPU-native** while staying lightweight enough to run on free or Pro Colab GPUs.

## Why this exists

Most agent frameworks are CPU-bound, opaque, and hard to reproduce. ColabGPU Agent Lab is the opposite:

- **Colab-first**: one-click runnable, no local setup.
- **GPU-accelerated where it matters**: embeddings, memory search, planning rollouts, and simulation.
- **Deterministic benchmarks**: fixed seeds and metrics you can trust.
- **Notebook-as-a-paper**: structured like a research artifact you can export.

## What you get (initial roadmap)

### 1) GPU-Accelerated Cognitive Stack

A clear, inspectable dataflow with explicit GPU offload targets.

```
[Perception] → [GPU Memory] → [Planner] → [Tool Exec] → [Reflection]
```

Planned GPU usage:
- FAISS-GPU for memory similarity search.
- GPU embeddings for rapid context retrieval.
- Vectorized rollouts for planning and simulation.

### 2) Agent Stress-Test Suite

A set of deterministic, GPU-batched cognitive benchmarks:

| Test                | What it Measures         |
| ------------------- | ------------------------ |
| Tool Maze           | Tool selection reasoning |
| Memory Drift        | Long-horizon recall      |
| Deception Detection | Self-consistency         |
| Recursive Planning  | Depth vs compute         |
| Energy Budget       | Reasoning efficiency     |

Each test outputs:
- Seeded run artifacts
- Metrics (accuracy, cost proxy, step counts)
- Plots for quick comparison

### 3) Live GPU Telemetry Overlay

A lightweight, notebook-native telemetry panel to monitor:
- GPU memory
- Tokens/sec (or tokens/step)
- Planning depth
- Memory growth
- Cost proxy

### 4) Notebook-as-a-Paper

A single notebook structured as:
1. Abstract
2. Method
3. Experiments
4. Results
5. Reproducibility

Export to PDF to get a research-ready artifact.

## Proposed repo structure

```
colabgpu-agent-lab/
├── notebooks/
│   └── colabgpu_agent_lab.ipynb
├── src/
│   ├── agents/
│   ├── benchmarks/
│   ├── memory/
│   ├── planner/
│   ├── telemetry/
│   └── utils/
├── assets/
│   └── figures/
├── data/
│   └── seeds/
└── README.md
```

## Suggested stack (GPU-friendly)

- **PyTorch** + **CUDA** for compute
- **FAISS-GPU** for memory retrieval
- **cuDF/cuML** (optional) for fast metric aggregation
- **Plotly** or **Altair** for notebook-native plots
- **NVML** (via `pynvml`) for GPU telemetry

## First benchmark suite (v0)

1. **Tool Maze**
   - Tiny deterministic environment with tools and rewards
   - Measures decision quality under tool constraints
2. **Memory Drift**
   - Sliding-window tasks with long-horizon recall
   - Measures retention vs. compute budget
3. **Recursive Planning**
   - Depth-limited tree search with known optimal solutions
   - Measures quality vs. planning depth

## Quick start (planned)

1. Open the notebook in Colab.
2. Run the setup cell to install GPU dependencies.
3. Select a benchmark and an agent policy.
4. Run experiments and export results.

## Status

**Current Implementation**: ~30% Complete (Prototype Stage)

This repository has a working foundation with:
- ✅ 3 agent types (ReactiveAgent, MemoryAgent, PlannerAgent)
- ✅ 1 complete benchmark (Tool Maze)
- ✅ FAISS GPU/CPU memory system
- ✅ Basic telemetry (GPU memory)
- ✅ 13 passing tests
- ⚠️ 2 stub environments (Memory Drift, Recursive Planner)
- ⚠️ Missing 3 benchmarks (Deception Detection, Energy Budget, full implementations)

**See detailed status**: [`STATUS.md`](STATUS.md) | [`INSPECTION_REPORT.md`](INSPECTION_REPORT.md)

### 📚 Documentation

- **[SETUP.md](SETUP.md)** - Installation, usage, and troubleshooting
- **[STATUS.md](STATUS.md)** - Current implementation status summary  
- **[INSPECTION_REPORT.md](INSPECTION_REPORT.md)** - Comprehensive 10-section analysis
- **[TODO.md](TODO.md)** - Task list for contributors
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - At-a-glance command reference

### 🚀 Quick Start

```bash
# Install and test
pip install -r requirements.txt
python tests/run_tests.py

# Run benchmark
python benchmarks/run_all.py
```

See [SETUP.md](SETUP.md) for detailed instructions.
