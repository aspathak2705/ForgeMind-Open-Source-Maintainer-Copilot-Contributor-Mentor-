from core.services.explain_service import ExplainService


def explain(query: str):

    service = ExplainService()

    result = service.explain(query)

    if not result:
        print("No matches found")
        return

    print()

    print(f"Repository Explanation: {query}")

    print()

    if result["files"]:

        print("Files:")

        for file in sorted(result["files"]):

            print(f"- {file}")

        print()

    if result["classes"]:

        print("Classes:")

        for cls in sorted(result["classes"]):

            print(f"- {cls}")

        print()

    if result["functions"]:

        print("Functions:")

        for func in sorted(result["functions"]):

            print(f"- {func}")

        print()

    if result["imports"]:

        print("Imports:")

        for imp in sorted(result["imports"]):

            print(f"- {imp}")

        print()
