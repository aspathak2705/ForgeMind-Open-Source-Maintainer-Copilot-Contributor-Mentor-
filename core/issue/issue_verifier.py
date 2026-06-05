from agents.repository_agent.repository_agent import RepositoryAgent
from core.issue.confidence_calculator import ConfidenceCalculator


class IssueVerifier:

    def __init__(self):
        self.repository_agent = RepositoryAgent()
        self.confidence = ConfidenceCalculator()

    def verify(
        self,
        issue_text,
        files,
        classes,
        importance_scores=None,
    ):
        if (not files and not classes) or importance_scores is None:
            context = self.repository_agent.get_repository_context(issue_text) or {}
            files = context.get("files", [])
            classes = context.get("classes", [])
            importance_scores = list(context.get("importance", {}).values())

        score = self.confidence.calculate(
            files,
            classes,
            importance_scores,
        )

        if score >= 80:
            return (
                "likely_valid",
                score,
            )

        if score >= 50:
            return (
                "possible_issue",
                score,
            )

        return (
            "weak_evidence",
            score,
        )
