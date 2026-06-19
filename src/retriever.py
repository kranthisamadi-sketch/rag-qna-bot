import chromadb
from src.embedder import embed_texts

_client = None
_collection = None

def get_collection(persist_dir: str = "./chroma_store"):
    global _client, _collection
    if _collection is None:
        _client = chromadb.PersistentClient(path=persist_dir)
        _collection = _client.get_or_create_collection("documents")
    return _collection

def index_chunks(chunks: list[dict], persist_dir: str = "./chroma_store"):
    col = get_collection(persist_dir)
    texts = [c["text"] for c in chunks]
    embeddings = embed_texts(texts)
    ids = [f"chunk_{i}" for i in range(len(chunks))]
    metadatas = [{"source": c["source"], "page": c["page"]} for c in chunks]
    col.add(ids=ids, embeddings=embeddings, documents=texts, metadatas=metadatas)
    print(f"Indexed {len(chunks)} chunks.")

def retrieve(query: str, k: int = 5) -> list[dict]:
    col = get_collection()
    query_embedding = embed_texts([query])[0]
    results = col.query(query_embeddings=[query_embedding], n_results=k)
    chunks = []
    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        chunks.append({"text": doc, "source": meta["source"], "page": meta["page"]})
    return chunks