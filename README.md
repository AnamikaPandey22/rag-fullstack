# 🚀 RAG Full Stack Backend

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-orange?style=for-the-badge)
![Sentence Transformers](https://img.shields.io/badge/SentenceTransformers-Embeddings-red?style=for-the-badge)

</p>

A lightweight **Retrieval-Augmented Generation (RAG) backend** that enables semantic document search using **FastAPI**, **Sentence Transformers**, and **FAISS**.

The application extracts text from uploaded PDF documents, converts the content into vector embeddings, indexes them using FAISS, and retrieves the most relevant document chunks for a user query.

---

# ✨ Features

- 📄 Upload PDF documents
- ✂️ Automatic text chunking
- 🧠 Generate semantic embeddings using Sentence Transformers
- ⚡ Fast similarity search with FAISS
- 🔍 Retrieve the most relevant document chunks
- 🚀 REST APIs built with FastAPI

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| FastAPI | REST API |
| Sentence Transformers | Text Embeddings |
| FAISS | Vector Similarity Search |
| NumPy | Numerical Operations |
| PyPDF | PDF Text Extraction |

---

# 🏗 System Workflow

```text
              PDF Upload
                   │
                   ▼
         Extract Text (PyPDF)
                   │
                   ▼
          Split into Chunks
                   │
                   ▼
Generate Sentence Embeddings
                   │
                   ▼
        Build FAISS Index
                   │
──────────────────────────────────────
                   │
              User Query
                   │
                   ▼
     Generate Query Embedding
                   │
                   ▼
        Similarity Search
                   │
                   ▼
      Retrieve Relevant Chunks
```

---

# 📂 Project Structure

```
rag-fullstack/

│
├── backend/
│   │
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── chunking.py
│   │   ├── embedding.py
│   │   └── retrieval.py
│   │
│   ├── routes/
│   │   ├── upload.py
│   │   ├── query.py
│   │   └── main.py
│
└── .gitignore
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/rag-fullstack.git
```

Move into the project

```bash
cd rag-fullstack
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
uvicorn routes.main:app --reload
```

---

# 📌 API Endpoints

## Upload PDF

```http
POST /upload
```

Uploads a PDF document, extracts its text, creates embeddings, and builds the FAISS index.

---

## Query

```http
GET /query?q=your_question
```

Returns the most relevant document chunks for the provided query.

---

## Health Check

```http
GET /health
```

Returns the current API status.

---

# 🔍 Retrieval Pipeline

1. Upload a PDF document.
2. Extract text from every page.
3. Split the text into overlapping chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings in a FAISS vector index.
6. Convert the user query into an embedding.
7. Retrieve the most semantically similar chunks.

---

# 📈 Current Limitations

- Supports one uploaded document at a time.
- Uses an in-memory FAISS index.
- Retrieves relevant chunks but does not yet generate answers with an LLM.
- No persistent vector database.

---

# 🚀 Future Improvements

- Integrate Gemini/OpenAI/Llama for answer generation
- Persistent vector storage
- Support multiple PDF uploads
- Hybrid Search (Keyword + Semantic)
- Docker support
- Authentication
- Streamlit/React frontend
- Conversation memory

---

# 👨‍💻 Author

**Anamika Pandey**

AI & Machine Learning Enthusiast

Built using FastAPI, FAISS, and Sentence Transformers.
