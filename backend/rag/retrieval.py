from typing import List

import faiss
import numpy as np

index = None
stored_chunks: List[str] = []


def create_index(
    embeddings: np.ndarray,
    chunks: List[str]
) -> None:
    """
    Create a FAISS vector index.

    Args:
        embeddings: Embedding vectors.
        chunks: Original text chunks.
    """

    global index, stored_chunks

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    stored_chunks = chunks


def search(
    query_embedding: np.ndarray,
    top_k: int = 3
) -> List[str]:
    """
    Retrieve the most relevant chunks.

    Args:
        query_embedding: Embedding of the user query.
        top_k: Number of results.

    Returns:
        List of retrieved text chunks.
    """

    if index is None:
        raise RuntimeError("Index has not been created.")

    _, indices = index.search(
        np.array([query_embedding]),
        top_k
    )

    return [
        stored_chunks[i]
        for i in indices[0]
    ]
