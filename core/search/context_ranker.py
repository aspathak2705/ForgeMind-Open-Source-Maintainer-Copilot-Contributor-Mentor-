class ContextRanker:

    def rank_files(
        self,
        files: list[dict],
    ):

        ranked = sorted(
            files,
            key=lambda file: (
                file.get(
                    "importance",
                    0,
                )
                +
                (
                    file.get(
                        "impact_score",
                        0,
                    )
                    * 20
                )
            ),
            reverse=True,
        )

        return ranked