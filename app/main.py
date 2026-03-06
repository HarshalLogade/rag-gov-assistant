from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_chat import ask

app = FastAPI(
    title="Gov Scheme AI API",
    description="AI-powered government scheme advisor",
    version="1.0"
)

class Query(BaseModel):
    question: str


@app.get("/")
def home():
    return {"status": "API running"}


@app.post("/chat")
def chat(q: Query):

    answer = ask(q.question)

    return {"answer": answer}