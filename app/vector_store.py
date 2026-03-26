import os
from pathlib import Path
import sys

# Handle imports properly
try:
    from langchain_community.vectorstores import FAISS
    from langchain_community.embeddings import HuggingFaceEmbeddings
except ImportError:
    from langchain.vectorstores import FAISS
    from langchain.embeddings import HuggingFaceEmbeddings

from app.rag_loader import load_schemes

def create_vector_db():
    print("📂 Loading schemes...")
    docs = load_schemes()
    
    print("🤖 Creating embeddings...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-MiniLM-L3-v2"  # Smaller, ~50MB
    )
    
    print("💾 Building FAISS index...")
    db = FAISS.from_documents(docs, embeddings)
    
    # Save to absolute path
    current_dir = Path(__file__).resolve().parent.parent
    vector_db_path = current_dir / "vector_db"
    
    db.save_local(str(vector_db_path))
    print(f"✅ Vector DB created at: {vector_db_path}")


if __name__ == "__main__":
    create_vector_db()