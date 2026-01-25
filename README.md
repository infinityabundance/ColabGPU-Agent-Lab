# ColabGPU Agent Lab

A GPU-accelerated, fully reproducible agent research lab that runs in a single Google Colab notebook.

## What this is

This repo is a measurement instrument for agents: deterministic environments, GPU-backed memory, and
telemetry that makes experiments reproducible and inspectable.

## Repo structure

```
colab-gpu-agent-lab/
├── agent_lab.ipynb        # The paper, the lab, the demo
├── agents/
│   ├── base.py            # Agent interface
│   ├── reactive.py
│   ├── memory_agent.py
│   └── planner_agent.py
├── memory/
│   ├── gpu_faiss.py       # FAISS-GPU vector store
│   └── embeddings.py
├── environments/
│   ├── tool_maze.py
│   ├── memory_drift.py
│   └── recursive_planner.py
├── benchmarks/
│   └── run_all.py
├── telemetry/
│   ├── gpu.py
│   └── timing.py
├── plots/
│   └── visualize.py
├── requirements.txt
└── README.md
```

## Quick start (Colab)

1. Open `agent_lab.ipynb` in Google Colab.
2. Run the setup cell to install dependencies.
3. Execute the GPU check and FAISS test cells.
4. Run the Tool Maze demo to see metrics and plots.

## Reproducibility

- Deterministic seeds via `memory/embeddings.py`.
- GPU VRAM telemetry via `telemetry/gpu.py`.
- Benchmarks entry point in `benchmarks/run_all.py`.

## License

See [LICENSE](LICENSE).
