from core.llm.agent_reasoner import (
    AgentReasoner,
)


class ReleaseNotesGenerator:

    def __init__(self):

        self.reasoner = (
            AgentReasoner()
        )

    def generate(
        self,
        repository_context: dict,
    ):

        try:

            return (
                self.reasoner
                .maintainer_analysis(
                    repository_context
                )
            )

        except Exception:

            return (
                "Maintainer summary unavailable."
            )