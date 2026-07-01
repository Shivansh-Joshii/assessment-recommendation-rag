import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

with open("data/catalog.json", "r") as file:
    catalog = json.load(file)

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("data/shl_index.faiss")


def search_assessments(query, top_k=5):

    query_embedding = model.encode(query)

    query_embedding = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for i in indices[0]:

        results.append({
            "name": catalog[i]["name"],
            "description": catalog[i]["description"],
            "url": catalog[i]["link"],
            "job_levels": catalog[i]["job_levels"],
            "keys": catalog[i]["keys"],
            "duration": catalog[i]["duration"],
            "remote": catalog[i]["remote"]
        })

    return results
