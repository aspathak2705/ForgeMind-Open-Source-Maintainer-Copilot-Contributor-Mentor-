from core.services.repository_service import RepositoryService
from core.graph.graph_builder import GraphBuilder

def graph():

    service = RepositoryService()

    rows = service.get_all_files()

    dependency_graph = GraphBuilder.build(rows)

    print("\nDependency Graph\n")

    for file, deps in dependency_graph.items():
        print(file)

        for dep in deps:
            print(f"  -> {dep}")

        print()