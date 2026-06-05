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

from core.issue.reproduction_generator import (
    ReproductionGenerator,
)

from core.issue.recommendation_engine import (
    RecommendationEngine,
)

from core.issue.plausibility_engine import (
    PlausibilityEngine,
)

from core.issue.confidence_calculator import (
    ConfidenceCalculator,
)

from core.issue.severity_calculator import (
    SeverityCalculator,
)

from agents.repository_agent.repository_agent import (
    RepositoryAgent,
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

        self.reproducer = (
            ReproductionGenerator()
        )

        self.recommender = (
            RecommendationEngine()
        )

        self.plausibility = (
            PlausibilityEngine()
        )

        self.confidence_calculator = (
            ConfidenceCalculator()
        )

        self.severity_calculator = (
            SeverityCalculator()
        )

        self.repository_agent = (
            RepositoryAgent()
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

        context = (
            self.analyzer.analyze(
                issue_text
            )
        )

        importance_scores = []

        for file_path in context["files"]:

            importance = (
                self.repository_agent
                .get_file_importance(
                    file_path
                )
            )

            importance_scores.append(
                importance
            )

        plausibility_score = (
            self.plausibility.score(
                context["files"],
                context["classes"],
            )
        )

        verification, confidence = (
            self.verifier.verify(
                context["files"],
                context["classes"],
                importance_scores,
                plausibility_score,
            )
        )

        avg_importance = 0

        if importance_scores:

            avg_importance = (
                sum(
                    importance_scores
                )
                // len(
                    importance_scores
                )
            )

        severity = (
            self.severity_calculator
            .calculate(
                issue_type,
                avg_importance,
            )
        )

        reproduction_steps = (
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
            related_classes=context[
                "classes"
            ],
            reproduction_steps=reproduction_steps,
            recommendation=recommendation,
        )