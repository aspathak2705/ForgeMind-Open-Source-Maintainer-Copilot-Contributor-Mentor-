from storage.memory.memory_store import (
    MemoryStore,
)


class MemoryService:

    def __init__(self):

        self.store = (
            MemoryStore()
        )

    def record(
        self,
        agent: str,
        task: str,
        result: dict,
    ):

        self.store.add(
            {
                "agent": agent,
                "task": task,
                "result": result,
            }
        )

    def history(self):

        return (
            self.store.get_all()
        )

    def count(self):

        return (
            self.store.count()
        )