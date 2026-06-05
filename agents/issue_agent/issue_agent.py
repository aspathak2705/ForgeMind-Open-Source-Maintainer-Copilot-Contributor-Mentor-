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
from core.issue.repository_importance import RepositoryImportance

from core.issue.severity_calculator import (
    SeverityCalculator,
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

        self.importance = RepositoryImportance()

        self.severity_calculator = (
            SeverityCalculator()
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

        importance_scores = [
            self.importance.calculate(
                file_name
            )
            for file_name in context["files"]
        ]

        verification, confidence = (
            self.verifier.verify(
                issue_text,
                context["files"],
                context["classes"],
                importance_scores,
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

        avg_importance = (
            sum(importance_scores)
            // max(
                len(importance_scores),
                1
            )
        )

        severity = (
            self.severity_calculator.calculate(
                issue_type,
                avg_importance,
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
