"""Embedding helpers."""

from __future__ import annotations

import numpy as np


def normalize_embeddings(vectors: np.ndarray) -> np.ndarray:
    """Normalize embeddings to unit length for cosine similarity."""
    norms = np.linalg.norm(vectors, axis=1, keepdims=True) + 1e-12
    return vectors / norms


def seed_everything(seed: int) -> None:
    """Deterministic seeding for numpy."""
    np.random.seed(seed)
