from core.search.repository_search import (
    RepositorySearch,
)


class QueryService:

    def __init__(self):

        self.search_engine = (
            RepositorySearch()
        )

    def find_symbol(
        self,
        query: str,
    ):

        return self.search_engine.search(
            query
        )