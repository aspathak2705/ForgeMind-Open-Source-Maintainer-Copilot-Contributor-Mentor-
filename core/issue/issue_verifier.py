class IssueVerifier:

    def verify(
        self,
        related_files: list[str],
        related_classes: list[str],
    ):

        evidence = (
            len(related_files)
            + len(related_classes)
        )

        if evidence >= 5:
            return (
                "likely_valid",
                90,
            )

        if evidence >= 2:
            return (
                "possible_issue",
                70,
            )

        return (
            "weak_evidence",
            40,
        )