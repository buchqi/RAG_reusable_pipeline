from src.document_loader import load_documents
from src.chunker import chunk_documents
from src.embedder import embed_chunks, embed_text
from src.vector_store import build_index, search_index
from src.rag_pipeline import generate_answer

docs = load_documents("data/docs")
chunks = chunk_documents(docs, chunk_size=500, overlap=100)
embedded_chunks = embed_chunks(chunks)

index = build_index(embedded_chunks)

questions = [
    "What is the refund window?",
    "Can I refund a downloaded digital product?",
    "Can I return food?"
]

for question in questions:
    print("\nQUESTION:", question)

    query_embedding = embed_text(question)
    retrieved_chunks = search_index(query_embedding, index, embedded_chunks, top_k=2)

    print("Retrieved chunks:")
    for chunk in retrieved_chunks:
        print(chunk["source"], chunk["score"])

    answer = generate_answer(question, retrieved_chunks)

    print("ANSWER:")
    print(answer)
    print("=" * 60)

query_embedding = embed_text(question)
retrieved_chunks = search_index(query_embedding, index, embedded_chunks, top_k=2)

print("\nRetrieved chunks:")
for chunk in retrieved_chunks:
    print(chunk["source"], chunk["score"])

answer = generate_answer(question, retrieved_chunks)

print("\nAnswer:")
print(answer)