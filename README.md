# RAG Document Q&A Bot

A command-line Retrieval-Augmented Generation (RAG) system that answers natural language questions using only information from a local collection of documents (PDF, TXT, DOCX), with clear source citations for every answer.

## Tech Stack

| Component | Library | Version |
|---|---|---|
| PDF parsing | PyMuPDF (fitz) | 1.24.x |
| DOCX parsing | python-docx | 1.1.x |
| Text chunking | langchain-text-splitters | 0.2.x |
| Embedding model | sentence-transformers (all-MiniLM-L6-v2) | 3.0.x |
| Vector database | ChromaDB | 0.5.x |
| LLM (answer generation) | Ollama (llama3.2, local) | 0.6.2 (Python client) |
| CLI interface | rich | 13.x |
| Environment config | python-dotenv | 1.0.x |
| Language | Python | 3.11+ |

## Architecture Overview