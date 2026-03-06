import os
from dotenv import load_dotenv
import google.generativeai as genai
from retriever import search

# load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def ask(question):

    docs = search(question)

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are an assistant that helps farmers find government schemes.

Answer ONLY using the context below.

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(prompt)

    return response.text


if __name__ == "__main__":

    while True:

        q = input("\nAsk: ")

        ans = ask(q)

        print("\nAnswer:\n", ans)