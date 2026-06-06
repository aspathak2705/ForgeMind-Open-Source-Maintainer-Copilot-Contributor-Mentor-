from core.llm.agent_reasoner import (
    AgentReasoner,
)


class RecommendationEngine:

    def __init__(self):

        self.reasoner = (
            AgentReasoner()
        )

    def generate(
        self,
        severity: str,
        files: list[str],
        issue_text: str,
        classes: list[str] | None = None,
    ):

        if not files:

            return (
                "Gather more information"
            )

        repository_context = {
            "severity": severity,
            "files": files,
            "classes": classes or [],
        }

        try:

            return (
                self.reasoner
                .analyze_issue(
                    issue_text,
                    repository_context,
                )
            )

        except Exception:

            return (
                f"Investigate {files[0]}"
            )