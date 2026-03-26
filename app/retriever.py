import os
from pathlib import Path
import time
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

retriever = None

def get_retriever():
    global retriever

    if retriever is None:
        print("🔄 Starting retriever initialization...")
        
        # Get absolute path to vector_db
        current_dir = Path(__file__).resolve().parent.parent
        vector_db_path = current_dir / "vector_db"
        
        print(f"📂 Loading FAISS from: {vector_db_path}")
        
        # Load embedding model
        print("🔄 Loading embedding model (this takes 30-60 seconds on first request)...")
        start_time = time.time()
        
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        print(f"✅ Embedding model loaded in {time.time()-start_time:.2f} seconds")
        
        # Load FAISS index
        print("📦 Loading FAISS index...")
        start_time = time.time()
        
        db = FAISS.load_local(
            str(vector_db_path),
            embeddings,
            allow_dangerous_deserialization=True
        )
        
        print(f"✅ FAISS index loaded in {time.time()-start_time:.2f} seconds")
        
        retriever = db.as_retriever(search_kwargs={"k": 5})
        print("✅ Retriever ready!")

    return retriever


def search(query):
    print(f"🔍 Searching vector DB for: {query}")
    
    global retriever

    if retriever is None:
        get_retriever()

    start_time = time.time()
    docs = retriever.invoke(query)
    print(f"📄 Retrieved {len(docs)} documents in {time.time()-start_time:.2f} seconds")

    seen = set()
    unique = []

    for d in docs:
        name = d.metadata["id"]
        if name not in seen:
            unique.append(d)
            seen.add(name)

    return unique[:3]