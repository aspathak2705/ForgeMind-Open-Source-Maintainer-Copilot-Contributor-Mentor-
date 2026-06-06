from rich import print

from storage.memory.memory_service import (
    MemoryService,
)


def memory():

    service = (
        MemoryService()
    )

    print()

    print(
        f"Stored Records: "
        f"{service.count()}"
    )

    print()

    for record in (
        service.history()
    ):

        print(record)