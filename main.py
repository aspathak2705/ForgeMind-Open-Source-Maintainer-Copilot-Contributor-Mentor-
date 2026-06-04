import typer

from commands.graph import graph
from commands.index import index
from commands.summary import summary

app = typer.Typer()

app.command()(index)
app.command()(summary)
app.command()(graph)

if __name__ == "__main__":
    app()
