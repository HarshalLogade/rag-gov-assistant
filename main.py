from fastapi import FastAPI
from pydantic import BaseModel
from rag_chat import ask

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/chat")

def chat(q: Query):

    answer = ask(q.question)

    return {"answer": answer}