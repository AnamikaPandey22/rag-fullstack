from typing import List


def chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50
) -> List[str]:
    """
    Split text into overlapping chunks.

    Args:
        text: Input document.
        chunk_size: Maximum characters per chunk.
        overlap: Number of overlapping characters.

    Returns:
        List of text chunks.
    """

    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk size.")

    chunks = []

    step = chunk_size - overlap

    for i in range(0, len(text), step):
        chunks.append(text[i:i + chunk_size])

    return chunks
