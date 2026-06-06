import json
from pathlib import Path

from core.graph.dependency_graph import (
    DependencyGraph,
)


class GraphBuilder:

    @staticmethod
    def build(rows):

        graph = DependencyGraph()

        repository_files = {}

        for row in rows:

            file_path = row[1]

            stem = Path(
                file_path
            ).stem

            repository_files[
                stem
            ] = file_path

        for row in rows:

            file_path = row[1]

            imports = json.loads(
                row[2]
            )

            for imp in imports:

                # Handle:
                # core.issue.issue_classifier
                module_name = (
                    imp.split(".")[-1]
                )

                if (
                    module_name
                    in repository_files
                ):

                    graph.add_dependency(
                        file_path,
                        repository_files[
                            module_name
                        ],
                    )

        return graph