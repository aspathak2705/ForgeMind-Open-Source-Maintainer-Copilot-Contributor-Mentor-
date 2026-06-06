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
from commands.help import help_command
from commands.doctor import doctor
from commands.dashboard import show_dashboard
from commands.review import review
from commands.mentor import mentor


app = typer.Typer(
    help="ForgeMind - Nemotron-Powered Open Source Maintainer Copilot"
)


@app.callback(
    invoke_without_command=True
)
def main(
    ctx: typer.Context,
):
    if ctx.invoked_subcommand is None:
        show_dashboard()



app.command()(index)
app.command()(summary)
app.command()(graph)
app.command()(ask)
app.command()(review)
app.command()(mentor)


app.command()(explain)
app.command()(triage)


app.command()(maintain)


app.command()(memory)
app.command()(reflections)


app.command(name="help")(help_command)
app.command()(doctor)


if __name__ == "__main__":
    app()
