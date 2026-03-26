import os
from pathlib import Path
import time
import sys

# Handle imports properly
try:
    from langchain_community.vectorstores import FAISS
    from langchain_community.embeddings import HuggingFaceEmbeddings
except ImportError:
    from langchain.vectorstores import FAISS
    from langchain.embeddings import HuggingFaceEmbeddings

retriever = None

def get_retriever():
    global retriever

    if retriever is None:
        print("🔄 Starting retriever initialization...")
        
        # Get absolute path to vector_db
        current_dir = Path(__file__).resolve().parent.parent
        vector_db_path = current_dir / "vector_db"
        
        print(f"📂 Loading FAISS from: {vector_db_path}")
        
        # Use the SAME embedding model as vector_store.py
        print("🔄 Loading embedding model...")
        start_time = time.time()
        
        try:
            embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/paraphrase-MiniLM-L3-v2",
                model_kwargs={'device': 'cpu'},
                encode_kwargs={'normalize_embeddings': False}
            )
            print(f"✅ Embedding model loaded in {time.time()-start_time:.2f} seconds")
        except Exception as e:
            print(f"❌ Error loading embeddings: {e}")
            sys.stdout.flush()
            raise

        print("📦 Loading FAISS index...")
        start_time = time.time()
        
        try:
            db = FAISS.load_local(
                str(vector_db_path),
                embeddings,
                allow_dangerous_deserialization=True
            )
            print(f"✅ FAISS index loaded in {time.time()-start_time:.2f} seconds")
        except Exception as e:
            print(f"❌ Error loading FAISS: {e}")
            sys.stdout.flush()
            raise

        retriever = db.as_retriever(search_kwargs={"k": 5})
        print("✅ Retriever ready")
        sys.stdout.flush()

    return retriever


def search(query):
    print(f"🔍 Searching vector DB for: {query}")
    sys.stdout.flush()

    global retriever

    if retriever is None:
        get_retriever()

    start_time = time.time()
    docs = retriever.invoke(query)
    print(f"📄 Retrieved {len(docs)} documents in {time.time()-start_time:.2f} seconds")
    sys.stdout.flush()

    seen = set()
    unique = []

    for d in docs:
        name = d.metadata["id"]
        if name not in seen:
            unique.append(d)
            seen.add(name)

    return unique[:3]