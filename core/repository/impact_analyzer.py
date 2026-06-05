from core.services.repository_service import (
    RepositoryService,
)

from core.graph.graph_builder import (
    GraphBuilder,
)


class ImpactAnalyzer:

    def __init__(self):

        self.repo = RepositoryService()

    def analyze(
        self,
        target_file: str,
    ):

        rows = self.repo.get_all_files()

        graph = GraphBuilder.build(rows)

        dependents = []

        for source, deps in graph.items():

            if target_file in deps:

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