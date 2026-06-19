import fitz
from pathlib import Path
from docx import Document as DocxDocument

def load_documents(data_dir: str) -> list[dict]:
    docs = []
    for path in Path(data_dir).iterdir():
        if path.suffix == ".pdf":
            docs.extend(_load_pdf(path))
        elif path.suffix == ".txt":
            docs.extend(_load_txt(path))
        elif path.suffix == ".docx":
            docs.extend(_load_docx(path))
    return docs

def _load_pdf(path: Path) -> list[dict]:
    doc = fitz.open(str(path))
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        if text:
            pages.append({"text": text, "source": path.name, "page": i + 1})
    return pages

def _load_txt(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8").strip()
    return [{"text": text, "source": path.name, "page": 1}]

def _load_docx(path: Path) -> list[dict]:
    doc = DocxDocument(str(path))
    text = "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    return [{"text": text, "source": path.name, "page": 1}]