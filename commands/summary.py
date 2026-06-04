from core.services.repository_service import RepositoryService


def summary():

    service = RepositoryService()

    data = service.get_summary()

    print("\nRepository Overview\n")

    print(f"Files: {data['files']}")
    print(f"Classes: {data['classes']}")
    print(f"Functions: {data['functions']}")

    print("\nMost Imported Modules:")

    for module, count in data["most_imported"]:
        print(
            f"  {module} ({count})"
        )

