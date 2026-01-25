"""FAISS-GPU vector store utilities."""

from __future__ import annotations

import faiss
import numpy as np


class GpuFaissIndex:
    """Simple FAISS GPU wrapper for cosine similarity search."""

    def __init__(self, dimension: int, gpu_id: int = 0) -> None:
        self.dimension = dimension
        self.gpu_id = gpu_id
        self.resources = faiss.StandardGpuResources()
        cpu_index = faiss.IndexFlatIP(dimension)
        self.index = faiss.index_cpu_to_gpu(self.resources, gpu_id, cpu_index)

    def add(self, vectors: np.ndarray) -> None:
        self.index.add(vectors.astype(np.float32))

    def search(self, queries: np.ndarray, top_k: int = 5) -> tuple[np.ndarray, np.ndarray]:
        scores, indices = self.index.search(queries.astype(np.float32), top_k)
        return scores, indices
