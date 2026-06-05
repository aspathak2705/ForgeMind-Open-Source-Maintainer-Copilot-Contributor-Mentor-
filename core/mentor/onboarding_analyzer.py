from core.services.repository_service import (
    RepositoryService,
)

from core.repository.repository_ranker import (
    RepositoryRanker,
)

from core.repository.impact_analyzer import (
    ImpactAnalyzer,
)


class OnboardingAnalyzer:

    def __init__(self):

        self.repo = RepositoryService()

        self.ranker = (
            RepositoryRanker()
        )

        self.impact = (
            ImpactAnalyzer()
        )

    def find_candidate_files(self):

        rows = self.repo.get_all_files()

        candidates = []

        for row in rows:

            file_path = row[1]

            ranking = (
                self.ranker.rank_file(
                    file_path
                )
            )

            impact = (
                self.impact.analyze(
                    file_path
                )
            )

            candidates.append(
                {
                    "file": file_path,
                    "importance": ranking[
                        "importance"
                    ],
                    "difficulty": ranking[
                        "difficulty"
                    ],
                    "impact_score": impact[
                        "impact_score"
                    ],
                }
            )

        candidates.sort(
            key=lambda x: (
                x["importance"],
                x["impact_score"],
            )
        )

        return [
            item["file"]
            for item in candidates
        ]