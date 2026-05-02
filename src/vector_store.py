import faiss
import numpy as np


def build_index(embedded_chunks: list[dict]):
    embeddings = [chunk["embedding"] for chunk in embedded_chunks]

    vectors = np.array(embeddings).astype("float32")

    faiss.normalize_L2(vectors)

    dimension = vectors.shape[1]

    index = faiss.IndexFlatIP(dimension)
    index.add(vectors)

    return index


def search_index(
    query_embedding: list[float],
    index,
    embedded_chunks: list[dict],
    top_k: int = 3
) -> list[dict]:

    query_vector = np.array([query_embedding]).astype("float32")

    faiss.normalize_L2(query_vector)

    scores, indices = index.search(query_vector, top_k)

    results = []

    for score, idx in zip(scores[0], indices[0]):
        chunk = embedded_chunks[idx]

        results.append({
            "id": chunk["id"],
            "source": chunk["source"],
            "text": chunk["text"],
            "score": float(score)
        })

    return results