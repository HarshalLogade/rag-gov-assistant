from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_chat import ask
from app.retriever import get_retriever
import time

app = FastAPI(
    title="Gov Scheme AI API",
    description="AI-powered government scheme advisor",
    version="1.0"
)

# 🔥 PRELOAD EVERYTHING HERE
@app.on_event("startup")
def startup_event():
    print("🔥 Preloading model + FAISS...")
    get_retriever()
    print("✅ System ready")


class Query(BaseModel):
    question: str


@app.get("/")
def home():
    return {"status": "API running"}


@app.post("/chat")
def chat(q: Query):

    start = time.time()
    print(f"📩 Received question: {q.question}")

    answer = ask(q.question)

    print(f"✅ Answer generated in {time.time()-start:.2f} seconds")

    return {"answer": answer}