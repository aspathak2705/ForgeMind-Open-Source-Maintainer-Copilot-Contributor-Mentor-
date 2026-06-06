import typer

from commands.graph import graph
from commands.index import index
from commands.summary import summary
from commands.ask import ask
from commands.explain import explain
from commands.triage import triage
from commands.maintain import maintain
from commands.memory import memory
from commands.reflection import reflections


app = typer.Typer()

app.command()(index)
app.command()(summary)
app.command()(graph)
app.command()(ask)
app.command()(explain)
app.command()(triage)
app.command()(maintain)
app.command()(memory)
app.command()(reflections)

if __name__ == "__main__":
    app()
