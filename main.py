from src.retriever import retrieve
from src.generator import generate_answer
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()

def main():
    console.print(Panel(
        "[bold green]RAG Document Q&A Bot[/bold green]\n"
        "Ask questions about your documents.\n"
        "Type [bold]quit[/bold] to exit.",
        expand=False
    ))

    while True:
        try:
            query = input("\n[Question] > ").strip()
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

        if query.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break
        if not query:
            continue

        console.print("[dim]Searching documents...[/dim]")
        chunks = retrieve(query, k=5)

        console.print(f"[dim]Found {len(chunks)} relevant chunks. Generating answer...[/dim]")
        answer = generate_answer(query, chunks)

        console.print(Panel(Markdown(answer), title="[bold blue]Answer[/bold blue]", border_style="blue"))

        console.print("\n[dim yellow]--- Retrieved source chunks ---[/dim yellow]")
        for i, c in enumerate(chunks, 1):
            console.print(f"[dim]{i}. {c['source']} (page {c['page']}): {c['text'][:150]}...[/dim]")

if __name__ == "__main__":
    main()