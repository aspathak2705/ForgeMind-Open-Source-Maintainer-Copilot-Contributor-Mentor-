class RecommendationEngine:

    def generate(
        self,
        severity: str,
        files: list[str],
    ):

        if files:

            return (
                f"Investigate {files[0]}"
            )

        return (
            "Gather more information"
        )