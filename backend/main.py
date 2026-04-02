from fastapi import FastAPI
from routes import upload, query

app = FastAPI()
app.include_router(upload.router)
app.include_router(query.router)

@app.get("/")
def home():
    return {"message": "RAG backend is running 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}