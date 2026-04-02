from fastapi import APIRouter, UploadFile, File
from pypdf import PdfReader
from rag.chunking import chunk_text
from rag.embedding import get_embeddings
from rag.retrieval import create_index

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    
    reader = PdfReader(file.file)
    
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    
    chunks = chunk_text(text)
    embeddings = get_embeddings(chunks)
    create_index(embeddings, chunks)
    return {
        "filename": file.filename,
        "num_chunks": len(chunks),
        "embedding_shape": str(embeddings.shape)
    }