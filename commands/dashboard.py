from rich.console import Console
from rich.panel import Panel
from rich.table import Table


console = Console()


def show_dashboard():
    console.print()

    console.print(
        Panel.fit(
            "[bold cyan]ForgeMind[/bold cyan]\n"
            "Nemotron-Powered Open Source Maintainer Copilot",
            border_style="cyan",
        )
    )

    console.print()

    table = Table(title="Available Commands")

    table.add_column("Category", style="cyan")
    table.add_column("Command", style="green")
    table.add_column("Description")

    table.add_row("Repository", "index <path>", "Index repository files")
    table.add_row("Repository", "summary", "Repository overview")
    table.add_row("Repository", "graph", "Dependency graph")
    table.add_row("Issue", "triage", "Analyze issue reports")
    table.add_row("Issue", "explain <topic>", "Explain repository components")
    table.add_row("Contributor", "mentor <topic>", "Generate onboarding path")
    table.add_row("Maintainer", "maintain", "Repository health analysis")
    table.add_row("Intelligence", "memory", "Shared agent memory")
    table.add_row("Intelligence", "reflections", "Agent learning history")
    table.add_row("System", "doctor", "System diagnostics")
    table.add_row(
    "Maintainer",
    "review <files>",
    "Repository-aware PR review",
)

    console.print(table)

    console.print()

    console.print(
        Panel.fit(
            "[bold]Examples[/bold]\n\n"
            "forgemind index .\n"
            "forgemind explain auth\n"
            "forgemind mentor auth\n"
            "forgemind maintain",
            border_style="green",
        )
    )

    console.print()
