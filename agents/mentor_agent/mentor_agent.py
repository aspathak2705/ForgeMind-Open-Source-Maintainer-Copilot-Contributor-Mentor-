from agents.repository_agent.repository_agent import (
    RepositoryAgent,
)

from core.mentor.difficulty_estimator import (
    DifficultyEstimator,
)

from core.mentor.onboarding_analyzer import (
    OnboardingAnalyzer,
)

from core.mentor.learning_path_generator import (
    LearningPathGenerator,
)


class MentorAgent:

    def __init__(self):

        self.repository_agent = (
            RepositoryAgent()
        )

        self.difficulty_estimator = (
            DifficultyEstimator()
        )

        self.onboarding_analyzer = (
            OnboardingAnalyzer()
        )

        self.learning_path_generator = (
            LearningPathGenerator()
        )

    def find_beginner_friendly_files(self):

        candidates = (
            self.onboarding_analyzer
            .find_candidate_files()
        )

        recommendations = []

        for file_path in candidates:

            impact_data = (
                self.repository_agent
                .get_file_impact(
                    file_path
                )
            )

            importance = (
                self.repository_agent
                .get_file_importance(
                    file_path
                )
            )

            difficulty = (
                self.difficulty_estimator
                .estimate(
                    importance,
                    impact_data[
                        "impact_score"
                    ],
                )
            )

            recommendations.append(
                {
                    "file": file_path,
                    "importance": importance,
                    "impact_score": impact_data[
                        "impact_score"
                    ],
                    "difficulty": difficulty,
                }
            )

        recommendations.sort(
            key=lambda x: (
                x["importance"],
                x["impact_score"],
            )
        )

        return recommendations

    def recommend_files(
        self,
        limit: int = 5,
    ):

        recommendations = (
            self.find_beginner_friendly_files()
        )

        return recommendations[:limit]

    def generate_learning_path(
        self,
        topic: str,
    ):

        context = (
            self.repository_agent
            .get_enriched_context(
                topic
            )
        )

        if not context:

            return {
                "topic": topic,
                "steps": [],
            }

        return (
            self.learning_path_generator
            .generate(
                topic,
                context,
            )
        )

    def explain_contribution_path(
        self,
        topic: str,
    ):

        learning_path = (
            self.generate_learning_path(
                topic
            )
        )

        recommendations = (
            self.recommend_files()
        )

        return {
            "topic": topic,
            "learning_path": learning_path,
            "recommended_files": recommendations,
        }