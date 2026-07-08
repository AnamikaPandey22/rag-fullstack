from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embeddings(chunks: List[str]) -> np.ndarray:
    """
    Generate vector embeddings for text chunks.

    Args:
        chunks: List of text chunks.

    Returns:
        NumPy array containing embeddings.
    """

    return model.encode(
        chunks,
        convert_to_numpy=True
    )
