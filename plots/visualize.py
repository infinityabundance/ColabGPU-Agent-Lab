"""Plotting utilities."""

from __future__ import annotations

import matplotlib.pyplot as plt


def plot_metric(series: list[float], title: str, ylabel: str) -> None:
    plt.figure(figsize=(6, 4))
    plt.plot(series, marker="o")
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel("Step")
    plt.grid(True, alpha=0.3)
    plt.show()
