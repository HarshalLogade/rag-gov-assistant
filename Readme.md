# Government Scheme RAG Chatbot

An AI-powered chatbot that helps users discover relevant **government schemes for farmers** using natural language questions.

The system uses **Retrieval-Augmented Generation (RAG)** to search a structured dataset of government schemes and generate helpful responses using an AI model.

Users can ask questions like:

```
solar pump subsidy
pension scheme for farmers
loan schemes for agriculture
organic farming support
```

The chatbot retrieves relevant schemes and generates a clear answer.

---

# Project Overview

This project combines:

- Semantic search
- Vector databases
- AI language models
- API backend

The system retrieves relevant government schemes from a dataset and generates answers using an AI model.

Example:

User query:

```
solar pump subsidy
```

Response:

```
PM-KUSUM provides subsidy support for solar water pumps for farmers.
The scheme offers about 60% subsidy through central and state governments.
```

---

# System Architecture

```
User Question
      ↓
Embedding Model
      ↓
FAISS Vector Database
      ↓
Retrieve Relevant Schemes
      ↓
Gemini AI Model
      ↓
Generated Answer
```

---

# Features

- Natural language queries
- Semantic search using embeddings
- AI-generated responses
- Government scheme dataset
- REST API backend
- Ready for mobile app integration

---

# Tech Stack

Backend

- Python
- FastAPI

AI / RAG

- Sentence Transformers
- FAISS Vector Database
- Google Gemini API

Tools

- Postman (API testing)

---

# Project Structure

```
rag-gov-assistant
│
├── schemes.json
├── requirements.txt
│
├── rag_loader.py
├── vector_store.py
├── retriever.py
├── rag_chat.py
├── main.py
├── test_search.py
│
└── vector_db/
```

---

# Installation

Clone the repository

```
git clone https://github.com/your-repo/rag-gov-assistant.git
cd rag-gov-assistant
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Setup API Key

Set your Gemini API key.

Windows PowerShell

```
$env:GEMINI_API_KEY="your_api_key"
```

---

# Build Vector Database

Run once to create embeddings.

```
python vector_store.py
```

This converts the scheme dataset into searchable vectors.

---

# Test Retrieval

```
python test_search.py
```

This tests whether the system retrieves the correct schemes.

---

# Run Chatbot (CLI)

```
python rag_chat.py
```

Example query

```
Ask: solar pump subsidy
```

---

# Run API Server

Start the backend API

```
uvicorn app.main:app --reload
```

Server will run at

```
http://127.0.0.1:8000
```

---

# API Endpoint

POST `/chat`

Example request

```
{
 "question": "solar pump subsidy"
}
```

Example response

```
{
 "answer": "PM-KUSUM provides subsidy support for solar water pumps..."
}
```

---

# API Testing

The API can be tested using **Postman**.

Example queries used during testing:

- solar pump subsidy
- pension scheme for farmers
- loan schemes for farmers
- organic farming schemes

---

# Future Improvements

- Metadata filtering (state, crops, eligibility)
- Multilingual support (Hindi / Marathi)
- Mobile app integration
- Improved scheme recommendation logic
- Deployment to cloud

---

# Deployment Plan

Next steps for the project:

1. Deploy backend API to cloud server
2. Generate secure API keys
3. Integrate API with Flutter mobile application

---

# License

This project is for educational and development purposes.

---
