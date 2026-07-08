from fastapi import FastAPI

from routes import query, upload

app = FastAPI(
    title="RAG Backend",
    description="Backend API for Retrieval-Augmented Generation.",
    version="1.0.0"
)

app.include_router(upload.router)
app.include_router(query.router)


@app.get("/")
def home():
    """Root endpoint."""

    return {
        "message": "RAG backend is running 🚀"
    }


@app.get("/health")
def health():
    """Health check endpoint."""

    return {
        "status": "healthy"
    }
