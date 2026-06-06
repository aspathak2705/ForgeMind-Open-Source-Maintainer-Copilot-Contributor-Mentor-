from rich import print

from storage.memory.memory_service import (
    MemoryService,
)

from core.reflection.reflection_service import (
    ReflectionService,
)

from core.llm.nemotron_provider import (
    NemotronProvider,
)


def doctor():

    print()

    print(
        "[bold cyan]ForgeMind Diagnostics[/bold cyan]"
    )

    print(
        "======================"
    )

    try:

        NemotronProvider()

        print(
            "[green]✓ Nemotron Available[/green]"
        )

    except Exception:

        print(
            "[red]✗ Nemotron Unavailable[/red]"
        )

    try:

        memory_count = (
            MemoryService()
            .count()
        )

        print(
            f"[green]✓ Memory Records:[/green] "
            f"{memory_count}"
        )

    except Exception:

        print(
            "[red]✗ Memory Service Error[/red]"
        )

    try:

        reflections = (
            ReflectionService()
            .all()
        )

        print(
            f"[green]✓ Reflections:[/green] "
            f"{len(reflections)}"
        )

    except Exception:

        print(
            "[red]✗ Reflection Service Error[/red]"
        )

    print()