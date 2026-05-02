from google import genai

from src.config import GEMINI_API_KEY, EMBEDDING_MODEL

client = genai.Client(api_key=GEMINI_API_KEY)


def embed_text(text: str) -> list[float]:
    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text
    )

    return response.embeddings[0].values


def embed_chunks(chunks: list[dict]) -> list[dict]:
    embedded_chunks = []

    for chunk in chunks:
        embedding = embed_text(chunk["text"])

        embedded_chunks.append({
            "id": chunk["id"],
            "source": chunk["source"],
            "text": chunk["text"],
            "embedding": embedding
        })

    return embedded_chunks