from google import genai

from src.config import GEMINI_API_KEY, GENERATION_MODEL

client = genai.Client(api_key=GEMINI_API_KEY)


def build_context(retrieved_chunks: list[dict]) -> str:
    context_parts = []

    for i, chunk in enumerate(retrieved_chunks, start=1):
        context_parts.append(
            f"[{i}] Source: {chunk['source']}\n"
            f"Text: {chunk['text']}"
        )

    return "\n\n".join(context_parts)


def generate_answer(question: str, retrieved_chunks: list[dict]) -> str:
    context = build_context(retrieved_chunks)

    prompt = f"""
You are a helpful RAG assistant.

Answer the user's question using ONLY the provided context.

If the answer is not found in the context, say:
"I don't know based on the provided documents."

Always cite the source filename in your answer.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model=GENERATION_MODEL,
        contents=prompt
    )

    return response.text