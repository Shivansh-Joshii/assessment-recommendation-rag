from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from retriever import search_assessments
from llm import generate_response

app = FastAPI(
    title="SHL Assessment Recommendation Bot",
    version="1.0.0"
)


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


@app.get("/")
def home():
    return {
        "message": "SHL Assessment Recommendation Bot is running."
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    # Latest recruiter query
    query = request.messages[-1].content

    # Semantic Search
    recommendations = search_assessments(query)

    # AI Explanation
    reply = generate_response(query, recommendations)

    return {
        "reply": reply,
        "recommendations": recommendations
    }