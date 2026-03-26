import os
from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_chat import ask
import time
import uvicorn

app = FastAPI(
    title="Gov Scheme AI API",
    description="AI-powered government scheme advisor",
    version="1.0"
)

class Query(BaseModel):
    question: str

@app.get("/")
def home():
    return {"status": "API running", "port": os.environ.get("PORT", "8000")}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/chat")
def chat(q: Query):
    start = time.time()
    print(f"📩 Received question: {q.question}")

    answer = ask(q.question)

    print(f"✅ Answer generated in {time.time()-start:.2f} seconds")

    return {"answer": answer}

# For direct execution
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)