class ReproductionGenerator:

    def generate(
        self,
        issue_text: str,
    ):

        text = issue_text.lower()

        if "login" in text:

            return [
                "Open login page",
                "Enter credentials",
                "Submit request",
                "Observe behavior",
            ]

        if "upload" in text:

            return [
                "Open upload page",
                "Select file",
                "Upload file",
                "Observe behavior",
            ]

        return [
            "Perform action",
            "Observe behavior",
        ]