from abc import ABC, abstractmethod


class LLMProvider(ABC):

    @abstractmethod
    def generate(
        self,
        prompt: str,
        reasoning: bool = True,
    ) -> str:
        pass