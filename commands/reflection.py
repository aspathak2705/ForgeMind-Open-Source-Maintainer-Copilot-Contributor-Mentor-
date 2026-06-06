from rich import print

from core.reflection.reflection_service import (
    ReflectionService,
)


def reflections():

    service = (
        ReflectionService()
    )

    print()

    for reflection in (
        service.all()
    ):

        print(reflection)