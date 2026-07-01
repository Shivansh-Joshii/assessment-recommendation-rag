import requests
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

url = "https://tcp-us-prod-rnd.shl.com/voiceRater/shl-ai-hiring/shl_product_catalog.json"

response = requests.get(url)

catalog = json.loads(response.text, strict=False)

with open("data/catalog.json", "w") as file:
    json.dump(catalog, file)

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = []

for assesment in catalog:

    text = (
        assesment["name"] + " " +
        assesment["description"] + " " +
        " ".join(assesment["job_levels"]) + " " +
        " ".join(assesment["keys"])
    )

    embedding = model.encode(text)

    embeddings.append(embedding)

embeddings = np.array(embeddings)

embeddings = embeddings.astype("float32")

index = faiss.IndexFlatL2(384)

index.add(embeddings)

faiss.write_index(index, "data/shl_index.faiss")

print("Index Created Successfully")