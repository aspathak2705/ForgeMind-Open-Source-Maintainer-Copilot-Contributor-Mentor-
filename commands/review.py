import typer

from rich import print

from core.services.pr_review_service import (
    PRReviewService,
)


def review(
    files: list[str] = typer.Argument(
        ...
    ),
):

    result = (
        PRReviewService()
        .review(files)
    )

    print()
    print(
        "[bold cyan]ForgeMind PR Review[/bold cyan]"
    )
    print()

    print(result)