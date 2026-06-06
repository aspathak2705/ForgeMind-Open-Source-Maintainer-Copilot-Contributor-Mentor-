from core.repository.impact_analyzer import (
    ImpactAnalyzer,
)

from core.llm.agent_reasoner import (
    AgentReasoner,
)

from storage.memory.agent_memory import (
    AgentMemory,
)

from core.reflection.reflection_service import (
    ReflectionService,
)


class PRReviewAgent:

    def __init__(self):

        self.impact = (
            ImpactAnalyzer()
        )

        self.reasoner = (
            AgentReasoner()
        )

        self.memory = (
            AgentMemory()
        )

        self.reflection = (
            ReflectionService()
        )

    def review(
        self,
        files: list[str],
    ):

        impact_data = (
            self.impact.analyze_all()
        )

        relevant = []

        for file_name in files:

            for item in impact_data.values():

                if (
                    item["file"]
                    == file_name
                ):

                    relevant.append(
                        item
                    )

        context = {
            "modified_files": files,
            "impact_analysis": relevant,
        }

        report = (
            self.reasoner.review_pr(
                context
            )
        )

        self.memory.remember(
            "pr_review_agent",
            "pr_review",
            {
                "files": files,
                "reviewed": len(
                    files
                ),
            },
        )

        self.reflection.record(
            "pr_review_agent",
            "PR review completed",
            {
                "files": len(
                    files
                )
            },
        )

        return report