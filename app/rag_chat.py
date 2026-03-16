import google.generativeai as genai
from app.retriever import search
import time

def ask(question):

    print("🔎 Retrieving documents...")
    docs = search(question)

    context = "\n\n".join([d.page_content for d in docs])

    print("🤖 Sending request to Gemini...")

    start = time.time()

    response = model.generate_content(
        f"""
        Use the following context to answer.

        {context}

        Question: {question}
        """
    )

    print(f"✨ Gemini responded in {time.time()-start:.2f}s")

    return response.text