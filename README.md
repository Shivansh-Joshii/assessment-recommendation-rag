# Assessment Recommendation RAG

An AI-powered Assessment Recommendation System built using Retrieval-Augmented Generation (RAG), Sentence Transformers, FAISS, FastAPI, and Groq Llama 3.3.

Instead of relying on traditional keyword matching, the system performs **semantic search** using Sentence Transformers and FAISS to retrieve the most relevant assessments, then uses the **Groq Llama 3.3** Large Language Model to generate professional recommendations.

---

## Features

- Semantic search using Sentence Transformers
- FAISS vector database for fast similarity search
- AI-generated recommendations using Groq Llama 3.3
- FastAPI REST API
- JSON response for easy frontend integration
- Modular architecture with separate indexing, retrieval, and generation layers

---

## Architecture

```
                    Recruiter Query
                           │
                           ▼
                     FastAPI (app.py)
                           │
                           ▼
              Retriever (retriever.py)
                           │
                           ▼
      Sentence Embeddings + FAISS Search
                           │
                           ▼
             Top Matching Assessments
                           │
                           ▼
                  Groq LLM (llm.py)
                           │
                           ▼
          AI Generated Recommendation
                           │
                           ▼
                     JSON Response
```

---

## Project Structure

```
assessment-recommendation-rag/

│── app.py
│── build_index.py
│── retriever.py
│── llm.py
│── config.py
│── requirements.txt
│── README.md
│
├── data/
│   ├── catalog.json
│   └── shl_index.faiss
```

---

## Tech Stack

- Python
- FastAPI
- Sentence Transformers
- FAISS
- Groq API
- NumPy
- Requests
- Pydantic

---

## Installation

Clone the repository

```bash
git clone https://github.com/Shivansh-Joshii/assessment-recommendation-rag.git

cd assessment-recommendation-rag
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GROQ_API_KEY=your_groq_api_key
```

If required, build the vector database

```bash
python build_index.py
```

Run the FastAPI server

```bash
uvicorn app:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### POST `/chat`

### Example Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring Backend Java Developers with Spring Boot experience"
    }
  ]
}
```

### Example Response

```json
{
  "reply": "...",
  "recommendations": [
    {
      "name": "Spring (New)",
      "description": "...",
      "duration": "9 minutes",
      "url": "..."
    }
  ]
}
```

---

## How It Works

1. Download the assessment catalog.
2. Convert assessment information into sentence embeddings.
3. Store embeddings inside a FAISS vector index.
4. Receive recruiter hiring requirements.
5. Convert the recruiter query into an embedding.
6. Retrieve the most semantically similar assessments.
7. Send the recruiter query and retrieved assessments to the Groq LLM.
8. Generate a professional explanation for the recommendations.
9. Return both the explanation and assessment details as a JSON response.

---

## Why RAG?

Traditional keyword search often misses relevant assessments when different terminology is used.

For example:

**Recruiter Query**

```
Backend Developer
```

may not contain the exact keywords present in an assessment.

Semantic search converts both recruiter requirements and assessment descriptions into embeddings, allowing similar meanings to match even when the wording differs.

The Large Language Model is used **after retrieval** to explain the recommendations instead of performing the search itself.

---

## Future Improvements

- Conversation memory
- Hybrid Search (Keyword + Semantic Search)
- Assessment reranking
- Docker support
- Cloud deployment
- Frontend interface
- Multi-turn recruiter conversations

---

## Author

**Shivansh Joshi**

B.Tech Artificial Intelligence & Data Science

GitHub: https://github.com/Shivansh-Joshii
