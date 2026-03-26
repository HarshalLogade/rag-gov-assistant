import os
from pathlib import Path
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from app.rag_loader import load_schemes

def create_vector_db():
    docs = load_schemes()
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db = FAISS.from_documents(docs, embeddings)
    
    # Save to absolute path
    current_dir = Path(__file__).resolve().parent.parent
    vector_db_path = current_dir / "vector_db"
    
    db.save_local(str(vector_db_path))
    print(f"✅ Vector DB created at: {vector_db_path}")


if __name__ == "__main__":
    create_vector_db()