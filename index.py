from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.ingest import load_documents
from src.retriever import index_chunks

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

def main():
    print("Loading documents from ./data ...")
    pages = load_documents("./data")
    
    if not pages:
        print("ERROR: No documents found in ./data folder. Add your PDFs/TXTs first.")
        return

    sources = set(p["source"] for p in pages)
    print(f"Loaded {len(pages)} pages from {len(sources)} files: {sources}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " "]
    )

    chunks = []
    for page in pages:
        splits = splitter.split_text(page["text"])
        for split in splits:
            chunks.append({
                "text": split,
                "source": page["source"],
                "page": page["page"]
            })

    print(f"Created {len(chunks)} chunks. Now embedding and indexing...")
    index_chunks(chunks)
    print("\nDone! Your vector database is ready.")
    print("Now run: python main.py")

if __name__ == "__main__":
    main()