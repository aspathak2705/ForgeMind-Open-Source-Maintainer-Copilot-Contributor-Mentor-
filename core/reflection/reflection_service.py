from core.reflection.reflection_store import (
    ReflectionStore,
)


class ReflectionService:

    def __init__(self):

        self.store = (
            ReflectionStore()
        )

    def record(
        self,
        agent: str,
        observation: str,
        metadata: dict | None = None,
    ):

        self.store.add(
            {
                "agent": agent,
                "observation": observation,
                "metadata": metadata
                or {},
            }
        )

    def all(self):

        return (
            self.store.get_all()
        )