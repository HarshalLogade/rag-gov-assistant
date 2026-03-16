from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

retriever = None

def get_retriever():
    global retriever

    if retriever is None:

        embeddings = HuggingFaceEmbeddings(
            model_name="models/paraphrase-MiniLM-L3-v2"
        )

        db = FAISS.load_local(
            "vector_db",
            embeddings,
            allow_dangerous_deserialization=True
        )

        retriever = db.as_retriever(search_kwargs={"k": 5})

    return retriever


def search(query):

    r = get_retriever()

    docs = r.invoke(query)

    seen = set()
    unique = []

    for d in docs:
        name = d.metadata["id"]

        if name not in seen:
            unique.append(d)
            seen.add(name)

    return unique[:3]