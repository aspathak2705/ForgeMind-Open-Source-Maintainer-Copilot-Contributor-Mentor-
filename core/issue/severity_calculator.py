class SeverityCalculator:

    def calculate(
        self,
        issue_type: str,
        average_importance: int,
    ):
        issue_type = issue_type.lower()

        if issue_type == "bug":
            if average_importance >= 60:
                return "high"
            return "medium"

        if issue_type == "feature":
            if average_importance >= 50:
                return "medium"
            return "low"

        if issue_type == "question":
            if average_importance >= 30:
                return "medium"
            return "low"

        if average_importance >= 70:
            return "high"

        return "medium"
