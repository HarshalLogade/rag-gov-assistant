from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_chat import ask
from app.retriever import get_retriever
import time
import uvicorn
import os
import sys
import asyncio

app = FastAPI(
    title="Gov Scheme AI API",
    description="AI-powered government scheme advisor",
    version="1.0"
)

class Query(BaseModel):
    question: str

# Force pre-load on startup
print("🚀 Starting application...")
print("🔄 Attempting to pre-load models...")
sys.stdout.flush()

try:
    # Try to load with timeout
    import signal
    
    def timeout_handler(signum, frame):
        raise TimeoutError("Model loading timed out after 60 seconds")
    
    # Set timeout (Unix only)
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(60)
    
    retriever = get_retriever()
    
    signal.alarm(0)  # Cancel timeout
    print("✅ Models pre-loaded successfully on startup!")
    
except TimeoutError:
    print("⚠️ Model loading timed out. Will load on first request instead.")
except Exception as e:
    print(f"⚠️ Could not pre-load models: {e}")
    print("Models will load on first request")

sys.stdout.flush()

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
    sys.stdout.flush()

    try:
        answer = ask(q.question)
        print(f"✅ Answer generated in {time.time()-start:.2f} seconds")
        sys.stdout.flush()
        return {"answer": answer}
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.stdout.flush()
        return {"error": str(e)}, 500