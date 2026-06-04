from collections import defaultdict

class DependencyGraph:

    def __init__(self):
        self.graph = defaultdict(set)

    def add_dependency(
            self,
            source: str,
            target:str
    ):
        self.graph[source].add(target)

    def items(self):
        return self.graph.items()

    def get_dependencies(
            self,
            file_name:str
    ):
        return list(
            self.graph.get(
                file_name,
                []
            )
        )