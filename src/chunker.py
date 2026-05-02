def chunk_documents(documents,chunk_size = 500 ,overlap = 100):
    chunks = []

    for doc in documents:
        text = doc["text"]
        source = doc["source"]

        start = 0
        chunk_index = 0

        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]

            chunks.append(
                {
                "id": f"{source}_chunk_{chunk_index}",
                "source": source,
                "text": chunk_text
                })

            chunk_index +=1 
            start += chunk_size - overlap
    return chunks
