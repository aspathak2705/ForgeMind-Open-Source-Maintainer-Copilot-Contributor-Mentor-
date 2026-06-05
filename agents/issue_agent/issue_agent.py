from core.issue.issue_model import (
    IssueAnalysis,
)

from core.issue.issue_classifier import (
    IssueClassifier,
)

from core.issue.issue_analyzer import (
    IssueAnalyzer,
)

from core.issue.issue_verifier import (
    IssueVerifier,
)

from core.issue.severity_estimator import (
    SeverityEstimator,
)

from core.issue.reproduction_generator import (
    ReproductionGenerator,
)

from core.issue.recommendation_engine import (
    RecommendationEngine,
)


class IssueAgent:

    def __init__(self):

        self.classifier = (
            IssueClassifier()
        )

        self.analyzer = (
            IssueAnalyzer()
        )

        self.verifier = (
            IssueVerifier()
        )

        self.severity = (
            SeverityEstimator()
        )

        self.reproducer = (
            ReproductionGenerator()
        )

        self.recommender = (
            RecommendationEngine()
        )

    def analyze(
        self,
        issue_text: str,
    ):

        issue_type = (
            self.classifier.classify(
                issue_text
            )
        )

        severity = (
            self.severity.estimate(
                issue_text
            )
        )

        context = (
            self.analyzer.analyze(
                issue_text
            )
        )

        verification, confidence = (
            self.verifier.verify(
                context["files"],
                context["classes"],
            )
        )

        reproduction = (
            self.reproducer.generate(
                issue_text
            )
        )

        recommendation = (
            self.recommender.generate(
                severity,
                context["files"],
            )
        )

        return IssueAnalysis(
            issue_type=issue_type,
            severity=severity,
            verification=verification,
            confidence=confidence,
            related_files=context["files"],
            related_classes=context["classes"],
            reproduction_steps=reproduction,
            recommendation=recommendation,
        )