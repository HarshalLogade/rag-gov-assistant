from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from rag_loader import load_schemes

def create_vector_db():
    docs = load_schemes()
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db = FAISS.from_documents(docs, embeddings)
    db.save_local("vector_db")
    print("Vector DB created")


if __name__ == "__main__":
    create_vector_db()