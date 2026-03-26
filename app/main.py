from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_chat import ask
import time
import os
import sys

app = FastAPI(
    title="Gov Scheme AI API",
    description="AI-powered government scheme advisor",
    version="1.0"
)

class Query(BaseModel):
    question: str

# Remove all print statements at module level - they can cause issues
# Just log after startup

@app.on_event("startup")
async def startup_event():
    print("🚀 Application started successfully!", flush=True)
    print("💡 First request will load models (30-90 seconds)", flush=True)
    print("💡 Subsequent requests will be fast", flush=True)

@app.get("/")
def home():
    return {"status": "API running", "port": os.environ.get("PORT", "10000")}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/chat")
def chat(q: Query):
    start = time.time()
    print(f"📩 Received question: {q.question}", flush=True)
    
    try:
        answer = ask(q.question)
        print(f"✅ Answer generated in {time.time()-start:.2f} seconds", flush=True)
        return {"answer": answer}
    except Exception as e:
        print(f"❌ Error: {e}", flush=True)
        return {"error": str(e)}, 500