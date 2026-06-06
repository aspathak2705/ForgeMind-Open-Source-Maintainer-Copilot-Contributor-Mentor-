from core.services.repository_service import (
    RepositoryService,
)

from core.graph.graph_builder import (
    GraphBuilder,
)


class ImpactAnalyzer:

    def __init__(self):

        self.repo = (
            RepositoryService()
        )

    def analyze(
        self,
        target_file: str,
    ):

        rows = (
            self.repo.get_all_files()
        )

        graph = (
            GraphBuilder.build(
                rows
            )
        )

        dependents = []

        for (
            source,
            dependencies,
        ) in graph.items():

            if (
                target_file
                in dependencies
            ):

                dependents.append(
                    source
                )

        return {
            "file": target_file,
            "dependents": dependents,
            "impact_score": len(
                dependents
            ),
        }

    def analyze_all(self):

        rows = (
            self.repo.get_all_files()
        )

        results = {}

        for row in rows:

            file_path = row[1]

            results[
                file_path
            ] = self.analyze(
                file_path
            )

        return results