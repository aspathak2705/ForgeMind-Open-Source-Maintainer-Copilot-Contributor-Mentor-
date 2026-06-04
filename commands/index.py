import typer

from core.indexer import RepositoryIndexer


def index(path: str = typer.Argument(".")) -> None:
    indexer = RepositoryIndexer()
    count = indexer.index(path)
    typer.echo(f"Indexed {count} Python files")
