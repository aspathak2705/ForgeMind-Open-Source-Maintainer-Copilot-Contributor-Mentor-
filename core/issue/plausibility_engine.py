class PlausibilityEngine:

    def score(
        self,
        files,
        classes,
    ):

        score = 0

        score += len(files) * 20
        score += len(classes) * 20

        return min(
            score,
            100,
        )