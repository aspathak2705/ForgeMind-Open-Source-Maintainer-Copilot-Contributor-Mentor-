from rich import print
import typer

from agents.mentor_agent.mentor_agent import (
    MentorAgent,
)


def mentor(
    topic: str = typer.Argument(
        ...,
        help="Topic or repository area to learn",
    ),
):

    result = (
        MentorAgent()
        .explain_contribution_path(
            topic
        )
    )

    print()

    print(
        "[bold cyan]ForgeMind Contributor Mentor[/bold cyan]"
    )

    print()

    print(
        f"[bold]Topic:[/bold] {result['topic']}"
    )

    print()

    print(
        "[bold]Learning Path[/bold]"
    )

    learning_path = result.get(
        "learning_path",
        {}
    )

    if isinstance(
        learning_path,
        dict,
    ):

        steps = learning_path.get(
            "steps",
            []
        )

        for index, step in enumerate(
            steps,
            start=1,
        ):

            print(
                f"{index}. {step}"
            )

    else:

        print(
            learning_path
        )

    print()

    print(
        "[bold]Recommended Files[/bold]"
    )

    for file_name in result.get(
        "recommended_files",
        [],
    ):

        print(
            f"- {file_name}"
        )

    print()