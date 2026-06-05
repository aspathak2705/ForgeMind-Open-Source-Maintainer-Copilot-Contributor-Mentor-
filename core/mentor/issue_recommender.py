from agents.repository_agent.repository_agent import (
    RepositoryAgent,
)

from core.mentor.difficulty_estimator import (
    DifficultyEstimator,
)

from core.mentor.onboarding_analyzer import (
    OnboardingAnalyzer,
)


class IssueRecommender:

    def __init__(self):

        self.repo_agent = (
            RepositoryAgent()
        )

        self.difficulty = (
            DifficultyEstimator()
        )

        self.onboarding = (
            OnboardingAnalyzer()
        )

    def recommend(
        self,
        limit: int = 5,
    ):

        candidate_files = (
            self.onboarding
            .find_candidate_files()
        )

        recommendations = []

        for file_path in candidate_files:

            importance = (
                self.repo_agent
                .get_file_importance(
                    file_path
                )
            )

            impact = (
                self.repo_agent
                .get_file_impact(
                    file_path
                )
            )

            difficulty = (
                self.difficulty
                .estimate(
                    importance,
                    impact[
                        "impact_score"
                    ],
                )
            )

            recommendations.append(
                {
                    "file": file_path,
                    "difficulty": difficulty,
                    "importance": importance,
                    "impact_score": impact[
                        "impact_score"
                    ],
                }
            )

        recommendations.sort(
            key=lambda x: (
                x["importance"],
                x["impact_score"],
            )
        )

        return recommendations[:limit]