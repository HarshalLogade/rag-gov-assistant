import os
from pathlib import Path

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
        # Get absolute path to vector_db
        current_dir = Path(__file__).resolve().parent.parent
        vector_db_path = current_dir / "vector_db"
        
        print(f"📂 Loading FAISS from: {vector_db_path}")
        
        # Use the SAME embedding model as vector_store.py
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        print("📦 Loading FAISS index...")

        db = FAISS.load_local(
            str(vector_db_path),
            embeddings,
            allow_dangerous_deserialization=True
        )

        retriever = db.as_retriever(search_kwargs={"k": 5})
        print("✅ Retriever ready")

    return retriever


def search(query):
    print(f"🔍 Searching vector DB for: {query}")

    global retriever

    if retriever is None:
        get_retriever()

    docs = retriever.invoke(query)

    print(f"📄 Retrieved {len(docs)} documents")

    seen = set()
    unique = []

    for d in docs:
        name = d.metadata["id"]
        if name not in seen:
            unique.append(d)
            seen.add(name)

    return unique[:3]