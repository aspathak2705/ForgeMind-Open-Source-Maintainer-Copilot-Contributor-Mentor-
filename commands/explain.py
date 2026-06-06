from agents.repository_agent.repository_agent import (
    RepositoryAgent,
)
from pathlib import Path


def explain(query: str):

    agent = RepositoryAgent()

    context = (
        agent.get_enriched_context(
            query
        )
    )

    if not context:

        print(
            f"\nNo repository context found for '{query}'."
        )

        return

    print("\n" + "=" * 50)
    print(
        f"Repository Explanation: {query}"
    )
    print("=" * 50)

    print()

    # Files Section
    files = context.get(
        "files",
        []
    )

    if files:

        print("Files")
        print("-" * 20)

        for file_info in files:

            print(
                Path(
                    file_info["file"]
                ).name
            )

            print(
                f"Importance: "
                f"{file_info['importance']}"
            )

            print(
                f"Difficulty: "
                f"{file_info['difficulty']}"
            )

            print(
                f"Impact Score: "
                f"{file_info['impact_score']}"
            )

            dependents = (
                file_info.get(
                    "dependents",
                    []
                )
            )

            if dependents:

                print(
                    "Dependents:"
                )

                for dep in dependents:

                    print(
                        f"  - {dep}"
                    )

            print()

    # Classes Section
    classes = context.get(
        "classes",
        []
    )

    functions = context.get(
        "functions",
        []
    )

    if classes:

        print("Classes")
        print("-" * 20)

        for class_name in classes:

            print(
                f"- {class_name}"
            )

        print()

    if functions:

        print("Functions")
        print("-" * 20)

        for function_name in functions:

            print(
                f"- {function_name}"
            )

        print()

    # Imports Section
    imports = context.get(
        "imports",
        []
    )

    if imports:

        print("Imports")
        print("-" * 20)

        for imp in imports:

            print(
                f"- {imp}"
            )

        print()

    print("=" * 50)