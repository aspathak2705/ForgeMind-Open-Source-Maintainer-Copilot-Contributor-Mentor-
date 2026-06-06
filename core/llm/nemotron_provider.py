import os

from dotenv import load_dotenv
from openai import OpenAI

from core.llm.llm_provider import (
    LLMProvider,
)

load_dotenv()

class NemotronProvider(
    LLMProvider
):

    def __init__(self):

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv(
                "OPENROUTER_API_KEY"
            ),
        )

        self.model = (
            "nvidia/nemotron-3-super-120b-a12b:free"
        )

    def generate(
        self,
        prompt: str,
        reasoning: bool = True,
    ) -> str:

        response = (
            self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                extra_body={
                    "reasoning": {
                        "enabled": reasoning
                    }
                },
            )
        )

        return (
            response
            .choices[0]
            .message
            .content
        )

    def continue_reasoning(
        self,
        previous_messages: list,
    ) -> str:

        response = (
            self.client.chat.completions.create(
                model=self.model,
                messages=previous_messages,
                extra_body={
                    "reasoning": {
                        "enabled": True
                    }
                },
            )
        )

        return (
            response
            .choices[0]
            .message
            .content
        )