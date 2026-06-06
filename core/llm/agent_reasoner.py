from core.llm.nemotron_provider import (
    NemotronProvider,
)

from core.llm.prompt_builder import (
    PromptBuilder,
)


class AgentReasoner:

    def __init__(self):

        self.llm = (
            NemotronProvider()
        )

    def analyze_issue(
        self,
        issue_text: str,
        repository_context: dict,
    ):

        prompt = (
            PromptBuilder
            .issue_analysis_prompt(
                issue_text,
                repository_context,
            )
        )

        return self.llm.generate(
            prompt
        )

    def mentor_guidance(
        self,
        issue_context: dict,
        repository_context: dict,
    ):

        prompt = (
            PromptBuilder
            .mentor_prompt(
                issue_context,
                repository_context,
            )
        )

        return self.llm.generate(
            prompt
        )

    def maintainer_analysis(
        self,
        repository_context: dict,
    ):

        prompt = (
            PromptBuilder
            .maintainer_prompt(
                repository_context
            )
        )

        return self.llm.generate(
            prompt
        )