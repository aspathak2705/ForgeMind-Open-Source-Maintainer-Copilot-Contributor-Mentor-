import typer

from commands.graph import graph
from commands.index import index
from commands.summary import summary
from commands.ask import ask
from commands.explain import explain


app = typer.Typer()

app.command()(index)
app.command()(summary)
app.command()(graph)
app.command()(ask)
app.command()(explain)

if __name__ == "__main__":
    app()
