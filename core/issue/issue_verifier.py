from core.issue.confidence_calculator import (
    ConfidenceCalculator,
)


class IssueVerifier:

    def __init__(self):

        self.confidence = (
            ConfidenceCalculator()
        )

    def verify(
        self,
        files,
        classes,
        importance_scores,
        plausibility_score,
    ):

        confidence = (
            self.confidence.calculate(
                files,
                classes,
                importance_scores,
            )
        )

        final_score = (
            confidence * 0.7
            +
            plausibility_score * 0.3
        )

        final_score = int(
            min(
                final_score,
                100,
            )
        )

        if final_score >= 80:

            return (
                "likely_valid",
                final_score,
            )

        if final_score >= 50:

            return (
                "possible_issue",
                final_score,
            )

        return (
            "weak_evidence",
            final_score,
        )