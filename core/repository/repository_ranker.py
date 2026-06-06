import json

from core.services.repository_service import (
    RepositoryService,
)

from core.repository.impact_analyzer import (
    ImpactAnalyzer,
)


class RepositoryRanker:

    def __init__(self):

        self.repo = (
            RepositoryService()
        )

        self.impact = (
            ImpactAnalyzer()
        )

    def rank_file(
        self,
        file_path: str,
    ):

        rows = (
            self.repo.get_all_files()
        )

        target_row = None

        for row in rows:

            if row[1] == file_path:

                target_row = row
                break

        if not target_row:

            return {
                "importance": 0,
                "difficulty": 0,
                "impact": {},
            }

        imports = json.loads(
            target_row[2]
        )

        classes = json.loads(
            target_row[3]
        )

        functions = json.loads(
            target_row[4]
        )

        impact = (
            self.impact.analyze(
                file_path
            )
        )

        importance = (
            len(classes) * 15
            + len(functions) * 8
            + len(imports) * 3
            + impact["impact_score"] * 25
        )

        importance = min(
            importance,
            100,
        )

        difficulty = min(
            importance + 10,
            100,
        )

        return {
            "importance": importance,
            "difficulty": difficulty,
            "impact": impact,
        }