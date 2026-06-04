import typer

from commands.graph import graph
from commands.index import index
from commands.summary import summary
from commands.ask import ask

app = typer.Typer()

app.command()(index)
app.command()(summary)
app.command()(graph)
app.command()(ask)

if __name__ == "__main__":
    app()
