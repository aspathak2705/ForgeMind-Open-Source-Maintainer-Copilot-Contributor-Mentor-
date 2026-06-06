from storage.memory.memory_service import (
    MemoryService,
)


class AgentMemory:

    def __init__(self):

        self.memory = (
            MemoryService()
        )

    def remember(
        self,
        agent: str,
        task: str,
        result: dict,
    ):

        self.memory.record(
            agent,
            task,
            result,
        )