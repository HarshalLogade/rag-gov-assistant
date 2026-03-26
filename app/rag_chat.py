import os
import time
from dotenv import load_dotenv
import google.generativeai as genai
from app.retriever import search

# load env
load_dotenv()

# configure API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# initialize model
model = genai.GenerativeModel("gemini-2.5-flash")

def ask(question):
    print("🔎 Retrieving documents...")
    docs = search(question)

    context = "\n\n".join([d.page_content for d in docs])

    print("🤖 Sending request to Gemini...")

    start = time.time()

    response = model.generate_content(
        f"""
        You are a helpful assistant for Indian government schemes for farmers.
        Use the following context to answer the question accurately.
        If the context doesn't contain the answer, say so politely.

        Context:
        {context}

        Question: {question}

        Answer:
        """
    )

    print(f"✨ Gemini responded in {time.time()-start:.2f}s")

    return response.text