from core.repository.impact_analyzer import (
    ImpactAnalyzer,
)


class RepositoryRanker:

    def __init__(self):

        self.impact = (
            ImpactAnalyzer()
        )

    def rank_file(
        self,
        file_path: str,
    ):

        result = (
            self.impact.analyze(
                file_path
            )
        )

        importance = min(
            result["impact_score"] * 20,
            100,
        )

        difficulty = min(
            importance + 10,
            100,
        )

        return {
            "importance": importance,
            "difficulty": difficulty,
            "impact": result,
        }