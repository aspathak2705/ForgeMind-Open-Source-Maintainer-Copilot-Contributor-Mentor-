from core.services.repository_service import (
    RepositoryService,
)

from core.graph.graph_builder import (
    GraphBuilder,
)


class RepositoryImportance:

    def __init__(self):

        self.repo = RepositoryService()

    def calculate(
        self,
        target_file: str,
    ) -> int:

        rows = self.repo.get_all_files()

        graph = GraphBuilder.build(rows)

        incoming = 0
        outgoing = 0

        for source, deps in graph.items():

            if target_file in deps:
                incoming += 1

            if source == target_file:
                outgoing = len(deps)

        score = (
            incoming * 2
            + outgoing
        ) * 10

        return min(score, 100)