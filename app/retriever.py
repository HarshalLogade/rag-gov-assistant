from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

retriever = None

def get_retriever():
    global retriever

    if retriever is None:
        print("⚙️ Loading embedding model...")

        embeddings = HuggingFaceEmbeddings(
            model_name="models/paraphrase-MiniLM-L3-v2"
        )

        print("📦 Loading FAISS index...")

        db = FAISS.load_local(
            "vector_db",
            embeddings,
            allow_dangerous_deserialization=True
        )

        print("🔎 Creating retriever...")

        retriever = db.as_retriever(search_kwargs={"k": 5})

        print("✅ Retriever ready")

    return retriever


def search(query):

    print(f"🔍 Searching vector DB for: {query}")

    r = get_retriever()

    docs = r.invoke(query)

    print(f"📄 Retrieved {len(docs)} documents")

    seen = set()
    unique = []

    for d in docs:
        name = d.metadata["id"]

        if name not in seen:
            unique.append(d)
            seen.add(name)

    return unique[:3]