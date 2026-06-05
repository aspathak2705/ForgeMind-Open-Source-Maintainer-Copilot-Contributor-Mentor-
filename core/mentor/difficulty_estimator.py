class DifficultyEstimator:

    def estimate(
        self,
        importance,
        impact_score,
    ):

        score = (
            importance
            +
            impact_score * 5
        )

        if score < 30:
            return "beginner"

        if score < 70:
            return "intermediate"

        return "advanced"