import os
from pathlib import Path
import time
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

retriever = None

def get_retriever():
    global retriever

    if retriever is None:
        print("🔄 Starting retriever initialization...", flush=True)
        
        current_dir = Path(__file__).resolve().parent.parent
        vector_db_path = current_dir / "vector_db"
        
        print(f"📂 Loading FAISS from: {vector_db_path}", flush=True)
        
        print("🔄 Loading embedding model (this takes 30-60 seconds on first request)...", flush=True)
        start_time = time.time()
        
        try:
            embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )
            print(f"✅ Embedding model loaded in {time.time()-start_time:.2f} seconds", flush=True)
        except Exception as e:
            print(f"❌ Error loading embeddings: {e}", flush=True)
            raise
        
        print("📦 Loading FAISS index...", flush=True)
        start_time = time.time()
        
        try:
            db = FAISS.load_local(
                str(vector_db_path),
                embeddings,
                allow_dangerous_deserialization=True
            )
            print(f"✅ FAISS index loaded in {time.time()-start_time:.2f} seconds", flush=True)
        except Exception as e:
            print(f"❌ Error loading FAISS: {e}", flush=True)
            raise

        retriever = db.as_retriever(search_kwargs={"k": 5})
        print("✅ Retriever ready!", flush=True)

    return retriever


def search(query):
    print(f"🔍 Searching vector DB for: {query}", flush=True)
    
    global retriever

    if retriever is None:
        get_retriever()

    start_time = time.time()
    docs = retriever.invoke(query)
    print(f"📄 Retrieved {len(docs)} documents in {time.time()-start_time:.2f} seconds", flush=True)

    seen = set()
    unique = []

    for d in docs:
        name = d.metadata["id"]
        if name not in seen:
            unique.append(d)
            seen.add(name)

    return unique[:3]