import json
from pathlib import Path

from core.issue.issue_analyzer import IssueAnalyzer
from core.issue.issue_classifier import IssueClassifier
from core.issue.issue_model import IssueAnalysis
from core.issue.issue_verifier import IssueVerifier
from core.issue.recommendation_engine import RecommendationEngine
from core.issue.reproduction_generator import ReproductionGenerator
from core.issue.severity_estimator import SeverityEstimator
from core.services.repository_service import RepositoryService


class TriageService:

    def __init__(self):
        self.analyzer = IssueAnalyzer()
        self.classifier = IssueClassifier()
        self.estimator = SeverityEstimator()
        self.verifier = IssueVerifier()
        self.recommender = RecommendationEngine()
        self.reproduction = ReproductionGenerator()
        self.repo = RepositoryService()

    def triage(self, issue_text: str) -> IssueAnalysis:
        related = self.analyzer.analyze(issue_text)

        related_files = sorted(
            {
                Path(file_path).name
                for file_path in related["files"]
            }
        )

        related_classes = set(related["classes"])

        for row in self.repo.get_all_files():
            file_path = row[1]
            class_names = json.loads(row[3])

            if Path(file_path).name in related_files:
                related_classes.update(class_names)

        related_classes = sorted(related_classes)

        verification, confidence = self.verifier.verify(
            related_files,
            related_classes,
        )

        severity = self.estimator.estimate(issue_text)

        return IssueAnalysis(
            issue_type=self.classifier.classify(issue_text),
            severity=severity,
            verification=verification,
            confidence=confidence,
            related_files=related_files,
            related_classes=related_classes,
            reproduction_steps=self.reproduction.generate(issue_text),
            recommendation=self.recommender.generate(
                severity,
                related_files,
            ),
        )
