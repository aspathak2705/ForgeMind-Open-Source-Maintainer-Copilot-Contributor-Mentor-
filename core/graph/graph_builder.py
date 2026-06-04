import json

from core.graph.dependency_graph import DependencyGraph


class GraphBuilder:

    @staticmethod

    def build(rows):

        graph = DependencyGraph()

        for row in rows:

            file_path = row[1]

            imports = json.loads(row[2])

            for imp in imports:
                
                graph.add_dependency(
                    file_path,
                    imp
                )
        return graph
    

    