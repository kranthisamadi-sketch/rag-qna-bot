import ollama

SYSTEM_PROMPT = """You are a document Q&A assistant. Answer ONLY using the provided context.
If the answer is not in the context, say exactly: "I could not find this information in the documents."
Always end your answer with a Sources: line listing the filenames and page numbers used."""

def generate_answer(query: str, chunks: list[dict]) -> str:
    context = "\n\n---\n\n".join(
        f"[Source: {c['source']}, page {c['page']}]\n{c['text']}"
        for c in chunks
    )
    user_message = f"Context:\n{context}\n\nQuestion: {query}"

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
    )
    return response["message"]["content"]