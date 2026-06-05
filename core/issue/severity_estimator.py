class SeverityEstimator:

    CRITICAL = [
        "security",
        "vulnerability",
        "data loss",
    ]

    HIGH = [
        "crash",
        "exception",
        "fails",
        "broken",
    ]

    LOW = [
        "ui",
        "typo",
        "spelling",
    ]

    def estimate(self, text: str):

        text = text.lower()

        for keyword in self.CRITICAL:
            if keyword in text:
                return "critical"

        for keyword in self.HIGH:
            if keyword in text:
                return "high"

        for keyword in self.LOW:
            if keyword in text:
                return "low"

        return "medium"