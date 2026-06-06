from rich import print

from core.services.maintainer_service import (
    MaintainerService,
)


def maintain():

    result = (
        MaintainerService()
        .analyze()
    )

    print()
    print(
        "[bold]Repository Health[/bold]"
    )

    for key, value in result[
        "health"
    ].items():

        print(
            f"{key}: {value}"
        )

    print()
    print(
        "[bold]Hotspots[/bold]"
    )

    for hotspot in result[
        "hotspots"
    ]:

        print(
            f"- {hotspot['file']} "
            f"(impact={hotspot['impact_score']})"
        )

    print()
    print(
        "[bold]Nemotron Summary[/bold]"
    )

    print(
        result["summary"]
    )