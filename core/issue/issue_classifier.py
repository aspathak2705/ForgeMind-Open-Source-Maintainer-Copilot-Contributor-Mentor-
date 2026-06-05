class IssueClassifier:

    BUG_KEYWORDS = [
        "crash",
        "error",
        "bug",
        "fails",
        "exception",
        "broken",
        "issue",
    ]

    FEATURE_KEYWORDS = [
        "feature",
        "enhancement",
        "add",
        "support",
        "implement",
    ]

    QUESTION_KEYWORDS = [
        "how",
        "why",
        "what",
        "when",
        "?",
    ]

    def classify(self, text: str):

        text = text.lower()

        for keyword in self.BUG_KEYWORDS:
            if keyword in text:
                return "bug"

        for keyword in self.FEATURE_KEYWORDS:
            if keyword in text:
                return "feature"

        for keyword in self.QUESTION_KEYWORDS:
            if keyword in text:
                return "question"

        return "unknown"