from fastapi import APIRouter
from rag.embedding import model
from rag.retrieval import search

router = APIRouter()

@router.get("/query")
def query(q: str):
    
    query_embedding = model.encode([q])[0]
    results = search(query_embedding)
    
    return {
        "query": q,
        "results": results
    }