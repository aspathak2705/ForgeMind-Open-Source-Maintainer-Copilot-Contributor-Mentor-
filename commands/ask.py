from core.services.query_service import (
    QueryService,
)


def ask(query: str):

    service = QueryService()

    results = service.find_symbol(
        query
    )

    if not results:

        print("No matches found.")
        return

    print()

    print(
        f"Results for '{query}'"
    )

    print()

    for result in results[:10]:

        print(
            f"[{result.match_type}] "
            f"{result.matched_value}"
        )

        print(
            f"  File: "
            f"{result.file_path}"
        )

        print()