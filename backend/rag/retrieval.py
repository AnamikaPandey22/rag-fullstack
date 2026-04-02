import faiss
import numpy as np

index = None
stored_chunks = []

def create_index(embeddings, chunks):
    global index, stored_chunks
    
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    
    index.add(embeddings)
    stored_chunks = chunks

def search(query_embedding, top_k=3):
    global index, stored_chunks
    
    distances, indices = index.search(
        np.array([query_embedding]), top_k
    )
    
    results = [stored_chunks[i] for i in indices[0]]
    return results