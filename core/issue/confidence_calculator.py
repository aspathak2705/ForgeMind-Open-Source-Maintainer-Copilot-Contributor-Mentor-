class ConfidenceCalculator:

    def calculate(
        self,
        files: list[str],
        classes: list[str],
        importance_scores: list[int],
    ):
        if not files and not classes:
            return 15

        score = 0

        score += len(files) * 25
        score += len(classes) * 25
        score += sum(importance_scores) // max(len(importance_scores), 1)

        return min(score, 100)
