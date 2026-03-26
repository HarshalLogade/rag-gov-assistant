from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_chat import ask
import time
import os

app = FastAPI(
    title="Gov Scheme AI API",
    description="AI-powered government scheme advisor",
    version="1.0"
)

class Query(BaseModel):
    question: str

print("🚀 Starting application...")
print("💡 First request will take 30-90 seconds to load models")
print("💡 Subsequent requests will be fast")

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
    
    # Just call ask - no timeout wrapper
    answer = ask(q.question)
    
    print(f"✅ Answer generated in {time.time()-start:.2f} seconds")
    return {"answer": answer}