from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(
    search_kwargs={
        "k":5
    }
)


def search(query):

    docs = retriever.invoke(query)

    seen = set()
    unique = []

    for d in docs:
        name = d.metadata["id"]

        if name not in seen:
            unique.append(d)
            seen.add(name)

    return unique[:3]