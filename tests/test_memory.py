"""Test suite for memory and embedding utilities."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from memory.embeddings import normalize_embeddings, seed_everything
from memory.gpu_faiss import GpuFaissIndex


def test_normalize_embeddings():
    """Test embedding normalization to unit length."""
    vectors = np.array([
        [3.0, 4.0],
        [5.0, 12.0],
    ])
    
    normalized = normalize_embeddings(vectors)
    
    # Check that norms are 1.0
    norms = np.linalg.norm(normalized, axis=1)
    assert np.allclose(norms, 1.0), f"Expected unit norms, got {norms}"
    
    # Check specific values
    assert np.allclose(normalized[0], [0.6, 0.8]), f"Expected [0.6, 0.8], got {normalized[0]}"
    assert np.allclose(normalized[1], [5/13, 12/13]), f"Expected [5/13, 12/13], got {normalized[1]}"
    
    print("✓ normalize_embeddings test passed")


def test_seed_everything():
    """Test that seeding produces reproducible results."""
    seed_everything(42)
    result1 = np.random.rand(5)
    
    seed_everything(42)
    result2 = np.random.rand(5)
    
    assert np.array_equal(result1, result2), "Seeding should produce identical results"
    print("✓ seed_everything test passed")


def test_gpu_faiss_index():
    """Test FAISS index creation, addition, and search."""
    dim = 8
    index = GpuFaissIndex(dim)
    
    # Add vectors
    vectors = np.random.rand(10, dim).astype(np.float32)
    vectors = vectors / np.linalg.norm(vectors, axis=1, keepdims=True)  # Normalize for cosine similarity
    index.add(vectors)
    
    # Search
    queries = np.random.rand(2, dim).astype(np.float32)
    queries = queries / np.linalg.norm(queries, axis=1, keepdims=True)
    scores, indices = index.search(queries, top_k=3)
    
    # Check shapes
    assert scores.shape == (2, 3), f"Expected shape (2, 3), got {scores.shape}"
    assert indices.shape == (2, 3), f"Expected shape (2, 3), got {indices.shape}"
    
    # Check that indices are valid
    assert np.all(indices >= 0), "All indices should be non-negative"
    assert np.all(indices < 10), "All indices should be less than 10"
    
    print("✓ GpuFaissIndex test passed")


def test_gpu_faiss_self_search():
    """Test that searching for added vectors returns themselves as top results."""
    seed_everything(123)
    dim = 4
    index = GpuFaissIndex(dim)
    
    # Add normalized vectors
    vectors = np.random.rand(5, dim).astype(np.float32)
    vectors = vectors / np.linalg.norm(vectors, axis=1, keepdims=True)
    index.add(vectors)
    
    # Search with the same vectors
    scores, indices = index.search(vectors, top_k=1)
    
    # Each vector should find itself as the top match
    expected_indices = np.arange(5).reshape(-1, 1)
    assert np.array_equal(indices, expected_indices), \
        f"Expected each vector to find itself, got {indices.flatten()} vs {expected_indices.flatten()}"
    
    # Scores should be close to 1.0 (perfect cosine similarity)
    assert np.all(scores > 0.99), f"Expected scores near 1.0, got {scores}"
    
    print("✓ GpuFaissIndex self-search test passed")


if __name__ == "__main__":
    test_normalize_embeddings()
    test_seed_everything()
    test_gpu_faiss_index()
    test_gpu_faiss_self_search()
    print("\n✅ All memory tests passed!")
